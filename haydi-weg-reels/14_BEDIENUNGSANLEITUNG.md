# Bedienungsanleitung Reel-Studio v39 (Hauptplan v4 · Final-Audit)

Stand 09.11.2026 · Studio-Link (privat, aktualisiert auf v39): **https://claude.ai/artifact/8QEHxEEQYiNQizX9tXVzDz** · Dein bisheriges Studio (v37) bleibt unverändert unter seiner alten Adresse; v38 liegt als Sicherung in `backup/reel-studio-v38-vor-upgrade.html`.
Lokal: `studio/reel-studio-v39.html` lässt sich direkt im Browser (Chrome/Edge) öffnen; alle Funktionen außer Cloud-Sync, Datei-Downloads über die Claude-Sicherung und KI-Produktionsplan laufen auch lokal.

## 1 Aufbau

- **Kopfzeile:** Hauptplan 09.11.2026–05.02.2027, Statistik (Reels mit Audio, freigegeben, exportiert, gepostet), Bibliothek (Logo, Sounds).
- **Seitenleiste:** Plan-Umschalter **Hauptplan 39 / Specials 51 / Alle**, darunter Serien-Filter (Mo/Mi/Fr), **Themenwelt-Filter (Natur-Wunder · Hotel-Legenden · Regeln & Realität · Alte Welten)** und Status-Filter (Monat, Offen, Freigegeben, ohne Audio). Jedes Reel zeigt Datum, Serie/Folge, Strukturbuchstabe A–E, Fortschrittsbalken, QS/OK-Marke und Posting-Marken.
- **Karten je Reel** (von oben): 1 Content-Studio · 2 Hook-Studio · 3 CapCut-Studio · 4 KI-Produktionsplan (nur im Claude-Viewer) · 5 Sprechtext · 6 Fertiges Video aus CapCut · 7 Voiceover · 8 Audio-Analyse · 9 Hook-Overlay · 10 Untertitel · 11 Beschreibungen · 12 Qualitäts-Studio · 13 Export & Posting.
- **Vorschau rechts:** Handy-Player mit Hook und Untertiteln, Timeline, Tasten (Leertaste = Play/Pause, S = Sound setzen, Strg/Cmd+Z = Rückgängig).

## 2 Arbeitsablauf je Reel (Hauptplan)

