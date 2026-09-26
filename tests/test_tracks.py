from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_tracks():
    response = client.get("/tracks/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_track():
    track_data = {
        "title": "Test Track",
        "artist": "Test Artist",
        "genre": "House",
        "bpm": 124,
        "key": "A Minor",
        "status": "Demo",
        "audio_file": None,
    }

    response = client.post("/tracks/", json=track_data)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test Track"
    assert data["artist"] == "Test Artist"
    assert data["genre"] == "House"
    assert data["bpm"] == 124
    assert data["key"] == "A Minor"
    assert data["status"] == "Demo"
    assert "id" in data


def test_update_track():
    track_data = {
        "title": "Track Before Update",
        "artist": "Test Artist",
        "genre": "Techno",
        "bpm": 130,
        "key": "C Minor",
        "status": "Draft",
        "audio_file": None,
    }

    create_response = client.post("/tracks/", json=track_data)
    track_id = create_response.json()["id"]

    updated_data = {
        "title": "Track After Update",
        "artist": "Updated Artist",
        "genre": "House",
        "bpm": 126,
        "key": "G Minor",
        "status": "Final",
        "audio_file": None,
    }

    response = client.put(f"/tracks/{track_id}", json=updated_data)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Track After Update"
    assert data["artist"] == "Updated Artist"
    assert data["genre"] == "House"
    assert data["bpm"] == 126
    assert data["key"] == "G Minor"
    assert data["status"] == "Final"


def test_delete_track():
    track_data = {
        "title": "Track To Delete",
        "artist": "Delete Artist",
        "genre": "House",
        "bpm": 122,
        "key": "D Minor",
        "status": "Demo",
        "audio_file": None,
    }

    create_response = client.post("/tracks/", json=track_data)
    track_id = create_response.json()["id"]

    delete_response = client.delete(f"/tracks/{track_id}")

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Track erfolgreich gelöscht"

    get_response = client.get(f"/tracks/{track_id}")

    assert get_response.status_code == 404


def test_filter_tracks_by_genre():
    track_data = {
        "title": "Filter Test Track",
        "artist": "Filter Artist",
        "genre": "Trance",
        "bpm": 138,
        "key": "E Minor",
        "status": "Demo",
        "audio_file": None,
    }

    client.post("/tracks/", json=track_data)

    response = client.get("/tracks/?genre=Trance")

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 1
    assert any(track["genre"] == "Trance" for track in data)


def test_invalid_track_id_returns_404():
    response = client.get("/tracks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Track nicht gefunden"
