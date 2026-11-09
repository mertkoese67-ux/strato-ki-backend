# -*- coding: utf-8 -*-
"""Erzeugt die v3-Lieferdokumente aus data/reels_hauptplan_v3.json (+ v2-Backup für ALT→NEU-Vergleich)."""
import json, csv, os, statistics, datetime
from collections import Counter
from kalender import SERIE_HINWEIS, STRUKTUR, THEMENWELTEN
OUT = "/home/user/strato-ki-backend/haydi-weg-reels/"
SP = os.path.dirname(os.path.abspath(__file__)) + "/"
v3 = json.load(open(OUT + "data/reels_hauptplan_v3.json", encoding="utf-8")); R3 = v3["reels"]
v2 = json.load(open(OUT + "backup/reels_hauptplan_v2-vor-upgrade.json", encoding="utf-8")); R2 = {r["id"]: r for r in v2["reels"]}
STAND = v3["meta"]["stand"]
def win(r): return [h for h in r["hooks"] if h["winner"]][0]
def ks(r, role): return [k for k in r["key_shots"] if k["role"] == role][0]
def ksl(r): return " / ".join({"gefunden": "✅", "verfügbar, ungeprüft": "🟡", "nicht gefunden": "❌"}[k["status"]] for k in r["key_shots"])
def wk(r): return (r["nr"] - 1)//3 + 1
avg3 = sum(r["scorecard"]["total"] for r in R3)/39; avg2 = sum(R2[r["id"]]["scorecard"]["total"] for r in R3)/39
L3 = [r["cut"]["total_sec"] for r in R3]; L2 = [R2[r["id"]]["cut"]["total_sec"] for r in R3]
KSC = Counter(k["status"] for r in R3 for k in r["key_shots"])
dec = Counter(r["decision_v3"] for r in R3)
hotels = [(r["id"], r["hotel"]) for r in R3 if r["hotel"]]

# ------------------------------------------------------------ 02 Masterplan v3
L = ["# haydi-weg Reel-Masterplan 09.11.2026 – 05.02.2027 · Fassung v3 (Content-Upgrade, Stand %s)" % STAND, "",
     "Basis: Masterplan 06.11.2026 → v2 (09.11., 6 Themen ersetzt) → **v3 (09.11., Content-Upgrade)**: %d Themen ersetzt, %d radikal überarbeitet, %d behalten; alle 39 mit neuen Hooks (Bild · Satz · Overlay · Frage), neuen Sprechtexten, Schlüsselaufnahmen mit Materialstatus, dynamischen Schnittplänen und strenger Scorecard. Alle Details je Reel: `data/reels_hauptplan_v3.json` (im Reel-Studio v39 eingebettet und importierbar). Die 51 Specials sind nicht Teil dieses Plans und blieben unverändert." % (dec["ERSETZT"], dec["RADIKAL VERBESSERN"], dec["BEHALTEN"]), "",
     "## 1 Strategie (verbindlich)", "",
     "- Unterhaltsamer DACH-Reiseentdeckungskanal; Prioritäten: Reichweite bei Nicht-Followern, erste Sekunden, Wiedergabedauer, Shares/Saves, Profilbesuche, Follower je 1.000 Views, Premium-Marke, Vertrauen.",
     "- Bis 31.12.2026 keine Verkaufs-CTAs; keine Personen vor der Kamera; eigene Antalya-Hotelvideos bleiben Specials.",
     "- Nur korrekt zugeordnetes, rechtmäßig nutzbares Fremdmaterial (Envato Elements bevorzugt, Pexels/Pixabay ergänzend, Budget ≤ 50 €/Monat, keine Käufe ohne Freigabe). Keine erfundenen Clipverfügbarkeiten, keine falschen Drehorte oder Hotels.",
     "- Drei feste Wochentage bleiben (Mo „Fakt oder Fake?“, Mi „Was dir keiner sagt“, Fr „Reisewissen“). %s" % SERIE_HINWEIS,
     "- Ohne echte ElevenLabs-Audiodatei sind alle Timecodes vorläufig; das Studio rechnet nach Audio-Upload um.", "",
     "## 2 Content-Identität und Follow-Strategie (neu in v3)", "",
     "**Wiedererkennung ohne Monotonie.** Der Kanal hat vier wiederkehrende Themenwelten, die in jeder Endkarte als Zeile stehen und im Studio als Filter dienen. Sie sind der Grund zu folgen („mehr aus dieser Welt“), ohne dass jedes Reel gleich beginnt:", "",
     "| Themenwelt | Versprechen | Reels |", "|---|---|---|"]
for tw, txt in THEMENWELTEN.items():
    L.append("| **%s** | %s | %s |" % (tw, txt, ", ".join(r["id"] for r in R3 if r["themenwelt"] == tw)))
