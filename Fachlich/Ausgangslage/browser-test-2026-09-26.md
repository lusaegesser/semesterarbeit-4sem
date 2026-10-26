# Browserprüfung vom 26.09.2026

Die Prüfung erfolgte auf einer getrennten lokalen Instanz mit temporärer Datenbank,
Testpasswort und einer erzeugten 10-Sekunden-WAV-Datei. Echte Zugangsdaten und
Aufnahmen wurden nicht verwendet.

## Erfolgreich geprüft

- Administrator-Anmeldung über das Formular.
- Set erfassen, ohne die optionalen Felder BPM und Tonart auszufüllen.
- WAV-Datei über die Dateiauswahl hochladen; Bestätigung erscheint.
- Audioplayer lädt die Aufnahme und erkennt die Dauer (10 Sekunden).
- Freigabelink erstellen und nach Abmeldung als Gast öffnen.
- Gastkommentar bei Sekunde 3 speichern; Text und Zeitmarke werden angezeigt.
- Klick auf 0:03 setzt die Abspielposition auf Sekunde 3 (DOM geprüft).
- Gastansicht bei 390 × 844 Pixeln: kein horizontaler Überlauf.
- Administrator sieht den Gastkommentar nach erneutem Anmelden.
- Freigabe widerrufen: Gast erhält nach Neuladen keinen Player und keine Kommentare.
- Abmelden entfernt die Administratoransicht.

## Korrektur

Der positive Freigabehinweis wird erst nach erfolgreichem Laden des Sets angezeigt.
Bei ungültigem oder widerrufenem Link bleibt nur die Fehlermeldung sichtbar.
Beim Neuladen werden bisherige Karten vor dem Abruf entfernt, damit ein fehlgeschlagener
Abruf keine veraltete Ansicht stehen lässt.

## Grenzen

Die mobile Prüfung erfolgte durch Anpassung der Browserbreite, nicht auf physischem
iPhone/Android. Die WAV-Datei enthält Stille; Klangqualität und mehrstündige echte
Aufnahmen wurden nicht geprüft. Produktionshosting und Spam-Schutz bleiben offen.

API-Tests und ein Docker-Test ergänzen die manuelle Browserprüfung. Der Containertest
prüft insbesondere den Datenerhalt nach Ersetzen des Containers.
