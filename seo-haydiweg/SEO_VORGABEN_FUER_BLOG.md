# SEO-Vorgaben für das Blog (verbindlich für Projekt 1)

**Stand:** 05.11.2026 · **Herausgeber:** SEO-Projekt (Projekt 2, Ordner `seo-haydiweg/`)
**Rangfolge (Vorgabe des Inhabers):** Diese Datei definiert die übergeordneten SEO-Regeln. Die Blogstrategie richtet sich danach. Wenn ein Blogartikel nur durch eine Ausnahme sinnvoll ist, wird das gemeinsam entschieden und in der Übergabedatei vermerkt.

---

## 1. Keyword-Besitz („ein Keyword – eine URL“)

- Maßgeblich ist **`SEO_KEYWORD_ZUORDNUNG.csv`**: 89 bestehende Seiten, 5 geplante Regionsseiten, 36 Blogartikel.
- Ein Blogartikel darf das **Hauptkeyword einer Seite** weder als Fokus-Keyword nutzen noch an den Anfang seines Titels stellen. Beispiele:
  - Erlaubt: „Ägypten im Winter: Wetter …“, weil die Ägypten-Seite „Ägypten Urlaub“ besitzt.
  - Nicht erlaubt: „Ägypten Urlaub im Winter …“
- Seiten besitzen die **Buchungs- und Übersichts-Keywords** („{Land} Urlaub“, „Pauschalreisen“, „Last Minute“, „Reisebüro Minden“, „{Monat} Reiseziele“, Hotelnamen).
- Blogartikel besitzen **Fragen, Vergleiche, Kosten, Einreise, Ferientermine und Monats- bzw. Wetterfragen zu einem Land** („Ägypten im Januar“, „Kreta oder Rhodos“, „Türkei Urlaub Kosten“).
- Neue Blogthemen außerhalb des Plans: vorher in der Keyword-Zuordnung prüfen und eintragen.

## 2. SEO-Titel (Rank Math „SEO-Titel“)

| Regel | Vorgabe |
|---|---|
| Aufbau | `Hauptbegriff: konkreter Nutzen \| haydi-weg` |
| Marke | „ \| haydi-weg“ am Ende, entfällt nur, wenn sonst gekürzt würde |
| Breite | **≤ 580 px** (Arial 20 px). Die Zeichenzahl ist nur ein Richtwert (ca. 50–62) |
| Jahreszahl | im Titel **ja** bei Saison-, Ferien-, Kosten- und Einreisethemen; in der **URL nie** |
| Verboten | Emojis und Häkchen (✅ ✔️ ☀️ ➡️), „die besten“, „Testsieger“, „günstigste“, Rabatt- oder Preisversprechen, Großbuchstaben-Wörter |
| H1 vs. Titel | H1 und Titel gleiche Aussage (die H1 darf länger sein); sonst schreibt Google den Titel eher um |
| Eindeutigkeit | kein Titel doppelt oder fast gleich (Ähnlichkeit > 0,8 laut `seo_abgleich.py`); bei Serien wie Osterferien/Sommerferien den Untertitel unterschiedlich formulieren |

## 3. Meta-Description

- 120–155 Zeichen (≤ ca. 960 px), **Du-Form**, natürlicher Satz, keine Keyword-Liste.
- Konkreter Inhalt (was steht im Artikel) und ein leiser Handlungsaufruf („… oder persönlich beraten lassen“).
- Keine Preise, Rabatte oder Superlative. Keine doppelten Descriptions.

## 4. URLs, Kategorien, Archive

| Thema | Vorgabe |
|---|---|
| Slugs | jahresneutral: `fruehbucher`, `osterferien`, `sommerferien`, `pfingstferien`, `brueckentage` (statt `…-2027`). Die Jahreszahl wird jedes Jahr nur in Titel und Text aktualisiert |
| Permalink | `/%category%/%postname%/` bleibt (bestehender Beitrag `/tuerkei/tuerkei-hotel-mit-aquapark/`). **Kategorie eines Beitrags nach Veröffentlichung nicht mehr ändern** (ändert die URL) |
| Neue Kategorien | Ägypten, Spanien, Griechenland, Dubai, Fernreisen, Reiseplanung – erlaubt |
| Kategoriearchive | Erst **indexieren**, wenn ≥ 5 veröffentlichte Beiträge **und** ein eigener Einleitungstext vorhanden sind; bis dahin in Rank Math auf `noindex`. Titelmuster „{Thema}-Ratgeber: Tipps & Reiseinfos \| haydi-weg“ – nie „{Land} Urlaub“ |
| Bestehende Ratgeber-Seiten | `/reise-blog/…` und `/reisethemen/…` bleiben WordPress-**Seiten**; nicht in Beiträge umwandeln (URL-Wechsel) |

