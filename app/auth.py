import hashlib
import hmac
import os
import secrets
import time
from collections import deque
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Float
from app.database import Base, SessionLocal
from app.config import DATA_DIR

COOKIE = "archive_session"
router = APIRouter(prefix="/auth", tags=["Anmeldung"])
attempts = deque(maxlen=100)

class AdminSession(Base):
    __tablename__ = "admin_sessions"
    token_hash = Column(String(64), primary_key=True)
    expires_at = Column(Float, nullable=False)

def digest(token):
    return hashlib.sha256(token.encode()).hexdigest()

def hash_password(password):
    salt = secrets.token_hex(16)
    result = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 600000)
    return f"{salt}:{result.hex()}"

def configured_hash():
    if os.getenv("ADMIN_PASSWORD_HASH"):
        return os.environ["ADMIN_PASSWORD_HASH"]
    path = DATA_DIR / "admin-password.hash"
    return path.read_text().strip() if path.exists() else None

def verify(password, encoded):
    try:
        salt, expected = encoded.split(":")
        actual = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 600000).hex()
        return hmac.compare_digest(actual, expected)
    except (ValueError, AttributeError):
        return False

def is_admin(request):
    token = request.cookies.get(COOKIE, "")
    if not token:
        return False
    with SessionLocal() as db:
        session = db.get(AdminSession, digest(token))
        return bool(session and session.expires_at > time.time())

def require_admin(request: Request):
    if not is_admin(request):
        raise HTTPException(401, "Bitte als Administrator anmelden")

class Login(BaseModel):
    password: str = Field(min_length=1, max_length=1024)

@router.get("/status")
def status(request: Request):
    return {"authenticated": is_admin(request), "configured": bool(configured_hash())}

@router.post("/login")
def login(body: Login, response: Response):
    stored = configured_hash()
    if not stored:
        raise HTTPException(503, "Administrator-Passwort zuerst lokal einrichten")
    now = time.time()
    while attempts and attempts[0] < now - 60:
        attempts.popleft()
    if len(attempts) >= 10:
        raise HTTPException(429, "Zu viele Anmeldeversuche. In einer Minute erneut versuchen.")
    attempts.append(now)
    if not verify(body.password, stored):
        raise HTTPException(401, "Passwort ist nicht korrekt")
    token = secrets.token_urlsafe(32)
    with SessionLocal() as db:
        db.query(AdminSession).filter(AdminSession.expires_at <= now).delete()
        db.add(AdminSession(token_hash=digest(token), expires_at=now + 8 * 3600))
        db.commit()
    response.set_cookie(COOKIE, token, max_age=8 * 3600, httponly=True,
                        samesite="strict", secure=os.getenv("COOKIE_SECURE", "false").lower() == "true")
    return {"authenticated": True}

@router.post("/logout")
def logout(request: Request, response: Response):
    with SessionLocal() as db:
        db.query(AdminSession).filter(AdminSession.token_hash == digest(request.cookies.get(COOKIE, ""))).delete()
        db.commit()
    response.delete_cookie(COOKIE)
    return {"authenticated": False}
