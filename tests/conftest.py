import os
import tempfile
import pytest

# Configure storage before importing the application. Never touch user data.
_storage = tempfile.TemporaryDirectory(prefix="dj-archive-tests-")
os.environ["DATA_DIR"] = _storage.name
os.environ["DATABASE_URL"] = "sqlite:///" + _storage.name.replace("\\", "/") + "/test.db"

from app.database import Base, engine
from app.config import UPLOAD_DIR

@pytest.fixture(autouse=True)
def clean_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    for path in UPLOAD_DIR.iterdir():
        path.unlink()

def pytest_sessionfinish(session, exitstatus):
    engine.dispose()
    _storage.cleanup()


from fastapi.testclient import TestClient
from app.main import app
from app import auth

_password_hash = auth.hash_password("test-password-123")

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("ADMIN_PASSWORD_HASH", _password_hash)
    auth.attempts.clear()
    with TestClient(app, headers={"X-Archive-Request": "1"}) as client:
        assert client.post("/auth/login", json={"password": "test-password-123"}).status_code == 200
        yield client
