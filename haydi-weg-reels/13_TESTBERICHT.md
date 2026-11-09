# Testbericht Reel-Studio v38

Stand: 2026-11-09 03:49 UTC · Testlauf automatisiert mit Playwright/Chromium (headless) gegen `studio/reel-studio-v38.html` (lokale Datei) · 31 Prüfungen, 31 bestanden, 0 fehlgeschlagen · Laufzeit 18 s.

Testdaten: synthetische, sprachähnliche Audiodatei `tests/vo_test.wav` (20,04 s, Silben-Bursts und Satzpausen) sowie daraus erzeugte `tests/vo_test.mp3`. **Eine echte ElevenLabs-Aufnahme lag in dieser Sitzung nicht vor** (kein Konto/Kosten) – die Analyse (Hüllkurve, Segmente, Silbenkerne, Alignment) wurde mit dem synthetischen Signal geprüft; mit echter Sprache ist das Verfahren identisch, die Trefferqualität der Silben-Erkennung muss am ersten echten Reel in der Vorschau kontrolliert werden.

| Nr | Prüfung | Ergebnis | Detail |
|---|---|---|---|
| T01 | Studio lädt ohne JavaScript-Fehler | ✅ bestanden | keine Fehler |
| T02 | Hauptplan 39 Reels geladen, 51 Specials erhalten | ✅ bestanden | main=39 specials=51 alle=90 |
| T02b | IDs H01–H39 vollständig und eindeutig | ✅ bestanden | H01,H02,H03… |
| T03 | Alle Studio-Karten vorhanden | ✅ bestanden | Content-Studio – Konzept & Produktionsstatus / Hook-Studio – 5 Hooks, Bewertung, Sieger & 3 Cover / CapCut-Studio – vollständiger Schnittplan (16 Felder je Szene) / KI-Produktionsplan / Sprechtext für ElevenLabs / Fertiges Video aus CapCut / Voiceover – damit die Untertitel exakt sitzen / Audio-Analyse – reale Sprechdauer / Hook – Schlagzeile am Anfang / Untertitel / Beschreibung für Instagram, Ti |
| T04 | Hook-Studio: 5 bewertete Hooks, Sieger wechselbar und gespeichert | ✅ bestanden | rows=5 pick=2 |
| T04b | 195 Hooks mit je 7 Kriterien bewertet | ✅ bestanden | 39 × 5 = 195 |
| T05 | Cover: 3 Konzepte, Übernahme als Hook-Overlay wirkt auf Kopfzeile | ✅ bestanden | hook="*×4* Hotelbetten seit 2002" |
| T05b | 117 Cover-Konzepte insgesamt | ✅ bestanden | 117 |
| T06 | Sprechtexte: 39 vollständig, Zahlen ausgeschrieben, ≤3 Tags, keine Platzhalter, 50–95 Wörter | ✅ bestanden | alle ok |
| T06b | Sprechtext-Kopierknopf vorhanden | ✅ bestanden |  |
| T07 | CapCut-Plan: 16 Felder je Szene, Timecodes HH:MM:SS:FF, Status vorläufig ohne Audio | ✅ bestanden | rows=7 cols=18 badge=Zeiten vorläufig |
| T07b | Alle 39 Schnittpläne mit vollständigen Feldern | ✅ bestanden |  |
| T08 | Timecode-Mathematik (30 fps, HH:MM:SS:FF, lückenlose Szenen, Summe = Gesamt) | ✅ bestanden | {"a":true,"b":true,"c":true,"d":true,"cont":true,"sum":true,"t":"00:01:01:01"} |
| T09 | Audio-Upload WAV: Datei gespeichert, reale Dauer erkannt, CapCut-Zeiten „aus Audio“ | ✅ bestanden | dur=20.043990929705217 badge=Zeiten aus Audio letzte Szene Ende=00:00:20:20 |
| T09b | Audio-Analyse zeigt Segmente, Silbenkerne und Abweichung zur Schätzung | ✅ bestanden | 8Audio-Analyse – reale Sprechdauer & SynchronisationDateivo_test.wavReale Sprechdauer00:00:20:01 (20.04 s)Schätzung vorher00:00:33:26 → Abweichung −13.8 sSprechtempo4.14 Wörter/s (83 Wörter)Sprachsegmente6 erkannt · erstes ab 00:00:00:03Silbenkerne61 erkannt ( |
| T11 | Untertitel aus Audio: Zeilen monoton, erste ≥ Stimmstart, letzte ≤ Audioende | ✅ bestanden | {"n":23,"first":0.2,"last":19.670000000000005,"mono":true,"dur":20.043990929705217,"vs":0.1} |
| T12 | Manuelle Zeitkorrektur je Zeile wird übernommen und gespeichert | ✅ bestanden | {"src":"manual","n":23,"t2":1.24} |
| T12b | Zurück auf automatische Zeiten | ✅ bestanden |  |
| T13 | Speicherung: Audio, Notizen und Hook-Wahl überleben das Neuladen (localStorage + IndexedDB) | ✅ bestanden | {"cur":"H03","vo":"vo_test.wav","notes":"Testnotiz 123","pick":2,"have":true} |
| T10 | Audio-Upload MP3: dekodiert, Dauer erkannt | ✅ bestanden | {"real":true,"dur":20.043990929705217} |
| T14 | Export CapCut-Schnittplan CSV | ✅ bestanden | haydi-weg_2026-11-16_H04_stammt-das-matterhorn-aus-afrika_capcut.csv |
| T14b | Export Produktionspaket ZIP (Schnittplan, Sprechtext, SRT, Hooks, Cover, Stock, Fakten, Captions, Audio) | ✅ bestanden | haydi-weg_2026-11-16_H04_stammt-das-matterhorn-aus-afrika_produktionspaket.zip |
| T14c | Export SRT mit Zeitstempeln | ✅ bestanden | haydi-weg_2026-11-16_H04_stammt-das-matterhorn-aus-afrika_untertitel.srt |
| T14d | Export Gesamtpaket aller 39 (ZIP) | ✅ bestanden | haydi-weg_hauptplan_2026-11-09_bis_2027-02-05.zip |
| T15 | Freigabe ohne Fakten-/Material-/Hook-Check wird blockiert (mit Hinweis) | ✅ bestanden | Freigabe erst, wenn Faktencheck, Materialcheck, Vortags-Prüfung und Hook-QA abgehakt sind. |
| T15b | Ungültige Import-Datei wird abgewiesen | ✅ bestanden | Kein Hauptplan-Format (reels_hauptplan_v2) erkannt. |
| T16 | Hauptplan-JSON-Import ersetzt Inhalte, behält Studio-Zustand (Audio) je Reel-ID | ✅ bestanden | title=TEST-IMPORT Matterhorn vo=vo_test.mp3 |
| T16b | Importierter Hauptplan überlebt Neuladen und lässt sich auf die eingebettete Fassung zurücksetzen | ✅ bestanden | TEST-IMPORT Matterhorn |
| T17 | Specials (v37-Daten) rendern unverändert, ohne Hauptplan-Karten | ✅ bestanden | special=V-N01 cards=9 |
| T18 | Mobile Ansicht (390 px): kein horizontales Scrollen, Reel-Auswahl mit allen Reels | ✅ bestanden | {"sw":390,"iw":390,"pick":90} |
| T19 | Keine JavaScript-Fehler während der gesamten Testfahrt | ✅ bestanden | keine |

## Zuordnung zu den geforderten Tests

| Anforderung | Abgedeckt durch | Status |
|---|---|---|
| Import der 39 Reels | T02, T02b, T16, T16b | bestanden |
| Hook-Bewertungen | T04, T04b | bestanden |
| Cover-Varianten | T05, T05b | bestanden |
| Sprechertexte | T06, T06b | bestanden |
| CapCut-Pläne | T07, T07b | bestanden |
| Timecode-Mathematik | T08 | bestanden |
| Audio-Upload und Analyse | T09, T09b, T10 (WAV + MP3, synthetisch) | bestanden – echte ElevenLabs-Datei offen |
| Untertitel-Synchronisation | T11 | bestanden |
| Manuelle Korrekturen | T12, T12b | bestanden |
| Speicherung | T13 (localStorage + IndexedDB, Neuladen) | bestanden |
| Exporte | T14 (CSV), T14b (ZIP je Reel), T14c (SRT), T14d (Gesamt-ZIP) | bestanden |
| Fehlerbehandlung | T15 (Freigabe-Sperre), T15b (ungültiger Import) | bestanden |
| Desktop | 1440 × 1000 px (alle Tests) | bestanden |
| Mobile | T18 (390 × 844 px, kein horizontales Scrollen, Reel-Auswahl) | bestanden |
| Specials-Regression | T17 | bestanden |
| Video-Export (MP4/WebM), Cover-PNG | nicht automatisiert (WebCodecs/MediaRecorder in headless Chromium ohne GPU unzuverlässig); Funktionen aus v37 unverändert übernommen | nicht geprüft |
| KI-Produktionsplan, KI-Bildprüfung (Claude-`sample`) | nur im Claude-Viewer verfügbar; nicht in der lokalen Datei testbar | nicht geprüft |
| Cloud-Sync (`db`) | neues Artefakt startet mit leerer Datenbank; Schreiben ab erstem Klick im Viewer | Funktionsprüfung: siehe Übergabe |
| Safari/Firefox | nicht getestet (nur Chromium verfügbar) | nicht geprüft |
| Higgsfield-Vorabcheck > 80 | kostenpflichtig, nicht ausgeführt | nicht geprüft |

## Screenshots

- `tests/screenshot_v38_desktop.png` (1400 px)
- `tests/screenshot_v38_mobile.png` (390 px)

## Wiederholen

```
node haydi-weg-reels/tests/studio.test.js   # Playwright und Chromium müssen installiert sein
```