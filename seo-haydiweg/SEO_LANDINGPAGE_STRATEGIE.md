# SEO-Architektur & Landingpage-Strategie haydi-weg

**Leitlinie:** Weniger, dafür bessere Seiten. Jede neue Seite braucht echte eigene Inhalte (Videos, Erfahrungen, Beratung), sonst wird sie nicht gebaut. Keine Städte-Doorway-Seiten („Reisebüro Bad Oeynhausen“ usw.), keine Massen-Landingpages mit getauschtem Ländernamen.

Positionierung, die überall durchscheinen soll:
**Reisebüro mit persönlicher Beratung in Minden · Türkei-Spezialist mit selbst gefilmten Hotels · weltweite Reisen · faire Preise mit Cashback bei Online-Buchung**

---

## 1. Welche Zielgebietsseiten fehlen?

Bewertet nach vorhandener Kompetenz (Hotels gefilmt?) und Suchintention. **Nur Seiten mit echtem Inhalt.**

| Priorität | Neue Seite (Vorschlag URL) | Warum | Inhaltlicher Kern (Pflicht) |
|---|---|---|---|
| **1** | `/urlaubsziele/tuerkei-urlaub-buchen/antalya-lara/` | Mardan Palace, Swandor Topkapi gefilmt; „Antalya Urlaub“ ist eines der wichtigsten Türkei-Keywords | Lara vs. Konyaaltı vs. Altstadt, Transferzeiten, eigene Hotels, Reisezeit, FAQ |
| **1** | `/urlaubsziele/tuerkei-urlaub-buchen/alanya/` | 6 Hotels gefilmt (Quattro ×2, Rubi ×2, Selene, Serenity) | Konaklı/Avsallar/Türkler/Zentrum im Vergleich, Strandtypen, Hotels nach Urlaubsart |
| **1** | `/urlaubsziele/tuerkei-urlaub-buchen/belek/` | 4 Hotels gefilmt (Ela, Selectum ×2, Spice) | Golf, Sandstrand, Familien-Resorts, Transfer |
| **2** | `/urlaubsziele/tuerkei-urlaub-buchen/kemer/` | 3 Hotels gefilmt (Mirage, NG Phaselis, Swandor Kemer) | Göynük/Kiriş/Tekirova, Berge + Meer, Steg-Strände. **Abstimmung Blog:** Blogartikel #35 „Urlaub in Kemer“ zielt auf dasselbe Keyword → Empfehlung: Inhalt von #35 als diese Seite nutzen (siehe `SEO_ABGLEICH_BLOGSTRATEGIE.md`) |
| **2** | `/urlaubsziele/tuerkei-urlaub-buchen/side/` | **Bestehende** `/tuerkei-urlaub-side/` dorthin umziehen (301), statt neu zu bauen | wie heute + eigene Hotels |
| ~~2~~ | ~~`/fruehbucher/`~~ **gestrichen** (Abstimmung Blog, 05.11.2026) | „Frühbucher {saison}“ wird allein vom Blogartikel #11 besetzt (jahresneutraler Slug). Eine zweite Frühbucher-URL würde mit ihm konkurrieren. | – |
| ~~3~~ | ~~`/tuerkei/adults-only-hotels/`~~ **an das Blog-Projekt übergeben** | Wird durch Blogartikel #31 „Adults-Only-Hotels in der Türkei“ abgedeckt (muss Selene Beach & Spa verlinken) | – |
| **3** | Hurghada, Mallorca, Kreta | **Erst** wenn eigene Hotels besucht/gefilmt wurden. Bis dahin decken die Länderseiten diese Begriffe in H2-Abschnitten ab. | – |

**Nicht bauen:** eigene Seiten für jedes der 30 Ziele, „Pauschalreisen {Land}“ zusätzlich zu „{Land} Urlaub buchen“ (wäre Kannibalisierung), Städte-Seiten rund um Minden.

## 2. Welche Seiten konkurrieren um dieselben Keywords?

