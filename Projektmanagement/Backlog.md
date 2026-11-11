# Product Backlog

Stand: 11.11.2026. Priorisierung mit MoSCoW und relative Schätzung mit Story Points; keine Stundenschätzungen.
MoSCoW beschreibt die Wichtigkeit, nicht den Aufwand. Sprint 2/3 sind Grobplanungen.

Repository, Jira-Board, Backlog, Zielzuordnung und Dozentenzugriffe zählen zur
Vorarbeit (Sprint 0). Dafür wird kein eigener Jira-Sprint und kein Sprintbericht
geführt. Bestehende Vorgänge bleiben ohne Sprintzuordnung erhalten.

| Plan-ID | Jira | Story | Zuordnung | Story Points | MoSCoW |
| --- | --- | --- | --- | ---: | --- |
| P01 | SEM4-1 | Repository und Projektgrundlagen | Vorarbeit | 3 | Must |
| P02 | SEM4-2 | Antragsziele und Nachweise | Vorarbeit | 3 | Must |
| P05 | SEM4-8 | Dozentenzugriffe und Kommunikation | Vorarbeit | 2 | Must |
| P03 | SEM4-6 | Tests und CI isoliert prüfen | Sprint 1 | 5 | Must |
| P04 | SEM4-7 | Testlücke schliessen | Sprint 1 | 5 | Must |
| P06 | SEM4-9 | Review und Retrospektive | Sprint 1, begleitendes PM | 2 | Must |
| P07 | SEM4-10 | Tests mit GHCR-Publish verbinden | Sprint 2 | 8 | Must |
| P08 | SEM4-11 | Kubernetes und Helm vorbereiten | Sprint 2 | 8 | Must |
| P09 | SEM4-12 | Deployment-Runner begrenzen | Sprint 3 | 5 | Must |
| P10 | SEM4-13 | Deployment, Smoke-Test und Rollback | Sprint 3 | 8 | Must |
| P11 | SEM4-14 | Datenerhalt und Restore | Sprint 3 | 8 | Must |
| P12 | SEM4-15 | MMP und Abschlussunterlagen | Sprint 3, begleitendes PM | 5 | Must |
| P13 | SEM4-34 | Design und BPM-Bereiche über CI-/Registry-Pipeline veröffentlichen | Sprint 2, optional | 5 | Could |
| P14 | SEM4-35 | App weiterentwickeln: Mitwirkendenkonten über die vollständige CI/CD-Pipeline ausliefern | Sprint 3, optional | 8 | Could |

Abschlussfenster: 22.–27.01.2027 für Enddokumentation und Präsentation.
Weitere App-Funktionen ausserhalb P13/P14 und Hochverfügbarkeit gehören nicht zum Umfang (Won’t).

## Optionale App-Weiterentwicklung – Ergänzung vom 04.11.2026

P13 und P14 ergänzen die App und dienen gleichzeitig als praktische Tests der
in Sprint 2 und 3 aufgebauten Lösungen: P13 nutzt Tests, Build und Registry-Publish;
P14 prüft die vollständige Kette bis Deployment, Smoke-Test und Rückfall.
Beide Stories sind Could; die Must-Ziele des Antrags haben Vorrang.
Sie werden nur bei verbleibender Kapazität umgesetzt und erweitern die Pflichtziele nicht.

## P01 – Repository und Projektgrundlagen vorbereiten

Als Projektverantwortlicher möchte ich eine verständliche gemeinsame Ablage, damit Dozierende Ziele und Fortschritt beurteilen können.

Vorarbeit (Sprint 0); **Story Points: 3 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Antrag ist verlinkt; Corrado Parisi und Armin Dörzbach sind mit Rollen eingetragen.
- [ ] PM und Fachliches sind gegenseitig verlinkt; Vorleistungen sind ausgewiesen.
- [ ] Lokale Arbeitsanweisungen bleiben unversioniert; verbleibende Historienprüfung ist dokumentiert.
- [ ] Offizielle Merkblätter und offene Formvorgaben sind nachvollziehbar erfasst.

