# Archivierter Zwischenstand vom 26.10.2026

Momentaufnahme vor der Neugliederung. Für aktuelle Aufgaben gilt der
[aktuelle Projektstand](../projektstand.md). Der Text dokumentiert den damaligen
Stand; Aussagen können inzwischen überholt sein.

## Aktueller Stand: Repository und Sprintplanung vorbereitet

- Antrag unter `Projektmanagement/Antrag/` abgelegt; Annahme durch Lukas bestätigt.
- Projektmanagementdozent: Corrado Parisi; Fachdozent: Armin Dörzbach.
- [Sprint-1-Dokumentation](../../Projektmanagement/00_Sprints/Sprint1/README.md),
  [Product Backlog](../../Projektmanagement/Backlog.md),
  [DoD](../../Projektmanagement/Definition-of-Done.md),
  [Risiken](../../Projektmanagement/Risiken.md) und
  [Anforderungsmatrix](../../Fachlich/Anforderungsmatrix.md) vorbereitet.
- Sprint 1: sechs Stories, 20 Punkte; vorläufig 22 Stunden plus 5 Stunden Reserve.
  Stundenbudget bleibt offen; kein endgültiges Commitment und kein Sprintstart.
- Jira SEM4, Board 67 über die Anbindung befüllt: drei Epics (SEM4-3 bis SEM4-5),
  zwölf Stories und 18 Sprint-1-Unteraufgaben. SEM4-1/SEM4-2 aktualisiert, keine
  doppelten Stories. Drei Sprints mit Zielen und Daten vorbereitet; alle ungestartet.
  [Ticketzuordnung](../../Projektmanagement/Jira-Abbildung.md).
- Sprint-Dokumentation anhand des von Lukas hochgeladenen Auszugs aus Semesterarbeit 2
  aufgebaut: Direktzugriffe, Inhaltsverzeichnis, Goal, Epics/Stories/Task-Tabellen,
  MoSCoW, Commitment/DoD und offene Review-/Retro-Abschnitte. Frühere Ergebnisse
  nicht als Ergebnisse von SetFlow übernommen.
- Lokale Arbeitsanweisungen bleiben auf dem Rechner und werden nicht weiter
  versioniert; öffentliche Dokumentation von lokalen Werkzeugbezeichnungen bereinigt.
  Frühere Commits bleiben unverändert. Vor öffentlicher Freigabe vollständige
  Historie und Dateistand prüfen. Noch keine Änderung der Sichtbarkeit.
- Bestehende fachliche Änderungen erhalten; keine App-Tests, Container oder
  Deployments in dieser PM-Vorbereitung ausgeführt. Kein Commit/Push vorgenommen.
- Prüfung der Vorbereitung: `git diff --check` ohne Fehler; lokale Linkziele in
  19 Markdown-Dateien vorhanden; Sprint-Sprungmarken gültig; sechs Sprint-1-Stories,
  18 Task-Zeilen und zehn beschriftete Tabellen vorhanden;
  zwölf eindeutige Backlog-IDs P01–P12;
  Ignore-Regeln und lokale Erhaltung der Arbeitsanweisungen bestätigt.
  Keine lokalen Werkzeugbezeichnungen mehr in den geprüften Hauptdokumenten,
  docs/ und .github/. Historie und GitHub-Einstellungen nicht abschliessend geprüft.
- Jira-Rückleseprüfung: 33 Vorgänge (drei Epics, zwölf Stories, 18 Unteraufgaben),
  Story-Punkte, Epic-/Task-Eltern und Sprintzuordnungen kontrolliert. Elf native
  «Blocks»-Links bestätigt. Alle Vorgänge «Zu erledigen», alle drei Sprints «future».
  Eine Zeitüberschreitung bei einer Verknüpfung wurde durch Rücklesen geklärt;
  keine doppelte Verknüpfung im abschliessenden Stand festgestellt.

### Als Nächstes

1. Zeitbudget klären und Sprintumfang bestätigen; danach Sprint 1 starten.
2. Dokumente prüfen und versionieren; Dozentenkonten und Einladungsweg klären.
3. Repo-/Board-Zugriffe ermöglichen, bestätigen lassen und Planning-Mitteilung versenden.
4. Offizielles Merkblatt A beschaffen und formelle Anforderungen abgleichen.

Die folgenden Abschnitte halten frühere Zwischenstände fest; offene Punkte zu
Antragsablage, Dozenten und Jira sind durch diesen aktuellen Stand ersetzt.

