# HTTPS fuer sets.luukeez.com

Vorbereitet am 09.10.2026. Noch nicht oeffentlich aktiviert.

Die normale App bleibt lokal unter http://127.0.0.1:8000 erreichbar.
Caddy ist im optionalen Compose-Profil `https` und startet erst bei Aktivierung.
Seine Ports binden ausschliesslich an 192.168.178.47. Zertifikate liegen im
dauerhaften caddy-data-Volume. Zugriffslogs bleiben deaktiviert, damit Freigabetokens
nicht protokolliert werden. Das Caddy-Image ist per Digest festgelegt.

## Vor Aktivierung

- DNS A sets.luukeez.com muss auf die aktuelle oeffentliche IPv4 zeigen.
- Vorhandene AAAA- und CAA-Eintraege pruefen; keine unpassende IPv6-Adresse verwenden.
- Router-Zuordnung 192.168.178.47 muss reserviert bleiben.
- Router TCP 80 -> 192.168.178.47:80 und TCP 443 -> 192.168.178.47:443.
- Windows-Firewall: gezielte eingehende TCP-Freigaben fuer 80/443 vorbereiten.
- Keine DMZ, keine Freigabe von Port 8000, keine Aenderung an Telefonie/UDP.
- Sicherung separat vom Laptop aufbewahren.

## Aktivierung (erst nach gemeinsamer Pruefung)

Im Projektordner C:\repos\dj-set-archive:

1. In der vorhandenen .env COOKIE_SECURE=true setzen. ARCHIVE_VOLUME und
   ARCHIVE_VOLUME_EXTERNAL unveraendert lassen.
2. `docker compose --profile https up -d app caddy`
3. `docker compose logs --tail 40 caddy` auf erfolgreiche Zertifikatsausstellung pruefen.
4. Ueber Mobilfunk https://sets.luukeez.com pruefen: Zertifikat, Anmeldung,
   Audio-Teilabruf, Kommentare und Freigabelink. HTTP muss auf HTTPS umleiten.
5. Eingehenden und ausgehenden Telefonanruf testen.

Es wird kein ARCHIVE_TLS im produktiven Betrieb gesetzt. Caddy beschafft das
oeffentliche Zertifikat automatisch, sobald DNS und Erreichbarkeit stimmen.
Ein lokales Testzertifikat bestaetigt diese oeffentliche Erreichbarkeit nicht.

## Sicherung und Rueckfall

`python scripts/manage.py backup` funktioniert weiter mit dem bestehenden
Archivvolume. Python muss auf dem Host verfuegbar sein; aktuell wurde fuer diese
Verwaltungsbefehle eine lokal bereitgestellte Python-Laufzeit verwendet.
Die App-Sicherung enthaelt keine Caddy-Zertifikate. Deren Verlust erfordert eine
erneute Zertifikatsausstellung; das caddy-data-Volume deshalb erhalten.

Zum Abschalten des externen Zugriffs Routerregeln deaktivieren/entfernen und
`docker compose --profile https stop caddy` ausfuehren.
Fuer reinen lokalen HTTP-Betrieb COOKIE_SECURE=false in .env setzen und
`docker compose up -d app` ausfuehren. Datenvolume nicht wechseln oder loeschen.

Keine `down -v`- oder Prune-Befehle verwenden.
Docker Desktop startet nach Windows-Anmeldung; unbeaufsichtigter Start ohne
Anmeldung ist weiterhin nicht eingerichtet.
Bei Ausfall externe IPv4 mit DNS-Ziel vergleichen: sie ist dynamisch.
