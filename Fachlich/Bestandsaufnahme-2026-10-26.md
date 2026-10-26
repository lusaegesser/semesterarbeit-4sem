# Fachliche Bestandsaufnahme vom 26.10.2026

## Ausgangsbasis

Die Anwendung stammt aus dem DJ-Set-Archiv-Vorprojekt. Ausgangscommit:
`08e83f3`. Die technische Ablage liegt nach der Umstrukturierung unter
`Fachlich/Anwendung/`.

| Bereich | Vorhandener Stand |
| --- | --- |
| App | FastAPI, SQLite, Uploads, Anmeldung, Freigabelinks und Kommentare |
| Tests | API-, Storage-, Zugriffs- und Backup-Tests mit temporären Daten |
| CI | pytest-Job und isolierter Container-Smoke-Test |
| Betrieb | Docker Compose, Caddy-Konfiguration und Backup-/Restore-Werkzeuge |

*Tabelle 01: Vorleistungen.*

## Neue Semesterarbeitsleistung

Ausstehend sind die gezielte Testergänzung, GHCR-Veröffentlichung,
Kubernetes-/Helm-Zielumgebung, geschützter Runner sowie die neuen
Deployment-, Rollback- und Datenerhaltnachweise.

Die Anforderungsmatrix ordnet diese Leistungen den Antragszielen zu.
Die Tests der Umstrukturierung werden gesondert protokolliert.