## 5. Interne Verlinkung (Pflicht)

1. Jeder Artikel verlinkt **im ersten Drittel, im Fließtext** auf seine Ziel- oder Themenseite (Spalte „Pflicht-Link auf“ in der Keyword-Zuordnung), mit beschreibendem Ankertext.
2. Kette: **Ratgeber → Zielgebiet/Region → Hotelvideo → /buchen/ oder WhatsApp.**
3. Türkei-Artikel verlinken mindestens ein passendes **Hotelvideo** (`/hotel/…`) – das ist der stärkste Unterschied zu den Portalen.
4. Nicht verlinken auf: die 3 dünnen Hotelseiten (Acapulco, htop Amatista, L’Azure), `/category/tuerkei/`, `/tuerkei/`, `/hotel/`, `/reise-blog/beste-reiseziele-2024/` (wird umgezogen).
5. Nach Veröffentlichung trägt das SEO-Projekt Rückverlinkungen von den Zielseiten zu den Artikeln ein (siehe Übergabe).

## 6. Cashback-Formulierung (eine Sprachregelung für beide Projekte)

| Wo | Formulierung |
|---|---|
| Titel | Cashback nur auf `/cashback/` im Titel |
| Description, CTA-Kasten | „Bei Online-Buchung über haydiweg.de **30 bis 1.000 € Cashback ab 700 € Reisepreis**“ + Link auf `/cashback/` |
| Fließtext | „bis zu 1.000 € Cashback“ nur zusammen mit „ab 700 € Reisepreis“ bzw. „gestaffelt nach Reisepreis“ und Link auf die Teilnahmebedingungen |
| Nie | Cashback bei Buchungen per WhatsApp, Telefon oder im Büro versprechen (laut Teilnahmebedingungen ausgeschlossen) |

Grundlage: Teilnahmebedingungen auf `/cashback/`, Stand 28.10.2026.

## 7. Fakten, die nur so genannt werden dürfen

| Fakt | Formulierung | Quelle (Website) |
|---|---|---|
| Google-Bewertung | „5,0 bei Google“ (Anzahl nur mit Datum) | Startseite |
| Erfahrung | „Reisebüro in Minden seit 2014“ | Startseite |
| Hotelvideos | „Hotels selbst besucht und gefilmt“ (Zahlen 14/15 nur, wenn aktuell gezählt) | Startseite, Türkei-Seite |
| Öffnungszeiten | Mo–Fr 14–19 Uhr, Sa 10–15 Uhr | Kontakt |
| WhatsApp | **eine** Nummer – Klärung offen (0157 92326450 vs. 0155 63462222), bis dahin 0157 92326450 wie im Footer | Footer |

## 8. Strukturierte Daten für Beiträge

- `BlogPosting` (Rank Math „Artikel → Blogbeitrag“), Autor = echte Person (z. B. Hatice Köse) mit Autorenseite, nicht „admin“.
- FAQ-Abschnitt gern, FAQ-Schema optional (kein Rich-Result-Effekt, unschädlich).
- Kein Review-, Product-, Offer- oder Hotel-Rating-Schema.

## 9. Zusammenspiel mit dem SEO-Snippet (technisch geprüft)

- Der Snippet ändert **nur** die 56 Seiten-IDs und die 1 Kategorie, die er kennt. **Beiträge des Blogs werden nie überschrieben.**
- Getestet am 05.11.2026 in WordPress 7.1.4 mit Rank Math und der Permalink-Struktur `/%category%/%postname%/`, Snippet im Modus „live“. Ein Beitrag mit eigenem `rank_math_title` und eigener `rank_math_description` gab genau diese Werte aus.
- Einzige Ausnahme, gewollt: Hat ein Beitrag **keinen** eigenen Rank-Math-Titel, wird nur das alte Suffix „ - haydi-weg ☀ Urlaub leicht gemacht“ durch „ | haydi-weg“ ersetzt.
- **Deshalb gilt: Jeder Blogartikel bekommt einen eigenen SEO-Titel und eine eigene Description in Rank Math.**

## 10. Freigaben

Nichts wird veröffentlicht, aktiviert oder in den produktiven Einstellungen geändert, solange der Inhaber es nicht ausdrücklich freigibt. Das gilt für beide Projekte, für den Snippet ebenso wie für Blogartikel, Kategorien, noindex-Einstellungen und Weiterleitungen.
