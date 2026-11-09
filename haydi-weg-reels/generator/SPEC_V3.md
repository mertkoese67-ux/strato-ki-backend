# SPEC v3 – Content-Upgrade der 39 Hauptplan-Reels (haydi-weg Reisen, Minden)

Ziel: von 7,6/10 auf ehrliche 9+/10. Nicht analysieren, sondern UMSETZEN: jede Reel-Definition in `gen/rNN.py` wird nach dieser Spezifikation neu geschrieben.
Alte Fassung (v2) zum Nachschlagen: `gen_v2/rNN.py` (gleiche Reel-Nummern) und `/home/user/strato-ki-backend/haydi-weg-reels/data/reels_hauptplan_v2.json`.
Kalender/Kuratierung (verbindlich, nicht ändern): `gen/kalender.py` → FINAL-Tupel (nr, datum, wd, serie, folge, titel, ort, themenwelt, entscheidung, alt_titel, struktur, ziel_s, begründung).
Generatorkern (nicht ändern; Probleme melden): `gen/build.py`. Lint je Modul: `cd gen && python3 build.py r03` (nur dieses Modul). NICHT `--write` ausführen.

## Harte Regeln (Auftraggeber)
- Keine Verkaufs-CTAs bis Ende 2026 (keine Preise, kein „buchen“, kein „Angebot“, kein „Link in Bio“, keine Beratung) – weder im Sprechtext noch in Captions. Eintrittsregeln dürfen erwähnt werden, Hotelpreise nie.
- Keine Personen vor der Kamera, keine Gesichter groß. Eigene Antalya-Hotelvideos bleiben Specials – nicht einplanen.
- Keine erfundenen Clipverfügbarkeiten. Keine falschen Drehorte oder Hotels. Jeder Hotel-/Ortsname nur, wenn belegt (Faktenliste unten oder eigene WebSearch, Quelle nennen).
- Ohne echte ElevenLabs-Audiodatei nur vorläufige Timecodes (macht build.py automatisch).
- Zusätzliches Stockbudget max. 50 €/Monat; Envato Elements bevorzugt, Pexels/Pixabay frei; keine Käufe.
- Strenge Bewertung, keine künstlichen Scores. Wenn ein Reel ehrlich unter 9 bleibt: so lassen und im Protokoll begründen.
- Die Weekday-Slots und 13 Wochen stehen fest (kalender.py).

## Was an v2 schwach war (muss in v3 sichtbar anders sein)
1. Zu viele sachliche Erklärvideos → Geschichte statt Lexikon; max. 2–3 Zahlen pro Reel, keine Zahlenlawine.
2. Hooks informativ statt überraschend → 5 echte Typen, Bild + Satz + Overlay + Frage (siehe unten).
3. Immer gleiche Struktur → 5 Strukturen A–E, Einstiege variieren, Teaser nicht überall.
4. Zu wenige konkrete Hotels/Resorts → wo im Kalender vorgesehen, Hotel/Resort konkret benennen (`hotel="…"`).
5. Teilweise ungesichertes Stock → 3 Schlüsselaufnahmen mit ehrlichem Status, recherchiert (Methode unten).
6. Einheitslängen 29–36 s → Ziel-Länge je Reel aus kalender.py (22–42 s), Toleranz ±7 s (Lint).
7. Zu wenige Follow-Gründe → Themenwelt-Endkarte, wiederkehrende Formate, aber keine monotonen Serieneinstiege.

