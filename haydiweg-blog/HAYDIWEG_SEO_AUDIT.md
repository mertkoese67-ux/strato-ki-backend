# SEO-Istbericht haydiweg.de

Stand: 05.11.2026 · Methode: Crawl aller 89 URLs aus der XML-Sitemap und der öffentlichen WordPress-REST-API, nur lesend, mit 0,3 Sekunden Pause zwischen Abrufen. Dazu kamen Labormessungen mit Chromium (Mobil-Emulation Pixel 7) und Google-Autocomplete als Nachfragesignal.

**Was diese Analyse NICHT enthält:** Daten aus der Google Search Console und aus Google Analytics (GA4-Property `G-88LNC86BM5` ist eingebunden). Dafür gibt es in dieser Umgebung keinen autorisierten Zugang. Deshalb nenne ich keine Klicks, Impressionen, Rankings oder Besucherzahlen. Alle Aussagen zu Kannibalisierung und Ranking-Chancen sind **Hypothesen**, die in der Search Console geprüft werden müssen (siehe Abschnitt 9).

Die Rohdaten liegen in `_arbeitsdaten/` (URL-Liste, Mediathek-Inventar, Autocomplete).

---

## 1. Technische Basis (festgestellt)

| Komponente | Befund |
|---|---|
| CMS | WordPress, PHP 8.4, Apache (STRATO) |
| Page Builder | Elementor + Elementor Pro, ElementsKit |
| SEO-Plugin | **Rank Math** (Sitemap, Schema, Meta). Die Namespaces `rankmath/v1/…` sind in der REST-API aktiv |
| Performance | WP Rocket aktiv |
| Weitere | All-in-One WP Migration (ai1wm), Trustindex (Bewertungs-Widget), Elementor-MCP-Composer und WordPress-MCP-Endpunkt (`/wp-json/mcp`), eigener Cookie-Consent mit Google Analytics, YouTube und Maps |
| Buchungsstrecke | /buchen/ mit eingebetteter IBE. Nicht analysiert und nicht verändert |
| Weiterleitungen | http → https und www → ohne www jeweils 301, korrekt |
| robots.txt | Sauber: sperrt nur /wp-admin/ und verweist auf die Sitemap |
| XML-Sitemap | `sitemap_index.xml` von Rank Math: 1 Beitrag, 87 Seiten, 1 Kategorie |

## 2. Inhaltsbestand

| Typ | Anzahl | Bemerkung |
|---|---|---|
| Echte Blog-**Beiträge** (post) | **1** | „Türkei-Hotels mit Aquapark“ vom 02.11.2026, Kategorie Türkei |
| Ratgeber als **Seiten** unter /reise-blog/ | 11 | z. B. Checkliste, Reiseziele im Winter, Günstige Reiseziele |
| Monatsseiten /reisethemen/reiseziele-<monat>/ | 12 + Übersicht | |
| Themenseiten (Ostern, Pfingsten, Herbstferien, Silvester, Weihnachten, Winterurlaub, Familienurlaub, Strandurlaub …) | 13 | |
| Zielgebietsseiten /urlaubsziele/…-urlaub-buchen/ | 17 + Übersicht | 5.300 bis 6.100 Wörter, mit FAQ-Schema |
| Türkei-Unterseiten (Reisezeit, Istanbul ×2, Strände) | 4 | |
| Hotelseiten /hotel/ | 19 | 16 ausführliche Seiten mit eigenem Video, 3 dünne Platzhalter (Spanien/Kroatien) |
| Kategorien | Türkei (1 Beitrag), Uncategorized (leer, noindex) | |
| Mediathek | 947 Dateien | 42 % WebP, 10 % AVIF, 37 % JPEG, 9 % PNG |

**Wichtigster Strukturbefund:** Bisher wurde fast der gesamte Ratgeber-Inhalt als *Seiten* gebaut. Das hat Folgen:
- Diese Seiten haben kein BlogPosting-Schema, kein sichtbares Aktualisierungsdatum, keinen RSS-Feed und kein Kategoriearchiv.
- Rank Math kennzeichnet sie als `Article` mit Datum 2024, obwohl sie überarbeitet wurden.
- Neue Artikel sollten deshalb Beiträge werden (siehe CLAUDE_BLOG_ANFORDERUNGEN W1).

## 3. On-Page: Titles, Descriptions, Überschriften

