# Product Backlog

Stand: 26.10.2026. Verantwortlich: Lukas Sägesser. Alle Einträge sind Must-Ziele des
Antrags bzw. notwendige PM-Arbeit. Zusätzliche App-Funktionen, Hochverfügbarkeit und
persönliche Website sind ausserhalb des Umfangs (Won’t). Verbesserungen ohne
Antragsbezug werden erst nach den Must-Zielen bewertet.

Plan-IDs P01–P12 sind stabile lokale Referenzen, keine erfundenen Jira-Tickets.
Punkte (Fibonacci) und Stunden sind vorläufige Schätzungen. Kapazität ist offen.
Sprint 2/3 sind eine Grobplanung und werden beim jeweiligen Planning neu bewertet.

Die zwölf Stories sind in Jira erfasst und drei Epics zugeordnet; Kennungen siehe
[Jira-Abbildung](Jira-Abbildung.md). Die 18 Sprint-1-Unteraufgaben und Task-Tabellen
stehen in der [Sprint-Dokumentation](00_Sprints/Sprint1/README.md).
Task-Aufwand ist in den Story-Schätzungen enthalten.

Tabelle 1: Priorisierte Roadmap.

| Plan-ID | Story | Sprint | Punkte | Stunden |
| --- | --- | ---: | ---: | ---: |
| P01 | Repository und Projektgrundlagen vorbereiten | 1 | 3 | 4 |
| P02 | Antragsziele und Nachweise zuordnen | 1 | 3 | 3 |
| P03 | Vorhandene Tests und CI isoliert prüfen | 1 | 5 | 5 |
| P04 | Erkannte Testlücke gezielt schliessen | 1 | 5 | 6 |
| P05 | Dozentenzugriffe und Planning-Kommunikation vorbereiten | 1 | 2 | 2 |
| P06 | MVP-Review und Retrospektive durchführen | 1 | 2 | 2 |
| P07 | Tests mit versioniertem GHCR-Publish verbinden | 2 | 8 | 10 |
| P08 | Lokale Kubernetes- und Helm-Zielumgebung vorbereiten | 2 | 8 | 10 |
| P09 | Lokalen Deployment-Runner begrenzen | 3 | 5 | 7 |
| P10 | Deployments mit Smoke-Test und Rollback nachweisen | 3 | 8 | 10 |
| P11 | Datenerhalt und isolierten Restore nachweisen | 3 | 8 | 10 |
| P12 | MMP und Abschlussunterlagen vorbereiten | 3 | 5 | 7 |

Sprint 2 endet am 13.12.2026; Sprint 3 am 21.01.2027. P12 enthält laufende
Review-Arbeit sowie den Abschluss vom 22.–27.01.2027. Das Abschlussfenster ist
kein vierter Umsetzungssprint. Review/Retro für Sprint 2 und 3 jeweils zum
Sprintende durchführen und im Planning als Aufwand berücksichtigen.

## P01 – Repository und Projektgrundlagen vorbereiten

Als Projektverantwortlicher möchte ich eine verständliche gemeinsame Ablage, damit Dozierende Ziele und Fortschritt beurteilen können.

Sprint 1; Must; 3 Punkte; 4 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Antrag ist verlinkt; Corrado Parisi und Armin Dörzbach sind mit Rollen eingetragen.
- [ ] PM und Fachliches sind gegenseitig verlinkt; Vorleistungen sind ausgewiesen.
- [ ] Lokale Arbeitsanweisungen bleiben unversioniert; verbleibende Historienprüfung ist dokumentiert.
- [ ] Offizielle Merkblätter und offene Formvorgaben sind nachvollziehbar erfasst.

## P02 – Antragsziele und Nachweise zuordnen

Als Fachdozent möchte ich messbare Antragsziele den geplanten Nachweisen zuordnen können, damit die Zielerreichung überprüfbar ist.

Sprint 1; Must; 3 Punkte; 3 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Alle Antragsziele A01–A07 sind mit Termin und Plan-ID erfasst.
- [ ] Vorleistung und neue Leistung sind pro Ziel getrennt.
- [ ] Jedes Ziel hat ein konkretes Nachweisformat; nicht erbrachte Nachweise bleiben als geplant bezeichnet.

