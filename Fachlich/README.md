# Fachlicher Teil

[Startseite](../README.md) · [Projektmanagement](../Projektmanagement/README.md) ·
[Anforderungsmatrix](Anforderungsmatrix.md) · [Nachweise](Nachweise/README.md)

Dieses Hauptdokument führt durch Ausgangslage, Ziele, Architektur, Umsetzung,
Tests und Betrieb von SetFlow. Der Schwerpunkt der Semesterarbeit 4 liegt auf
der DevOps-Pipeline. Stand: 26.10.2026; neue technische Umsetzung und Nachweise
sind überwiegend noch offen. Fachdozent: Armin Dörzbach.

## Inhaltsverzeichnis

- [Ausgangslage und Vorleistungen](#ausgangslage-und-vorleistungen)
- [Anforderungen und Abnahme](#anforderungen-und-abnahme)
- [Struktur und Architektur](#struktur-und-architektur)
- [Umsetzung nach Epics](#umsetzung-nach-epics)
- [Tests und Nachweise](#tests-und-nachweise)
- [Betrieb und Rückfall](#betrieb-und-rückfall)
- [Soll-Ist-Vergleich und Abschluss](#soll-ist-vergleich-und-abschluss)
- [Anhang und Quellen](#anhang-und-quellen)

## Ausgangslage und Vorleistungen

Die vorhandene Python-/FastAPI-Anwendung verwaltet DJ-Sets mit SQLite,
Audio-Uploads bis 1 GB, Administrator-Anmeldung, Freigabelinks und zeitbezogenen
Kommentaren. Der bisherige Betrieb verwendet Docker Compose. Backup-/Restore-
Werkzeuge und HTTPS-Vorbereitung wurden aus dem Vorprojekt übernommen.

Der bestehende Workflow enthält pytest und einen Docker-Smoke-Test. Anwendung,
Tests und bisherige Betriebsverfahren sind Vorleistungen. Neue Semesterarbeitsleistung
ist ihre gezielte Weiterentwicklung zur durchgängigen CI/CD-Pipeline samt Nachweisen.

[Ausgangslage und Vorprojekt](Ausgangslage/README.md) und
[Bestandsaufnahme vom 26.10.2026](Bestandsaufnahme-2026-10-26.md) halten Herkunft,
Implementierungsstand und Prüfgrenzen fest. Historische Testergebnisse werden
nicht als neu durchgeführte Tests ausgewiesen.

## Anforderungen und Abnahme

Grundlage ist der [Antrag](../Projektmanagement/Antrag/README.md), dessen Annahme
Lukas bestätigt hat. Die [Anforderungs- und Nachweismatrix](Anforderungsmatrix.md)
ordnet A01–A07 jeweils Termin, Vorleistung, neue Leistung und Nachweis zu.

Tabelle 01: Technische Abnahmebereiche.

| Bereich | Geplanter Nachweis | Termin |
| --- | --- | --- |
| Tests und Registry | Antragsfälle mit pytest/HTTPX; drei Publish-Läufe; absichtlicher Testfehler sperrt Veröffentlichung | 13.12.2026 |
| Deployment | Lokaler begrenzter Runner, drei Helm-Deployments mit Health-Smoke-Test, erfolgreicher Rollback | 21.01.2027 |
| Daten | Pod-Ersatz mit erhaltenen Daten; isolierter Restore mit DB-Integrität, Anzahlen und Audio-SHA-256 | 21.01.2027 |

Die konkrete Abnahme erfolgt pro Story anhand ihrer Akzeptanzkriterien und der
[Definition of Done](../Projektmanagement/Definition-of-Done.md).

## Struktur und Architektur

### Repository

Tabelle 02: Technische Ablage im bestehenden Repository.

| Pfad | Inhalt |
| --- | --- |
| [app/](../app/) | FastAPI-Anwendung und Datenzugriff |
| [frontend/](../frontend/) | Browseroberfläche |
| [tests/](../tests/) | Automatisierte Tests |
| [scripts/](../scripts/) | Verwaltung, Backup und Container-Smoke-Test |
| [.github/workflows/](../.github/workflows/) | Bestehende und künftig erweiterte Pipeline |
| [Dockerfile](../Dockerfile), [compose.yaml](../compose.yaml), [deploy/](../deploy/) | Container und bisherige Betriebsdateien |

Die Dokumentation ist in [Projektmanagement](../Projektmanagement/README.md) und
Fachliches gegliedert. [Repository-Struktur](../docs/repository-struktur.md)
erläutert die Ablage und den Lesepfad. Codeversionen werden über Git geführt.

### Ist und Zielbild

Ist: Compose-basierter Betrieb mit vorhandenen Test- und Sicherungswerkzeugen.
Ziel: GitHub Actions prüft Änderungen und veröffentlicht Commit-gekennzeichnete
Images in GHCR. Vertrauenswürdige Deployment-Jobs nutzen einen lokalen Runner,
der mit Helm in einen eigenen lokalen Kubernetes-Namespace deployt.
Die Cluster-Variante ist noch zu begründen. Die Kubernetes-API bleibt ohne
öffentliche Freigabe; der lokale Runner verarbeitet keine Pull-Request-Jobs.

Entscheide und ihre Begründung stehen im [Entscheidungsprotokoll](../docs/entscheidungen.md).
Das Zielbild ist geplant; es beschreibt noch keine nachgewiesene Installation.

## Umsetzung nach Epics

### Epic A – Projektgrundlagen und Sprintsteuerung

Die fachliche Zuordnung der Antragsziele erfolgt in P02 / SEM4-2.
Methodik, Kapazität und Sprintberichte stehen im [PM-Hauptdokument](../Projektmanagement/README.md).

### Epic B – Automatisierte Tests und versionierte Images

Tabelle 03: Geplante Arbeit in Epic B.

| Story | Thema | Fachlicher Stand |
| --- | --- | --- |
| P03 / SEM4-6 | Tests und CI isoliert prüfen | Testdateien vorhanden; Ausführung und Abdeckung neu prüfen |
| P04 / SEM4-7 | Begründete Testlücke schliessen | Auswahl nach P03; noch nicht implementiert |
| P07 / SEM4-10 | Tests, Build und GHCR verbinden | Testworkflow vorhanden; Publish und neue Nachweise offen |

Nach Umsetzung je Story ergänzen: Problem, gewählter Ansatz, relevante Änderungen,
begründete Entscheide, Testresultat und bereinigter Nachweis. Kleine Codeausschnitte
werden mit dem tatsächlichen Git-Stand verlinkt.

### Epic C – Kontrollierte Bereitstellung und Datenerhalt

Tabelle 04: Geplante Arbeit in Epic C.

| Story | Thema | Fachlicher Stand |
| --- | --- | --- |
| P08 / SEM4-11 | Kubernetes und Helm vorbereiten | Cluster-Auswahl und Chart offen |
| P09 / SEM4-12 | Lokalen Runner begrenzen | Installation, Rechte und Triggerprüfung offen |
| P10 / SEM4-13 | Deployments, Smoke-Test und Rollback | Helm-Nachweise offen |
| P11 / SEM4-14 | Pod-Datenerhalt und isolierter Restore | Neue Kubernetes-Nachweise offen; bestehende Backup-Werkzeuge sind Vorleistung |

Die [Jira-Zuordnung](../Projektmanagement/Jira-Abbildung.md) verlinkt alle tatsächlichen
Vorgänge. Umsetzungsergebnisse werden erst nach Durchführung ergänzt.

## Tests und Nachweise

Neue Tests verwenden getrennte Daten und Umgebungen. Ein Testprotokoll nennt
Datum, Commit, Voraussetzung, Durchführung, Soll/Ist, Ergebnis und Grenzen.
Die [Nachweisübersicht](Nachweise/README.md) führt zu den abgelegten Resultaten.
Screenshots und optionale Demos liegen unter [Medien](Medien/README.md).

Aus historischen Protokollen werden keine aktuellen Erfolgsaussagen abgeleitet.
Private Audiodateien, Tokens, Passwort-Hashes und Backup-Archive werden nicht abgelegt.

## Betrieb und Rückfall

Die [Betriebsdokumentation](../docs/README.md) kennzeichnet die übernommenen
Anleitungen und Protokolle des bisherigen Compose-Betriebs. Sie beziehen sich auf
den separaten Alt-Checkout und ersetzen keine Anleitung für den künftigen Cluster.
Vor Betriebsänderungen werden Projektname, Ports, Volumes und Datenisolation geprüft.

Für die neue Zielumgebung sind Installation, Update, Runner-Start, Sicherung,
Restore und Rollback noch anhand der tatsächlichen Umsetzung zu dokumentieren.
Ein einzelner Projektlaptop bietet keine Hochverfügbarkeit.

## Soll-Ist-Vergleich und Abschluss

Die abschliessende Bewertung ist offen. Nach Umsetzung werden A01–A07 mit den
tatsächlichen Ergebnissen abgeglichen. Abweichungen, Einschränkungen und offene
Punkte erhalten eine Begründung. P12 / SEM4-15 bündelt die Abschlussunterlagen.

## Anhang und Quellen

- [Anforderungsmatrix](Anforderungsmatrix.md)
- [Ausgangslage](Ausgangslage/README.md)
- [Tests und Nachweise](Nachweise/README.md)
- [Medien](Medien/README.md)
- [Betrieb und historische Protokolle](../docs/README.md)

### Quellenstand

Derzeitige Grundlage sind der Antrag, das bestehende Repository mit seiner
Git-Historie und die verlinkten Bestandsprotokolle. Technische Referenzen werden
bei ihrer tatsächlichen Verwendung mit Bezug zur Story ergänzt.
Erforderliche Quellen- und Hilfsmitteldeklarationen werden mit den gültigen
Schulvorgaben abgeglichen.

### Abbildungs- und Tabellenverzeichnis

In diesem Hauptdokument sind noch keine Abbildungen eingebunden.

- Tabelle 01: Technische Abnahmebereiche.
- Tabelle 02: Technische Ablage im bestehenden Repository.
- Tabelle 03: Geplante Arbeit in Epic B.
- Tabelle 04: Geplante Arbeit in Epic C.

[Zur Startseite](../README.md)
