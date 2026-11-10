# Testbericht Reel-Studio v39 (Daten v4 · Final-Audit)

Stand: 2026-11-10 23:12 UTC · Testlauf automatisiert mit Playwright/Chromium (headless) gegen `studio/reel-studio-v39.html` (lokale Datei, Daten v4) · 38 Prüfungen, 38 bestanden, 0 fehlgeschlagen · Laufzeit 22 s.

Testdaten: synthetische, sprachähnliche Audiodatei `tests/vo_test.wav` (20,04 s) und `tests/vo_test.mp3`. **Eine echte ElevenLabs-Aufnahme lag nicht vor** – Audio-Analyse und Untertitel-Ausrichtung sind mit dem Testsignal geprüft, nicht mit echter Stimme. T01–T19 = Regression v38, T20–T24 = v39-Felder, T25 = Audit-Gewichte aus den Daten. Oberfläche und Funktionen des Studios wurden im v4-Schritt nicht verändert (nur Daten eingespielt).

| Nr | Prüfung | Ergebnis | Detail |
|---|---|---|---|
| T01 | Studio lädt ohne JavaScript-Fehler | ✅ bestanden | keine Fehler |
| T02 | Hauptplan 39 Reels geladen, 51 Specials erhalten | ✅ bestanden | main=39 specials=51 alle=90 |
| T02b | IDs H01–H39 vollständig und eindeutig | ✅ bestanden | H01,H02,H03… |
| T03 | Alle Studio-Karten vorhanden | ✅ bestanden | Content-Studio – Konzept & Produktionsstatus / Hook-Studio – 5 Hooks (Bild · Satz · Overlay · Frage), Bewertung, Sieger & 3 Cover / CapCut-Studio – vollständiger Schnittplan (16 Felder je Szene) / KI- |
| T04 | Hook-Studio: 5 bewertete Hooks, Sieger wechselbar und gespeichert | ✅ bestanden | rows=5 pick=3 |
| T04b | 195 Hooks mit je 7 Kriterien bewertet | ✅ bestanden | 39 × 5 = 195 |
| T05 | Cover: 3 Konzepte, Übernahme als Hook-Overlay wirkt auf Kopfzeile | ✅ bestanden | hook="1910 ausgebrannt, *1991* Hotel" |
| T05b | 117 Cover-Konzepte insgesamt | ✅ bestanden | 117 |
| T06 | Sprechtexte: 39 vollständig, Zahlen ausgeschrieben, ≤3 Tags, keine Platzhalter, 35–120 Wörter (Länge folgt der Geschichte) | ✅ bestanden | alle ok |
| T06b | Sprechtext-Kopierknopf vorhanden | ✅ bestanden |  |
| T07 | CapCut-Plan: 16 Felder je Szene, Timecodes HH:MM:SS:FF, Status vorläufig ohne Audio | ✅ bestanden | rows=8 cols=18 badge=Zeiten vorläufig |
| T07b | Alle 39 Schnittpläne mit vollständigen Feldern | ✅ bestanden |  |
| T08 | Timecode-Mathematik (30 fps, HH:MM:SS:FF, lückenlose Szenen, Summe = Gesamt) | ✅ bestanden | {"a":true,"b":true,"c":true,"d":true,"cont":true,"sum":true,"t":"00:01:01:01"} |
| T09 | Audio-Upload WAV: Datei gespeichert, reale Dauer erkannt, CapCut-Zeiten „aus Audio“ | ✅ bestanden | dur=20.043990929705217 badge=Zeiten aus Audio letzte Szene Ende=00:00:22:20 |
| T09b | Audio-Analyse zeigt Segmente, Silbenkerne und Abweichung zur Schätzung | ✅ bestanden | 8Audio-Analyse – reale Sprechdauer & SynchronisationDateivo_test.wavReale Sprechdauer00:00:20:01 (20.04 s)Schätzung vorher00:00:38:11 → Abweichung −18.3 sSprechtempo4.69 Wörter/s (94 Wörter)Sprachsegm |
| T11 | Untertitel aus Audio: Zeilen monoton, erste ≥ Stimmstart, letzte ≤ Audioende | ✅ bestanden | {"n":20,"first":0.2,"last":19.670000000000005,"mono":true,"dur":20.043990929705217,"vs":0.1} |
| T12 | Manuelle Zeitkorrektur je Zeile wird übernommen und gespeichert | ✅ bestanden | {"src":"manual","n":20,"t2":1.23} |
| T12b | Zurück auf automatische Zeiten | ✅ bestanden |  |
| T13 | Speicherung: Audio, Notizen und Hook-Wahl überleben das Neuladen (localStorage + IndexedDB) | ✅ bestanden | {"cur":"H03","vo":"vo_test.wav","notes":"Testnotiz 123","pick":3,"have":true} |
| T10 | Audio-Upload MP3: dekodiert, Dauer erkannt | ✅ bestanden | {"real":true,"dur":20.043990929705217} |
| T14 | Export CapCut-Schnittplan CSV | ✅ bestanden | haydi-weg_2026-11-16_H04_stammt-das-matterhorn-aus-afrika_capcut.csv |
| T14b | Export Produktionspaket ZIP (Schnittplan, Sprechtext, SRT, Hooks, Cover, Stock, Fakten, Captions, Audio) | ✅ bestanden | haydi-weg_2026-11-16_H04_stammt-das-matterhorn-aus-afrika_produktionspaket.zip |
| T14c | Export SRT mit Zeitstempeln | ✅ bestanden | haydi-weg_2026-11-16_H04_stammt-das-matterhorn-aus-afrika_untertitel.srt |
| T14d | Export Gesamtpaket aller 39 (ZIP) | ✅ bestanden | haydi-weg_hauptplan_2026-11-09_bis_2027-02-05.zip |
| T15 | Freigabe ohne Fakten-/Material-/Hook-Check wird blockiert (mit Hinweis) | ✅ bestanden | Freigabe erst, wenn Faktencheck, Materialcheck, Vortags-Prüfung und Hook-QA abgehakt sind. |
| T15b | Ungültige Import-Datei wird abgewiesen | ✅ bestanden | Kein Hauptplan-Format (reels_hauptplan_v2) erkannt. |
| T16 | Hauptplan-JSON-Import ersetzt Inhalte, behält Studio-Zustand (Audio) je Reel-ID | ✅ bestanden | title=TEST-IMPORT Matterhorn vo=vo_test.mp3 |
| T16b | Importierter Hauptplan überlebt Neuladen und lässt sich auf die eingebettete Fassung zurücksetzen | ✅ bestanden | TEST-IMPORT Matterhorn |
| T20 | Themenwelt-Filter (4 Themenwelten) filtert die Liste | ✅ bestanden | chips=5 Hotel-Legenden=20 |
| T21 | Schlüsselaufnahmen: 3 je Reel (117) mit ehrlichem Status, Tabelle in Content-Studio | ✅ bestanden | {"n":117,"valid":true,"roles":39,"found":78,"missing":7,"missNote":true} |
| T21b | Materialstatus einer Schlüsselaufnahme wird gespeichert | ✅ bestanden |  |
| T22 | Hooks: 195 mit Bild + Satz + Overlay + Frage, 5 feste Typen, Overlay ins Video übernehmbar | ✅ bestanden | {"n":195,"comp":true,"types":true} |
| T23 | Plan v3: Strukturen A–E, nie zweimal hintereinander gleich, Längen 22–42 s variabel, 4 Themenwelten, Freitag „Reisewissen“ | ✅ bestanden | {"structures":"ABCDE","consecutive":false,"min":26.51,"max":46.09,"sd":4.31,"rw":"Reisewissen","tw":4} |
| T24 | Studio-Zustand als JSON (Schema v39) exportierbar | ✅ bestanden | haydi-weg_studio_zustand.json |
| T25 | Qualitäts-Studio rechnet mit den Audit-Gewichten aus den Daten | ✅ bestanden | {"w":{"hook":25,"visual":25,"story":20,"share":15,"dach":5,"facts":10},"d":{"hook":25,"visual":25,"story":20,"share":15,"dach":5,"facts":10},"tot":9,"ref":9} |
| T17 | Specials (v37-Daten) rendern unverändert, ohne Hauptplan-Karten | ✅ bestanden | special=V-N01 cards=9 |
| T18 | Mobile Ansicht (390 px): kein horizontales Scrollen, Reel-Auswahl mit allen Reels | ✅ bestanden | {"sw":390,"iw":390,"pick":90} |
| T19 | Keine JavaScript-Fehler während der gesamten Testfahrt | ✅ bestanden | keine |

