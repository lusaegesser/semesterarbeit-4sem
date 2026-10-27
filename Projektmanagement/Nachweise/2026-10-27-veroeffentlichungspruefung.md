# Prüfung vor öffentlicher Freigabe

Stand: 27.10.2026. Prüfung vor dem geplanten Sichtbarkeitswechsel.

## Umfang

Alle erreichbaren GitHub-Branches und Tags nach Fetch: 19 Commits, 137 eindeutige
Dateistände. Textdateien und XML-Inhalte des Word-Antrags wurden auf typische
Zugangsdaten, private Schlüssel, Passwort-Hashes, Kontaktdaten und Betriebsangaben
geprüft. Commit-Metadaten, PR-Texte und veröffentlichte Artefakte wurden gesichtet.

## Ergebnis

- Keine typischen Tokens, privaten Schlüssel oder gespeicherten Passwort-Hashes gefunden.
- Keine versionierten Datenbanken, privaten Audiodateien oder Backup-Archive gefunden.
- Frühere Commits enthalten Werkzeugnennungen und eine damalige öffentliche IP-Adresse.
- Der Word-Antrag enthält zusätzliche Namen, Kontaktadressen und historische Vorlagenmetadaten.
- Commit-Metadaten enthalten eine persönliche E-Mail-Adresse.
- Aktuelle Betriebsdateien enthalten interne Netzwerkadressen und den Anwendungsdomainnamen.
- Keine Releases, veröffentlichten Actions-Artefakte oder PR-Kommentare vorhanden.

## Entscheidung

Die aufgeführten historischen Angaben und Dokumentmetadaten werden beibehalten.
Die öffentliche Freigabe ist vorgesehen; eine Historienbereinigung erfolgt nicht.

## Grenzen

Eigenprüfung mit Mustervergleich und Sichtung; keine Garantie auf vollständige
Secret-Erkennung. Actions-Logs, GitHub-Caches und nicht mehr referenzierte
serverseitige Git-Objekte wurden nicht vollständig geprüft. Die Prüfung ist
keine Sicherheitsprüfung der öffentlich erreichbaren Anwendung.
