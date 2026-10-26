# Projektstand – 26.10.2026

## Erledigt

- Antrag, Ziele, Backlog, DoD und Risiken dokumentiert.
- Drei Sprints vorbereitet; Sprint 1 mit sechs Stories und 18 Tasks.
- Jira-Zuordnung mit drei Epics, zwölf Stories und elf Abhängigkeiten erfasst.
- Dokumentation in Projektmanagement und Fachliches gegliedert.
- App, Tests, Skripte und Containerdateien nach `Fachlich/Anwendung/` verschoben.
- CI-Arbeitsordner und Dependency-Cache an die neue Struktur angepasst.
- Startseite auf Projektbeschreibung und die beiden Hauptbereiche reduziert.

## Offen

- Zeitbudget und verbleibenden Sprintumfang bestätigen; Sprint 1 starten.
- Dozentenzugriffe und Planning-Mitteilung durchführen.
- Offizielle Form- und Bewertungsvorgaben vollständig abgleichen.
- Testabdeckung beurteilen und DevOps-Pipeline weiterentwickeln.
- Cluster, Runner, Deployments, Rollback und Datenerhalt nachweisen.

## Prüfung der Umstrukturierung

Die Anwendungsdateien wurden zunächst unverändert verschoben. Docker-Buildkontext,
Frontend-Pfad, Testimporte und relative Skriptpfade beziehen sich weiterhin auf
denselben gemeinsamen Anwendungsordner. Compose erhält einen eigenen Projektnamen
und ein eigenes Standardvolume.

20 vorhandene Tests bestanden. Docker-Build sowie isolierte Prüfungen von Health,
Oberfläche und Zugriffsschutz erfolgreich. Compose-Konfiguration und lokale
Dokumentlinks geprüft. Der Nachweis liegt unter
`Fachlich/Nachweise/2026-10-26-repository-struktur.md`.
Der bisherige produktive Checkout und seine Daten bleiben unverändert.

## Veröffentlichung

Die Änderung wird in wenigen logischen Commits über den bestehenden Pull Request
integriert. Nach erfolgreichen Prüfungen wird `main` aktualisiert, damit die
normale Repository-Startseite den aktuellen Stand zeigt.
