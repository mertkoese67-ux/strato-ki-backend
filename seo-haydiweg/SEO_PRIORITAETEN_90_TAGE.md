# SEO-Prioritäten: 90-Tage-Plan & Erfolgsmessung

**Start:** KW 46/2026 (ab 09.11.2026) · Reihenfolge nach Wirkung ÷ Aufwand · ✅ = ohne Programmierung in Rank Math/Elementor machbar

---

## Phase 1 – Tage 1–14: schnelle, sichere Verbesserungen

| # | Aufgabe | Wo | Aufwand |
|---|---|---|---|
| 1 | **Ausgangswerte sichern** (siehe Messkonzept) – *vor* jeder Änderung | Search Console | 30 min |
| 2 | Snippet installieren, **Vorschau** testen, live schalten, WP Rocket leeren | Code Snippets | 1–2 h |
| 3 | **Rufnummern vereinheitlichen** (WhatsApp 0155… vs. 0157…, Festnetz im Schema) | Elementor, Rank Math Lokales SEO, Google-Profil | 1 h ✅ |
| 4 | Rank Math Lokales SEO: Telefon **+49 571 73075925** (bzw. korrekte Nummer), `sameAs` Instagram/Facebook/TikTok/YouTube/Google-Profil, Beschreibung neu (Du-Form, 1–2 Sätze), Website-Name „haydi-weg“ | Rank Math → Titel & Meta | 30 min ✅ |
| 5 | Rank Math → Titel & Meta → **Seiten**: Standard-Titelvorlage `%title% \| haydi-weg`, Schema-Standard für Seiten **„Keiner“** (Blogartikel bleiben Article) | Rank Math | 15 min ✅ |
| 6 | 3 dünne Hotelseiten (Acapulco, htop Amatista, L’Azure): veraltete Angebotslinks (Juni/Juli 2026) entfernen; **noindex**, bis sie ausgebaut sind | Elementor, Rank Math | 30 min ✅ |
| 7 | `/category/tuerkei/` → noindex; `/hotel/` → 301 auf `/urlaub-empfehlungen/` | Rank Math → Weiterleitungen | 10 min ✅ |
| 8 | Startseite H1: „Urlaub buchen mit persönlicher Beratung – dein Reisebüro in Minden“, Claim „Dein Urlaub. Unsere Erfahrung.“ (mit Leerzeichen) darunter | Elementor | 15 min ✅ |
| 9 | Saisonseiten Weihnachten/Silvester/Winter: Inhalte kurz prüfen (aktuelle Ziele, interne Links auf Ägypten/Dubai/Kanaren) – Saison läuft jetzt | Elementor | 1–2 h ✅ |
| 10 | `haydi-weg.de` direkt per 301 auf `https://haydiweg.de/` | STRATO Domainverwaltung | 10 min ✅ |

## Phase 2 – Tage 15–45: Inhalte an die neuen Titel angleichen

| # | Aufgabe |
|---|---|
| 11 | H1 angleichen, damit Google die neuen Titel nicht umschreibt: Türkei-, Ägypten-, Griechenland-, Spanien-Seite je einen Satz „Planung für 2027“ im Intro; H1 „Ostern Urlaub“ → „Osterurlaub: Reiseziele & Tipps“, „Pfingsten Urlaub“ → „Pfingsturlaub …“, „Türkei Urlaub - Side“ → „Side Urlaub: Hotels, Strände & Ausflüge“, „Türkei Urlaub Mittelmeer Strände“ → „Die schönsten Strände der Türkei am Mittelmeer“ |
| 12 | `/buchen/`: H1 + 150–250 Wörter Text oberhalb der Suche |
| 13 | „Beste Reiseziele 2024“ auf **2027** aktualisieren, neue URL `/reise-blog/beste-reiseziele/` + 301; danach Snippet-Eintrag einkommentieren |
| 14 | `/tuerkei-urlaub-side/` → `/urlaubsziele/tuerkei-urlaub-buchen/side/` (301), Hotels in Side ergänzen |
| 15 | **Neue Regionsseiten** Alanya und Belek (meiste gefilmte Hotels) – mit eigenen Videos, Vergleichstabelle, FAQ; Titel nach Muster „Alanya Urlaub {saison}: Orte, Hotels & Reisezeit \| haydi-weg“ |
| 16 | ~~Frühbucher-Seite~~ → entfällt, wird durch Blogartikel #11 abgedeckt (siehe `SEO_KEYWORD_ZUORDNUNG.csv`) |
| 17 | Interne Verlinkung nach den Regeln in `SEO_LANDINGPAGE_STRATEGIE.md` Abschnitt 5 (Blog → Ziel → Hotel → Buchung) |
| 18 | Google-Unternehmensprofil: Fotos, Leistungen, 1 Beitrag pro Woche (Hotelvideo) |

## Phase 3 – Tage 46–90: Ausbau & Auswertung

| # | Aufgabe |
|---|---|
| 19 | Regionsseiten Antalya/Lara und Kemer |
| 20 | Video-Schema (VideoObject) für die 15 Hotelseiten (Rank Math PRO) |
| 21 | Autorenseite (echte Person) statt „admin“ für Blogartikel |
| 22 | Kannibalisierung Winter: Blogartikel auf „warme Reiseziele im Winter“ umschreiben, Querverlinkung |
| 23 | **Auswertung nach 8 Wochen** (siehe unten), Titel mit schwacher CTR nachschärfen |
| 24 | Optional: bewährte Titel per Rank-Math-CSV-Import dauerhaft übernehmen und Snippet deaktivieren |

