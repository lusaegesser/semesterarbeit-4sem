# DJ Set Archive

Lokale Entwicklungsbasis für ein DJ-Set-Archiv. Übernommen aus Semesterarbeit 3
(Commit `6e4aa42`): FastAPI, SQLAlchemy, Track-Verwaltung, Filter, Audio-Uploads,
HTML/JavaScript-Oberfläche und sechs API-Tests. Das ursprüngliche Repository bleibt unverändert.

## Lokal starten (Windows / PowerShell)

```powershell
cd C:\repos\dj-set-archive
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Browser: http://127.0.0.1:8000 — API-Dokumentation: http://127.0.0.1:8000/docs

Frontend und API laufen unter derselben Adresse. Es ist kein separater Webserver nötig.
Datenbank und Audiodateien werden unter `data/` gespeichert und nicht eingecheckt.
Es wurden keine vorhandenen Audiodateien oder Datenbanken übernommen.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Jeder Test erhält eine leere Datenbank. Alle Testdaten liegen in einem temporären
Verzeichnis und werden anschliessend entfernt. GitHub Actions führt dieselben Tests aus.

## Docker (Docker Desktop muss laufen)

```powershell
docker compose up --build -d
docker compose logs -f
docker compose down
```

Die App ist ebenfalls unter http://127.0.0.1:8000 erreichbar. Das Volume
`archive-data` speichert Datenbank und Uploads unabhängig vom Container.
`docker compose down -v` löscht dieses Volume samt Daten; zum normalen Stoppen
deshalb nur `docker compose down` verwenden.

## Konfiguration

Umgebungsvariablen: `DATA_DIR` (Standard `data`), `DATABASE_URL` (Standard SQLite
im Datenverzeichnis), `MAX_UPLOAD_BYTES` (Standard 512 MiB).

## Aktueller Umfang

- Tracks erfassen, suchen, bearbeiten und löschen.
- MP3/WAV hochladen und im Browser abspielen; Dateityp wird bisher nur anhand
  der Endung geprüft. Uploadnamen werden serverseitig generiert.
- Gesundheitsprüfung unter `/health` (Prozessstatus, keine Datenbankprüfung).

**Nur lokale Entwicklung:** Anmeldung, Zugriffsrechte und Freigabelinks fehlen
noch. Deshalb ausschliesslich auf localhost betreiben, nicht öffentlich deployen.
Die bisherige Track-Oberfläche ist noch keine fertige Set-Verwaltung.

## Nächste Etappen

1. Set-Datenmodell und mobile Oberfläche gestalten; Track-Felder wie BPM und
   Tonart auf ihren Nutzen für vollständige Sets prüfen.
2. Administrator-Anmeldung, Freigaben und Zeitmarken-Kommentare umsetzen.
3. Speicherbedarf ermitteln, Hosting und Backups planen.
4. Semesterarbeit 4: Benutzerkonten mit Uploads, Kubernetes/Helm und DevOps.

PostgreSQL, Objektspeicher, Terraform und Argo CD sind noch nicht umgesetzt.
Die konkrete Abgrenzung richtet sich nach der Aufgabenstellung der Semesterarbeit.

## Herkunft und Unterricht

- https://gitlab.com/lukas03saegesser/semesterarbeit-3sem
- https://ch-tbz-wb.gitlab.io/Stud/devops/0_Organisatorisches/Tagesplanungen/Readme/
- https://helm-basics.training.acend.ch/docs/