L += ["", "**Fünf Storytelling-Strukturen**, nie zweimal hintereinander dieselbe (Skriptprüfung):", ""]
sc = Counter(r["structure"] for r in R3)
for k, v in STRUKTUR.items(): L.append("- **%s – %s** (%d Reels: %s)" % (k, v, sc[k], ", ".join(r["id"] for r in R3 if r["structure"] == k)))
L += ["", "**Einstiege und Enden variieren.** Gesprochenes „Fakt oder Fake“ nur in %s; alle anderen Montagsfolgen stellen die Frage direkt und tragen das Serienlabel nur als Overlay. Ein gesprochener Teaser auf die nächste Folge steht in %d von 39 Reels (%s); die übrigen enden mit einer Pointe oder einem bleibenden Bild – der Teaser steht dort nur auf der Endkarte." % (
    ", ".join(r["id"] for r in R3 if r["series"] == "FoF" and r["vo"]["full"].lstrip("[a-z] ").startswith("Fakt oder Fake")), sum(1 for r in R3 if r["teaser_spoken"]), ", ".join(r["id"] for r in R3 if r["teaser_spoken"])),
      "", "**Längen folgen der Geschichte:** %d–%d s (vorläufig), Standardabweichung %.1f s (v2: %d–%d s, %.1f s)." % (min(L3), max(L3), statistics.pstdev(L3), min(L2), max(L2), statistics.pstdev(L2)),
      "", "**Konkrete Hotels und Resorts** (nur mit belegten Fakten, nie mit Preisen): " + " · ".join("%s %s" % (i, h) for i, h in hotels) + ".",
      "", "**Follow-Mechanik je Reel:** 1) erstes Bild stoppt den Daumen ohne Ton, 2) der gesprochene Satz öffnet eine Frage, 3) die Auflösung kommt spätestens bei 70 % der Länge, 4) ein zweites Aha oder ein Haken belohnt das Dranbleiben, 5) die Endkarte nennt Themenwelt und nächste Folge. Teil-/Speicherimpuls entsteht durch den konkreten Nutzwert („wann“, „welche Regel“, „welcher Ort“) – nicht durch Aufforderungen. Keine Zahlenversprechen: Follower je 1.000 Views, Shares und Profilbesuche werden gemessen (`09_KPI_TESTSTRATEGIE.md`), nicht vorhergesagt.", "",
      "## 3 Was sich gegenüber v2 geändert hat", "", "| Bereich | v2 (09.11., früh) | v3 (Content-Upgrade) |", "|---|---|---|",
      "| Themen | 39, davon 6 gegenüber dem 06.11. ersetzt | %d weitere ersetzt (%s), %d radikal überarbeitet (%s) – Details `15_UPGRADE_AENDERUNGEN_ALT_NEU.md` |" % (dec["ERSETZT"], ", ".join(r["id"] for r in R3 if r["decision_v3"] == "ERSETZT"), dec["RADIKAL VERBESSERN"], ", ".join(r["id"] for r in R3 if r["decision_v3"] == "RADIKAL VERBESSERN")),
      "| Hooks | 5 Typen, Satz + erstes Bild | 5 neue Typen (Visueller Schock · Neugierlücke · Überraschende Behauptung · Emotionaler Konflikt · Erwartung gegen Realität), jeder Hook = Bild + Satz + Overlay + offene Frage; Floskel-Sperre automatisch |",
      "| Struktur | ein Bogen für alle | 5 Strukturen A–E, nie zweimal hintereinander |",
      "| Längen | 29–36 s | %d–%d s |" % (min(L3), max(L3)),
      "| Material | Stockliste je Reel, IDs aus Plan-Recherche ungeprüft | 3 Schlüsselaufnahmen je Reel mit Status aus Suchseiten-Recherche am 09.11.: ✅ gefunden %d · 🟡 verfügbar, ungeprüft %d · ❌ nicht gefunden %d (mit Umbau) |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"]),
      "| Hotels | 5 konkret | %d konkret benannt |" % len(hotels),
      "| Qualität | Ø %.2f, 0 Reels ≥ 9,0 | Ø %.2f, %d Reels ≥ 9,0 – streng bewertet, Begründungen in `16_QUALITAETSBEWERTUNG_KRITISCH.md` |" % (avg2, avg3, sum(1 for r in R3 if r["scorecard"]["total"] >= 9)),
      "| Studio | v38 | v39: Themenwelt-Filter, Struktur, Schlüsselaufnahmen mit Status, Hooks mit 4 Komponenten, Overlay-Übernahme ins Video; alle v37/v38-Funktionen erhalten |", "",
      "## 4 Kalender und Reel-Übersicht", "", "| Nr | Datum | Serie | Titel | Themenwelt | Str. | Länge | Sieger-Hook (gesprochen) | Material | QS |", "|---|---|---|---|---|---|---|---|---|---|"]
for r in R3:
    L.append("| %02d | %s %s | %s #%d | %s | %s | %s | %.0f s | %s | %s | %.2f |" % (r["nr"], r["weekday"], r["date_de"], r["series"], r["episode"], r["title"], r["themenwelt"], r["structure"], r["cut"]["total_sec"], win(r)["spoken"], ksl(r), r["scorecard"]["total"]))
L += ["", "Material-Legende: ✅ gefunden (Treffer auf Suchseite gelistet) · 🟡 verfügbar, ungeprüft · ❌ nicht gefunden (Umbau/Alternative im Plan) – Reihenfolge Scroll-Stop / Story / Reveal.", "", "## 5 Reel-Steckbriefe", ""]
for r in R3:
    w = win(r); r2 = R2[r["id"]]
    L += ["### %s · %s %s · %s #%d · %s" % (r["id"], r["weekday"], r["date_de"], r["series_name"], r["episode"], r["title"]), "",
          "**Ort:** %s · **Themenwelt:** %s · **Struktur:** %s – %s · **Upgrade:** %s%s · **Länge:** ca. %d s (vorläufig %.1f s) · **QS:** %.2f (v2: %.2f)" % (r["place"], r["themenwelt"], r["structure"], r["structure_name"], r["decision_v3"], (" (vorher: „%s“)" % r["title_v2"]) if r["title_v2"] != r["title"] else "", r["target_sec"], r["cut"]["total_sec"], r["scorecard"]["total"], r2["scorecard"]["total"]), "",
          "**Warum so:** %s" % r["decision_reason"], "",
          "**Behauptung:** %s%s%s" % (r["claim"], (" · **Auflösung:** " + r["answer"]) if r["answer"] else "", (" · **Hotel/Resort:** " + r["hotel"]) if r["hotel"] else ""), "",
          "**Sieger-Hook (%s, Ø %.2f):** Bild: %s · Gesprochen: „%s“ · Overlay: %s · Frage im Kopf: %s – %s" % (w["typ"], w["total"], w["first_frame"], w["spoken"], w["overlay"].replace("*", ""), w["question"], r["hook_winner_reason"]), "",
          "**Schlüsselaufnahmen:** " + " · ".join("%s: %s (%s %s, **%s**%s)" % (k["role"], k["motif"], k["source"], k["ref"], k["status"], (" – " + k["note"]) if k["note"] else "") for k in r["key_shots"]), "",
          "**Cover:** " + " · ".join("%d) %s [%s]" % (i+1, c["headline"], c["yellow"]) for i, c in enumerate(r["covers"])), "",
          "**Sprechtext (%d Wörter, ca. %.0f s vorläufig):** %s" % (r["vo"]["words"], r["vo"]["est_sec"], r["vo"]["full"].replace("\n", " ")), "",
          "**Endkarte:** %s (%s)" % (r["end_card"], "Teaser gesprochen" if r["teaser_spoken"] else "Teaser nur Grafik"), "",
          "**Schnitt:** %d Szenen, %s (vorläufig) · Musik: %s" % (len(r["cut"]["scenes"]), r["cut"]["total_tc"], r["cut"]["music"]), "",
          "**Fakten gesichert:** " + " · ".join("%s [%s]" % (f["fact"], f["source"]) for f in r["facts"]["secured"]), "",
          "**Vor Posting prüfen:** " + " · ".join(r["approval"]["pre_post_checks"] + r["facts"]["to_check"]), "",
          "**ALT → NEU:** " + " · ".join(r["changelog_vs_plan"]), "",
          "**Offen:** " + (" · ".join(r["open_points"]) if r["open_points"] else "nichts"), ""]
