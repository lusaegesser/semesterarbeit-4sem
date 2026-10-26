# SetFlow – Semesterarbeit 4

Aufbau einer DevOps-Pipeline für ein DJ-Set-Archiv.

**Zeitraum:** 26.10.2026–27.01.2027. **Schwerpunkt:** DevOps.
Projektmanagement ist Pflichtbestandteil; Kubernetes/Helm dienen als Zielumgebung.
Die Annahme des Antrags wurde von Lukas bestätigt. Die finale angenommene Datei
muss noch unter `Projektmanagement/Antrag/` abgelegt werden; sie hat Vorrang vor Planungsentwürfen.

## Einstieg

- [Fachliche Dokumentation](Fachlich/Dokumentation.md)
- [Projektmanagement](Projektmanagement/Dokumentation.md)
- [Aktueller Projektstand](docs/projektstand.md)
- [Entscheidungen](docs/entscheidungen.md)
- [Regeln für Codex](AGENTS.md)

App-Code, Tests und Deployment-Dateien bleiben an ihren bisherigen Pfaden.
Die gemeinsame Semesterarbeitsdokumentation liegt unter Fachlich/ und Projektmanagement/.
Jira verwaltet Aufgaben; GitHub verwaltet Code, Pipeline und Dokumentation.

## Zwei Arbeitsplätze

ASUS: technische Umsetzung und fachliche Nachweise. Arbeitslaptop: Planung,
Dokumentation, Reviews und Präsentation. Beide verwenden eigene lokale Klone
desselben privaten GitHub-Repositorys. Keine synchronisierte Netzwerkablage.

Vor Beginn `git pull --ff-only`, dann pro Aufgabe einen Branch verwenden.
Änderungen prüfen, committen und pushen; vor Gerätewechsel abschliessen.
Nicht gleichzeitig dieselben Dateien auf beiden Geräten ändern.
Jira-Ticketkennung in Branch, Commit oder Pull Request aufnehmen.

## Herkunft und Betrieb

Ausgangsrepository: https://github.com/lusaegesser/dj-set-archive
Übernommene Git-Historie: Ausgangscommit `08e83f3` vom 27.09.2026.
Zusätzlich übernommen: lokale HTTPS-Vorbereitung (Compose, Caddy und Betriebsanleitung).
Die frühere README steht unter `Fachlich/Ausgangslage/README-Vorprojekt.md`.

Der bisherige produktive Betrieb unter `C:\repos\dj-set-archive` bleibt getrennt.
In diesem neuen Repository fehlen absichtlich `.env`, Datenbank, Audiodateien,
Backups, Passwort-Hashes und Caddy-Zertifikate. **Hier nicht ungeprüft Compose starten:**
Die übernommene Konfiguration kann andernfalls auf bestehende Volumenamen und Ports zeigen.

Vorleistungen umfassen App, Tests, bereits vorhandenen GitHub-Testworkflow,
Docker-Betrieb, Backup/Restore und HTTPS. Neue Semesterarbeitsleistungen werden
ab dem Projektstart getrennt dokumentiert. Kubernetes, Helm-Deployment,
Registry-Veröffentlichung und lokaler Deployment-Runner sind noch zu prüfen/umzusetzen.
