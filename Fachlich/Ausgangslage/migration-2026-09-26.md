# Migration von Python zu Docker · 26.09.2026

- Ausgangsbestand: 0 Sets, 0 Kommentare, 0 Freigaben und 2 Sitzungen.
- Administrator-Passwort-Hash übernommen; Passwort nicht geändert.
- Python-Prozess auf Port 8000 beendet; App durch Docker Compose ersetzt.
- Vollständige Sicherung vor dem Wechsel unter `backups/python-before-docker-20260926.zip`.
- Wiederherstellung in ein neues, eigenes Docker-Volume.
- Weitere Docker-Sicherung erstellt, geprüft und erneut in ein neues Volume zurückgespielt.
- Datenbankinhalte und Datensatzanzahlen mit der ursprünglichen Sicherung verglichen: identisch.
- Passwort-Datei per SHA-256 verglichen: identisch. SQLite-Dateiheader können beim Backup wechseln; deshalb zusätzlich logischer Datenvergleich.
- `/health` erfolgreich; Administrator-Passwort als eingerichtet erkannt.
- Vorherige Ablage und vorheriges Docker-Volume als Rückfall behalten.

Mit separaten Testdaten geprüft: Wiederherstellung von Set, Audioaufnahme,
Kommentar und Passwort-Hash; beschädigte Archive und unsichere Pfade werden abgewiesen.
20 automatisierte Tests bestanden; der Docker-Test prüft ebenfalls Backup/Restore.

Sicherungen liegen bislang auf demselben Laptop. Ein externer Sicherungsort
und ein automatischer Zeitplan sind noch nicht eingerichtet.
