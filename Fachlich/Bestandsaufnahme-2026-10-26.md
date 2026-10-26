# Fachliche Bestandsaufnahme vom 26.10.2026

Nachtrag vom 26.10.2026: Der Antrag ist inzwischen unter
[Projektmanagement/Antrag](../Projektmanagement/Antrag/) abgelegt. Fachdozent ist
Armin Dörzbach, PM-Dozent Corrado Parisi. Die ursprünglichen Prüfgrenzen unten
bleiben als historischer Stand erhalten. Die aktuelle Zuordnung der Ziele steht
in der [Anforderungsmatrix](Anforderungsmatrix.md).

## Quellen und Prüfgrenzen

Geprüft: lokaler Checkout von https://github.com/lusaegesser/semesterarbeit-4sem,
Commit `6e59200`, README, Projektstand, Entscheidungsprotokoll, fachliche und
PM-Dokumentation, App-Einstieg, Testdateien, Docker-/Compose-Konfiguration und
GitHub-Workflow. Der Arbeitsbaum war vor der Prüfung sauber.

Externe Unterlagen unter `C:\Users\Lukas\Documents\richtlinien sem arbeit`:
- `Ergaenzungen_Semesterarbeiten_ITCNE.pdf` (14 Seiten, Text ausgelesen).
- `ITCNE25_Semesterarbeit 4 (Einreichungsformular) v2.docx` (Text und Tabellen ausgelesen).
- `Merkblatt A.url` und `Merkblatt B.url` (Verweise auf offizielle GitLab-Merkblätter).

GitHub konnte weder mit `git ls-remote` noch über den Webabruf verifiziert werden.
Die lokalen Remote-Tracking-Daten belegen keinen aktuellen Serverstand.
Die offiziellen Merkblätter waren über den Webabruf nicht inhaltlich lesbar.
Abgabeformalitäten, Bewertungsgewichtung und KI-Vorgaben sind deshalb noch anhand
dieser Originalquellen zu prüfen. Keine Tests, Container oder Deployments ausgeführt;
keine Aussage über aktuelle Lauffähigkeit oder erfolgreiche GitHub-Actions-Läufe.

## Antrag als fachliche Arbeitsgrundlage

Die vorhandene DOCX enthält den ausgefüllten SetFlow-Antrag. Annahme laut Lukas;
in der ausgelesenen Datei fehlen ausgefüllter Genehmigungsentscheid, begleitender
Dozent und Unterschrift. Eine finale angenommene Fassung ist im Repository noch
nicht hinterlegt. Der Text konkretisiert folgende Ziele:

| Bereich | Ziel und Nachweis | Termin |
| --- | --- | --- |
| CI | Unit-Tests für Passwortprüfung/Uploadbegrenzung; API-Tests für Anmeldung, Rechte, Upload, Audioabruf, Links und Kommentare; getrennte Testdaten | 13.12.2026 |
| Registry | Veröffentlichung nach erfolgreichen Hauptbranch-Tests, Image mit Commit gekennzeichnet; drei erfolgreiche Läufe und ein absichtlich fehlschlagender Test, der Veröffentlichung verhindert | 13.12.2026 |
| CD | Lokaler Runner, geschützte Hauptbranch-Deployment-Jobs, Helm und lokaler Kubernetes-Cluster; drei aufeinanderfolgende Deployments mit Health-Smoke-Test; geprüfter Helm-Rollback | 21.01.2027 |
| Datenerhalt | Testset mit Audio, Kommentar und Freigabelink überlebt Pod-Ersatz | 21.01.2027 |
| Restore | Getrennte Testumgebung; Datenbankintegrität, Datensatzanzahlen und Audio-SHA-256 stimmen überein | 21.01.2027 |

Kubernetes-API bleibt ohne öffentliche Freigabe; lokaler Runner führt keine
Pull-Request-Jobs aus und erhält auf den Projekt-Namespace begrenzte Rechte.
Hochverfügbarkeit gehört nicht zum Umfang. Abschluss und Abgabe gemäss Antrag:
27.01.2027. Drei Sprints, Jira und fortlaufende GitHub-Dokumentation sind vorgesehen.

## Richtlinienabgleich

Das Ergänzungs-PDF bezeichnet sich ausdrücklich als Empfehlungen und ersetzt
keine offiziellen Merkblätter. Es betont agile Umsetzung mit mindestens drei
Sprints, sichtbarem Fortschritt, Zielen und Releases sowie laufendem Einbezug der
Dozierenden. Videos und Einzelbesprechungen sind freiwillig. Zwei zentrale Dateien
für Fachliches und Projektmanagement sind ausdrücklich als mögliche Struktur genannt.
Die vorhandene Aufteilung passt dazu; ergänzende Betriebsnachweise sollten aus den
zentralen Dokumenten verlinkt werden.

Für die fachliche Dokumentation fehlen noch ausgearbeitete Problemstellung und
Zielgruppe, messbare Ziele mit Herkunft, Ist-/Soll-Architektur, begründete technische
Entscheide, Testplan und Testprotokolle sowie abschliessender Soll-Ist-Vergleich.
Abbildungen und Tabellen sollen beschriftet und in Verzeichnissen erfasst werden.
PM führt Planning, Review, Retrospektive, Schätzungen, DoD und Kommunikation;
fachliche Nachweise werden damit verlinkt. Keine Aktivitäten nachträglich erfinden.

## Tatsächlicher Implementierungsstand

- FastAPI-App, Tests und Backup-/Betriebsunterlagen sind übernommene Vorleistungen.
- Vorhandener Workflow führt pytest und `scripts/docker_smoke.py` in zwei Jobs aus.
  Ein Job für GHCR-Veröffentlichung oder Helm-Deployment fehlt.
- Testdateien für Zugriff, Tracks, Storage und Backup sind vorhanden. Die Fixture
  verwendet ein temporäres Datenverzeichnis und eine separate SQLite-Datenbank.
  Funktionsabdeckung und Testerfolg wurden hier nicht nachgewiesen.
- Keine Helm-Charts oder Kubernetes-Manifeste im geprüften Dateibestand vorhanden.
- Compose kann standardmässig das Alt-Volume `dj-set-archive_archive-data` verwenden;
  HTTPS enthält eine feste lokale IP und Ports 80/443. Betrieb daraus erst nach
  Kollisionsprüfung. Produktiver Alt-Checkout bleibt unberührt.

## Nächste fachliche Aufgabe

Nach Zuordnung zu einem Jira-Ticket eine Anforderungs- und Nachweismatrix aus dem
finalen Antrag erstellen: Ziel, Akzeptanzkriterium, bestehende Vorleistung, neue
Leistung, Testfall und Nachweisort. Danach vorhandene Tests und CI isoliert prüfen.
Vorher finale Antragsfassung und offizielle Merkblätter verfügbar machen bzw. prüfen.
