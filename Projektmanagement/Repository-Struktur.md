# Repository-Struktur

[Startseite](../README.md)

Die Startseite führt zu zwei Hauptbereichen. Technische Inhalte liegen unter
`Fachlich/`, Planung und Sprintberichte unter `Projektmanagement/`.

```text
README.md
Fachlich/
  README.md
  Anwendung/
    app/ frontend/ tests/ scripts/ deploy/
    Dockerfile compose.yaml requirements.txt
  Betrieb/
  Ausgangslage/
  Nachweise/ Medien/
  Anforderungsmatrix.md
  Entscheidungen.md
Projektmanagement/
  README.md
  00_Sprints/
  01_Anhang/ 02_Bilder/
  Antrag/ Nachweise/
  Backlog.md Definition-of-Done.md Risiken.md
  Jira-Abbildung.md
  Projektstand.md
.github/
  workflows/
  CONTRIBUTING.md
```

Jira führt Aufgaben und Status. Git versioniert Code und Dokumentation.
Die CI-Konfiguration bleibt im von GitHub erwarteten Ordner `.github/workflows/`.
Lokale Umgebungen, Secrets und Betriebsdaten werden ignoriert.
