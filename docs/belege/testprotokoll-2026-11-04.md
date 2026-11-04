# Testprotokoll Deeplink-Tests vom 04.11.2026

**Methode:** Jeder Test war genau ein Seitenaufruf in Headless-Chromium mit Viewport 1366×900 und Locale de-DE. Nach dem Laden habe ich 25 Sekunden gewartet und dann den sichtbaren Text, die iFrame-URL und die Antworten gesichert, die der Browser ohnehin geladen hat. Ich habe nichts angeklickt, kein Formular abgeschickt und die Buchungsstrecke nicht betreten.

Testhotel: Quattro Family Club Dem Hotel, `aid=156021`.

Dieses Protokoll enthält nur Auszüge. Die vollständigen Rohdateien lagen im temporären Arbeitsverzeichnis der Sitzung und sind nicht dauerhaft gesichert. Hoteltexte (© GIATA) habe ich bewusst nicht übernommen.

## Test 1 – 00:26 Uhr (UTC)

**Aufruf:**
`https://haydiweg.de/buchen/?aid=156021&ddate=2027-06-01&rdate=2027-06-30&dur=7&depap=PAD&talloc=2-8&adult=2&child=8`

**iFrame-URL, vom Loader erzeugt:**
`https://pauschalreise.schmetterling.de/search/offer?aid=156021&taid=46850&dur=7&depap=PAD&ibe=package&ddate=2027-06-01&rdate=2027-06-30&talloc=2-8&srtReg=15&srtHot=5&adult=2&child=8&utm_campaign=suchmaske&utm_medium=website&utm_source=haydiweg`

**Angezeigtes Angebot (Auszug):**
```
Bester Familienpreis inkl. Kinderrabatt
Günstigstes Angebot aus 55 Veranstaltern
8 Tage, 7 Übernachtungen
Mo. 14.06.27 - Mo. 21.06.27
FZ Landblick Hauptgebäude / Familienzimmer
All Inclusive Plus, ohne Hoteltransfer
Hinflug:  01:55 Paderborn-Lippstadt → 06:25 Antalya, direkt
Rückflug: 23:35 Antalya → 02:25 Paderborn-Lippstadt, direkt
Gesamtpreis 1.992,00 €   |   ⌀ Preis pro Person 664,00 €
```

**Verfügbarkeitsprüfung, von der IBE selbst ausgelöst:**
- `status AVAILABLE`, `bookable: true`
- Meldung „712 Buchung möglich, bitte AKTION "B" verwenden“
- Veranstalter `ANEX`
- Reisezeitraum `startDate 2027-06-14`, `endDate 2027-06-21`
- Flughäfen `PAD` / `AYT`

**Screenshot:** `test1-deeplink.png`. Er zeigt Hotel, Termin, Dauer und Preis. Abflughafen und Belegung sind darauf **nicht** sichtbar; sie stehen nur im Textauszug oben.

## Test 2 – 00:27 Uhr (UTC)

**Aufruf:**
`…/buchen/?aid=156021&ddate=2027-06-14&rdate=2027-06-21&dur=7&depap=PAD&talloc=2-8&brand=ANEX`

Der Parameter `child` fehlte absichtlich.

**iFrame-URL:**
`…/search/offer?aid=156021&taid=46850&brand=ANEX&dur=7&depap=PAD&ibe=package&ddate=2027-06-14&rdate=2027-06-21&talloc=2-8&srtReg=15&srtHot=5&adult=2&utm_…`

Die IBE ergänzte `adult=2`, aber **kein** `child`.

**Angezeigtes Angebot (Auszug):**
```
Bester Preis – Günstigstes Angebot des Veranstalters
8 Tage, 7 Übernachtungen, Mo. 14.06.27 - Mo. 21.06.27
Doppelz. Nur für Männer (ROH) / Doppelzimmer
All Inclusive Plus, Flüge wie Test 1
Gewählter Veranstalter
Gesamtpreis 1.716,00 €   |   Preis pro Person 858 €
```

**Verfügbarkeitsprüfung:** `AVAILABLE`, Veranstalter `ANEX`, `2027-06-14` bis `2027-06-21`, `PAD` / `AYT`.

## Test 3 – 00:29 Uhr (UTC)

**Aufruf:** Ausgabe von `node tools/ibe-deeplink.js`, also Test 1 plus `utm_source=flyer&utm_medium=print&utm_campaign=flyer-2026-11-04-01`.

**iFrame-URL:** wie Test 1. Die Flyer-UTMs wurden vom Loader wie vorgesehen nicht weitergereicht.

**Angezeigtes Angebot (Auszug):**
```
Bester Familienpreis inkl. Kinderrabatt
Günstigstes Angebot aus 55 Veranstaltern
8 Tage, 7 Übernachtungen, Mo. 14.06.27 - Mo. 21.06.27
Doppelzimmer Run of House / Doppelzimmer      <-- anderes Zimmer als in Test 1
All Inclusive Plus, Flüge wie Test 1
Gesamtpreis 1.992,00 €   |   ⌀ Preis pro Person 664,00 €
```

**Verfügbarkeitsprüfung:** `AVAILABLE`, Veranstalter `ANEX`, gleicher Termin, `PAD` / `AYT`.

## Auswertung

| Merkmal | Beleg | Bewertung |
|---|---|---|
| Hotel (`aid`) | Test 1–3, Name im Seitentext | **bestätigt** |
| Zeitraum (`ddate`/`rdate`) und Dauer (`dur=7`) | Termin liegt im Fenster, „7 Übernachtungen“ | **bestätigt** |
| Abflughafen (`depap=PAD`) | Seitentext und Verfügbarkeitsprüfung `PAD` | **bestätigt** |
| Personenzahl mit `child` | 664 € × 3 = 1.992 €, Hinweis „Familienpreis inkl. Kinderrabatt“ | **indirekt bestätigt**: 3 Personen, davon mindestens 1 Kind. Die IBE nennt die Belegung nicht im Klartext. |
| Kinderalter 8 wird preislich berücksichtigt | – | **nicht geprüft**. Ein Vergleich mit anderem Alter fehlt. |
| Ohne `child` fällt das Kind weg | Test 2: 858 € × 2 = 1.716 €, „Doppelz.“ | **bestätigt** |
| `brand=ANEX` legt den Veranstalter fest | Test 2 zeigt „Gewählter Veranstalter“ | **nicht aussagekräftig**: Auch ohne `brand` war ANEX der günstigste Veranstalter. |
| Exaktes Datum wird übernommen | Test 2 | **nicht aussagekräftig**: Derselbe Termin war ohnehin der günstigste. |
| Gleiches Angebot bei erneutem Aufruf | Test 1 und Test 3 im Abstand von etwa 3 Minuten | **nur teilweise**: Preis, Termin und Flüge waren gleich, das **Zimmer war verschieden**. |
| Generator erzeugt funktionierenden Link | Test 3 | **bestätigt** für genau diese Kombination (2 Erw. + 1 Kind, 1 Abflughafen, `dur` fest). |
