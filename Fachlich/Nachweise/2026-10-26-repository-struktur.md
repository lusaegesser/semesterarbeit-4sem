# Prüfung der Repository-Struktur

Datum: 26.10.2026. Aufgabe: SEM4-1.
Geprüfter Stand: Umstrukturierung auf `feature/SEM4-1-projektgrundlagen`.

## Durchführung und Ergebnis

| Prüfung | Soll | Ist |
| --- | --- | --- |
| Bestehende Tests | Alle Tests bestehen aus dem neuen Anwendungsordner | 20 Tests bestanden, 7,49 Sekunden; Windows / Python 3.12 |
| Docker-Build | Anwendung und Abhängigkeiten werden korrekt kopiert | Build aus `Fachlich/Anwendung/` erfolgreich; Python 3.13 |
| Container-Health | `/health` liefert `status: ok` | Erfolgreich |
| Oberfläche | `/` liefert die App-Oberfläche | HTTP 200, erwarteter Seitentitel vorhanden |
| Zugriffsschutz | Anonyme Abfrage der Sets wird abgewiesen | HTTP 401 |
| Compose-Konfiguration | Neuer Buildkontext und getrennte Standardablage | Projekt `setflow-semesterarbeit`, Volume `setflow-semesterarbeit-data` |
| Dokumentation | Lokale Ziele und Sprungmarken erreichbar | 40 Markdown-Dateien, 116 lokale Verweise ohne Fehler |

*Tabelle 01: Strukturprüfung.*

Der Container-Test verwendete ein schreibgeschütztes Dateisystem mit temporärem
`/tmp`, ohne Netzwerk, Portfreigabe oder persistente Volumes. Der produktive Betrieb
und seine Daten wurden nicht verändert.

## Grenzen

Die Prüfung belegt die verschobene Anwendung und ihre bestehenden Funktionen.
GHCR, Kubernetes, Helm-Deployment und die neuen Datenerhaltnachweise sind weiterhin
separate Arbeitspakete. Die GitHub-CI prüft den veröffentlichten Commit zusätzlich.
