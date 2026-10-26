# SetFlow – Semesterarbeit 4

SetFlow erhält eine DevOps-Pipeline für ein bestehendes DJ-Set-Archiv:
automatisierte Tests, versionierte Container-Images und kontrollierte
Bereitstellung mit Helm in einem lokalen Kubernetes-Cluster.

**Autor:** Lukas Sägesser · **Lehrgang:** ITCNE25, TBZ HF
**Zeitraum:** 26.10.2026–27.01.2027 · **Schwerpunkt:** DevOps
**Projektmanagementdozent:** Corrado Parisi · **Fachdozent:** Armin Dörzbach

## Dokumentation

| Bereich | Einstieg und Inhalt |
| --- | --- |
| **[Projektmanagement](Projektmanagement/README.md)** | Auftrag, Ziele, Stakeholder, Risiken, Planung und Reflexion |
| **[Fachlicher Teil](Fachlich/README.md)** | Ausgangslage, Anforderungen, Architektur, Umsetzung, Tests und Betrieb |
| [Sprints](Projektmanagement/00_Sprints/README.md) | Planning, Review und Retrospektive je Sprint |
| [Projektstand](docs/projektstand.md) | Erledigtes, offene Punkte und nächste Schritte |

Die Gliederung folgt der Semesterarbeit 2 mit klaren Einstiegen und getrennten
Detailnachweisen. Der [Lesepfad und die Repository-Struktur](docs/repository-struktur.md)
erklären die Ablage.

## Aktueller Einstieg

Sprint 1 ist [detailliert vorbereitet](Projektmanagement/00_Sprints/Sprint1/README.md).
Sein Ziel ist eine überprüfbare Testbasis mit einer begründeten Testergänzung.
Sprint 2 und 3 sind grob geplant. Stundenbudget und endgültiges Commitment sind offen;
die Sprints wurden noch nicht gestartet.

- [Jira SEM4 – Board 67](https://lukas-saegesser.atlassian.net/jira/software/projects/SEM4/boards/67/backlog)
- [Product Backlog](Projektmanagement/Backlog.md)
- [Antrag und Annahmestand](Projektmanagement/Antrag/README.md)
- [Anforderungs- und Nachweismatrix](Fachlich/Anforderungsmatrix.md)
- [Entscheidungsprotokoll](docs/entscheidungen.md)

Jira führt Aufgaben und Status. GitHub enthält Code, Pipeline und Dokumentation.
Das Repository bleibt vorerst privat; eine öffentliche Freigabe ist zum Abschluss vorgesehen.

## Code und technische Ablage

Anwendung, Tests und Betriebsdateien liegen an ihren bestehenden Pfaden:

`app/` · `frontend/` · `tests/` · `scripts/` · `.github/workflows/` · `deploy/`

Die [fachliche Dokumentation](Fachlich/README.md#struktur-und-architektur) erläutert
die Komponenten. Versionsstände werden über Git-Commits, Tags und Releases geführt.

## Herkunft und laufender Betrieb

Ausgangsrepository: [DJ-Set-Archiv](https://github.com/lusaegesser/dj-set-archive);
übernommener Ausgangscommit `08e83f3` vom 27.09.2026. Vorleistungen umfassen App,
Tests, bestehenden GitHub-Testworkflow, Docker-Betrieb, Backup/Restore und
HTTPS-Vorbereitung. Details unter [Ausgangslage](Fachlich/Ausgangslage/README.md).

Der produktive Alt-Checkout `C:\repos\dj-set-archive` bleibt getrennt.
In diesem Repository fehlen absichtlich Secrets und Betriebsdaten.
**Compose erst nach Prüfung von Projektname, Ports und Volumenamen starten.**
Die übernommenen Dateien können auf bestehende Ports und Volumes zeigen.

[Betriebsunterlagen und historische Protokolle](docs/README.md) beschreiben den
bisherigen Stand. Neue technische Leistungen werden mit eigenen Nachweisen dokumentiert.

## Zusammenarbeit

Der [Git-Workflow](CONTRIBUTING.md) dokumentiert Branching, Conventional Commits,
Eigenprüfung, Pull Requests und Releases für die Einzelarbeit.

ASUS: technische Umsetzung und Nachweise. Arbeitslaptop: Planung, Dokumentation
und Review. Beide verwenden eigene lokale Klone mit GitHub als gemeinsamer Ablage.

Vor Arbeitsbeginn den Git-Status und den gemeinsamen Stand prüfen; bei sauberem
Arbeitsstand mit `git pull --ff-only` aktualisieren. Pro Aufgabe einen Branch mit
Jira-Bezug verwenden. Änderungen prüfen und vor Gerätewechsel abschliessen.
Gleichzeitige Änderungen derselben Dateien vermeiden.
