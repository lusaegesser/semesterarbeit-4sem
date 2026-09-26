from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
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
app.include_router(tracks.router)

@app.get("/health")
def health():
    return {"status": "ok"}

app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")
app.mount("/", StaticFiles(directory=Path(__file__).resolve().parent.parent / "frontend", html=True), name="frontend")
