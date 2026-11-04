# IBE-Prüfung haydiweg.de/buchen/ – Bericht

> **Korrekturhinweis (Nachprüfung):** Nach erneuter Durchsicht der Rohdaten habe ich folgende Aussagen korrigiert. (1) Test 3 war **nicht identisch** mit Test 1: Preis, Termin und Flüge waren gleich, das Zimmer war ein anderes. (2) Der Abstand zwischen Test 1 und Test 3 betrug etwa **3 Minuten**, nicht 10. (3) `brand` und das exakte Datum wurden zwar übernommen, ihre Wirkung ist damit aber nicht belegt, weil ANEX und der 14.06. auch ohne diese Vorgaben das Ergebnis waren. (4) Die Belegung ist nur **indirekt** belegt (Preis pro Person × 3 = Gesamtpreis); das Kinderalter wurde nicht geprüft. Einzelheiten stehen in `docs/belege/testprotokoll-2026-11-04.md`.

Stand: 04.11.2026 · Methode: ausschließlich lesende Abrufe der öffentlich ausgelieferten Seiten und Skripte, dazu drei einzelne Seitenaufrufe des Testangebots in einem Headless-Browser (so wie ein Besucher). Ich habe keine Buchungsschritte geklickt, keine Formulare abgeschickt, keine Daten verändert, keine Schutzmaßnahmen umgangen und kein externes Unternehmen kontaktiert.

---

## 1. Ausgangslage und Zugang

| Punkt | Befund |
|---|---|
| Dieses Repository (`strato-ki-backend`) | Enthält **keinen WordPress-Code**. Es ist ein Express- und OpenAI-Wrapper (`api/index.js`), der Airline-Belege per KI ausliest. |
| WordPress-Backend, Theme, Elementor-Daten | **Kein Zugang.** Untersucht habe ich nur das ausgelieferte HTML. |
| Website-Technik | WordPress mit Elementor 4.3.6, WP Rocket 3.24 und ElementsKit; Cookie-Banner von CookieYes. |
| Verträge, Einrichtungsmail von Schmetterling, IBE-Dokumentation | **Lagen nicht vor.** Der Code verweist auf eine „Einrichtungsmail von Schmetterling“. |

## 2. Eingesetzte Buchungsmaschine

| Merkmal | Nachweis |
|---|---|
| Produkt | **Amadeus Leisure IBE („ALIBE“)**. Ausprägung vermutlich *Advanced*; das schließe ich nur aus dem Parameternamen `mandator=man-advanced`. Belege: `<app-root-alibe>`, Marker „AMADEUS-IBE“, Fonts `amadeus-ibe-icons`, API-Parameter `mandator=man-advanced`. |
| Betreiber, Mandant | Schmetterling, über `/api/config`: `customer=schmetterling`, `mandator=alibe`, `kid=890002`, `giataUser=944412`, `environment=prd`. |
| Hosts | `pauschalreise.schmetterling.de` (Pauschalreise) und `eigenanreise.schmetterling.de` (nur Hotel). |
| Agenturkennung | `taid=46850`, im Loader fest gesetzt. |
| Infrastruktur | Inhalte von Traveltainment (`*.images.traveltainment.eu`, `eum.traveltainment.de`), Hotelinhalte von GIATA, CDN und WAF von Imperva/Incapsula. |
| Frontend-Version | Angular **21.2.25**, Bundle `main.c3a4a0da0d054a91.js`, Bootstrap 4.6.0. Eine eigene Produktversionsnummer der IBE wird **nicht ausgeliefert**. Die Hash-Dateinamen ändern sich mit jedem Release. |
| iFrame zulässig? | Ja. Der CSP-Header der IBE erlaubt `frame-ancestors 'self' https:`. |

