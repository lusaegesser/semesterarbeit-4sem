# Tests und GHCR Veröffentlichung

Der Workflow `.github/workflows/tests.yml` erweitert die bestehende Testpipeline
um versionierte Container-Images. pytest und Container-Smoke-Test bleiben getrennte
Pflichtjobs. Nur wenn beide erfolgreich sind, darf der Publish-Job beginnen.

## Trigger und Berechtigungen

Push und Pull Request führen die Tests auf GitHub-gehosteten Runnern aus.
Veröffentlicht wird ausschliesslich im Repository
`lusaegesser/semesterarbeit-4sem` auf `refs/heads/main`, bei Push oder manuellem
`workflow_dispatch`. Ein PR veröffentlicht auch bei erfolgreichen Tests kein Image.

Alle Jobs erhalten standardmässig `contents: read`. Nur `publish` erhält zusätzlich
`packages: write`. Die Anmeldung verwendet das kurzlebige `GITHUB_TOKEN` des Jobs;
kein persönlicher Token oder lokales Secret ist erforderlich. Neue Docker- und
Artefakt-Actions sind auf am 23.11.2026 verifizierte Commit-SHAs festgelegt.

## Image und Nachweis

Image: `ghcr.io/lusaegesser/semesterarbeit-4sem`.

| Kennung | Zweck |
| --- | --- |
| `sha-<vollständiger Commit-SHA>` | Zuordnung zum geprüften Quellstand |
| `sha-<SHA>-run-<Lauf-ID>-<Versuch>` | Zuordnung zu genau einem Veröffentlichungsversuch |
| `sha256:<Digest>` | Eindeutiger Image-Inhalt für spätere Deployments |

Tabelle 01: Image-Kennungen.

Buildkontext ist `Fachlich/Anwendung`. OCI-Labels verknüpfen Repository und Commit.
Es gibt keinen `latest`-Tag. Die Job-Zusammenfassung und das Artefakt
`publish-evidence-<Lauf-ID>-<Versuch>` enthalten Commit, Lauf-URL, Tags und Digest
als `publish-evidence.json`. Benötigte Nachweise zeitnah ins Repository übernehmen,
bevor die Actions-Aufbewahrungsfrist abläuft.

Ein Commit-Tag kann bei einem erneuten Build desselben Commits auf einen anderen
Digest zeigen, etwa wegen des veränderlichen Python-Basisimages. Für P08/P09 das
Image deshalb per Digest oder geprüftem laufbezogenem Tag auswählen. Dies ist
keine Zusicherung bitgleicher Neubauten. Das erste Package übernimmt die
GHCR-Standardberechtigungen; Sichtbarkeit nicht ungeprüft ändern.

## Test Vorabcheck

Aus `Fachlich/Anwendung`:

```powershell
python scripts/ci_tests.py
```

Das Skript protokolliert die Python-Version, vergleicht alle gepinnten
Abhängigkeiten, führt `pip check` aus und prüft Schreiben/Lesen im temporären
Verzeichnis. Erst danach startet pytest mit den bestehenden isolierten Fixtures.
Lokal muss `TEMP`/`TMP` auf einen beschreibbaren Testpfad zeigen; die CI nutzt
den temporären Bereich des GitHub-Runners. Es werden keine `.env` oder
produktiven Daten benötigt.

## Nachweis der Publish Sperre

Nach Integration auf `main` denselben Workflow zweimal manuell ausführen:
einmal mit `inject_test_failure: true`, danach wieder mit `false`.
Beide Läufe müssen denselben Commit und `refs/heads/main` verwenden.

Der negative Lauf ergänzt ausschliesslich eine temporäre pytest-Datei mit einer
absichtlich falschen Assertion. Die echte Testsuite läuft mit; pytest liefert
Exit 1. Die Datei wird beim Verlassen des Skripts entfernt. Der Publish-Job wird
wegen seines fehlgeschlagenen Pflichtjobs übersprungen. Es gibt keine zusätzliche
Publish-Bedingung, welche den Fehler-Schalter separat abweist; damit wird die
tatsächliche Abhängigkeit von den Tests geprüft.

Für den negativen Lauf Jobstatus, Fehler und Lauf-ID sichern. Anschliessend den
laufbezogenen Tag in GHCR prüfen: Er darf nicht existieren. Ein vorhandener
Commit-Tag eines früheren erfolgreichen Laufs ist kein Gegenbeweis. Ein Auth- oder
Netzwerkfehler beim Registry-Zugriff belegt keine fehlende Veröffentlichung.
Das erfolgreiche Gegenstück mit `false` muss denselben Publish-Pfad einschliesslich
Registry-Anmeldung und Image-Veröffentlichung durchlaufen.

Der Job `verify-negative-publish` führt diese lesende Prüfung im negativen
Hauptbranch-Lauf aus: Er verlangt `test=failure`, `container=success` und
`publish=skipped`, liest zunächst den bestehenden Commit-Tag und prüft danach
den fehlenden Versuchstag. Das Artefakt `negative-publish-evidence-…` sichert
beide Registry-Antworten. Der gesamte Lauf bleibt wegen des absichtlichen
pytest-Fehlers erwartungsgemäss rot; der Kontrolljob muss erfolgreich sein.

Für die drei positiven Nachweise sind drei tatsächlich abgeschlossene
Publish-Läufe erforderlich. Ein Push-Lauf und zwei manuelle positive Läufe sind
möglich; Lauf-ID, SHA, laufbezogener Tag und Digest getrennt dokumentieren.
Das sind drei Ausführungen, nicht zwangsläufig drei unterschiedliche Quellstände.

## Betrieb und Rückfall

Der Workflow veröffentlicht Images und führt kein Deployment aus.
Keine bestehenden Compose-Container, Volumes oder Daten werden ersetzt.
Bei Pipeline-Problemen zunächst die letzte geprüfte Konfiguration per normalem
PR wiederherstellen. Bereits geprüfte Digests bleiben als Referenz erhalten;
keine Registry-Bereinigung oder Datenwiederherstellung ist Teil dieser Story.

## Technische Referenzen

- [GitHub: Docker-Images veröffentlichen](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images)
- [GitHub: Packages mit GitHub Actions](https://docs.github.com/en/packages/managing-github-packages-using-github-actions-workflows/publishing-and-installing-a-package-with-github-actions)
- [Docker: build-push-action und Digest-Ausgabe](https://github.com/docker/build-push-action)
