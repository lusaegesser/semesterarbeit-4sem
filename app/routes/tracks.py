import os
from uuid import uuid4
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Track, Share, Comment
from app.auth import require_admin
from app.schemas import TrackCreate, TrackResponse

router = APIRouter(prefix="/tracks", tags=["Tracks"], dependencies=[Depends(require_admin)])

from app.config import UPLOAD_DIR, MAX_UPLOAD_BYTES
ALLOWED_EXTENSIONS = [".mp3", ".wav"]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE TRACK
@router.post("/", response_model=TrackResponse)
def create_track(track: TrackCreate, db: Session = Depends(get_db)):
    new_track = Track(**track.model_dump())

    db.add(new_track)
    db.commit()
    db.refresh(new_track)

    return new_track


# GET ALL TRACKS + FILTER
@router.get("/", response_model=list[TrackResponse])
def get_tracks(
    title: str | None = Query(default=None),
    artist: str | None = Query(default=None),
    genre: str | None = Query(default=None),
    key: str | None = Query(default=None),
    min_bpm: int | None = Query(default=None),
    max_bpm: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Track)

    if title:
        query = query.filter(Track.title.ilike(f"%{title}%"))

    if artist:
        query = query.filter(Track.artist.ilike(f"%{artist}%"))

    if genre:
        query = query.filter(Track.genre.ilike(f"%{genre}%"))

    if key:
        query = query.filter(Track.key.ilike(f"%{key}%"))

    if min_bpm is not None:
        query = query.filter(Track.bpm >= min_bpm)

    if max_bpm is not None:
        query = query.filter(Track.bpm <= max_bpm)

    return query.all()


# GET SINGLE TRACK
@router.get("/{track_id}", response_model=TrackResponse)
def get_track(track_id: int, db: Session = Depends(get_db)):
    track = db.query(Track).filter(Track.id == track_id).first()

    if track is None:
        raise HTTPException(status_code=404, detail="Track nicht gefunden")

    return track


# UPDATE TRACK
@router.put("/{track_id}", response_model=TrackResponse)
def update_track(
    track_id: int, updated_track: TrackCreate, db: Session = Depends(get_db)
):
    track = db.query(Track).filter(Track.id == track_id).first()

    if track is None:
        raise HTTPException(status_code=404, detail="Track nicht gefunden")

    track.title = updated_track.title
    track.artist = updated_track.artist
    track.genre = updated_track.genre
    track.bpm = updated_track.bpm
    track.key = updated_track.key
    track.status = updated_track.status

    db.commit()
    db.refresh(track)

    return track


# DELETE TRACK
@router.delete("/{track_id}")
def delete_track(track_id: int, db: Session = Depends(get_db)):
    track = db.query(Track).filter(Track.id == track_id).first()

    if track is None:
        raise HTTPException(status_code=404, detail="Track nicht gefunden")

    audio_file = track.audio_file
    db.query(Share).filter(Share.track_id == track_id).delete()
    db.query(Comment).filter(Comment.track_id == track_id).delete()
    db.delete(track)
    db.commit()

    if audio_file:
        (UPLOAD_DIR / Path(audio_file).name).unlink(missing_ok=True)
    return {"message": "Track erfolgreich gelöscht"}


# UPLOAD AUDIO FILE
@router.post("/{track_id}/upload", response_model=TrackResponse)
def upload_audio_file(
    track_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    track = db.query(Track).filter(Track.id == track_id).first()

    if track is None:
        raise HTTPException(status_code=404, detail="Track nicht gefunden")

    file_extension = os.path.splitext(file.filename or "")[1].lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400, detail="Nur MP3- und WAV-Dateien sind erlaubt"
        )

    # Never use the client filename as a filesystem path.
    safe_filename = f"{uuid4().hex}{file_extension}"
    file_path = UPLOAD_DIR / safe_filename
    previous = track.audio_file
    try:
        size = 0
        with file_path.open("wb") as buffer:
            while chunk := file.file.read(1024 * 1024):
                size += len(chunk)
                if size > MAX_UPLOAD_BYTES:
                    raise HTTPException(status_code=413, detail="Audiodatei ist zu gross")
                buffer.write(chunk)
        track.audio_file = f"uploads/{safe_filename}"
        db.commit()
    except Exception:
        db.rollback()
        file_path.unlink(missing_ok=True)
        raise
    finally:
        file.file.close()
    if previous:
        (UPLOAD_DIR / Path(previous).name).unlink(missing_ok=True)
    db.refresh(track)
    return track
