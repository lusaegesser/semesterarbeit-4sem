# Fachlicher Teil

[Startseite](../README.md) · [Projektmanagement](../Projektmanagement/README.md)

## Ausgangslage und Vorleistungen

SetFlow ist eine FastAPI-Anwendung mit SQLite, Audio-Uploads, Administrator-Anmeldung,
Freigabelinks und zeitbezogenen Kommentaren. Anwendung, Tests, bestehende CI,
Docker-Betrieb und Backup-/Restore-Verfahren stammen aus dem Vorprojekt.

Die Semesterarbeit ergänzt die durchgängige Verbindung von Prüfung, versioniertem
Image und kontrollierter Bereitstellung. Neue Leistungen werden getrennt nachgewiesen.

## Anforderungen und Abnahme

Der Antrag ist abgelegt. Die Anforderungsmatrix ordnet Ziele und Nachweise zu.

| Bereich | Nachweis | Termin |
| --- | --- | --- |
| Tests und Images | Antragsfälle mit pytest/HTTPX, drei Publish-Läufe und Publish-Sperre bei Testfehler | 13.12.2026 |
| Deployment | Drei Helm-Deployments mit Smoke-Test und erfolgreicher Rollback | 21.01.2027 |
| Daten | Pod-Datenerhalt und isolierter Restore mit Integritäts-, Anzahl- und SHA-256-Vergleich | 21.01.2027 |

*Tabelle 01: Technische Abnahmebereiche.*

## Struktur und Architektur

Die technische Ablage liegt vollständig unter `Fachlich/`.

| Ordner | Inhalt |
| --- | --- |
| `Anwendung/` | App, Oberfläche, Tests, Skripte und Containerdateien |
| `Betrieb/` | Betriebs- und Sicherungsanleitungen |
| `Ausgangslage/` | Vorprojekt und historische Protokolle |
| `Nachweise/`, `Medien/` | Neue Prüfprotokolle und bereinigte Abbildungen |

*Tabelle 02: Fachliche Ablage.*

Ist: Compose-Betrieb mit bestehenden Tests und Sicherungswerkzeugen.
Ziel: GitHub Actions prüft Änderungen und veröffentlicht Commit-Images in GHCR.
Ein lokaler Runner deployt mit Helm in einen eigenen Kubernetes-Namespace.
Die Kubernetes-API bleibt privat; der Runner verarbeitet keine PR-Jobs.

## Umsetzung nach Epics

| Epic | Stories | Stand |
| --- | --- | --- |
| A – Projektgrundlagen | P02: Ziele und Nachweise | Matrix vorbereitet |
| B – Tests und Images | P03: Bestandsprüfung; P04: Testergänzung; P07: CI/GHCR | Technische Weiterentwicklung offen |
| C – Bereitstellung und Daten | P08: Kubernetes/Helm; P09: Runner; P10: Deployment/Rollback; P11: Datenerhalt/Restore | Umsetzung und Nachweise offen |

*Tabelle 03: Umsetzungsschwerpunkte.*

Anwendung und Testwerkzeuge liegen gemeinsam unter `Anwendung/`. Die CI verwendet
diesen Arbeitsordner. Docker-Buildkontext und relative App-Pfade bleiben konsistent.

## Tests und Nachweise

Tests verwenden isolierte Daten und Umgebungen. Protokolle enthalten Datum,
Commit, Voraussetzung, Schritte, Soll/Ist, Ergebnis und Grenzen.
Private Aufnahmen, Zugangsdaten und Backup-Archive gehören nicht ins Repository.

## Betrieb und Rückfall

Die übernommenen Anleitungen beziehen sich auf den bisherigen Compose-Betrieb.
Installation, Update und Rückfall der neuen Zielumgebung werden mit der Umsetzung
dokumentiert. Der bisherige produktive Checkout bleibt unverändert.

## Soll-Ist-Vergleich und Abschluss

Die Zielerreichung wird abschliessend anhand der Anforderungsmatrix bewertet.
Abweichungen und Einschränkungen werden begründet.

## Unterlagen

- [Anwendung und Tests](Anwendung/README.md)
- [Anforderungsmatrix](Anforderungsmatrix.md)
- [Betrieb](Betrieb/README.md)
- [Entscheidungen](Entscheidungen.md)
- [Nachweise](Nachweise/README.md)

### Quellen und Verzeichnisse

Grundlage sind Antrag, Repository und Bestandsprotokolle. Technische Referenzen
und erforderliche Hilfsmitteldeklarationen werden bei Verwendung ergänzt.

Tabelle 01: Abnahmebereiche. Tabelle 02: Ablage. Tabelle 03: Umsetzungsschwerpunkte.
