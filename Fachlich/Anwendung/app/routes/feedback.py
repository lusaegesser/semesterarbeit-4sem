import secrets
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy.orm import Session
from app.auth import require_admin, is_admin, digest
from app.config import UPLOAD_DIR
from app.models import Track, Share, Comment
from app.schemas import TrackResponse
from app.routes.tracks import get_db

router = APIRouter(tags=["Freigaben und Feedback"])

def accessible(track_id, request, db):
    track = db.get(Track, track_id)
    token = request.headers.get("X-Share-Token") or request.query_params.get("share", "")
    share = db.get(Share, digest(token)) if token else None
    if not track or not (is_admin(request) or (share and share.track_id == track_id)):
        raise HTTPException(404, "Set nicht verfügbar oder Freigabe widerrufen")
    return track

class CommentCreate(BaseModel):
    author: str = Field(min_length=1, max_length=80)
    body: str = Field(min_length=1, max_length=2000)
    seconds: int = Field(ge=0, le=7 * 24 * 3600)

    @field_validator("author", "body")
    @classmethod
    def not_blank(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Darf nicht leer sein")
        return value

class CommentResponse(CommentCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

@router.post("/tracks/{track_id}/share", dependencies=[Depends(require_admin)])
def create_share(track_id: int, db: Session = Depends(get_db)):
    if not db.get(Track, track_id):
        raise HTTPException(404, "Set nicht gefunden")
    token = secrets.token_urlsafe(32)
    db.query(Share).filter(Share.track_id == track_id).delete()
    db.add(Share(token_hash=digest(token), track_id=track_id))
    db.commit()
    return {"path": f"/#set={track_id}&share={token}"}

@router.delete("/tracks/{track_id}/share", dependencies=[Depends(require_admin)])
def revoke_share(track_id: int, db: Session = Depends(get_db)):
    db.query(Share).filter(Share.track_id == track_id).delete()
    db.commit()
    return {"revoked": True}

@router.get("/shared/{track_id}", response_model=TrackResponse)
def shared_track(track_id: int, request: Request, db: Session = Depends(get_db)):
    return accessible(track_id, request, db)

@router.get("/tracks/{track_id}/audio")
def audio(track_id: int, request: Request, db: Session = Depends(get_db)):
    track = accessible(track_id, request, db)
    if not track.audio_file:
        raise HTTPException(404, "Noch keine Aufnahme vorhanden")
    path = UPLOAD_DIR / Path(track.audio_file).name
    if not path.is_file():
        raise HTTPException(404, "Aufnahme nicht vorhanden")
    media_type = "audio/mpeg" if path.suffix == ".mp3" else "audio/wav"
    return FileResponse(path, media_type=media_type, headers={"Cache-Control": "no-store"})

@router.get("/tracks/{track_id}/comments", response_model=list[CommentResponse])
def comments(track_id: int, request: Request, db: Session = Depends(get_db)):
    accessible(track_id, request, db)
    return db.query(Comment).filter(Comment.track_id == track_id).order_by(Comment.seconds, Comment.id).all()

@router.post("/tracks/{track_id}/comments", response_model=CommentResponse, status_code=201)
def add_comment(track_id: int, body: CommentCreate, request: Request, db: Session = Depends(get_db)):
    accessible(track_id, request, db)
    comment = Comment(track_id=track_id, **body.model_dump())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

@router.delete("/comments/{comment_id}", dependencies=[Depends(require_admin)])
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.get(Comment, comment_id)
    if not comment:
        raise HTTPException(404, "Kommentar nicht gefunden")
    db.delete(comment)
    db.commit()
    return {"deleted": True}