1. **Content-Studio lesen:** Themenwelt, Storytelling-Struktur (A Mystery → Enthüllung · B Erwartung → Realität · C Historischer Konflikt → Wendepunkt · D Visuelles Rätsel → Erklärung · E Erlebnis → Haken), Upgrade-Entscheidung mit altem Titel und Begründung, konkretes Hotel/Resort, Ziel-Länge, Endkarte, Behauptung, DACH-Anker, Storytelling-Bogen. **Schlüsselaufnahmen – Material zuerst:** drei Zeilen (Scroll-Stop / Story / Reveal) mit Status aus der Recherche vom 09.11. (✅ gefunden · 🟡 verfügbar, ungeprüft · ❌ nicht gefunden mit Alternative) und einem eigenen Status-Feld (offen / geprüft & lizenziert / ersetzt / nicht nötig), das gespeichert wird. Eigene Notizen eintragen.
2. **Hook-Studio:** Fünf Hooks je Reel (Visueller Schock · Neugierlücke · Überraschende Behauptung · Emotionaler Konflikt · Erwartung gegen Realität), jeder als Kombination aus **erstem Bild ohne Ton, gesprochenem Einstieg, Text-Overlay und offener Frage**, sieben Kriterien bewertet, Sieger per Radio wählbar. „Overlay“ in der Hook-Zeile übernimmt das Text-Overlay dieses Hooks ins Video (Manrope ExtraBold, ein Wort gelb) und in die Kopfzeile; bei einem Cover setzt „Als Hook-Overlay“ die Cover-Headline als Overlay, „Als Cover-Headline“ das Thumbnail. Standard ist das Overlay des Sieger-Hooks. Zum Schluss „Hook & Cover geprüft und freigegeben (QA)“ abhaken.
3. **Sprechtext kopieren** → in ElevenLabs (Eleven v3, Stimme Mert_V2) einfügen, MP3/WAV exportieren. Texte sind fertig: Zahlen ausgeschrieben, höchstens drei Audio-Tags, keine Platzhalter. Längen folgen der Geschichte (22–42 s); wo die Endkarte „Teaser nur Grafik“ sagt, endet der Sprechtext mit der Pointe – der Teaser steht nur auf der Endkarte.
4. **Voiceover ablegen** (Karte 7): Das Studio liest die Datei lokal, misst die echte Sprechdauer und richtet Untertitel an Pausen und Silben aus. Karte 8 zeigt Dauer, Abweichung zur Schätzung, Segmente, Silbenkerne und Pausen; „Szenen & Untertitel aus Audio neu berechnen“ setzt alles zurück auf die automatische Ausrichtung.
5. **CapCut-Studio:** Der 16-Feld-Schnittplan zeigt jetzt **„Zeiten aus Audio“** statt „vorläufig“: Szenengrenze = Start der ersten Untertitelzeile der Szene. „Schnittplan kopieren“, CSV/Markdown/JSON oder gleich das **Produktionspaket (ZIP)** mit Schnittplan, Sprechtext, SRT, Hooks, Cover, Stock, Fakten, Captions und Audio. In CapCut: Clips nach Plan setzen, VO darunter, Musik −18 dB, Export 1080×1920 oder 2160×3840 **ohne** Text und Untertitel.
6. **Fertiges Video ablegen** (Karte 6): Das Studio erkennt den Versatz der Stimme im Video, legt Hook-Overlay und Untertitel darüber.
7. **Untertitel prüfen** (Karte 10): Player starten; sitzt eine Zeile nicht, in der Tabelle „Untertitel-Zeiten je Zeile“ Start/Ende in Sekunden ändern (sofort wirksam), ± 0,1 s für alle, oder „Zurück auf automatisch“. Alternativ ElevenLabs-Speech-to-Text-JSON/SRT importieren (wortgenau) oder tappen.
8. **Qualitäts-Studio:** Scorecard-Regler (gewichtet, Ziel ≥ 9,0 – ehrlich bewerten, Score ersetzt keine Prüfung), Faktencheck abhaken, Materialcheck je Clip (offen / geprüft & lizenziert / ersetzt / nicht nötig) plus die drei Schlüsselaufnahmen mit Recherche-Status, Vortags-Checkliste. **Freigabe** geht erst, wenn Fakten, Material, Vortags-Prüfung und Hook-QA erledigt sind – sonst erklärt das Studio, was fehlt. Verbesserungen ins Protokoll tippen (Enter).
9. **Export & Posting:** Video exportieren (MP4, Hook + Untertitel eingebrannt, −14 LUFS), Cover-PNG, Beschreibungen kopieren (≤ 5 Hashtags Instagram), Häkchen „Video fertig / Instagram / TikTok“.

## 3 Import und Datensicherung

- **Hauptplan-JSON importieren** (Export-Karte): `data/reels_hauptplan_v3.json` oder eine überarbeitete Fassung im selben Format (v2-Dateien werden weiterhin gelesen, zeigen dann aber keine Themenwelt/Struktur/Schlüsselaufnahmen). Ersetzt Texte, Hooks, Pläne und Fakten der 39 Reels; Audio, Häkchen, Korrekturen bleiben je Reel-ID erhalten. Der Import wird im Browser gespeichert und lässt sich auf die eingebettete Fassung zurücksetzen.
- **Studio-Zustand sichern (JSON)** und **wiederherstellen**: alle Häkchen, Notizen, Zeiten, Scorecards. Vor einem Gerätewechsel sichern. Hochgeladene Dateien (Audio, Video, Clips) liegen nur im Browser des jeweiligen Geräts.
- **Gesamt-ZIP aller 39:** Schnittpläne (CSV/MD), Hooks, Sprechtexte, SRT, Kalender, Studio-Zustand.
- Im Claude-Viewer werden Texte, Häkchen und Zeiten zusätzlich im Konto gespeichert (Cloud-Sync); lokal nur im Browser.

