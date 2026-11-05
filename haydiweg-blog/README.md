# haydi-weg Blogstrategie 2026/2027 – Projektübersicht

Stand: 05.11.2026 · **Analysierend und vorbereitend. Nichts ist veröffentlicht, nichts auf der Website verändert.**

## Dateien

| Datei | Inhalt |
|---|---|
| CLAUDE_BLOG_ANFORDERUNGEN.md | Anforderungen. Hinweis: kein Zugriff auf claude.ai-Chats, ein Export wird benötigt |
| HAYDIWEG_SEO_AUDIT.md | Istbericht aus Blog-Sicht (89 URLs, Mediathek, Mobil-Messung) |
| BLOG_STRATEGIE_2026_2027.md | Frequenz, Cluster, Top 10, Conversion, Aktualisierungsprozess |
| REDAKTIONSPLAN_3_MONATE.csv | 36 Termine + 3 Ersatztermine mit allen 13 Planfeldern (Semikolon, UTF-8) |
| REDAKTIONSKALENDER.md | lesbarer Kalender |
| BLOG_ARTIKEL/ | 39 vollständige Entwürfe (Markdown + Frontmatter) |
| WORDPRESS_IMPORT/ + WORDPRESS_IMPORT_STATUS.md | WXR-Import (nur Entwürfe), HTML-Versionen, Anleitung |
| SEO_QUALITAETSPRUEFUNG.md | Kriterien, Ergebnisse, offene Prüfpunkte, Aktualisierungsprozess |
| BLOG_REPORTING_KONZEPT.md | KPIs, GA4-Events, Ziele, Monatsmethode |
| SEO_ABSTIMMUNG_MIT_PROJEKT_2.md / UEBERGABE_BLOG_AN_SEO.md / BLOG_SEO_KEYWORD_MAP.csv | Abstimmung und Übergabe an das SEO-Projekt |
| _arbeitsdaten/ | Styleguide, Rohdaten (URL-Liste, Mediathek, Autocomplete, Live-SEO-Stand), Skripte |

## Skripte (wiederaufnehmbar, überschreiben keine Artikel)

```bash
cd haydiweg-blog/_arbeitsdaten
python3 build_plan.py          # CSV + Kalender aus einer Datenquelle
python3 qa_check.py --links    # Qualitätsprüfung aller Entwürfe
python3 seo_abgleich.py [P2-Titel.csv] [P2-Meta.csv]   # Kollisionen mit Seiten-SEO
python3 build_keyword_map.py   # Übergabe-CSV
python3 build_wxr.py           # WordPress-Import (nur Entwürfe)
```

## Ausgeführt ✅ / offen ⏳

| Phase | Status |
|---|---|
| 1 Chats analysieren | ⏳ Kein Zugriff auf claude.ai-Chats. Anforderungen stammen aus dem Masterprompt und der Website. **Chat-Export nachreichen** |
| 2 Website-Analyse | ✅ Crawl, Mediathek, Mobil-Labormessung. ⏳ GSC und GA4 (kein Zugang) |
| 3 Frequenz | ✅ Empfehlung: 3 pro Woche bis Januar, danach 2 neue + 1 Update |
| 4 Themenplanung | ✅ auf Basis von Autocomplete und Suchintention. ⏳ Suchvolumina (kein Tool) |
| 5 Redaktionsplan | ✅ |
| 6 Artikel | ✅ 39 Entwürfe. ⏳ 125 `[PRÜFEN]`-Marker redaktionell auflösen |
| 7 Bilder | ✅ Vorschläge und ALT-Texte. ⏳ Rechteprüfung, 84 Bildplätze mit Status MEDIENPRÜFUNG |
| 8 WordPress | ✅ Importdatei. ⏳ Import, Elementor- und Mobilprüfung (kein autorisierter Zugang, lokaler Testimport von der Sicherheitsprüfung blockiert) |
| 9 Qualitätskontrolle | ✅ automatisch 39/39 bestanden. ⏳ manuelle Endkontrolle je Artikel |
| 10 Reporting | ✅ Konzept. ⏳ GA4-Events und GSC-Zugang einrichten |
| SEO-Abstimmung | ✅ Regeln, Werkzeug und Übergabe. ⏳ Ergebnisse von Projekt 2 nicht zugänglich |
