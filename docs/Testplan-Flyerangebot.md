# Testplan: Ein reales Veranstalter-Flyerangebot Ende-zu-Ende prüfen

Status: **Entwurf, noch nicht durchgeführt.** In dieser Sitzung liegt noch **kein Veranstalter-Flyer** vor. Für den Start brauche ich einen Flyer als PDF oder Bild.

Ziel: Für **ein** reales Flyerangebot belegen, ob sich die Kette „Flyer → Daten → Link → richtige Reise in der IBE → Preisvergleich“ ohne Kontakt zu Schmetterling oder Amadeus und ohne Produktivänderung umsetzen lässt.

**Grenzen für alle Schritte:**
- keine Buchung und kein Betreten der Buchungsstrecke („zur Buchung“ wird nicht geklickt)
- keine direkten Aufrufe interner IBE-Schnittstellen
- keine Änderungen an haydiweg.de
- höchstens 10 einzelne Seitenaufrufe pro Testtag, mindestens 60 Sekunden Abstand

## 0. Voraussetzungen (vor dem Test zu klären, intern)

| Nr. | Voraussetzung | Wer | Status |
|---|---|---|---|
| V1 | Ein aktueller Veranstalter-Flyer mit einem konkreten Angebot | Mert | offen |
| V2 | Eigene Unterlagen sichten: Vertrag, AGB und Einrichtungsmail mit Schmetterling, Vertriebsvereinbarung mit dem Veranstalter. Gesucht sind Aussagen zu automatisierten Abfragen, API-Nutzung, Bild- und Textnutzung und zur Werbung mit Veranstalterpreisen. | Mert (ohne externen Kontakt) | offen |
| V3 | Klären, ob Inhalte aus Veranstalter-Flyern (Texte, Bilder, Preise) von euch neu veröffentlicht werden dürfen | Mert, ggf. eigene Rechtsberatung | offen |
| V4 | Kanal für die Veröffentlichung festlegen (Website, Instagram, WhatsApp, Druck) | Mert | offen |

## 1. Flyerdaten erfassen (Soll-Werte)

Pro Angebot werden diese Felder aus dem Flyer übernommen. Zuerst trägt ein Mensch die Werte von Hand ein (Referenz), anschließend extrahiert die KI dieselben Felder, und beides wird verglichen.

| Feld | Beispielinhalt | Pflicht |
|---|---|---|
| Veranstalter | z. B. „ANEX Tour“ | ja |
| Hotelname, Ort, Ziel | | ja |
| Reisezeitraum bzw. konkreter Termin | | ja |
| Dauer in Nächten | | ja |
| Abflughafen bzw. Abflughäfen | | ja |
| Belegung (Erwachsene, Kinder mit Alter) | | ja |
| Zimmerart | | ja |
| Verpflegung | | ja |
| Preis p. P. und/oder Gesamtpreis, Preisart („ab“) | | ja |
| Preisstand, Gültigkeit, Bedingungen (z. B. Frühbucher, Kontingent) | | ja |
| Transfer, Rail & Fly | | optional |

**Abnahme T1:** Alle Pflichtfelder der KI-Extraktion stimmen mit der manuellen Erfassung überein. Jede Abweichung wird protokolliert.

## 2. Hotel und Veranstalter der IBE zuordnen

| Schritt | Vorgehen | Abnahme |
|---|---|---|
| T2.1 | Hotel in der normalen IBE auf haydiweg.de/buchen/ von Hand suchen und die `aid` aus der Adresszeile notieren | IBE zeigt denselben Hotelnamen und Ort wie der Flyer |
| T2.2 | Veranstaltercode notieren (z. B. ANEX); er steht im Veranstalterfilter der IBE | Code passt zum Veranstalter auf dem Flyer |

Hinweis: Eine **automatische** Zuordnung von Flyer-Hotel zu `aid` ist bisher nicht vorhanden und nicht getestet. Ohne Zugriff auf interne Schnittstellen bleibt sie vorerst ein Handgriff von etwa 1 Minute pro Hotel. Bereits zugeordnete Hotels werden in einer Tabelle gespeichert und wiederverwendet.

## 3. Link erzeugen

