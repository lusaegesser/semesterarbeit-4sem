# Sprint 2

[Jira-Board](https://lukas-saegesser.atlassian.net/jira/software/projects/SEM4/boards/67/backlog) · [Projektmanagement](../../README.md)

## Inhaltsverzeichnis

- [Sprint Planning](#sprint-planning)
- [Epics, User Stories und Tasks](#epics-user-stories-und-tasks)
- [Bewertung mit MoSCoW](#bewertung-mit-moscow)
- [Erwartetes Commitment und Definition of Done](#erwartetes-commitment-und-definition-of-done)
- [Sprint Review](#sprint-review)
- [Sprint Retrospektive](#sprint-retrospektive)

## Sprint Planning

**Thema:** Geprüfte Container-Images und isolierte Helm-Zielumgebung.\
**Geplanter Zeitraum:** 16.11.2026 bis 13.12.2026.\
**Planungsstand:** 11.11.2026; Planning vorbereitet, Sprint noch nicht gestartet.\
**Verantwortlich:** Lukas Sägesser.\
**Projektmanagementdozent:** Corrado Parisi. **Fachdozent:** Armin Dörzbach.

Sprint 1 lieferte die geprüfte Testbasis und sieben neue Passwortfälle; insgesamt
27 Tests bestanden. MVP `v0.1.0` ist veröffentlicht. Anwendung, ursprüngliche Tests
und bestehender Testworkflow bleiben Vorleistungen. Sprint 2 erweitert die
Pipeline um GHCR und bereitet Kubernetes/Helm isoliert vor.

### Sprint Goal

**Geprüfte Änderungen werden als Commit-gekennzeichnete GHCR-Images veröffentlicht;
ein Testfehler sperrt Publish. Kubernetes und Helm stellen ein geprüftes Image
isoliert bereit. Optional wird die Pipeline mit Design- und BPM-Weiterentwicklung
erprobt.**

### Schätzung und Priorität

**16 SP Must** (P07/P08) und **5 SP Could** (P13); maximal **21 SP**.
Die Schätzungen sind relativ und vorläufig; das verfügbare Zeitbudget ist offen.
Task-Aufwand ist in den Stories enthalten. P13 wird erst nach den Must-Zielen
umgesetzt. Review, Retrospektive und Nachweise begleiten die technische Arbeit.

### Übernahme aus Sprint 1

Vor dem ersten Testlauf Interpreter, Abhängigkeiten und temporären Schreibpfad
prüfen und im Testprotokoll festhalten (P07.1). Status und Checklisten bei jedem
Story-Abschluss gemeinsam nachführen.

### Umfangsänderung vom 11.11.2026

P13 umfasst zusätzlich BPM-Bereiche wie `127–150`. Bestehende Einzelwerte und
mehrere Genres per Kommatrennung bleiben erhalten. Wegen Datenverträglichkeit,
Validierung und Tests steigt die vorläufige Schätzung von 3 auf 5 SP.
Die Story bleibt Could und dient als reale App-Änderung zur Pipeline-Erprobung.

## Epics, User Stories und Tasks

Tabelle 01: Epics und Sprintumfang.

| Epic | Jira | Umfang |
| --- | --- | --- |
| B – Automatisierte Tests und versionierte Images | SEM4-4 | P07, P13 |
| C – Kontrollierte Bereitstellung und Datenerhalt | SEM4-5 | P08 |

### User Story P07 – Tests mit versioniertem GHCR-Publish verbinden

**Jira:** [SEM4-10](https://lukas-saegesser.atlassian.net/browse/SEM4-10) · **Story Points:** 8 · **MoSCoW:** Must.

Als Entwickler möchte ich geprüfte Commit-Images automatisch veröffentlichen, damit deploybare Versionen eindeutig nachvollziehbar sind.

Akzeptanzkriterien:

- [ ] Test-Vorabcheck für Interpreter, Abhängigkeiten und beschreibbaren Temp-Pfad ist dokumentiert.
- [ ] pytest/HTTPX deckt die Antragsfälle einschliesslich Passwortprüfung und Uploadbegrenzung ab.
- [ ] Publish erfolgt nur nach erfolgreichen Hauptbranch-Tests; Commit-Tag und Digest sind nachvollziehbar.
- [ ] Drei erfolgreiche CI-/Publish-Läufe sind verlinkt.
- [ ] Ein absichtlicher Testfehler verhindert die Veröffentlichung; negativer Nachweis ohne produktive Beeinträchtigung.

Tabelle 02: Tasks P07.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P07.1 | **Test-Vorabcheck und Abdeckung prüfen:** Interpreter, gepinnte Abhängigkeiten und beschreibbaren Temp-Pfad prüfen; A02 mit den 27 vorhandenen Tests abgleichen und nötige Upload-Grenzfälle ergänzen. | SEM4-36 |
| P07.2 | **Tests als Publish-Sperre verknüpfen:** GitHub-Workflow so erweitern, dass Publish nur nach erfolgreichen Tests und ausschliesslich für vertrauenswürdige Hauptbranch-Läufe erfolgt; minimale Berechtigungen und getrennte PR-Tests. | SEM4-37 |
| P07.3 | **Versionierte Images und drei Läufe nachweisen:** Commit-gekennzeichnete Images in GHCR veröffentlichen; Commit, Lauf, Image-Tag und Digest für drei erfolgreiche Durchläufe protokollieren. | SEM4-38 |
| P07.4 | **Fehlerfall und gesperrten Publish belegen:** Einen absichtlichen Testfehler in einem kontrollierten, publish-fähigen Testpfad auslösen und fehlende Veröffentlichung nachweisen; kein blosser PR-Lauf ohne Publish-Berechtigung. Fehler anschliessend zurücknehmen. | SEM4-39 |

### User Story P08 – Lokale Kubernetes- und Helm-Zielumgebung vorbereiten

**Jira:** [SEM4-11](https://lukas-saegesser.atlassian.net/browse/SEM4-11) · **Story Points:** 8 · **MoSCoW:** Must.

Als Betreiber möchte ich eine begründete lokale Zielumgebung, damit SetFlow reproduzierbar bereitgestellt werden kann.

Akzeptanzkriterien:

- [ ] Cluster-Variante und Ressourcen sind begründet; Architektur und Wiederaufbau sind dokumentiert.
- [ ] Helm-Chart parametrisiert Image, Konfiguration und persistente Daten; keine Secrets im Git.
- [ ] Separater Projekt-Namespace und Kollisionsprüfung schützen den bestehenden Compose-Betrieb.
- [ ] Isolierte Helm-Installation und Health-Prüfung sind protokolliert; Kubernetes-API bleibt privat.

Tabelle 03: Tasks P08.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P08.1 | **Zielumgebung und Ressourcen festlegen:** Lokale Cluster-Variante anhand vorhandener Hardware begründen; benötigte Ressourcen, Wiederaufbau und Trennung vom Compose-Betrieb dokumentieren. | SEM4-40 |
| P08.2 | **Helm-Chart erstellen und prüfen:** Image/Tag oder Digest, Konfiguration, Service und persistente Daten parametrieren; keine Secrets im Git; Chart mit lint und gerenderten Manifesten prüfen. | SEM4-41 |
| P08.3 | **Isolierte Installation vorbereiten:** Eigenen Namespace, Volumes und Ports vor Installation auf Kollisionen prüfen; synthetische Daten und begrenzte Zugriffe verwenden; Kubernetes-API nicht öffentlich freigeben. | SEM4-42 |
| P08.4 | **Installation und Health nachweisen:** Geprüftes Image in der isolierten Umgebung mit Helm installieren; Health und Persistenzkonfiguration kontrollieren, Installations-/Wiederaufbauschritte dokumentieren. | SEM4-43 |

### User Story P13 – App weiterentwickeln: Orange-Schwarz-Design und BPM-Bereiche über die CI-/Registry-Pipeline veröffentlichen

**Jira:** [SEM4-34](https://lukas-saegesser.atlassian.net/browse/SEM4-34) · **Story Points:** 5 · **MoSCoW:** Could.

Als Nutzer möchte ich eine lesbare Orange-Schwarz-Oberfläche und BPM-Bereiche für meine Sets, damit SetFlow besser bedienbar ist und die neue Pipeline mit einer echten App-Änderung geprüft wird.

Akzeptanzkriterien:

- [ ] Orange-Schwarz-Design mit lesbaren Texten, Statusmeldungen und Fokuszuständen auf Desktop und Smartphone; SetFlow-Titelbild bleibt erhalten.
- [ ] Einzelne BPM-Werte und aufsteigende Bereiche wie 127–150 lassen sich erfassen, speichern, bearbeiten und anzeigen; ungültige/umgekehrte Bereiche werden abgewiesen.
- [ ] Bestehende Sets und BPM-Einzelwerte bleiben erhalten; mehrere Genres per Kommatrennung bleiben nutzbar.
- [ ] Regressionstests prüfen BPM-Werte, Bereiche, ungültige Eingaben und bestehende Bedienabläufe.
- [ ] Die reale App-Änderung durchläuft Tests, Build und GHCR-Publish; Commit, Lauf und Image-Digest sind dokumentiert.

Tabelle 04: Tasks P13.

| Task | Beschreibung | Jira |
| --- | --- | --- |
| P13.1 | **Orange-Schwarz-Oberfläche gestalten:** Vorhandenes SetFlow-Titelbild beibehalten; Farbschema, Lesbarkeit, Fokuszustände und mobile Bedienung prüfen. | SEM4-44 |
| P13.2 | **BPM-Einzelwert und Bereich ermöglichen:** Einzelwerte sowie Bereiche wie 127–150 erfassen, speichern, bearbeiten und anzeigen; aufsteigende Werte validieren und vorhandene Datensätze erhalten. Mehrere Genres per Komma bleiben nutzbar. | SEM4-45 |
| P13.3 | **Regression und Datenverträglichkeit prüfen:** Einzelwert, Bereich, umgekehrte/ungültige Eingabe und bestehende Datensätze testen; Upload, Wiedergabe und Freigabe weiter prüfen. | SEM4-46 |
| P13.4 | **App-Änderung über Pipeline veröffentlichen:** Tests, Build und GHCR-Publish mit der realen Änderung durchlaufen; Commit, Digest und Resultate dokumentieren. Prüfung der vollständigen Deploymentkette folgt in Sprint 3. | SEM4-47 |

### Reihenfolge und Abgrenzung

P07.1 → P07.2 → P07.3/P07.4. P08.1/P08.2 können parallel vorbereitet werden;
P08.4 verwendet ein geprüftes Image aus P07. P13 folgt den Must-Zielen P07/P08.
Der negative Publish-Nachweis muss denselben grundsätzlich publish-fähigen
Triggerpfad prüfen; ein ohnehin nicht veröffentlichender PR allein genügt nicht.

Tests und Helm-Installation verwenden eigene Daten, Namespaces, Volumes und Ports.
Der bisherige Compose-Betrieb bleibt erhalten. Lokaler Runner, automatisches
Deployment, Rollback und vollständiger Datenerhalt-/Restore-Nachweis folgen in
Sprint 3. Das Helm-Experiment ist noch kein produktives Deployment.

## Bewertung mit MoSCoW

Tabelle 05: Priorisierung.

| Umfang | Kategorie | Begründung |
| --- | --- | --- |
| P07 – Tests und GHCR-Publish | Must | Erfüllt den CI-/Image-Nachweis A02/A03. |
| P08 – Kubernetes und Helm | Must | Schafft die isolierte Grundlage für A04 und Sprint 3. |
| Ergänzende Pipeline-Übersicht | Should | Erleichtert das Verständnis nach Erfüllung der Pflichtnachweise. |
| P13 – Design und BPM-Bereiche | Could | Reale App-Weiterentwicklung zur Erprobung der neuen Pipeline. |
| Mitwirkendenkonten / automatisches Produktivdeployment | Won’t in Sprint 2 | P14 und vollständige CI/CD-Nachweise gehören zu Sprint 3. |

## Erwartetes Commitment und Definition of Done

- A02-Testfälle sind abgeglichen; nötige Ergänzungen und CI bestehen.
- Drei erfolgreiche GHCR-Veröffentlichungen sind mit Commit, Tag und Digest belegt.
- Ein kontrollierter Testfehler verhindert Publish nachvollziehbar.
- Ein geprüftes Image läuft per Helm in einer getrennten Zielumgebung; Health,
  Konfiguration und Wiederaufbau sind dokumentiert.
- Review und Retrospektive vergleichen Soll/Ist und bestimmen eine Massnahme für Sprint 3.
- P13 liefert nur bei verbleibender Kapazität Design-/BPM-Verbesserungen mit Pipeline-Nachweis.

Es gilt die gemeinsame [Definition of Done](../../Definition-of-Done.md).
Geplanter Mehrwert: **MLP**, Release-Vorschlag `v0.2.0` nach erfüllter DoD.
Der Release wird erst nach tatsächlicher Prüfung erstellt. Kommunikation erfolgt
über Teams; Nachrichtentexte werden nicht im Repository gesammelt.

## Sprint Review

Tabelle 06: Review-Rahmen.

| Datum | Beteiligte | Git-Stand / Release |
| --- | --- | --- |
| | | |

Tabelle 07: Soll-Ist-Vergleich.

| Story | Erwartetes Ergebnis | Ist / Akzeptanzkriterien | Nachweis |
| --- | --- | --- | --- |
| P07 / SEM4-10 | Geprüfte GHCR-Images und Publish-Sperre | | |
| P08 / SEM4-11 | Isolierte Kubernetes-/Helm-Installation | | |
| P13 / SEM4-34 | Optionale Design-/BPM-Änderung über Pipeline | | |

### Rückmeldungen und Folgeaufgaben

### Burndown Chart

### Reflexion und Learnings

### Verbesserungsideen für kommende Sprints

### Gesamtbeurteilung des Sprints

## Sprint Retrospektive

### Was lief gut

### Was lief weniger gut

### Verbesserungsideen

Tabelle 08: Massnahmen aus der Retrospektive.

| Beobachtung | Massnahme | Verantwortlich | Termin | Jira |
| --- | --- | --- | --- | --- |
| | | | | |

### Fazit

## Abbildungsverzeichnis

## Tabellenverzeichnis

- Tabelle 01: Epics und Sprintumfang.
- Tabelle 02: Tasks P07.
- Tabelle 03: Tasks P08.
- Tabelle 04: Tasks P13.
- Tabelle 05: Priorisierung.
- Tabelle 06: Review-Rahmen.
- Tabelle 07: Soll-Ist-Vergleich.
- Tabelle 08: Massnahmen aus der Retrospektive.

## Weitere Unterlagen

[Backlog](../../Backlog.md) · [Jira-Zuordnung](../../Jira-Abbildung.md)