## P02 – Antragsziele und Nachweise zuordnen

Als Fachdozent möchte ich messbare Antragsziele den geplanten Nachweisen zuordnen können, damit die Zielerreichung überprüfbar ist.

Vorarbeit (Sprint 0); **Story Points: 3 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Alle Antragsziele A01–A07 sind mit Termin und Plan-ID erfasst.
- [ ] Vorleistung und neue Leistung sind pro Ziel getrennt.
- [ ] Jedes Ziel hat ein konkretes Nachweisformat; nicht erbrachte Nachweise bleiben als geplant bezeichnet.

## P03 – Vorhandene Tests und CI isoliert prüfen

Als Entwickler möchte ich den tatsächlichen Test- und CI-Stand kennen, damit ich gezielte Verbesserungen statt Doppelarbeit plane.

Sprint 1; **Story Points: 5 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Tests für Login, Rechte, Upload, Audio, Links, Kommentare und Backup sind zugeordnet.
- [ ] pytest wird mit getrennten Daten ausgeführt; Datum, Commit, Soll/Ist und Ergebnis sind protokolliert.
- [ ] GitHub-Testworkflow und Container-Smoke-Test werden geprüft; Betriebs-/Port-/Volume-Isolation ist vorher belegt.
- [ ] Mindestens eine relevante Testlücke oder begründete Qualitätsverbesserung ist identifiziert.

## P04 – Erkannte Testlücke gezielt schliessen

Als Entwickler möchte ich eine nachgewiesene Testlücke schliessen, damit Regressionen früher erkannt werden.

Sprint 1; **Story Points: 5 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Aus P03 ist eine begründete Lücke ausgewählt und mit Antragsziel verknüpft.
- [ ] Die Ergänzung prüft sinnvolles Verhalten inklusive passendem Fehler- oder Grenzfall.
- [ ] Relevante Tests und CI sind erfolgreich; Änderung und Nachweis sind verlinkt.
- [ ] Bestehende Tests werden weiterhin als Vorleistung bezeichnet.

## P05 – Dozentenzugriffe und Planning-Kommunikation vorbereiten

Als Projektverantwortlicher möchte ich Repo und Board für die Dozierenden zugänglich vorbereiten, damit frühes Feedback möglich wird.

Vorarbeit (Sprint 0); **Story Points: 2 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Repo- und Board-Link sowie Rollen Corrado/Armin sind dokumentiert.
- [ ] Einladungsweg und verfügbare Leserechte sind geprüft; tatsächliche Einladungen/Zugriff bleiben bis Durchführung offen.
- [ ] Planning-Mitteilung enthält Sprintziel, Umfang und MoSCoW-Prioritäten.
- [ ] Versand und Zugriffsbestätigung werden nach Durchführung erfasst.

## P06 – MVP-Review und Retrospektive durchführen

Als Projektverantwortlicher möchte ich den ersten Mehrwert prüfen und reflektieren, damit Sprint 2 auf tatsächlichen Erkenntnissen aufbaut.

Sprint 1; **Story Points: 2 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] MVP-Demo zeigt Testbasis, neue Ergänzung und CI-Nachweis; Soll/Ist ist dokumentiert.
- [ ] Release v0.1.0 wird nur nach erfüllter DoD erstellt und verlinkt.
- [ ] Review-Ergebnis und tatsächliches Feedback sind datiert; Review-Mitteilung wird vorbereitet.
- [ ] Retrospektive nennt mindestens eine konkrete Massnahme für Sprint 2; keine Durchführung vorwegnehmen.

## P07 – Tests mit versioniertem GHCR-Publish verbinden

Als Entwickler möchte ich geprüfte Commit-Images automatisch veröffentlichen, damit deploybare Versionen eindeutig nachvollziehbar sind.

Sprint 2; **Story Points: 8 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] pytest/HTTPX deckt die Antragsfälle einschliesslich Passwortprüfung und Uploadbegrenzung ab.
- [ ] Publish erfolgt nur nach erfolgreichen Hauptbranch-Tests; Commit-Tag und Digest sind nachvollziehbar.
- [ ] Drei erfolgreiche CI-/Publish-Läufe sind verlinkt.
- [ ] Ein absichtlicher Testfehler verhindert die Veröffentlichung; negativer Nachweis ohne produktive Beeinträchtigung.

