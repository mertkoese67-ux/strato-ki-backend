# haydi-weg – SEO-Audit 2026/2027

**Stand:** 05.11.2026 · **Untersucht:** https://haydiweg.de (alle 89 URLs aus der XML-Sitemap plus Stichproben außerhalb der Sitemap)
**Vollständiges Seiteninventar (alle 10 geforderten Felder je URL):** `HAYDIWEG_SEO_INVENTAR.csv`

---

## 1. Methode und Grenzen

| Schritt | Vorgehen |
|---|---|
| Crawl | `sitemap_index.xml` → `page-sitemap.xml`, `post-sitemap.xml`, `category-sitemap.xml` = **89 URLs**. Jede URL einzeln abgerufen (ohne Weiterleitungen zu folgen), `<head>` und Body ausgewertet. |
| Ausgewertet | Statuscode, `<title>` (Anzahl + Inhalt), Meta-Description (Anzahl + Inhalt), robots, Canonical, H1/H2, WordPress-ID (body-Klasse / REST-Link), JSON-LD-Typen, Wortzahl, eingebundene IBE-Links |
| Zusatzprüfungen | `/robots.txt`, www/http-Weiterleitungen, Pfade außerhalb der Sitemap (`/ueber-uns/`, `/terminbuchung/`, `/hotel/`, `/tuerkei/`, `/author/admin/`, `/?s=`, `/reise-blog/page/2/`, `/buchen/?ibe=…`) |
| Plugin-Quellcode | Rank Math 1.0.281 (Free-Kern, auf dem PRO aufsetzt) heruntergeladen und die Filter für Titel/Description im Quellcode verifiziert |
| Test | Snippet in einer echten WordPress-7.1-Installation mit Rank Math getestet (siehe `SEO_TEST_UND_ROLLBACK.md`) |

**Nicht verfügbar und daher nicht verwendet:** Google Search Console, Suchvolumen, CTR, Rankings, Analytics, Backend-Zugang. Alle Aussagen zu „Potenzial“ sind qualitative Einschätzungen, keine Messwerte. Es wurden keine Zahlen erfunden.

---

## 2. Technische Architektur (festgestellt)

| Komponente | Befund | Quelle |
|---|---|---|
| CMS | WordPress, Theme **Twenty Nineteen** + **Elementor 4.3.6** (Seiten-Template `elementor_header_footer`) | body-Klassen, `meta generator` |
| SEO-Plugin | **Rank Math PRO** – erzeugt `<title>`, Description, robots, Canonical, OG/Twitter, JSON-LD, Sitemaps | HTML-Kommentar „Suchmaschinen-Optimierung durch Rank Math PRO“ |
| Weitere SEO-Quellen | **Keine.** Jede der 89 Seiten hat genau 1 `<title>`, maximal 1 Description, 1 OG-Titel. Kein Yoast/AIOSEO/SEOPress, kein Theme-Titel, kein bestehendes Titel-Snippet erkennbar. | Zählung im HTML |
| Cache | **WP Rocket 3.24** (Minify, CDN, Preload) | `meta generator` |
| Server | Apache 2.4.69, **PHP 8.4.27** (STRATO) | HTTP-Header |
| Buchungs-IBE | Schmetterling (`pauschalreise.schmetterling.de` auf `/buchen/`, `schmetterling-urania.com` in Hotel-Links) – wird per JavaScript geladen, Inhalte sind für Google nicht als eigener Text sichtbar | HTML |
| Cookie-Banner | CookieYes | HTML |
| Termine | extern über koalendar.com (keine eigene Terminseite, `/terminbuchung/` = 404) | Links |
| robots.txt | sauber (`/wp-admin/` gesperrt, Sitemap angegeben) | `/robots.txt` |
| Weiterleitungen | `www` → non-www (301), `http` → `https` (301), `wp-sitemap.xml`/`sitemap.xml` → `sitemap_index.xml` (301) ✔ | |
| Indexierung | Alle 89 Sitemap-URLs: `index, follow`, selbstreferenzierender Canonical ✔. Suche, Autorenarchiv, 404, `uncategorized`: `noindex` ✔ | robots-Meta |

**Wichtigste Konsequenz für die Umsetzung:** Rank Math ist die einzige Quelle für Titel und Description. Jede Änderung muss über Rank Math laufen (nativ im Editor oder über die offiziellen Rank-Math-Filter). Ein zusätzlicher eigener `<title>`-Hook (z. B. `document_title_parts`) oder Ausgabepuffer wäre falsch und würde Konflikte erzeugen.

---

## 3. Gesamtbewertung der aktuellen SEO-Titel

### Note: **6 von 10**

**Was bereits gut ist (ehrlich festgehalten):**
- Die meisten Titel wurden offensichtlich schon einmal überarbeitet: Keyword vorne, Marke hinten, sauber unter ca. 580 px, keine Duplikate.
- Die 15 Hotelseiten mit eigenem Video haben ein starkes, eigenständiges Muster („*Hotel Ort: Hotelvideo & Erfahrungen*“), das kein großes Portal so bietet.
- Descriptions sind natürlich formuliert, keine Keyword-Listen, Cashback meist mit Bedingungen.