## Modulaufbau (unverändert)
```python
# -*- coding: utf-8 -*-
from build import R, S, H, C, KS, ST
PEX = "frei (Pexels-Lizenz: kommerziell, ohne Pflichtnennung)"
PIX = "frei (Pixabay-Lizenz: kommerziell, ohne Pflichtnennung)"
ENV = "Abo (Envato Elements, kommerzielle Nutzung inkl. Social Media – Lizenz je Download registrieren)"
OWN = "eigene Grafik (CapCut, Markenfarben) – keine Lizenz nötig"
REELS = []
REELS.append(R("03", ...))
```
Pflichtfelder in `R(nr, …)`:
- `claim` (prüfbare Kernbehauptung, 1–2 Sätze), `answer` (FoF: „Fakt“/„Fake“/„Halb wahr“; sonst ""), `dach` (DACH-Anker), `emotion`,
- `hotel` (konkret benanntes Hotel/Resort oder ""),
- `arc` = dict mit genau diesen Schlüsseln: scrollstopper, setup, curiosity, build, resolution, second_aha, ending (je 1 Satz; Benennung der Struktur-Phasen in der gewählten Struktur A–E),
- `scenes` = Liste von `S(vo, sub, motif, place, cam, frame, move, light, stock, cut, trans, overlay, music, sfx, subhint, role=..., hold=0.0)`
  - role: erste Szene `"hook"`, genau eine (oder mehr) `"reveal"`, letzte Szene `"end"` (Endkarte, vo="" wenn kein gesprochener Teaser), sonst `"body"`.
  - `sub` = Untertitelfassung (Ziffern statt Zahlwörter, ohne Audio-Tags, ≤ 2 Zeilen/≤ 38 Zeichen pro Zeile sinngemäß); "" = automatisch aus vo.
  - `stock` = Liste Suchbegriffe (englisch) für diese Szene. Alle 13 Textfelder müssen gefüllt sein (Lint).
  - Hook-Szene: `subhint` enthält „keine Untertitel“. Endkarte: `hold=1.0`, Grafik, `stock=["eigene Endcard"]`.
  - Dynamische Szenenlängen: kurze Schnitte (1 Satz, ~2 s) neben längeren Takes (Reveal 4–6 s). Nicht 6× gleich lang.
- `hooks` = genau 5 `H(typ, spoken, frame, overlay, question, sc, reason)` in DIESER Reihenfolge der Typen:
  `"Visueller Schock"`, `"Neugierlücke"`, `"Überraschende Behauptung"`, `"Emotionaler Konflikt"`, `"Erwartung gegen Realität"`.
  - spoken: erster gesprochener Satz, ≤ 18 Wörter, Zahlen ausgeschrieben, keine Floskeln (Lint-Liste: „das musst du sehen“, „du wirst nicht glauben“, „unglaublich“, „krass“, „Geheimtipp“, „atemberaubend“, „wusstest du“, „niemand spricht darüber“, „verrückt“, „Wahnsinn“, „unfassbar“, „magisch“, „Paradies“, „traumhaft“, „Must-See“, „Schock“, „was dann passiert“, „bis zum Ende“, „warte bis“ …), nicht mit „Dieser/Diese/Dieses“, kein „sieht aus wie“, kein „Würdest du“.
  - frame: das erste sichtbare Bild, MUSS ohne Ton funktionieren (konkretes Motiv, Ort, Kadrage).
  - overlay: Text-Overlay im ersten Bild, ≤ 7 Wörter (ein Wort gelb markiert mit *Sternchen*, z. B. "Palast → *Stadion* → Hotel").
  - question: die offene Frage, die im Kopf des Zuschauers entsteht (1 Satz, als Frage).
  - sc: 7 Noten 1–10 in Reihenfolge scrollstop, verstaendlich, originalitaet, emotion, visuell, glaubwuerdig, dach. Streng! 10 nur, wenn wirklich nichts fehlt.
  - reason: 1 Satz, warum stark/schwach.
- `winner` = Index 0–4, `winner_reason` = 2–3 Sätze (warum dieser, was mit dem zweitbesten passiert, z. B. TikTok-Variante). Der Sieger-Hook ist der erste gesprochene Satz der Hook-Szene (scenes[0].vo) – muss identisch sein.
- `covers` = 3 `C(headline, yellow, image, variant)` – Varianten „A Frage“, „B Zahl/Behauptung“, „C Themenwelt“. Headline ≤ 2 Zeilen (≤ 28 Zeichen), `yellow` muss Teilstring der Headline sein.
- `key_shots` = genau 3 `KS(role, motif, source, ref, status, note)` mit role in dieser Reihenfolge: `"Scroll-Stop"`, `"Story"`, `"Reveal"`.
  - status: `"gefunden"` (Treffer mit passendem Titel/Motiv auf der Suchergebnisseite gelistet, Referenz = Pexels-ID oder Envato-Titel+Autor), `"verfügbar, ungeprüft"` (Treffer plausibel, Motiv/Ort nicht sicher), `"nicht gefunden"` (dann `note` = Alternative oder Umbau der Szene – Pflicht).
  - source: "Pexels" / "Envato Elements" / "Pixabay" / "Eigene Grafik". ref: ID bzw. Titel (Autor). note: Suchbegriffe + Fund, z. B. "Suche „ciragan palace“: 2 Treffer (daniel_atw, frimufilms); Ort im Titel bestätigt".
