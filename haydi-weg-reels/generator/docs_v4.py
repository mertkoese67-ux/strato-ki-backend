# -*- coding: utf-8 -*-
"""Erzeugt die v4-Lieferdokumente aus data/reels_hauptplan_v4.json (+ v3-Backup für ALT→NEU-Vergleich)."""
import json, csv, os, statistics, datetime
from collections import Counter
from kalender import SERIE_HINWEIS, STRUKTUR, THEMENWELTEN
OUT = "/home/user/strato-ki-backend/haydi-weg-reels/"
SP = os.path.dirname(os.path.abspath(__file__)) + "/"
v3 = json.load(open(OUT + "data/reels_hauptplan_v4.json", encoding="utf-8")); R3 = v3["reels"]
v2 = json.load(open(OUT + "backup/reels_hauptplan_v3-vor-hotelaudit.json", encoding="utf-8")); R2 = {r["id"]: r for r in v2["reels"]}
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
L = ["# haydi-weg Reel-Masterplan 09.11.2026 – 05.02.2027 · Fassung v4 (Final Ultra-Premium Content Audit, Stand %s)" % STAND, "",
     "Basis: Masterplan 06.11. → v2 → v3 (09.11.) → **v4 (10.11., Final-Audit)**: %d Reels durch DACH-relevante Hotel-/Resort-Reels ersetzt, %d behalten – alle 39 mit den fünf Audit-Hook-Typen (Visueller Schock · Neugierlücke · Überraschende Behauptung · Erwartung gegen Realität · Emotionaler WOW-Moment), Audit-Gewichten (Hook 25 · Visuell 25 · Story 20 · Share/Follow 15 · DACH 5 · Fakten 10), Schlüsselaufnahmen mit Materialstatus und Produktionsbereitschaft. Hotel-Audit: `19_FINAL_AUDIT_HOTELS.md` (99 Kandidaten, Dubletten-Check). Alle Details je Reel: `data/reels_hauptplan_v4.json` (im Reel-Studio eingebettet und importierbar). Die 51 Specials sind nicht Teil dieses Plans und blieben unverändert." % (dec.get("ERSETZT (Hotel)", 0), dec.get("BEHALTEN", 0)), "",
     "## 1 Strategie (verbindlich)", "",
     "- Unterhaltsamer DACH-Reiseentdeckungskanal; Prioritäten: Reichweite bei Nicht-Followern, erste Sekunden, Wiedergabedauer, Shares/Saves, Profilbesuche, Follower je 1.000 Views, Premium-Marke, Vertrauen.",
     "- Bis 31.12.2026 keine Verkaufs-CTAs; keine Personen vor der Kamera; eigene Antalya-Hotelvideos bleiben Specials.",
     "- Nur korrekt zugeordnetes, rechtmäßig nutzbares Fremdmaterial (Envato Elements bevorzugt, Pexels/Pixabay ergänzend, Budget ≤ 50 €/Monat, keine Käufe ohne Freigabe). Keine erfundenen Clipverfügbarkeiten, keine falschen Hotelaufnahmen: Ein Hotel-Reel ohne nachgewiesene Schlüsselaufnahme des Hotels ist nicht produktionsbereit (Status im Studio).",
     "- Hotels nur, wenn sie für D/A/CH-Urlauber tatsächlich relevant sind (Veranstalter, Direktflüge, Nachfrage); keine bereits behandelten Häuser (Regnum The Crown ausgeschlossen, Dubletten-Check in `19_FINAL_AUDIT_HOTELS.md`); Storytelling statt Hotelwerbung, keine Preise.",
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
      "## 3 Was sich gegenüber v3 geändert hat", "", "| Bereich | v3 (Content-Upgrade) | v4 (Final-Audit) |", "|---|---|---|",
      "| Themen | 39 (6 ersetzt, 12 radikal) | %d durch Hotel-/Resort-Reels ersetzt (%s) – Details `18_FINAL_AUDIT_ALT_NEU.md` |" % (dec.get("ERSETZT (Hotel)", 0), ", ".join(r["id"] for r in R3 if r["decision_v3"] == "ERSETZT (Hotel)")),
      "| Hooks | 5 Typen (… Emotionaler Konflikt …) | 5 Audit-Typen: Visueller Schock · Neugierlücke · Überraschende Behauptung · Erwartung gegen Realität · Emotionaler WOW-Moment; Bild + Satz + Overlay + Frage; Floskel- und Werbesprache-Sperre |",
      "| Gewichte | 25/20/20/15/10/10 | Final-Audit 25/25/20/15/5/10 (Visuell rauf, DACH runter) |",
      "| Längen | 24–46 s | %d–%d s |" % (min(L3), max(L3)),
      "| Material | 3 Schlüsselaufnahmen (89/18/10) | 3 Schlüsselaufnahmen je Reel: ✅ %d · 🟡 %d · ❌ %d; Hotel-Reels ohne Hotelnachweis = „nicht produktionsbereit“ (%d Reels) |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"], sum(1 for r in R3 if "nicht produktionsbereit" in r["approval"]["status"])),
      "| Hotels | 16 konkret, überwiegend Legenden | %d konkret benannt, davon %d Hotel-/Resort-Reels (Flag) – alle DACH-geprüft, Dubletten-Check gegen Specials/Oktober/Plan |" % (len(hotels), sum(1 for r in R3 if r.get("hotel_reel"))),
      "| Qualität | Ø %.2f (alte Gewichte) | Ø %.2f mit Audit-Gewichten, %d Reels ≥ 9,0 – streng, Begründungen in `20_FINAL_AUDIT_BEWERTUNG.md` |" % (avg2, avg3, sum(1 for r in R3 if r["scorecard"]["total"] >= 9)),
      "| Studio | v39 | unverändert (Oberfläche/Funktionen), nur Daten v4 eingespielt; Scorecard-Gewichte werden aus den Daten gelesen |", "",
      "## 4 Kalender und Reel-Übersicht", "", "| Nr | Datum | Serie | Titel | Themenwelt | Str. | Länge | Sieger-Hook (gesprochen) | Material | QS |", "|---|---|---|---|---|---|---|---|---|---|"]
