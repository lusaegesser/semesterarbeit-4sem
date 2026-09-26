from fastapi.testclient import TestClient
from app.main import app
from app.auth import COOKIE, AdminSession, digest
from app.database import SessionLocal

def make_set(client):
    return client.post("/tracks/", json={"title": "Evening", "artist": "Lukas", "genre": "House", "bpm": 0, "key": "", "status": ""}).json()["id"]

def test_private_data_and_csrf(client):
    track_id = make_set(client)
    with TestClient(app) as guest:
        assert guest.get("/tracks/").status_code == 401
        assert guest.get(f"/tracks/{track_id}").status_code == 401
        assert guest.get(f"/tracks/{track_id}/audio").status_code == 404
        assert guest.get("/uploads/anything.mp3").status_code == 404
        assert guest.post("/auth/login", json={"password": "test-password-123"}).status_code == 403
        assert guest.post("/tracks/", json={}, headers={"X-Archive-Request": "1"}).status_code == 401

def test_share_comment_audio_and_revoke(client):
    track_id = make_set(client)
    other = make_set(client)
    client.post(f"/tracks/{track_id}/upload", files={"file": ("set.mp3", b"ID3test")})
    path = client.post(f"/tracks/{track_id}/share").json()["path"]
    token = path.split("share=")[1]
    with TestClient(app, headers={"X-Archive-Request": "1", "X-Share-Token": token}) as guest:
        assert guest.get(f"/shared/{track_id}").status_code == 200
        assert guest.get(f"/shared/{other}").status_code == 404
        assert guest.get(f"/tracks/{track_id}/audio").content == b"ID3test"
        assert guest.put(f"/tracks/{track_id}", json={}).status_code == 401
        comment = guest.post(f"/tracks/{track_id}/comments", json={"author": "Friend", "body": "Nice transition", "seconds": 42})
        assert comment.status_code == 201
        assert client.get(f"/tracks/{track_id}/comments").json()[0]["seconds"] == 42
        assert guest.delete(f"/comments/{comment.json()['id']}").status_code == 401
        client.delete(f"/tracks/{track_id}/share")
        assert guest.get(f"/shared/{track_id}").status_code == 404
        assert guest.get(f"/tracks/{track_id}/audio").status_code == 404
        assert guest.post(f"/tracks/{track_id}/comments", json={"author": "X", "body": "X", "seconds": 0}).status_code == 404

def test_rotation_deletion_and_validation(client):
    track_id = make_set(client)
    old = client.post(f"/tracks/{track_id}/share").json()["path"].split("share=")[1]
    client.post(f"/tracks/{track_id}/share")
    with TestClient(app, headers={"X-Share-Token": old}) as guest:
        assert guest.get(f"/shared/{track_id}").status_code == 404
    assert client.post(f"/tracks/{track_id}/comments", json={"author": " ", "body": "x", "seconds": -1}).status_code == 422
    comment = client.post(f"/tracks/{track_id}/comments", json={"author": "Admin", "body": "x", "seconds": 1}).json()
    assert client.delete(f"/comments/{comment['id']}").status_code == 200
    client.delete(f"/tracks/{track_id}")
    assert client.get(f"/tracks/{track_id}/comments").status_code == 404

def test_bad_login_logout_and_expiry(client):
    assert client.post("/auth/login", json={"password": "wrong"}).status_code == 401
    token = client.cookies.get(COOKIE)
    with SessionLocal() as db:
        db.get(AdminSession, digest(token)).expires_at = 0
        db.commit()
    assert client.get("/tracks/").status_code == 401
    assert client.post("/auth/login", json={"password": "test-password-123"}).status_code == 200
    assert client.post("/auth/logout").status_code == 200
    assert client.get("/tracks/").status_code == 401

def test_login_throttling(client):
    for _ in range(9):
        assert client.post("/auth/login", json={"password": "wrong"}).status_code == 401
    assert client.post("/auth/login", json={"password": "wrong"}).status_code == 429