### Einbindung auf /buchen/ (Elementor-HTML-Widget)
* Leeres `<iframe id="hw-ibe-frame">`. Das Skript `hw-ibe-loader` setzt die `src`.
* Fast alle Query-Parameter von `haydiweg.de/buchen/?…` werden **1:1 an die IBE durchgereicht**. Ausgenommen sind `utm_*`, `gclid`, `fbclid` und Ähnliche.
* `taid`, `srtReg` und `srtHot` sowie die UTM-Werte überschreibt der Loader **immer**. Agenturkennung und Sortierung lassen sich über die Adresszeile also nicht manipulieren.
* Der Loader wählt die Seite der IBE so:
  * mit `aid` → `/search/offer` (Hotel mit Angeboten),
  * mit `rid` oder `cyid` → `/search/hotel`,
  * sonst → `/search/region`.
* Mit `ibe=hotel` wechselt der Loader auf den Eigenanreise-Host.
* Höhe und Scrollen werden per `postMessage` abgestimmt: `iberesized`, `scroll`, `parent-scroll`, `parent-resize`. Nachrichten anderer Herkunft werden ignoriert. Die Umsetzung ist sauber.

### Auffälligkeiten im Website-Code (ohne Änderung, nur zur Info)
1. **Widerspruch bei den Filtern.** Laut Loader-Kommentar sind `dfl` (nur Direktflug) und `trans` (mit Transfer) bewusst nicht gesetzt, „sonst fällt ein Teil der Angebote weg“. Die Suchmaske setzt aber fest `dfl=1` und `trans=1`. Wer über die Suchmaske sucht, sieht deshalb vermutlich weniger Angebote. Das folgt aus dem Code und ist nicht getestet.
2. **Die Suchmaske umgeht die Buchungsseite.** Sie öffnet die IBE direkt in einem neuen Tab auf schmetterling.de und nicht über `haydiweg.de/buchen/`.
3. **Reisedauer prüfen.** Die Maske rechnet „1 Woche → `dur=6`“. Im Test ergab `dur=7` die Anzeige „8 Tage, 7 Übernachtungen“. „1 Woche“ in der Maske sucht demnach vermutlich Reisen mit 6 Nächten, nicht die übliche Woche mit 7 Nächten. Die Maske selbst habe ich nicht getestet.
4. Die meisten Ziele in der Suchmaske haben noch **keine `rid`**. Wer sie wählt, sucht ohne Einschränkung auf das Ziel. Die Konsole warnt bereits darauf hin.
5. `utm_campaign` setzt der Loader auf `suchmaske` (mit `ddate`) oder `buchungsseite`. Eigene Flyer-UTMs erscheinen deshalb nur im Analytics von haydiweg.de, **nicht in der IBE-Auswertung**.

## 3. Öffentliche Dokumentation (Recherche)

* Amadeus nennt auf der Produktseite nur, dass „spezielle Deep Links“ konfigurierbar sind und dass es eine iFrame-Variante gibt (*Starter*). Eine **öffentliche Parameter- oder API-Dokumentation existiert nicht**. Laut den Rahmenbedingungen der IBE steht sie in der „ausführlichen Dokumentation“ und ist über den Projektansprechpartner bei Amadeus erhältlich.
* Die Amadeus Leisure Platform bietet laut Amadeus APIs an. Das Angebot richtet sich an Veranstalter und Vertriebspartner mit eigenem Vertrag. Es gibt keinen Self-Service-Zugang und kein öffentliches Entwicklerportal für den deutschen Pauschalreisemarkt.
* Die öffentlichen Amadeus-Self-Service-APIs (Flug und Hotel) decken **keine Pauschalreisen** ab und helfen hier nicht.
* Zu Schmetterling (Quadra, Neo, IBE) gibt es nur Fachpresse, keine öffentliche Deeplink- oder API-Dokumentation.
* Die Parameterbedeutung habe ich deshalb aus dem **öffentlich ausgelieferten Frontend-Code** der IBE abgelesen. Dort steht eine Zuordnung von internen Feldern zu URL-Parametern:
  * `aid` (IFF-Hotelcode, alter Name „IFF“), `ddate`, `rdate`, `dur`, `depap`
  * `adult`, `child`, `talloc`, `brand` (Veranstalter), `rid`, `cyid`, `rgid`, `nid`
  * `dfl`, `destap`, `fops` (Airline), `rcode` (Zimmercode), `sea`, `raf`, `cancel`, `stars`, `ibe`, `noheader`
  * Dazu kommen ältere Aliasnamen: `termin`, `ruecktermin`, `abflughafen`, `IFF`, `dauer`, `marke`, `sleistung`.

  Das ist **keine zugesicherte Schnittstelle**. Amadeus kann sie mit jedem Release ändern.