for r in R3:
    L.append("| %02d | %s %s | %s #%d | %s | %s | %s | %.0f s | %s | %s | %.2f |" % (r["nr"], r["weekday"], r["date_de"], r["series"], r["episode"], r["title"], r["themenwelt"], r["structure"], r["cut"]["total_sec"], win(r)["spoken"], ksl(r), r["scorecard"]["total"]))
L += ["", "Material-Legende: ✅ gefunden (Treffer auf Suchseite gelistet) · 🟡 verfügbar, ungeprüft · ❌ nicht gefunden (Umbau/Alternative im Plan) – Reihenfolge Scroll-Stop / Story / Reveal.", "", "## 5 Reel-Steckbriefe", ""]
for r in R3:
    w = win(r); r2 = R2[r["id"]]
    L += ["### %s · %s %s · %s #%d · %s" % (r["id"], r["weekday"], r["date_de"], r["series_name"], r["episode"], r["title"]), "",
          "**Ort:** %s · **Themenwelt:** %s · **Struktur:** %s – %s · **v4:** %s%s · **Länge:** ca. %d s (vorläufig %.1f s) · **QS (Audit):** %.2f (v3: %.2f) · **Freigabe:** %s" % (r["place"], r["themenwelt"], r["structure"], r["structure_name"], r["decision_v3"], (" (vorher: „%s“)" % r["title_v2"]) if r["title_v2"] != r["title"] else "", r["target_sec"], r["cut"]["total_sec"], r["scorecard"]["total"], r2["scorecard"]["total"], r["approval"]["status"]), "",
          ("**DACH-Relevanz:** %s · **Dubletten:** %s" % (r.get("dach_begruendung", ""), r.get("dubletten_status", ""))) if r.get("hotel_reel") else "", "",
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

# ------------------------------------------------------------ 18 Änderungsliste ALT → NEU (v3 → v4)
dec4 = Counter(r["decision_v3"] for r in R3)
hot_new = [r for r in R3 if r["decision_v3"] == "ERSETZT (Hotel)"]
nready = [r for r in R3 if "nicht produktionsbereit" in r["approval"]["status"]]
L = ["# Final-Audit: Änderungsliste ALT → NEU (v3 Content-Upgrade → v4 Final-Audit, Stand %s)" % STAND, "",
     "Ausgangslage v3: Ø %.2f/10 (alte Gewichte 25/20/20/15/10/10), Längen %d–%d s, 16 Hotels konkret (überwiegend Legenden), Schlüsselaufnahmen 89/18/10. Auftrag v4: nur DACH-relevante Hotels/Resorts mit visuellem WOW, keine bereits verwendeten Häuser (Regnum The Crown ausgeschlossen), Hooks mit „Emotionaler WOW-Moment“, Audit-Gewichte 25/25/20/15/5/10, Hotel ohne Footage-Nachweis = nicht produktionsbereit. Studio-Oberfläche und Specials unverändert." % (avg2, min(L2), max(L2)), "",
     "## 1 Plan-Ebene", "", "| # | ALT (v3) | NEU (v4) | Grund |", "|---|---|---|---|",
     "| A1 | 39 Themen (6 ersetzt, 12 radikal) | %d Themen durch Hotel-/Resort-Reels ersetzt (%s), %d behalten und auf v4 gehoben | DACH-Hotel-Audit mit 99 Kandidaten (`19_FINAL_AUDIT_HOTELS.md`) |" % (len(hot_new), ", ".join(r["id"] for r in hot_new), dec4.get("BEHALTEN", 0)),
     "| A2 | Hook-Typ 4 „Emotionaler Konflikt“, Typ 5 „Erwartung gegen Realität“ | Typ 4 „Erwartung gegen Realität“, Typ 5 „Emotionaler WOW-Moment“ – 195 Hooks neu bewertet (Satz + erstes Bild + Overlay gemeinsam) | Auftrag |",
     "| A3 | Gewichte 25/20/20/15/10/10 | 25/25/20/15/5/10 (Visuell rauf, DACH runter); Studio liest die Gewichte aus den Daten | Final-Audit |",
     "| A4 | Hotel-Reels ohne Flag | `hotel_reel` + DACH-Begründung + Dubletten-Status je Hotel-Reel; %d Reels mit konkretem Hotel, davon %d Hotel-/Resort-Reels | Nachvollziehbarkeit |" % (len(hotels), sum(1 for r in R3 if r.get("hotel_reel"))),
     "| A5 | Schlüsselaufnahmen mit Status | zusätzlich Produktionsbereitschaft: Scroll-Stop oder Reveal „nicht gefunden“ = „Material offen – nicht produktionsbereit“ (%s) | keine falschen Hotelaufnahmen, kein Reveal ohne Bild |" % (", ".join(r["id"] for r in nready) or "keins"),
     "| A6 | Werbesprache nicht geprüft | Lint sperrt Werbesprache („exklusiv“, „verwöhnt“, „buchbar“ …) und Preise | Storytelling statt Hotelwerbung |",
     "| A7 | Themenwelt „Hotel-Legenden“ = historische Hotels | „Hotel-Legenden“ = Hotels, die man gesehen haben muss (Pools, Architektur, Lagunen, Legenden) – Filter im Studio unverändert | Content-Identität |",
     "| A8 | Scorecard Ø %.2f | Ø %.2f (Audit-Gewichte), %d Reels ≥ 9,0 | streng, keine künstlichen Neunen |" % (avg2, avg3, sum(1 for r in R3 if r["scorecard"]["total"] >= 9)), "",
     "## 2 Reel-Ebene", "", "| Nr | Datum | v4 | ALT (v3) | NEU (v4) | Hotel | Str. | Länge v3 → v4 | QS v3 → v4 (Audit) | Freigabe | Was konkret anders ist |", "|---|---|---|---|---|---|---|---|---|---|---|"]
for r in R3:
    r2 = R2[r["id"]]
    L.append("| %s | %s | **%s** | %s | %s | %s | %s | %.0f → %.0f s | %.2f → %.2f | %s | %s |" % (r["id"], r["date_de"], r["decision_v3"], r2["title"], r["title"], r.get("hotel") or "–", r["structure"], r2["cut"]["total_sec"], r["cut"]["total_sec"], r2["scorecard"]["total"], r["scorecard"]["total"], "⚠ nicht produktionsbereit" if "nicht produktionsbereit" in r["approval"]["status"] else "Vorprüfung", " · ".join(r["changelog_vs_plan"][:4])))
L += ["", "## 3 Ersetzte Themen und warum", "", "| Nr | Thema v3 | Entscheidung | Neues Reel | Begründung |", "|---|---|---|---|---|"]
for r in hot_new: L.append("| %s | %s | %s | %s | %s |" % (r["id"], r["title_v2"], r["decision_v3"], r["title"], r["decision_reason"]))
L += ["", "## 4 Was NICHT geändert wurde", "", "- Die 51 Specials (v37-Daten), die Studio-Oberfläche und alle Funktionen (nur Daten eingespielt; Gewichte werden aus den Daten gelesen).", "- Wochentage, 13 Wochen, Postingdaten, Serien (Mo Fakt oder Fake? · Mi Was dir keiner sagt · Fr Reisewissen), Strukturen A–E, Themenwelten.", "- Regeln: keine Verkaufs-CTAs bis Ende 2026, keine Preise, keine Personen vor der Kamera, Budget ≤ 50 €/Monat ohne Freigabe, Untertitel-Stil, Timecodes vorläufig bis Audio vorliegt."]
open(OUT + "18_FINAL_AUDIT_ALT_NEU.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 21 Top-12 für die erste Produktion
def ready_score(r):
    ks = {k["role"]: k["status"] for k in r["key_shots"]}
    pen = sum({"gefunden": 0, "verfügbar, ungeprüft": 0.15, "nicht gefunden": 0.6}[ks[k]] for k in ("Scroll-Stop", "Story", "Reveal"))
    if "nicht produktionsbereit" in r["approval"]["status"]: pen += 2
    return r["scorecard"]["total"] - pen
top = sorted(R3, key=lambda r: (-ready_score(r), r["nr"]))[:12]
L = ["# Die zwölf stärksten Reels für die erste Produktion (Final-Audit v4)", "",
     "Auswahl = Audit-Score (Hook 25 · Visuell 25 · Story 20 · Share/Follow 15 · DACH 5 · Fakten 10) **minus** Materialrisiko (Schlüsselaufnahme ungeprüft −0,15, nicht gefunden −0,6, Hotel ohne Nachweis −2). Nur Reels, deren Material nach Prüfung der Detailseiten sofort produzierbar ist. Postingdaten bleiben wie im Kalender; die zwölf werden zuerst produziert, die übrigen folgen in Kalenderreihenfolge.", "",
     "| Rang | Reel | Posting | Titel | Themenwelt | Str. | Audit-QS | Material (SS/Story/Reveal) | Freigabe | Warum zuerst |", "|---|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(top, 1):
    L.append("| %d | %s | %s %s | %s | %s | %s | **%.2f** | %s | %s | %s |" % (i, r["id"], r["weekday"], r["date_de"], r["title"], r["themenwelt"], r["structure"], r["scorecard"]["total"], ksl(r), r["approval"]["status"].split(" –")[0], r["decision_reason"].split(";")[0][:140]))
L += ["", "## Je Reel: Startpaket", ""]
for i, r in enumerate(top, 1):
    w = win(r)
    L += ["### %d · %s · %s (%s %s)" % (i, r["id"], r["title"], r["weekday"], r["date_de"]), "",
          "- **Erstes Bild (ohne Ton):** %s · Overlay: %s · gesprochen: „%s“" % (w["first_frame"], w["overlay"].replace("*", ""), w["spoken"]),
          "- **Schlüsselaufnahmen:** " + " · ".join("%s – %s %s (**%s**%s)" % (k["role"], k["source"], k["ref"], k["status"], (": " + k["note"]) if k["note"] else "") for k in r["key_shots"]),
          "- **Hotel/Resort:** %s%s" % (r.get("hotel") or "–", (" · DACH: " + r.get("dach_begruendung", "")) if r.get("hotel_reel") else ""),
          "- **Fakten am Vortag:** " + (" · ".join(r["facts"]["to_check"]) or "keine offenen"),
          "- **Audio:** `03_SPRECHERTEXTE/%s*.txt` (%d Wörter, ca. %.0f s) → ElevenLabs Mert_V2 → Studio: Zeiten aus Audio, Untertitel prüfen, CapCut-Export" % (r["id"], r["vo"]["words"], r["vo"]["est_sec"]), ""]
rest = [r for r in R3 if r not in top]
L += ["## Nicht in den Top 12 – und warum", "", "| Reel | Titel | Audit-QS | Material | Grund |", "|---|---|---|---|---|"] + ["| %s | %s | %.2f | %s | %s |" % (r["id"], r["title"], r["scorecard"]["total"], ksl(r), ("Schlüsselaufnahme (Scroll-Stop/Reveal) nicht gefunden – erst mit Pressematerial/Lizenzfoto" if "nicht produktionsbereit" in r["approval"]["status"] else "Schlüsselaufnahme nicht gefunden/ungeprüft" if any(k["status"] != "gefunden" for k in r["key_shots"]) else "Score unter den Top 12")) for r in rest] + ["",
     "## Produktionsstandard", "", "1. Detailseiten der Schlüsselaufnahmen öffnen (Ort, Urheber, Personen, Lizenz), Envato-Lizenz je Download registrieren; Hotel-Clips nur mit Hotelname im Titel oder Pressefreigabe.", "2. Sprechtext unverändert in ElevenLabs (Eleven v3, Mert_V2), MP3 ins Studio → „Szenen & Untertitel aus Audio neu berechnen“ → Zeilen prüfen → SRT.", "3. CapCut nach Schnittplan (9:16, 30 fps), Hook ohne Untertitel, Logo ab Sekunde 3, Endkarte mit Themenwelt; Export ohne Text, Overlay/Untertitel im Studio.", "4. Freigabe-Gate im Studio (Fakten, Material inkl. Schlüsselaufnahmen, Vortag, Hook-QA). Keine Preise, kein Verkaufs-CTA."]
open(OUT + "21_TOP12_ERSTE_PRODUKTION.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 20 Final-Audit-Bewertung (streng)
L = ["# Final-Audit: Qualitätsbewertung des v4-Plans (Stand %s)" % STAND, "",
     "Gewichtung: Hook/erster Frame 25 % · Visuelle Faszination 25 % · Storytelling 20 % · Share-/Follow-Potenzial 15 % · DACH-Relevanz 5 % · Fakten/Umsetzbarkeit 10 %. Noten sind Einschätzungen der Redaktion nach Überarbeitungsrunden – **keine Messwerte, keine Erfolgsversprechen, keine künstlichen Neunen**. Ein Hotel ohne nachgewiesenes Schlüsselfootage ist nicht produktionsbereit, unabhängig vom Score.", "",
     "## 1 Gesamtbild", "", "| Kennzahl | v3 | v4 |", "|---|---|---|",
     "| Ø Scorecard | %.2f (alte Gewichte) | **%.2f** (Audit-Gewichte) |" % (avg2, avg3),
     "| Reels ≥ 9,0 | %d | %d |" % (sum(1 for r in R2.values() if r["scorecard"]["total"] >= 9), sum(1 for r in R3 if r["scorecard"]["total"] >= 9)),
     "| Reels < 8,5 | %d | %d |" % (sum(1 for r in R2.values() if r["scorecard"]["total"] < 8.5), sum(1 for r in R3 if r["scorecard"]["total"] < 8.5)),
     "| Längen | %d–%d s (sd %.1f) | %d–%d s (sd %.1f) |" % (min(L2), max(L2), statistics.pstdev(L2), min(L3), max(L3), statistics.pstdev(L3)),
     "| Schlüsselaufnahmen gefunden / ungeprüft / nicht gefunden | 89 / 18 / 10 | %d / %d / %d |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"]),
     "| Hotel-/Resort-Reels (Flag) | – | %d (konkrete Hotels gesamt %d) |" % (sum(1 for r in R3 if r.get("hotel_reel")), len(hotels)),
     "| Nicht produktionsbereit (Scroll-Stop oder Reveal nicht gefunden) | – | %d (%s) |" % (len(nready), ", ".join(r["id"] for r in nready) or "–"), "",
     "## 2 Je Reel (streng)", "", "| Reel | Titel | Hook | Vis | Story | Share | DACH | Fakt | **v4** | v3 | Material | Freigabe | Rest-Schwäche (letzte Runde) |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in R3:
    sc = r["scorecard"]["scores"]
    L.append("| %s | %s | %d | %d | %d | %d | %d | %d | **%.2f** | %.2f | %s | %s | %s |" % (r["id"], r["title"], sc["hook"], sc["visual"], sc["story"], sc["share"], sc["dach"], sc["facts"], r["scorecard"]["total"], R2[r["id"]]["scorecard"]["total"], ksl(r), "⚠" if "nicht produktionsbereit" in r["approval"]["status"] else "✓", r["scorecard"]["iterations"][-1][:220]))
low = [r for r in R3 if r["scorecard"]["total"] < 9]
L += ["", "## 3 Reels unter 9,0 – Begründung", ""] + (["- **%s %s (%.2f):** %s" % (r["id"], r["title"], r["scorecard"]["total"], r["scorecard"]["iterations"][-1]) for r in low] or ["- keine"]) + [""]
krit = SP + "kritik_v4.md"
if os.path.exists(krit): L += [open(krit, encoding="utf-8").read()]
open(OUT + "20_FINAL_AUDIT_BEWERTUNG.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 13 Testbericht
tp = OUT + "tests/testergebnis.json"
if os.path.exists(tp):
    t = json.load(open(tp, encoding="utf-8"))
    if "results" in t and "passed" in t:
        L = ["# Testbericht Reel-Studio v39 (Daten v4 · Final-Audit)", "",
             "Stand: %s UTC · Testlauf automatisiert mit Playwright/Chromium (headless) gegen `studio/reel-studio-v39.html` (lokale Datei, Daten v4) · %d Prüfungen, %d bestanden, %d fehlgeschlagen · Laufzeit %d s." % (t["stand"][:16].replace("T", " "), len(t["results"]), t["passed"], t["failed"], t["seconds"]), "",
             "Testdaten: synthetische, sprachähnliche Audiodatei `tests/vo_test.wav` (20,04 s) und `tests/vo_test.mp3`. **Eine echte ElevenLabs-Aufnahme lag nicht vor** – Audio-Analyse und Untertitel-Ausrichtung sind mit dem Testsignal geprüft, nicht mit echter Stimme. T01–T19 = Regression v38, T20–T24 = v39-Felder, T25 = Audit-Gewichte aus den Daten. Oberfläche und Funktionen des Studios wurden im v4-Schritt nicht verändert (nur Daten eingespielt).", "",
             "| Nr | Prüfung | Ergebnis | Detail |", "|---|---|---|---|"]
        for x in t["results"]: L.append("| %s | %s | %s | %s |" % (x["id"], x["name"], "✅ bestanden" if x["ok"] else "❌ fehlgeschlagen", x["detail"].replace("|", "/")[:200]))
        L += ["", "## Zuordnung zu den geforderten Tests", "", "| Gefordert | Prüfungen |", "|---|---|", "| Import | T02, T02b, T15b, T16, T16b |", "| Speicherung | T13, T16b, T21b |", "| Navigation | T02, T17, T18, T20 |", "| Vorschau | T05, T22 |", "| Hook-Bewertungen | T04, T04b, T22 |", "| Audio-Upload | T09, T09b, T10 |", "| Untertitel | T11, T12, T12b, T14c |", "| Export | T14, T14b, T14c, T14d, T24 |", "| Plan v4 | T21, T23, T25 |", "",
              "## Nicht getestet (ehrlich)", "", "- Echte ElevenLabs-Audiodatei (Stimme Mert_V2).", "- Browser außer Chromium.", "- Veröffentlichung auf Instagram/TikTok (nicht Teil des Auftrags).", "- Download/Lizenzierung echter Stock-Clips und Hotel-Pressematerial (keine Käufe ohne Freigabe).", "",
              "## Screenshots", "", "- `tests/v39_content_studio_H03.png`, `tests/v39_schluesselaufnahmen_H03.png`, `tests/v39_hook_studio_H03.png`, `tests/v39_themenwelt_filter.png`, `tests/v39_mobile_390.png` (Fassung v39/v3) · v4-Screenshots: `tests/v4_*.png`", "",
              "## Wiederholen", "", "```", "cd haydi-weg-reels/tests && node studio.test.js ../studio/reel-studio-v39.html", "```"]
        open(OUT + "13_TESTBERICHT.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 12 Offene Punkte (v4)
nf = [(r, k) for r in R3 for k in r["key_shots"] if k["status"] == "nicht gefunden"]
uk = [(r, k) for r in R3 for k in r["key_shots"] if k["status"] == "verfügbar, ungeprüft"]
miss = [(r, st) for r in R3 for st in r["stock"] if st["missing"]]
L = ["# Offene Punkte (ehrlich, Stand %s · Fassung v4 Final-Audit)" % STAND, "",
     "## A Entscheidungen des Auftraggebers", "",
     "1. **Startdatum:** Reel 01 war für den 09.11. geplant – Kalender beibehalten und Reels 01–03 nachproduzieren oder alles um eine Woche schieben? (`21_TOP12_ERSTE_PRODUKTION.md`)",
     "2. **Studio-Artefakt:** Daten v4 wurden in das Artefakt dieser Übergabe (https://claude.ai/artifact/8QEHxEEQYiNQizX9tXVzDz, privat) eingespielt; Oberfläche/Funktionen unverändert, v37-Artefakt unangetastet. Soll es das v37-Artefakt ersetzen?",
     "3. **Pressematerial/Lizenzfotos:** %d Reels haben für Scroll-Stop oder Reveal keinen Stock-Nachweis und sind bis zur Freigabe von Pressematerial bzw. Lizenzfoto „nicht produktionsbereit“ (%s). Anfrage über Veranstalter/Hotelvertrieb bzw. Bildarchiv – oder Tausch gegen Reserve aus `19_FINAL_AUDIT_HOTELS.md`." % (len(nready), ", ".join("%s %s" % (r["id"], r["hotel"] or r["title"]) for r in nready) or "–"),
     "4. **Ersetzte Themen** (%s): Einspruch → Rückkehr zur v3-Fassung ist über `backup/reels_hauptplan_v3-vor-hotelaudit.json` (Studio-Import) jederzeit möglich." % ", ".join(r["id"] for r in hot_new),
     "5. **Posting-Uhrzeiten** weiterhin offen (Vorschlag 18:00 Uhr, Test 12:00 in Woche 7–8).",
     "6. **Datei „haydi-weg Reel-Studio(3).html“** lag nicht vor; Basis war das v39-Studio dieser Übergabe. Falls „(3)“ eine andere Fassung ist: hochladen, Daten v4 lassen sich per Import einspielen.", "",
     "## B Material (vor Produktion)", "",
     "7. **Prüfstand der Schlüsselaufnahmen:** %d gefunden · %d verfügbar, ungeprüft · %d nicht gefunden (von 117). „Gefunden“ = Treffer mit passendem Titel/ID auf der Suchergebnisseite (Pexels/Envato); Detailseiten (Lizenztext, Urheber, Personen, exakter Ort) waren nicht erreichbar → vor jedem Download prüfen, Envato-Lizenz je Download registrieren. Envato-Treffer zeigen ohne Login „currently unavailable“ – Vorschau im Abo prüfen." % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"]),
     "8. **Nicht gefundene Schlüsselaufnahmen (Umbau im Plan):**"] + ["   - %s %s – %s: %s → %s" % (r["id"], r["title"], k["role"], k["motif"], k["note"]) for r, k in nf] + [
     "9. **Verfügbar, aber ungeprüft:**"] + ["   - %s – %s: %s (%s %s)%s" % (r["id"], k["role"], k["motif"], k["source"], k["ref"], (" – " + k["note"]) if k["note"] else "") for r, k in uk] + [
     "10. **Fehlende Zusatzclips:**"] + ["   - %s – %s → %s" % (r["id"], st["shot"], st["alternative"]) for r, st in miss] + [
     "11. **Hotel-Innenaufnahmen** (Cloud-22-Pool, Address-Pool, Emirates-Palace-Innenräume, Hubertus-Glasboden, Cap-Rocat-Suiten, Domes-Villen innen) gibt es nicht als Stock – nur Pressematerial mit schriftlicher Freigabe.",
     "12. Budget: keine Käufe ohne Freigabe; Einzelkäufe max. 50 €/Monat.", "",
     "## C Fakten (vor Posting)", "",
     "13. Alle „Vor Posting prüfen“-Punkte je Reel (Studio-Checkliste mit Freigabe-Sperre); datumsabhängig: Zugangsregeln der Pools (Atlantis The Royal, Address), Dine-Out-Bedingungen Ikos, Manta-Saison Hanifaru, Pragser-Wildsee-Regel, Navagio, Benagil, Maya Bay.",
     "14. Offene Prüfpunkte je Reel:"] + ["   - %s: %s" % (r["id"], " · ".join(r["facts"]["to_check"])) for r in R3 if r["facts"]["to_check"]] + [
     "15. AA-Sicherheitslage am Vortag für Ägypten (12, 25, 32), Marokko (23), Türkei (01, 03, 08, 10, 15, 33), Thailand (29), VAE (07, 19, 26).", "",
     "## D Technik", "",
     "16. Echte ElevenLabs-Audiodatei lag nicht vor (synthetisches Testsignal); Video-Export/Cover-PNG/KI-Funktionen nicht automatisiert getestet; Safari/Firefox nicht getestet.",
     "17. Studio-Code unverändert gegenüber v39; die Scorecard-Gewichte werden aus den eingebetteten Daten gelesen (Fallback: alte Gewichte, falls jemand v3-Daten importiert).", "",
     "## E Dokumente / Quellen", "",
     "18. Frühere Chat-Verläufe, Google-Drive-Dateien und das Live-Konto (Instagram/TikTok) waren nicht einsehbar; der Dubletten-Check beruht auf Specials v37, Oktober-Skripten/Content-Plan und Plan v3 – jeder neue Hotel-Kandidat ist „gegen Live-Konto ungeprüft“.",
     "19. Die 51 Specials wurden nicht bewertet oder verändert."]
open(OUT + "12_OFFENE_PUNKTE.md", "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------ 11 Änderungsprotokoll: Abschnitt v3 → v4 anhängen (idempotent)
p11 = OUT + "11_AENDERUNGSPROTOKOLL.md"; s11 = open(p11, encoding="utf-8").read()
mark = "## 5 Final-Audit v3 → v4"
s11 = s11.split(mark)[0].rstrip() + "\n\n" + "\n".join([mark + " (10.11.2026)", "",
     "Vollständige Liste: `18_FINAL_AUDIT_ALT_NEU.md`; Hotel-Audit: `19_FINAL_AUDIT_HOTELS.md`. Backups vor der Änderung: `backup/reel-studio-v39-vor-hotelaudit.html`, `backup/reels_hauptplan_v3-vor-hotelaudit.json`. Specials, Studio-Oberfläche und -Funktionen unverändert.", "",
     "| Bereich | v3 | v4 |", "|---|---|---|",
     "| Themen | 39 | %d durch DACH-Hotel-/Resort-Reels ersetzt, %d behalten |" % (len(hot_new), dec4.get("BEHALTEN", 0)),
     "| Hooks | Typ 4 Konflikt / Typ 5 Erwartung | Typ 4 Erwartung gegen Realität / Typ 5 Emotionaler WOW-Moment; 195 Hooks neu |",
     "| Gewichte | 25/20/20/15/10/10 | 25/25/20/15/5/10 |",
     "| Hotel-Felder | – | hotel_reel, DACH-Begründung, Dubletten-Status, Produktionsbereitschaft |",
     "| Material | 89/18/10 | %d/%d/%d; %d Hotel-Reels ohne Hotelnachweis (nicht produktionsbereit) |" % (KSC["gefunden"], KSC["verfügbar, ungeprüft"], KSC["nicht gefunden"], len(nready)),
     "| Scorecard | Ø %.2f | Ø %.2f |" % (avg2, avg3),
     "| Studio | v39 | v39 mit Daten v4 (Beschriftung „Plan v4“, Gewichte aus Daten) |",
     "| Daten | reels_hauptplan_v3.json | reels_hauptplan_v4.json + Import-Tabellen v4 |"]) + "\n"
open(p11, "w", encoding="utf-8").write(s11)

# ------------------------------------------------------------ README
L = ["# haydi-weg Reel-Produktion · Hauptplan 09.11.2026–05.02.2027 · Fassung v4 (Final Ultra-Premium Content Audit)", "",
     "Übergabe 09./10.11.2026 (drei Durchgänge: Grundlieferung v2, Content-Upgrade v3, Final-Audit v4). Reihenfolge zum Lesen:", "",
     "| Nr | Datei | Inhalt |", "|---|---|---|",
     "| 00 | `00_PROJEKTGRUNDLAGE.md` | Ausgangsplan, Quelleninventar, Entscheidungen, Backups |",
     "| 01 | `01_THEMENBEWERTUNG_60plus.md/.csv` | 73 Themenkandidaten (Grundlieferung), Reserveliste |",
     "| 02 | `02_MASTERPLAN_FINAL.md` | **v4-Masterplan**: Strategie, Content-Identität, Kalender, 39 Steckbriefe |",
     "| 03 | `03_SPRECHERTEXTE/` | 39 ElevenLabs-Texte v4 |",
     "| 04 | `04_CAPCUT_SCHNITTPLAENE/` | 39 Schnittpläne (Schlüsselaufnahmen, 16 Felder + Rolle, Timecodes vorläufig) |",
     "| 05 | `05_HOOKS_195.csv/.md` | 195 Hooks v4 (Visueller Schock · Neugierlücke · Überraschende Behauptung · Erwartung gegen Realität · Emotionaler WOW-Moment) |",
     "| 06 | `06_COVER_117.csv/.md` | 117 Cover-Konzepte |",
     "| 07 | `07_STOCK_QUELLEN.csv/.md`, `07_SCHLUESSELAUFNAHMEN_117.csv` | Material- und Quellencheck mit Status |",
     "| 08 | `08_KALENDER_13_WOCHEN.csv/.md` | 13-Wochen-Kalender v4 |",
     "| 09 | `09_KPI_TESTSTRATEGIE.md` | KPI-Dashboard, Reviews, Testplan |",
     "| 10 | `10_QUALITAET_SCORECARDS.md/.csv` | Scorecards v4 (Audit-Gewichte), Verbesserungsprotokoll |",
     "| 11 | `11_AENDERUNGSPROTOKOLL.md` | Änderungen 06.11. → v2 → v3 → v4 |",
     "| 12 | `12_OFFENE_PUNKTE.md` | Ehrliche Liste offener Punkte |",
     "| 13 | `13_TESTBERICHT.md` | Automatisierte Tests (Playwright) |",
     "| 14 | `14_BEDIENUNGSANLEITUNG.md` | Reel-Studio bedienen |",
     "| 15–17 | `15_…`, `16_…`, `17_…` | Durchgang v3 (Änderungsliste, Bewertung, Prioritäten) – Historie |",
     "| 18 | `18_FINAL_AUDIT_ALT_NEU.md` | **ALT-NEU-Vergleich v3 → v4** |",
     "| 19 | `19_FINAL_AUDIT_HOTELS.md` | **Dubletten-Check und DACH-Hotel-Audit** (99 Kandidaten, Footage-Status) |",
     "| 20 | `20_FINAL_AUDIT_BEWERTUNG.md` | **Strenge Qualitätsbewertung v4** |",
     "| 21 | `21_TOP12_ERSTE_PRODUKTION.md` | **Die zwölf stärksten Reels für die erste Produktion** |",
     "| – | `studio/reel-studio-v39.html` | Reel-Studio (Oberfläche v39, Daten v4; Artefakt-Link in 14) |",
     "| – | `data/reels_hauptplan_v4.json` | Vollständige Daten der 39 Reels v4 (Studio-Import) |",
     "| – | `data/02_haydi-weg_ReelStudio_Import_v4.xlsx/.csv/.json` | Importtabellen v4 |",
     "| – | `data/reels_specials_v37.json` | Die 51 Specials (unverändert) |",
     "| – | `backup/` | v37-Original, v38/v39 und v2/v3-Daten vor den Änderungen |",
     "| – | `generator/` | Reproduzierbarer Generator (Kalender, Spezifikation, Module, Audit-Daten) |",
     "| – | `tests/` | Testsuite, Testergebnis, Test-Audio, Screenshots |",
     "| – | `haydi-weg_reel_produktion_v4_2026-11-10.zip` | Alles als ZIP (v4) · ältere ZIPs = v2/v3 |", "",
     "Regeln überall: keine Verkaufs-CTAs bis Ende 2026, keine Preise, keine Personen vor der Kamera, nur lizenziertes Fremdmaterial (Hotel-Reels nur mit nachgewiesenem Hotelmaterial oder Pressefreigabe), Timecodes ohne Audio vorläufig, Scores sind Einschätzungen."]
open(OUT + "README.md", "w", encoding="utf-8").write("\n".join(L))
print("Dokumente v4 geschrieben. Ø v3 %.2f → v4 %.2f · KS %s · Hotels %d · nicht produktionsbereit %d" % (avg2, avg3, dict(KSC), len(hotels), len(nready)))
