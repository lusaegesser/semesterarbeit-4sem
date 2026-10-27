# Sprint 1

[Jira-Board](https://lukas-saegesser.atlassian.net/jira/software/projects/SEM4/boards/67/backlog) · [Projektmanagement](../../README.md)

## Inhaltsverzeichnis

- [Sprint Planning](#sprint-planning)
- [Epics, User Stories und Tasks](#epics-user-stories-und-tasks)
- [Bewertung mit MoSCoW](#bewertung-mit-moscow)
- [Erwartetes Commitment und Definition of Done](#erwartetes-commitment-und-definition-of-done)
- [Sprint Review](#sprint-review)
- [Sprint Retrospektive](#sprint-retrospektive)

## Sprint Planning

**Thema:** Automatisierte Tests und überprüfbare CI für SetFlow.\
**Sprint-Dauer:** 26.10.2026 bis 15.11.2026.\
**Planungsstand:** 27.10.2026; Sprint läuft.\
**Verantwortlich:** Lukas Sägesser.\
**Projektmanagementdozent:** Corrado Parisi. **Fachdozent:** Armin Dörzbach.

Anwendung, vorhandene Tests und bisheriger Testworkflow sind Vorleistungen.
Repository-Einrichtung, Jira-Board, Backlog, Zielzuordnung und Dozentenzugriffe
gehören zur Vorarbeit (Sprint 0), ohne eigene Sprint-Dokumentation.
Registry und Kubernetes-Deployment folgen in Sprint 2/3.

### Sprint Goal

**Bestehende Tests und CI sind isoliert geprüft und mindestens eine begründete
Testlücke ist geschlossen, sodass Regressionen an SetFlow früh erkannt werden.**

### Schätzung und Priorität

Der Sprint umfasst **12 Story Points**. Story Points vergleichen Komplexität und
Unsicherheit; MoSCoW bestimmt die Priorität. Das verfügbare Zeitbudget ist offen.

### Planungsänderung vom 27.10.2026

P01, P02 und P05 werden nach Sprintstart der Vorarbeit zugeordnet und aus dem
laufenden Sprint entfernt. Sprintziel und Priorisierung werden entsprechend
angepasst. Start- und Enddatum bleiben unverändert.

## Epics, User Stories und Tasks

Tabelle 01: Epics und Sprintumfang.

| Epic | Jira | Umfang in Sprint 1 |
| --- | --- | --- |
| B – Automatisierte Tests und versionierte Images | SEM4-4 | P03, P04 |
| A – Projektgrundlagen und Sprintsteuerung | SEM4-3 | P06: begleitendes Review und Retrospektive |

### Epic B – Automatisierte Tests und versionierte Images

#### User Story P03 – Vorhandene Tests und CI isoliert prüfen

**Jira:** [SEM4-6](https://lukas-saegesser.atlassian.net/browse/SEM4-6) · **Story Points:** 5 · **MoSCoW:** Must.

Als Entwickler möchte ich den tatsächlichen Test- und CI-Stand kennen, damit ich gezielte Verbesserungen statt Doppelarbeit plane.

Akzeptanzkriterien:

- [ ] Tests für Login, Rechte, Upload, Audio, Links, Kommentare und Backup sind zugeordnet.
- [ ] pytest wird mit getrennten Daten ausgeführt; Datum, Commit, Soll/Ist und Ergebnis sind protokolliert.
- [ ] GitHub-Testworkflow und Container-Smoke-Test werden geprüft; Betriebs-/Port-/Volume-Isolation ist vorher belegt.
- [ ] Mindestens eine relevante Testlücke oder begründete Qualitätsverbesserung ist identifiziert.

**Tasks**

Tabelle 02: Tasks P03.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P03.1 | **Isolierte Testumgebung prüfen:** Temporäre Daten, Namespaces/Volumes und Ports vor Ausführung prüfen; Produktivbetrieb unverändert lassen. | [SEM4-22](https://lukas-saegesser.atlassian.net/browse/SEM4-22) |
| P03.2 | **Bestehende Tests und Workflow ausführen:** pytest, vorhandenen Container-Smoke-Test und GitHub-Testworkflow prüfen; Datum, Commit, Soll/Ist und Resultate dokumentieren. | [SEM4-23](https://lukas-saegesser.atlassian.net/browse/SEM4-23) |
| P03.3 | **Abdeckung und Testlücken beurteilen:** Login, Rechte, Upload, Audio, Freigaben, Kommentare und Backup abgleichen; sinnvolle Lücke für P04 begründen. | [SEM4-24](https://lukas-saegesser.atlassian.net/browse/SEM4-24) |

#### User Story P04 – Erkannte Testlücke gezielt schliessen

**Jira:** [SEM4-7](https://lukas-saegesser.atlassian.net/browse/SEM4-7) · **Story Points:** 5 · **MoSCoW:** Must.

Als Entwickler möchte ich eine nachgewiesene Testlücke schliessen, damit Regressionen früher erkannt werden.

Akzeptanzkriterien:

- [ ] Aus P03 ist eine begründete Lücke ausgewählt und mit Antragsziel verknüpft.
- [ ] Die Ergänzung prüft sinnvolles Verhalten inklusive passendem Fehler- oder Grenzfall.
- [ ] Relevante Tests und CI sind erfolgreich; Änderung und Nachweis sind verlinkt.
- [ ] Bestehende Tests werden weiterhin als Vorleistung bezeichnet.

**Tasks**

Tabelle 03: Tasks P04.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P04.1 | **Testergänzung aus Bestandsprüfung auswählen:** Kleine fachlich relevante Lücke aus P03 mit Antragsziel und erwartetem Verhalten festlegen. | [SEM4-25](https://lukas-saegesser.atlassian.net/browse/SEM4-25) |
| P04.2 | **Test mit Fehler- oder Grenzfall ergänzen:** Test mit isolierten Daten implementieren; Verhalten aussagekräftig prüfen und keine Umsetzung bloss spiegeln. | [SEM4-26](https://lukas-saegesser.atlassian.net/browse/SEM4-26) |
| P04.3 | **Tests und CI prüfen und nachweisen:** Relevante Tests und CI ausführen; neuen Beitrag, Resultate und Grenzen dokumentieren. | [SEM4-27](https://lukas-saegesser.atlassian.net/browse/SEM4-27) |

### Epic A – Begleitendes Projektmanagement

#### User Story P06 – MVP-Review und Retrospektive durchführen

**Jira:** [SEM4-9](https://lukas-saegesser.atlassian.net/browse/SEM4-9) · **Story Points:** 2 · **MoSCoW:** Must.

Als Projektverantwortlicher möchte ich den ersten Mehrwert prüfen und reflektieren, damit Sprint 2 auf tatsächlichen Erkenntnissen aufbaut.

Akzeptanzkriterien:

- [ ] MVP-Demo zeigt Testbasis, neue Ergänzung und CI-Nachweis; Soll/Ist ist dokumentiert.
- [ ] Release v0.1.0 wird nur nach erfüllter DoD erstellt und verlinkt.
- [ ] Review-Ergebnis und tatsächliches Feedback sind datiert; Review-Mitteilung wird vorbereitet.
- [ ] Retrospektive nennt mindestens eine konkrete Massnahme für Sprint 2; keine Durchführung vorwegnehmen.

**Tasks**

Tabelle 04: Tasks P06.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P06.1 | **MVP-Demo und Soll-Ist vorbereiten:** Anforderungsmatrix, Testergänzung und CI-Nachweis demonstrierbar machen; offene Ziele sichtbar halten. | [SEM4-31](https://lukas-saegesser.atlassian.net/browse/SEM4-31) |
| P06.2 | **Release und Review durchführen:** v0.1.0 erst nach DoD erstellen; tatsächliches Review/Feedback und Mitteilungsentwurf dokumentieren. | [SEM4-32](https://lukas-saegesser.atlassian.net/browse/SEM4-32) |
| P06.3 | **Retrospektive und Folgemassnahme festhalten:** Was lief gut/weniger gut, konkrete Verbesserung mit Verantwortlichkeit und Termin für Sprint 2 erfassen. | [SEM4-33](https://lukas-saegesser.atlassian.net/browse/SEM4-33) |

### Reihenfolge und Abhängigkeiten

P03 → P04 → P06. Die Zielzuordnung aus der Vorarbeit bildet die Grundlage.
Tests verwenden getrennte Daten und Umgebungen.

## Bewertung mit MoSCoW

Tabelle 05: Priorisierung.

| Umfang | Kategorie | Begründung |
| --- | --- | --- |
| P03 – Test-/CI-Bestandsprüfung | Must | Grundlage für gezielte Verbesserungen. |
| P04 – Gezielte Testergänzung | Must | Neuer technischer Mehrwert des Sprints. |
| P06 – Review und Retrospektive | Must | Ergebnisprüfung und Verbesserung des Vorgehens. |
| Zusätzliche Testübersicht als Abbildung | Should | Erleichtert die Übersicht nach Erfüllung der Must-Ziele. |
| Demo-Video | Could | Ergänzende Darstellung der Ergebnisse. |
| Registry, Kubernetes und Deployment | Won’t in Sprint 1 | Umsetzung in Sprint 2/3. |

## Erwartetes Commitment und Definition of Done

- Bestehende Tests und CI sind isoliert geprüft; Abdeckung und Lücken sind dokumentiert.
- Mindestens eine relevante Testlücke ist mit Fehler- oder Grenzfall geschlossen.
- Relevante Tests und CI bestehen; Änderungen und Nachweise sind versioniert.
- Review und Retrospektive bewerten den technischen Mehrwert und liefern eine Massnahme für Sprint 2.

Es gilt die gemeinsame [Definition of Done](../../Definition-of-Done.md).
Geplanter Release: MVP / `v0.1.0`.

## Sprint Review

| Datum | Beteiligte | Git-Stand / Release |
| --- | --- | --- |
| | | |

Tabelle 06: Soll-Ist-Vergleich.

| Story | Erwartetes Ergebnis | Ist / Akzeptanzkriterien | Nachweis |
| --- | --- | --- | --- |
| P03 / SEM4-6 | Tests und CI isoliert prüfen | | |
| P04 / SEM4-7 | Testlücke schliessen | | |
| P06 / SEM4-9 | Review und Retrospektive | | |

### Rückmeldungen und Folgeaufgaben

### Burndown Chart

### Reflexion und Learnings

### Verbesserungsideen für kommende Sprints

### Gesamtbeurteilung des Sprints

## Sprint Retrospektive

### Was lief gut

### Was lief weniger gut

### Verbesserungsideen

Tabelle 07: Massnahmen aus der Retrospektive.

| Beobachtung | Massnahme | Verantwortlich | Termin | Jira |
| --- | --- | --- | --- | --- |
| | | | | |

### Fazit

## Abbildungsverzeichnis

## Tabellenverzeichnis

- Tabelle 01: Epics und Sprintumfang.
- Tabelle 02: Tasks P03.
- Tabelle 03: Tasks P04.
- Tabelle 04: Tasks P06.
- Tabelle 05: Priorisierung.
- Tabelle 06: Soll-Ist-Vergleich.
- Tabelle 07: Massnahmen aus der Retrospektive.

## Weitere Unterlagen

[Backlog](../../Backlog.md) · [Jira-Zuordnung](../../Jira-Abbildung.md)