## P08 – Lokale Kubernetes- und Helm-Zielumgebung vorbereiten

Als Betreiber möchte ich eine begründete lokale Zielumgebung, damit SetFlow reproduzierbar bereitgestellt werden kann.

Sprint 2; **Story Points: 8 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Cluster-Variante und Ressourcen sind begründet; Architektur und Wiederaufbau sind dokumentiert.
- [ ] Helm-Chart parametrisiert Image, Konfiguration und persistente Daten; keine Secrets im Git.
- [ ] Separater Projekt-Namespace und Kollisionsprüfung schützen den bestehenden Compose-Betrieb.
- [ ] Isolierte Helm-Installation und Health-Prüfung sind protokolliert; Kubernetes-API bleibt privat.

## P09 – Lokalen Deployment-Runner begrenzen

Als Betreiber möchte ich nur vertrauenswürdige Deployments zulassen, damit Runner und Cluster geschützt bleiben.

Sprint 3; **Story Points: 5 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Nur geschützte Hauptbranch-Deployment-Jobs laufen lokal; keine Pull-Request-Jobs.
- [ ] Kubernetes-Rechte sind auf den Projekt-Namespace begrenzt und nachvollziehbar geprüft.
- [ ] Secrets und Runner-Betrieb sind geschützt dokumentiert; öffentliche API-Freigabe ist nicht erforderlich.
- [ ] Tarif-/Branchschutzgrenzen sind geprüft und wirksame Umsetzung belegt.

## P10 – Deployments mit Smoke-Test und Rollback nachweisen

Als Betreiber möchte ich geprüfte Releases und einen Rückfall, damit Änderungen kontrolliert ausgeliefert werden.

Sprint 3; **Story Points: 8 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Drei aufeinanderfolgende Helm-Deployments verwenden geprüfte Images und bestehen automatischen /health-Smoke-Test.
- [ ] Commit, Image-Digest, Helm-Revision und Ergebnis jedes Laufs sind verlinkt.
- [ ] Eine frühere Version wird per Helm-Rollback wiederhergestellt und erfolgreich geprüft.
- [ ] Fehlerreaktion und Rückfall sind dokumentiert; Produktionsdaten bleiben geschützt.

## P11 – Datenerhalt und isolierten Restore nachweisen

Als Nutzer möchte ich meine Sets und Freigaben behalten, damit Pod-Wechsel und Wiederherstellung keine Daten verlieren.

Sprint 3; **Story Points: 8 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Testset, synthetische Audiodatei, Kommentar und Freigabelink bleiben nach Pod-Ersatz erhalten.
- [ ] Sicherung wird geprüft und in getrenntem Namespace/Volume wiederhergestellt.
- [ ] DB-Integrität, Datensatzanzahlen und Audio-SHA-256 stimmen mit der Sicherung überein.
- [ ] Nachweis und Rückfallplan sind dokumentiert; keine privaten Daten oder Backup-Archive im Git.

## P12 – MMP und Abschlussunterlagen vorbereiten

Als Projektverantwortlicher möchte ich Zielerreichung und Erkenntnisse nachvollziehbar abschliessen, damit die Arbeit beurteilt werden kann.

Sprint 3; **Story Points: 5 · MoSCoW: Must**.

Akzeptanzkriterien:

- [ ] Sprint-2- und Sprint-3-Planning, Review, Release und Retro werden nach tatsächlicher Durchführung nachgeführt.
- [ ] Soll/Ist aller Antragsziele, Testnachweise, Betrieb und Risiken sind verlinkt.
- [ ] Abgabeform, Quellen, erforderliche Hilfsmitteldeklaration und Präsentation sind nach gültigen Schulvorgaben geprüft.
- [ ] Vollständige Git-Historie und Dateistand werden vor öffentlicher Freigabe geprüft; Sichtbarkeitswechsel bleibt separate Aktion.

