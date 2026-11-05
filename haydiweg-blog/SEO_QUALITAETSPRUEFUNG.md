# SEO-Qualitätsprüfung der Blog-Entwürfe

Stand: 05.11.2026 · Geprüft: 39 Entwürfe (36 im Plan, davon 3 Dubai-Artikel zurückgestellt, plus 3 Ersatzartikel R1–R3)

## 1. Ergebnis auf einen Blick

| Kennzahl | Wert |
|---|---|
| Entwürfe, die die automatische Prüfung bestanden haben | **39 / 39** |
| Wörter gesamt | 77.817 (1.559–2.609 je Artikel) |
| Textüberschneidungen zwischen Artikeln (Duplicate Content) | keine (Jaccard 6-Wort-Shingles ≤ 0,08) |
| Doppelte Fokus-Keywords | keine |
| Titel- oder Meta-Kollisionen mit den 89 bestehenden Seiten | keine (Abgleich gegen den Live-Stand vom 05.11.) |
| Titel über 580 px | keine (nach Korrektur) |
| Externe Quellen-URLs geprüft | 188, davon 183 erreichbar. 5 blockieren automatische Abrufe oder haben Zertifikatsfehler (gesetze-im-internet.de, hnms.gr, mira.gov.mv, dhmi.gov.tr, worldheritagesite.org). Diese bitte manuell im Browser prüfen |
| Offene `[PRÜFEN]`-Marker im Text | **125** |
| Redaktionelle Prüfpunkte im Frontmatter | 263 |
| Bildplätze mit Status MEDIENPRÜFUNG | 84 Platzhalter. 9 Beitragsbilder ohne eigenes Bild, 30 Beitragsbilder aus der Mediathek (Rechte trotzdem bestätigen, siehe 4.) |

**„Bestanden“ heißt: technisch und strukturell freigabefähig.** Kein Artikel ist ohne redaktionelle Endkontrolle veröffentlichungsreif. Die `[PRÜFEN]`-Marker und Bildplätze sind absichtlich sichtbar und müssen vor dem Planen aufgelöst werden.

Die Detailtabelle pro Artikel steht in `_arbeitsdaten/qa_ausgabe.txt`, die Rohdaten in `_arbeitsdaten/qa_ergebnis.json`.

## 2. Überprüfbare Qualitätskriterien

Jeder Artikel muss **alle** Muss-Kriterien erfüllen. Die automatisch prüfbaren laufen mit `python3 haydiweg-blog/_arbeitsdaten/qa_check.py --links`.

| # | Kriterium | Prüfung | Art |
|---|---|---|---|
| K1 | Thematische Relevanz: Der Artikel stützt eine Zielgebietsseite, ein Angebot oder eine Kernkompetenz | Redaktionsplan, Spalte „Begründung“ | Muss, manuell |
| K2 | Suchintention: Die Antwort steht im ersten Absatz, der Content-Typ passt zur Intention | Fokus-Keyword im Einstieg + Sichtprüfung | Muss, auto + manuell |
| K3 | SEO-Title ≤ 60 Zeichen **und** ≤ 580 px | `qa_check.py`, `seo_abgleich.py` | Muss, auto |
| K4 | Meta-Description 130–155 Zeichen, mit Nutzen und Keyword | `qa_check.py` | Muss, auto |
| K5 | Fokus-Keyword in H1, Einstieg, mindestens einer H2 und der Meta. Natürliche Variante erlaubt, mindestens 3 von 4 | `qa_check.py` | Muss, auto |
| K6 | 4–10 interne Links (Hubs bis 14), nur auf existierende oder geplante URLs | `qa_check.py` | Muss, auto |
| K7 | Kein Duplicate Content (Jaccard < 0,08), keine doppelten Fokus-Keywords, keine Titel-Kollision mit Seiten | `qa_check.py`, `seo_abgleich.py` | Muss, auto |
| K8 | FAQ mit 4–6 echten Nutzerfragen | `qa_check.py` + Autocomplete-Abgleich | Muss, auto |
| K9 | Quellen: mindestens 2 seriöse Quellen mit Abrufdatum, alle zeitabhängigen Aussagen belegt | `qa_check.py` + manuell | Muss |
| K10 | **Keine** erfundenen Preise, Erlebnisse, Bewertungen oder Tests. „Gefilmt“ nur bei eigenen Hotelseiten | Euro-Regex + manuell | Muss |
| K11 | Alle `[PRÜFEN]` aufgelöst, alle Redaktionskästen entfernt | Suche nach „PRÜFEN“ und „BILD (Redaktion)“ im WordPress-Entwurf | Muss vor Veröffentlichung |
| K12 | Bildrechte geklärt: eigenes Material oder dokumentierte Lizenz, ALT-Text gesetzt | Medienprüfung | Muss vor Veröffentlichung |
| K13 | Mobile Lesbarkeit: Absätze ≤ 4 Sätze, Tabellen ≤ 5 Spalten, Vorschau auf dem Smartphone geprüft | WordPress-Vorschau | Muss vor Veröffentlichung |
| K14 | Eignung für KI-Suche: klare Frage-Antwort-Struktur, Fakten mit Quelle und Datum, Autor erkennbar | Sichtprüfung | Soll |
| K15 | Keine verbotenen Floskeln, kein Keyword-Stuffing | `qa_check.py` + Lektorat | Muss |

**Regel:** Ein Artikel, der ein Muss-Kriterium nicht erfüllt, geht zurück in die Überarbeitung und wird danach komplett neu geprüft (Skript + Sichtprüfung).

## 3. In dieser Runde überarbeitet

