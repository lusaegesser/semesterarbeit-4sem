# Titelbild in der laufenden App

Am 04.11.2026 wurden nur Startseite, ergänzende Bild-CSS-Regeln und Titelbild
in den bisherigen Betriebscheckout übernommen. Das vollständige Redesign bleibt P13.

Die alten Frontenddateien liegen lokal unter `backups/branding-before-20261104/`.
Das bisherige Image bleibt als `dj-set-archive-app:before-setflow-branding-20261104`
erhalten. Das App-Image wurde neu gebaut und nur der App-Service ersetzt;
Compose-Konfiguration, Ports, Datenvolume und HTTPS-Proxy blieben unverändert.

## Prüfung

- Laufender Health-Endpunkt liefert `status: ok`.
- Startseite enthält den SetFlow-Bildkopf.
- Banner liefert HTTP 200 mit `image/png`; SHA-256 entspricht der Repository-Datei.
- Derselbe Datenmount ist nach dem Containerwechsel aktiv; Proxy nicht neu gestartet.
- Ein isolierter Vorabprüfbefehl scheiterte an Shell-Quoting, bevor Prüfungen liefen.
  Die genannten HTTP-Prüfungen erfolgten erfolgreich nach dem Containerwechsel.

## Rückfall

Alte Frontenddateien aus der lokalen Sicherung zurückkopieren, das gesicherte Image
als `dj-set-archive-app:latest` taggen und nur `app` mit `--no-build --no-deps`
neu erstellen. Das Datenvolume bleibt dabei erhalten. Kein Restore erforderlich.

Keine Datenmigration und kein neuer CI/CD-Pipeline-Nachweis durch diese manuelle Aktualisierung.