`tools/ibe-deeplink.js` wird mit den Soll-Werten aufgerufen, und zwar in drei Varianten:

- **L1:** mit Veranstalter (`brand`), exaktem Termin und exakter Dauer
- **L2:** ohne Veranstalter, exakter Termin
- **L3:** ohne Veranstalter, Zeitraum von ±7 Tagen um den Flyertermin

## 4. Link öffnen und abgleichen (Kerntest)

Jeder Link wird **einmal** geöffnet, entweder von einem Menschen im Browser oder als einzelner Headless-Aufruf.

| Prüfpunkt | Soll (Flyer) | Ist (IBE) | ok? |
|---|---|---|---|
| Hotel | | | |
| Veranstalter | | | |
| Hin- und Rücktermin | | | |
| Nächte | | | |
| Abflughafen (Hin- und Rückflug) | | | |
| Personen (Preis p. P. × Personen = Gesamtpreis) | | | |
| Zimmerart | | | |
| Verpflegung | | | |
| Gesamtpreis | | | |
| Abweichung in € und % | | | |

**Abnahme T4:**
- Hotel, Termin, Nächte, Abflughafen und Personenzahl stimmen bei L1 überein.
- Der Preis weicht höchstens um die vorher festgelegte Toleranz ab (Vorschlag: ±5 %).
- Weichen Zimmer oder Verpflegung ab, gilt das als „**nicht korrekte Reise**“.

## 5. Ergänzende Prüfungen (schließen die bisherigen Testlücken)

| Nr. | Test | Zweck |
|---|---|---|
| T5.1 | Gleicher Link, Kinderalter 2 / 8 / 14 | Wirkt das Kinderalter auf den Preis? |
| T5.2 | 2 Erwachsene + 2 Kinder | Funktionieren mehrere Kinder? |
| T5.3 | Zwei Abflughäfen (z. B. `PAD,HAJ`) | Werden mehrere Abflughäfen akzeptiert? |
| T5.4 | Mit und ohne `brand`, wenn ein anderer Veranstalter günstiger wäre | Legt `brand` den Veranstalter wirklich fest? |
| T5.5 | Termin ohne Angebot (z. B. ausgebucht oder außerhalb der Saison) | Wie sieht „nicht verfügbar“ aus? Das ist Voraussetzung für jede spätere Prüfung. |
| T5.6 | Zimmer- bzw. Verpflegungsfilter (`rcode`, Board) | Lässt sich das Zimmer aus dem Flyer festlegen? |
| T5.7 | Link als QR-Code auf dem Smartphone | Funktioniert der Weg mobil und mit Cookie-Banner? |
| T5.8 | Flyer-UTM in Google Analytics von haydiweg.de | Lässt sich der Erfolg pro Flyer messen? |

## 6. Preisverlauf messen (manuell, ohne Automatik)

Ein Mitarbeiter öffnet denselben L1-Link 4-mal am Tag (z. B. 6, 12, 18 und 24 Uhr) an **3 aufeinanderfolgenden Tagen** im eigenen Browser und trägt Preis und Verfügbarkeit ein.

So zeigt sich, wie stark und wie oft sich Preise tatsächlich ändern. Daraus folgt, ob eine Prüfung alle 6 Stunden überhaupt nötig ist oder ob eine tägliche Prüfung reicht.

## 7. Ergebnisbewertung

| Ergebnis | Folge |
|---|---|
| T4 bestanden und V2/V3 positiv geklärt | Pilot mit 8 Angeboten pro Tag. Die Preisprüfung bleibt manuell oder halbautomatisch, bis die Erlaubnis für eine Automatik belegt ist. |
| T4 bestanden, V2/V3 ungeklärt | Flyer nur mit eigenen Texten und Bildern und mit „ab“-Preis samt Preisstand. Keine Automatik. |
| T4 nicht bestanden (falsche Reise) | Flyerangebote nicht als Einzelangebot verlinken, sondern als Hotel mit Zeitraum, mit dem Hinweis „Preis tagesaktuell“. |

## Protokoll

Für jeden Testschritt werden Datum und Uhrzeit, der Link, ein Screenshot und das Ergebnis in `docs/belege/` abgelegt.
