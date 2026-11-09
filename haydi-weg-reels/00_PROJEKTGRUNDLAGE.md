# haydi-weg Reel-Produktion – Konsolidierte Projektgrundlage

Stand: 09.11.2026 (Nachtlauf, autonome Bearbeitung) · Branch `claude/haydi-weg-reel-produktion-kojny0`
Auftraggeber: haydi-weg Reisen, Minden (Mert) · Kanal: Instagram primär, TikTok sekundär, YouTube Shorts optional

---

## 1 Verbindlicher Ausgangsplan

**Identifiziert und als Basis festgelegt:**
„haydi-weg Reel-Masterplan 09.11.2026–05.02.2027“ (Claude-Docs-Artefakt, 7 Tabs; PDF-Fassung `01_haydi-weg_Masterplan.pdf`, Stand 06.11.2026).

Eindeutige Merkmale, die den richtigen Plan vom älteren unterscheiden:

| Merkmal | Verbindlicher Plan (06.11.2026) | Älterer Plan im Reel-Studio v37 |
|---|---|---|
| Zeitraum | 09.11.2026–05.02.2027, 13 Wochen | 04.11.2026–30.01.2027 |
| Umfang | 39 Reels, Mo/Mi/Fr | 51 „Hotelgeschichten“-Specials, 17 pro Monat |
| Serien | Mo „Fakt oder Fake?“, Mi „Was dir keiner sagt“, Fr „Reisewissen in 30 Sekunden“ | ohne feste Serien (kind info/wow) |
| Erstes / letztes Reel | 01 Düden-Wasserfall (09.11.) / 39 Elafonisi (05.02.) | V-N01 … V-J17 |
| Bewertung | Redaktion 8,34 · Zweitbewertung 6,50 · Konsens 7,42 | Audit alter Plan: 4,83 |

Der Masterplan ist **Grundlage, keine unveränderliche Themenliste**. Themen dürfen laut Auftrag ersetzt werden, wenn Material, Fakten oder Reichweitenpotenzial nicht tragen. Alle Abweichungen stehen in `11_AENDERUNGSPROTOKOLL.md`.

### 1.1 Zugehörige Dateien laut Masterplan (Tab 1, „Aufbau und Dateien“)

| Datei | Status am 09.11.2026 |
|---|---|
| 01_haydi-weg_Masterplan.pdf | Inhalt vollständig über das Claude-Docs-Artefakt gelesen (Tabs 1–5 und 7 vollständig, Tab 6 KPI & Tests vollständig gelesen, Export in Tab 6 wegen Größe nur als Lesefassung) |
| 02_haydi-weg_ReelStudio_Import.xlsx / .csv / .json | **Nicht zugänglich.** Die Dateien liegen laut Plan in Google Drive; in dieser Sitzung besteht kein Zugriff auf Google Drive und keine Datei dieses Namens in zugänglichen Quellen. Sie werden aus dem gelesenen Planinhalt **neu erzeugt** (siehe `data/`), nicht „wiederhergestellt“. |
| Bestehendes Reel-Studio | Zugänglich: claude.ai-Artefakt „haydi-weg Reel-Studio“, Version 37 (Hooks 05.11.), 3.093.798 Byte, vollständig gesichert |

---

## 2 Quelleninventar – was gelesen wurde, was nicht

### 2.1 Vollständig gelesene Quellen (Kopien in `backup/quelldokumente/`)