## 4. Praxistest Angebots-Deeplink

Testhotel: *Quattro Family Club Dem* (`aid=156021`, GIATA 419100). Ich habe drei Einzelaufrufe gemacht, nur angesehen und nicht geklickt.

| Test | URL-Parameter (an haydiweg.de/buchen/) | Ergebnis |
|---|---|---|
| 1 | `aid=156021&ddate=2027-06-01&rdate=2027-06-30&dur=7&depap=PAD&talloc=2-8&adult=2&child=8` | ✅ Hotel korrekt. Zeitraum korrekt; der günstigste Termin Mo 14.06. bis Mo 21.06.27 wurde vorgewählt. ✅ „8 Tage, 7 Übernachtungen“. ✅ Hin- und Rückflug Paderborn-Lippstadt ↔ Antalya, direkt. ✅ „Bester Familienpreis inkl. Kinderrabatt“, Familienzimmer, All Inclusive Plus. **Gesamtpreis 1.992,00 €** (664 € p. P. × 3 Personen), günstigstes von 55 Veranstaltern (ANEX). Die IBE meldete automatisch eine Verfügbarkeitsprüfung „AVAILABLE / bookable“. ⚠️ Die Belegung ist nur indirekt über den Preis belegt; das Kinderalter wurde nicht geprüft. |
| 2 | wie 1, aber exakter Termin `ddate=2027-06-14&rdate=2027-06-21`, `brand=ANEX`, **ohne `child`** | ⚪ Exakter Termin und Veranstalter ANEX wurden übernommen. Das ist **nicht aussagekräftig**, weil Test 1 ohne diese Vorgaben zum selben Ergebnis kam. ❌ **Das Kind wurde nicht übernommen** (nur 2 Erwachsene, Zimmer „Doppelz. Nur für Männer“, 1.716 €). Daraus folgt: `talloc` allein reicht nicht, `child` ist Pflicht. |
| 3 | Link aus `tools/ibe-deeplink.js` (wie Test 1 plus Flyer-UTM) | ✅ Gleicher Preis (1.992,00 €), gleicher Termin, gleiche Flüge, etwa 3 Minuten nach Test 1. ⚠️ **Anderes Zimmer** („Doppelzimmer Run of House“ statt „FZ Landblick Hauptgebäude“). Dieselbe URL liefert also nicht zwingend exakt dasselbe Angebot. |

Fazit: Ein direkter Angebotslink, der Hotel, Reisedatum, Abflughafen und Belegung übernimmt, **funktioniert über die eigene Domain** und mit der eigenen Agenturkennung. Bedingung: `adult` und `child` werden immer mitgesetzt. Den Generator dafür habe ich in `tools/ibe-deeplink.js` angelegt; er greift nicht aufs Netz zu.

Nicht geprüft habe ich, ob ein **einzelnes, eingefrorenes Angebot** (`offerId` bzw. `/book?availableOffer=…`) dauerhaft verlinkbar ist. Die `offerId` ist ein langer, verschlüsselter Token, der sehr wahrscheinlich nur in einer Sitzung oder für kurze Zeit gilt. Ein Test hätte bedeutet, die Buchungsstrecke zu betreten; das habe ich unterlassen.

