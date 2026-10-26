# DJ Set Archive

Lokale Entwicklungsbasis für ein DJ-Set-Archiv. Übernommen aus Semesterarbeit 3
(Commit `6e4aa42`): FastAPI, SQLAlchemy, Track-Verwaltung, Filter, Audio-Uploads,
HTML/JavaScript-Oberfläche und sechs API-Tests. Das ursprüngliche Repository bleibt unverändert.

## Aktueller Betrieb auf diesem Laptop

Die App läuft seit 26.09.2026 mit Docker Compose auf http://127.0.0.1:8000.
Das vorhandene Administrator-Passwort wurde übernommen. Das aktive Daten-Volume
steht in der lokalen `.env`. `data/` ist nur noch die unveränderte Rückfallkopie
aus dem Python-Betrieb. Keine zweite App auf Port 8000 starten.

Sicherung: `./.venv/Scripts/python.exe scripts/manage.py backup`

Wiederherstellung: `./.venv/Scripts/python.exe scripts/manage.py restore backups/DATEINAME.zip`

Details und Rückfallverfahren: [Betriebsanleitung](../../docs/backup-operations.md).

## Alternative: Python-Entwicklungsbetrieb (Windows / PowerShell)

```powershell
cd C:\repos\dj-set-archive
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m app.setup_admin
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --no-access-log
```

Browser: http://127.0.0.1:8000

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
docker compose exec app python -m app.setup_admin
docker compose logs -f
docker compose down
```

Die App ist ebenfalls unter http://127.0.0.1:8000 erreichbar. Das Volume
`archive-data` speichert Datenbank und Uploads unabhängig vom Container.
`docker compose down -v` löscht dieses Volume samt Daten; zum normalen Stoppen
deshalb nur `docker compose down` verwenden.

## Konfiguration

Umgebungsvariablen: `DATA_DIR` (Standard `data`), `DATABASE_URL` (Standard SQLite
im Datenverzeichnis), `MAX_UPLOAD_BYTES` (Standard 1 GB = 1.000.000.000 Bytes).

## Anmeldung und Freigaben

`python -m app.setup_admin` fragt ein Passwort verdeckt ab (mindestens 12 Zeichen).
Ein gesalzener PBKDF2-Hash wird unter `data/admin-password.hash` gespeichert und
nicht eingecheckt. Ohne Einrichtung bleibt die Anmeldung gesperrt. Erneutes
Ausführen setzt das Passwort zurück und beendet alle Sitzungen. Alternativ kann
`ADMIN_PASSWORD_HASH` gesetzt werden; diese Variable hat Vorrang vor der Datei.
Sitzungen laufen nach acht Stunden ab. Die Einrichtung ist nur einmal nötig.
Docker hat einen separaten Datenspeicher und benötigt eine eigene Einrichtung.

## Aktueller Umfang

- Administrator: Sets erfassen, suchen, bearbeiten und löschen, MP3/WAV hochladen.
- Browser-Audioplayer mit Zeitmarken-Kommentaren und Sprung zur Abspielposition.
- Privater Zugriff auf Sets und Audio; kein öffentlicher Upload-Ordner.
- Ein widerrufbarer Freigabelink pro Set; neue Links ersetzen die bisherigen.
- Jeder Besitzer des Links kann hören und kommentieren. Anzeigenamen sind nicht
  verifiziert. Administrator kann Kommentare löschen.
- Die kompatible Track-Datenstruktur bleibt erhalten; BPM und Tonart sind optional
  in der Oberfläche. Dateitypen werden bisher nur anhand der Endung geprüft.

## Grenzen der lokalen Entwicklungsfassung

Noch nicht öffentlich deployen: HTTPS-Konfiguration, externe Backup-Kopie, eine verteilte
Begrenzung der Anmeldeversuche und Kommentar-Spamschutz fehlen. Die Login-Begrenzung
gilt pro Prozess: insgesamt zehn Versuche pro Minute. Bei späterem HTTPS-Betrieb
`COOKIE_SECURE=true` setzen.

Links mit `127.0.0.1` funktionieren nur auf diesem Laptop. Für Kollegen brauchen
wir eine erreichbare, abgesicherte Adresse. Widerruf verhindert weitere Abrufe;
bereits heruntergeladene Audiodaten lassen sich damit nicht zurückholen.
Freigabetokens werden beim Audioabruf als Query-Parameter übertragen. Uvicorn läuft
daher ohne Zugriffslog; spätere Proxy-Logs müssen Query-Parameter ebenfalls auslassen.

Alle schreibenden API-Anfragen benötigen `X-Archive-Request: 1` als CSRF-Schutz.
Die Oberfläche setzt den Header automatisch. Fremdes CORS wird nicht erlaubt.
Die Content-Security-Policy erlaubt nur lokale Skripte; die externe Swagger-Oberfläche
wird dadurch nicht geladen. Das API-Schema steht unter `/openapi.json` bereit.

## Nächste Etappen

1. Mit echten Sets testen und Oberfläche/Set-Metadaten verfeinern.
2. Hosting, Speicherbedarf, externe Backup-Kopie und Produktionsabsicherung planen.
3. Semesterarbeit 4: Benutzerkonten mit Uploads, Kubernetes/Helm und DevOps.

PostgreSQL, Objektspeicher, Terraform und Argo CD sind noch nicht umgesetzt.

## Herkunft und Unterricht

- https://gitlab.com/lukas03saegesser/semesterarbeit-3sem
- https://ch-tbz-wb.gitlab.io/Stud/devops/0_Organisatorisches/Tagesplanungen/Readme/
- https://helm-basics.training.acend.ch/docs/

## Git Bash unter Windows

In Git Bash werden Schrägstriche verwendet:

```bash
cd /c/repos/dj-set-archive
./.venv/Scripts/python.exe -m app.setup_admin
./.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --no-access-log
```

Das Passwort-Setup nur bei der ersten Einrichtung oder zum Zurücksetzen ausführen.

## Automatischer Containertest

```bash
python scripts/docker_smoke.py
```

Voraussetzung: laufende Docker Engine mit Compose v2. Der Test erstellt ein eigenes,
eindeutig benanntes Compose-Projekt, einen zufälligen lokalen Port und ein separates
Volume. Er prüft Anmeldung, Upload, Gastkommentar, Audio-Teilabruf und den Erhalt von
Sitzung, Set, Audio, Kommentar und Freigabe beim Ersetzen des Containers. Anschliessend
prüft er den Widerruf der Freigabe und die Abmeldung. Nur seine eigenen Testressourcen
werden danach entfernt. Die normale App und deren Daten werden nicht verwendet.

Derselbe Test läuft in GitHub Actions als separater Linux-Container-Job neben pytest.
