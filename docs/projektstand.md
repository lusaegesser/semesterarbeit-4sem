# Projektstand – 26.10.2026

## Auftrag

Semesterarbeit 4: SetFlow, DevOps-Schwerpunkt. Antrag laut Lukas angenommen.
Zeitraum 26.10.2026–27.01.2027, drei Sprints, Jira, zentrale GitHub-Ablage.
Neue lokale Kopie: C:\repos\semesterarbeit-4sem.

## Vorbereitung abgeschlossen

- Originalrepository mit Historie übernommen, Original nicht verändert.
- Fachlich/ und Projektmanagement/ sowie Einstieg und Codex-Regeln vorbereitet.
- Lokale Compose-/Caddy-Dateien übernommen, keine privaten Daten/Secrets kopiert.
- Vorhandene pytest-/Container-CI als Vorleistung erkannt.

## Historischer Betriebsstand (nicht heute erneut getestet)

ASUS A17 / Windows 11 Home / Docker Desktop mit WSL 2.
Produktive App im separaten Alt-Checkout C:\repos\dj-set-archive.
sets.luukeez.com mit Caddy/Let's Encrypt, Router TCP 80/443 auf Laptop.
Lokale IP war 192.168.178.47; öffentliche IP war dynamisch 178.193.53.47.
App-Volume war dj-set-archive-restore-6554df730ee3, .env nur im Alt-Checkout.
RustDesk für Fernzugriff; Docker startet nach Windows-Anmeldung.

## Noch offen

1. Privates GitHub-Repository semesterarbeit-4sem erstellen und origin verbinden/pushen.
2. Finale angenommene Antragsdatei und Fachdozent hinterlegen.
3. Jira-URL, Ticketpräfix, Zeitbudget und Definition of Done ergänzen.
4. Neues Repository auf Arbeitslaptop klonen und auf beiden Geräten als lokales Codex-Projekt öffnen.
5. Sprint 1 anhand tatsächlicher Vorleistungen planen; Testabdeckung und vorhandene CI prüfen.
6. GitHub-Berechtigungen/Branchschutz und Umsetzungsgrenzen des Tarifs prüfen.

## Nächster Schritt

GitHub-Ablage fertigstellen, danach Antrag/Jira ergänzen und Sprint-1-Planning durchführen.
Kein Kubernetes oder Deployment ohne abgegrenzte Aufgabe implementieren.