| Kürzel | Dokument | Rolle |
|---|---|---|
| MP1 | Masterplan Tab 1 Überblick & Kalender | **verbindlich** |
| MP2–MP4 | Masterplan Tabs 2–4 Briefings Reels 01–39 | **verbindlich** |
| MP5 | Masterplan Tab 5 Skriptpakete Top 12 (Reels 04, 06, 10, 11, 12, 26, 28, 32, 34, 35, 37, 38) | **verbindlich** |
| MP6 | Masterplan Tab 6 KPI & Tests | **verbindlich** (Kernzahlen in `09_KPI_TESTSTRATEGIE.md` übernommen; Textfassung nicht in `backup/quelldokumente/`, da der Export der Tab-Größe wegen nur als Lesefassung vorlag) |
| MP7 | Masterplan Tab 7 Qualitätssicherung & Quellen | **verbindlich** |
| AUDIT | „Audit 39-Reel-Plan DACH“ (Bewertung alter Plan 4,83; Wettbewerber-Tabelle; 10 Mechanismen; 8 Hook-Regeln; 21 Ersatzkandidaten) | Vorarbeit zum Masterplan, Regeln übernommen |
| H_ProductionBible | Production Bible Nov 26–Jan 27 (Produktionsstandards, 21 Pakete für den älteren Plan) | **Standards gelten weiter**, Pakete = Specials |
| H_ReelStrategie | Reel-Strategie Okt/Nov 26 (Formate PLOT-TWIST u. a.) | verworfener Ansatz, nur Ideenquelle |
| H_90Tage | 90-Tage-Strategie Phase 3 (Hotelkanal-Positionierung, Tests T1–T8, 111 Inhalte) | überholt, KPI-Dashboard-Logik teilweise übernommen |
| H_Wettbewerb | Wettbewerbsanalyse Phase 2 | Ideen-/Vergleichsquelle |
| H_SocialAudit2 | Social-Media-Audit 2.0 Phase 1 (Mardan-Ausreißer 217 Follows) | Ist-Analyse, Referenz für KPI-Basis |
| H_Sprechtexte | Sprechtexte ElevenLabs Oktober (Tag-Regeln v4, «»-Platzhalter, Lautschrift) | **Sprecherregeln gelten weiter** |
| H_Growth | Growth-Analyse Okt 26 (13 Serienformate, CTA-Strategie) | Ideenquelle |
| H_ContentPlan | Content-Plan ab 21.10. (Serien A/B/C) | überholt |
| STUDIO v37 | Quellcode Reel-Studio Version 37 inkl. DATA (51 Reels), CC_SHEETS, SFXLIB, MASTER_PROMPT | **Code-Basis, wird erweitert, nicht neu gebaut** |
| REPO | `mertkoese67-ux/strato-ki-backend` (Express-Wrapper `/api/ki-analyse`, Vercel) | keine Reel-Inhalte; bleibt unverändert |

### 2.2 Nicht zugängliche Quellen (ehrlich dokumentiert)

- **Frühere Chat-Verläufe** (claude.ai-Konversationen): kein Zugriff aus dieser Sitzung. Analysiert wurden ausschließlich die daraus entstandenen Dokumente (2.1).
- **Google Drive** (`02_haydi-weg_ReelStudio_Import.*`, eigene Antalya-Hotelvideos, Logo-Dateien): kein Zugriff.
- **Instagram-/TikTok-Insights**: kein Zugriff; alle KPI-Zahlen stammen aus den Dokumenten (2.652 IG-Follower am 06.11.2026 laut Tab 6).
- **Pexels-/Pixabay-Detailseiten**: Suchseiten liefern aus dieser Umgebung HTTP 403, Suchoperatoren werden ignoriert. Die im Plan genannten Clip-IDs (Recherche 06.11.2026) konnten am 09.11.2026 **nicht erneut geöffnet** werden. Lizenzstatus im Stockprotokoll ist daher „laut Plan-Recherche 06.11.2026, am 09.11. nicht nachgeprüft“, nie „geprüft“.
- **Envato Elements**: kein Konto in dieser Sitzung; Suchbegriffe werden geliefert, Treffer nicht.
- **ElevenLabs-Konto / Stimme „Mert_V2“**: keine Audioerzeugung in dieser Sitzung (kostenpflichtig, nicht freigegeben). Tests der Audio-Analyse laufen mit lokal erzeugten WAV-Dateien.
- **Higgsfield-Vorabcheck (> 80)**: nicht ausgeführt (kostenpflichtig, keine Freigabe). Bleibt Freigabebedingung des Plans und offener Punkt.

---

## 3 Verbindliche Entscheidungen (gelten für alle 39 Reels)