| Keyword-Cluster | Konkurrierende Seiten | Lösung |
|---|---|---|
| Winterurlaub / warme Ziele im Winter | `/winterurlaub/`, `/reise-blog/reiseziele-im-winter/`, `/reisethemen/reiseziele-dezember/` (+ Januar, Februar) | `/winterurlaub/` = **Buchungs**-Seite „Sonne oder Schnee“; Blogartikel auf **„warme Reiseziele im Winter“** fokussieren (neuer Titel); Monatsseiten bleiben bei „Wo ist es im Dezember warm?“. Gegenseitig verlinken. |
| Alleine reisen | `/singlereisen/` ↔ `/reise-blog/alleine-reisen-tipps/` | Singlereisen = Buchung/Angebote (Einzelzimmerzuschlag, Ziele); Blog = Tipps & Sicherheit. Titel bereits getrennt. |
| All Inclusive Sommer / Türkei | `/sommerurlaub-all-inclusive/` ↔ `/urlaubsziele/tuerkei-urlaub-buchen/` | Sommerseite = länderübergreifend (Türkei, Ägypten, Griechenland, Spanien). Türkei-Seite = Türkei. Im Text „Türkei All Inclusive“ auf die Türkei-Seite verlinken. |
| Urlaub buchen / Pauschalreisen | Startseite ↔ `/pauschalreisen/` ↔ `/buchen/` | Startseite = Marke + Beratung; `/pauschalreisen/` = Keyword „Pauschalreisen“; `/buchen/` = Werkzeug (Suche). Titel sind jetzt klar getrennt. |
| Beste Reiseziele | `/reise-blog/beste-reiseziele-2024/` ↔ `/urlaubsziele/` | Artikel auf 2027 aktualisieren, Hub bleibt „Urlaubsziele“. |
| Türkei-Kategorie | `/category/tuerkei/` und `/tuerkei/` ↔ Türkei-Seite | Kategorie auf **noindex**, bis sie mindestens 5 Beiträge hat. |

## 3. Keywords für die Startseite

**Ja:** Urlaub buchen · persönliche Beratung · Reisebüro Minden · Türkei (Spezialist) · Pauschalreisen · selbst gefilmte Hotels (Marke + Vertrauen).
**Nein (eigene Landingpages):** Länder, Last Minute, Cashback-Details, Saisonbegriffe.

H1-Vorschlag: **„Urlaub buchen mit persönlicher Beratung – dein Reisebüro in Minden“**, Claim „Dein Urlaub. Unsere Erfahrung.“ als Unterzeile (mit Leerzeichen).

## 4. Keywords für eigenständige Landingpages

| Landingpage | Hauptkeyword | Nebenkeywords |
|---|---|---|
| `/urlaubsziele/tuerkei-urlaub-buchen/` | Türkei Urlaub | Pauschalreisen Türkei, Türkei All Inclusive, Türkei Urlaub 2027 |
| Regionen (neu) | Antalya Urlaub, Alanya Urlaub, Belek Urlaub, Kemer Urlaub | + „Hotels“, „All Inclusive“, „beste Reisezeit“ |
| `/pauschalreisen/` | Pauschalreisen buchen | Pauschalreise, Flug und Hotel |
| `/last-minute-urlaub/` | Last Minute Urlaub | Last Minute Türkei/Ägypten |
| Blogartikel #11 (Slug `fruehbucher`) | Frühbucher 2027 | Sommerurlaub 2027 früh buchen – *keine eigene Landingpage* |
| `/reisebuero-minden-urlaub-buchen/` | Reisebüro Minden | Reiseberatung Minden, Türkei Reisebüro |
| `/cashback/` | Reise Cashback | Urlaub mit Cashback |
| `/urlaub-empfehlungen/` | Türkei Hotels Erfahrungen | Hotelvideos Türkei |
| Hotelseiten | {Hotelname} | {Hotel} Erfahrungen, {Hotel} Video |

