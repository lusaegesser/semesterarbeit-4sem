from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app import auth
from app.routes import feedback
from fastapi.staticfiles import StaticFiles
from app.config import UPLOAD_DIR
from app.database import engine, Base
from app.models import Track
from app.routes import tracks

@asynccontextmanager
async def lifespan(app):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="DJ Set Archive – lokale Entwicklungsbasis", lifespan=lifespan)

@app.middleware("http")
async def request_protection(request: Request, call_next):
    if request.method in {"POST", "PUT", "PATCH", "DELETE"} and request.headers.get("X-Archive-Request") != "1":
        return JSONResponse({"detail": "Fehlender Anforderungsschutz"}, status_code=403)
    response = await call_next(request)
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Cache-Control"] = "no-store"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self'; media-src 'self'; frame-ancestors 'none'; base-uri 'none'"
    return response

app.include_router(auth.router)
app.include_router(feedback.router)
app.include_router(tracks.router)

@app.get("/health")
def health():
    return {"status": "ok"}

app.mount("/", StaticFiles(directory=Path(__file__).resolve().parent.parent / "frontend", html=True), name="frontend")
