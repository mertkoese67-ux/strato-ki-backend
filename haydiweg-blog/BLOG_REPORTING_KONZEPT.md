# SEO-Reporting-Konzept für den haydi-weg-Blog (November 2026 bis April 2027)

Grundsatz: Wir messen nur, was die Werkzeuge tatsächlich liefern. Prognosewerte gibt es nicht. Ziele sind als **Richtungs- und Prozessziele** formuliert. Absolute Zielwerte legen wir erst fest, wenn nach 8 Wochen echte Ausgangsdaten aus der Search Console vorliegen.

## 1. Datenquellen und Einrichtung (einmalig)

| Quelle | Zweck | Einrichtung |
|---|---|---|
| Google Search Console | Klicks, Impressionen, CTR, Position, Indexierung | Property `https://haydiweg.de/` prüfen. Für die Auswertung brauche ich einen Nutzer mit Leserechten oder einen monatlichen Export (Leistung → Exportieren → Google Sheets/CSV) |
| GA4 (`G-88LNC86BM5`, bereits eingebunden) | Besucher pro Artikel, Wege vom Blog zu Angeboten, Conversions | Events anlegen (siehe 3.). Beachten: GA4 erfasst nur Nutzer mit Einwilligung, die Zahlen sind deshalb **systematisch zu niedrig** und zeigen eher Trends als absolute Werte |
| Rank Math | Fokus-Keywords, Index-Status, optional Rank-Math-Analytics (verbindet GSC) | ist bereits vorhanden |
| IBE / Buchungsdaten | zuordenbare Buchungen | Prüfen, ob die IBE eine Referrer- oder Kampagnen-Übergabe (UTM, Agentur-ID, Subkennung) unterstützt. Falls nicht, nur über WhatsApp-Anfragen zuordnen |
| WhatsApp | Anfragen pro Artikel | Jeder Artikel hat einen vorausgefüllten Text mit Artikelnamen. Im Reisebüro wird pro Anfrage ein Strich in einer Tabelle gemacht: Datum, Artikel, Anfrage, gebucht ja/nein |

## 2. Kennzahlen (KPIs)

| KPI | Quelle | Definition | Rhythmus |
|---|---|---|---|
| Organische Klicks (Blog gesamt) | GSC | Seitenfilter: URL enthält eine der Blogkategorien (`/tuerkei/`, `/aegypten/`, `/spanien/`, `/griechenland/`, `/dubai/`, `/fernreisen/`, `/reiseplanung/`) | monatlich |
| Impressionen | GSC | wie oben | monatlich |
| Ø Position | GSC | nur pro Artikel und Suchanfrage sinnvoll. Der Gesamtdurchschnitt verfälscht durch neue Long-Tail-Rankings | monatlich |
| CTR | GSC | Klicks / Impressionen pro Artikel | monatlich |
| Indexierte Artikel | GSC → Seiten, Rank Math Index-Status | Anzahl veröffentlichter Beiträge mit Status „indexiert“ | wöchentlich in den ersten 8 Wochen |
| Wichtige Keywords | GSC Suchanfragen-Filter | Fokus-Keyword aus dem Redaktionsplan, Position und Impressionen | monatlich |
| Organische Besucher pro Artikel | GA4 → Berichte → Seiten, Segment „Organic Search“ | Sitzungen mit Einstieg auf dem Artikel | monatlich |
| Blog → Angebot | GA4-Events `click_buchen`, `click_hotelseite`, `click_cashback` mit Parameter `quellseite` | Anteil der Blog-Sitzungen mit mindestens einem dieser Events | monatlich |
| Blog → Anfrage | GA4-Event `click_whatsapp` + WhatsApp-Strichliste | Anzahl pro Artikel | monatlich |
| Zuordenbare Buchungen | IBE-Bericht / Strichliste | Buchungen mit nachweisbarem Blog-Kontakt | monatlich, Bewertung quartalsweise |

## 3. GA4-Events (Vorschlag, Einbau nur nach deiner Freigabe)

Umsetzung über den Google Tag Manager oder über das vorhandene Tracking-Setup. Plugins oder Themes ändere ich dafür nicht ohne Freigabe.

| Event | Auslöser | Parameter |
|---|---|---|
| `click_whatsapp` | Klick auf Link mit `wa.me` | `quellseite` (Pfad), `link_text` |
| `click_buchen` | Klick auf Link zu `/buchen/` | `quellseite` |
| `click_hotelseite` | Klick auf Link zu `/hotel/` | `quellseite`, `ziel` |
| `click_cashback` | Klick auf Link zu `/cashback/` | `quellseite` |
| `scroll_75` | 75 % Scrolltiefe auf Beiträgen | `quellseite` |

Als Schlüsselereignisse (Conversions) markieren: `click_whatsapp` und `click_buchen`.

## 4. Ziele (realistisch, ohne erfundene Zahlen)