## 5. Automatisierte Preis- und Verfügbarkeitsabfrage

* **Dokumentierte Möglichkeit: keine gefunden.** Mit dem vorhandenen Zugang ist keine API freigegeben, und es gibt keine Zugangsdaten und keine Dokumentation.
* **Technisch beobachtet:** Die IBE holt ihre Preise über eine interne JSON-Schnittstelle, unter anderem:
  * `POST /api/search/offers/list`, `…/offers/departuredate`, `…/offers/duration`
  * `POST /api/book/availabilitycheck`

  Diese Schnittstelle ist **undokumentiert**, nur für das eigene Frontend gedacht und durch Imperva-Bot-Schutz abgesichert. Eine Nutzung durch eigene Skripte wäre **nicht autorisiert**. Ich habe sie deshalb bewusst **nicht direkt angesprochen** und nur mitgelesen, was der Browser beim normalen Seitenaufruf ohnehin abruft.
* **Alternative „Headless-Browser lädt den öffentlichen Deeplink und liest den angezeigten Preis“:** Das funktioniert technisch, wie die Tests zeigen. Es ist aber trotzdem automatisierter Zugriff auf ein Fremdsystem. Ob die Vertragsbedingungen mit Schmetterling und Amadeus das erlauben, ist **ungeklärt**.

### Eignung für eine Prüfung alle 6 Stunden
Annahme: 8 neue Flyer pro Tag, jeder etwa 14 Tage aktiv. Dann laufen rund 110 Angebote gleichzeitig. Bei 4 Prüfungen am Tag sind das etwa **450 Seitenaufrufe pro Tag**. Jeder Aufruf löst rund 10 bis 12 Anfragen an das IBE-Backend aus, darunter eine **echte Verfügbarkeitsanfrage beim Veranstalter** (`availabilitycheck`).

Diese Last erzeugt Kosten beim Betreiber und verschlechtert das Verhältnis von Suchen zu Buchungen („Look-to-Book“). Außerdem besteht das Risiko, dass der Imperva-Schutz die Zugriffe sperrt. Das ist eine Einschätzung, getestet habe ich es nicht. Das kann im schlimmsten Fall auch echte Kunden an der gemeinsamen IP treffen. Eine 6-stündliche Vollautomatik ist daher **nicht ohne Freigabe** zu empfehlen.

### Bildrechte
* Die Hotelbilder und -texte in der IBE stammen von GIATA bzw. den Veranstaltern; die Texte tragen den Vermerk „© GIATA GmbH 1996 – 2026“.
* Ob ihr diese Bilder auf **gedruckten oder digitalen Flyern** nutzen dürft, geht aus den vorliegenden Unterlagen **nicht hervor**. **Ungeklärt.**
* Ebenso **ungeklärt** sind die Rechte an den Bildern auf haydiweg.de selbst (Uploads 2024/06 und andere), weil Herkunft und Lizenz nicht dokumentiert sind.

---

## 6. Ergebnis in drei Kategorien

### ✅ Nachweislich funktionsfähig
* IBE-Einbindung per iFrame auf `/buchen/` mit fester Agenturkennung `taid=46850`, Höhenanpassung und Scroll-Abstimmung.
* Angebots-Deeplink über `haydiweg.de/buchen/?aid=…&ddate=…&rdate=…&dur=…&depap=…&adult=…&child=…&talloc=…`. Hotel, Zeitraum, Dauer und Abflughafen werden übernommen; die Personenzahl (3, davon mindestens 1 Kind) indirekt über den Preis. Getestet mit einem Hotel und einer Belegung, zweimal mit gleichem Preis.
* Die IBE zeigt beim Aufruf den aktuellen Gesamtpreis und prüft die Verfügbarkeit selbst. Der Kunde sieht also immer den tagesaktuellen Preis.
* Der Deeplink-Generator `tools/ibe-deeplink.js` erzeugt einen funktionierenden Link für die getestete Kombination.