**Strategie und Ton**
1. Unterhaltsamer DACH-Reiseentdeckungskanal; Prioritäten: Reichweite, erste Sekunden, Wiedergabedauer, Shares/Saves, Follower, Premium-Marke, Vertrauen.
2. **Bis 31.12.2026 keine Verkaufs-CTAs** in Reels oder Captions; ab Februar 2027 höchstens eine dezente Profilzeile, nicht im Reel.
3. **Keine Personen vor der Kamera.** Keine Gesichter in Großaufnahme in Stockclips.
4. **Eigene Antalya-Hotelvideos und Vlogs bleiben separate Specials** außerhalb der 39 Haupt-Reels. Im Studio: die 51 bestehenden Reels (V-N/V-D/V-J) bleiben als „Specials“ erhalten und bearbeitbar.
5. Hauptplan ausschließlich mit **korrekt zugeordnetem, rechtmäßig nutzbarem Fremdmaterial**; keine falschen Drehorte, keine erfundenen Quellen oder Lizenzen; fehlt ein Schlüsselclip realistisch, wird das Thema ersetzt.
6. Follow-Versprechen (Profil, Bio, Serienabbinder identisch): „haydi-weg zeigt dir die Orte, Fakten und Reise-Irrtümer, die du vor deiner nächsten Buchung kennen solltest, erklärt von Reiseprofis seit 2014.“

