# Abstimmung Blogstrategie (Projekt 1) ↔ SEO-Optimierung (Projekt 2)

Stand: 05.11.2026, ca. 02:10 UTC · Erstellt in Projekt 1 (Branch `claude/haydiweg-blogstrategie`, Ordner `haydiweg-blog/`)

## 1. Was ich über Projekt 2 tatsächlich weiß und was nicht

| Information | Quelle | Sicher? |
|---|---|---|
| Projekt 2 läuft als eigene Claude-Code-Cloud-Session „Haydi-weg SEO-Optimierung 2026/2027“ (gestartet 05.11.2026, 01:48 UTC) | Sitzungsliste des Kontos (nur gelesen) | ja |
| Auftrag: Audit, Konkurrenzanalyse, 3 Titelvarianten + finaler Titel und Meta für **alle** Seiten, Landingpage-Strategie, **PHP-Snippet** für Titel/Meta, Test/Rollback, 90-Tage-Prioritäten | Masterprompt im Sitzungsverlauf (nur gelesen) | ja |
| Ausgabeordner `seo-haydiweg/` mit u. a. `HAYDIWEG_SEO_AUDIT.md`, `SEO_TITEL_VORHER_NACHHER.csv`, `SEO_META_DESCRIPTIONS.csv`, `SEO_LANDINGPAGE_STRATEGIE.md`, `HAYDIWEG_FINAL_SEO_SNIPPET.php` | Sitzungsverlauf | ja (Dateinamen), Inhalte **nicht gelesen** |
| Snippet-Stand: 56 Seiten-Overrides + 1 Kategorie, Steuerung über WordPress-Seiten-IDs mit Pfad-Absicherung, Pixelbreiten-Prüfung (Titel ≤ 580 px), Test in einer **lokalen** WordPress-Kopie mit Rank Math | Sitzungsverlauf | ja |
| „Beste Reiseziele 2024“ ist dort als vorbereiteter, **noch deaktivierter** Override mit Platzhalter `{saison}` = 2027 enthalten | Sitzungsverlauf | ja |
| Neuer Cashback-Titel dort: „Urlaub mit Cashback: 30 bis 1.000 € zurück \| haydi-weg“ | Testausgabe im Sitzungsverlauf | ja (Entwurf) |
| Finale Titel, Meta-Descriptions und Hauptkeywords pro Seite | – | **nein**: Die Dateien liegen im Container von Projekt 2 und sind noch nicht gepusht |
| Wie sich der Snippet bei **Beiträgen** (posts) verhält, z. B. Fallback für neue Inhalte | – | **nein**: Das ist die wichtigste offene Abhängigkeit, siehe 3.1 |

Ich habe mit Projekt 2 nicht kommuniziert und dort nichts verändert.

## 2. Rangfolge der Vorgaben (deine Anweisung vom 05.11.2026)

1. **Projekt 2 (SEO) legt die übergeordneten Regeln fest:** Titelformat, Markenplatzierung, Pixelgrenze, Meta-Stil, Keyword-Zuordnung je Seite, Landingpage-Architektur, Schema und die Technik (Snippet und Rank Math).
2. **Projekt 1 (Blog) passt sich an:** Blogtitel, Fokus-Keywords und interne Links werden nach der Zusammenführung gegen die Seiten-Keyword-Map von Projekt 2 geprüft und bei Konflikten angepasst. **Ausnahme:** Wenn eine Seite in Projekt 2 ein Keyword besetzt, das *nur* ein Blogartikel inhaltlich sinnvoll beantworten kann (Informationsfrage statt Buchungsseite), wird das gemeinsam entschieden und in der Übergabe vermerkt.

## 3. Abhängigkeiten und Risiken

### 3.1 Snippet-Fallback ↔ Blog-Metadaten (kritisch)

Projekt 2 soll laut Auftrag „für neue Seiten einen sinnvollen Fallback“ vorsehen. Die 36 Blog-Entwürfe bringen eigene Rank-Math-Metadaten mit (`rank_math_title`, `rank_math_description`, `rank_math_focus_keyword`).
**Anforderung an den Snippet:** Für Beiträge (post_type `post`), bei denen `rank_math_title` bzw. `rank_math_description` gesetzt ist, darf er **nichts überschreiben**. Andernfalls ersetzt der Fallback die im Plan abgestimmten Blogtitel.
→ Vor Aktivierung des Snippets mit einem importierten Entwurf prüfen (Vorschau-Modus).

### 3.2 Doppelte Dateinamen

Beide Projekte erzeugen eine Datei `HAYDIWEG_SEO_AUDIT.md`, aber in getrennten Ordnern (`haydiweg-blog/` und `seo-haydiweg/`).
**Regel:** Die Datei in `seo-haydiweg/` ist das Master-Audit für Seiten-SEO. Die Blog-Version behandelt den Blickwinkel Blog und Inhalte und wird beim Zusammenführen als Anhang eingeordnet.

### 3.3 Keyword-Abgrenzung Blog ↔ Seiten (vorläufig, gegen Live-Stand geprüft)

