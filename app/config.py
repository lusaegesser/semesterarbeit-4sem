import os
from pathlib import Path

DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
UPLOAD_DIR = DATA_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{(DATA_DIR / 'archive.db').as_posix()}")
MAX_UPLOAD_BYTES = int(os.getenv("MAX_UPLOAD_BYTES", str(1_000_000_000)))