## P03 – Vorhandene Tests und CI isoliert prüfen

Als Entwickler möchte ich den tatsächlichen Test- und CI-Stand kennen, damit ich gezielte Verbesserungen statt Doppelarbeit plane.

Sprint 1; Must; 5 Punkte; 5 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Tests für Login, Rechte, Upload, Audio, Links, Kommentare und Backup sind zugeordnet.
- [ ] pytest wird mit getrennten Daten ausgeführt; Datum, Commit, Soll/Ist und Ergebnis sind protokolliert.
- [ ] GitHub-Testworkflow und Container-Smoke-Test werden geprüft; Betriebs-/Port-/Volume-Isolation ist vorher belegt.
- [ ] Mindestens eine relevante Testlücke oder begründete Qualitätsverbesserung ist identifiziert.

## P04 – Erkannte Testlücke gezielt schliessen

Als Entwickler möchte ich eine nachgewiesene Testlücke schliessen, damit Regressionen früher erkannt werden.

Sprint 1; Must; 5 Punkte; 6 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Aus P03 ist eine begründete Lücke ausgewählt und mit Antragsziel verknüpft.
- [ ] Die Ergänzung prüft sinnvolles Verhalten inklusive passendem Fehler- oder Grenzfall.
- [ ] Relevante Tests und CI sind erfolgreich; Änderung und Nachweis sind verlinkt.
- [ ] Bestehende Tests werden weiterhin als Vorleistung bezeichnet.

## P05 – Dozentenzugriffe und Planning-Kommunikation vorbereiten

Als Projektverantwortlicher möchte ich Repo und Board für die Dozierenden zugänglich vorbereiten, damit frühes Feedback möglich wird.

Sprint 1; Must; 2 Punkte; 2 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Repo- und Board-Link sowie Rollen Corrado/Armin sind dokumentiert.
- [ ] Einladungsweg und verfügbare Leserechte sind geprüft; tatsächliche Einladungen/Zugriff bleiben bis Durchführung offen.
- [ ] Planning-Mitteilung enthält Sprintziel, vorläufige Schätzungen, Umfang und offene Kapazität.
- [ ] Versand erfolgt durch Lukas; Versand und Zugriffsbestätigung werden erst danach erfasst.

## P06 – MVP-Review und Retrospektive durchführen

Als Projektverantwortlicher möchte ich den ersten Mehrwert prüfen und reflektieren, damit Sprint 2 auf tatsächlichen Erkenntnissen aufbaut.

Sprint 1; Must; 2 Punkte; 2 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] MVP-Demo zeigt Testbasis, neue Ergänzung und CI-Nachweis; Soll/Ist ist dokumentiert.
- [ ] Release v0.1.0 wird nur nach erfüllter DoD erstellt und verlinkt.
- [ ] Review-Ergebnis und tatsächliches Feedback sind datiert; Review-Mitteilung wird vorbereitet.
- [ ] Retrospektive nennt mindestens eine konkrete Massnahme für Sprint 2; keine Durchführung vorwegnehmen.

## P07 – Tests mit versioniertem GHCR-Publish verbinden

Als Entwickler möchte ich geprüfte Commit-Images automatisch veröffentlichen, damit deploybare Versionen eindeutig nachvollziehbar sind.

Sprint 2; Must; 8 Punkte; 10 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] pytest/HTTPX deckt die Antragsfälle einschliesslich Passwortprüfung und Uploadbegrenzung ab.
- [ ] Publish erfolgt nur nach erfolgreichen Hauptbranch-Tests; Commit-Tag und Digest sind nachvollziehbar.
- [ ] Drei erfolgreiche CI-/Publish-Läufe sind verlinkt.
- [ ] Ein absichtlicher Testfehler verhindert die Veröffentlichung; negativer Nachweis ohne produktive Beeinträchtigung.

## P08 – Lokale Kubernetes- und Helm-Zielumgebung vorbereiten

Als Betreiber möchte ich eine begründete lokale Zielumgebung, damit SetFlow reproduzierbar bereitgestellt werden kann.

