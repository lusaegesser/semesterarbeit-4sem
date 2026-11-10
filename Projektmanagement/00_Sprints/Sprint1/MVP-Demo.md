# MVP-Demo und technische Ergebnisprüfung

## Ergebnis

Das technische Sprintziel ist erreicht: Die vorhandene Testbasis ist geprüft,
eine begründete Passwort-Testlücke geschlossen und die CI erfolgreich.
P03 und P04 sind in Jira erledigt (10 von 12 geplanten Story Points).
Eigenreview und Retro-Massnahme wurden am 10.11.2026 bestätigt.
Release: [v0.1.0](https://github.com/lusaegesser/semesterarbeit-4sem/releases/tag/v0.1.0).

## Demo in vier Schritten

| Schritt | Gezeigtes Ergebnis | Nachweis |
| --- | --- | --- |
| 1. Ausgangslage | 20 vorhandene Tests und Container-Test als Vorleistung; Login, Rechte, Upload, Audio, Freigaben, Kommentare und Backup zugeordnet | [P03-Abdeckungsmatrix](../../../Fachlich/Nachweise/2026-10-27-P03-tests-ci.md) |
| 2. Neuer Beitrag | Sieben direkte Passwort-Testfälle: richtig/falsch, Unicode, unterschiedliche Hashes sowie fehlende/fehlerhafte Hashformate | [Neue Testdatei](../../../Fachlich/Anwendung/tests/test_passwords.py), [P04-Nachweis](../../../Fachlich/Nachweise/2026-11-04-P04-passworttests.md) |
| 3. Ausführung | Neue Fälle separat und gemeinsam mit der Regressionstestsuite erfolgreich | Tabelle 02 unten |
| 4. Automatisierung | GitHub prüft pytest und Container-Smoke-Test bei Push/PR | [CI-Lauf 41826425587](https://github.com/lusaegesser/semesterarbeit-4sem/actions/runs/41826425587) |

Tabelle 01: Ablauf der MVP-Demo.

Der sichtbare Mehrwert ist eine nachvollziehbare Testbasis mit gezieltem
Regressionsschutz. Neue Produktfunktionen, Registry oder Kubernetes sind nicht
das Ergebnis dieses Sprints. Das separat ergänzte Titelbild ist kein Ersatz
für den geplanten technischen Mehrwert.

## Tatsächliche Prüfung am 10.11.2026

Geprüfter versionierter Stand: `c505014ba88fe41b1d7a43c5fcacb983c06f599f`.
Die lokalen, uncommittierten Ergänzungen zum Titelbild-Betrieb wurden nicht
als Teil des MVP-Kandidaten bewertet.

| Prüfung | Soll | Ist |
| --- | --- | --- |
| Passworttests separat | Alle sieben Fälle bestehen | `7 passed in 3.32s`, Exit 0 |
| Gesamtsuite | Alle 27 Fälle bestehen | `27 passed in 12.41s`, Exit 0 |
| CI desselben versionierten Stands | pytest und Container-Smoke-Test erfolgreich | Beide Jobs `success`, über GitHub-API zurückgelesen |
| Release vorhanden | Vor Veröffentlichung Doppelanlage ausschliessen | Kein `v0.1.0`-Tag auf origin und kein GitHub-Release gefunden |

Tabelle 02: Ergebnisprüfung des MVP-Kandidaten.

Lokale Befehle aus `Fachlich/Anwendung` mit Python 3.12.14:

```powershell
..\..\.venv\Scripts\python.exe -m pytest -q tests/test_passwords.py
..\..\.venv\Scripts\python.exe -m pytest -q
```

Für diesen Lauf zeigten `TEMP`/`TMP` auf den separaten Ordner `.venv/p06-tmp`.
Die bestehende Testfixture erzeugt eigene SQLite-/Uploaddaten; keine Host-Ports,
Compose-Starts oder produktiven Datenzugriffe. Der Ordner wurde danach entfernt.
Der Container-Test wurde heute nicht lokal wiederholt; dessen Nachweis stammt
aus dem erfolgreichen CI-Job des genannten Commits. Die Testsuite ist unverändert.

## Soll-Ist und Grenzen des Antrags

| Bereich | Stand am 10.11.2026 | Weiteres Vorgehen |
| --- | --- | --- |
| A01 / Sprintsteuerung | Planning vorhanden; P03/P04 abgeschlossen; P06 läuft | Eigenreview bestätigt; Test-Vorabcheck für Sprint 2 vereinbart |
| A02 / Testbasis | Funktionale Zuordnung und sieben neue Passwortfälle belegt | Weitere Testlücken bei P07 berücksichtigen; kein Anspruch auf vollständige Coverage |
| A03 / Images | Noch keine GHCR-Publish-Verknüpfung oder Publish-Sperre nachgewiesen | P07, Sprint 2 |
| A04/A05 / Bereitstellung | Keine neuen Kubernetes-/Helm-/Runner-Nachweise | P08–P10, Sprint 2/3 |
| A06/A07 / Daten | Vorhandene Compose-/Backup-Prüfungen sind keine Kubernetes-Nachweise | P11, Sprint 3 |

Tabelle 03: Abgrenzung zu den [Antragszielen](../../../Fachlich/Anforderungsmatrix.md).