- `music` (Stimmung, BPM, Pegel), `stock` = Liste `ST(shot, source, ref, terms, status, missing=False, alt="", scenes="")` (alle Clips des Reels, inkl. Endkarte; `missing=True` nur, wenn ein benötigter Zusatzclip fehlt),
- `facts` = Liste (fakt, quelle) – nur Belegtes; `check` = Liste offener Prüfpunkte (ehrlich); `sources` = Liste Quellen (Domain/Name),
- `score` = dict(hook, visual, story, share, dach, facts) 1–10 (Gewichte 25/20/20/15/10/10, Ziel ≥ 9,0 ehrlich),
- `iterations` = ≥ 2 Strings „Runde n: …“ (Was war schwach, was wurde geändert, was bleibt schwach), `prepost` = Liste Prüfpunkte vor Posting,
- `cap_ig` (≤ 7 Hashtags, mit 📍 Ort), `cap_tt`, `cap_yt` (Titel ≤ 90 Zeichen) – ohne Verkaufs-CTA; erlaubt: „Speichern“, „Folgen für die nächste Themenwelt“, „Schreib mir, ob du es wusstest“,
- `changelog` = Liste „ALT → NEU“-Sätze gegenüber v2 (bei ERSETZT: alter Titel und warum ersetzt), `open` = offene Punkte,
- `end_card` = Grafiktext der Endkarte: Themenwelt-Zeile + Teaser auf die nächste Folge derselben Serie (Titel aus kalender.py, nächste Folge = Nr+3), z. B. "NATUR-WUNDER · Fakt oder Fake? #1 → Montag: Stammt das Matterhorn aus Afrika?",
- `teaser_spoken` = True/False (siehe Zuteilung unten). Wenn True: letzte Szene hat vo mit dem gesprochenen Teaser (1 Satz, Bezug zur nächsten Folge derselben Serie). Wenn False: letzte Szene vo="" (nur Grafik), der Sprechtext endet mit einem starken letzten Satz (Pointe, Bild, Frage), nicht mit „Folge uns“.
- optional `structure="A"` (Standard: aus kalender.py – NICHT abweichen ohne Grund), `approval` (Standardtext ok).

## Sprechtext (ElevenLabs, Mert_V2, Eleven v3)
- Natürliches, emotionales Deutsch, kurze Sätze, direkte Ansprache „du“, ein Erzähler, der vor Ort steht. Kein Lexikon, keine Zahlenlawine (max. 2–3 Zahlen, alle ausgeschrieben: „neunzehnhundertzehn“, „zweitausendfünfzehn“). Konkrete Sinnesbilder.
- Länge folgt der Geschichte: Ziel-Sekunden aus kalender.py; Richtwert Wörter ≈ Ziel-s × 2,2 (22 s ≈ 48 W, 30 s ≈ 66 W, 42 s ≈ 92 W). Lint: 35–120 Wörter, 16–48 s, ±7 s zum Ziel.
- Audio-Tags: max. 3 aus [curious] [whispers] [excited] [sighs] [laughs] [serious] – sparsam, nur am Satzanfang. Keine <break>-Tags.
- Einstieg variieren – Pflichtzuteilung:
  - Gesprochenes „Fakt oder Fake …“ im ersten Satz NUR bei 01, 10, 22, 37. Alle anderen FoF-Reels: Frage/Behauptung direkt, „Fakt oder Fake?“ nur als Overlay/Endstempel.
  - WDKS/RW: nie mit Serienname beginnen; nie zwei Reels mit demselben ersten Wort-Paar (z. B. nicht 4× „Hier …“, nicht 4× „Stell dir vor“).
  - Verbotene Einstiege: „Wusstest du“, „Stell dir vor“ (max. 1× im ganzen Plan → nicht verwenden), „Es gibt einen Ort“, „Heute zeige ich dir“.
- Gesprochener Teaser (teaser_spoken=True) NUR bei: 01, 05, 09, 13, 17, 21, 25, 29, 33, 37, 02, 14, 26. Alle anderen: False (Teaser nur auf der Endkarte).
- Auflösung/Kern spätestens bei 70 % der Länge; danach zweites Aha oder Haken; starkes Ende (Pointe oder Bild, das bleibt).
- Strukturen (Pflicht aus kalender.py): A Mystery → Enthüllung (Frage offen halten, Enthüllung in Reveal-Szene) · B Erwartung → überraschende Realität (erst Klischee zeigen, dann Bruch) · C Historischer Konflikt → Wendepunkt (Datum/Ereignis als Bruch, heute als Wendepunkt) · D Visuelles Rätsel → Erklärung (Bild zuerst, Erklärung folgt dem Bild) · E Außergewöhnliches Erlebnis → überraschender Haken (Erlebnis positiv, dann der Haken, dann Umgang damit).