Sprint 2; Must; 8 Punkte; 10 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Cluster-Variante und Ressourcen sind begründet; Architektur und Wiederaufbau sind dokumentiert.
- [ ] Helm-Chart parametrisiert Image, Konfiguration und persistente Daten; keine Secrets im Git.
- [ ] Separater Projekt-Namespace und Kollisionsprüfung schützen den bestehenden Compose-Betrieb.
- [ ] Isolierte Helm-Installation und Health-Prüfung sind protokolliert; Kubernetes-API bleibt privat.

## P09 – Lokalen Deployment-Runner begrenzen

Als Betreiber möchte ich nur vertrauenswürdige Deployments zulassen, damit Runner und Cluster geschützt bleiben.

Sprint 3; Must; 5 Punkte; 7 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Nur geschützte Hauptbranch-Deployment-Jobs laufen lokal; keine Pull-Request-Jobs.
- [ ] Kubernetes-Rechte sind auf den Projekt-Namespace begrenzt und nachvollziehbar geprüft.
- [ ] Secrets und Runner-Betrieb sind geschützt dokumentiert; öffentliche API-Freigabe ist nicht erforderlich.
- [ ] Tarif-/Branchschutzgrenzen sind geprüft und wirksame Umsetzung belegt.

## P10 – Deployments mit Smoke-Test und Rollback nachweisen

Als Betreiber möchte ich geprüfte Releases und einen Rückfall, damit Änderungen kontrolliert ausgeliefert werden.

Sprint 3; Must; 8 Punkte; 10 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Drei aufeinanderfolgende Helm-Deployments verwenden geprüfte Images und bestehen automatischen /health-Smoke-Test.
- [ ] Commit, Image-Digest, Helm-Revision und Ergebnis jedes Laufs sind verlinkt.
- [ ] Eine frühere Version wird per Helm-Rollback wiederhergestellt und erfolgreich geprüft.
- [ ] Fehlerreaktion und Rückfall sind dokumentiert; Produktionsdaten bleiben geschützt.

## P11 – Datenerhalt und isolierten Restore nachweisen

Als Nutzer möchte ich meine Sets und Freigaben behalten, damit Pod-Wechsel und Wiederherstellung keine Daten verlieren.

Sprint 3; Must; 8 Punkte; 10 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Testset, synthetische Audiodatei, Kommentar und Freigabelink bleiben nach Pod-Ersatz erhalten.
- [ ] Sicherung wird geprüft und in getrenntem Namespace/Volume wiederhergestellt.
- [ ] DB-Integrität, Datensatzanzahlen und Audio-SHA-256 stimmen mit der Sicherung überein.
- [ ] Nachweis und Rückfallplan sind dokumentiert; keine privaten Daten oder Backup-Archive im Git.

## P12 – MMP und Abschlussunterlagen vorbereiten

Als Projektverantwortlicher möchte ich Zielerreichung und Erkenntnisse nachvollziehbar abschliessen, damit die Arbeit beurteilt werden kann.

Sprint 3; Must; 5 Punkte; 7 Stunden (vorläufig).

Akzeptanzkriterien:

- [ ] Sprint-2- und Sprint-3-Planning, Review, Release und Retro werden nach tatsächlicher Durchführung nachgeführt.
- [ ] Soll/Ist aller Antragsziele, Testnachweise, Betrieb und Risiken sind verlinkt.
- [ ] Abgabeform, Quellen, erforderliche Hilfsmitteldeklaration und Präsentation sind nach gültigen Schulvorgaben geprüft.
- [ ] Vollständige Git-Historie und Dateistand werden vor öffentlicher Freigabe geprüft; Sichtbarkeitswechsel bleibt separate Aktion.

## Abhängigkeiten

P01 → P02 → P03 → P04 → P06. P05 läuft früh begleitend.
P03/P04 → P07; P02 → P08; P07/P08 → P09 → P10 → P11.
P12 begleitet Reviews und bündelt den Abschluss; Ergebnisse nicht erst am Ende dokumentieren.

Für jede Story gilt die [Definition of Done](Definition-of-Done.md).
Jira-Zuordnung und Übertragungsstand: [Jira-Abbildung](Jira-Abbildung.md).
