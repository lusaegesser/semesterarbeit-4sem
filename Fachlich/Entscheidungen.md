# Entscheidungsprotokoll

## 26.10.2026 – Gemeinsames Repository

Code, Pipeline und Dokumentation werden im Repository `semesterarbeit-4sem`
geführt. Die Git-Historie und die Vorleistungen der Anwendung bleiben erhalten.
Der bisherige produktive Betrieb bleibt bis zu einer gesonderten Umstellung bestehen.

## 26.10.2026 – Technische Zielumgebung

GitHub-gehostete Runner übernehmen Tests und Image-Builds. GHCR speichert
Commit-gekennzeichnete Images. Ein lokaler Runner deployt mit Helm in einen
lokalen Kubernetes-Cluster. Die Kubernetes-API bleibt privat.
Die Cluster-Variante wird bei der Umsetzung begründet.

## 26.10.2026 – Dokumentationsstruktur

Die Startseite verlinkt die Hauptbereiche Projektmanagement und Fachliches.
Sprintberichte enthalten Planning, Review und Retrospektive.
Details und Nachweise werden in den jeweiligen Bereichen geführt.

## 26.10.2026 – Technische Ablage

App, Oberfläche, Tests, Skripte und Containerdateien liegen gemeinsam unter
`Fachlich/Anwendung/`. Dadurch bleiben ihre relativen Pfade und der
Docker-Buildkontext konsistent. Die GitHub-Workflows verwenden diesen Arbeitsordner.
Eine pytest-Konfiguration hält die Importpfade auch beim gezielten Testaufruf stabil.

Compose erhält das Projekt `setflow-semesterarbeit` und das Standardvolume
`setflow-semesterarbeit-data`, um die bisherige Datenablage nicht versehentlich
zu verwenden. Bestehende Betriebsdaten werden durch diese Änderung nicht migriert.

## 26.10.2026 – GitHub Flow

Kurze Aufgabenbranches, Conventional Commits und Pull Requests bilden den
Änderungsprozess. Eigenprüfung und unabhängiges Review werden unterschieden.
Releases folgen nach tatsächlicher Abnahme. Die Regeln stehen unter
`.github/CONTRIBUTING.md`.

## 23.11.2026 – Publish nach geprüften Hauptbranch Tests

Der vorhandene Workflow wird um einen abhängigen GHCR-Job erweitert.
Publish setzt erfolgreiche pytest- und Container-Jobs sowie `main` im eigenen
Repository voraus. Nur dieser Job erhält Package-Schreibrechte; Anmeldung mit
`GITHUB_TOKEN` statt persönlichem Token. Vollständiger Commit-Tag, laufbezogener
Tag und Digest verbinden Quellstand, Lauf und Image. Für spätere Deployments
ist der Digest massgeblich, da ein erneuter Build einen Commit-Tag verändern kann.

Ein manueller Hauptbranch-Lauf kann einen temporären pytest-Fehler einschalten.
Der Publish-Pfad bleibt grundsätzlich derselbe; ausschliesslich die fehlgeschlagene
Testabhängigkeit verhindert Publish. Dadurch muss für den negativen Nachweis
kein absichtlich defekter App-Commit in den Hauptbranch integriert werden.