| Blogartikel | Mögliche Konkurrenz | Vorläufige Abgrenzung |
|---|---|---|
| 06 Türkei im Winter, 28 Wassertemperatur Türkei | /urlaubsziele/tuerkei-urlaub-buchen/beste-reisezeit-tuerkei/ | Die Seite behält „beste reisezeit türkei“. Die Blogartikel zielen auf „türkei im januar/februar“ und „wassertemperatur türkei“ |
| 13 Osterferien 2027, 29 Pfingstferien 2027 | /ostern-urlaub/, /pfingsten-urlaub/ | Die Seiten behalten „urlaub ostern/pfingsten“. Die Artikel zielen auf die *Ferientermine* |
| 14 Familienurlaub Türkei, 23 Baby Türkei | /familienurlaub/, Aquapark-Beitrag, /urlaubsziele/tuerkei-urlaub-buchen/ | /familienurlaub/ = allgemein. Artikel 14 = Hotelwahl nach Kindesalter, Türkei |
| 09 All Inclusive oder Halbpension | /sommerurlaub-all-inclusive/ | Vergleichsfrage vs. Sommer-Landingpage |
| 17 Pauschalreise oder selbst buchen | /pauschalreisen/ | Informationsfrage vs. Buchungsseite „pauschalreise buchen“ |
| 08 Side oder Belek, 35 Kemer | /tuerkei-urlaub-side/ | Die Seite = „urlaub side“. Artikel 08 = Vergleich. Artikel 35 hat keine Seitenkonkurrenz |
| 01 Kanaren im Winter | /winterurlaub/, /reise-blog/reiseziele-im-winter/ | Inselvergleich, nicht „winterurlaub“ |

Diese Tabelle ist mit Projekt 2 abzugleichen, sobald dessen Keyword-Zuordnung vorliegt (Skript siehe 4).

### 3.4 Sprachregelungen, die beide Projekte gleich verwenden müssen

| Thema | Blog-Entwürfe aktuell | Projekt 2 (Entwurf) | Zu entscheiden |
|---|---|---|---|
| Cashback-Formulierung | „bis zu 1.000 € Cashback für berechtigte Online-Buchungen gemäß Teilnahmebedingungen“ | „30 bis 1.000 € zurück“ | Eine Formulierung festlegen, die den Teilnahmebedingungen entspricht. Danach Blog-Entwürfe per Suchen/Ersetzen angleichen |
| Marke im Title | „… \| haydi-weg“ am Ende, entfällt bei Platzmangel | (vermutlich gleich, Titel enden auf „\| haydi-weg“) | bestätigen |
| Jahreszahlen | in Saisonartikeln im Titel („2027“), Slug-Empfehlung jahresneutral | Platzhalter `{saison}` | gemeinsame Regel: Jahreszahl im Titel ja, im Slug nein |
| Titellänge | ≤ 60 Zeichen **und** ≤ 580 px (Skript prüft beides) | Pixelbreite | übernommen |

### 3.5 Struktur- und Architekturthemen (Projekt 2 entscheidet)

- Neue Blog-Kategorien (Ägypten, Spanien, Griechenland, Dubai, Fernreisen, Reiseplanung): Kategoriearchive werden indexierbar. Projekt 2 hat bereits einen Override für 1 Kategorie (vermutlich /category/tuerkei/). Titel und Meta der neuen Kategorien sollten dort mit aufgenommen werden.
- Fehlende Zielgebietsseiten (z. B. Thailand) gehören in `SEO_LANDINGPAGE_STRATEGIE.md` von Projekt 2. Die Blogartikel 15 und 22 verlinken bis dahin /urlaubsziele/.
- Bei Autor-Schema, Hotel-Schema und dünnen Hotelseiten überschneiden sich beide Audits. Die Umsetzung liegt bei Projekt 2.

## 4. Werkzeug für die Zusammenführung

`_arbeitsdaten/seo_abgleich.py` prüft alle Blog-Entwürfe auf:
- doppelte oder sehr ähnliche Titel (Blog ↔ Seiten, Blog ↔ Blog),
- doppelte Meta-Descriptions,
- Fokus-Keywords, die vollständig im Titel oder in der H1 einer Seite stecken,
- Titel-Pixelbreite über 580 px.

```bash
# heute: gegen den Live-Stand
python3 haydiweg-blog/_arbeitsdaten/seo_abgleich.py
# nach Zusammenführung: gegen die finalen Titel aus Projekt 2
python3 haydiweg-blog/_arbeitsdaten/seo_abgleich.py seo-haydiweg/SEO_TITEL_VORHER_NACHHER.csv seo-haydiweg/SEO_META_DESCRIPTIONS.csv
```

## 5. Was in Projekt 1 bewusst NICHT passiert

- Es werden keine Titel oder Meta-Descriptions bestehender **Seiten** vorgeschlagen oder geändert. Das ist Aufgabe von Projekt 2. Die Seiten-Befunde im Blog-Audit sind nur Hinweise.
- Es gibt keinen eigenen PHP-Snippet und keine Rank-Math-Einstellungen.
- Nichts wird veröffentlicht oder aktiviert. Die Blog-Importdatei setzt alle Artikel auf **Entwurf**.