## Schlüsselaufnahmen & Stock – Recherchemethode (ehrlich, keine Erfindung)
Pro Reel 3 Schlüsselaufnahmen prüfen (Scroll-Stop-Bild, Story-Bild, Reveal). Suchen mit WebFetch:
- Pexels: `https://www.pexels.com/search/videos/<begriffe mit %20>/` → Liste von `/video/<slug>-<id>/`; die ID ist die Referenz. Detailseiten (Lizenz/Ort) liefern 403 – deshalb Status höchstens „gefunden“ mit Prüfhinweis. Prompt für WebFetch: „Liste alle /video/…-<id>/ Slugs mit ID“.
- Envato Elements: `https://elements.envato.com/stock-video/<begriffe mit + verbunden>` → Titel + Autor der Treffer. Prompt: „Liste die Titel und Autoren der Stock-Video-Treffer“. Treffer mit passendem Ort im Titel = „gefunden“ (Lizenz im Abo); nur thematisch passend = „verfügbar, ungeprüft“.
- Pixabay-Suchseiten sind aus dieser Umgebung nicht lesbar → nicht als „gefunden“ eintragen (nur Suchbegriff).
- Wenn ein Schlüsselmotiv nicht gefunden wird: Szene umbauen (z. B. Grafik, Archivfoto-Hinweis, anderer Blickwinkel) und im `note` erklären; bei fehlendem Kernmotiv ggf. Story anpassen. Niemals IDs erfinden oder übernehmen, ohne sie in einer Suchseite gesehen zu haben (v2-IDs dürfen übernommen werden, wenn sie in der Liste „Bereits gesichtete Treffer“ unten stehen oder du sie selbst siehst).
- Archivfotos (historische Aufnahmen) sind kein Stock: als „Eigene Grafik“ mit Hinweis „historisches Foto – Rechte vor Nutzung klären (Wikimedia Commons/Public Domain prüfen)“ und Status „verfügbar, ungeprüft“ eintragen.

### Bereits gesichtete Treffer (09.11.2026, Suchergebnisseiten)
Pexels-Video-IDs (Slug-Titel passten zum Begriff):
- matera: 27562816, 15437330, 38330892, 16668218, 36097834, 15437328, 35542255, 17692709 · Envato „matera“: 8 Aerial-Treffer (gefunden)
- aswan/nile: 29233301, 29233187, 29233144, 35879466, 27433325, 29233131, 29233354 (Nil/Assuan allgemein; KEIN Old-Cataract-spezifischer Treffer) · Envato „old cataract aswan“: keine passenden Treffer → nicht gefunden
- santorini oia: 6554524, 20707597, 20663587, 32547016, 20663590, 20663589, 28122184, 10748208, 20621718, 20621738, 20591107, 20591098, 32558783, 20621697, 20621926, 34712511, 32558781, 6250832, 20591128, 6523735, 20663588, 32558787, 20707629, 6554714
- zugspitze: 33592694 (Gipfelkreuz), 39371628 (Seilbahnstation), 30402431/30402327/30402467/30402569 (Eibsee Winter), 36166624 · Envato „schneefernerhaus“: nichts → Schneefernerhaus-spezifisch nicht gefunden
- furka pass: 38912361 „historic swiss hotel amidst scenic alps“, 39195162 „scenic swiss mountain hotel with cars“, 38790546 „aerial view of swiss mountain road and hotel“, Straßen 34797485, 31100626, 13126809, 13126791, 28180173, 18626954, 35058292/35058293 · Envato „furka belvedere“: nichts
- rhone glacier: 38912361, 38790547 „stunning aerial view of swiss glacier“, 38816937 „majestic glacier scenery in swiss alps“, 30090909/30090907/30090908/30090905, 27769126–27769128, 30625450–30625452, 29876340, 35589634
- duden waterfall: 8857891 (unterer Fall, Drohne), 30543066, 31989766, 15348925 (unterer), 8860809 (unterer), 12177468 = OBERER Fall (nicht verwenden)
- giza pyramids: 32537704, 10717893, 10719817, 34208468, 19502910, 19502488, 4174146, 10719349, 29622798, 20284255/20284253 (Timelapse), 32537727
- Envato „ciragan palace“: „Ciragan Palace as seen from the Bosphorus“ (daniel_atw), „View of the Ciragan Palace from a ship“ (frimufilms) → gefunden (Ort im Titel); Pexels „ciragan palace“: nur Dolmabahçe → nicht gefunden
Alle anderen Motive: selbst suchen (Pexels + Envato), Ergebnis protokollieren.