## 5. Verlinkung Blog ↔ Angebotsseiten

Prinzip **„Ratgeber → Ziel → Hotel → Buchung/Beratung“**:

```
Blog/Ratgeber ──► Zielgebiets-/Regionsseite ──► Hotelseite (Video) ──► /buchen/ oder WhatsApp
      ▲                       │                          │
      └──── „Passend dazu“ ◄──┴──── Ratgeber zur Region ◄┘
```

Konkrete Regeln:
1. Jeder Blogartikel verlinkt **im Fließtext** (nicht nur im Kasten „Passend dazu“) auf genau **eine** passende Zielgebiets- oder Themenseite mit beschreibendem Ankertext („Türkei Urlaub mit All Inclusive“ statt „hier“).
2. Jede Zielgebietsseite verlinkt auf ihre 2–4 wichtigsten Ratgeber (beste Reisezeit, Sehenswürdigkeiten, Strände).
3. Jede Hotelseite verlinkt auf ihre **Regionsseite** (sobald vorhanden) und auf den Aquapark-/Adults-only-Vergleich, wenn passend.
4. Monatsseiten verlinken jedes genannte Ziel auf seine Länderseite.
5. Cashback wird nur verlinkt, nicht wiederholt erklärt; der Satz „ab 700 € Reisepreis“ steht bei jeder Erwähnung dabei.
6. `/hotel/` per **301 auf `/urlaub-empfehlungen/`** leiten (Rank Math → Weiterleitungen), damit der Elternpfad nicht ins Leere führt.

## 6. Verbessern statt neu bauen

| Bestehende Seite | Verbesserung |
|---|---|
| `/tuerkei-urlaub-side/` | in den Türkei-Pfad verschieben (301), eigene Hotels ergänzen, H1 „Side Urlaub: Hotels, Strände & Ausflüge“ |
| `/reise-blog/beste-reiseziele-2024/` | Inhalt auf 2027, neue URL `/reise-blog/beste-reiseziele/` (jahresneutral, 301 von alt), danach vorbereiteten Snippet-Eintrag einschalten |
| 3 dünne Hotelseiten | ausbauen (Video, eigene Eindrücke) **oder** noindex + aus der Sitemap nehmen; Angebotslinks mit festen, abgelaufenen Daten entfernen |
| `/buchen/` | H1 + 150–250 Wörter erklärender Text oberhalb der IBE (wie suchen, welche Veranstalter, Cashback-Hinweis, Beratung) |
| `/category/tuerkei/` | noindex, Kategoriebeschreibung ergänzen |
| `/traumurlaub/` | sehr allgemeine Seite: entweder mit `/urlaubsziele/` zusammenlegen (301) oder als „Reiseberatung: so finden wir deinen Traumurlaub“ schärfen |
| Startseite | H1 korrigieren (s. o.) |

## 7. Strukturierte Daten (technisch und inhaltlich sinnvoll)