open(OUT + "02_MASTERPLAN_FINAL.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 08 Kalender
season = {"01": "Start Plan (09.11.) – Nachholtermin für 01–03 festlegen", "10": "1. Advent 29.11. – Weihnachtsmarkt am Tag danach", "19": "Vor den Weihnachtsferien (Winterurlaub)", "21": "1. Weihnachtstag – Reel bewusst kurz (22 s)", "24": "Neujahr – Zugspitze/Schnee", "26": "06.01. Heilige Drei Könige (BW/BY/ST, AT) – Posting nachmittags testen", "37": "Vortag des Lichtphänomens (2.2.)", "39": "Staffelfinale – Endkarte „13 Wochen, 39 Orte“"}
L = ["# 13-Wochen-Kalender (Fassung v3) · 09.11.2026 – 05.02.2027", "",
     "Drei feste Serien, 3 Reels pro Woche (Mo/Mi/Fr), 39 Reels, 13 Wochen – unverändert. Freitag heißt ab v3 „Reisewissen“ (%s). Wochentage per Kalenderrechnung geprüft; nie dasselbe Land und nie dieselbe Struktur direkt hintereinander." % SERIE_HINWEIS.split(":")[1].strip(), "",
     "**Startdatum:** Der Plan beginnt am 09.11.2026 (heute). Empfehlung unverändert: Daten beibehalten, Reels 01–03 in Woche 2 nachproduzieren (siehe `17_PRODUKTIONSPRIORITAETEN_1-12.md`).", "",
     "| Nr | Datum | KW | Wo | Serie | Titel | Ort | Themenwelt | Struktur | Länge | Upgrade v3 | QS | Material | Saison / Hinweis |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
rows = []
for r in R3:
    d = datetime.date(*map(int, r["date"].split("-"))); prev = (d - datetime.timedelta(days=1)).strftime("%d.%m.%Y")
    L.append("| %02d | %s %s | %d | %d | %s #%d | %s | %s | %s | %s | %.0f s | %s | %.2f | %s | %s |" % (r["nr"], r["weekday"], r["date_de"], r["kw"], wk(r), r["series"], r["episode"], r["title"], r["place"], r["themenwelt"], r["structure"], r["cut"]["total_sec"], r["decision_v3"], r["scorecard"]["total"], ksl(r), season.get("%02d" % r["nr"], "")))
    rows.append(["%02d" % r["nr"], r["date_de"], r["weekday"], r["kw"], wk(r), r["series"], r["episode"], r["title"], r["title_v2"], r["place"], r["themenwelt"], r["structure"], r["structure_name"], r["target_sec"], round(r["cut"]["total_sec"], 1), r["decision_v3"], r["scorecard"]["total"], ksl(r), r["hotel"], season.get("%02d" % r["nr"], ""), prev])
land = Counter(r["place"].split(" ")[0] for r in R3)
L += ["", "## Verteilung", "", "- Länder: " + " · ".join("%s %d" % (k, v) for k, v in land.most_common()) + ".",
      "- Themenwelten: " + " · ".join("%s %d" % (k, v) for k, v in Counter(r["themenwelt"] for r in R3).items()) + ".",
      "- Strukturen: " + " · ".join("%s %d" % (k, v) for k, v in sorted(sc.items())) + ".",
      "- Längen: %d–%d s, Ø %.1f s." % (min(L3), max(L3), sum(L3)/39),
      "- Fakt-oder-Fake-Auflösungen: " + " · ".join("#%d %s" % (r["episode"], r["answer"]) for r in R3 if r["series"] == "FoF") + ".", "",
      "## Vortags-Prüfung", "", "Jedes Reel wird am Vortag (Spalte in der CSV) geprüft: Fakten mit Datum (Eintritt, Sperrungen, Reservierungsregeln, Flaggen), Clip-Orte auf den Detailseiten, Lizenzregistrierung, kein Verkaufs-CTA, Hook ohne Ton verständlich. Freigabe im Studio erst, wenn alle Häkchen gesetzt sind."]
open(OUT + "08_KALENDER_13_WOCHEN.md", "w", encoding="utf-8").write("\n".join(L))
with open(OUT + "08_KALENDER_13_WOCHEN.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(["Nr","Datum","Wochentag","KW","Woche im Plan","Serie","Folge","Titel v3","Titel v2","Ort","Themenwelt","Struktur","Struktur-Name","Ziel s","Länge vorläufig s","Upgrade v3","QS v3","Material (Scroll-Stop/Story/Reveal)","Hotel/Resort","Saison/Hinweis","Vortags-Prüfung"]); w.writerows(rows)

# ------------------------------------------------------------ 15 Änderungsliste ALT → NEU
L = ["# Änderungsliste ALT → NEU (v2 vom 09.11. früh → v3 Content-Upgrade, Stand %s)" % STAND, "",
     "Ausgangslage v2: Ø %.2f/10, kein Reel ≥ 9, Längen %d–%d s (Standardabweichung %.1f s), %d von 13 Montagsfolgen mit gesprochenem „Fakt oder Fake“, 39 von 39 mit gesprochenem Teaser am Ende, Stock-IDs ungeprüft übernommen. Die vom Auftraggeber genannten Schwächen wurden nicht relativiert, sondern umgesetzt – die Liste unten zeigt je Reel, was konkret anders ist." % (avg2, min(L2), max(L2), statistics.pstdev(L2), sum(1 for i in R2.values() if i["series"] == "FoF" and i["vo"]["full"].startswith("Fakt oder Fake"))), "",
     "## 1 Plan-Ebene", "", "| # | ALT (v2) | NEU (v3) | Grund |", "|---|---|---|---|",
     "| U1 | 39 Themen, viele Erklärvideos | %d ersetzt, %d radikal umgebaut, %d behalten (aber neu geschrieben) – %d Themen wurden infrage gestellt | Entertainment-Potenzial entscheidet, keine Quoten |" % (dec["ERSETZT"], dec["RADIKAL VERBESSERN"], dec["BEHALTEN"], dec["ERSETZT"] + dec["RADIKAL VERBESSERN"]),
     "| U2 | 5 Hook-Typen (WOW/Behauptung/Lücke/Konflikt/Erwartung), Satz + Bild | 5 Typen neu (Visueller Schock · Neugierlücke · Überraschende Behauptung · Emotionaler Konflikt · Erwartung gegen Realität); jeder Hook = erstes Bild + gesprochener Satz + Overlay + offene Frage; Floskeln, leere Superlative und Fake-Cliffhanger per Lint gesperrt | Hooks waren informativ, nicht überraschend |",
     "| U3 | Ein Storybogen für alle | Fünf Strukturen A–E, Zuordnung je Reel, nie zweimal hintereinander | Wiederholte Erzählmuster |",
     "| U4 | Längen 29–36 s | %d–%d s, Ziel je Reel im Kalender, Toleranz ±7 s | Einheitslängen |" % (min(L3), max(L3)),
     "| U5 | Gesprochener Teaser in allen 39 | Teaser gesprochen in %d Reels, sonst nur Endkarte; Serienformel nur in 4 Montagsfolgen gesprochen | Monotone Serieneinstiege/-enden |" % sum(1 for r in R3 if r["teaser_spoken"]),
     "| U6 | Stockliste mit IDs aus der Plan-Recherche, ungeprüft | 3 Schlüsselaufnahmen je Reel, am 09.11. über Pexels-/Envato-Suchseiten geprüft: ✅ %d · 🟡 %d · ❌ %d; bei ❌ Umbau im Plan | Teilweise ungesichertes Stock |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"]),
     "| U7 | 5 Hotels konkret | %d Hotels/Resorts konkret und belegt (ohne Preise) | Zu wenige spektakuläre Hotels |" % len(hotels),
     "| U8 | Cluster (Natur-WOW, Hotelkonzept …) | 4 Themenwelten als Content-Identität (Endkarte, Studio-Filter) | Zu wenige Follow-Gründe |",
     "| U9 | Freitag „Reisewissen in 30 Sekunden“ | „Reisewissen“ | Längen folgen der Geschichte |",
     "| U10 | Scorecard Ø %.2f | Ø %.2f, streng, ≥ 2 Runden je Reel; Score ersetzt keine Prüfung | Ziel 9+ ehrlich |" % (avg2, avg3),
     "| U11 | Studio v38 | Studio v39 (neue Felder, Filter, Overlay-Übernahme), alle Funktionen/Daten/Specials erhalten, Backup vor Änderung | Auftrag |", "",
     "## 2 Reel-Ebene", "", "| Nr | Datum | Entscheidung | ALT (v2) | NEU (v3) | Struktur | Länge v2 → v3 | QS v2 → v3 | Was konkret anders ist |", "|---|---|---|---|---|---|---|---|---|"]
for r in R3:
    r2 = R2[r["id"]]
    L.append("| %s | %s | **%s** | %s | %s | %s | %.0f → %.0f s | %.2f → %.2f | %s |" % (r["id"], r["date_de"], r["decision_v3"], r2["title"], r["title"], r["structure"], r2["cut"]["total_sec"], r["cut"]["total_sec"], r2["scorecard"]["total"], r["scorecard"]["total"], " · ".join(r["changelog_vs_plan"])))
L += ["", "## 3 Infrage gestellte Themen und Entscheidung", "", "| Nr | Thema v2 | Schwäche | Entscheidung | Ergebnis |", "|---|---|---|---|---|"]
for r in R3:
    if r["decision_v3"] != "BEHALTEN":
        L.append("| %s | %s | %s | %s | %s |" % (r["id"], r["title_v2"], r["decision_reason"].split(".")[0] + ".", r["decision_v3"], r["title"]))
L += ["", "## 4 Was NICHT geändert wurde", "", "- Die 51 Specials (v37-Daten) – nicht Teil des Auftrags, im Studio unverändert.", "- Wochentage, 13 Wochen, Postingdaten.", "- Regeln: keine Verkaufs-CTAs bis Ende 2026, keine Personen vor der Kamera, Budget ≤ 50 €/Monat, Untertitel-Stil (Manrope SemiBold, Ziffern, keine Untertitel im Hook).", "- Timecode-Logik (30 fps, HH:MM:SS:FF, vorläufig bis Audio vorliegt) und die Audio-Analyse des Studios."]
open(OUT + "15_UPGRADE_AENDERUNGEN_ALT_NEU.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 17 Produktionsprioritäten 1–12
first = [r for r in R3 if r["nr"] <= 12]
def risk(r):
    n_miss = sum(1 for k in r["key_shots"] if k["status"] == "nicht gefunden"); n_unk = sum(1 for k in r["key_shots"] if k["status"] == "verfügbar, ungeprüft")
    return n_miss*3 + n_unk + (1 if any(st["missing"] for st in r["stock"]) else 0) + min(2, len(r["facts"]["to_check"]))//2
order = sorted(first, key=lambda r: (-risk(r), r["nr"]))
L = ["# Produktionsprioritäten für die ersten 12 Reels (09.11.–04.12.2026)", "",
     "Grundsatz: **Material zuerst.** Jedes Reel wird erst produziert, wenn die drei Schlüsselaufnahmen auf den Detailseiten geprüft (Ort, Urheber, Personen, Lizenz) und heruntergeladen sind. Reels mit offenem Material (❌/🟡) oder datumsabhängigen Fakten werden zuerst recherchiert, damit die Postingdaten halten. Startlage: 09.11. ist bereits Posting-Tag von Reel 01 – Reels 01–03 werden nachproduziert (Empfehlung: Reihenfolge beibehalten, in Woche 2 zusätzlich posten oder Daten um eine Woche schieben – Entscheidung Auftraggeber, siehe `12_OFFENE_PUNKTE.md`).", "",
     "## 1 Reihenfolge der Vorbereitung (Material- und Faktenrisiko zuerst)", "", "| Prio | Reel | Posting | Titel | Material (SS/Story/Reveal) | Fehlende Zusatzclips | Fakten zu prüfen | Risiko |", "|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(order, 1):
    L.append("| %d | %s | %s %s | %s | %s | %s | %d | %s |" % (i, r["id"], r["weekday"], r["date_de"], r["title"], ksl(r), ", ".join(st["shot"] for st in r["stock"] if st["missing"]) or "–", len(r["facts"]["to_check"]), "hoch" if risk(r) >= 4 else "mittel" if risk(r) >= 2 else "niedrig"))
L += ["", "## 2 Produktionsplan in Wochen", "", "| Produktionswoche | Reels | Aufgaben |", "|---|---|---|",
      "| Wo 1 (09.–15.11.) | 01, 02, 03 (+ Material 04–06 sichern) | Schlüsselaufnahmen prüfen/laden, ElevenLabs-Audio 01–03, Studio: Audio hochladen → Zeiten aus Audio → Untertitel prüfen → CapCut-Export; Vortags-Faktencheck; Nachholtermin 01–03 festlegen |",
      "| Wo 2 (16.–22.11.) | 04, 05, 06 (+ Material 07–09) | wie oben; 05: Glasiglu-Material und Hotelname bestätigen; 06: Anaga-Nebelwald-Clip (Reveal) |",
      "| Wo 3 (23.–29.11.) | 07, 08, 09 (+ Material 10–12) | 08: Antiker-Pool-Säulen-Clip; 09: Club-Med-Archivfoto Rechte klären |",
      "| Wo 4 (30.11.–06.12.) | 10, 11, 12 | 10: Marktquellen 1434/1384/1296 gegenlesen; 12: Old-Cataract-Terrasse (Alternative laut Plan) |", "",
      "## 3 Je Reel: Was vor der Produktion fertig sein muss", ""]
for r in first:
    w = win(r)
    L += ["### %s · %s %s · %s (%s #%d, Struktur %s, ca. %d s)" % (r["id"], r["weekday"], r["date_de"], r["title"], r["series"], r["episode"], r["structure"], r["target_sec"]), "",
          "- **Erstes Bild (ohne Ton):** %s · Overlay: %s" % (w["first_frame"], w["overlay"].replace("*", "")),
          "- **Schlüsselaufnahmen:** " + " · ".join("%s – %s %s (**%s**%s)" % (k["role"], k["source"], k["ref"], k["status"], (": " + k["note"]) if k["note"] else "") for k in r["key_shots"]),
          "- **Zusatzclips offen:** " + (" · ".join("%s → %s" % (st["shot"], st["alternative"]) for st in r["stock"] if st["missing"]) or "keine"),
          "- **Fakten am Vortag:** " + (" · ".join(r["facts"]["to_check"]) or "keine offenen"),
          "- **Audio:** Sprechtext `03_SPRECHERTEXTE/%s*.txt` (%d Wörter) in ElevenLabs (Mert_V2, Eleven v3) → MP3 ins Studio → Zeiten/Untertitel neu rechnen" % (r["id"], r["vo"]["words"]),
          "- **Freigabe-Gate im Studio:** Faktencheck, Materialcheck (inkl. 3 Schlüsselaufnahmen), Vortags-Prüfung, Hook-QA", ""]
L += ["## 4 ElevenLabs- und Schnitt-Standard (gilt für alle 12)", "", "1. Sprechtext unverändert einfügen (Audio-Tags bleiben in eckigen Klammern), Stimme Mert_V2, Modell Eleven v3, Stabilität mittel, Stil leicht.", "2. MP3 im Studio ablegen → „Szenen & Untertitel aus Audio neu berechnen“ → Untertitel-Zeilen hören und ggf. je Zeile korrigieren → SRT exportieren.", "3. CapCut: Schnittplan (CSV/MD) aus dem Studio, 9:16, 30 fps, Hook ohne Untertitel, Logo weiß ab Sekunde 3, Endkarte mit Themenwelt-Zeile (Teaser gesprochen nur, wo markiert).", "4. Vor Upload: Freigabe im Studio auf „Freigegeben“ (Gate), Captions aus dem Studio, kein Verkaufs-CTA.", "", "Keine Zahlenversprechen zur Reichweite; gemessen wird nach `09_KPI_TESTSTRATEGIE.md`."]
open(OUT + "17_PRODUKTIONSPRIORITAETEN_1-12.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 16 Kritische Qualitätsbewertung (Tabellen + Text aus kritik_v3.md)
L = ["# Kritische Qualitätsbewertung des v3-Plans (Stand %s)" % STAND, "",
     "Gewichtung laut Auftrag: Hook/erstes Bild 25 % · Visuelle Stärke 20 % · Storytelling 20 % · Shareability 15 % · DACH-Relevanz 10 % · Fakten/Umsetzbarkeit 10 %. Alle Noten sind Einschätzungen der Redaktion nach mindestens zwei Überarbeitungsrunden – **keine Messwerte, keine Erfolgsversprechen**. Ein Score ersetzt keine Rechte-, Fakten- oder Materialprüfung; die Freigabe im Studio bleibt an diese Prüfungen gebunden.", "",
     "## 1 Gesamtbild", "", "| Kennzahl | v2 | v3 |", "|---|---|---|",
     "| Ø Scorecard | %.2f | **%.2f** |" % (avg2, avg3),
     "| Reels ≥ 9,0 | %d | %d |" % (sum(1 for r in R2.values() if r["scorecard"]["total"] >= 9), sum(1 for r in R3 if r["scorecard"]["total"] >= 9)),
     "| Reels < 8,5 | %d | %d |" % (sum(1 for r in R2.values() if r["scorecard"]["total"] < 8.5), sum(1 for r in R3 if r["scorecard"]["total"] < 8.5)),
     "| Längen | %d–%d s (sd %.1f) | %d–%d s (sd %.1f) |" % (min(L2), max(L2), statistics.pstdev(L2), min(L3), max(L3), statistics.pstdev(L3)),
     "| Schlüsselaufnahmen gefunden / ungeprüft / nicht gefunden | – (nicht erhoben) | %d / %d / %d |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"]),
     "| Konkrete Hotels/Resorts | 5 | %d |" % len(hotels), "",
     "## 2 Je Reel (streng)", "", "| Reel | Titel | Hook | Vis | Story | Share | DACH | Fakt | **v3** | v2 | Material | Rest-Schwäche (letzte Runde) |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in R3:
    s = r["scorecard"]["scores"]
    L.append("| %s | %s | %d | %d | %d | %d | %d | %d | **%.2f** | %.2f | %s | %s |" % (r["id"], r["title"], s["hook"], s["visual"], s["story"], s["share"], s["dach"], s["facts"], r["scorecard"]["total"], R2[r["id"]]["scorecard"]["total"], ksl(r), r["scorecard"]["iterations"][-1][:220]))
low = [r for r in R3 if r["scorecard"]["total"] < 9]
L += ["", "## 3 Reels unter 9,0 – warum sie trotzdem im Plan bleiben", ""] + (["- **%s %s (%.2f):** %s" % (r["id"], r["title"], r["scorecard"]["total"], r["scorecard"]["iterations"][-1]) for r in low] or ["- keine"]) + [""]
krit = SP + "kritik_v3.md"
if os.path.exists(krit): L += [open(krit, encoding="utf-8").read()]
open(OUT + "16_QUALITAETSBEWERTUNG_KRITISCH.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 13 Testbericht (aus tests/testergebnis.json)
tp = OUT + "tests/testergebnis.json"
if os.path.exists(tp):
    t = json.load(open(tp, encoding="utf-8"))
    if "results" in t and "passed" in t:
        L = ["# Testbericht Reel-Studio v39", "",
             "Stand: %s UTC · Testlauf automatisiert mit Playwright/Chromium (headless) gegen `studio/reel-studio-v39.html` (lokale Datei) · %d Prüfungen, %d bestanden, %d fehlgeschlagen · Laufzeit %d s." % (t["stand"][:16].replace("T", " "), len(t["results"]), t["passed"], t["failed"], t["seconds"]), "",
             "Testdaten: synthetische, sprachähnliche Audiodatei `tests/vo_test.wav` (20,04 s) und daraus erzeugte `tests/vo_test.mp3`. **Eine echte ElevenLabs-Aufnahme lag auch in dieser Sitzung nicht vor** (kein Konto, keine Kosten ohne Freigabe) – Audio-Analyse und Untertitel-Ausrichtung wurden mit dem Testsignal geprüft; die Qualität der Ausrichtung auf echte Stimme ist damit **nicht** nachgewiesen und bleibt im Studio je Zeile korrigierbar. Die v3-Prüfungen T20–T24 sind neu; T01–T19 sind die v38-Prüfungen gegen die neue Fassung (Regression).", "",
             "| Nr | Prüfung | Ergebnis | Detail |", "|---|---|---|---|"]
        for x in t["results"]: L.append("| %s | %s | %s | %s |" % (x["id"], x["name"], "✅ bestanden" if x["ok"] else "❌ fehlgeschlagen", x["detail"].replace("|", "/")[:200]))
        L += ["", "## Zuordnung zu den geforderten Tests", "", "| Gefordert | Prüfungen |", "|---|---|",
              "| Import | T02, T02b, T15b, T16, T16b |", "| Speicherung | T13, T16b, T21b |", "| Navigation | T02, T17, T18, T20 |", "| Vorschau | T05, T22 (Hook-Overlay in Kopfzeile/Vorschau) |", "| Hook-Bewertungen | T04, T04b, T22 |",
              "| Audio-Upload | T09, T09b, T10 |", "| Untertitel | T11, T12, T12b, T14c |", "| Export | T14, T14b, T14c, T14d, T24 |", "| Plan v3 (Strukturen, Längen, Themenwelten, Schlüsselaufnahmen) | T21, T23 |", "",
              "## Nicht getestet (ehrlich)", "", "- Echte ElevenLabs-Audiodatei (Stimme Mert_V2) – nur synthetisches Testsignal.", "- Browser außer Chromium (Safari/iOS, Firefox) – nicht in dieser Umgebung.", "- Veröffentlichung auf Instagram/TikTok (ausdrücklich nicht Teil des Auftrags).", "- Download/Lizenzierung echter Stock-Clips (keine Käufe ohne Freigabe).", "",
              "## Wiederholen", "", "```", "cd haydi-weg-reels/tests && node studio.test.js ../studio/reel-studio-v39.html", "```"]
        open(OUT + "13_TESTBERICHT.md", "w", encoding="utf-8").write("\n".join(L))
print("Dokumente v3 geschrieben. Ø v2 %.2f → v3 %.2f · Längen %d–%d s · KS %s · Hotels %d" % (avg2, avg3, min(L3), max(L3), dict(KSC), len(hotels)))

# ------------------------------------------------------------ 12 Offene Punkte (v3)
nf = [(r, k) for r in R3 for k in r["key_shots"] if k["status"] == "nicht gefunden"]
uk = [(r, k) for r in R3 for k in r["key_shots"] if k["status"] == "verfügbar, ungeprüft"]
miss = [(r, st) for r in R3 for st in r["stock"] if st["missing"]]
L = ["# Offene Punkte (ehrlich, Stand %s · Fassung v3)" % STAND, "",
     "## A Entscheidungen des Auftraggebers", "",
     "1. **Startdatum:** Reel 01 war für den 09.11. geplant – Kalender beibehalten und Reels 01–03 nachproduzieren (Empfehlung, `17_PRODUKTIONSPRIORITAETEN_1-12.md`) oder alles um eine Woche schieben?",
     "2. **Studio-Artefakt:** v39 wurde **in das v38-Artefakt** (https://claude.ai/artifact/8QEHxEEQYiNQizX9tXVzDz, privat, diese Übergabe) eingespielt; das ursprüngliche v37-Artefakt blieb unverändert. Soll v39 das v37-Artefakt ersetzen? Dann bitte bestätigen (Clips/Audio/Häkchen liegen im Browser je Artefakt-Adresse; Studio-Zustand als JSON sichern und wiederherstellen).",
     "3. **Freitagsserie heißt „Reisewissen“** (ohne „in 30 Sekunden“), weil die Längen jetzt 22–42 s betragen. Rückbenennung ist ein Eintrag in `SERIE` (kalender.py) bzw. `HW.SERIES` im Studio.",
     "4. **Sechs Themen ersetzt** (03, 12, 20, 24, 27, 36) und zwölf radikal umgebaut – Begründungen in `15_UPGRADE_AENDERUNGEN_ALT_NEU.md`. Einspruch gegen einen Tausch → Reserveliste `01_THEMENBEWERTUNG_60plus.md`.",
     "5. **Posting-Uhrzeiten** weiterhin nicht festgelegt (Vorschlag 18:00 Uhr, Test 12:00 in Woche 7–8).",
     "6. **Datei „haydi-weg Reel-Studio_Final(1).html“** lag nicht vor; Basis des Upgrades ist das v38 dieser Übergabe (auf byteidentischem v37). Falls „Final(1)“ eine andere Fassung ist: hochladen – `v39_patch.js` ist auf jede v37/v38-Fassung übertragbar.", "",
     "## B Material (vor Produktion)", "",
     "7. **Prüfstand der Schlüsselaufnahmen:** %d gefunden · %d verfügbar, ungeprüft · %d nicht gefunden (von 117). „Gefunden“ = Treffer mit passendem Titel/ID auf der Suchergebnisseite (Pexels/Envato) am %s; Detailseiten (Lizenztext, Urheber, Personen, exakter Ort) waren nicht erreichbar → vor jedem Download prüfen, Envato-Lizenz je Download registrieren." % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"], STAND),
     "8. **Nicht gefundene Schlüsselaufnahmen (Umbau im Plan):**"] + ["   - %s %s – %s: %s → %s" % (r["id"], r["title"], k["role"], k["motif"], k["note"]) for r, k in nf] + [
     "9. **Verfügbar, aber ungeprüft:**"] + ["   - %s – %s: %s (%s %s)%s" % (r["id"], k["role"], k["motif"], k["source"], k["ref"], (" – " + k["note"]) if k["note"] else "") for r, k in uk] + [
     "10. **Fehlende Zusatzclips (nicht Schlüsselaufnahmen):**"] + ["   - %s – %s → %s" % (r["id"], st["shot"], st["alternative"]) for r, st in miss] + [
     "11. **Historische Fotos** (Çırağan-Ruine/Şeref-Stadion, Old Cataract um 1900, Schneefernerhaus-Hotelzeit, Matera 1950er, Belvédère mit Gletscher, Club Med 1950, Adlon vor 1945, Meteora-Netz, Bad Gastein Leerstand) nur mit geklärter Lizenz (Wikimedia Commons/Public Domain prüfen); bis dahin gekennzeichnete Grafik.",
     "12. Budget: keine Käufe ohne Freigabe; Envato-Abo-Downloads zählen nicht als Zusatzkosten, Einzelkäufe (z. B. Pond5/Shutterstock) max. 50 €/Monat nach Freigabe.", "",
     "## C Fakten (vor Posting)", "",
     "13. Alle „Vor Posting prüfen“-Punkte je Reel (Studio: Qualitäts-Studio, Checkliste mit Freigabe-Sperre). Datumsabhängig: Venedig-Eintritt 2027, Pragser-Wildsee-Regel 2026/27, Navagio-Zugang, Seceda-Drehkreuz 2027, Kappadokien-Flaggenregel, Benagil-Regeln, Maya-Bay-Zeitfenster.",
     "14. Offene Prüfpunkte je Reel (aus den Paketen):"] + ["   - %s: %s" % (r["id"], " · ".join(r["facts"]["to_check"])) for r in R3 if r["facts"]["to_check"]] + [
     "15. AA-Sicherheitslage am Vortag für Ägypten (12, 25), Marokko (23), Türkei (01, 03, 08, 15, 26, 33), Thailand (29).", "",
     "## D Technik", "",
     "16. **Echte ElevenLabs-Audiodatei** lag nicht vor; Audio-Analyse und Sync mit synthetischer Sprach-WAV/MP3 getestet (T09–T12). Am ersten echten Reel Silben-Erkennung prüfen; bei Abweichung ElevenLabs-Speech-to-Text-JSON importieren.",
     "17. Video-Export (WebCodecs/MediaRecorder), Cover-PNG, KI-Produktionsplan und KI-Bildprüfung nicht automatisiert getestet (headless ohne GPU bzw. nur im Claude-Viewer); Code aus v37 unverändert.",
     "18. Safari/Firefox nicht getestet (nur Chromium 1440 px / 390 px).",
     "19. Cloud-Sync (`db`) des Artefakts: Zustand wird ab dem ersten Klick gespeichert; nach dem v39-Update bleiben lokale Daten (localStorage/IndexedDB) erhalten, weil die Adresse gleich bleibt – Funktionsprüfung im Viewer offen.", "",
     "## E Dokumente / Quellen", "",
     "20. Frühere Chat-Verläufe und Google-Drive-Dateien waren nicht zugänglich; ausgewertet wurden nur die in `00_PROJEKTGRUNDLAGE.md` gelisteten Projektdateien und die protokollierten Web-Recherchen (Quellen je Reel in `07_STOCK_QUELLEN.md` und in den Paketen).",
     "21. Die 51 Specials wurden nicht bewertet oder verändert (nicht Teil des Auftrags)."]
open(OUT + "12_OFFENE_PUNKTE.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 11 Änderungsprotokoll: Abschnitt v2 → v3 anhängen (idempotent)
p11 = OUT + "11_AENDERUNGSPROTOKOLL.md"; s11 = open(p11, encoding="utf-8").read()
mark = "## 4 Content-Upgrade v2 → v3"
s11 = s11.split(mark)[0].rstrip() + "\n\n" + "\n".join([mark + " (09.11.2026, zweiter Durchgang)", "",
     "Vollständige Liste: `15_UPGRADE_AENDERUNGEN_ALT_NEU.md`. Backups vor der Änderung: `backup/reel-studio-v38-vor-upgrade.html`, `backup/reels_hauptplan_v2-vor-upgrade.json`. Die 51 Specials blieben unverändert.", "",
     "| Bereich | v2 | v3 |", "|---|---|---|",
     "| Themen | 39 (6 gegenüber 06.11. ersetzt) | %d weitere ersetzt, %d radikal umgebaut, %d behalten und neu geschrieben |" % (dec["ERSETZT"], dec["RADIKAL VERBESSERN"], dec["BEHALTEN"]),
     "| Hooks | 195, Satz + Bild | 195 neu: Bild + Satz + Overlay + Frage, 5 neue Typen, Floskel-Lint |",
     "| Struktur | ein Bogen | A–E, nie zweimal hintereinander |",
     "| Längen | %d–%d s | %d–%d s |" % (min(L2), max(L2), min(L3), max(L3)),
     "| Material | Stockliste | + 3 Schlüsselaufnahmen je Reel mit Recherche-Status (✅ %d · 🟡 %d · ❌ %d) |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"]),
     "| Themenwelten | Cluster | 4 Themenwelten (Endkarte, Studio-Filter) |",
     "| Serie Fr | „Reisewissen in 30 Sekunden“ | „Reisewissen“ |",
     "| Scorecard | Ø %.2f | Ø %.2f (streng, ≥ 2 Runden) |" % (avg2, avg3),
     "| Studio | v38 | v39: Themenwelt-Filter, Struktur in Liste/Kopf, Schlüsselaufnahmen-Tabelle mit Status (Content- und Qualitäts-Studio), Hook-Tabelle mit Overlay/Frage und „Overlay“-Übernahme, Hooks-CSV mit 4 Komponenten, Import liest v3 und v2, Zustand-Schema v39 |",
     "| Daten | reels_hauptplan_v2.json | reels_hauptplan_v3.json (+ Import-Tabellen v3 CSV/JSON/XLSX mit Tabs Hooks, Cover, Schlüsselaufnahmen, Schnittpläne, Stock, Änderungen) |",
     "| Tests | 31 Prüfungen | 31 Regression + 6 neue (T20–T24) |"]) + "\n"
open(p11, "w", encoding="utf-8").write(s11)

# ------------------------------------------------------------ README
L = ["# haydi-weg Reel-Produktion · Hauptplan 09.11.2026–05.02.2027 · Fassung v3 (Content-Upgrade)", "",
     "Übergabe vom 09.11.2026 (autonomer Lauf, zwei Durchgänge: Grundlieferung v2, dann Content-Upgrade v3). Reihenfolge zum Lesen:", "",
     "| Nr | Datei | Inhalt |", "|---|---|---|",
     "| 00 | `00_PROJEKTGRUNDLAGE.md` | Ausgangsplan, Quelleninventar (zugänglich / nicht zugänglich), Entscheidungen, Backups |",
     "| 01 | `01_THEMENBEWERTUNG_60plus.md/.csv` | 73 Kandidaten bewertet (Grundlieferung), Reserveliste |",
     "| 02 | `02_MASTERPLAN_FINAL.md` | **v3-Masterplan**: Strategie, Content-Identität/Follow-Strategie, Kalender, 39 Steckbriefe |",
     "| 03 | `03_SPRECHERTEXTE/` | 39 ElevenLabs-Texte v3 (gesamt + je Szene + Endkarte) |",
     "| 04 | `04_CAPCUT_SCHNITTPLAENE/` | 39 Schnittpläne (Schlüsselaufnahmen, 16 Felder + Rolle, Timecodes vorläufig) MD + CSV |",
     "| 05 | `05_HOOKS_195.csv/.md` | 195 neue Hooks: Bild · Satz · Overlay · Frage, 7 Kriterien, Sieger begründet |",
     "| 06 | `06_COVER_117.csv/.md` | 117 Cover-Konzepte |",
     "| 07 | `07_STOCK_QUELLEN.csv/.md`, `07_SCHLUESSELAUFNAHMEN_117.csv` | Material- und Quellencheck mit ehrlichem Status (gefunden / verfügbar, ungeprüft / nicht gefunden) |",
     "| 08 | `08_KALENDER_13_WOCHEN.csv/.md` | 13-Wochen-Kalender v3 (Themenwelt, Struktur, Länge, Material, Vortags-Prüfung) |",
     "| 09 | `09_KPI_TESTSTRATEGIE.md` | KPI-Dashboard-Definition, Reviews, Testplan |",
     "| 10 | `10_QUALITAET_SCORECARDS.md/.csv` | Gewichtete Scorecards v3, Verbesserungsprotokoll |",
     "| 11 | `11_AENDERUNGSPROTOKOLL.md` | Änderungen 06.11. → v2 → v3, Studio v37 → v38 → v39 |",
     "| 12 | `12_OFFENE_PUNKTE.md` | Ehrliche Liste offener Punkte |",
     "| 13 | `13_TESTBERICHT.md` | Automatisierte Tests (Playwright) gegen Studio v39 |",
     "| 14 | `14_BEDIENUNGSANLEITUNG.md` | Reel-Studio v39 bedienen, Import/Export, Grenzen |",
     "| 15 | `15_UPGRADE_AENDERUNGEN_ALT_NEU.md` | **Änderungsliste ALT → NEU** je Reel und Plan-Ebene |",
     "| 16 | `16_QUALITAETSBEWERTUNG_KRITISCH.md` | **Kritische Qualitätsbewertung** (streng, mit Rest-Schwächen) |",
     "| 17 | `17_PRODUKTIONSPRIORITAETEN_1-12.md` | **Produktionsprioritäten für die ersten 12 Reels** |",
     "| – | `studio/reel-studio-v39.html` | Reel-Studio v39 (lokal nutzbar; Artefakt-Link in 14) |",
     "| – | `data/reels_hauptplan_v3.json` | Vollständige Daten der 39 Reels v3 (Studio-Import) |",
     "| – | `data/02_haydi-weg_ReelStudio_Import_v3.xlsx/.csv/.json` | Importtabellen v3 |",
     "| – | `data/reels_specials_v37.json` | Die 51 Specials aus v37 (Sicherung, unverändert) |",
     "| – | `backup/` | v37-Original, v38 und v2-Daten vor dem Upgrade, Textfassungen der Quelldokumente |",
     "| – | `tests/` | Testsuite v39, Testergebnis, Test-Audio, Screenshots |",
     "| – | `haydi-weg_reel_produktion_v3_2026-11-09.zip` | Alles als ZIP |", "",
     "Regeln, die überall gelten: keine Verkaufs-CTAs bis Ende 2026, keine Personen vor der Kamera, nur lizenziertes Fremdmaterial (Budget ≤ 50 €/Monat, keine Käufe ohne Freigabe), Timecodes ohne Audio sind vorläufig, Scores sind Einschätzungen und ersetzen keine Prüfung."]
open(OUT + "README.md", "w", encoding="utf-8").write("\n".join(L))
print("12/11/README aktualisiert")
