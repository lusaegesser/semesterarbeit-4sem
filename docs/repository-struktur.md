# Repository-Struktur und Lesepfad

[Startseite](../README.md)

Die Gliederung orientiert sich an der Semesterarbeit 2: eine Startseite, zwei
Hauptdokumente, Sprintberichte sowie getrennte Ablagen für Anhänge und Medien.
Der bestehende Ordnername `Fachlich/` bleibt erhalten.

## Lesepfad

1. [Startseite](../README.md): Auftrag, Orientierung und aktueller Einstieg.
2. [Projektmanagement](../Projektmanagement/README.md): Initiierung, Ziele,
   Stakeholder, Methoden, Planung, Sprintberichte und Reflexion.
3. [Fachlicher Teil](../Fachlich/README.md): Ausgangslage, Anforderungen,
   Architektur, Umsetzung nach Epics, Tests, Betrieb und Zielvergleich.
4. [Projektstand](projektstand.md): aktueller Stand, Prüfgrenzen und nächste Schritte.

## Ablage

```text
README.md
Projektmanagement/
  README.md                     PM-Hauptdokument
  00_Sprints/README.md           Sprintübersicht
    Sprint1/README.md            Detailliertes Planning, Review und Retro
    Sprint2/README.md            Grobplanung, später Review und Retro
    Sprint3/README.md            Grobplanung, später Review und Retro
  01_Anhang/README.md            Ergänzende Unterlagen und Verweise
  02_Bilder/README.md            Bereinigte PM-Abbildungen
  Antrag/                       Einreichungsformular und Annahmestand
  Nachweise/                    PM- und Kommunikationsnachweise
  Backlog.md                    Nutzerziele und Akzeptanzkriterien
  Definition-of-Done.md
  Risiken.md
  Jira-Abbildung.md             Ticketzuordnung und Kommunikation
Fachlich/
  README.md                     Fachliches Hauptdokument
  Ausgangslage/                 Herkunft und Vorprojekt
  Medien/                       Architekturabbildungen und optionale Demos
  Nachweise/                    Neue Testprotokolle und Ergebnisse
  Anforderungsmatrix.md          Ziele, Vorleistungen und Nachweise
docs/
  README.md                     Betriebs- und Dokumentationsübersicht
  projektstand.md                Aktueller Stand
  entscheidungen.md              Begründete Entscheide
  archiv/                       Frühere Zwischenstände
app/ frontend/ tests/ scripts/   Bestehende Implementierung und Prüfungen
.github/workflows/              CI und künftige Erweiterungen
deploy/ Dockerfile compose.yaml Bestehende Betriebsdateien
```

## Pflege und Kompatibilität

Tabelle 01: Inhalt und führender Ablageort.

| Inhalt | Führender Ort |
| --- | --- |
| Ablauf, Status und Sprintzuordnung | Jira |
| Nutzerziele und Kriterien | Backlog, mit Jira abgeglichen |
| Planung, Review und Retrospektive | Jeweiliges Sprintdokument |
| Technische Erklärung und Story-Nachweise | Fachliches Hauptdokument mit Verweisen |
| Aktueller Stand und nächste Schritte | docs/projektstand.md |
| Begründete Entscheide | docs/entscheidungen.md |
| Quellcodeversionen | Git-Commits, Tags und Releases |

Die bisherigen Dateien `Projektmanagement/Dokumentation.md`,
`Fachlich/Dokumentation.md` und `Projektmanagement/Sprint-1-Planning.md`
bleiben als kurze Weiterleitungen erhalten. Bestehende Links und Jira-Verweise
bleiben damit nutzbar. Antrag, Backlog, Matrix und technische Dateipfade behalten
ihre bisherigen Orte.

Hauptdokumente erklären die Zusammenhänge; Detailseiten enthalten Kriterien,
Protokolle und Belege. Historische Ergebnisse werden als Vorleistung bezeichnet.
Neue leere Medien-/Nachweisablagen werden erst mit tatsächlichen Belegen ergänzt.

Referenz der Gliederung:
[Semesterarbeit 2](https://gitlab.com/lukas03saegesser/semesterarbeit-2sem),
geprüfter Git-Stand `7ed6b81d48abbcbc13c2a61d45b44804f8a8b2fe`.
