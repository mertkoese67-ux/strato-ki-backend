# Übergabe: Blogstrategie (Projekt 1) → Zusammenführung mit SEO-Optimierung (Projekt 2)

Stand: 05.11.2026 · Branch `claude/haydiweg-blogstrategie` · Ordner `haydiweg-blog/` · **Nichts ist veröffentlicht oder aktiviert.**

## Was Projekt 1 liefert

| Datei | Zweck bei der Zusammenführung |
|---|---|
| `BLOG_SEO_KEYWORD_MAP.csv` | **Kernstück der Übergabe:** pro Blogartikel URL, SEO-Title (Zeichen und px), Meta, Fokus- und Nebenkeywords, Pillar-Seite, Status. Diese Datei mit der Keyword-Zuordnung der Seiten aus Projekt 2 zusammenführen |
| `REDAKTIONSPLAN_3_MONATE.csv` / `REDAKTIONSKALENDER.md` | 36 Termine vom 09.11.2026 bis 29.01.2027, davon 3 Dubai-Artikel zurückgestellt und durch R1–R3 ersetzt |
| `BLOG_ARTIKEL/*.md` | 39 Entwürfe mit Frontmatter |
| `WORDPRESS_IMPORT/*.xml` | WXR-Import, alle Artikel als **Entwurf**, mit Rank-Math-Metadaten |
| `SEO_ABSTIMMUNG_MIT_PROJEKT_2.md` | Rangfolge der Vorgaben, Abhängigkeiten, vorläufige Keyword-Abgrenzung |
| `_arbeitsdaten/seo_abgleich.py` | Kollisionsprüfung Blog ↔ Seiten (Titel, Meta, Keywords, px) |
| `HAYDIWEG_SEO_AUDIT.md` | Audit aus Blog-Sicht. **Für Seiten-SEO gilt das Audit aus Projekt 2** |

## Zusammenführung in 5 Schritten

1. Die Ergebnisse von Projekt 2 (`seo-haydiweg/`) auf einen Branch pushen. Beide Ordner liegen nebeneinander, Dateien werden nicht überschrieben.
2. Den Abgleich laufen lassen:
   `python3 haydiweg-blog/_arbeitsdaten/seo_abgleich.py seo-haydiweg/SEO_TITEL_VORHER_NACHHER.csv seo-haydiweg/SEO_META_DESCRIPTIONS.csv`
3. Befunde auflösen. **Projekt 2 hat Vorrang.** Bei Konflikten wird der Blogtitel bzw. das Fokus-Keyword angepasst. Danach `build_keyword_map.py` und `build_wxr.py` neu ausführen.
4. Die Regeln aus `SEO_LANDINGPAGE_STRATEGIE.md` (Projekt 2) gegen die Pillar-Spalte der Keyword-Map prüfen. Neue Landingpages (z. B. Thailand) als Linkziele in die Artikel aufnehmen.
5. Den Snippet aus Projekt 2 nur auf Staging und nur mit importierten Blog-Entwürfen testen (siehe offene Punkte 1).

## Offene Abhängigkeiten (müssen vor Aktivierung geklärt sein)

1. **Snippet-Fallback:** Für Beiträge mit gesetztem `rank_math_title` bzw. `rank_math_description` darf der PHP-Snippet aus Projekt 2 nichts überschreiben.
2. **Cashback-Formulierung vereinheitlichen:** Blog: „bis zu 1.000 € … gemäß Teilnahmebedingungen“, Projekt 2 (Entwurf): „30 bis 1.000 € zurück“.
3. **WhatsApp-Nummer:** Die Website verwendet 0157 92326450 (Kontaktseite, Header, Footer) **und** 0155 63462222 (CTAs auf ca. 60 Inhaltsseiten). Die Blog-Entwürfe nutzen 0157 92326450. Bitte festlegen, welche gilt.
4. **Neue Kategorien** (Ägypten, Spanien, Griechenland, Fernreisen, Reiseplanung, Zypern, Portugal; Dubai erst bei Reaktivierung): Titel und Meta der Kategoriearchive gehören in die Seiten-SEO von Projekt 2.
5. **Autor „admin“** im Schema: Beide Audits empfehlen ein echtes Autorenprofil. Die Umsetzung wird einmal zentral entschieden.
6. **„Beste Reiseziele 2024“:** Projekt 2 hat dafür einen vorbereiteten Override (`{saison}`). Der Inhalt muss vorher auf 2027 aktualisiert werden. Im Blog-Plan ist das nicht enthalten, damit es nicht doppelt erledigt wird.
7. **Ägypten-Zielgebietsseite:** Behauptet sie eigene Hotelbesuche? Bitte prüfen.
8. **Widersprüche auf Hotelseiten** (Zimmerzahlen, Verpflegung, Entfernungen): Details in SEO_QUALITAETSPRUEFUNG.md, Abschnitt 4.

## Fehlende Informationen aus Projekt 2 (für Projekt 1 nicht zugänglich)

- Finale Seitentitel, Meta-Descriptions und Hauptkeyword pro Seite
- Inhalt der Landingpage-Strategie (fehlende Zielgebietsseiten, Linkregeln Blog → Angebot)
- Verhalten des Snippets bei Beiträgen und Kategorien

Sobald diese Informationen vorliegen, sind Schritt 2 und 3 oben in etwa einer Stunde erledigt.