## 4 Specials (51 Reels aus v37)

Über den Plan-Umschalter erreichbar; alle bisherigen Funktionen (Produktionspaket, Material-Plan, Auto-Schnitt, Hook, Untertitel, Export) sind unverändert. Eigene Antalya-Hotelvideos gehören hierher, nicht in den Hauptplan.

## 5 Regeln, die das Studio durchsetzt oder anzeigt

- Keine Untertitel, solange der Hook steht; Hook ≤ 2 Zeilen, ein Schlüsselwort gelb; Logo weiß unten rechts ab Sekunde 3; Serienkarte am Ende.
- Timecodes ohne Audio = vorläufig (Kennzeichnung in Karte und Export). Keine framegenauen Zeiten werden vorgetäuscht.
- Freigabe nur mit Faktencheck, Materialcheck, Vortags-Prüfung und Hook-QA.
- Keine Preise, keine Verkaufs-CTAs, keine Links in Reels oder Captions (Qualitätsprüfung im Export warnt).

## 5a Fassung v4 (Final-Audit, 10.11.2026)

- Oberfläche und Funktionen sind unverändert; eingespielt wurden nur die Daten v4 (`data/reels_hauptplan_v4.json`). Die Scorecard-Gewichte liest das Studio jetzt aus den Daten (Final-Audit: Hook 25 · Visuell 25 · Story 20 · Share/Follow 15 · DACH 5 · Fakten 10).
- Hook-Typen v4: Visueller Schock · Neugierlücke · Überraschende Behauptung · Erwartung gegen Realität · Emotionaler WOW-Moment.
- Hotel-Reels zeigen im Content-Studio Hotel/Resort, DACH-Begründung und Dubletten-Status; Reels ohne nachgewiesenes Hotelmaterial stehen auf „Material offen – nicht produktionsbereit“ und lassen sich erst nach Materialnachweis freigeben.
- Rückkehr zur v3-Fassung: `backup/reels_hauptplan_v3-vor-hotelaudit.json` über „Hauptplan-JSON importieren“.

## 6 Bekannte Grenzen

- Audio-Analyse ist eine lokale Näherung (Hüllkurve, Silbenkerne, dynamische Programmierung) – kein Spracherkenner. Für wortgenaue Zeiten: ElevenLabs „Speech to Text“ → JSON importieren.
- KI-Produktionsplan und KI-Bildprüfung funktionieren nur im Claude-Viewer (Capability „sample“).
- Downloads laufen im Claude-Viewer über die Sicherungsabfrage; in der lokalen Datei als normaler Browser-Download.
- Getestet in Chromium (Desktop 1440 px, Mobil 390 px); Safari/Firefox nicht geprüft.
- Die Datei „haydi-weg Reel-Studio_Final(1).html“ aus dem Auftrag lag in dieser Umgebung nicht vor; Basis des Upgrades ist das v38-Studio dieser Übergabe (das selbst auf dem byteidentisch gesicherten v37 aufsetzt). Falls „Final(1)“ eine andere Fassung ist, bitte hochladen – die v39-Erweiterung ist als Patch (`v39_patch.js`) auf jede v37/v38-Fassung übertragbar.

## 7 Tests wiederholen

```
node haydi-weg-reels/tests/studio.test.js haydi-weg-reels/studio/reel-studio-v39.html
```
Ergebnis in `tests/testergebnis.json` und `13_TESTBERICHT.md`.
