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

## 26.10.2026 – Dokumentation und spätere Veröffentlichung

Das Repository bleibt während der Vorbereitung privat und soll zum Abschluss
öffentlich werden. Lokale Arbeitsanweisungen werden ignoriert und nicht weiter
versioniert. Bereits vorhandene Historie bleibt vorerst erhalten; vor dem
Sichtbarkeitswechsel sind Dateistand und Historie zu prüfen. Kein Umschreiben der
Historie oder Sichtbarkeitswechsel durch die aktuelle Vorbereitung.

Jira SEM4 (Board 67) führt Status und Sprintzuordnung; GitHub enthält fachliche
und PM-Dokumentation. Plan-IDs verbinden Antrag, Backlog und Nachweise, bis die
konkreten Jira-Kennungen zugeordnet sind. Kapazität bleibt bis zur Angabe von Lukas offen.

## 26.10.2026 – Sprintstruktur und Jira-Hierarchie

Sprint 1 erhält unter `Projektmanagement/00_Sprints/Sprint1/README.md` eine
zusammenhängende Dokumentation nach dem von Lukas bereitgestellten Aufbau der
Semesterarbeit 2. Die frühere Planning-Datei bleibt als Weiterleitung erhalten.
Planning, Review und Retrospektive sind getrennte Abschnitte; Ergebnisse werden
erst nach tatsächlicher Durchführung ergänzt.

Jira bildet drei fachliche Epics ab: Projektgrundlagen/Sprintsteuerung, Tests/Images
und Bereitstellung/Datenerhalt. Die zwölf Stories behalten ihre Plan-IDs; für
Sprint 1 werden 18 Unteraufgaben angelegt. Deren Aufwand ist bereits in den
Story-Schätzungen enthalten. Sprint 2/3 bleiben Grobplanung, bis Kapazität und
jeweiliges Commitment abgestimmt sind. Kein Sprint wird automatisch gestartet.

## 26.10.2026 – Hauptdokumente und Navigation wie Semesterarbeit 2

Die Referenzarbeit wurde bei Git-Stand
`7ed6b81d48abbcbc13c2a61d45b44804f8a8b2fe` gelesen. Die neue Startseite verlinkt
`Projektmanagement/README.md` und `Fachlich/README.md` als Hauptdokumente.
Sprintübersicht, Anhang, Bilder, Medien und Nachweise erhalten eigene Einstiege.
Der bestehende Name `Fachlich/` und alle Code-/Deploymentpfade bleiben erhalten.

Die früheren `Dokumentation.md`-Dateien bleiben als Weiterleitungen bestehen.
Details wie Backlog, Matrix und Protokolle werden von den Hauptdokumenten verlinkt;
historische Zwischenstände stehen im Archiv. Versionen werden über Git-Commits,
Tags und Releases geführt. Die Ordnerstruktur enthält keine übernommenen
Codekopien oder Medien der Semesterarbeit 2.

## 26.10.2026 – GitHub Flow für die Einzelarbeit

Die Schulunterlagen «Tag 02 – Git und Versionskontrolle» wurden gelesen und in
`CONTRIBUTING.md` auf SetFlow übertragen: kurze Aufgabenbranches, Conventional
Commits, PRs, transparente Eigenprüfung und Releases erst nach Abnahme.
Ein dauerhafter `develop`-Branch ist für dieses Einzelprojekt nicht vorgesehen.
Die Eigenprüfung wird nicht als unabhängige Freigabe bezeichnet.

Der vorbereitete Repository-/Dokumentationsstand wird in fünf logischen Commits
auf `feature/SEM4-1-projektgrundlagen` veröffentlicht. Ein PR macht den gesamten
Diff und CI-Ergebnisse prüfbar. Integration in `main` und der erste MVP-Release
sind getrennte Schritte; kein Release allein für die Commit-Anzahl.
