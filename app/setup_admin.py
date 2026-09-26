"""Run locally: python -m app.setup_admin. Password input is hidden."""
import getpass
from app.auth import hash_password, AdminSession
from app.config import DATA_DIR
from app.database import Base, engine, SessionLocal

def main():
    password = getpass.getpass("Neues Administrator-Passwort (mindestens 12 Zeichen): ")
    if len(password) < 12:
        raise SystemExit("Bitte mindestens 12 Zeichen verwenden.")
    if password != getpass.getpass("Passwort wiederholen: "):
        raise SystemExit("Passwörter stimmen nicht überein.")
    (DATA_DIR / "admin-password.hash").write_text(hash_password(password))
    Base.metadata.create_all(engine)
    with SessionLocal() as db:
        db.query(AdminSession).delete()
        db.commit()
    print("Passwort eingerichtet. Bestehende Sitzungen wurden beendet.")

if __name__ == "__main__":
    main()