| Zeitpunkt | Ziel | Messbar über |
|---|---|---|
| bis Ende Dezember 2026 | Alle bis dahin veröffentlichten Artikel sind innerhalb von 14 Tagen nach Veröffentlichung indexiert | GSC Seitenbericht |
| bis Ende Januar 2027 | Jeder Artikel hat in der GSC Impressionen für sein Fokus-Keyword **oder** für eine passende Long-Tail-Variante | GSC Suchanfragen pro Seite |
| Februar 2027 | **Ausgangswerte festlegen:** Klicks, Impressionen und CTR der ersten Artikel aus dem November. Daraus werden absolute Ziele für das 2. Quartal abgeleitet | Monatsbericht |
| bis Ende März 2027 | Die Gesamtklicks der Blogkategorien steigen von Monat zu Monat. Für mindestens 10 Artikel steht ein Long-Tail-Keyword in den Top 10 | GSC |
| bis Ende April 2027 | Anfragen aus dem Blog lassen sich nachweisen (WhatsApp-Strichliste/Events). Für die Top-5-Artikel ist die Quote Besucher → Angebotsklick bekannt | GA4 + Strichliste |

## 5. Wann lassen sich belastbare Aussagen treffen?

Das sind Erfahrungswerte und keine Prognose. Neue Inhalte auf einer etablierten Domain verhalten sich typischerweise so:

| Frage | Frühester belastbarer Zeitpunkt | Begründung |
|---|---|---|
| Wird ein Artikel indexiert? | wenige Tage bis 2 Wochen | Die GSC zeigt den Status direkt an. Notfalls per URL-Prüfung eine Indexierung beantragen |
| Bekommt ein Artikel Impressionen? | 2–6 Wochen | Google testet neue Seiten für verschiedene Suchanfragen |
| Ist die Position eines Artikels stabil? | 8–12 Wochen | Ranking-Schwankungen zu Beginn sind normal |
| Funktioniert die Content-Strategie insgesamt? | 4–6 Monate (etwa April/Mai 2027) | Erst dann gibt es genug Artikel und Datenpunkte. Saisonale Themen ranken teils erst in der nächsten Saison voll |
| Bringt der Blog Buchungen? | 6–12 Monate | Reisebuchungen haben lange Entscheidungswege, und viele Buchungen laufen über mehrere Besuche |

**Wichtig bei saisonalen Artikeln:** „Ägypten im Winter“ oder „Osterferien 2027“ verlieren nach der Saison Traffic. Das ist kein Misserfolg. Bewertet wird im Vergleich zur selben Saison im Folgejahr.

## 6. Monatlicher Bericht (Vorlage, 1 Seite)

```
Blog-Monatsbericht <Monat> · erstellt am <Datum>

1. Überblick (GSC, Blogkategorien)
   Klicks | Impressionen | CTR | Veränderung zum Vormonat
2. Indexierung: veröffentlicht X | indexiert Y | Probleme: …
3. Top 5 Artikel nach Klicks (mit Fokus-Keyword, Position)
4. Aufsteiger: Suchanfragen mit Positionen 8–20 (schnelle Verbesserung möglich)
5. Absteiger / Kannibalisierung: Suchanfragen, für die 2+ URLs ranken
6. Conversion: WhatsApp-Klicks | Buchen-Klicks | Anfragen lt. Strichliste | Buchungen
7. Entscheidungen für den nächsten Monat (siehe Abschnitt 7)
```

## 7. Methode für die monatliche Anpassung der Themenplanung

Am ersten Montag jedes Monats nimmt sich die Redaktion etwa 60 Minuten Zeit:

1. **Aufsteiger ausbauen:** Suchanfragen auf Position 8–20 mit mindestens zweistelligen Impressionen bekommen einen eigenen Abschnitt oder eine FAQ im bestehenden Artikel. Der Title wird geschärft.
2. **Neue Fragen aufgreifen:** Suchanfragen, für die ein Artikel rankt, die er aber nicht beantwortet, kommen auf die Themenliste. Hat die Frage eine eigene Suchintention, wird ein eigener Artikel daraus, sonst eine Ergänzung.
3. **CTR-Probleme beheben:** Artikel mit vielen Impressionen und einer CTR unter dem Durchschnitt der eigenen Blogartikel bekommen einen neuen Title und eine neue Meta-Description. Die Änderung wird dokumentiert und nach 4 Wochen verglichen.
4. **Kannibalisierung auflösen:** Ranken zwei URLs abwechselnd für dieselbe Suchanfrage, legen wir eine Haupt-URL fest. Die andere wird geschärft oder per 301 zusammengeführt.
5. **Cluster gewichten:** Im Cluster mit dem besten Verhältnis aus Anfragen pro Besucher wird der nächste Monat stärker besetzt.
6. **Nichts tun bei unter 8 Wochen alten Artikeln.** Sie werden noch nicht bewertet.

Die Entscheidungen werden im Redaktionsplan (CSV, Spalte „Status“) und als neue Zeilen für Folgeartikel festgehalten.

## 8. Automatisierbar

- GSC-Export per Search-Console-API in ein Google Sheet (wöchentlich), daraus erzeugt ein Skript den Monatsbericht
- Prüfung der Indexierung über die URL-Inspection-API
- Monatliche Prüfung, ob sich die Einreiseseiten des Auswärtigen Amts geändert haben, mit Hinweis an die Redaktion
- Liste der Aufsteiger-Keywords (Position 8–20) automatisch erstellen

Voraussetzung: ein Dienstkonto bzw. eine API-Freigabe für die Search Console. Dafür brauche ich deine Zustimmung.