**Warum trotzdem nur 6:**
- Die Titel sind korrekt, aber **austauschbar**: „*Spanien Urlaub buchen – Mallorca & Kanaren*“ könnte von jedem Portal stammen. Die echten Stärken (Türkei-Spezialist seit 2014, Hotels selbst gefilmt, 5,0 bei Google, persönliche Beratung in Minden) kommen in den Titeln fast nie vor.
- Kein Saisonbezug (2027), obwohl die Konkurrenz ihn bei allen Angebotsseiten nutzt und gerade jetzt (November) die Sommer-2027-Planung beginnt.
- Startseite ohne Ort und ohne Spezialisierung.
- Einige Ausreißer ziehen die Gesamtqualität deutlich herunter (Tippfehler, Slogan-Suffix, veraltete Jahreszahl 2024, Emojis/Häkchen).

---

## 4. Die zehn wichtigsten Schwachstellen

| # | Schwachstelle | Betroffen | Wirkung |
|---|---|---|---|
| 1 | **Fehlende Differenzierung in Titeln**: USP (Türkei-Spezialist, selbst gefilmte Hotels, 5,0 Google, Beratung vor Ort) taucht kaum auf | Startseite, Türkei, Minden, Hotel-Hub, Zielgebiete | Kein Grund, haydi-weg statt TUI/CHECK24 anzuklicken |
| 2 | **Drei dünne Hotelseiten** (Acapulco Lloret, htop Amatista, L’Azure): Tippfehler „Acaplco“, Slogan-Suffix „☀ Urlaub leicht gemacht“, identische Description „Die besten Angebote mit top Preis-Leistungs-Verhältnis.“, kein Video, fast nur Vorlagentext, Angebotslinks mit **abgelaufenen Reisedaten (Juni/Juli 2026)** | 5644, 5633, 5687 | Thin Content, schlechter Eindruck, Qualitätssignal für die ganze Domain |
| 3 | **Veralteter Artikel „Beste Reiseziele 2024“** (Titel, H1, FAQ, URL) mit „✅ ✔️“ und Keyword-Wiederholung in der Description | 2811 | Veraltet im November 2026, Klickverlust, Abwertung als nicht aktuell |
| 4 | **Schema-Fehler aus Rank Math**: `Article` auf Startseite und Landingpages, Autor „admin“, Telefon falsch formatiert (`+49-0571-73075925`), Organisationsbeschreibung in Sie-Form, keyword-lastig und in Anführungszeichen, `sameAs` nur YouTube, WebSite-Name „haydi-weg ☀ Urlaub leicht gemacht“ | alle Seiten | Falscher Seitentyp, schwaches E-E-A-T, unschöner Website-Name in Google |
| 5 | **NAP-Inkonsistenz**: WhatsApp 0155 63462222 (Minden-Seite) vs. 0157 92326450 (Footer, 126×) vs. 0571-73075925 (nur im Schema) | Lokale SEO | Widersprüchliche Kontaktdaten schwächen das lokale Ranking und verwirren Kunden |
| 6 | **Kein Saisonbezug** (2027) auf Angebots- und Zielgebietsseiten | Türkei, Ägypten, Griechenland, Spanien, Sommer, Ostern … | Niedrigere Klickrate als Wettbewerber, die „2026/2027“ zeigen |
| 7 | **Fehlende Regionsseiten Türkei** (Antalya/Lara, Alanya, Belek, Kemer): Hotels dort sind gefilmt, aber es gibt keine Landingpage pro Region – nur Side existiert, und das außerhalb der Türkei-Struktur (`/tuerkei-urlaub-side/`) | Türkei-Cluster | Größte ungenutzte Chance mit echter Kompetenz |
| 8 | **Kannibalisierung**: `/winterurlaub/` ↔ `/reise-blog/reiseziele-im-winter/` ↔ Monatsseiten Dez–Feb; `/singlereisen/` ↔ `/reise-blog/alleine-reisen-tipps/`; `/sommerurlaub-all-inclusive/` ↔ Türkei-Seite | 7 Seiten | Google schwankt zwischen den Seiten, keine rankt stark |
| 9 | **Hub-Lücken**: `/hotel/` (Elternpfad aller Hotelseiten) = 404, Breadcrumb springt von „Home“ direkt zum Hotel; Kategorie `/category/tuerkei/` (1 Beitrag, keine Description, H1 „Kategorie-Archiv:“) zusätzlich unter `/tuerkei/` erreichbar | Hotels, Kategorie | Schwache interne Struktur, Thin Archive |
| 10 | **Startseite/Buchungsseite**: H1 der Startseite „Dein Urlaub.Unsere Erfahrung.“ (ohne Leerzeichen, ohne Keyword); `/buchen/` ohne H1 und mit fast keinem indexierbaren Text | 982, 6793 | Unklare Relevanzsignale für die zwei wichtigsten Einstiege |

