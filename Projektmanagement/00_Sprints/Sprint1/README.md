# Sprint 1

Direktzugriffe: [Jira-Board](https://lukas-saegesser.atlassian.net/jira/software/projects/SEM4/boards/67/backlog) · [Planning](#sprint-planning) · [Review](#sprint-review) · [Retrospektive](#sprint-retrospektive) · [Projektmanagement](../../Dokumentation.md)

## Inhaltsverzeichnis

- [Sprint Planning](#sprint-planning)
- [Sprint Goal](#sprint-goal)
- [Epics, User Stories und Tasks](#epics-user-stories-und-tasks)
- [Bewertung mit MoSCoW](#bewertung-mit-moscow)
- [Erwartetes Commitment und Definition of Done](#erwartetes-commitment-und-definition-of-done)
- [Sprint Review](#sprint-review)
- [Sprint Retrospektive](#sprint-retrospektive)
- [Abbildungsverzeichnis](#abbildungsverzeichnis)
- [Tabellenverzeichnis](#tabellenverzeichnis)

## Sprint Planning

**Thema:** Projektgrundlagen und überprüfbare Testbasis für SetFlow.
**Sprint-Dauer:** 26.10.2026 bis 15.11.2026.
**Planungsstand:** 26.10.2026. Planung vorbereitet; Stundenbudget und endgültiges Commitment offen.
**Verantwortlich:** Lukas Sägesser.
**Projektmanagementdozent:** Corrado Parisi. **Fachdozent:** Armin Dörzbach.

Die bestehende FastAPI-Anwendung, Tests, Docker-/Backup-Verfahren und der bisherige
Testworkflow sind Vorleistungen. Sprint 1 schafft die Grundlage für deren gezielte
Weiterentwicklung. Registry und Kubernetes-Deployment folgen in Sprint 2/3.

### Sprint Goal

**Antragsziele und Vorleistungen sind nachvollziehbar zugeordnet. Bestehende Tests
und CI sind isoliert geprüft und mindestens eine begründete Testlücke ist
geschlossen, sodass Änderungen an SetFlow fundiert beurteilt werden können.**

### Kapazität und Schätzung

Das Stundenbudget ist noch offen. Geplant sind vorläufig 20 Story
Points und 22 Stunden Arbeit sowie 5 Stunden Reserve. Das ist ein Planungsbedarf
von 27 Stunden, keine bestätigte Verfügbarkeit und keine erfasste Arbeitszeit.
Fibonacci-Punkte vergleichen Komplexität und Unsicherheit; es gibt keine feste
Umrechnung in Stunden. Task-Aufwand ist in der jeweiligen Story enthalten.

Die sechs Stories bilden den vorgeschlagenen Sprintumfang. Bei geringer Kapazität
wird P04 auf eine kleine relevante Lücke begrenzt und der Umfang transparent
abgestimmt. Der Sprint bleibt bis zum Kapazitätsabgleich ungestartet. Es wird keine
bereits durchgeführte Besprechung mit Dozierenden behauptet.

## Epics, User Stories und Tasks

Tabelle 01: Epics und Sprintumfang.

| Epic | Jira | Umfang in Sprint 1 |
| --- | --- | --- |
| A – Projektgrundlagen und Sprintsteuerung | [SEM4-3](https://lukas-saegesser.atlassian.net/browse/SEM4-3) | P01, P02, P05, P06 |
| B – Automatisierte Tests und versionierte Images | [SEM4-4](https://lukas-saegesser.atlassian.net/browse/SEM4-4) | P03, P04 |
| C – Kontrollierte Bereitstellung und Datenerhalt | [SEM4-5](https://lukas-saegesser.atlassian.net/browse/SEM4-5) | Kein Sprint-1-Umfang; Vorbereitung ab Sprint 2 |

### Epic A – Projektgrundlagen und Sprintsteuerung

#### User Story P01 – Repository und Projektgrundlagen vorbereiten

**Jira:** [SEM4-1](https://lukas-saegesser.atlassian.net/browse/SEM4-1) · **Story Points:** 3 · **Aufwand:** 4 Stunden (vorläufig).

Als Projektverantwortlicher möchte ich eine verständliche gemeinsame Ablage, damit Dozierende Ziele und Fortschritt beurteilen können.

Akzeptanzkriterien:

- [ ] Antrag ist verlinkt; Corrado Parisi und Armin Dörzbach sind mit Rollen eingetragen.
- [ ] PM und Fachliches sind gegenseitig verlinkt; Vorleistungen sind ausgewiesen.
- [ ] Lokale Arbeitsanweisungen bleiben unversioniert; verbleibende Historienprüfung ist dokumentiert.
- [ ] Offizielle Merkblätter und offene Formvorgaben sind nachvollziehbar erfasst.

**Tasks**

Tabelle 02: Tasks P01.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P01.1 | **Antrag, Rollen und Einstieg verknüpfen:** Antrag im Repository prüfen, Corrado Parisi und Armin Dörzbach mit Rollen eintragen und Einstieg/Navigation abgleichen. | [SEM4-16](https://lukas-saegesser.atlassian.net/browse/SEM4-16) |
| P01.2 | **Arbeitsregeln und Ablage bereinigen:** Lokale Anweisungen ignorieren; öffentliche Dokumentation und gegenseitige Links prüfen. Frühere Historie nicht ungeprüft umschreiben. | [SEM4-17](https://lukas-saegesser.atlassian.net/browse/SEM4-17) |
| P01.3 | **Formvorgaben und offene Grundlagen festhalten:** Merkblatt A und Gültigkeit weiterer Vorgaben klären; verbleibende Lücken und zuständige Rückfragen dokumentieren. | [SEM4-18](https://lukas-saegesser.atlassian.net/browse/SEM4-18) |

#### User Story P02 – Antragsziele und Nachweise zuordnen

**Jira:** [SEM4-2](https://lukas-saegesser.atlassian.net/browse/SEM4-2) · **Story Points:** 3 · **Aufwand:** 3 Stunden (vorläufig).

Als Fachdozent möchte ich messbare Antragsziele den geplanten Nachweisen zuordnen können, damit die Zielerreichung überprüfbar ist.

Akzeptanzkriterien:

- [ ] Alle Antragsziele A01–A07 sind mit Termin und Plan-ID erfasst.
- [ ] Vorleistung und neue Leistung sind pro Ziel getrennt.
- [ ] Jedes Ziel hat ein konkretes Nachweisformat; nicht erbrachte Nachweise bleiben als geplant bezeichnet.

**Tasks**

Tabelle 03: Tasks P02.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P02.1 | **Antragsziele messbar erfassen:** Alle Antragsziele A01–A07 mit Abnahmekriterien und Terminen aus dem Antrag übernehmen. | [SEM4-19](https://lukas-saegesser.atlassian.net/browse/SEM4-19) |
| P02.2 | **Vorleistungen und neue Leistungen trennen:** App, Tests, Workflow und Backup-Verfahren als Vorleistung zuordnen; neue Semesterarbeitsleistung je Ziel benennen. | [SEM4-20](https://lukas-saegesser.atlassian.net/browse/SEM4-20) |
| P02.3 | **Testfälle und Nachweisorte zuordnen:** Pro Ziel Plan-ID, geplanten Test und bereinigten Nachweisort festlegen; fehlende Nachweise als geplant kennzeichnen. | [SEM4-21](https://lukas-saegesser.atlassian.net/browse/SEM4-21) |

#### User Story P05 – Dozentenzugriffe und Planning-Kommunikation vorbereiten

**Jira:** [SEM4-8](https://lukas-saegesser.atlassian.net/browse/SEM4-8) · **Story Points:** 2 · **Aufwand:** 2 Stunden (vorläufig).

Als Projektverantwortlicher möchte ich Repo und Board für die Dozierenden zugänglich vorbereiten, damit frühes Feedback möglich wird.

Akzeptanzkriterien:

- [ ] Repo- und Board-Link sowie Rollen Corrado/Armin sind dokumentiert.
- [ ] Einladungsweg und verfügbare Leserechte sind geprüft; tatsächliche Einladungen/Zugriff bleiben bis Durchführung offen.
- [ ] Planning-Mitteilung enthält Sprintziel, vorläufige Schätzungen, Umfang und offene Kapazität.
- [ ] Versand und Zugriffsbestätigung werden nach Durchführung erfasst.

**Tasks**

Tabelle 04: Tasks P05.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P05.1 | **Einladungsweg und Rechte prüfen:** Dozentenkonten und passende Repo-/Jira-Leserechte klären; keine Einladungen als erfolgt behaupten. | [SEM4-28](https://lukas-saegesser.atlassian.net/browse/SEM4-28) |
| P05.2 | **Planning-Mitteilung vorbereiten:** Sprintziel, Links, Schätzungen, offenen Kapazitätsabgleich und Feedbackfragen in einen Teams-Entwurf aufnehmen. | [SEM4-29](https://lukas-saegesser.atlassian.net/browse/SEM4-29) |
| P05.3 | **Versand und Zugriff nach tatsächlicher Durchführung erfassen:** Versanddatum und Zugriffsbestätigungen nach Durchführung dokumentieren. | [SEM4-30](https://lukas-saegesser.atlassian.net/browse/SEM4-30) |

#### User Story P06 – MVP-Review und Retrospektive durchführen

**Jira:** [SEM4-9](https://lukas-saegesser.atlassian.net/browse/SEM4-9) · **Story Points:** 2 · **Aufwand:** 2 Stunden (vorläufig).

Als Projektverantwortlicher möchte ich den ersten Mehrwert prüfen und reflektieren, damit Sprint 2 auf tatsächlichen Erkenntnissen aufbaut.

Akzeptanzkriterien:

- [ ] MVP-Demo zeigt Testbasis, neue Ergänzung und CI-Nachweis; Soll/Ist ist dokumentiert.
- [ ] Release v0.1.0 wird nur nach erfüllter DoD erstellt und verlinkt.
- [ ] Review-Ergebnis und tatsächliches Feedback sind datiert; Review-Mitteilung wird vorbereitet.
- [ ] Retrospektive nennt mindestens eine konkrete Massnahme für Sprint 2; keine Durchführung vorwegnehmen.

**Tasks**

Tabelle 05: Tasks P06.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P06.1 | **MVP-Demo und Soll-Ist vorbereiten:** Anforderungsmatrix, Testergänzung und CI-Nachweis demonstrierbar machen; offene Ziele sichtbar halten. | [SEM4-31](https://lukas-saegesser.atlassian.net/browse/SEM4-31) |
| P06.2 | **Release und Review durchführen:** v0.1.0 erst nach DoD erstellen; tatsächliches Review/Feedback und Mitteilungsentwurf dokumentieren. | [SEM4-32](https://lukas-saegesser.atlassian.net/browse/SEM4-32) |
| P06.3 | **Retrospektive und Folgemassnahme festhalten:** Was lief gut/weniger gut, konkrete Verbesserung mit Verantwortlichkeit und Termin für Sprint 2 erfassen. | [SEM4-33](https://lukas-saegesser.atlassian.net/browse/SEM4-33) |

### Epic B – Automatisierte Tests und versionierte Images

#### User Story P03 – Vorhandene Tests und CI isoliert prüfen

**Jira:** [SEM4-6](https://lukas-saegesser.atlassian.net/browse/SEM4-6) · **Story Points:** 5 · **Aufwand:** 5 Stunden (vorläufig).

Als Entwickler möchte ich den tatsächlichen Test- und CI-Stand kennen, damit ich gezielte Verbesserungen statt Doppelarbeit plane.

Akzeptanzkriterien:

- [ ] Tests für Login, Rechte, Upload, Audio, Links, Kommentare und Backup sind zugeordnet.
- [ ] pytest wird mit getrennten Daten ausgeführt; Datum, Commit, Soll/Ist und Ergebnis sind protokolliert.
- [ ] GitHub-Testworkflow und Container-Smoke-Test werden geprüft; Betriebs-/Port-/Volume-Isolation ist vorher belegt.
- [ ] Mindestens eine relevante Testlücke oder begründete Qualitätsverbesserung ist identifiziert.

**Tasks**

Tabelle 06: Tasks P03.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P03.1 | **Isolierte Testumgebung prüfen:** Temporäre Daten, Namespaces/Volumes und Ports vor Ausführung prüfen; Produktivbetrieb unverändert lassen. | [SEM4-22](https://lukas-saegesser.atlassian.net/browse/SEM4-22) |
| P03.2 | **Bestehende Tests und Workflow ausführen:** pytest, vorhandenen Container-Smoke-Test und GitHub-Testworkflow prüfen; Datum, Commit, Soll/Ist und Resultate dokumentieren. | [SEM4-23](https://lukas-saegesser.atlassian.net/browse/SEM4-23) |
| P03.3 | **Abdeckung und Testlücken beurteilen:** Login, Rechte, Upload, Audio, Freigaben, Kommentare und Backup abgleichen; sinnvolle Lücke für P04 begründen. | [SEM4-24](https://lukas-saegesser.atlassian.net/browse/SEM4-24) |

#### User Story P04 – Erkannte Testlücke gezielt schliessen

**Jira:** [SEM4-7](https://lukas-saegesser.atlassian.net/browse/SEM4-7) · **Story Points:** 5 · **Aufwand:** 6 Stunden (vorläufig).

Als Entwickler möchte ich eine nachgewiesene Testlücke schliessen, damit Regressionen früher erkannt werden.

Akzeptanzkriterien:

- [ ] Aus P03 ist eine begründete Lücke ausgewählt und mit Antragsziel verknüpft.
- [ ] Die Ergänzung prüft sinnvolles Verhalten inklusive passendem Fehler- oder Grenzfall.
- [ ] Relevante Tests und CI sind erfolgreich; Änderung und Nachweis sind verlinkt.
- [ ] Bestehende Tests werden weiterhin als Vorleistung bezeichnet.

**Tasks**

Tabelle 07: Tasks P04.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P04.1 | **Testergänzung aus Bestandsprüfung auswählen:** Kleine fachlich relevante Lücke aus P03 mit Antragsziel und erwartetem Verhalten festlegen. | [SEM4-25](https://lukas-saegesser.atlassian.net/browse/SEM4-25) |
| P04.2 | **Test mit Fehler- oder Grenzfall ergänzen:** Test mit isolierten Daten implementieren; Verhalten aussagekräftig prüfen und keine Umsetzung bloss spiegeln. | [SEM4-26](https://lukas-saegesser.atlassian.net/browse/SEM4-26) |
| P04.3 | **Tests und CI prüfen und nachweisen:** Relevante Tests und CI ausführen; neuen Beitrag, Resultate und Grenzen dokumentieren. | [SEM4-27](https://lukas-saegesser.atlassian.net/browse/SEM4-27) |

### Reihenfolge und Abhängigkeiten

P01 → P02 → P03 → P04 → P06. P05 läuft früh begleitend.
Die Abhängigkeiten sind in Jira als Blockierungen erfasst. Keine App-Tests,
Compose-Starts, Restore-Vorgänge oder Deployments allein durch das Planning
ausführen. Für P03/P04 vorab getrennte Testdaten, Ports und Volumes prüfen.

## Bewertung mit MoSCoW

Tabelle 08: Priorisierung und Begründung.

| User Story / Option | Kategorie | Begründung |
| --- | --- | --- |
| P01 – Repository und Grundlagen | Must | Gemeinsame, nachvollziehbare Arbeitsgrundlage und Schulvorgaben sind Voraussetzung. |
| P02 – Antrags-/Nachweismatrix | Must | Ohne Zielzuordnung kann die neue Leistung nicht zuverlässig abgegrenzt und beurteilt werden. |
| P03 – Test-/CI-Bestandsprüfung | Must | Tatsächliche Vorleistungen und Lücken müssen vor einer Erweiterung bekannt sein. |
| P04 – Gezielte Testergänzung | Must | Liefert den neuen überprüfbaren Mehrwert dieses MVP. |
| P05 – Zugriffe und Kommunikation | Must | Frühes Feedback und Einsicht sind Teil des Antrags. |
| P06 – Review und Retrospektive | Must | Ergebnisprüfung und Verbesserung gehören zum vereinbarten agilen Vorgehen. |
| Zusätzliche bereinigte Übersichtsabbildung | Should | Hilft beim Lesen; erst nach den Must-Zielen und mit tatsächlichem Nachweis erstellen. |
| Demo-Video mit Audio | Could | Kann Feedback erleichtern; schriftliche Demo mit Nachweisen genügt. |
| Zusätzliche App-Funktionen / Hochverfügbarkeit | Won’t | Gehören nicht zum genehmigten DevOps-Schwerpunkt. |

Die optionalen Darstellungen sind kein zusätzliches Commitment und erhalten keine
erfundenen Tickets oder Aufwandserfassungen.

## Erwartetes Commitment und Definition of Done

**Vorgeschlagene Ergebnisse bis Sprintende:**

- Ziele A01–A07 sind mit Vorleistung, neuer Leistung, Test und Nachweisort verbunden.
- Repository, Backlog, DoD und Risiken sind verständlich zugänglich vorbereitet.
- Bestehende Tests/CI sind tatsächlich geprüft und Ergebnisse protokolliert.
- Eine begründete Testergänzung ist implementiert und erfolgreich geprüft.
- Dozierenden-Zugriff und Planning-/Review-Kommunikation sind nachvollziehbar
  vorbereitet; tatsächliche Einladungen und Versand werden separat bestätigt.
- MVP-Review und Retrospektive liefern einen Soll-Ist-Vergleich und eine konkrete
  Massnahme für Sprint 2.

Das endgültige Commitment wird nach Kapazitätsabgleich festgelegt.
Die [gemeinsame Definition of Done](../../Definition-of-Done.md) gilt zusätzlich
zu den storiespezifischen Kriterien. Insbesondere müssen Nachweise tatsächlich
vorliegen, Änderungen geprüft und versioniert sowie die Dokumentation aktualisiert
sein. Eigenprüfung und externes Feedback sind transparent zu unterscheiden.

**Release-Vorschlag:** `v0.1.0` nach erfüllter DoD. Kein Tag oder Release wurde
durch das Planning erstellt.

## Sprint Review

**Status:** noch nicht durchgeführt. Vorgesehen bis 15.11.2026; konkreten Termin
abstimmen. Die folgenden Felder dienen der späteren Erfassung.

- Datum und Form: offen.
- Tatsächlich Beteiligte / asynchron Informierte: offen.
- Gezeigter Git-Stand und Release: offen.
- Demo und Testnachweise: offen.
- Rückmeldungen von Corrado / Armin und Folgeaufgaben: nach Eingang ergänzen.

Tabelle 09: Soll-Ist-Vergleich beim Review.

| Story | Erwartetes Ergebnis | Ist / Akzeptanzkriterien | Nachweis |
| --- | --- | --- | --- |
| P01 / [SEM4-1](https://lukas-saegesser.atlassian.net/browse/SEM4-1) | Repository und Projektgrundlagen vorbereiten | Noch nicht abgenommen | Nach Durchführung ergänzen |
| P02 / [SEM4-2](https://lukas-saegesser.atlassian.net/browse/SEM4-2) | Antragsziele und Nachweise zuordnen | Noch nicht abgenommen | Nach Durchführung ergänzen |
| P03 / [SEM4-6](https://lukas-saegesser.atlassian.net/browse/SEM4-6) | Vorhandene Tests und CI isoliert prüfen | Noch nicht abgenommen | Nach Durchführung ergänzen |
| P04 / [SEM4-7](https://lukas-saegesser.atlassian.net/browse/SEM4-7) | Erkannte Testlücke gezielt schliessen | Noch nicht abgenommen | Nach Durchführung ergänzen |
| P05 / [SEM4-8](https://lukas-saegesser.atlassian.net/browse/SEM4-8) | Dozentenzugriffe und Planning-Kommunikation vorbereiten | Noch nicht abgenommen | Nach Durchführung ergänzen |
| P06 / [SEM4-9](https://lukas-saegesser.atlassian.net/browse/SEM4-9) | MVP-Review und Retrospektive durchführen | Noch nicht abgenommen | Nach Durchführung ergänzen |

### Burndown Chart

Erst nach tatsächlichem Sprintstart und gepflegten Schätzungen/Statusänderungen
aus Jira übernehmen. Bislang kein Burndown-Nachweis vorhanden.

### Reflexion und Learnings

Nach dem Review mit konkreten Beobachtungen ergänzen. Keine früheren Erfahrungen
aus Semesterarbeit 2 als Ergebnisse dieser Arbeit übernehmen.

### Verbesserungsideen für kommende Sprints

Erst auf Basis der tatsächlichen Durchführung formulieren und als Folgeaufgabe
mit Verantwortlichkeit und Termin festhalten.

### Gesamtbeurteilung des Sprints

Offen. Sprintziel erreicht / teilweise erreicht / nicht erreicht mit Begründung
und tatsächlichen Nachweisen bewerten. Noch keine Erfolgsaussage.

## Sprint Retrospektive

**Status:** noch nicht durchgeführt; im Anschluss an das Review vorgesehen.

### Was lief gut

Nach Durchführung ergänzen.

### Was lief weniger gut

Nach Durchführung ergänzen.

### Verbesserungsideen

Tabelle 10: Massnahmen aus der Retrospektive.

| Beobachtung | Konkrete Massnahme | Verantwortlich | Termin | Jira |
| --- | --- | --- | --- | --- |
| Nach Durchführung ergänzen | Offen | Offen | Offen | Offen |

### Fazit

Nach der tatsächlichen Retrospektive ergänzen.

## Abbildungsverzeichnis

Noch keine Abbildungen eingebunden. Jira-Board, Burndown oder Demo-Screenshots
erst nach tatsächlicher Aufnahme und Bereinigung ergänzen und beschriften.

## Tabellenverzeichnis

- Tabelle 01: Epics und Sprintumfang.
- Tabelle 02: Tasks P01.
- Tabelle 03: Tasks P02.
- Tabelle 04: Tasks P05.
- Tabelle 05: Tasks P06.
- Tabelle 06: Tasks P03.
- Tabelle 07: Tasks P04.
- Tabelle 08: Priorisierung und Begründung.
- Tabelle 09: Soll-Ist-Vergleich beim Review.
- Tabelle 10: Massnahmen aus der Retrospektive.

## Grundlage und weiterführende Dokumente

Der Aufbau orientiert sich an der
[Sprint-1-Dokumentation aus Semesterarbeit 2](https://gitlab.com/lukas03saegesser/semesterarbeit-2sem/-/tree/main/Projektmanagement/00_Sprints/Sprint1?ref_type=heads).
Inhalte und Ergebnisse sind für SetFlow neu geplant; historische Review-Ergebnisse
werden nicht übernommen.

[Gesamtbacklog](../../Backlog.md) · [Jira-Zuordnung](../../Jira-Abbildung.md) ·
[Risiken](../../Risiken.md) · [Anforderungsmatrix](../../../Fachlich/Anforderungsmatrix.md) ·
[Projektmanagement](../../Dokumentation.md)
