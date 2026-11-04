# Testprotokoll: Flyer „TUI MAGIC LIFE Redsina Sharm el Sheikh“, 04.11.2026

Durchgeführt nach `docs/Testplan-Flyerangebot.md`, Abschnitte 1 bis 4.

**Rahmen:**
- 7 Seitenaufrufe über haydiweg.de/buchen/, jeweils im Abstand von mindestens 60 Sekunden, zwischen 00:45 und 00:54 Uhr UTC
- keine Buchung, „zur Buchung“ wurde nie geklickt
- keine direkten Aufrufe interner Schnittstellen
- keine Änderungen an der Website

Der Flyer selbst ist **nicht** im Repository abgelegt, weil die Rechte an Bild und Logo von TUI ungeklärt sind.

## 1. Soll-Werte laut Flyer (manuell erfasst)

| Feld | Flyer |
|---|---|
| Veranstalter | TUI |
| Hotel | TUI MAGIC LIFE Redsina Sharm el Sheikh, Nabq, Ägypten |
| Termin | „z. B. am 09.12.2026“, 7 Nächte, also Rückreise 16.12.2026 |
| Abflughafen | Düsseldorf (DUS) |
| Zimmer und Verpflegung | Doppelzimmer, All Inclusive |
| Preis | „pro Person ab € 699“, „bis zu 41 % sparen“ |
| Belegung | **nicht angegeben**; für den Test angenommen: 2 Erwachsene (Doppelzimmer) |
| Preisstand, Gültigkeit, Bedingungen, Transfer | **nicht angegeben** |

Die KI-Extraktion aus dem Flyer (T1) ist **nicht getestet**, weil der Baustein noch nicht existiert. Die Werte oben habe ich von Hand abgelesen.

## 2. Zuordnung zur IBE (T2)

| Schritt | Ergebnis |
|---|---|
| Hotelsuche über das Feld „Wohin soll es gehen?“, Eingabe „Redsina“ | Genau ein Treffer: „TUI MAGIC LIFE Redsina Sharm El Sheikh – Sharm el Sheikh – Nabq Bay, Ägypten“ ✅ |
| Hotelnummer | Nach Auswahl des Treffers erscheint in der URL **`aid=25710`** ✅ |
| Veranstaltercode | Aus der Veranstalterliste der IBE: `TUID` = „TUI Deutschland“, außerdem `XTUI` = „TUI XTUI“ ✅ |

Dafür waren 3 Seitenaufrufe nötig. Beim dritten habe ich versehentlich „Merkzettel anzeigen“ geklickt; das ist nur eine Anzeige, es wurden keine Daten gespeichert.

## 3. Link-Tests (T3/T4), jeweils 2 Erwachsene, 7 Nächte, ab DUS

| Test | Link-Parameter | Ergebnis in der IBE |
|---|---|---|
| **L2**, ohne Veranstalter, exakter Termin | `aid=25710&ddate=2026-12-09&rdate=2026-12-16&dur=7&depap=DUS&adult=2&talloc=2-` | Mi 09.12. bis Mi 16.12.26, **Family Room Garden View (Familienzimmer)**, All Inclusive, inkl. Transfer und Zug zum Flug. DUS 11:30 → SSH 17:10 und zurück 18:10 → 22:25, direkt. Veranstalter `TUID`. **1.952,00 € gesamt, 976 € p. P.** Verfügbarkeitsprüfung: `AVAILABLE`. |
| **L1**, mit `brand=TUID`, 1. Versuch | wie L2 plus `&brand=TUID` | ❌ **IBE-Fläche blieb leer.** Die IBE sprang auf ihre Startseite (`/`), es gab keine Angebotssuche. Ein Kunde hätte eine leere Seite gesehen. |
| **L3**, ohne Veranstalter, Zeitraum ±7 Tage | `ddate=2026-12-02&rdate=2026-12-23`, sonst wie L2 | Günstigstes Angebot So 13.12. bis So 20.12.26, **Double Room Pool View (Doppelzimmer)**, All Inclusive, `TUID`. **1.854,00 € gesamt, 927 € p. P.** Im Preiskalender (gesamt für 2 Personen): 07.12. 2.281 €, **08.12. 1.719 €**, 09.12. ohne Wert, 10.12. 1.748 €, 11.12. 2.319 €, 12.12. 1.854 €. |
| **L1**, 2. Versuch, identische URL | wie L1 | ✅ Lädt diesmal normal. Mi 09.12. bis Mi 16.12.26, **Family Room Pool View (Familienzimmer)**, All Inclusive, „Gewählter Veranstalter“ `TUID`. **2.022,00 € gesamt, 1.011 € p. P.** `AVAILABLE`. |