### 🟡 Technisch möglich, aber noch nicht bestätigt
* Automatisches Auslesen des angezeigten Preises per Headless-Browser über den öffentlichen Deeplink. Technisch belegt, **Erlaubnis ungeklärt**.
* Wirkung von `brand` (Veranstalter) und exaktem Termin: Die Werte werden übernommen, ihre Wirkung ist nicht belegt.
* Ob das Kinderalter korrekt in den Preis eingeht; mehrere Kinder, mehrere Abflughäfen, Dauerspannen.
* Dass dieselbe URL immer exakt dasselbe Angebot zeigt: Im Test wechselte das Zimmer.
* Festlegen von Zimmer und Verpflegung im Link (`rcode`, Board-Filter): Die Parameter existieren im Code, ich habe sie nicht getestet.
* Dauerhafte Links auf ein einzelnes, exaktes Angebot (`offerId`, `availableOffer`): Die Token sind wahrscheinlich kurzlebig. Ungetestet, weil dafür die Buchungsstrecke nötig wäre.
* Stabilität der Parameternamen über künftige IBE-Releases: Sie sind nur aus dem Code abgelesen und nicht vertraglich zugesichert.
* Nur-Hotel-Links (`ibe=hotel`): Der Weg ist im Loader angelegt, ich habe ihn nicht getestet.

### ⛔ Mit dem vorhandenen Zugang nicht umsetzbar oder nicht überprüfbar
* Eine **dokumentierte und autorisierte API** für Preis- und Verfügbarkeitsabfragen: Es liegen weder Zugangsdaten noch Dokumentation noch Vertragsklauseln vor. **API-Berechtigung ungeklärt.**
* Direkte Nutzung der internen `/api/search/…`- und `/api/book/…`-Endpunkte: nicht autorisiert, bot-geschützt, **bewusst nicht getestet**.
* Ein Testlauf der Buchungsstrecke: laut Auftrag ausgeschlossen.
* Prüfung von WordPress-Backend, Plugin-Konfiguration und Elementor-Rohdaten: kein Zugang.
* Exakte Produktversion der IBE: Sie wird nicht ausgeliefert. Nachweisbar ist nur die Frontend-Basis Angular 21.2.25 mit dem Build-Hash.
* **Bildrechte** für Flyer: ungeklärt.

---

## 7. Empfehlung: wirtschaftlichste sichere Umsetzung (8 Flyer pro Tag)

**Grundsatz:** Der Flyer verkauft einen **Zeitraum mit Ab-Preis**, nicht ein eingefrorenes Angebot. Der Link führt immer in die Live-Suche auf haydiweg.de, wo der Kunde den tagesaktuellen Preis sieht. Damit entfällt der Zwang, Preise ständig maschinell zu überwachen.