| Typ | Wo | Wie (Rank Math, ohne Code) |
|---|---|---|
| **TravelAgency / LocalBusiness** | global | Rank Math → Titel & Meta → Lokales SEO: Telefon im Format **+49 571 73075925** (bzw. die Nummer, unter der Kunden wirklich anrufen), Öffnungszeiten, Geo-Koordinaten, **sameAs**: Instagram, Facebook, TikTok, YouTube, Google-Unternehmensprofil. Beschreibung in Du-Form, 1–2 Sätze, ohne Anführungszeichen. |
| **WebSite** | global | Website-Name auf **„haydi-weg“** setzen (Rank Math → Titel & Meta → Global/Lokales SEO); alternativer Name „haydi-weg Reisebüro“. Sonst zeigt Google ggf. „haydi-weg ☀ Urlaub leicht gemacht“ als Site-Namen. |
| **WebPage / AboutPage / ContactPage** | Startseite, Landingpages, Kontakt | Rank Math → Titel & Meta → Seiten: Schema-Typ **„Keiner“** statt „Article“ als Standard für Seiten; Blogartikel behalten „Article/BlogPosting“. Kontakt = ContactPage, Minden = AboutPage (bereits). |
| **Article/BlogPosting** | Blog | Autor: echte Person (z. B. Hatice Köse) mit Autorenseite statt „admin“ – stärkt E-E-A-T. |
| **BreadcrumbList** | alle | vorhanden; nach der /hotel/-Weiterleitung Ebene „Hotelvideos“ ergänzen. |
| **VideoObject** | Hotelseiten | Eigene YouTube-Videos als VideoObject auszeichnen (Rank Math PRO Video-Schema). Kann Video-Vorschauen in der Suche bringen. |
| **FAQPage** | vorhanden | unschädlich, bringt aber seit 2023 für normale Unternehmen keine Rich Results mehr – kein Ausbau nötig. |
| **Nicht verwenden** | – | `Hotel` mit `aggregateRating`/Sternen (es sind keine eigenen Gästebewertungen), `Offer`/`Product` mit Preisen (Preise ändern sich und kommen aus der IBE), Review-Schema für Google-Bewertungen (verboten: Selbst-Bewertungen). |

## 8. Canonical- und Indexierungsprobleme

| Befund | Bewertung | Maßnahme |
|---|---|---|
| Alle 89 Sitemap-URLs mit Selbst-Canonical und `index` | ✔ | – |
| `/buchen/?ibe=…` → Canonical auf `/buchen/` | ✔ korrekt | – |
| `/reise-blog/page/2/` → Canonical auf `/reise-blog/` | akzeptabel (Elementor-Seite) | – |
| `/tuerkei/` liefert 200 mit Kategorieinhalt (Canonical auf `/category/tuerkei/`) | kleiner Duplikat-Pfad | Kategorie noindex; optional 301 `/tuerkei/` → `/category/tuerkei/` |
| `/hotel/` = 404, ist aber Elternpfad | Strukturfehler | 301 → `/urlaub-empfehlungen/` |
| 3 dünne Hotelseiten indexiert | Qualitätsrisiko | ausbauen oder noindex |
| `haydi-weg.de` → `http://haydiweg.de/` → `https://` | 2 Sprünge | direkte 301 auf `https://haydiweg.de/` beim Domain-Anbieter/STRATO |
| Suche, Autor, 404, uncategorized = noindex | ✔ | – |

**Der Snippet verändert keine Canonicals und keine robots-Werte** (im Test nachgewiesen).

## 9. Größtes Potenzial für qualifizierten Traffic

