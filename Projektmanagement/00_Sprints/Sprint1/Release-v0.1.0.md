# Release v0.1.0

Erster Semesterarbeits-MVP vom 10.11.2026.
Versionierter Stand und Quellcode: [GitHub-Release v0.1.0](https://github.com/lusaegesser/semesterarbeit-4sem/releases/tag/v0.1.0).

## Änderungen

- Vorhandene Tests und CI isoliert geprüft und fachlich zugeordnet (P03).
- Sieben direkte Passwort-Testfälle ergänzt (P04): richtiges/falsches Passwort,
  Unicode, unterschiedliche gesalzene Hashes und fehlerhafte Hashformate.
- Sprint-Ergebnis und offene Antragsziele nachvollziehbar dokumentiert.

## Prüfungen

27 Tests bestanden; neue Passwortfälle separat 7/7 erfolgreich.
[CI des Kandidaten](https://github.com/lusaegesser/semesterarbeit-4sem/actions/runs/41826425587)
mit erfolgreichem Test- und Containerjob.
[Demo und Nachweise](MVP-Demo.md).
Der Release-Tag wird auf dem erfolgreich geprüften integrierten Stand erstellt.

## Einschränkungen und Betrieb

App, ursprüngliche 20 Tests, Testworkflow und Container-/Backup-Verfahren sind
Vorleistungen. GHCR-Veröffentlichung, Helm, Runner und Kubernetes-Datenerhalt
sind weiterhin offen. Dieses Release stellt keinen neuen produktiven Betrieb bereit.

Keine Datenmigration und kein automatisches Deployment durch das Release.
Bei einer späteren beauftragten Installation gelten die Betriebsanleitungen;
ein Rückwechsel des Codes stellt keine früheren Daten wieder her.

## Review und Verbesserung

Asynchrones Eigenreview am 10.11.2026 bestätigt. Zu Beginn von Sprint 2 werden
Interpreter, Abhängigkeiten und temporärer Schreibpfad geprüft und dokumentiert.
Dozierenden-Feedback ist nicht erfasst.