1. **Angebotsauswahl (Mitarbeiter, etwa 15 Minuten pro Tag).** In der normalen IBE werden 8 Angebote ausgewählt. Hotel-`aid`, Zeitraum, Abflughäfen, Belegung und gesehener Preis kommen in eine Tabelle oder ein Formular. Am besten wählt ihr einen Zeitraum von 2 bis 4 Wochen, damit ein Preis auch dann gültig bleibt, wenn ein einzelner Termin ausverkauft ist.
2. **KI-Texterstellung (bestehendes Backend erweitern).** Ein neuer Endpunkt im vorhandenen `strato-ki-backend` erzeugt aus den Angebotsdaten Flyer-Texte. Er nutzt das bereits verwendete Modell (`gpt-4o-mini`) und arbeitet nur mit eigenen Eingaben; die IBE wird dabei nicht abgefragt. Bei 8 Texten pro Tag liegen die Kosten im Cent-Bereich.
3. **Link und QR-Code.** `tools/ibe-deeplink.js` erzeugt den Link auf haydiweg.de/buchen/ (immer mit `adult` und `child`) samt eigener UTM-Kampagne pro Flyer. Daraus entsteht der QR-Code.
4. **Preisangabe rechtssicher gestalten.** Angeben: „ab X € p. P. / Gesamtpreis Y €“, Belegung, Abflughafen, Zeitraum und „Preis Stand TT.MM., HH:MM Uhr, tagesaktuell, Verfügbarkeit vorbehalten“. Die Pflichtangaben nach PAngV lasst bitte intern prüfen; das ist keine Rechtsberatung.
5. **Kontrolle der aktiven Flyer ohne Fremd-Automatik.** Ein interner Report listet täglich alle aktiven Flyer-Links. Ein Mitarbeiter öffnet sie stichprobenartig oder vollständig. Bei etwa 110 Links und rund 10 Sekunden pro Link sind das etwa 20 Minuten pro Tag. Weicht der Preis um mehr als einen festgelegten Wert ab (z. B. 10 %) oder ist kein Angebot mehr da, wird der Flyer manuell auf „inaktiv“ gesetzt.
6. **Automatische 6-Stunden-Prüfung erst nach Klärung.** Sie kommt erst in Frage, wenn aus euren **eigenen Unterlagen** (Vertrag, AGB oder Einrichtungsmail mit Schmetterling) hervorgeht, dass ihr eine API nutzen oder automatisiert abfragen dürft. Erst dann sollte ein Headless-Checker mit maximal 4 Durchläufen pro Tag gebaut werden, mit Drosselung (ein Aufruf alle 30 bis 60 Sekunden) und nur für aktive Flyer. Bis dahin: **nicht automatisieren**.
7. **Bilder.** Bis die Rechte geklärt sind, nur eigene Fotos oder ordentlich lizenzierte Stockbilder verwenden, keine aus der IBE übernehmen.

**Warum das am wirtschaftlichsten ist:** Ihr braucht keine API-Lizenz und keine Server-Infrastruktur für Scraping und tragt kein Sperr- oder Vertragsrisiko. Laufende Kosten entstehen nur für die KI-Texte (Cent-Bereich) und etwa 30 bis 40 Minuten Personalzeit pro Tag. Weil jeder Link in die Live-IBE führt, sieht der Kunde nie einen veralteten Preis im Buchungsprozess.

### Kurzfristige Korrekturen auf der Website (empfohlen, nicht durchgeführt)
* In der Suchmaske `dfl=1` und `trans=1` entfernen; das entspricht der Absicht im Loader-Kommentar.
* Die Umrechnung der Reisedauer in der Suchmaske prüfen (1 Woche = 7 Nächte → `dur=7`).
* Die fehlenden `rid`-Werte für die Ziele in der Suchmaske eintragen.
* Überlegen, ob die Suchmaske ebenfalls über `/buchen/` statt direkt auf schmetterling.de verlinken soll.

---
*Quellen der Recherche:*
* [Amadeus Leisure IBE](https://amadeus.com/de/reiseverkaufer/produkte/internet-booking-engine)
* [Amadeus Leisure IBE (EN)](https://amadeus.com/en/portfolio/retail-travel-agencies/leisure-ibe)
* [Amadeus Leisure Platform](https://amadeus.com/de/reiseverkaufer/produkte/leisure-platform-benelux)
* [touristik-aktuell: Schmetterling Homepage-Konzept](https://www.touristik-aktuell.de/reisevertrieb/schmetterling-homepage-konzept-fuer-reisebueros/)
* [touristik-aktuell: Schmetterling KI für die Website](https://www.touristik-aktuell.de/reisevertrieb/schmetterling-ki-fuer-die-website-booking-fuer-hotel-only/)
* Technische Belege: öffentlich ausgeliefertes HTML von haydiweg.de/buchen/ sowie HTML, JS-Bundle und HTTP-Header von pauschalreise.schmetterling.de, abgerufen am 04.11.2026.
