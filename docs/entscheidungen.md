# Entscheidungsprotokoll

## 26.10.2026 – Gemeinsame Semesterarbeitsablage

Ein neues privates GitHub-Repository semesterarbeit-4sem enthält App, Tests,
Pipeline und Dokumentation. Die bewährte Aufteilung Fachlich/ und Projektmanagement/
bleibt erhalten. Das ursprüngliche App-Repository und der laufende Betrieb bleiben
bis zu einer geplanten Umstellung bestehen. Git-Historie und Vorleistungen werden erhalten.

## Arbeitsplätze

ASUS: Umsetzung, Cluster und fachliche Nachweise. Arbeitslaptop: Planung und Dokumentation.
Beide klonen dasselbe Repository, synchronisieren über GitHub und vermeiden parallele
Änderungen derselben Dateien. Keine Secrets oder Betriebsdaten werden synchronisiert.

## Genehmigte technische Richtung

GitHub Actions und GHCR; GitHub-gehostete Runner für Tests/Builds, lokaler Runner
für vertrauenswürdige Deployments mit Helm in einen lokalen Kubernetes-Cluster.
Kubernetes dient als Zielumgebung, DevOps bleibt Hauptthema. Konkrete Cluster-Variante offen.
