# Zusammenarbeit an SetFlow / Semesterarbeit 4

## Vor jeder Aufgabe

- README.md, docs/projektstand.md und relevante Dokumentation lesen.
- Git-Status prüfen und fremde/lokale Änderungen erhalten.
- Angenommenen Antrag unter Projektmanagement/Antrag/ berücksichtigen, sobald vorhanden.
- Deutsch mit Schweizer Rechtschreibung, knapp und nachvollziehbar erklären.
- Pro Chat eine abgegrenzte Jira-Aufgabe bearbeiten; keine unabhängigen Themen beimischen.

## Umfang

DevOps ist Schwerpunkt: bestehende CI erweitern, versionierte Images, Registry,
Deployment mit lokalem Runner und Helm, Smoke-Test, Rollback und Datenerhalt.
Jira: drei Sprints. GitHub: gemeinsame Ablage für Code und Dokumentation.
Projektmanagement und fachliche Dokumentation getrennt, gegenseitig verlinkt.
Die persönliche Website luukeez.com ist ausserhalb dieses Projekts.

## Laufenden Betrieb schützen

- Produktiver Alt-Checkout C:\repos\dj-set-archive bleibt unberührt, bis eine konkrete
  Umstellung beauftragt ist. Vorliegende Erlaubnis im Chat berücksichtigen.
- Keine Compose-Starts, Restore-Vorgänge oder Deployments aus diesem neuen Checkout
  ohne Prüfung von Compose-Projektname, Ports und Volumenamen auf Kollisionen.
- Tests mit isolierten Daten/Volumes/Namespaces ausführen.
- Keine Prune-Befehle, kein down -v, kein Überschreiben bestehender Daten.
- Vor risikobehafteten Datenänderungen geprüfte Sicherung und Rückfallplan vorsehen.
- Keine Änderungen an Router, DNS, WordPress oder Fernwartung ohne Aufgabenbezug.

## Datenschutz und Nachweise

- Keine Secrets, .env, Passwort-Hashes, Tokens, kubeconfigs, privaten Audiodateien oder
  Backup-Archive einchecken. Screenshots/Logs vor Ablage bereinigen.
- Technische Behauptungen und Tests am tatsächlichen Stand prüfen.
- Vorhandene App, Tests und GitHub-Workflows als Vorleistungen ausweisen.
- Keine Tests, Reviews, Besprechungen oder Jira-Aktivitäten erfinden/nachdatieren.
- Nachrichten an Dozierende nur entwerfen, sofern Versand nicht ausdrücklich beauftragt ist.

## Abschluss jeder Aufgabe

- Relevante Prüfungen durchführen, Ergebnis und Grenzen dokumentieren.
- docs/projektstand.md mit Erledigtem, offenen Punkten und nächstem Schritt aktualisieren.
- Wesentliche Architekturentscheidungen in docs/entscheidungen.md nachtragen.
- Fachliche bzw. PM-Dokumentation bei fachlich relevanten Änderungen aktualisieren.
- Nicht automatisch committen/pushen, sofern dies nicht durch den Auftrag autorisiert ist.
