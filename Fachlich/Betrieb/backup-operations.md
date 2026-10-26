# Docker-Betrieb, Sicherung und Wiederherstellung

Alle Befehle werden im Projektordner `C:\repos\dj-set-archive` ausgeführt.
Die Beispiele passen zu Git Bash; in PowerShell funktionieren die `/`-Pfade ebenfalls.
Docker Desktop muss laufen. Kein paralleler Python-Server auf Port 8000.

## Normaler Betrieb

```bash
docker compose up -d --build
docker compose ps
docker compose logs --tail 50 app
docker compose stop app
docker compose start app
```

Die Adresse bleibt http://127.0.0.1:8000. Datenbank, Passwort-Hash und Aufnahmen
liegen im Docker-Volume. Die lokale `.env` enthält mit `ARCHIVE_VOLUME` den Namen
des aktiven Volumes; `ARCHIVE_VOLUME_EXTERNAL=true` schützt wiederhergestellte
Volumes zusätzlich vor dem Entfernen durch Compose; sie gehört nicht ins Git-Repository. Nicht manuell auf einen
anderen Volume-Namen wechseln. Ein frisches Volume enthält keine bisherigen Daten.
Die ursprüngliche Python-Ablage `data/` bleibt nach der Migration als Rückfallkopie
erhalten, wird von Docker jedoch nicht weiter aktualisiert.

## Geprüfte Sicherung erstellen

```bash
./.venv/Scripts/python.exe scripts/manage.py backup
```

Das Werkzeug stoppt ausschliesslich den App-Service, sichert dessen Volume und
startet ihn anschliessend wieder, falls er zuvor lief. Andere Docker-Projekte
bleiben unverändert. Während der Sicherung ist die App kurz nicht erreichbar;
bei grossen Audiodateien kann diese Unterbrechung länger dauern.

Unter `backups/` entsteht eine neue ZIP-Datei. Sie enthält:

- SQLite-Datenbank: Sets, Kommentare, Freigaben und Sitzungen.
- Audiodateien aus `uploads/`.
- Den gespeicherten Administrator-Passwort-Hash, falls vorhanden.
- Ein Manifest mit SHA-256-Prüfsummen, Dateigrössen und Datensatzanzahlen.

Die Datenbank wird über die SQLite-Backup-API kopiert. Anschliessend prüft das
Werkzeug die gesamte Sicherung durch separates Entpacken, Prüfsummenvergleich,
Datenbank-Integritätsprüfung und Kontrolle der referenzierten Audiodateien.
Es werden nur die lokal gespeicherten SQLite-Daten unterstützt; ein externer
`DATABASE_URL` benötigt ein eigenes Backup-Verfahren.

**Die ZIP-Dateien sind nicht verschlüsselt.** Sie enthalten private Aufnahmen und
Zugangsdaten in gehashter Form. `backups/` wird weder in Git noch in das Docker-Image
übernommen. Für Schutz vor Laptop-/Datenträgerausfall zusätzlich eine verschlüsselte
Kopie auf einem getrennten Datenträger oder geeigneten Backup-Speicher aufbewahren.
Es ist noch kein automatischer Zeitplan eingerichtet; vor Updates und nach neuen
Uploads manuell sichern. Backups werden nicht automatisch gelöscht.

## Sicherung wiederherstellen

```bash
./.venv/Scripts/python.exe scripts/manage.py restore backups/DATEINAME.zip
```

Der Ablauf ist absichtlich reversibel:

1. Neues, eindeutig benanntes Docker-Volume erstellen.
2. Archiv vollständig prüfen und in dieses leere Volume zurückspielen.
3. Falls die bisherige Docker-App läuft, zusätzlich deren aktuellen Stand sichern.
4. `.env` auf das neue Volume umstellen und den App-Container ersetzen.
5. Erreichbarkeit prüfen; bei einem Startfehler zur vorherigen Konfiguration wechseln.

Das bisherige Volume wird nicht gelöscht. Die Ausgabe nennt das neue Volume.
Freigaben und Sitzungen aus dem Sicherungszeitpunkt werden ebenfalls zurückgespielt:
Ein danach widerrufener Link kann dadurch wieder gültig werden. Bei Wiederherstellung
nach einem Sicherheitsvorfall Passwort neu setzen und Freigaben erneut widerrufen.

Zum bewussten Rückwechsel auf ein vorheriges Volume dessen Namen in `.env` als
`ARCHIVE_VOLUME=...` setzen und `docker compose up -d --force-recreate app` ausführen.
Vorher den aktuellen Stand sichern. Kein `docker compose down -v` und kein
`docker volume prune` zur normalen Wartung verwenden; diese Befehle können Daten löschen.

## Erstmalige Übernahme aus dem Python-Betrieb

Nur bei gestopptem Python-Server:

```bash
./.venv/Scripts/python.exe scripts/archive_backup.py create --data-dir data --archive backups/python-before-docker.zip
./.venv/Scripts/python.exe scripts/archive_backup.py verify --archive backups/python-before-docker.zip
./.venv/Scripts/python.exe scripts/manage.py restore backups/python-before-docker.zip
```

Die Quellablage bleibt unverändert. Passwort-Setup nicht erneut ausführen, da der
bisherige Passwort-Hash mit übernommen wird.

## Tests

```bash
./.venv/Scripts/python.exe -m pytest -q
./.venv/Scripts/python.exe scripts/docker_smoke.py
```

Der Containertest nutzt nur eigene Wegwerfdaten. Er prüft neben Anmeldung und
Medienzugriff auch eine vollständige Sicherung und Wiederherstellung.