## Gesicherte Fakten (WebSearch 09.11.2026) – nutzbar mit Quellenangabe
- Çırağan-Palast (Istanbul): Brand 19./20. Januar 1910 (Ursache umstritten: Heizungs-/Elektrodefekt vs. Brandstiftung – im Text offen lassen), danach Ruine; ab 1930 nutzte Beşiktaş das Gelände als Şeref-Stadion; Ende der 1980er von einer japanischen Gesellschaft (Kumagai Gumi) erworben; 1991 als Çırağan Palace Kempinski eröffnet (Palastflügel mit Suiten, Hotelneubau daneben). Quellen: kempinski.com (Hotelgeschichte), Beşiktaş JK-Vereinsgeschichte, Wikipedia (gegenlesen).
- Old Cataract Aswan (heute Sofitel Legend Old Cataract): von Thomas Cook & Son gebaut, eröffnet Jahreswende 1899/1900; Agatha Christie wohnte dort, „Tod auf dem Nil“ (1937) spielt teils im Haus; Verfilmung 1978 dort gedreht; Gäste u. a. Winston Churchill. Quellen: sofitel-legend.com (Hotelgeschichte), Agatha-Christie-Archiv/Biografien, Filmdatenbanken.
- Santorini Höhlenhäuser (yposkafa): in Bimsstein/Tuff gegraben, ursprünglich Behausungen armer Familien und Schiffsleute; Erdbeben 9. Juli 1956 (Magnitude ca. 7,5–7,8) zerstörte viele; seitdem Umbau zu Höhlenhotels/Suiten. „teuerste Suiten“ als Aussage nur relativ („gehören heute zu den gefragtesten“), nicht als Rekord. Quellen: santorini.gr / Archäologie-/Architekturquellen, EMSC/USGS zum Beben.
- Schneefernerhaus (Zugspitze): Hotel 20. Januar 1931 – 14. Januar 1992 auf rund 2.650 m, damals Deutschlands höchstgelegenes Hotel; nach US-Nutzung 1945–52 wieder Hotel; seit 12. Mai 1999 Umweltforschungsstation Schneefernerhaus (UFS). Quellen: schneefernerhaus.de (Geschichte), Bayerische Zugspitzbahn.
- Matera: Gesetz Nr. 619 vom 17. Mai 1952 (De Gasperi) zur Räumung der Sassi, rund 15.000 Menschen umgesiedelt; Bezeichnung „vergogna d'Italia“ (Togliatti 1948); UNESCO-Welterbe 9. Dezember 1993; Kulturhauptstadt Europas 2019; heute Höhlenhotels (z. B. Sextantio Le Grotte della Civita – Name nur, wenn in eigener Recherche bestätigt). Quellen: UNESCO whc.unesco.org, Comune di Matera, Treccani.
- Hotel Belvédère Furkapass: 1882 von Josef Seiler erbaut (Familie Seiler), Eisgrotte im Rhonegletscher seit 1894 jährlich neu geschlagen; Goldfinger-Verfolgungsjagd 1964 auf dem Pass gedreht; Hotel seit Saisonende 2015 geschlossen (Familie Carlen), Gletscher hat sich so weit zurückgezogen, dass er vom Hotel aus nicht mehr sichtbar ist. Rückzugszahl in Metern nur mit GLAMOS-Quelle (glamos.ch), sonst „über einen Kilometer seit der Hoteleröffnung“ NICHT behaupten → qualitativ bleiben. Quellen: SRF, NZZ, glamos.ch, gletscher.ch.
- Mena House (Gizeh, heute Marriott Mena House): königliches Jagdhaus 1869, Hotel seit 1886; Kairoer Konferenz November 1943 fand im Hotel statt (Roosevelt, Churchill, Chiang Kai-shek). Quellen: marriott.com Hotelgeschichte, Nationalarchive.
- Parador de Las Cañadas del Teide: einziges Hotel im Teide-Nationalpark, rund 2.150 m, 37 Zimmer. Quelle: parador.es.
- Kurumba Maldives: erstes Resort der Malediven, eröffnet 3. Oktober 1972 mit rund 30 Zimmern (Vihamanaafushi). Quelle: kurumba.com Geschichte, visitmaldives.com.
- Pexels-Lizenz: kommerzielle Nutzung ohne Pflichtnennung; Envato Elements: Abo-Lizenz je Download registrieren.
Nicht bestätigt (nicht behaupten): Fleecedecken auf dem Rhonegletscher-Detail (ok nur als „Teile des Gletschers werden mit Planen abgedeckt“ – gilt für die Eisgrotte, Quelle SRF; prüfen), Venedig-Pfahlzahl 1.106.657 (nur „über eine Million“ mit schwacher Quelle → als „Millionen Pfähle“ formulieren, Quelle angeben oder prüfen lassen), Santorini „teuerste Suiten Europas“.
Noch zu recherchieren (vom jeweiligen Modul-Autor, WebSearch, Quelle nennen): Jugendherberge Schloss Laufen am Rheinfall (existiert? seit wann?), Hotel Pragser Wildsee (seit 1899? Zufahrtsregel 2026 für Hotelgäste?), Hallstatt Beinhaus (Anzahl Schädel, bemalt seit wann, letzter Schädel 1995?), Venedig Eintritt 2027 (Tage/Beträge – nur mit offizieller Quelle cda.ve.it/Comune di Venezia; sonst ohne Zahl), Navagio-Strand aktueller Status (Sperrung, Aufschüttungsplan), Seceda-Drehkreuz 2025, Kakslauttanen/Glasiglus (Saariselkä, seit wann), Club Med Alcúdia 1950, Striezelmarkt 1434/Bautzen 1384/Wien 1296, Badrutt-Wette 1864 (Quellenlage), Adlon-Daten (1907/1945/1997), Bad Gastein Straubinger/Badeschloss (Wiedereröffnung 2023/24), Maya Bay (Sperrung 2018–2022, Baderegel), Benagil (Regeln seit 13.08.2024), Meteora (Netz/Winde, Treppen 1920er), Ephesos (Küste heute ca. 7–8 km entfernt), Pamukkale Antiker Pool (Säulen durch Erdbeben 7. Jh.?), Zelve-Umsiedlung 1952, Teide 3.715 m, Lençóis Regen ~1.200 mm, Plitvice Kalktuff, Papageifisch-Sand (Perry 2015), Palma Kathedrale 2.2./11.11. „Acht“, Alberobello Trulli-Legende, Riad-Definition, Polarkreiswanderung ~14–15 m/Jahr, Matterhorn Dent-Blanche-Decke/afrikanische Platte, Düden 40 m/8 km, Malediven Gästehausgesetz 2009, Nordlicht-Bedingungen.

