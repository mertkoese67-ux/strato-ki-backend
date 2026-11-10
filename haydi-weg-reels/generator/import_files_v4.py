# -*- coding: utf-8 -*-
"""Erzeugt die flachen Import-Dateien (CSV/JSON/XLSX) aus data/reels_hauptplan_v4.json."""
import json, csv, os
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
OUT = "/home/user/strato-ki-backend/haydi-weg-reels/data/"
j = json.load(open(OUT + "reels_hauptplan_v4.json", encoding="utf-8"))
reels = j["reels"]
def win(r): return [h for h in r["hooks"] if h["winner"]][0]
cols = ["id","nr","datum","wochentag","kw","serie","serie_name","folge","titel","titel_v3","entscheidung_v4","ort","themenwelt","struktur","struktur_name","ziel_sec","hotel","hotel_reel","dach_begruendung","dubletten_status","behauptung","aufloesung","dach_anker","emotion",
        "hook_sieger_gesprochen","hook_sieger_bild","hook_sieger_overlay","hook_sieger_frage","cover1","cover2","cover3",
        "schluessel_scrollstop","schluessel_story","schluessel_reveal","vo_woerter","vo_est_sec","vo_text","untertitel_zeilen","szenen","gesamt_tc_vorlaeufig","endkarte","teaser_gesprochen","musik",
        "qs_hook","qs_visuell","qs_story","qs_share","qs_dach","qs_fakten","qs_gesamt","freigabe","caption_ig","caption_tt","yt_titel","offene_punkte"]
rows = []
for r in reels:
    w = win(r); ks = {k["role"]: k for k in r["key_shots"]}
    def ksf(role): k = ks[role]; return "%s · %s %s · %s%s" % (k["motif"], k["source"], k["ref"], k["status"], (" · " + k["note"]) if k["note"] else "")
    s = r["scorecard"]["scores"]
    rows.append(dict(id=r["id"], nr=r["nr"], datum=r["date_de"], wochentag=r["weekday"], kw=r["kw"], serie=r["series"], serie_name=r["series_name"], folge=r["episode"], titel=r["title"], titel_v3=r["title_v2"], entscheidung_v4=r["decision_v3"],
        ort=r["place"], themenwelt=r["themenwelt"], struktur=r["structure"], struktur_name=r["structure_name"], ziel_sec=r["target_sec"], hotel=r["hotel"], hotel_reel="ja" if r.get("hotel_reel") else "nein", dach_begruendung=r.get("dach_begruendung",""), dubletten_status=r.get("dubletten_status",""), behauptung=r["claim"], aufloesung=r["answer"], dach_anker=r["dach_anchor"], emotion=r["emotion"],
        hook_sieger_gesprochen=w["spoken"], hook_sieger_bild=w["first_frame"], hook_sieger_overlay=w["overlay"], hook_sieger_frage=w["question"],
        cover1=r["covers"][0]["headline"], cover2=r["covers"][1]["headline"], cover3=r["covers"][2]["headline"],
        schluessel_scrollstop=ksf("Scroll-Stop"), schluessel_story=ksf("Story"), schluessel_reveal=ksf("Reveal"),
        vo_woerter=r["vo"]["words"], vo_est_sec=r["vo"]["est_sec"], vo_text=r["vo"]["full"], untertitel_zeilen="\n".join(r["subs"]["scenes"]), szenen=len(r["cut"]["scenes"]), gesamt_tc_vorlaeufig=r["cut"]["total_tc"],
        endkarte=r["end_card"], teaser_gesprochen="ja" if r["teaser_spoken"] else "nein", musik=r["cut"]["music"],
        qs_hook=s["hook"], qs_visuell=s["visual"], qs_story=s["story"], qs_share=s["share"], qs_dach=s["dach"], qs_fakten=s["facts"], qs_gesamt=r["scorecard"]["total"], freigabe=r["approval"]["status"],
        caption_ig=r["captions"]["ig"], caption_tt=r["captions"]["tt"], yt_titel=r["captions"]["yt_title"], offene_punkte=" · ".join(r["open_points"])))
with open(OUT + "02_haydi-weg_ReelStudio_Import_v4.csv", "w", newline="", encoding="utf-8") as f:
    wr = csv.DictWriter(f, fieldnames=cols, delimiter=";"); wr.writeheader(); wr.writerows(rows)