## 4. Abgleich Flyer und IBE

| Prüfpunkt | Flyer | IBE (beste Übereinstimmung, L2) | ok? |
|---|---|---|---|
| Hotel | Magic Life Redsina | Magic Life Redsina (`aid=25710`) | ✅ |
| Veranstalter | TUI | TUID (TUI Deutschland) | ✅ |
| Termin | 09.12. bis 16.12.2026 | 09.12. bis 16.12.2026 | ✅ |
| Nächte | 7 | 7 | ✅ |
| Abflughafen | Düsseldorf | Düsseldorf (Hin- und Rückflug) | ✅ |
| Personen | nicht angegeben | 2 (976 € × 2 = 1.952 €) | ⚪ nicht prüfbar |
| Zimmer | Doppelzimmer | **Familienzimmer**; an diesem Termin wurde kein Doppelzimmer angezeigt | ❌ |
| Verpflegung | All Inclusive | All Inclusive | ✅ |
| Preis p. P. | ab 699 € | **976 €**, mit `brand` 1.011 €. Günstigster gefundener Wert im Fenster 2. bis 23.12.: etwa 860 € (08.12.) | ❌ **+40 %** am Flyertermin |

## 5. Bewertung

1. **Hotel, Termin, Dauer, Abflughafen, Veranstalter und Verpflegung** lassen sich für dieses reale Flyerangebot verlinken und werden übernommen.
2. **Die genaue Reise laut Flyer ist nicht erreichbar.** Am 09.12. zeigt die IBE kein Doppelzimmer, und der Flyerpreis von 699 € p. P. erscheint nirgends im geprüften Zeitraum. Warum, ist **nicht feststellbar**. Mögliche Gründe:
   - Der Flyerpreis ist veraltet; ein Preisstand fehlt auf dem Flyer.
   - Es handelt sich um einen Aktions- oder Kontingentpreis, der nicht in der IBE liegt.
   - Es gelten andere Bedingungen.

   Keiner dieser Gründe ist belegt.
3. **`brand=TUID` liefert ein anderes Zimmer und einen höheren Preis** (1.011 € statt 976 €) als die Suche ohne Veranstaltervorgabe, obwohl auch diese bei `TUID` landete. Die Ursache ist unbekannt.
4. **Einer von 7 Aufrufen schlug fehl** (leere IBE). Dieselbe URL funktionierte 3 Minuten später. Die Ursache ist unbekannt. Es könnte eine vorübergehende Störung sein oder eine Reaktion des Bot-Schutzes auf den Headless-Browser; das ist nicht belegt. Folgen:
   - Eine automatische Prüfung würde solche Fehlschläge als „nicht verfügbar“ fehlinterpretieren, wenn sie nicht gezielt erkannt und wiederholt werden.
   - Ob echte Kunden das auch sehen können, ist nicht geprüft.

**Ergebnis nach Testplan Abschnitt 7:** **T4 nicht bestanden** (Zimmer und Preis stimmen nicht). Für dieses Angebot gilt deshalb: Es nicht als exaktes Einzelangebot mit 699 € bewerben. Stattdessen Hotel und Zeitraum verlinken und mit einem selbst in der IBE ermittelten Preis samt Preisstand werben, zum Beispiel „ab 927 € p. P. im DZ, Stand 04.11.2026“.