1. **Türkei-Cluster** (Türkei-Seite + 4 Regionen + 15 Hotelvideos + Aquapark-Vergleich) – hier ist echte Kompetenz vorhanden, und Hotelnamen-Suchen sind kaufnah.
2. **Hotelseiten** – Suchende nach „{Hotel} Erfahrungen“ stehen kurz vor der Buchung; eigenes Video ist ein klares Klickargument.
3. **Lokal: „Reisebüro Minden“** – die Konkurrenz in den Ergebnissen ist schwach formuliert (TUI-Filialseite, Verzeichnisse).
4. **Saisonseiten Winter/Weihnachten/Silvester** jetzt (Nov/Dez) und **Sommer 2027 / Frühbucher / Sommerferien** ab Dezember (über die Blogartikel #11, #13, #16, #29 – siehe Keyword-Zuordnung).
5. **Ägypten** als Winterziel (die Startseite bewirbt es bereits).

## 10. Lokale SEO für das Reisebüro in Minden

| Maßnahme | Detail |
|---|---|
| **Google-Unternehmensprofil** | Kategorie „Reisebüro“ (primär), Zusatzkategorien prüfen; Öffnungszeiten identisch mit Website (Mo–Fr 14–19, Sa 10–15); Website-Link auf `/reisebuero-minden-urlaub-buchen/` oder Startseite; Fotos des Büros + Team; regelmäßige Beiträge (Hotelvideos!); Produkte/Leistungen „Türkei-Reisen“, „Pauschalreisen“, „Last Minute“ |
| **NAP vereinheitlichen** | **Eine** WhatsApp-Nummer und **eine** Festnetznummer überall gleich (Website-Footer, Minden-Seite, Kontakt, Schema, Google-Profil, Facebook, Instagram, Verzeichnisse). Aktuell drei verschiedene Nummern. |
| **Bewertungen** | Nach jeder Reise freundlich um eine Google-Bewertung bitten (Link per WhatsApp); auf Bewertungen antworten. Die Zahl „5,0 bei Google / 51 Bewertungen“ auf der Website aktuell halten (im Titel/Description wird nur „5,0 bei Google“ genannt, damit der Text nicht ständig angepasst werden muss). |
| **Verzeichnisse** | Einträge in Das Örtliche, Gelbe Seiten, Cylex, 11880, Apple Maps, Bing Places mit identischen Daten |
| **Lokale Inhalte** | Auf der Minden-Seite: Anfahrt, Parken, Einzugsgebiet im Fließtext (Minden, Porta Westfalica, Bad Oeynhausen, Petershagen, Hille) – **ohne** eigene Seiten pro Ort |
| **Abflughäfen** | Inhalte zu Abflügen ab Hannover, Paderborn, Münster/Osnabrück, Düsseldorf – das ist für Kunden aus Minden echter Mehrwert (z. B. als Abschnitt auf der Minden-Seite) |
| **Lokale Links** | Kooperationen mit Minden-Marketing, Vereinen, lokaler Presse (z. B. Reisevortrag, Türkei-Abend) |

---

## Cashback-Regel für alle Texte

Cashback wird nur dort beworben, wo die Bedingungen erreichbar sind: **Startseite** (verlinkt), **/cashback/** (vollständig), **/buchen/** (mit Staffel). In Titeln steht immer **„30 bis 1.000 €“** oder es steht nichts; die Formulierung „bis zu 1.000 €“ allein wird in neuen Titeln nicht verwendet, weil der Höchstbetrag erst ab 19.900 € Reisepreis gilt. Bestehende Descriptions mit „bis zu 1.000 € Cashback“ (z. B. Last Minute alt, Zypern, Herbstferien alt) wurden entweder ersetzt oder sind in `SEO_META_DESCRIPTIONS.csv` als „beibehalten“ markiert. **Empfehlung:** Auch dort bei der nächsten Überarbeitung „Cashback ab 700 € Reisepreis“ ergänzen.

---

## Nachtrag 05.11.2026: Abstimmung mit der Blogstrategie (Projekt 1)

- Verbindliche Keyword-Zuordnung für alle 89 Seiten, 5 geplante Regionsseiten und 36 Blogartikel: **`SEO_KEYWORD_ZUORDNUNG.csv`**
- Regeln für das Blog: **`SEO_VORGABEN_FUER_BLOG.md`**
- Befunde und offene Entscheidungen: **`SEO_ABGLEICH_BLOGSTRATEGIE.md`**
- Geändert aufgrund des Abgleichs: Türkei-Seitentitel ohne „Preise“ (Blog #25 besetzt „türkei urlaub kosten“), Landingpage `/fruehbucher/` gestrichen (Blog #11), Adults-only-Beitrag an Blog #31 übergeben, Kemer-Konflikt mit Blog #35 dokumentiert.
- **Neue Blog-Kategorien** (Ägypten, Spanien, Griechenland, Dubai, Fernreisen, Reiseplanung): Archive erst indexieren, wenn sie ≥ 5 veröffentlichte Beiträge und einen eigenen Einleitungstext haben; Titelmuster „{Thema}-Ratgeber: Tipps & Reiseinfos | haydi-weg“, damit sie nicht mit den Zielgebietsseiten („{Land} Urlaub …“) konkurrieren.