**Serienlogik**
7. Drei feste Serien mit Folgennummer (#1–#13), jede Folge kündigt die nächste konkret an; Finale #13 endet mit Community-Frage. Verteilung Mo/Mi/Fr darf laut Auftrag optimiert werden (Begründung im Änderungsprotokoll).
8. „Fakt oder Fake?“-Auflösungen nicht vorhersehbar: Fakt (#1, #5, #7, #11, #12, #13), Fake (#2, #3, #6, #9), „kommt drauf an“ (#4, #8, #10) laut Plan; bei Themenwechsel wird die Verteilung neu geprüft.

**Hook- und Skriptregeln** (Audit + Masterplan)
9. Hook 0–2,5 s, erste Einstellung muss ohne Ton funktionieren; keine Hooks mit „Dieser…“, „sieht aus wie“, „Würdest du…?“; DACH-Anker bis Sekunde 5; Auflösung frühestens bei ~70 % der Länge (Ausnahme: Zwei-Aha-Struktur).
10. Jedes Reel hat eine **prüfbare Behauptung**, eine Auflösung im Video, einen DACH-Anker. Jede Zahl im Voice-over hat eine Quelle oder wird gestrichen; Einschätzungen werden als solche gekennzeichnet.
11. Sprecherlänge 20–35 s Richtwert; ElevenLabs Eleven v3 (bzw. aktuelles Modell), Stimme „Mert_V2“; Zahlen im Sprechtext ausgeschrieben, in Untertiteln als Ziffern; höchstens 3 Audio-Tags je Text; keine `<break>`-Tags; keine Platzhalter.

**Produktionsstandards** (Production Bible, gelten weiter)
12. 9:16, 1080×1920, 30 fps, Timecode HH:MM:SS:FF. Untertitel Manrope SemiBold, ≤ 2 Zeilen, ~32–38 Zeichen, Position 60–70 % Höhe, keine Untertitel während des Hooks (Hook selbst = Manrope ExtraBold, Navy #1C2C5C / Gelb #FBDC15, ein Schlüsselwort gelb). Faktenoverlays ≤ 4 Wörter. Logo klein weiß unten rechts ab Sekunde 3. Serienabbinder letzte 2 s. Musik kommerziell lizenziert, −18 bis −20 dB unter Voice-over, Zielpegel −14 LUFS. ≤ 5 Hashtags Instagram. Keine Preise, keine Links.
13. Markenfarben #1C2C5C (Navy), #FBDC15 (Gelb), #0CA0DE (Hellblau), Weiß. Eigene Grafiken (Karten, Kalender, Illustrationen) in CapCut in diesen Farben; Illustrationen als solche kennzeichnen.

**Timecode-Regel** (Auftrag, verbindlich)
14. Ohne echte ElevenLabs-Audiodatei sind alle Szenenzeiten **vorläufig** (Schätzung 2,45 Wörter/s + 0,35 s je Pause „…“, ausgewiesen als „vorläufig“). Erst nach Audio-Upload berechnet das Reel-Studio die reale Sprechdauer und synchronisiert Szenen und Untertitel. Es werden keine framegenauen Sprechzeiten vorgetäuscht.

**Qualitätssicherung**
15. Gewichtete QS laut Auftrag: Hook/erstes Bild 25 % · Visuelle Stärke 20 % · Storytelling 20 % · Shareability 15 % · DACH-Relevanz 10 % · Fakten/Umsetzbarkeit 10 %. Ziel ≥ 9/10, aber keine aufgeblähten Noten. Schwache Konzepte mindestens zweimal überarbeiten. Fakten, Bildrechte und Materialzuordnung sind Pflicht für die Freigabe.
16. Freigaberegel des Plans bleibt: Nacharbeit erledigt · „Vor Posting prüfen“ am Vortag abgehakt · Material lizenziert und zugeordnet. (Higgsfield-Vorabcheck > 80 bleibt im Plan, wurde hier nicht ausgeführt.)

**Stock und Budget**
17. Envato Elements bevorzugt (Abo), ergänzend Pexels/Pixabay (kommerzielle Nutzung ohne Pflichtnennung, Urheber trotzdem protokollieren); Zusatzbudget **max. 50 €/Monat**; keine Käufe ohne gesonderte Bestätigung.

**Technik / Studio**
18. Bestehendes Reel-Studio (v37) **erweitern, nicht neu bauen**; Funktionen, Daten (51 Specials, IndexedDB-Clips, Untertitel-Stil, Export-Pipeline) erhalten. Kostenlose lokale Lösungen bevorzugen (Browser-Audioanalyse statt API). Keine funktionslosen Buttons.
19. Vor Änderungen Backups (siehe 5). Keine unwiederbringliche Löschung. Keine Veröffentlichungen, Käufe oder produktiven Deployments ohne Bestätigung – v38 wurde deshalb **als neues, privates Artefakt** veröffentlicht; das bestehende v37-Artefakt bleibt unverändert, die Ablösung entscheidet der Auftraggeber (`12_OFFENE_PUNKTE.md`, A2).

---

## 4 Verworfene oder überholte Ideen (nicht unbemerkt vermischen)

| Idee / Quelle | Status | Grund |
|---|---|---|
| 51-Reel-„Hotelgeschichten“-Plan 04.11.–30.01. (Studio v37) | **Specials**, nicht Hauptplan | vom Masterplan 06.11. abgelöst; Antalya-/Hotelvideos als separate Specials gewünscht |
| Alter 39-Reel-Plan (Audit 4,83) | verworfen | 16 Reels mit gesperrtem Material/Ort, Kalenderfehler, keine Serienlogik |
| PLOT-TWIST/Formatkatalog Reel-Strategie Okt | verworfen | durch 3 feste Serien ersetzt |
| 90-Tage-Strategie „Hotelkanal“ mit Verkaufs-CTA | verworfen | CTA-Verbot bis Ende 2026; Entdeckungskanal statt Verkaufskanal |
| Ultra-Luxus-Hotel-Montagen | verworfen | Auftrag: konkrete Hotels nur mit belegbaren Fakten und passendem Material, keine generischen Luxus-Montagen |
| Gestrichene Themen (Tab 7.5): Waitomo, ICEHOTEL, Zao, Abu Simbel, Grüner See, La Geria, Sørvågsvatn, Stille Nacht/Oberndorf, Kawah Ijen, Landebahn Madeira, Polarlichter DE, „Wüste nachts kalt“ | bleiben gestrichen | kein frei lizenzierbarer, zuordenbarer Clip; Madeira-Höhenangabe falsch; Sinai mit AA-Hinweis |
| 21 Ersatzkandidaten des Audits | Vergleichsquelle | fließen in die ≥60-Kandidatenbewertung ein (`01_THEMENBEWERTUNG_60plus.md`) |
| ElevenLabs-«»-Platzhalter (Sprechtexte Okt) | verworfen | Auftrag: keine Platzhalter, nur fertige Texte |

---

## 5 Backups (vor jeder Änderung angelegt)

| Objekt | Backup |
|---|---|
| Reel-Studio v37 (Live-Artefakt) | `haydi-weg-reels/backup/reel-studio-v37-original.html` (3.093.798 Byte, byteidentisch); das bestehende Artefakt selbst bleibt unverändert online – v38 wurde als neues, privates Artefakt veröffentlicht (Link in `14_BEDIENUNGSANLEITUNG.md`) |
| 51 Specials-Datensätze (DATA aus v37) | `haydi-weg-reels/data/reels_specials_v37.json` |
| Quelldokumente (Masterplan, Audit, Historie) | `haydi-weg-reels/backup/quelldokumente/*.txt` (Textfassungen) |
| Repo-Code (`api/index.js` usw.) | unverändert, nicht berührt |

Nutzerdaten im Browser (IndexedDB `haydiweg-reelstudio`, localStorage `hw-reelstudio-v1`) werden vom neuen Studio **gelesen und weiterverwendet**, nie gelöscht; Schema-Erweiterungen sind additiv.

---

## 6 Zustand des Reel-Studios v37 (Funktionsinventar, bleibt erhalten)

- **Daten**: 51 Reels (V-N01–17, V-D01–17, V-J01–17), Felder id/day/month/kind/title/hook/vo/subs/shots/notes/mood/len/cap/pkg/capcut.
- **Timeline**: `TL(v)` aus Shot-Gewichten, festen Dauern und VO-Wortankern; `estVo` Schätzung; `tcCap` HH:MM:SS:FF bei 30 fps; Final-Modus (fertiges CapCut-Video hochladen, Studio legt nur Hook + Untertitel darüber; `detectVoOffset` Kreuzkorrelation; `detectCuts` Frame-Fingerprint).
- **Untertitel**: automatischer Zeilenumbruch (≤38 Zeichen, Schwachwort-Regeln), Ausgleich der Zeilen, DP-Alignment der Zeilen auf Sprachsegmente mit Silbenkernen (lokale Forced-Alignment-Näherung ohne API), SRT/VTT/ElevenLabs-JSON-Import, manuelles Tappen, SRT-Export; Design-System DS (Navy/Gelb, Manrope, Keyword gelb, Zonenwahl nach Bildhelligkeit).
- **Karten je Reel**: CapCut-Karte, Paket-Karte (Brief, Hooks, Schnitttabelle, Post, QS, Checkliste), KI-Produktionsplan (Claude-Sample), Skript, Materialplan, Finalvideo, Final-VO, Hook, Untertitel, Captions (IG/TT/YT), Export & Posting (QC, Cover-PNG, MP4 per WebCodecs, WebM per MediaRecorder, ZIP mit Schnittliste/SRT/Sprechtext).
- **Speicher**: localStorage (Zustand), IndexedDB (Dateien: VO, Musik, Final, Clips, Logo, SFX), optional claude-db.
- **Eigene Projekte**: `openNewProject()`/`registerCustom()` für Custom-Reels.

**Bekannte Schwächen, die v38 behebt** (Details `11_AENDERUNGSPROTOKOLL.md`): `baseName()` schreibt für alle Nicht-Custom-Reels „2026-10-“; Kopfzeile nennt den alten Plan; keine Planumschaltung; kein Hook-Scoring, keine Cover-Varianten, keine 16-Feld-Schnittpläne, keine gewichtete Scorecard, keine zeilenweise Zeitkorrektur der Untertitel, kein JSON-Import eines Hauptplans.

---

## 7 Arbeitsweise dieses Nachtlaufs

1. Masterplan identifiziert, Historie gelesen, Grundlage (dieses Dokument).
2. ≥60 Themenkandidaten bewertet → `01_THEMENBEWERTUNG_60plus.md/.csv`.
3. 39 Reels vollständig ausgearbeitet → `data/reels_hauptplan_v2.json` (Importformat), `03_SPRECHERTEXTE/`, `04_CAPCUT_SCHNITTPLAENE/`, `05_HOOKS_195.csv`, `06_COVER_117.csv`, `07_STOCK_QUELLEN.csv/.md`.
4. Reel-Studio v38 aus v37 erweitert → `studio/reel-studio-v38.html`, veröffentlicht als Artefakt.
5. Automatisierte Tests (Playwright) → `13_TESTBERICHT.md`.
6. Kalender, KPI, Scorecards, Änderungsprotokoll, offene Punkte, Bedienungsanleitung, ZIP.

Alle Zahlen, die Einschätzungen sind (Scores, Hook-Noten, Sekunden ohne Audio, KPI-Szenarien), sind als Einschätzung gekennzeichnet. Erfolgsversprechen werden nicht gemacht.