## Auftrag

Semesterarbeit 4: SetFlow, DevOps-Schwerpunkt. Antrag laut Lukas angenommen.
Zeitraum 26.10.2026–27.01.2027, drei Sprints, Jira, zentrale GitHub-Ablage.
Neue lokale Kopie: C:\repos\semesterarbeit-4sem.

## Vorbereitung abgeschlossen

- Originalrepository mit Historie übernommen, Original nicht verändert.
- Fachlich/ und Projektmanagement/ sowie Einstieg und Arbeitsregeln vorbereitet.
- Lokale Compose-/Caddy-Dateien übernommen, keine privaten Daten/Secrets kopiert.
- Vorhandene pytest-/Container-CI als Vorleistung erkannt.

## Historischer Betriebsstand (nicht heute erneut getestet)

ASUS A17 / Windows 11 Home / Docker Desktop mit WSL 2.
Produktive App im separaten Alt-Checkout C:\repos\dj-set-archive.
sets.luukeez.com mit Caddy/Let's Encrypt, Router TCP 80/443 auf Laptop.
Lokale IP war 192.168.178.47; öffentliche IP war dynamisch 178.193.53.47.
App-Volume war dj-set-archive-restore-6554df730ee3, .env nur im Alt-Checkout.
RustDesk für Fernzugriff; Docker startet nach Windows-Anmeldung.

## Offene Punkte vor der Planung (historischer Zwischenstand)

1. GitHub-Repository erstellt und origin verbunden; main erfolgreich gepusht: https://github.com/lusaegesser/semesterarbeit-4sem. Sichtbarkeit und Dozierenden-Zugriffe im GitHub-Konto prüfen.
2. Finale angenommene Antragsdatei und Fachdozent hinterlegen.
3. Jira-URL, Ticketpräfix, Zeitbudget und Definition of Done ergänzen.
4. Neues Repository auf Arbeitslaptop klonen und auf beiden Geräten als lokale Arbeitskopie öffnen.
5. Sprint 1 anhand tatsächlicher Vorleistungen planen; Testabdeckung und vorhandene CI prüfen.
6. GitHub-Berechtigungen/Branchschutz und Umsetzungsgrenzen des Tarifs prüfen.

## Damaliger nächster Schritt

Antrag/Jira ergänzen, Projekt auf beiden Laptops öffnen und Sprint-1-Planning durchführen.
Kein Kubernetes oder Deployment ohne abgegrenzte Aufgabe implementieren.

## Prüfung der Projektgrundlagen – 26.10.2026

Lokale Repository-Dokumentation und Richtlinienordner inhaltlich geprüft.
Ergebnisse und Grenzen: [Prüfung der Projektgrundlagen](../../Projektmanagement/Pruefung-Projektgrundlagen.md).
Ausgefüllter SetFlow-Antrag liegt im Richtlinienordner, jedoch ohne ausgefüllten
Genehmigungsentscheid und ohne Dozentenangaben. Finale angenommene Fassung im Repo
fehlt weiterhin. Merkblatt A war online nicht abrufbar; Merkblatt B betrifft die
Diplomarbeit, Anwendbarkeit noch klären. GitHub-Remote-Prüfung scheiterte an der
Netzwerk-/Namensauflösung. Keine Tests oder Deployments ausgeführt.
Nächste PM-Aufgabe: offizielle Grundlage/Antrag und Jira-Ticket ergänzen, danach
Sprint-1-Planning mit Kapazität, Sprintziel, Stories, Akzeptanzkriterien und DoD.

## Fachliche Bestandsaufnahme – 26.10.2026

Repository und externer Richtlinienordner geprüft; Ergebnisse und Prüfgrenzen:
[Fachliche Bestandsaufnahme](../../Fachlich/Bestandsaufnahme-2026-10-26.md).
Ausgefüllter Antrag im Richtlinienordner gefunden; finale angenommene Fassung im
Repository und Dozentenangabe bleiben offen. Ergänzungs-PDF ausgewertet;
offizielle verlinkte Merkblätter nicht inhaltlich abrufbar. GitHub-Serverstand und
Actions-Ergebnisse konnten nicht verifiziert werden. Keine Tests/Deployments ausgeführt.
Nächster fachlicher Schritt: Jira-Aufgabe zuordnen, finale Quellen klären und
Anforderungs-/Nachweismatrix erstellen; danach isolierte Test-/CI-Bestandsprüfung.