json.dump(dict(meta=dict(stand=j["meta"]["stand"], schema="reelstudio_import_v4", quelle="reels_hauptplan_v4.json", hinweis="Flache Tabelle; vollständige Daten in reels_hauptplan_v4.json (im Studio importierbar)"), rows=rows),
          open(OUT + "02_haydi-weg_ReelStudio_Import_v4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
wb = Workbook(); ws = wb.active; ws.title = "Hauptplan 39"
hdr_fill = PatternFill("solid", fgColor="1C2C5C"); hdr_font = Font(bold=True, color="FFFFFF")
def sheet(ws, header, data):
    ws.append(header)
    for c in ws[1]: c.fill = hdr_fill; c.font = hdr_font; c.alignment = Alignment(vertical="top", wrap_text=True)
    for row in data: ws.append([("\n".join(x) if isinstance(x, list) else x) for x in row])
    for i, h in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = 14 if len(str(h)) < 12 else min(60, 18 + len(str(h)))
    ws.freeze_panes = "A2"
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(vertical="top", wrap_text=True)
sheet(ws, cols, [[r[c] for c in cols] for r in rows])
ws2 = wb.create_sheet("Hooks 195")
sheet(ws2, ["Reel","Datum","Titel","Typ","Gesprochen","Erstes Bild","Overlay","Offene Frage","Scroll-Stop","Verständlich","Originell","Emotion","Visuell","Glaubwürdig","DACH","Gesamt","Sieger","Begründung"],
      [[r["id"], r["date_de"], r["title"], h["typ"], h["spoken"], h["first_frame"], h["overlay"], h["question"]] + [h["scores"][k] for k in ["scrollstop","verstaendlich","originalitaet","emotion","visuell","glaubwuerdig","dach"]] + [h["total"], "★" if h["winner"] else "", h["reason"]] for r in reels for h in r["hooks"]])
ws3 = wb.create_sheet("Cover 117")
sheet(ws3, ["Reel","Datum","Titel","#","Headline","gelb","Bild","Variante"], [[r["id"], r["date_de"], r["title"], i+1, c["headline"], c["yellow"], c["image"], c["variant"]] for r in reels for i, c in enumerate(r["covers"])])
ws4 = wb.create_sheet("Schluesselaufnahmen 117")
sheet(ws4, ["Reel","Datum","Titel","Rolle","Motiv","Quelle","Referenz","Status","Hinweis"], [[r["id"], r["date_de"], r["title"], k["role"], k["motif"], k["source"], k["ref"], k["status"], k["note"]] for r in reels for k in r["key_shots"]])
ws5 = wb.create_sheet("Schnittplaene")
sheet(ws5, ["Reel","Datum","Titel","Szene","Rolle","TC Start (vorläufig)","TC Ende","Dauer s","Sprechtext","Motiv","Ort","Kamera","Bildausschnitt","Bewegung","Licht","Stock-Suchbegriffe","Schnittart","Übergang","Overlay","Musik","SFX","Untertitel-Hinweis"],
      [[r["id"], r["date_de"], r["title"], s["nr"], s["role"], s["tc_in"], s["tc_out"], s["dur_s"], s["vo"], s["motif"], s["place"], s["cam"], s["frame"], s["move"], s["light"], ", ".join(s["stock"]), s["cut"], s["trans"], s["overlay"], s["music"], s["sfx"], s["subhint"]] for r in reels for s in r["cut"]["scenes"]])
ws6 = wb.create_sheet("Stock & Quellen")
sheet(ws6, ["Reel","Titel","Clip","Quelle","Referenz","Suchbegriffe","Lizenz","Prüfstand","Fehlt","Alternative","Szenen"], [[r["id"], r["title"], st["shot"], st["source"], st["ref"], st["search_terms"], st["license_status"], st["checked"], "JA" if st["missing"] else "", st["alternative"], st["scenes"]] for r in reels for st in r["stock"]])
ws7 = wb.create_sheet("Aenderungen v3 → v4")
sheet(ws7, ["Reel","Datum","Entscheidung","Titel v2","Titel v3","Struktur","Themenwelt","Begründung","Änderungen im Detail"], [[r["id"], r["date_de"], r["decision_v3"], r["title_v2"], r["title"], r["structure"] + " " + r["structure_name"], r["themenwelt"], r["decision_reason"], r["changelog_vs_plan"]] for r in reels])
wb.save(OUT + "02_haydi-weg_ReelStudio_Import_v4.xlsx")
print("Import-Dateien v3 geschrieben:", len(rows), "Zeilen")