| Artikel | Befund | Korrektur |
|---|---|---|
| 14, 25, 26 | Einstieg begann mit dem nackten Keyword („Türkei Urlaub Kosten: …“) und wirkte roboterhaft | Sätze natürlich umformuliert |
| 14 | Zimmerzahl, die auf unseren Hotelseiten uneinheitlich ist | entfernt, `[PRÜFEN]` gesetzt |
| 13, 16, 29 | Die drei Ferientitel waren gleich gebaut. „Aller Bundesländer“ ist bei Pfingstferien sachlich falsch | Titel unterschiedlich und präzise formuliert |
| 04, 16 | Titel über 580 px | gekürzt |
| 35 / R1 | Kemer- und Alanya-Titel fast identisch | R1-Titel neu formuliert |
| alle | WhatsApp-Nummer uneinheitlich | einheitlich die Nummer der Kontaktseite eingesetzt. **Bestätigung offen** |
| Plan | Orthodoxes Ostern 2027 falsch angenommen (richtig: 02.05.2027) | Plan korrigiert |
| 05, 10, 27 | Das Auswärtige Amt rät von Reisen in die VAE ab | zurückgestellt, Ersatzartikel R1–R3 |

Hinweise ohne Handlungsbedarf: Bei 14 und 17 steht das Fokus-Keyword nicht wörtlich in der H1, weil die H1 aus dem Plan bewusst natürlicher formuliert ist. Bei 07 und 04 erscheinen Euro-Beträge nur als Gebühren und Grenzwerte mit AA-Quelle (Visum, Zollanmeldung) und nicht als Reisepreise.

## 4. Was vor jeder Freigabe manuell zu prüfen ist (Top-Themen)

1. **Einreise (04, 07, 10, 22):** Die AA-Seite am Veröffentlichungstag erneut öffnen und das Datum „Stand“ vergleichen. Bei 04 ist ein Widerspruch auf der AA-Seite selbst vermerkt (Visumfreiheit gegenüber „Visum“).
2. **Sicherheitslage:** VAE (Dubai-Artikel, Malediven-Transit), Sinai (Artikel 20), Türkei (Grenzregionen). Jeweils die AA-Hinweise prüfen.
3. **Ferientermine (13, 16, 29, 24):** KMK-Übersicht (Stand 09.10.2025) und Kultusministerien. NRW und Niedersachsen sind doppelt geprüft.
4. **Unsere eigenen Hotelseiten widersprechen sich.** Diese Widersprüche bitte auf den Hotelseiten selbst korrigieren:
   - Mardan Palace: Ultra All Inclusive bzw. Golden Inclusive; 15 bzw. 16 km zum Flughafen
   - Quattro Beach: 438 bzw. 269 Zimmer
   - Rubi Platinum Sign: 167 bzw. 269 Zimmer
   - Selectum Family: Altersgrenzen des Miniclubs
   - Swandor Kemer: „Video geplant 23.10.2026“. Ist das Video online?
5. **Ägypten-Zielgebietsseite:** Ein Agent meldet, dass die Seite eigene Hotelbesuche in Ägypten behauptet. Falls das nicht zutrifft, ist das ein Glaubwürdigkeitsrisiko. Bitte prüfen (Hinweis an Projekt 2).
6. **Rechtliches (17, 32):** Die Aussagen zu §§ 651a ff. BGB habe ich stichprobenartig geprüft und sie sind plausibel. Trotzdem fachlich gegenlesen lassen. Bei 32 ist zu klären, ob haydi-weg Versicherungen vermittelt (§ 34d GewO). Davon hängt die CTA-Formulierung ab.
7. **Klima und Wassertemperaturen:** Wo keine amtliche Quelle verfügbar war, stehen Spannen mit `[PRÜFEN]`.
8. **Bilder:** Laut den Schreib-Agenten wirken einige Mediathek-Bilder wie Stock- oder KI-Bilder (u. a. IDs 876, 878, 880, 883, 4083). Dass ein Bild in der Mediathek liegt, heißt nicht, dass die Rechte geklärt sind. Vor der Verwendung Herkunft und Lizenz bestätigen.

## 5. Prozess für die laufende Aktualisierung

| Auslöser / Rhythmus | Artikel | Maßnahme |
|---|---|---|
| Vor jeder Veröffentlichung | alle | K1–K15, Skripte laufen lassen, `quellen_geprueft_am` aktualisieren |
| Monatlich (1. Montag) | 04, 07, 22 (+ 10 bei Reaktivierung) | AA-Seite: hat sich „Stand“ geändert? Wenn ja, Abschnitt anpassen und das Datum im Artikel aktualisieren |
| Monatlich | 05, 10, 27 (zurückgestellt), 19, 20 | Sicherheitslage prüfen. Dubai erst reaktivieren, wenn der AA-Hinweis aufgehoben ist |
| Quartalsweise | 19, 25, 27 (Kosten), 11 (Frühbucher) | Abgaben und Steuern prüfen (Tourism Dirham, Green Tax, Beherbergungssteuer Türkei, Balearen-Touristensteuer) |
| Jährlich im Oktober | 11, 13, 16, 24, 29 | Auf das Folgejahr umstellen: Titel, Termine, Feiertage. URL bleibt (siehe Strategie 9) |
| Bei Hotel-Änderungen | Türkei-Cluster | Hotelseite und alle verlinkenden Artikel gemeinsam aktualisieren |
| Nach 8 Wochen live | alle | GSC: Suchanfragen gegen den Artikel abgleichen und Kannibalisierung prüfen (BLOG_REPORTING_KONZEPT Kapitel 7) |

Automatisierbar ist die AA-Änderungserkennung: ein Skript vergleicht wöchentlich das Feld „Stand“ der AA-Länderseiten und meldet Änderungen.