**Kleinere Punkte:** `haydi-weg.de` leitet zuerst auf `http://haydiweg.de/` und erst dann auf https um (2 Sprünge); Mailadresse `info@haydi-weg.de` nutzt die Bindestrich-Domain, die Website nicht (bewusst halten, aber Weiterleitung direkt auf https setzen); FAQ-Schema erzeugt seit 2023 für normale Unternehmen keine Rich Results mehr (unschädlich, aber kein Hebel).

---

## 5. Befund nach Seitentyp

| Seitentyp | Anzahl | Titelqualität | Hauptproblem | Maßnahme |
|---|---|---|---|---|
| Startseite | 1 | mittel | ohne Ort/USP, H1 schwach | neuer Titel + Description, H1 korrigieren |
| Lokale Seiten (Minden, Kontakt) | 2 | gut | ohne Vertrauenssignal, NAP | Titel mit „seit 2014“, Rufnummern vereinheitlichen |
| Cashback / Buchen | 2 | gut | Staffel nicht ehrlich angedeutet („bis zu“) | „30 bis 1.000 €“ statt nur „bis zu 1.000 €“ |
| Angebotsseiten (Pauschal, Last Minute) | 2 | gut | sachlich, austauschbar | Nutzen + ehrliche Beratung |
| Zielgebiete | 14 + Hub | gut | ohne Jahr, ohne Nutzenversprechen | Saison + konkreter Inhalt (Regionen, Preise) |
| Türkei-Ratgeber | 5 | gut | – | gezielt ergänzt |
| Hotelseiten mit Video | 15 | **sehr gut** | – | **beibehalten** |
| Hotelseiten ohne Video | 3 | **schlecht** | Thin Content | Titel-Fix + ausbauen oder noindex |
| Themen/Saison | 12 | mittel | generisch, Kannibalisierung | Saison + Fokus schärfen |
| Monatsratgeber | 12 + Hub | gut | Frage „Wo ist es warm?“ fehlt | Frage-Titel für Nov–Mai |
| Blog | 11 + Übersicht | gut | 1 veralteter Artikel | 2024 → 2027 nach Inhaltsupdate |
| Kategorie | 1 | schlecht | Thin Archive | noindex |
| Pflichtseiten | 3 | gut | – | unverändert |

---

## 6. Ergebnis der Optimierung (Kurzfassung)

- **89 Seiten** analysiert, je **3 Titelalternativen + finaler Titel** → `SEO_TITEL_VORHER_NACHHER.csv`
- **56 Titel** werden geändert, **33 bewusst beibehalten** (sie sind bereits stark oder rechtlich/neutral).
- **30 neue Meta-Descriptions**, die übrigen 59 bleiben, weil sie schon passen → `SEO_META_DESCRIPTIONS.csv`
- Umsetzung über **einen getesteten Rank-Math-Filter-Snippet** mit Vorschau-Modus → `HAYDIWEG_FINAL_SEO_SNIPPET.php`
- Struktur, Landingpages, Schema, lokale SEO → `SEO_LANDINGPAGE_STRATEGIE.md`
- Ablaufplan und Messkonzept → `SEO_PRIORITAETEN_90_TAGE.md`

### Bewertungsmaßstab für die Titelvorschläge
Jeder Vorschlag wurde nach diesen Kriterien geprüft; die messbaren Kriterien stehen als Spalte „Prüfung“ in der CSV:

| Kriterium | Wie geprüft |
|---|---|
| Darstellung in Google | Pixelbreite mit Arial 20 px berechnet (Desktop-Grenze ca. 580–600 px), Spalte `px` |
| Keyword-Platzierung | Hauptkeyword in den ersten ca. 25 Zeichen? („vorne / enthalten / fehlt“) |
| Marke | „haydi-weg“ enthalten, sofern Platz |
| Relevanz/Suchintention | Abgleich mit H1/H2 der Seite: Der Titel verspricht nur, was die Seite enthält (z. B. „Preise“ nur, wo es die Abschnitte „All Inclusive … und was es kostet“ gibt) |
| Glaubwürdigkeit | keine Superlative, keine Rabatte, keine Preise, nur belegbare Fakten (seit 2014, 5,0 bei Google mit 51 Bewertungen, Hotels selbst gefilmt – alle auf der Website genannt) |
| Differenzierung | Formulierung, die ein Großportal nicht glaubwürdig nutzen kann (Beratung vor Ort, selbst getestet) |
| Wiederholungen | kein doppeltes Keyword, keine doppelten Titel |

> **Hinweis:** Google schreibt laut eigenen Angaben einen Teil der Titel selbst um (häufig, wenn Titel zu lang sind oder nicht zur H1 passen). Deshalb sollten H1 und Titel inhaltlich übereinstimmen – die nötigen H1-Anpassungen stehen in `SEO_PRIORITAETEN_90_TAGE.md`.
