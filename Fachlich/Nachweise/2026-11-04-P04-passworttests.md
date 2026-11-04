# P04 – Passwortprüfung gezielt testen

## Lücke und neuer Beitrag

Die [P03-Prüfung](2026-10-27-P03-tests-ci.md) zeigte: Login ist über die API
geprüft, direkte Unit-Tests des Passwortvertrags fehlen. Das Antragsziel
[A02](../Anforderungsmatrix.md) nennt ausdrücklich die Passwortprüfung.

Neu ist [tests/test_passwords.py](../Anwendung/tests/test_passwords.py) mit sieben
Testfällen. Sie rufen `hash_password` und `verify` direkt auf und prüfen sichtbares
Verhalten ohne Nachbau des Hashalgorithmus oder Mock der Kryptografie:

| Fall | Erwartetes Verhalten |
| --- | --- |
| ASCII-Passwort | Richtiges Passwort akzeptiert, abweichendes abgewiesen |
| Unicode-Passwort | Ebenso korrekte Unterscheidung bei Umlauten und weiteren Schriftzeichen |
| Zweimal dasselbe Passwort hashen | Unterschiedliche Hashes; beide verifizieren das Passwort |
| Fehlender Hash (`None`) | `False`, keine Ausnahme |
| Leerer Hash | `False`, keine Ausnahme |
| Hash ohne Trenner | `False`, keine Ausnahme |
| Hash mit zusätzlichem Trenner | `False`, keine Ausnahme |

Tabelle 01: Neue Passwort-Testfälle und Sollverhalten.

Die bisherigen 20 Tests, der Testworkflow und der Container-Smoke-Test bleiben
**Vorleistungen**. Anwendungslogik, Abhängigkeiten und Workflow wurden nicht geändert.
Weitere in P03 genannte Lücken, etwa die exakte Uploadgrenze, gehören nicht zu
dieser Ergänzung.

## Isolation und Ausführung

Arbeitsordner: `Fachlich/Anwendung`; Windows/Python 3.12.14. Interpreter:
`..\..\.venv\Scripts\python.exe`. `TEMP` und `TMP` zeigten für pytest auf einen
eigenen Ordner `.p04-tmp` im Anwendungsordner. Ausführung ausserhalb der Sandbox,
entsprechend den in P03 festgestellten Temp-Berechtigungsproblemen.

Die unveränderte `conftest.py` setzt temporäre SQLite-/Uploadpfade vor dem
App-Import. Auch die neuen Tests durchlaufen die bestehende Datenbank-Aufräumfixture;
die eigentlichen Assertions benötigen weder HTTP noch gespeicherte Betriebsdaten.
Alle Passwörter sind synthetisch, Hashes bleiben im Arbeitsspeicher. Kein Testwert
wird als Administratorkonfiguration gespeichert. Temporäre Testreste werden entfernt.

| Prüfung | Soll | Ist |
| --- | --- | --- |
| `python -m pytest -q tests/test_passwords.py` | Alle neuen Fälle bestehen | **7 passed in 4.86s**, Exit 0 |
| `python -m pytest -q` | Vorleistungen und Ergänzung bestehen gemeinsam | **27 passed in 17.44s**, Exit 0 |

Tabelle 02: Lokale pytest-Ergebnisse vom 04.11.2026.

Zusätzlich lief `python scripts/docker_smoke.py` erfolgreich (alle drei
PASS-Meldungen, Exit 0). Vorher geprüft: eigene generierte Compose-Datei ohne
Betriebs-.env, zufälliges Projekt `dj-archive-smoke-4fce1e669e`, eigenes Volume
`dj-archive-smoke-4fce1e669e_test-data`, dynamischer Loopback-Port
`127.0.0.1::8000`. Start/Login/Upload/Gastkommentar, Container-Ersatz mit
Datenerhalt und separater Restore bestanden. Create/Restore meldeten jeweils
3 Dateien, 1 Set, 1 Kommentar und 0 Freigaben/Sitzungen.
Die Testressourcen wurden entfernt. Vorher/nachher liefen die produktiven
Container mit denselben IDs `eee508f4e78f` und `d387d872f089`; die drei bestehenden
Volumes blieben unverändert. Alt-Checkout und Betriebsdaten wurden nicht berührt.
Das ist ein lokaler Container-Nachweis, kein Kubernetes- oder Remote-CI-Nachweis.

Der vorhandene GitHub-Workflow wurde gelesen: `python -m pytest -q` sammelt die
neue Testdatei automatisch im richtigen Arbeitsordner ein.
Die Ergänzung ist mit [Commit 22b3560](https://github.com/lusaegesser/semesterarbeit-4sem/commit/22b3560378d7aad10b9e3b83d1237abbdbf2a3b3)
auf `main` veröffentlicht. Der [GitHub-CI-Lauf 41795243957](https://github.com/lusaegesser/semesterarbeit-4sem/actions/runs/41795243957)
mit Python 3.13 ist erfolgreich abgeschlossen. Alle vier Akzeptanzkriterien sind
erfüllt; SEM4-7 und die Unteraufgaben SEM4-25 bis SEM4-27 sind in Jira **Erledigt**.