## Zuordnung zu den geforderten Tests

| Gefordert | Prüfungen |
|---|---|
| Import | T02, T02b, T15b, T16, T16b |
| Speicherung | T13, T16b, T21b |
| Navigation | T02, T17, T18, T20 |
| Vorschau | T05, T22 |
| Hook-Bewertungen | T04, T04b, T22 |
| Audio-Upload | T09, T09b, T10 |
| Untertitel | T11, T12, T12b, T14c |
| Export | T14, T14b, T14c, T14d, T24 |
| Plan v4 | T21, T23, T25 |

## Nicht getestet (ehrlich)

- Echte ElevenLabs-Audiodatei (Stimme Mert_V2).
- Browser außer Chromium.
- Veröffentlichung auf Instagram/TikTok (nicht Teil des Auftrags).
- Download/Lizenzierung echter Stock-Clips und Hotel-Pressematerial (keine Käufe ohne Freigabe).

## Screenshots

- `tests/v39_content_studio_H03.png`, `tests/v39_schluesselaufnahmen_H03.png`, `tests/v39_hook_studio_H03.png`, `tests/v39_themenwelt_filter.png`, `tests/v39_mobile_390.png` (Fassung v39/v3) · v4-Screenshots: `tests/v4_*.png`

## Wiederholen

```
cd haydi-weg-reels/tests && node studio.test.js ../studio/reel-studio-v39.html
```