from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app
from app.config import UPLOAD_DIR
from app.routes import tracks

client = TestClient(app)

def create():
    return client.post("/tracks/", json={"title": "Set", "artist": "DJ", "genre": "House", "bpm": 124, "key": "Am", "status": "Draft"}).json()["id"]

def test_upload_playback_replace_delete():
    track_id = create()
    response = client.post(f"/tracks/{track_id}/upload", files={"file": ("../../set.wav", b"RIFFtest", "audio/wav")})
    assert response.status_code == 200
    url = "/" + response.json()["audio_file"]
    assert ".." not in url
    assert client.get(url).content == b"RIFFtest"
    assert client.get(url, headers={"Range": "bytes=0-3"}).status_code == 206
    replacement = client.post(f"/tracks/{track_id}/upload", files={"file": ("set.mp3", b"ID3test", "audio/mpeg")})
    assert replacement.status_code == 200
    assert client.get(url).status_code == 404
    assert len(list(UPLOAD_DIR.iterdir())) == 1
    client.delete(f"/tracks/{track_id}")
    assert not list(UPLOAD_DIR.iterdir())

def test_reject_extension_and_oversized_upload(monkeypatch):
    track_id = create()
    assert client.post(f"/tracks/{track_id}/upload", files={"file": ("set.html", b"x")}).status_code == 400
    monkeypatch.setattr(tracks, "MAX_UPLOAD_BYTES", 2)
    assert client.post(f"/tracks/{track_id}/upload", files={"file": ("set.mp3", b"123")}).status_code == 413
    assert not list(UPLOAD_DIR.iterdir())
    assert client.get(f"/tracks/{track_id}").json()["audio_file"] is None

def test_client_cannot_set_audio_path():
    payload = {"title": "Set", "artist": "DJ", "genre": "House", "bpm": 124, "key": "Am", "status": "Draft", "audio_file": "../../secret"}
    assert client.post("/tracks/", json=payload).json()["audio_file"] is None

def test_frontend_and_health():
    assert client.get("/health").json() == {"status": "ok"}
    assert "DJ Set Archive" in client.get("/").text
    assert 'const API_URL = "/tracks/"' in client.get("/app.js").text
