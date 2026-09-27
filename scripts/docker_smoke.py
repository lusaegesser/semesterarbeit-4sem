"""End-to-end container check with disposable data. Requires Docker Compose v2."""
import io
import json
import secrets
import subprocess
import tempfile
import time
import uuid
import wave
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, parse_qs
from urllib.request import Request, build_opener, HTTPCookieProcessor


ROOT = Path(__file__).resolve().parents[1]


def main():
    project = "dj-archive-smoke-" + uuid.uuid4().hex[:10]
    with tempfile.TemporaryDirectory(prefix=project) as temporary:
        config = Path(temporary) / "compose.json"
        config.write_text(json.dumps({
            "services": {"app": {
                "build": str(ROOT),
                "ports": ["127.0.0.1::8000"],
                "environment": {"DATA_DIR": "/app/data"},
                "volumes": ["test-data:/app/data"],
            }},
            "volumes": {"test-data": {}},
        }), encoding="utf-8")
        command = ["docker", "compose", "-p", project, "-f", str(config)]

        def compose(*args, input=None, capture=False):
            result = subprocess.run(command + list(args), input=input, text=True,
                                    capture_output=capture, timeout=600)
            if result.returncode:
                if capture:
                    print(result.stdout, result.stderr)
                raise RuntimeError("Docker Compose failed: " + " ".join(args))
            return result.stdout.strip() if capture else None

        client = build_opener(HTTPCookieProcessor(CookieJar()))
        guest = build_opener()
        address = ""

        def request(path, method="GET", body=None, headers=None, anonymous=False, raw=False, expected=200):
            fields = {"X-Archive-Request": "1", **(headers or {})}
            if isinstance(body, dict):
                body = json.dumps(body).encode()
                fields["Content-Type"] = "application/json"
            req = Request(address + path, data=body, method=method, headers=fields)
            try:
                response = (guest if anonymous else client).open(req, timeout=15)
            except HTTPError as error:
                response = error
            with response:
                data = response.read()
                assert response.status == expected, f"{method} {path.split('?')[0]}: expected {expected}, got {response.status}"
                return data if raw else json.loads(data)

        def ready():
            nonlocal address
            address = "http://" + compose("port", "app", "8000", capture=True).splitlines()[0]
            for _ in range(60):
                try:
                    if request("/health") == {"status": "ok"}:
                        return
                except (OSError, URLError):
                    pass
                time.sleep(1)
            raise RuntimeError("Application did not become ready")

        try:
            compose("up", "--build", "-d")
            ready()
            assert request("/auth/status")["configured"] is False
            assert "DJ Set Archive" in request("/", raw=True).decode()
            request("/tracks/", anonymous=True, expected=401)
            password = secrets.token_urlsafe(24)
            # Only test credentials are written to this disposable volume.
            compose("exec", "-T", "app", "python", "-c",
                    "import sys; from app.auth import hash_password; from app.config import DATA_DIR; "
                    "(DATA_DIR / 'admin-password.hash').write_text(hash_password(sys.stdin.read()))",
                    input=password)
            request("/auth/login", "POST", {"password": password})
            track = request("/tracks/", "POST", {
                "title": "Container persistence test", "artist": "Test DJ", "genre": "House",
                "bpm": 124, "key": "", "status": "Draft",
            })
            track_id = track["id"]
            audio = io.BytesIO()
            with wave.open(audio, "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(8000)
                wav.writeframes(b"\x00\x00" * 800)
            boundary = "archive-smoke-" + uuid.uuid4().hex
            multipart = (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="sample.wav"\r\n'
                         'Content-Type: audio/wav\r\n\r\n').encode() + audio.getvalue() + f"\r\n--{boundary}--\r\n".encode()
            request(f"/tracks/{track_id}/upload", "POST", multipart,
                    headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
            shared = request(f"/tracks/{track_id}/share", "POST")
            token = parse_qs(urlsplit(shared["path"]).fragment)["share"][0]
            share_headers = {"X-Share-Token": token}
            request(f"/tracks/{track_id}/comments", "POST", {
                "author": "Listener", "body": "Keep this transition", "seconds": 0,
            }, headers=share_headers, anonymous=True, expected=201)
            print("PASS: container starts, login, upload, guest comment", flush=True)

            compose("up", "-d", "--force-recreate")
            ready()
            assert request("/auth/status")["authenticated"] is True
            assert request(f"/tracks/{track_id}")["title"] == track["title"]
            assert request(f"/tracks/{track_id}/audio", headers=share_headers, anonymous=True, raw=True) == audio.getvalue()
            assert request(f"/tracks/{track_id}/comments", headers=share_headers, anonymous=True)[0]["body"] == "Keep this transition"
            request(f"/tracks/{track_id}/audio", headers={**share_headers, "Range": "bytes=0-3"}, anonymous=True, raw=True, expected=206)
            request(f"/tracks/{track_id}/share", "DELETE")
            request(f"/shared/{track_id}", headers=share_headers, anonymous=True, expected=404)
            request(f"/tracks/{track_id}/audio", headers=share_headers, anonymous=True, expected=404)
            request("/auth/logout", "POST")
            request("/tracks/", expected=401)
            print("PASS: session, set, audio, comments and share survive container replacement; revocation and logout work", flush=True)
            compose("stop", "app")
            compose("run", "--rm", "--no-deps", "app", "python", "scripts/archive_backup.py",
                    "create", "--archive", "/app/data/smoke-backup.zip")
            # Restore into a new directory in a disposable helper container,
            # leaving the original volume unchanged.
            compose("run", "--rm", "--no-deps", "app", "python", "scripts/archive_backup.py",
                    "restore", "--archive", "/app/data/smoke-backup.zip", "--data-dir", "/tmp/restored")
            print("PASS: complete backup verified and restored in a separate directory", flush=True)

        finally:
            # This unique project and volume contain only this script's test data.
            compose("down", "--volumes", "--remove-orphans", "--rmi", "local")


if __name__ == "__main__":
    main()
