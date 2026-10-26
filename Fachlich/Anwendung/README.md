# Anwendung

[Fachlicher Teil](../README.md)

Hier liegt die bestehende SetFlow-Anwendung mit Tests und Containerkonfiguration.
Die ursprüngliche Git-Historie bleibt erhalten.

## Struktur

| Pfad | Inhalt |
| --- | --- |
| `app/` | FastAPI und Datenzugriff |
| `frontend/` | Browseroberfläche |
| `tests/` | Automatisierte Tests |
| `scripts/` | Sicherung, Verwaltung und Container-Smoke-Test |
| `deploy/` | Caddy-Konfiguration |
| `Dockerfile`, `compose.yaml` | Container-Build und Compose-Betrieb |

*Tabelle 01: Anwendungsstruktur.*

## Tests

Vom Repository-Hauptordner:

```powershell
cd Fachlich/Anwendung
python -m pip install -r requirements.txt
python -m pytest -q
```

Die Tests verwenden temporäre Daten und eine eigene SQLite-Datenbank.
Die GitHub-Workflows laufen ebenfalls in diesem Verzeichnis.

## Container

Der Docker-Buildkontext ist dieser Ordner:

```powershell
docker build -t setflow:local .
```

Compose verwendet das Projekt `setflow-semesterarbeit` und standardmässig das
Volume `setflow-semesterarbeit-data`. Die lokale App bindet Port 8000.
Vor einem Start sind Portbelegung und eigene `.env`-Werte zu prüfen.
Die Umstrukturierung migriert keine bestehenden Betriebsdaten.
