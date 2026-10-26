# Git-Workflow und Zusammenarbeit

[Startseite](../README.md) · [Projektmanagement](../Projektmanagement/README.md)

SetFlow wird als Einzelprojekt bearbeitet. Grundlage ist
der Unterricht [Tag 02 – Git und Versionskontrolle](https://ch-tbz-wb.gitlab.io/Stud/devops/0_Organisatorisches/Tagesplanungen/Tag02/),
abgeglichen am 26.10.2026. Die Übungen zu Teamarbeit werden auf eine reale
Einzelarbeit übertragen; fremde Reviews oder Konflikte werden nicht simuliert
und als echte Projektereignisse ausgewiesen.

## Branching-Strategie

Wir verwenden einen schlanken GitHub Flow: `main` enthält den integrierten Stand;
Änderungen entstehen auf kurzen Aufgabenbranches und werden über Pull Requests
zusammengeführt. Ein zusätzlicher dauerhafter `develop`-Branch ist bei einer
Person und drei Sprints nicht erforderlich.

Branch-Namen enthalten Jira-Kennung und Thema:

- `feature/SEM4-1-projektgrundlagen` für Aufgaben und Dokumentation.
- `bugfix/SEM4-42-beschreibung` für Fehlerkorrekturen.
- `hotfix/SEM4-42-beschreibung` für beauftragte dringende Betriebskorrekturen.

Die Kennung `SEM4-42` ist ein Formatbeispiel, kein vorhandener Vorgang.
Änderungen werden über Aufgabenbranches abgestimmt.

## Arbeitsablauf

1. `git status` prüfen und lokale Änderungen erhalten. Bei sauberem Arbeitsbaum
   `git fetch origin` und `git pull --ff-only` auf `main` ausführen.
2. Jira-Aufgabe auswählen, Scope und Akzeptanzkriterien lesen; Aufgabenbranch erstellen.
3. Kleine logische Änderungen umsetzen. Nur zugehörige Dateien explizit stagen.
4. `git diff` und `git diff --cached` prüfen; erforderliche Tests und Nachweise durchführen.
5. Conventional Commits erstellen und Branch zu `origin` pushen.
6. Pull Request mit Problem, Änderung, Jira-Bezug, Prüfungen und Grenzen erstellen.
7. Gesamten Diff selbst prüfen und CI-Ergebnisse beurteilen. Eigenprüfung als solche
   benennen. Ein unabhängiges Review nur bei tatsächlicher Durchführung dokumentieren.
8. Nach erfüllten Kriterien integrieren, gemeinsamen Stand synchronisieren und Jira
   anhand der tatsächlichen Definition of Done pflegen.

Das Erstellen eines PR oder ein erfolgreicher Push allein erfüllt noch keine
fachliche Abnahme. Ein offener PR wird nicht als gemergt bezeichnet.

## Commit-Konvention

Format: `type(scope): SEM4-N konkrete Änderung`.

- `docs` für Dokumentation, `test` für Tests, `feat` für neue Funktionalität,
  `fix` für Fehler, `refactor` für Umstrukturierung und `chore` für Repositorypflege.
- Ein Commit beschreibt eine logische Änderung. Vorleistungen und neue Leistungen
  bleiben erkennbar. Keine künstlichen Änderungen für eine Commit-Anzahl erzeugen.
- Kurzer Betreff; bei Bedarf ein Body mit Begründung und relevanten Grenzen.

Beispiel: `docs(sprints): SEM4-1 Sprintplanung und Tasks vorbereiten`.

## Pull Requests und Merge

Änderungen und Integration liegen bei der Projektleitung. Für das Einzelprojekt sind keine
unabhängigen Mindestfreigaben als durchgeführt vorausgesetzt. Falls später weitere
Personen beitragen, werden Review-Regeln entsprechend erweitert.

Standard ist der Merge-Commit, damit die kleinen inhaltlichen Commits im PR
erhalten bleiben. Squash eignet sich für noch nicht bereinigte Zwischenstände.
Rebase nur auf einem eigenen, nicht gemeinsam verwendeten Branch und ohne
ungeprüftes Umschreiben veröffentlichter Historie.

Branchschutz und tatsächlich erzwingbare Checks hängen von den GitHub-Einstellungen
und dem Tarif ab; die Konfiguration ist separat zu prüfen. Dokumentierte Regeln
werden nicht als bereits technisch erzwungen ausgegeben.

## Prüfungen

Die Testbefehle werden in `Fachlich/Anwendung/` ausgeführt.
Reine Dokumentation: Inhalte, lokale Links, Sprungmarken, Dateien und
`git diff --check` prüfen. Technische Änderungen: relevante pytest-/Container-
und Pipeline-Prüfungen gemäss [Definition of Done](../Projektmanagement/Definition-of-Done.md).
Die vorhandene CI läuft bei Push und Pull Request; ihr Ergebnis wird verlinkt.
Eine nicht ausgeführte oder fehlgeschlagene Prüfung bleibt sichtbar.

Keine produktiven Compose-Starts, Deployments oder Restores allein durch einen
Git-Workflow ausführen. Technische Tests verwenden eigene Daten und Umgebungen.

## Ignorierregeln

`.gitignore` schliesst Secrets und `.env`, lokale Arbeitsanweisungen,
virtuelle Umgebungen, Caches, generierte Dateien, Datenbanken, Uploads und Backups aus.
Diese Dateien enthalten lokale Zustände, reproduzierbare Ausgaben oder private Daten.
`.env.example` darf ausschliesslich bereinigte Beispielwerte enthalten.
Bereits versionierte Dateien werden durch eine neue Ignore-Regel nicht rückwirkend
aus der Historie entfernt. Vor einer öffentlichen Freigabe wird die Historie geprüft.

## Konflikte und Rückfall

Bei Konflikten beide Änderungen verstehen, gezielt zusammenführen und erneut prüfen.
Relevante Entscheidungen werden im PR bzw. Entscheidungsprotokoll erklärt.
Veröffentlichte Änderungen bei Bedarf mit `git revert` nachvollziehbar rückgängig machen.
Kein Force-Push auf `main` und kein automatisches Verwerfen lokaler Änderungen.

## Versionierung und Releases

Versionen folgen SemVer: Major für inkompatible Änderungen, Minor für neue
rückwärtskompatible Funktionalität, Patch für Fehlerkorrekturen. Während der
Weiterentwicklung sind `0.x.y`-Stände möglich; der vorgeschlagene erste
Semesterarbeits-MVP ist `v0.1.0` nach tatsächlicher Abnahme.

Ein Release benötigt einen geprüften integrierten Git-Stand, Nachweise und Release
Notes mit Änderungen, Prüfungen, Einschränkungen und Betriebs-/Rückfallhinweisen.
Die Projektleitung verantwortet annotierten Tag und GitHub-Release. Es wird kein Übungs-Release
aus dem Unterricht als erfolgreiches SetFlow-MVP ausgegeben.