## P13 – App weiterentwickeln: Orange-Schwarz-Design und BPM-Bereiche über die CI-/Registry-Pipeline veröffentlichen

Als Nutzer möchte ich eine lesbare Orange-Schwarz-Oberfläche und BPM-Bereiche für meine Sets, damit SetFlow besser bedienbar ist und die neue Pipeline mit einer echten App-Änderung geprüft wird.

Sprint 2; **Story Points: 5 (vorläufig) · MoSCoW: Could**. Jira: SEM4-34.

Akzeptanzkriterien:

- [ ] Orange-Schwarz-Design mit lesbaren Texten, Statusmeldungen und Fokuszuständen auf Desktop und Smartphone; SetFlow-Titelbild bleibt erhalten.
- [ ] Einzelne BPM-Werte und aufsteigende Bereiche wie 127–150 lassen sich erfassen, speichern, bearbeiten und anzeigen; ungültige/umgekehrte Bereiche werden abgewiesen.
- [ ] Bestehende Sets und BPM-Einzelwerte bleiben erhalten; mehrere Genres per Kommatrennung bleiben nutzbar.
- [ ] Regressionstests prüfen BPM-Werte, Bereiche, ungültige Eingaben und bestehende Bedienabläufe.
- [ ] Die reale App-Änderung durchläuft Tests, Build und GHCR-Publish; Commit, Lauf und Image-Digest sind dokumentiert.

Nach P07/P08 und den Must-Zielen; praktische Erprobung der CI-/Registry-Pipeline.
Die vollständige Deploymentkette folgt in Sprint 3. BPM-Bereiche erweitern die
frühere Design-Story; deshalb von 3 auf 5 SP neu geschätzt.

## P14 – App weiterentwickeln: Mitwirkendenkonten über die vollständige CI/CD-Pipeline ausliefern

Als Betreiber möchte ich persönliche Mitwirkendenkonten über die vollständige Pipeline ausliefern, damit die Weiterentwicklung von der Codeänderung bis zum laufenden Dienst nachvollziehbar geprüft wird.

Sprint 3; **Story Points: 8 (vorläufig) · MoSCoW: Could**. Jira: SEM4-35.

Akzeptanzkriterien:

- [ ] Drei persönliche Konten können administrativ angelegt werden; keine öffentliche Registrierung.
- [ ] Mitwirkende können eigene Sets hochladen, bearbeiten, löschen und mit widerrufbaren Links freigeben.
- [ ] Sets anderer Konten können ohne Freigabe weder eingesehen noch verändert werden; das Administratorkonto kann alle Sets verwalten.
- [ ] Passwörter werden sicher gehasht gespeichert; Tests prüfen Anmeldung, Eigentumsrechte und Freigaben.
- [ ] Bestehende Sets bleiben bei der Datenmodelländerung erhalten; Sicherung und Migration sind geprüft.
- [ ] Tests, Image-Publish, Helm-Deployment und Smoke-Test durchlaufen die vollständige Pipeline; Commit, Digest und Helm-Revision sind nachvollziehbar.
- [ ] Datenerhalt und Rückfall auf die vorherige Version sind mit der Datenmodelländerung isoliert geprüft; Helm-Rollback und nötiger Datenrückfall sind getrennt beschrieben.

Am Ende von Sprint 3 nach P09–P11 und den übrigen Must-Zielen; nutzt die vollständige CI/CD-Lösung.

## Abhängigkeiten

Vorarbeit: P01 → P02; P05 begleitet die Einrichtung.
Sprint 1: P03 → P04 → P06.
P03/P04 → P07; P02 → P08; P07/P08 → P09 → P10 → P11.
P07 → P13; P09–P11 → P14. Optionale Erweiterungen folgen den Must-Zielen.
P12 begleitet Reviews und bündelt den Abschluss; Ergebnisse nicht erst am Ende dokumentieren.

Für jede Story gilt die [Definition of Done](Definition-of-Done.md).
Jira-Zuordnung und Übertragungsstand: [Jira-Abbildung](Jira-Abbildung.md).
