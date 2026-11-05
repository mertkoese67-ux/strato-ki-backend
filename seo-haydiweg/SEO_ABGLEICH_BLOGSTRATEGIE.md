# Abgleich SEO-Projekt ↔ Blogstrategie (Projekt 1)

**Stand:** 05.11.2026 · erstellt im SEO-Projekt (Branch `claude/haydiweg-seo-audit`)

## 1. Welche Informationen tatsächlich vorlagen

| Information | Quelle | Status |
|---|---|---|
| Blogstrategie, Redaktionsplan (36 Artikel, 09.11.2026–29.01.2027), Abstimmungsdatei, Abgleich-Skript, 6 Artikelentwürfe (#01, #02, #03, #09, #13, #16) | Git-Branch `origin/claude/haydiweg-blogstrategie`, Stand Commit `b8ea541` (05.11.2026, 02:07 UTC), **nur gelesen** | ✔ gelesen |
| Die übrigen 30 Artikelentwürfe | – | **fehlen** (laut Branch „Zwischenstand“). Geprüft sind nur die geplanten H1-Titel und Keywords |
| Direkter Austausch mit dem Blog-Chat | – | **kein Zugriff**, keine Kommunikation, im Blog-Branch nichts verändert |
| Branch `claude/haydiweg-ibe-analysis-n8trsp` (IBE-Analyse, Deeplink-Generator) | Git | nur zur Kenntnis; für die SEO nicht relevant |
| Search Console, Analytics, Suchvolumen | – | nicht verfügbar (gilt für beide Projekte) |

## 2. Antworten auf die offenen Fragen des Blog-Projekts

Bezug: `haydiweg-blog/SEO_ABSTIMMUNG_MIT_PROJEKT_2.md`

| Frage (Blog) | Antwort (SEO) |
|---|---|
| 3.1 Überschreibt der Snippet die Rank-Math-Metadaten von Beiträgen? | **Nein.** Er greift nur bei den konfigurierten IDs (56 Seiten, 1 Kategorie). Ein Test mit einem Beitrag unter `/aegypten/…` mit eigenem `rank_math_title` und eigener Description im Live-Modus zeigte die Blogwerte unverändert. Ohne eigenen Titel wird nur das alte Suffix „☀ Urlaub leicht gemacht“ ersetzt. |
| 3.2 Doppelter Dateiname `HAYDIWEG_SEO_AUDIT.md` | Einverstanden: `seo-haydiweg/HAYDIWEG_SEO_AUDIT.md` ist das Master-Audit, die Blog-Version wird als Anhang „Blog-Sicht“ eingeordnet. Die Befunde decken sich (dünne Hotelseiten, „Beste Reiseziele 2024“, Autor „admin“, FAQ ohne Rich Results). Es gibt keine Widersprüche. |
| 3.3 Keyword-Abgrenzung | Die vorläufige Tabelle des Blog-Projekts wird **bestätigt**. Ergänzungen und Abweichungen stehen in Abschnitt 3 und vollständig in `SEO_KEYWORD_ZUORDNUNG.csv`. |
| 3.4 Cashback-Formulierung | Festgelegt in `SEO_VORGABEN_FUER_BLOG.md` §6. Die Blog-Formulierung „bis zu 1.000 € … gemäß Teilnahmebedingungen“ ist im Fließtext zulässig, wenn „ab 700 € Reisepreis“ ergänzt wird. In CTA-Kästen und Descriptions gilt „30 bis 1.000 € Cashback ab 700 € Reisepreis“. |
| 3.4 Marke, Jahreszahl, Titellänge | Bestätigt: „ \| haydi-weg“ am Ende, Jahreszahl im Titel ja und im Slug nein, ≤ 580 px. |
| 3.5 Neue Kategorien | Erlaubt; Archive erst ab 5 Beiträgen und mit eigenem Text indexieren, Titelmuster „{Thema}-Ratgeber …“. Kategorie-IDs sind erst nach dem Anlegen bekannt, deshalb werden Overrides für den Snippet bei Bedarf nachgetragen. |
| 3.5 Thailand-Seite | Keine Zielgebietsseite Thailand oder Bali vorgesehen (keine eigene Kompetenz/Hotels). #15 und #22 verlinken auf `/urlaubsziele/`. |

## 3. Befunde aus dem Abgleich aller 36 geplanten Artikel

**Automatisch:** Das Skript des Blog-Projekts (`seo_abgleich.py`), angewendet auf die **finalen** Titel dieses Projekts, findet **0 Konflikte** zwischen Blog und Seiten. Es meldet nur eine Ähnlichkeit von 0,94 zwischen den Blogtiteln #13 und #16. **Manuell:** Abgleich der Keywords und H1 aller 36 Planartikel mit der Keyword-Zuordnung.

| Ergebnis | Anzahl | Artikel |
|---|---|---|
| OK | 28 | – |
| OK mit Auflage | 1 | #12 Türkische Riviera Regionen: Die Türkei-Seite verlinkt prominent darauf, Titel ohne „Riviera“ |
| Konflikt vom SEO-Projekt gelöst | 1 | #25 „Türkei Urlaub Kosten“: Der Türkei-Seitentitel wurde von „… Regionen, Hotels **& Preise**“ auf „… **All Inclusive**, Regionen & Hotels“ geändert, Snippet und CSV sind aktualisiert und regressionsgetestet |
| Anpassung im Blog nötig | 5 | #11, #13, #16, #24, #29: **Slugs enthalten „2027“**. Das widerspricht der eigenen Blog-Regel („URL ohne Jahreszahl“) und erzwingt jedes Jahr neue URLs. Außerdem #13/#16: Untertitel stärker unterscheiden |
| **Entscheidung des Inhabers nötig** | 1 | **#35 „Urlaub in Kemer“** ↔ geplante Regionsseite `/urlaubsziele/tuerkei-urlaub-buchen/kemer/` (gleiches Keyword „kemer urlaub“) |

### Strategische Änderungen im SEO-Projekt infolge des Abgleichs
1. **Landingpage `/fruehbucher/` gestrichen.** Den Begriff „Frühbucher {saison}“ besetzt allein Blogartikel #11, mit Slug `fruehbucher`.
2. **Beitrag „Adults-Only-Hotels Türkei“** an das Blog-Projekt übergeben (#31).
3. Türkei-Seitentitel angepasst (siehe #25).
4. Neue Dateien: `SEO_KEYWORD_ZUORDNUNG.csv`, `SEO_VORGABEN_FUER_BLOG.md`, diese Datei, `UEBERGABE_SEO_BLOG.md`.

### Entscheidungsvorlage #35 Kemer
| Option | Wirkung | Empfehlung |
|---|---|---|
| **A** Inhalt von #35 wird die Regionsseite Kemer (WordPress-Seite unter dem Türkei-Pfad, Titel/Meta vom SEO-Projekt). Der Blog-Slot am 27.01.2027 wird neu belegt. | eine starke URL für „Kemer Urlaub“, konsistente Regionsstruktur (Alanya, Belek, Antalya, Side, Kemer) | **empfohlen** |
| B #35 bleibt Blogartikel, aber mit Fokus „Kemer oder Alanya“ (Vergleich). Die Regionsseite kommt später. | keine Konkurrenz, Kemer-Seite verzögert | möglich |
| C #35 bleibt wie geplant, und die Regionsseite Kemer entfällt | widerspricht der Regionsstruktur, Kemer-Hotelvideos ohne passende Landingpage | nicht empfohlen |

## 4. Fehlende Abhängigkeiten (offen)

| # | Abhängigkeit | Wer klärt | Auswirkung bis dahin |
|---|---|---|---|
| A1 | 30 Artikelentwürfe fehlen noch | Blog | Titel und Descriptions sind nicht final prüfbar; `seo_abgleich.py` nach Fertigstellung erneut laufen lassen |
| A2 | Gültige WhatsApp-Nummer (0157 92326450 oder 0155 63462222) | Inhaber | Beide Projekte verwenden vorerst 0157 92326450 (Footer) |
| A3 | Entscheidung #35 Kemer | Inhaber | Regionsseite Kemer nicht beginnen |
| A4 | Kategorie-IDs der neuen Blog-Kategorien | nach Anlage in WordPress | ggf. Term-Overrides im Snippet ergänzen, bis dahin greift Rank Math |
| A5 | Autorenprofil (Name, Foto, Bio) | Inhaber | beide Projekte empfehlen es, Umsetzung in Rank Math/WordPress |
| A6 | Liegen die Seiten-IDs live noch so vor? (Snippet prüft ID **und** Pfad) | vor Aktivierung | Einträge mit Abweichung greifen nicht (sicherer Ausfall) |
| A7 | Reihenfolge der Freigaben (Snippet vor oder nach den ersten Blogartikeln) | Inhaber | technisch unabhängig (siehe §2, 3.1) |
| A8 | `/reise-blog/` ist eine statische Seite, neue Beiträge erscheinen dort nicht automatisch (Befund Blog-Projekt) | Blog/Inhaber | Titel und Description der Seite bleiben unverändert; ein Beitragslisten-Widget beeinflusst die SEO-Vorgaben nicht |