---

## Erfolgsmessung (Phase 8)

### Grundsätze
- **Keine Prognose von Besuchern oder Umsatz** – dafür fehlen Ausgangsdaten. Gemessen wird die *Veränderung* gegenüber dem eigenen Ausgangswert.
- Neue Titel sind **keine Ranking-Garantie**. Ihre direkte Wirkung zeigt sich vor allem in der **Klickrate (CTR)** bei gleichbleibender Position.
- Google kann Titel umschreiben; ob der eigene Titel angezeigt wird, kann man nur stichprobenartig in der echten Suche prüfen.
- Saisonalität (Reisen!) verfälscht Vorher/Nachher-Vergleiche. Darum **immer gegen das Vorjahr** oder gegen eine Kontrollgruppe vergleichen.

### Ausgangswerte sichern (Tag 0)
Search Console → Leistung → Suchergebnisse → Zeitraum **letzte 3 Monate** und **gleicher Zeitraum Vorjahr** → Export (Google Sheets/CSV) für:
1. **Seiten**-Tab: Klicks, Impressionen, CTR, Position je URL
2. **Suchanfragen**-Tab: Top 200 Suchanfragen
3. Filter Suchanfrage enthält „minden“ / „reisebüro“ (lokal)
4. Filter Seite enthält `/hotel/` (Hotelnamen-Suchen)

### Kennzahlen

| Kennzahl | Quelle | Wann aussagekräftig | Erwartbare Richtung |
|---|---|---|---|
| **CTR je geänderter Seite** bei ähnlicher Position (±1) | GSC → Seiten → Vergleich 28 Tage vorher/nachher | **nach 3–6 Wochen** | kurzfristig messbar, direkte Wirkung der Titel |
| Anteil, in dem Google den eigenen Titel zeigt | Stichproben in der Google-Suche (Inkognito) für die 20 wichtigsten Seiten | nach 2–4 Wochen | – |
| Impressionen je Landingpage | GSC | 6–12 Wochen | mittelfristig (Saisonbezug „2027“, neue Regionsseiten) |
| Durchschnittliche Position der Top-Suchanfragen | GSC → Suchanfragen | 2–6 Monate | langfristig (Inhalte, Links, lokale Signale) |
| Organische Klicks gesamt | GSC | 3–6 Monate, **gegen Vorjahr** | langfristig |
| Lokale Sichtbarkeit | Google-Unternehmensprofil → Leistung: Suchanfragen, Anrufe, Routenplanungen, Website-Klicks | 4–8 Wochen | mittelfristig |
| **Anfragen aus organischer Suche** | GA4 (falls aktiv): Ereignisse Klick auf `wa.me`-Links, Klick auf koalendar-Termin, Kontaktformular – gefiltert nach Kanal „Organic Search“ | laufend | entscheidend fürs Geschäft |
| Online-Buchungen aus organischer Suche | Schmetterling-IBE: Agenturreporting nach Buchungen; Zuordnung zu „organisch“ nur möglich, wenn die IBE UTM/Referrer übernimmt oder ein Conversion-Tracking auf der Bestätigungsseite eingerichtet ist → **mit Schmetterling klären** | laufend | – |
| Persönliche Buchungen | Im Büro/WhatsApp kurz fragen „Wie haben Sie uns gefunden?“ und in einer Liste notieren | laufend | einfache, sehr aussagekräftige Ergänzung |

### Empfehlung zum Tracking (falls noch nicht vorhanden)
- **GA4 + Consent (CookieYes)**: Ereignisse `whatsapp_click`, `termin_click`, `buchen_click` (Klick auf „Reise suchen“) als Schlüsselereignisse.
- **UTM-Parameter** im Google-Unternehmensprofil-Websitelink (`?utm_source=google&utm_medium=organic&utm_campaign=gbp`), um Profil-Besucher von normaler organischer Suche zu trennen.

### Auswertungsrhythmus
| Zeitpunkt | Was |
|---|---|
| Woche 2 | Stichprobe: werden neue Titel angezeigt? Fehler in GSC? |
| Woche 6 | CTR-Vergleich je geänderter Seite (gleiche Position) – Titel mit sinkender CTR prüfen |
| Woche 12 | Gesamtbewertung: CTR, Impressionen, Klicks, Anfragen; Entscheidung über dauerhafte Übernahme in Rank Math |
| Monat 6 | Positionen, neue Regionsseiten, lokale Sichtbarkeit, Vorjahresvergleich zur Sommer-2027-Saison |

### Was kurzfristig vs. langfristig wirkt

| Kurzfristig (Wochen) | Langfristig (Monate) |
|---|---|
| Neue Titel/Descriptions → CTR | Regionsseiten Türkei → neue Rankings |
| Schema- und NAP-Korrekturen → saubere Darstellung | Interne Verlinkung → Stärkung der Geldseiten |
| Thin Content auf noindex → Qualitätssignal | Bewertungen, Google-Profil, lokale Links → Local Pack „Reisebüro Minden“ |
| Saisonbezug „2027“ → Relevanz zur Saisonplanung | Video-Schema, Autoren → Vertrauen (E-E-A-T) |
