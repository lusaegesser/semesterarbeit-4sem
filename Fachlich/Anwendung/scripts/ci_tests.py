"""Reproduzierbarer Test-Vorabcheck und optionaler negativer Publish-Nachweis."""

import argparse
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def preflight():
    print(f"Python {sys.version.split()[0]}", flush=True)
    for line in (ROOT / "requirements.txt").read_text().splitlines():
        name, expected = line.split("==", 1)
        try:
            actual = version(name)
        except PackageNotFoundError:
            raise RuntimeError(f"Fehlende Abhängigkeit: {name}") from None
        if actual != expected:
            raise RuntimeError(f"{name}: erwartet {expected}, installiert {actual}")
    subprocess.run([sys.executable, "-m", "pip", "check"], check=True)
    with tempfile.TemporaryDirectory(prefix="setflow-preflight-") as temporary:
        probe = Path(temporary) / "probe.txt"
        probe.write_text("setflow-test", encoding="utf-8")
        if probe.read_text(encoding="utf-8") != "setflow-test":
            raise RuntimeError("Temporärer Schreib-/Lesetest fehlgeschlagen")
    print("PASS: gepinnte Abhängigkeiten und temporärer Schreibpfad", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inject-test-failure", action="store_true")
    args = parser.parse_args()
    preflight()
    command = [sys.executable, "-m", "pytest", "-q", "tests"]
    if not args.inject_test_failure:
        return subprocess.run(command, cwd=ROOT).returncode
    # Nur temporäre synthetische Testdatei; App und versionierte Tests bleiben intakt.
    with tempfile.TemporaryDirectory(prefix="setflow-publish-gate-") as temporary:
        failure = Path(temporary) / "test_publish_gate.py"
        failure.write_text(
            'def test_intentional_publish_failure():\n'
            '    assert False, "P07: kontrollierter Testfehler sperrt Publish"\n',
            encoding="utf-8",
        )
        return subprocess.run(command + [str(failure)], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
