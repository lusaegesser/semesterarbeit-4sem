# Anforderungs- und Nachweismatrix

Grundlage: [Antrag](../Projektmanagement/Antrag/), Annahme durch Lukas bestätigt.
Stand: 26.10.2026. Nachweise sind geplant, sofern nicht ausdrücklich anders bezeichnet.
Die technischen Ziele werden hier zugeordnet; ihre Umsetzung erfolgt in eigenen Aufgaben.

Tabelle 1: Antragsziele, Vorleistungen und geplante Nachweise.

| ID | Messbares Ziel | Vorleistung / neue Leistung | Plan-ID | Nachweis und Termin |
| --- | --- | --- | --- | --- |
| A01 | Drei Sprints; Stories, Akzeptanzkriterien, DoD, Planning, Review, Retro; laufende GitHub-Doku | Grundstruktur vorhanden; konkrete Planung und Durchführung neu | P01, P05, P06, P12 | Jira, Sprintberichte, tatsächliche Teams-Mitteilungen; 27.01.2027 |
| A02 | pytest/HTTPX: Passwortprüfung und Uploadbegrenzung; API für Login, Rechte, Upload, Audio, Freigaben und Kommentare; isolierte Daten | Testdateien und temporäre Fixtures vorhanden; Ausführung/Abdeckung prüfen, gezielt ergänzen | P02–P04, P07 | Testmatrix, Testprotokoll, CI-Läufe; 13.12.2026 |
| A03 | Commit-gekennzeichnetes Image nach erfolgreichen Hauptbranch-Tests in GHCR; drei erfolgreiche Läufe; absichtlicher Testfehler verhindert Publish | Test-/Containerworkflow vorhanden; Build-/Publish-Verknüpfung und Registry neu | P07 | Drei Actions-Läufe und Image-Digests; negativer Lauf ohne Veröffentlichung; 13.12.2026 |
| A04 | Lokaler Kubernetes-Cluster und Helm; lokaler Runner nur für geschützte Hauptbranch-Deployments; Namespace-Rechte; keine öffentliche API | Docker-/Compose-Betrieb vorhanden; Kubernetes, Helm und Runner neu | P08, P09 | Architektur, Rechte-/Triggerprüfung, bereinigte Konfiguration; 21.01.2027 |
| A05 | Drei aufeinanderfolgende Deployments mit automatischem Health-Smoke-Test; erfolgreicher Helm-Rollback | Docker-Smoke-Test vorhanden; Helm-Deploy-/Rollback-Nachweise neu | P10 | Drei Deploy-Läufe, Revisionen/Image-Digests, Health-Resultat vor/nach Rollback; 21.01.2027 |
| A06 | Testset mit Audio, Kommentar und Freigabelink bleibt nach Pod-Ersatz erhalten | Docker-Datenerhalt und Backup-Verfahren vorhanden; Pod-/PVC-Nachweis neu | P11 | Vorher-/Nachher-Datensätze und funktionierender Link; 21.01.2027 |
| A07 | Restore getrennt; DB-Integrität, Anzahlen und Audio-SHA-256 entsprechen Sicherung | Backup-/Restore-Werkzeuge vorhanden; isolierter Kubernetes-Nachweis neu | P11 | Manifest, Integritätsprüfung, Zähl-/Prüfsummenvergleich; 21.01.2027 |

Keine neuen Erfolgsaussagen aus alten Protokollen ableiten. Testprotokolle enthalten
Datum, Commit, Umgebung, Testdaten, Schritte, Soll/Ist, Ergebnis und bereinigten
Nachweislink. Private Audiodateien, Sicherungsarchive und Zugangsdaten bleiben lokal.
