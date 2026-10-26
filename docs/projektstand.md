# Projektstand – 26.10.2026

[Startseite](../README.md) · [Projektmanagement](../Projektmanagement/README.md) ·
[Fachlicher Teil](../Fachlich/README.md) · [Entscheidungen](entscheidungen.md)

## Auftrag und Grundlagen

SetFlow, Semesterarbeit 4 mit DevOps-Schwerpunkt; Zeitraum 26.10.2026–27.01.2027.
Die Annahme des [Antrags](../Projektmanagement/Antrag/README.md) hat Lukas bestätigt.
Projektmanagementdozent: Corrado Parisi. Fachdozent: Armin Dörzbach.

## Erledigt

- Vorprojekt mit Git-Historie übernommen; App, Tests, vorhandene CI und bisherige
  Betriebsverfahren als Vorleistungen ausgewiesen. Produktiver Alt-Checkout unberührt.
- Dokumentation anhand Semesterarbeit 2 neu gegliedert: Startseite,
  [PM-Hauptdokument](../Projektmanagement/README.md),
  [fachliches Hauptdokument](../Fachlich/README.md), Sprintübersicht sowie
  Anhang-, Bilder-, Medien- und Nachweisablagen mit Navigation.
- [Sprint 1](../Projektmanagement/00_Sprints/Sprint1/README.md) mit Goal, Epics,
  sechs Stories, 18 Tasks, MoSCoW, Commitment-Vorschlag und offenen Review-/Retro-Abschnitten
  vorbereitet. Sprint 2/3 haben eigene als Grobplanung bezeichnete Seiten.
- Backlog, DoD, Risikoregister und Anforderungsmatrix angelegt und verlinkt.
- Jira befüllt und zurückgelesen: drei Epics (SEM4-3 bis SEM4-5), zwölf Stories,
  18 Unteraufgaben und elf native Blockierungslinks. Drei Sprints mit Zielen und
  geplanten Daten; alle Vorgänge «Zu erledigen», Sprints ungestartet.
  [Ticketzuordnung](../Projektmanagement/Jira-Abbildung.md).
- Lokale Arbeitsanweisungen bleiben ignoriert; bisherige Dokumentationspfade
  führen auf die neuen Hauptdokumente weiter. Code- und Deploymentpfade bleiben bestehen.
- [Git-Workflow](../CONTRIBUTING.md) gemäss DevOps-Unterricht für Einzelarbeit
  dokumentiert. Publikationsweg: fünf logische Conventional Commits auf
  `feature/SEM4-1-projektgrundlagen` mit Pull Request nach `main`.

## Offen und Prüfgrenzen

- Stundenbudget ist offen. Sprint 1 umfasst vorläufig 20 Punkte bzw. 22 Stunden
  plus 5 Stunden Reserve; endgültiges Commitment und Sprintstart stehen aus.
- GitHub-API bestätigt privates Repository, Hauptbranch `main` und Schreibrechte.
  Für `main` wurde keine Branchschutz-Konfiguration abgerufen (HTTP 404).
  Aktuelle CI-Ergebnisse und Integration sind am Pull Request zu prüfen;
  ein offener PR ist keine bereits erfolgte Integration oder Abnahme.
- Dozentenkonten, Einladungen, Zugriffsbestätigungen und tatsächliche Teams-Mitteilungen
  fehlen noch. Ein Kommunikationsentwurf ist vorbereitet.
- Offizielles Merkblatt A und Anwendbarkeit weiterer Form-/Bewertungsvorgaben
  müssen abgeglichen werden.
- Neue Test-/CI-Bestandsprüfung und technische Umsetzung stehen aus.
  Die Dokumentationsaufgaben haben keine App-Tests, Container, Restore-Vorgänge
  oder Deployments ausgeführt.
- Vor öffentlicher Freigabe Dateistand und vollständige Git-Historie prüfen.
  Frühere Commits bleiben vorerst unverändert.
- Übernommene HTTPS-Unterlagen enthalten unterschiedliche historische Statusangaben.
  Aktuellen Betrieb erst im Rahmen einer beauftragten Bestandsprüfung bestätigen.

## Prüfung dieser Strukturänderung

Inhalt und Dateistruktur der Semesterarbeit 2 bei Commit
`7ed6b81d48abbcbc13c2a61d45b44804f8a8b2fe` über Git gelesen.
Navigation und Hauptgliederung als Vorbild verwendet; Ergebnisse, Medien und
Codeversionen der früheren Arbeit wurden nicht übernommen.

Lokale Linkprüfung einschliesslich Git-Workflow abgeschlossen: 37 Markdown-Dateien,
223 lokale Verweise,
keine fehlenden Ziele oder defekten Sprungmarken. `git diff --check` ohne Fehler;
Code-, Test- und Deploymentdateien durch die Strukturänderung unverändert.
Gezielte Prüfung typischer Secret-Muster ohne Treffer; Antrags-DOCX ohne VBA.
Historische Detailstände bleiben im [Archiv](archiv/README.md) nachvollziehbar.

## Nächste Schritte

1. Stundenbudget klären, Sprintumfang bestätigen und Sprint 1 starten.
2. PR und CI prüfen, Integration abschliessen; Dozentenkonten und Einladungsweg klären.
3. Repo-/Board-Zugriffe ermöglichen und bestätigen lassen; Planning-Mitteilung versenden.
4. P03 / SEM4-6: vorhandene Tests und CI mit isolierten Daten prüfen.
5. Formvorgaben vervollständigen und tatsächliche Nachweise laufend nachführen.

## Historische Grundlagen

[Archivierter Zwischenstand vom 26.10.2026](archiv/projektstand-2026-10-26-vor-neugliederung.md) ·
[Betriebsunterlagen und Vorprojektprotokolle](README.md#vorprojekt-und-historischer-betrieb) ·
[Bestandsaufnahme](../Fachlich/Bestandsaufnahme-2026-10-26.md)

Historische IPs, Volumenamen und Testergebnisse sind keine neu bestätigten Betriebsnachweise.