## Bewertung (streng)
Scorecard 1–10 je Kriterium (Gewichte 25/20/20/15/10/10). Ziel ≥ 9,0 – aber nur, wenn der Hook ohne Ton funktioniert, die 3 Schlüsselaufnahmen mindestens „verfügbar, ungeprüft“ sind, die Story eine echte Wendung hat und ein Teil-/Speicherimpuls da ist. Ein Reel mit „nicht gefundenem“ Scroll-Stop-Bild bekommt in `visual` höchstens 8. Mindestens 2 Runden (`iterations`): Runde 1 = Schwäche der v2-Fassung bzw. erste v3-Fassung, Runde 2 = konkrete Änderung, Runde 3 optional. Rest-Schwächen ehrlich nennen.

## Ablauf je Modul
1. Alte Fassung lesen (`gen_v2/rNN.py`), verwertbare Fakten/Stock-IDs notieren.
2. Fakten für ERSETZT/RADIKAL-Reels per WebSearch sichern (Quelle protokollieren), offene Punkte in `check`.
3. Schlüsselaufnahmen per WebFetch suchen (Pexels + Envato), Status ehrlich setzen.
4. Reel schreiben (Struktur, Länge, Hooks mit 4 Komponenten, Cover, Szenen, Endkarte, Captions, Scorecard, Protokoll, Changelog ALT→NEU).
5. `python3 build.py rNN` – alle LINT-Hinweise beseitigen (QS<9 nur mit Begründung in iterations). Modul darf nur `from build import …` nutzen, keine anderen Dateien ändern.
6. Rückmeldung: je Reel eine Zeile (Entscheidung, Struktur, Länge, QS, Status der 3 Schlüsselaufnahmen, offene Fakten) + Liste der benutzten Quellen.
