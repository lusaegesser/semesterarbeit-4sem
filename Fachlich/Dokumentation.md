# Fachliche Dokumentation

## 1. Ausgangslage und Vorleistungen

Bestehende Python-/FastAPI-Anwendung mit SQLite, Audio-Uploads bis 1 GB,
Admin-Anmeldung, Freigabelinks und zeitbezogenen Kommentaren.
Docker Compose, Backup/Restore und HTTPS auf dem ASUS-Projektlaptop sind vorbereitet
bzw. nach bisherigem Protokoll getestet. Eine erneute Bestandsprüfung ist für neue Nachweise nötig.

Die übernommene `.github/workflows/`-Konfiguration enthält bereits pytest und
einen Docker-Smoke-Test. Diese Automatisierung ist Vorleistung, keine neue
Semesterarbeitsleistung. Neue Arbeit umfasst die gezielte Weiterentwicklung und Nachweise.

## 2. Anforderungen und Abnahmekriterien

Aus dem final angenommenen Antrag übernehmen. Dessen Datei steht noch aus.
Arbeitsstand: Testarten/Funktionsabdeckung, Registry-Images mit Commit-Tag,
drei erfolgreiche Deployments, Smoke-Test, Rollback und isolierter Restore mit Prüfsummenvergleich.

## 3. Architektur und Entscheidungen

Ist-/Soll-Architektur und ausgewählte Kubernetes-Variante begründen.
[Entscheidungsprotokoll](../docs/entscheidungen.md).

## 4. Umsetzung

CI, Build/Registry, Helm, Runner und Deployment schrittweise dokumentieren.
Lokaler Runner nur für vertrauenswürdige Deployment-Jobs; keine öffentliche Kubernetes-API.

## 5. Tests und Nachweise

Für jeden Test Voraussetzung, Durchführung, Soll/Ist, Datum und Ergebnis festhalten.
Bereinigte Nachweise unter Nachweise/ ablegen. Keine privaten Audios oder Tokens.

## 6. Betrieb und Rückfall

Installation, Update, Start nach Windows-Anmeldung, Backup, Restore und Rollback dokumentieren.
Ein Laptop ist keine hochverfügbare Umgebung.

## 7. Soll-Ist-Vergleich

Zum Abschluss mit den genehmigten Zielen abgleichen.
