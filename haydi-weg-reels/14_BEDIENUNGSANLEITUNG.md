# Bedienungsanleitung Reel-Studio v38

Stand 09.11.2026 · Studio-Link (privat, v38): **https://claude.ai/artifact/8QEHxEEQYiNQizX9tXVzDz** · Dein bisheriges Studio (v37) bleibt unverändert unter seiner alten Adresse.
Lokal: `studio/reel-studio-v38.html` lässt sich direkt im Browser (Chrome/Edge) öffnen; alle Funktionen außer Cloud-Sync, Datei-Downloads über die Claude-Sicherung und KI-Produktionsplan laufen auch lokal.

## 1 Aufbau

- **Kopfzeile:** Hauptplan 09.11.2026–05.02.2027, Statistik (Reels mit Audio, freigegeben, exportiert, gepostet), Bibliothek (Logo, Sounds).
- **Seitenleiste:** Plan-Umschalter **Hauptplan 39 / Specials 51 / Alle**, darunter Serien-Filter (Mo/Mi/Fr) und Status-Filter (Monat, Offen, Freigegeben, ohne Audio). Jedes Reel zeigt Datum, Serie/Folge, Fortschrittsbalken, QS/OK-Marke und Posting-Marken.
- **Karten je Reel** (von oben): 1 Content-Studio · 2 Hook-Studio · 3 CapCut-Studio · 4 KI-Produktionsplan (nur im Claude-Viewer) · 5 Sprechtext · 6 Fertiges Video aus CapCut · 7 Voiceover · 8 Audio-Analyse · 9 Hook-Overlay · 10 Untertitel · 11 Beschreibungen · 12 Qualitäts-Studio · 13 Export & Posting.
- **Vorschau rechts:** Handy-Player mit Hook und Untertiteln, Timeline, Tasten (Leertaste = Play/Pause, S = Sound setzen, Strg/Cmd+Z = Rückgängig).

## 2 Arbeitsablauf je Reel (Hauptplan)

1. **Content-Studio lesen:** Behauptung, Auflösung, DACH-Anker, Storytelling-Bogen, Änderungen und offene Punkte. Eigene Notizen eintragen (werden gespeichert).
2. **Hook-Studio:** Fünf bewertete Hooks, Sieger per Radio wählbar. Bei einem Cover auf „Als Hook-Overlay“ tippen – der kurze Text landet als Overlay im Video (Manrope ExtraBold, ein Wort gelb) und in der Kopfzeile; „Als Cover-Headline“ setzt das Thumbnail. Zum Schluss „Hook & Cover geprüft und freigegeben (QA)“ abhaken.
3. **Sprechtext kopieren** → in ElevenLabs (Eleven v3, Stimme Mert_V2) einfügen, MP3/WAV exportieren. Texte sind fertig: Zahlen ausgeschrieben, höchstens drei Audio-Tags, keine Platzhalter.
4. **Voiceover ablegen** (Karte 7): Das Studio liest die Datei lokal, misst die echte Sprechdauer und richtet Untertitel an Pausen und Silben aus. Karte 8 zeigt Dauer, Abweichung zur Schätzung, Segmente, Silbenkerne und Pausen; „Szenen & Untertitel aus Audio neu berechnen“ setzt alles zurück auf die automatische Ausrichtung.
5. **CapCut-Studio:** Der 16-Feld-Schnittplan zeigt jetzt **„Zeiten aus Audio“** statt „vorläufig“: Szenengrenze = Start der ersten Untertitelzeile der Szene. „Schnittplan kopieren“, CSV/Markdown/JSON oder gleich das **Produktionspaket (ZIP)** mit Schnittplan, Sprechtext, SRT, Hooks, Cover, Stock, Fakten, Captions und Audio. In CapCut: Clips nach Plan setzen, VO darunter, Musik −18 dB, Export 1080×1920 oder 2160×3840 **ohne** Text und Untertitel.
6. **Fertiges Video ablegen** (Karte 6): Das Studio erkennt den Versatz der Stimme im Video, legt Hook-Overlay und Untertitel darüber.
7. **Untertitel prüfen** (Karte 10): Player starten; sitzt eine Zeile nicht, in der Tabelle „Untertitel-Zeiten je Zeile“ Start/Ende in Sekunden ändern (sofort wirksam), ± 0,1 s für alle, oder „Zurück auf automatisch“. Alternativ ElevenLabs-Speech-to-Text-JSON/SRT importieren (wortgenau) oder tappen.
8. **Qualitäts-Studio:** Scorecard-Regler (gewichtet, Ziel ≥ 9,0 – ehrlich bewerten), Faktencheck abhaken, Materialcheck je Clip (offen / geprüft & lizenziert / ersetzt / nicht nötig), Vortags-Checkliste. **Freigabe** geht erst, wenn Fakten, Material, Vortags-Prüfung und Hook-QA erledigt sind – sonst erklärt das Studio, was fehlt. Verbesserungen ins Protokoll tippen (Enter).
9. **Export & Posting:** Video exportieren (MP4, Hook + Untertitel eingebrannt, −14 LUFS), Cover-PNG, Beschreibungen kopieren (≤ 5 Hashtags Instagram), Häkchen „Video fertig / Instagram / TikTok“.

## 3 Import und Datensicherung

- **Hauptplan-JSON importieren** (Export-Karte): `data/reels_hauptplan_v2.json` oder eine überarbeitete Fassung im selben Format. Ersetzt Texte, Hooks, Pläne und Fakten der 39 Reels; Audio, Häkchen, Korrekturen bleiben je Reel-ID erhalten. Der Import wird im Browser gespeichert und lässt sich auf die eingebettete Fassung zurücksetzen.
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

## 6 Bekannte Grenzen

- Audio-Analyse ist eine lokale Näherung (Hüllkurve, Silbenkerne, dynamische Programmierung) – kein Spracherkenner. Für wortgenaue Zeiten: ElevenLabs „Speech to Text“ → JSON importieren.
- KI-Produktionsplan und KI-Bildprüfung funktionieren nur im Claude-Viewer (Capability „sample“).
- Downloads laufen im Claude-Viewer über die Sicherungsabfrage; in der lokalen Datei als normaler Browser-Download.
- Getestet in Chromium (Desktop 1440 px, Mobil 390 px); Safari/Firefox nicht geprüft.

## 7 Tests wiederholen

```
node haydi-weg-reels/tests/studio.test.js
```
Ergebnis in `tests/testergebnis.json` und `13_TESTBERICHT.md`.