**Gut:** 85 von 89 URLs haben eigene, beschreibende Titles mit 46–61 Zeichen. Meta-Descriptions haben 122–160 Zeichen. Titel sind nicht doppelt. Fast jede Seite hat genau eine H1. Die Zielgebietsseiten haben klar formulierte Suchintentionen („Ägypten Urlaub buchen – Hurghada & Rotes Meer“).

**Probleme (priorisiert):**

| Prio | Befund | URL(s) | Empfehlung |
|---|---|---|---|
| Hoch | Generische Meta-Description „Die besten Angebote mit top Preis-Leistungs-Verhältnis.“ (55 Zeichen), Titel mit Tippfehler „Hotel Acaplco“, H1 „Hotel Empfehlung : …“, ca. 880 Wörter Vorlagentext, **0 Kontextlinks** | /hotel/hotel-acapulco-lloret/, /hotel/hotel-htop-amatista/, /hotel/l-azure-hotel/ | Entweder auf das Niveau der Türkei-Hotelseiten bringen oder auf `noindex` setzen bzw. zusammenführen. Im jetzigen Zustand gelten sie als „Thin Content“ |
| Hoch | Veralteter Inhalt, der indexiert ist: „Beste Reiseziele 2024“ (Title mit ✅-Emojis, alter Stil) | /reise-blog/beste-reiseziele-2024/ | Auf „Beste Reiseziele 2027“ aktualisieren. Die URL behalten oder per 301 auf eine neue Jahres-URL umleiten |
| Mittel | Keine H1 | /anfahrt/, /buchen/ | H1 ergänzen („Anfahrt zum Reisebüro in Minden“, „Reise suchen und buchen“) |
| Mittel | Keine Meta-Description, Title im alten Format „Anfahrt - haydi-weg ☀ Urlaub leicht gemacht“ | /anfahrt/ | Ergänzen bzw. vereinheitlichen |
| Mittel | Knappe H1 ohne Nutzenversprechen auf vielen Ratgeberseiten („Ostern Urlaub“, „Reiseziele Februar“, „Türkei Urlaub - Side“) | Themenseiten, /reisethemen/* | H1 an den (guten) Title angleichen, z. B. „Urlaub in Side: Hotels, Ausflüge und Tipps“ |
| Niedrig | „/reise-blog“ ohne Schrägstrich liefert 200 statt 301 | /reise-blog | Der Canonical ist korrekt, daher gering. Prüfen, ob WP Rocket den Slash-Redirect überspringt |

## 4. Indexierung, Canonicals, strukturierte Daten

- Alle 89 URLs sind `index, follow` und haben einen selbstreferenzierenden Canonical. Tag-, Autoren- und Uncategorized-Archive stehen korrekt auf `noindex`.
- Rank-Math-Schema: Organization/TravelAgency, WebSite, WebPage und BreadcrumbList sind überall vorhanden. Die Zielgebiets- und Hotelseiten haben FAQPage, der Beitrag hat BlogPosting.
- **Schwächen:**
  - Rechtstexte (AGB, Datenschutz, Impressum) und Hotelseiten tragen den Typ `Article`. Für Hotelseiten wäre ein `Hotel`- bzw. `LodgingBusiness`-Bezug sinnvoller. Für Rechtstexte reicht `WebPage`.
  - **Autor im Schema ist „admin“** (Person-Node mit Link auf /author/admin/). Das schwächt die E-E-A-T-Signale einer Reisebüro-Marke. Empfehlung: Autor „Hatice Köse“ mit Bio, Funktion und Verweis auf das Reisebüro in Minden.
  - Hinweis zu FAQPage: Google zeigt FAQ-Rich-Results seit 2023 nur noch für Behörden- und Gesundheitsseiten. Das Schema schadet nicht und hilft KI-Systemen beim Verständnis, bringt aber keine Snippet-Erweiterung mehr.

## 5. Interne Verlinkung

Gezählt wurden heuristisch die Kontextlinks im Inhaltsbereich, ohne Header, Footer und Navigation:

- **Stark verlinkt:** /reise-blog/reiseziele-im-winter/ (59), /urlaub-empfehlungen/ (58), /buchen/ (52), Beste Reisezeit Türkei (43), Aquapark-Beitrag (43). Das liegt an Teaser-Widgets, die sitewide eingebaut sind.
- **Kaum oder gar nicht verlinkt:**
  - 0 Links: die drei dünnen Hotelseiten, /anfahrt/, /reisethemen/
  - 1–2 Links: Quattro Beach, Rubi Platinum Spa, Serenity Queen, Spice, Swandor Kemer, Istanbul ×2, Alleine reisen, Urlaub mit Hund, Osteuropa
  - Die **Zielgebietsseite Ägypten** bekommt nur 9 Kontextlinks und die Dom. Republik 5, obwohl beide strategisch wichtig sind.
- **Folge für den Blog:** Jeder neue Artikel verlinkt seine Zielgebietsseite als Pillar, dazu passende gefilmte Hotels und 1–3 Schwesterartikel. Die Ziele sind im Redaktionsplan festgelegt. Gefilmte Hotels mit wenig Links (Spice, Swandor Kemer, Quattro, Rubi Spa, Serenity Queen) werden gezielt aus den Türkei-Artikeln 08, 12, 14, 31 und 35 angesteuert.

## 6. Mobile Darstellung und Ladezeiten (Labormessung)

Messung: Chromium mit Pixel-7-Emulation, ohne Netzwerkdrosselung, Rechenzentrum in der Cloud. Die Werte sind **nicht** mit den Felddaten (CrUX) gleichzusetzen. Für echte Werte bitte PageSpeed Insights oder den Core-Web-Vitals-Bericht in der Search Console nutzen.

| URL | TTFB | LCP | CLS | Requests | Horizontal-Scroll |
|---|---|---|---|---|---|
| Startseite | 724 ms | 2,0 s | 0,000 | 56 | nein |
| Aquapark-Beitrag | 512 ms | 2,5 s | 0,000 | 41 | nein |
| /reise-blog/ | 513 ms | 1,5 s | 0,000 | 51 | nein |
| Türkei-Zielgebiet | 592 ms | 1,7 s | 0,000 | 51 | nein |

- Layout-Stabilität ist sehr gut (CLS 0). Ein horizontales Überlaufen gibt es nicht. Die Mobilnavigation hat einen WhatsApp-Button und eine Cashback-Leiste.
- **Auffällig:** Das HTML ist sehr groß (Startseite ca. 730 KB, Hotelseiten bis 860 KB, Beitrag ca. 220 KB). Das kommt von Elementor-Markup, Inline-CSS und SVGs. Die TTFB von 500–720 ms ist für eine gecachte Seite eher hoch. Empfehlung: WP-Rocket-Cache-Vorladung und „Remove Unused CSS“ prüfen, außerdem Elementor-Optimierungen (Optimized DOM Output, Improved CSS Loading).
- Der Cookie-Banner überdeckt auf dem Smartphone fast den ganzen ersten Bildschirm. Das ist rechtlich in Ordnung, kann aber Absprungraten erhöhen. Es ist kein SEO-Problem, weil Google den Banner als Interstitial für Rechtszwecke akzeptiert.

## 7. Bilder

- Gut: moderne Formate (WebP/AVIF) bei der Mehrheit der neuen Bilder, Lazy Loading durch WP Rocket.
- **824 von 947 Mediendateien haben keinen ALT-Text in der Mediathek.** Im Crawl hatten 974 von 2.241 eingebundenen `<img>` kein ALT-Attribut. Ein Teil davon sind dekorative Icons, ein großer Teil sind aber Hotel- und Zielbilder.
- Dateinamen wie „Unbenannt-…“ und „Screenshot-…“ (52 Dateien) sowie „Snapinsta.app_…“ (5 Dateien, vermutlich Instagram-Downloads) bergen ein **Urheberrechtsrisiko**. Die Herkunft sollte geklärt werden, die Dateien werden in neuen Entwürfen nicht verwendet.
- Empfehlung: ALT-Texte nach Priorität nachpflegen, zuerst Hotel- und Zielgebietsseiten. Das lässt sich gut halbautomatisch mit Prüfung erledigen.

## 8. Blog-Präsentation auf der Startseite

Die Startseite verlinkt den Reise-Blog an vier Stellen, darunter ein Teaser „Türkei · Neu“ für den Aquapark-Beitrag und Kacheln für 5 Ratgeberseiten. **Das ist gut gelöst.** Die Teaser scheinen jedoch manuell gepflegt zu werden. Empfehlung: Ein Elementor-Loop-Grid „Neueste Beiträge“ (3 Kacheln) zeigt neue Artikel automatisch an, ohne dass bei jedem Beitrag die Startseite angepasst werden muss. **Das ist eine Änderung an der Live-Startseite und braucht deine Freigabe.**

/reise-blog/ ist eine statische Seite. Neue Beiträge erscheinen dort nicht automatisch. Empfehlung: Dort ebenfalls ein Loop-Grid nach Kategorien (Türkei, Ägypten, Spanien, Griechenland, Dubai, Fernreisen, Reiseplanung) einbauen.

## 9. Keyword-Kannibalisierung (Hypothesen, in der GSC zu prüfen)

| Themengruppe | Konkurrierende URLs | Risiko | Prüfung in der GSC |
|---|---|---|---|
| Winterurlaub | /winterurlaub/, /reise-blog/reiseziele-im-winter/, /reisethemen/reiseziele-dezember/, /reisethemen/reiseziele-januar/, /reisethemen/reiseziele-februar/ | **hoch** | Leistung → Suchanfragen „winter“, „warm im winter“ → Tab „Seiten“: Wechseln die URLs? |
| Alleinreisen | /reise-blog/alleine-reisen-tipps/ und /singlereisen/ | mittel | Suchanfragen „alleine reisen“, „singlereisen“ |
| Ostern/Pfingsten | /ostern-urlaub/ und /reisethemen/reiseziele-april/ (plus geplant: Osterferien 2027) | mittel | Die neuen Ferienartikel zielen auf *Termine* und grenzen sich damit ab |
| Türkei-Reisezeit | /beste-reisezeit-tuerkei/ und geplant „Türkei im Winter“ (06) und „Wassertemperatur Türkei“ (28) | mittel | Nach 8 Wochen prüfen. Falls die URLs um dieselben Suchanfragen konkurrieren, die Artikel als Abschnitte in die Reisezeit-Seite überführen und per 301 umleiten |
| Türkei-Familie | /familienurlaub/, Aquapark-Beitrag, geplant 14 und 23 | gering | Unterschiedliche Fokus-Keywords, gegenseitig verlinkt |

## 10. Welche Angebote der Blog stützen kann

| Zielgebietsseite / Angebot | Unterstützende neue Artikel |
|---|---|
| Türkei + 16 gefilmte Hotels | 04, 06, 08, 12, 14, 21, 23, 25, 28, 31, 35 |
| Ägypten | 02, 03, 07, 20, 26 |
| Spanien | 01, 21, 34 |
| Griechenland | 18, 30, 36 |
| Dubai | 05, 10, 27 |
| Malediven, Dom. Republik | 19, 33 |
| Pauschalreisen, Last Minute, Cashback | 09, 11, 17, 25, 32 |
| Familienurlaub | 13, 14, 16, 23, 26, 36 |
| **Lücke:** keine Zielgebietsseite für Thailand/Bali | 15 und 22 verlinken vorerst /urlaubsziele/. Empfehlung: Zielgebietsseite „Thailand Urlaub buchen“ anlegen |

## 11. Priorisierte Maßnahmenliste

| # | Maßnahme | Aufwand | Wirkung | Freigabe nötig |
|---|---|---|---|---|
| 1 | Search Console und GA4 für die Auswertung freigeben (Lesezugriff oder monatlicher Export) | gering | Voraussetzung für alles Weitere | ja |
| 2 | Autor „admin“ durch ein echtes Autorenprofil ersetzen (Name, Bio, Foto) | gering | E-E-A-T | ja |
| 3 | Drei dünne Hotelseiten überarbeiten oder auf noindex setzen | mittel | Qualitätssignal | ja |
| 4 | „Beste Reiseziele 2024“ auf 2027 aktualisieren | mittel | Aktualität, saisonaler Traffic im Januar | ja |
| 5 | Loop-Grid für neue Beiträge auf /reise-blog/ und der Startseite | gering | Neue Artikel werden schneller gefunden und gecrawlt | ja |
| 6 | Neue Kategorien anlegen: Ägypten, Spanien, Griechenland, Dubai, Fernreisen, Reiseplanung | gering | Struktur, Permalinks | ja |
| 7 | ALT-Texte nachpflegen (Hotel- und Zielgebietsseiten zuerst) | mittel | Bildersuche, Barrierefreiheit | ja |
| 8 | Klären, ob die Winter-Seiten kannibalisieren (nach GSC-Zugang) | gering | Ranking-Stabilität | – |
| 9 | H1 auf /anfahrt/ und /buchen/ ergänzen, Titel und Meta von /anfahrt/ | gering | Sauberkeit | ja |
| 10 | Zielgebietsseite Thailand anlegen | hoch | Fernreisen-Cluster | ja |
| 11 | Server-Antwortzeit und Elementor-DOM optimieren | mittel | Core Web Vitals | ja |
| 12 | Herkunft der Bilder mit „Snapinsta“, „Screenshot“ und „Unbenannt“ klären | gering | Rechtssicherheit | – |

Während der Analyse habe ich auf der Website nichts verändert.
