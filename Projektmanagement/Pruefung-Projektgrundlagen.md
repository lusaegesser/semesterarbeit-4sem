# Prüfung der Projektgrundlagen vom 26.10.2026

Nachtrag vom 26.10.2026: Antrag liegt inzwischen unter [Antrag/](Antrag/).
Corrado Parisi begleitet Projektmanagement, Armin Dörzbach das Fachliche.
Jira SEM4, Board 67 ist erreichbar. Der folgende Text hält die ursprüngliche
Prüfung fest; aktueller Stand in [Sprint-1-Planning](Sprint-1-Planning.md)
und [Jira-Abbildung](Jira-Abbildung.md).

## Umfang und Nachweisgrenzen

Geprüft wurden der lokale Git-Stand, README.md, docs/, die fachliche
und PM-Dokumentation, der vorhandene Testworkflow sowie die vier Dateien unter
`C:\Users\Lukas\Documents\richtlinien sem arbeit`.
Der Arbeitsstand war vor der Prüfung sauber. origin verweist auf
https://github.com/lusaegesser/semesterarbeit-4sem.git.
Die Remote-Abfrage scheiterte an der Netzwerk-/Namensauflösung. Synchronität mit
GitHub, Sichtbarkeit, Berechtigungen, Branchschutz und aktuelle Workflow-Ergebnisse
sind damit nicht geprüft. Es wurden keine App-Tests oder Betriebsbefehle ausgeführt.

## Richtlinien und Antrag

- `Ergaenzungen_Semesterarbeiten_ITCNE.pdf`: vollständig textlich geprüft (14 Seiten).
  Das Dokument bezeichnet sich ausdrücklich als Ergänzung mit Empfehlungen und
  ersetzt die offiziellen Merkblätter nicht. Es beschreibt mindestens drei Sprints,
  regelmässige Releases, Einsicht für Dozierende und proaktive Kommunikation.
  Ein fachliches und ein PM-Hauptdokument sind ausdrücklich erlaubt (Seite 7).
  User Stories, Akzeptanzkriterien, gemeinsame DoD, Planning, Review und Retrospektive
  sowie nachvollziehbare Tests und Reflexionen sind zentrale Orientierungspunkte.
  MoSCoW, Fibonacci-Schätzungen und ein Meilenstein-Gantt werden empfohlen.
  Videos und Einzelbesprechungen sind nicht verpflichtend. Die Aussage zur
  Nichtbenotung von Sprint 1 stammt aus dieser Ergänzung und ist noch mit den
  offiziellen Semesterarbeitsvorgaben abzugleichen.
- `ITCNE25_Semesterarbeit 4 (Einreichungsformular) v2.docx`: ausgefüllter SetFlow-Antrag.
  Termine und DevOps-Ausrichtung stimmen mit README und Sprintplan überein.
  Genehmigungsfeld, Datum und Dozentenunterschrift sind nicht ausgefüllt.
  Die Datei belegt daher allein keine formelle Genehmigung; Lukas hat die Annahme
  laut bisheriger Projektdokumentation bestätigt. Finale angenommene Fassung fehlt
  weiterhin unter `Projektmanagement/Antrag/`.
- `Merkblatt A.url`: verweist auf
  https://gitlab.com/ch-tbz-wb/general/semarbeit/-/blob/ITCNE25/Merkblatt-A-4-SemArbeit.md.
  Inhalt konnte bei dieser Prüfung weder über die verlinkte Seite noch den Raw-Link
  abgerufen werden. Offizielle Abgabe-, Form- und Bewertungsvorgaben bleiben offen.
- `Merkblatt B.url`: verweist auf
  https://gitlab.com/ch-tbz-wb/general/diparbeit/-/blob/main/Merkblatt-B.md.
  Der Raw-Inhalt war abrufbar und trägt den Titel «Diplomprüfung Merkblatt B»,
  Stand September 2024. Keine pauschale Übernahme der Diplomarbeitsvorgaben:
  Anwendbarkeit anhand Merkblatt A bzw. mit den Dozierenden klären.

## Abgleich und offene Punkte

1. **Arbeitsumfang dieses Chats:** Projektmanagement. Die Arbeitsweise sieht abgegrenzte Jira-Aufgaben vor. Jira-URL und Ticketkennung fehlen;
   Folgeaufgaben vor Umsetzung einem konkreten Ticket zuordnen.
2. **Antragsziele präzisieren:** Die fachliche Kurzfassung nennt drei erfolgreiche
   Deployments, lässt aber die drei erfolgreichen CI-Durchläufe und den gezielt
   fehlschlagenden Test aus dem vorliegenden Antrag noch aus. Ebenfalls verbindlich
   abzugleichen: Commit-Tag, Publish-Sperre bei Fehlern, drei aufeinanderfolgende
   Deployments, Helm-Rollback und getrennte Datenerhalt-/Restore-Nachweise.
3. **Sprint 1 konkretisieren:** Sprintziel, priorisierte User Stories mit
   Akzeptanzkriterien, Schätzungen, Kapazität/Zeitbudget, Commitment und gemeinsame
   Definition of Done fehlen. Sprinttermine sind dokumentiert, jedoch kein Nachweis
   eines bereits durchgeführten Plannings.
4. **Stakeholder und Kommunikation:** Fachdozent, Board-Link, Zugriffsprüfung und
   tatsächliche Planning-/Review-Mitteilungen fehlen. Antrag sieht Teams-Information
   nach jedem Planning und Review vor. Nur Entwürfe erstellen; Versand durch Lukas,
   sofern nicht ausdrücklich anders beauftragt.
5. **Risiken und Nachweise:** Bisher nur Risikostichworte. Bewertung mit
   Wahrscheinlichkeit, Auswirkung, Massnahmen und Verantwortlichkeit ergänzen.
   Quellen-/KI-Nachweis, Bild-/Tabellenbeschriftungen und zugehörige Verzeichnisse
   bei Erstellung der Abgabedokumentation berücksichtigen.
6. **Dokumentkonsistenz:** Gegenseitige direkte Links zwischen PM- und fachlichem
   Hauptdokument fehlen noch. `docs/https-operations.md` bezeichnet HTTPS als noch
   nicht aktiviert; `docs/projektstand.md` beschreibt einen historischen produktiven
   HTTPS-Betrieb. Historischen Status bei einer technischen Bestandsaufnahme klären;
   aus dieser Dokumentprüfung keinen neuen Betriebsnachweis ableiten.
7. **Vorleistungen:** Der vorhandene Workflow führt pytest und einen Container-Test
   aus. Registry-Veröffentlichung und Helm-Deployment sind darin nicht enthalten.
   Vorhandene App, Tests und Workflow weiterhin als Vorleistung ausweisen.

## Nächster Schritt

Offizielles Merkblatt A und finale angenommene Antragsfassung verfügbar machen,
Jira-Ticket und Beteiligte ergänzen. Danach Sprint-1-Planning mit Kapazität,
Sprintziel, Backlog und DoD als eigene abgegrenzte PM-Aufgabe ausarbeiten.
Keine Architekturentscheidung oder Änderung am laufenden Betrieb aus dieser Prüfung.
