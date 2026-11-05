# Übergabe: SEO-Projekt → Zusammenführung mit der Blogstrategie

**Stand:** 05.11.2026 · **SEO-Branch:** `claude/haydiweg-seo-audit`, Ordner `seo-haydiweg/` · **Blog-Branch:** `claude/haydiweg-blogstrategie`, Ordner `haydiweg-blog/`

## Status
- Nur Analyse und Vorbereitung. **Nichts ist live:** Der Snippet steht auf `'preview'`, nichts ist veröffentlicht, keine produktive Einstellung wurde geändert.
- Beide Ordner überschneiden sich nicht. Die Branches können ohne Dateikonflikte in einen gemeinsamen Branch zusammengeführt werden.

## Rangfolge
SEO-Vorgaben (`SEO_VORGABEN_FUER_BLOG.md` + `SEO_KEYWORD_ZUORDNUNG.csv`) stehen über der Blogstrategie.

## Was das Blog-Projekt übernehmen muss
1. Slugs jahresneutral: #11 `fruehbucher`, #13 `osterferien`, #16 `sommerferien`, #24 `brueckentage`, #29 `pfingstferien`
2. Untertitel von #13 und #16 deutlicher unterscheiden
3. Cashback-Sprachregelung (§6 der Vorgaben) in allen Entwürfen anwenden
4. Pflicht-Link je Artikel laut Spalte „Pflicht-Link auf“ der Keyword-Zuordnung
5. Jeder Artikel mit eigenem Rank-Math-Titel und eigener Description (≤ 580 px, keine Emojis)
6. Neue Kategoriearchive bis 5 Beiträge auf noindex, Titel „{Thema}-Ratgeber …“
7. Nach Fertigstellung der 30 fehlenden Entwürfe: `python3 haydiweg-blog/_arbeitsdaten/seo_abgleich.py seo-haydiweg/SEO_TITEL_VORHER_NACHHER.csv seo-haydiweg/SEO_META_DESCRIPTIONS.csv` muss 0 Konflikte mit Seiten melden

## Was das SEO-Projekt bereits angepasst hat
- Türkei-Seitentitel: „Türkei Urlaub {saison}: All Inclusive, Regionen & Hotels | haydi-weg“ (wegen Blog #25)
- Landingpage `/fruehbucher/` gestrichen (Blog #11), Adults-only-Beitrag an Blog #31 übergeben
- Snippet und CSVs neu erzeugt, PHP-Syntax geprüft, Regressionstest bestanden (nur die Türkei-Zeile hat sich geändert)

## Entscheidungen des Inhabers (vor der Zusammenführung)
1. **#35 Kemer:** Option A (wird Regionsseite, empfohlen), B (Vergleich „Kemer oder Alanya“) oder C
2. **Gültige WhatsApp-Nummer**
3. **Freigabe-Reihenfolge:** (a) Snippet in Vorschau testen → (b) Snippet live → (c) erste Blogartikel. Technisch ist jede Reihenfolge möglich.
4. Autorenprofil für Blog-Schema (Name, Foto, Kurzbio)

## Zusammenführung (Vorschlag)
```bash
git checkout -b claude/haydiweg-seo-blog-gesamt origin/main
git merge --no-ff origin/claude/haydiweg-seo-audit
git merge --no-ff origin/claude/haydiweg-blogstrategie
python3 haydiweg-blog/_arbeitsdaten/seo_abgleich.py seo-haydiweg/SEO_TITEL_VORHER_NACHHER.csv seo-haydiweg/SEO_META_DESCRIPTIONS.csv
```
Danach: Konflikte gemäß `SEO_KEYWORD_ZUORDNUNG.csv` auflösen. Nach Veröffentlichung der Blogartikel ergänzt das SEO-Projekt die Rückverlinkungen von den Zielgebietsseiten.

## Dateiindex SEO-Projekt
| Datei | Inhalt |
|---|---|
| `HAYDIWEG_SEO_AUDIT.md` | Master-Audit Seiten-SEO |
| `HAYDIWEG_SEO_INVENTAR.csv` | 89 URLs mit allen Inventarfeldern |
| `KONKURRENZANALYSE_REISEPORTALE.md` | Wettbewerber-Titel und -Muster |
| `SEO_TITEL_VORHER_NACHHER.csv` / `SEO_META_DESCRIPTIONS.csv` | Titel (3 Varianten + final) und Descriptions |
| `SEO_LANDINGPAGE_STRATEGIE.md` | Architektur, Regionsseiten, Schema, lokale SEO |
| `HAYDIWEG_FINAL_SEO_SNIPPET.php` | Rank-Math-Filter-Snippet (Modus preview) |
| `SEO_TEST_UND_ROLLBACK.md` | Installation, Testplan, Testprotokoll, Rollback |
| `SEO_PRIORITAETEN_90_TAGE.md` | Ablaufplan und Messkonzept |
| `SEO_KEYWORD_ZUORDNUNG.csv` | **gemeinsame** Keyword-Zuordnung Seiten + Blog |
| `SEO_VORGABEN_FUER_BLOG.md` | **verbindliche** Regeln für das Blog |
| `SEO_ABGLEICH_BLOGSTRATEGIE.md` | Abgleichsbefunde, Antworten, offene Abhängigkeiten |
