# -*- coding: utf-8 -*-
"""Generator v4 (Final-Audit 09.11.2026: DACH-Luxushotels, Visual WOW): baut aus den Reel-Definitionen (r*.py) alle Lieferdateien.
Timecodes sind VORLÄUFIG (Schätzung 2,45 Wörter/s + 0,35 s je '…'); erst das Reel-Studio berechnet nach Audio-Upload reale Zeiten."""
import json, re, csv, os, importlib, glob, datetime, statistics
from kalender import FINAL, SERIE, SERIE_HINWEIS, STRUKTUR, THEMENWELTEN, kw

FPS = 30
WPS = 2.45
OUT = "/home/user/strato-ki-backend/haydi-weg-reels/"
STAND = "09.11.2026"
HOOK_TYPES = ["Visueller Schock","Neugierlücke","Überraschende Behauptung","Erwartung gegen Realität","Emotionaler WOW-Moment"]
HOOK_CRIT = ["scrollstop","verstaendlich","originalitaet","emotion","visuell","glaubwuerdig","dach"]
QS_W = {"hook":25,"visual":25,"story":20,"share":15,"dach":5,"facts":10}
KS_ROLES = ["Scroll-Stop","Story","Reveal"]
KS_STATUS = ["gefunden","verfügbar, ungeprüft","nicht gefunden"]
TAG_RE = re.compile(r"\[[^\]]+\]")
# verbotene Floskeln / leere Superlative / Fake-Cliffhanger in Hooks (gesprochen + Overlay)
BANNED = ["das musst du sehen","du wirst nicht glauben","unglaublich","krass","geheimtipp","atemberaubend","wusstest du","niemand spricht darüber",
          "das wird dich","verrückt","wahnsinn","unfassbar","magisch","paradies","traumhaft","must-see","muss man gesehen haben","schock","schockierend",
          "was dann passiert","bis zum ende","warte bis","niemand erzählt dir","mind-blowing","nicht glauben, was"]
CAL = {r[0]: dict(zip(["nr","date","wd","serie","ep","title","place","themenwelt","decision","alt_title","structure","target_sec","why"], r)) for r in FINAL}
PROD_READY = "Vorprüfung bestanden – Freigabe erst nach Materialcheck, Faktencheck am Vortag"
NOT_READY = "Material offen – nicht produktionsbereit (Schlüsselaufnahme fehlt), erst nach Materialnachweis freigeben"

def words(t):
    t = TAG_RE.sub(" ", t)
    return len([w for w in re.split(r"\s+", t.strip()) if re.search(r"[A-Za-zÄÖÜäöüß0-9]", w)])

def est(t):
    return words(t)/WPS + 0.35*t.count("…")

def tc(sec):
    f = int(round(sec*FPS))
    h, r = divmod(f, 3600*FPS); m, r = divmod(r, 60*FPS); s, fr = divmod(r, FPS)
    return "%02d:%02d:%02d:%02d" % (h, m, s, fr)

def S(vo, sub, motif, place, cam, frame, move, light, stock, cut, trans, overlay, music, sfx, subhint, role="body", hold=0.0):
    assert role in ("hook","body","reveal","end"), role
    return dict(vo=vo, sub=sub, motif=motif, place=place, cam=cam, frame=frame, move=move, light=light,
                stock=stock, cut=cut, trans=trans, overlay=overlay, music=music, sfx=sfx, subhint=subhint, role=role, hold=hold)

def H(typ, spoken, frame, overlay, question, sc, reason):
    """Hook = Kombination aus erstem Bild (ohne Ton verständlich) + gesprochenem Einstieg + Text-Overlay + offener Zuschauerfrage."""
    assert typ in HOOK_TYPES, typ
    assert len(sc) == 7, (typ, sc)
    return dict(typ=typ, text=spoken, spoken=spoken, first_frame=frame, overlay=overlay, question=question,
                scores=dict(zip(HOOK_CRIT, sc)), total=round(sum(sc)/7, 2), reason=reason)

def C(headline, yellow, image, variant):
    return dict(headline=headline, yellow=yellow, image=image, variant=variant)

def KS(role, motif, source, ref, status, note=""):
    """Schlüsselaufnahme: Scroll-Stop-Bild · wichtigstes Storytelling-Bild · visueller Reveal. Status ehrlich."""
    assert role in KS_ROLES, role
    assert status in KS_STATUS, status
    if status == "nicht gefunden": assert note, ("nicht gefunden ohne Alternative/Umbau", motif)
    return dict(role=role, motif=motif, source=source, ref=ref, status=status, note=note)

def ST(shot, source, ref, terms, status, missing=False, alt="", scenes="", checked=""):
    if not checked:
        if source in ("Pexels","Pixabay","Envato Elements"):
            checked = "Suchergebnisseite am %s aus dieser Umgebung geöffnet (Treffer gelistet, Detailseite/Lizenz nicht geöffnet) – vor Download Ort, Urheber, Personen prüfen" % STAND if ref not in ("", "Suche") else "nur Suchbegriff – am %s kein passender Treffer gelistet" % STAND
        else:
            checked = "eigene Produktion/Grafik, keine Lizenz nötig"
    return dict(shot=shot, source=source, ref=ref, search_terms=terms, license_status=status, checked=checked, missing=missing, alternative=alt, scenes=scenes)

def R(nr, **k):
    k["nr"] = nr
    return k

def build_reel(d):
    cal = CAL[d["nr"]]
    nr, date, wd, serie, ep, title, place = cal["nr"], cal["date"], cal["wd"], cal["serie"], cal["ep"], cal["title"], cal["place"]
    y, m, dd = date.split("-")
    scenes = []
    t = 0.0
    for i, s in enumerate(d["scenes"]):
        dur = max(est(s["vo"]) + 0.15, 1.6) if s["vo"].strip() else 2.0
        if s["role"] == "hook": dur = max(dur, 2.5)
        dur += s.get("hold", 0.0)
        sc = dict(nr=i+1, tc_in=tc(t), tc_out=tc(t+dur), start_s=round(t, 2), end_s=round(t+dur, 2), dur_s=round(dur, 2))
        sc.update(s)
        if not sc["sub"].strip() and sc["vo"].strip(): sc["sub"] = TAG_RE.sub("", sc["vo"]).strip()
        sc["words"] = words(s["vo"])
        scenes.append(sc)
        t += dur
    vo_full = "\n".join(s["vo"] for s in d["scenes"] if s["vo"].strip())
    vo_words = words(vo_full)
    tags = TAG_RE.findall(vo_full)
    hooks = d["hooks"]
    assert len(hooks) == 5, nr
    assert [h["typ"] for h in hooks] == HOOK_TYPES, (nr, [h["typ"] for h in hooks])
    win = d["winner"]
    for i, h in enumerate(hooks): h["winner"] = (i == win)
    sc = d["score"]
    total = round(sum(sc[k]*QS_W[k] for k in QS_W)/100, 2)
    structure = d.get("structure", cal["structure"])
    assert structure in STRUKTUR, structure
    reel = dict(
        id="H%s" % nr, nr=int(nr), date=date, date_de="%s.%s.%s" % (dd, m, y), weekday=wd, kw=kw(date),
        series=serie, series_name=SERIE[serie], episode=ep, title=title, place=place,
        themenwelt=cal["themenwelt"], themenwelt_text=THEMENWELTEN[cal["themenwelt"]],
        decision_v3=cal["decision"], title_v2=cal["alt_title"], decision_reason=cal["why"],
        structure=structure, structure_name=STRUKTUR[structure], target_sec=cal["target_sec"],
        hotel=d.get("hotel", ""), hotel_reel=bool(d.get("hotel_reel", False)), dubletten_status=d.get("dubletten", "neu – gegen Specials v37, Oktober-Skripte und Plan v3 geprüft; gegen Live-Konto ungeprüft"), dach_begruendung=d.get("dach_begruendung", ""),
        claim=d["claim"], answer=d.get("answer", ""), dach_anchor=d["dach"], emotion=d["emotion"],
        story_arc=d["arc"],
        teaser_spoken=bool(d.get("teaser_spoken", False)), end_card=d["end_card"],
        vo=dict(full=vo_full, scenes=[s["vo"] for s in d["scenes"] if s["vo"].strip()], words=vo_words,
                est_sec=round(est(vo_full), 1), est_sec_label="vorläufig (%.2f Wörter/s, ohne echte Audiodatei)" % WPS,
                tags=tags, voice="Mert_V2", model="Eleven v3", rules="Zahlen ausgeschrieben, max. 3 Audio-Tags, keine <break>-Tags, keine Platzhalter"),
        subs=dict(scenes=[sc["sub"] for sc in scenes if sc["sub"].strip()], style="Manrope SemiBold, ≤2 Zeilen, ≤38 Zeichen, 60–70 % Höhe, Ziffern statt Zahlwörter, keine Untertitel während des Hooks"),
        hooks=hooks, hook_winner=hooks[win]["text"], hook_winner_reason=d["winner_reason"],
        covers=d["covers"],
        key_shots=d["key_shots"],
        cut=dict(format="9:16 · 1080×1920 · 30 fps", tc_format="HH:MM:SS:FF", timing_mode="VORLÄUFIG – geschätzt aus Wortzahl; nach Audio-Upload im Reel-Studio neu berechnen",
                 total_sec=round(t, 2), total_tc=tc(t), scenes=scenes, music=d["music"], logo="weiß, klein, unten rechts, ab 00:00:03:00",
                 series_card="letzte Szene: Themenwelt-Karte (Markenfarben, Logo weiß) – Teaser als Grafiktext" + (" + gesprochen" if d.get("teaser_spoken") else ", nicht gesprochen")),
        stock=d["stock"],
        facts=dict(secured=[dict(fact=f, source=s) for f, s in d["facts"]], to_check=d["check"], sources=d["sources"], checked_on=STAND),
        scorecard=dict(weights=QS_W, scores=sc, total=total, iterations=d["iterations"], label="Einschätzung Redaktion nach Nacharbeit, keine Messwerte; Score ersetzt keine Rechte-, Fakten- oder Materialprüfung"),
        approval=dict(status=d.get("approval", NOT_READY if any(k["status"] == "nicht gefunden" and k["role"] in ("Scroll-Stop","Reveal") for k in d["key_shots"]) else PROD_READY), pre_post_checks=d["prepost"],
                      requirements=["Fakten am Vortag geprüft", "alle Clips lizenziert und dem Ort/Hotel zugeordnet (keine falschen Hotelaufnahmen)", "Hook ohne Ton verständlich (erstes Bild + Overlay)", "keine Personen vor der Kamera, keine Gesichter groß", "kein Verkaufs-CTA, keine Preise (bis Ende 2026)", "Hotel-Reels: Schlüsselaufnahme des Hotels nachgewiesen"]),
        captions=dict(ig=d["cap_ig"], tt=d["cap_tt"], yt_title=d["cap_yt"]),
        changelog_vs_plan=d["changelog"], open_points=d["open"],
    )
    return reel

def lint(reel):
    errs = []
    vo = reel["vo"]["full"]
    plain = TAG_RE.sub("", vo)
    if re.search(r"\d", plain): errs.append("Ziffer im Sprechtext")
    if len(reel["vo"]["tags"]) > 3: errs.append("mehr als 3 Audio-Tags")
    if "<break" in vo: errs.append("<break>-Tag")
    if not 35 <= reel["vo"]["words"] <= 120: errs.append("Wortzahl %d" % reel["vo"]["words"])
    if not 16 <= reel["cut"]["total_sec"] <= 48: errs.append("Länge %.1f s" % reel["cut"]["total_sec"])
    if abs(reel["cut"]["total_sec"] - reel["target_sec"]) > 7: errs.append("Länge %.1f s weicht >7 s vom Ziel %d ab" % (reel["cut"]["total_sec"], reel["target_sec"]))
    if len(reel["covers"]) != 3: errs.append("Cover != 3")
    for s in reel["cut"]["scenes"]:
        for k in ("motif","place","cam","frame","move","light","stock","cut","trans","overlay","music","sfx","subhint"):
            if not s.get(k): errs.append("Szene %d Feld %s leer" % (s["nr"], k))
    if reel["cut"]["scenes"][0]["role"] != "hook": errs.append("erste Szene kein Hook")
    if reel["cut"]["scenes"][-1]["role"] != "end": errs.append("letzte Szene keine Endkarte (role=end)")
    if not any(s["role"] == "reveal" for s in reel["cut"]["scenes"]): errs.append("keine Reveal-Szene markiert")
    if "keine Untertitel" not in reel["cut"]["scenes"][0]["subhint"]: errs.append("Hook-Szene ohne 'keine Untertitel'")
    if len(reel["scorecard"]["iterations"]) < 2: errs.append("weniger als 2 Überarbeitungsrunden")
    if not reel["stock"]: errs.append("keine Stockliste")
    ks = reel["key_shots"]
    if len(ks) != 3 or [k["role"] for k in ks] != KS_ROLES: errs.append("Schlüsselaufnahmen nicht Scroll-Stop/Story/Reveal")
    for h in reel["hooks"]:
        txt = (h["spoken"] + " " + h["overlay"]).lower()
        for b in BANNED:
            if b in txt: errs.append("Floskel '%s' in Hook: %s" % (b, h["spoken"]))
        if re.match(r"^(Dieser|Diese|Dieses)\b", h["spoken"]): errs.append("Hook beginnt mit 'Dieser…': %s" % h["spoken"])
        if "sieht aus wie" in h["spoken"].lower(): errs.append("Hook 'sieht aus wie'")
        if h["spoken"].startswith("Würdest du"): errs.append("Hook 'Würdest du'")
        if words(h["spoken"]) > 18: errs.append("Hook-Satz > 18 Wörter: %s" % h["spoken"])
        if not h["overlay"].strip() or not h["question"].strip() or not h["first_frame"].strip(): errs.append("Hook-Komponente fehlt (%s)" % h["typ"])
        if words(h["overlay"]) > 7: errs.append("Overlay > 7 Wörter: %s" % h["overlay"])
        if re.search(r"\d", h["spoken"]): errs.append("Ziffer im gesprochenen Hook: %s" % h["spoken"])
    if not reel["end_card"].strip(): errs.append("Endkarte leer")
    if reel["hotel_reel"]:
        if not reel["hotel"]: errs.append("Hotel-Reel ohne Hotelname")
        if not reel["dach_begruendung"]: errs.append("Hotel-Reel ohne DACH-Begründung")
        if all(k["status"] == "nicht gefunden" for k in reel["key_shots"]): errs.append("Hotel-Reel ohne jeden Footage-Nachweis")
    for ph in ("zimmer, restaurants und", "bietet ihnen", "verwöhnt", "exklusiv", "luxuriös", "erstklassig", "traumurlaub", "buchbar", "ab sofort"):
        if ph in plain.lower(): errs.append("Werbesprache im Sprechtext: %s" % ph)
    _norm = lambda t: re.sub(r"\s+", " ", TAG_RE.sub("", t)).strip().rstrip(".!?…").lower()
    _w = [h for h in reel["hooks"] if h["winner"]][0]
    if _norm(_w["spoken"]) != _norm(reel["cut"]["scenes"][0]["vo"]): errs.append("Sieger-Hook ≠ gesprochener Satz der Hook-Szene")
    capt = (reel["captions"]["ig"]+reel["captions"]["tt"]).lower()
    if any(x in capt for x in ("buch jetzt","jetzt buchen","angebot","link in bio","rabatt","anfrage","beratung")) or re.search(r"\bab \d+ ?€", capt): errs.append("Verkaufs-CTA/Reisepreis in Caption")
    if re.search(r"(€|\beuro\b|\bpreis|kostet)", plain.lower()) and "eintritt" not in plain.lower(): errs.append("Preisangabe im Sprechtext prüfen (kein Verkaufs-CTA)")
    if reel["captions"]["ig"].count("#") > 7: errs.append("mehr als 7 Hashtags IG")
    if reel["scorecard"]["total"] < 9.0: errs.append("QS %.2f unter Ziel 9,0 (Begründung in Runden/offenen Punkten nötig)" % reel["scorecard"]["total"])
    return errs

def global_checks(reels):
    warn = []
    fof_formula = [r["id"] for r in reels if r["series"] == "FoF" and re.match(r"^\W*(\[[^\]]+\]\s*)?Fakt oder Fake", r["vo"]["full"])]
    if len(fof_formula) > 4: warn.append("Mehr als 4 FoF-Reels beginnen gesprochen mit 'Fakt oder Fake': %s" % ", ".join(fof_formula))
    wd = [r["id"] for r in reels if re.match(r"^\W*(\[[^\]]+\]\s*)?Was dir keiner sagt", r["vo"]["full"])]
    if wd: warn.append("WDKS-Reels mit Serienformel im Einstieg: %s" % ", ".join(wd))
    teaser = [r["id"] for r in reels if re.search(r"(Nächsten|Nächste Woche|Am Montag|Am Mittwoch|Am Freitag)", r["vo"]["scenes"][-1]) ]
    if len(teaser) > 15: warn.append("Zu viele gesprochene Teaser (%d): %s" % (len(teaser), ", ".join(teaser)))
    L = [r["cut"]["total_sec"] for r in reels]
    sd = statistics.pstdev(L)
    if sd < 3.5: warn.append("Längen zu gleichförmig (sd %.1f)" % sd)
    firsts = {}
    for r in reels:
        k = " ".join(TAG_RE.sub("", r["vo"]["scenes"][0]).split()[:2]).lower()
        firsts.setdefault(k, []).append(r["id"])
    for k, v in firsts.items():
        if len(v) > 3: warn.append("Einstieg '%s…' %d× (%s)" % (k, len(v), ", ".join(v)))
    for a, b in zip(reels, reels[1:]):
        if a["structure"] == b["structure"]: warn.append("gleiche Struktur hintereinander %s/%s (%s)" % (a["id"], b["id"], a["structure"]))
    return warn

def load_all(only=None):
    reels = []
    files = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "r*.py")))
    if only: files = [f for f in files if os.path.basename(f)[:-3] in only]
    for f in files:
        mod = importlib.import_module(os.path.basename(f)[:-3])
        reels += mod.REELS
    reels.sort(key=lambda d: d["nr"])
    return reels

def fname(reel):
    t = re.sub(r"[^A-Za-z0-9ÄÖÜäöüß]+", "_", reel["title"]).strip("_")[:48]
    return "%s_%s" % (reel["id"], t)

def write_outputs(reels):
    os.makedirs(OUT+"data", exist_ok=True); os.makedirs(OUT+"03_SPRECHERTEXTE", exist_ok=True); os.makedirs(OUT+"04_CAPCUT_SCHNITTPLAENE", exist_ok=True)
    for f in glob.glob(OUT+"03_SPRECHERTEXTE/*") + glob.glob(OUT+"04_CAPCUT_SCHNITTPLAENE/*"): os.remove(f)
    json.dump(dict(meta=dict(stand=STAND, plan="haydi-weg Reel-Masterplan 09.11.2026–05.02.2027, Fassung v4 (Final-Audit: DACH-Luxushotels, Visual WOW)", count=len(reels), fps=FPS, wps=WPS,
                             timing="Alle Timecodes vorläufig; reale Zeiten erst nach Audio-Upload im Reel-Studio", schema="reels_hauptplan_v4",
                             series=SERIE, series_note=SERIE_HINWEIS, structures=STRUKTUR, themenwelten=THEMENWELTEN, hook_types=HOOK_TYPES, key_shot_status=KS_STATUS), reels=reels),
              open(OUT+"data/reels_hauptplan_v4.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    # Sprechertexte
    allvo = ["# Alle 39 ElevenLabs-Sprechertexte (Fassung v4 · Stimme Mert_V2, Eleven v3)\n", "Regeln: Text unverändert einfügen; eckige Klammern sind Audio-Tags und werden nicht gesprochen. Zahlen sind ausgeschrieben. Längen folgen der Geschichte (22–42 s) und sind Schätzungen (%.2f Wörter/s) – maßgeblich ist die exportierte Audiodatei.\n" % WPS]
    for r in reels:
        head = "%s · %s %s · %s #%d · %s" % (r["id"], r["weekday"], r["date_de"], r["series_name"], r["episode"], r["title"])
        body = "%s\n%s\nStruktur %s (%s) · Themenwelt %s · Ziel ca. %d s\n\nWörter: %d · geschätzt ca. %.0f s (vorläufig)\n\n--- GESAMTTEXT (in ElevenLabs einfügen) ---\n%s\n\n--- NACH SZENEN ---\n%s\n\n--- ENDKARTE (Grafiktext, %s) ---\n%s\n" % (
            head, "="*len(head), r["structure"], r["structure_name"], r["themenwelt"], r["target_sec"], r["vo"]["words"], r["vo"]["est_sec"], r["vo"]["full"],
            "\n".join("Szene %d: %s" % (i+1, s) for i, s in enumerate(r["vo"]["scenes"])), "gesprochen + Grafik" if r["teaser_spoken"] else "nur Grafik", r["end_card"])
        open(OUT+"03_SPRECHERTEXTE/%s.txt" % fname(r), "w", encoding="utf-8").write(body)
        allvo.append("## %s\n\n*Struktur %s · %s · ca. %d s*\n\n%s\n\n*Wörter %d · ca. %.0f s (vorläufig) · Endkarte: %s*\n" % (head, r["structure"], r["themenwelt"], r["target_sec"], r["vo"]["full"].replace("\n", "  \n"), r["vo"]["words"], r["vo"]["est_sec"], r["end_card"]))
    open(OUT+"03_SPRECHERTEXTE/ALLE_39_SPRECHERTEXTE.md","w",encoding="utf-8").write("\n".join(allvo))
    # CapCut
    cols = ["Szene","TC Start","TC Ende","Dauer s","Rolle","Sprechtext (exakt)","Motiv (detailliert)","Ort/Hotel (exakt)","Kameraperspektive","Bildausschnitt","Bewegung","Licht/Atmosphäre","Stock-Suchbegriffe","Schnittart","Übergang","Text-Overlay","Musikstimmung","SFX","Untertitel-Hinweis"]
    allrows = []
    for r in reels:
        L = ["# CapCut-Schnittplan %s · %s" % (r["id"], r["title"]), "", "%s %s · %s #%d · %s · Themenwelt %s · Struktur %s (%s)" % (r["weekday"], r["date_de"], r["series_name"], r["episode"], r["place"], r["themenwelt"], r["structure"], r["structure_name"]), "",
             "**Format:** %s · **Timecode:** %s · **Gesamt (vorläufig):** %s (%.1f s, Ziel ca. %d s)" % (r["cut"]["format"], r["cut"]["tc_format"], r["cut"]["total_tc"], r["cut"]["total_sec"], r["target_sec"]), "",
             "> **Timecode-Regel:** %s" % r["cut"]["timing_mode"], "",
             "**Hook (Sieger):** %s  " % r["hook_winner"], "**Musik:** %s · **Logo:** %s · **Endkarte:** %s" % (r["cut"]["music"], r["cut"]["logo"], r["cut"]["series_card"]), "",
             "## Schlüsselaufnahmen (Material zuerst)", "", "| Rolle | Motiv | Quelle | Referenz | Status | Hinweis |", "|---|---|---|---|---|---|"] + \
            ["| %s | %s | %s | %s | **%s** | %s |" % (k["role"], k["motif"], k["source"], k["ref"], k["status"], k["note"] or "–") for k in r["key_shots"]] + ["",
             "| " + " | ".join(cols) + " |", "|" + "---|"*len(cols)]
        for s in r["cut"]["scenes"]:
            row = [str(s["nr"]), s["tc_in"], s["tc_out"], "%.1f" % s["dur_s"], s["role"], s["vo"] or "–", s["motif"], s["place"], s["cam"], s["frame"], s["move"], s["light"], ", ".join(s["stock"]), s["cut"], s["trans"], s["overlay"], s["music"], s["sfx"], s["subhint"]]
            L.append("| " + " | ".join(x.replace("|","/").replace("\n"," ") for x in row) + " |")
            allrows.append([r["id"], r["date_de"], r["title"]] + row)
        L += ["", "## Stock & Quellen", ""]
        for st in r["stock"]:
            L.append("- **%s** – %s %s · Suche: %s · Lizenz: %s · Prüfung: %s%s%s" % (st["shot"], st["source"], st["ref"], st["search_terms"], st["license_status"], st["checked"], (" · **FEHLT** – Alternative: %s" % st["alternative"]) if st["missing"] else "", (" · Szenen %s" % st["scenes"]) if st["scenes"] else ""))
        L += ["", "## Fakten", ""] + ["- ✅ %s (%s)" % (f["fact"], f["source"]) for f in r["facts"]["secured"]] + ["- ⚠️ prüfen: %s" % c for c in r["facts"]["to_check"]] + ["", "Quellen: " + " · ".join(r["facts"]["sources"]), "", "## Vor Posting prüfen", ""] + ["- [ ] %s" % c for c in r["approval"]["pre_post_checks"]]
        open(OUT+"04_CAPCUT_SCHNITTPLAENE/%s.md" % fname(r), "w", encoding="utf-8").write("\n".join(L))
        with open(OUT+"04_CAPCUT_SCHNITTPLAENE/%s.csv" % fname(r), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, delimiter=";"); w.writerow(cols)
            for s in r["cut"]["scenes"]:
                w.writerow([s["nr"], s["tc_in"], s["tc_out"], "%.1f" % s["dur_s"], s["role"], s["vo"], s["motif"], s["place"], s["cam"], s["frame"], s["move"], s["light"], ", ".join(s["stock"]), s["cut"], s["trans"], s["overlay"], s["music"], s["sfx"], s["subhint"]])
    with open(OUT+"04_CAPCUT_SCHNITTPLAENE/ALLE_39_SCHNITTPLAENE.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Reel","Datum","Titel"]+cols); w.writerows(allrows)
    # Hooks
    with open(OUT+"05_HOOKS_195.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Reel","Datum","Titel","Hook-Typ","Gesprochener Einstieg","Erstes Bild ohne Ton","Text-Overlay","Offene Zuschauerfrage"]+HOOK_CRIT+["Gesamt","Sieger","Begründung"])
        for r in reels:
            for h in r["hooks"]:
                w.writerow([r["id"], r["date_de"], r["title"], h["typ"], h["spoken"], h["first_frame"], h["overlay"], h["question"]] + [h["scores"][c] for c in HOOK_CRIT] + [h["total"], "★" if h["winner"] else "", h["reason"]])
    L = ["# 195 Hooks (Fassung v4 · 5 je Reel · 4 Komponenten)", "", "Jeder Hook ist die Kombination aus **erstem sichtbaren Bild** (muss ohne Ton funktionieren), **gesprochenem Einstieg**, **Text-Overlay** und der **offenen Frage**, die im Kopf des Zuschauers entsteht. Fünf Typen je Reel: Visueller Schock · Neugierlücke · Überraschende Behauptung · Erwartung gegen Realität · Emotionaler WOW-Moment. Kriterien je 1–10 (Einschätzung): Scroll-Stop · Verständlichkeit · Originalität · Emotion · visuelle Umsetzbarkeit · Glaubwürdigkeit · DACH-Fit. ★ = Sieger mit Begründung (nicht immer der Punktbeste, wenn Faktentreue oder Material dagegen sprechen). Keine Floskeln, keine leeren Superlative, keine Fake-Cliffhanger (automatisch geprüft).", ""]
    for r in reels:
        L += ["## %s · %s (%s %s · Struktur %s)" % (r["id"], r["title"], r["weekday"], r["date_de"], r["structure"]), "", "| Typ | Gesprochen | Erstes Bild (ohne Ton) | Overlay | Offene Frage | " + " | ".join(HOOK_CRIT) + " | Ø | Bewertung |", "|---|---|---|---|---|" + "---|"*len(HOOK_CRIT) + "---|---|"]
        for h in r["hooks"]:
            L.append("| %s%s | %s | %s | %s | %s | %s | **%.2f** | %s |" % ("★ " if h["winner"] else "", h["typ"], h["spoken"], h["first_frame"], h["overlay"], h["question"], " | ".join(str(h["scores"][c]) for c in HOOK_CRIT), h["total"], h["reason"]))
        L += ["", "**Sieger:** %s – %s" % (r["hook_winner"], r["hook_winner_reason"]), ""]
    open(OUT+"05_HOOKS_195.md", "w", encoding="utf-8").write("\n".join(L))
    # Covers
    with open(OUT+"06_COVER_117.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Reel","Datum","Titel","Cover #","Headline (Manrope ExtraBold, ≤2 Zeilen)","Gelbes Keyword (#FBDC15)","Bild","Variante"])
        for r in reels:
            for i, c in enumerate(r["covers"]): w.writerow([r["id"], r["date_de"], r["title"], i+1, c["headline"], c["yellow"], c["image"], c["variant"]])
    L = ["# 117 Cover-Konzepte (Fassung v4 · 3 je Reel)", "", "Design: Navy #1C2C5C, Gelb #FBDC15, Weiß; Headline Manrope ExtraBold ≤ 2 Zeilen, ein Schlüsselwort gelb; Bild mit ruhiger Zone für den Text (Zonenwahl macht das Studio automatisch). Variante A = Frage, B = Zahl/Behauptung, C = Themenwelt/Bild.", ""]
    for r in reels:
        L += ["## %s · %s" % (r["id"], r["title"]), "", "| # | Headline | gelb | Bild | Variante |", "|---|---|---|---|---|"] + ["| %d | %s | %s | %s | %s |" % (i+1, c["headline"], c["yellow"], c["image"], c["variant"]) for i, c in enumerate(r["covers"])] + [""]
    open(OUT+"06_COVER_117.md", "w", encoding="utf-8").write("\n".join(L))
    # Stock + Schlüsselaufnahmen
    with open(OUT+"07_STOCK_QUELLEN.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Reel","Datum","Titel","Benötigter Clip","Quelle","Referenz/ID","Suchbegriffe","Lizenzstatus","Prüfdatum/Prüfstand","Fehlt (Schlüsselshot)","Alternative","Szenen"])
        for r in reels:
            for st in r["stock"]: w.writerow([r["id"], r["date_de"], r["title"], st["shot"], st["source"], st["ref"], st["search_terms"], st["license_status"], st["checked"], "JA" if st["missing"] else "", st["alternative"], st["scenes"]])
    with open(OUT+"07_SCHLUESSELAUFNAHMEN_117.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Reel","Datum","Titel","Rolle","Motiv","Quelle","Referenz","Status","Hinweis/Alternative"])
        for r in reels:
            for k in r["key_shots"]: w.writerow([r["id"], r["date_de"], r["title"], k["role"], k["motif"], k["source"], k["ref"], k["status"], k["note"]])
    cnt = {s: sum(1 for r in reels for k in r["key_shots"] if k["status"] == s) for s in KS_STATUS}
    miss = [(r, st) for r in reels for st in r["stock"] if st["missing"]]
    L = ["# Stock- und Quellenliste (Fassung v4)", "", "Stand %s. **Prüfstand ehrlich:** Für jede Schlüsselaufnahme wurde am %s die Suchergebnisseite von Pexels bzw. Envato Elements aus dieser Umgebung geöffnet und ein passender Treffer (Titel/ID) protokolliert – die Detailseite mit Lizenztext, Urheber und Ort konnte nicht geöffnet werden (Pexels-Detailseiten liefern HTTP 403, Envato-Vorschau braucht ein Konto). Deshalb gilt: **„gefunden“** = Treffer mit passendem Titel/Motiv gelistet, vor Download Ort/Urheber/Personen prüfen · **„verfügbar, ungeprüft“** = Treffer plausibel, Motiv nicht sicher · **„nicht gefunden“** = keine passende Suche – Alternative oder Umbau steht dabei. Keine erfundenen Clipverfügbarkeiten. Lizenz Pexels/Pixabay: kommerziell ohne Pflichtnennung (Urheber trotzdem protokollieren); Envato Elements: Abo-Lizenz je Download registrieren. Zusätzliches Stockbudget max. 50 €/Monat, Käufe nur nach Freigabe." % (STAND, STAND), "",
         "## Schlüsselaufnahmen – Gesamtbild", "", "| Status | Anzahl von %d |" % (3*len(reels)), "|---|---|"] + ["| %s | %d |" % (s, cnt[s]) for s in KS_STATUS] + ["",
         "## Nicht gefundene Schlüsselaufnahmen (mit Umbau/Alternative)", "", "| Reel | Rolle | Motiv | Alternative/Umbau |", "|---|---|---|---|"] + \
        ["| %s %s | %s | %s | %s |" % (r["id"], r["title"], k["role"], k["motif"], k["note"]) for r in reels for k in r["key_shots"] if k["status"] == "nicht gefunden"] + ["",
         "## Fehlende Zusatz-Clips (%d)" % len(miss), "", "| Reel | Clip | Alternative |", "|---|---|---|"] + ["| %s %s | %s | %s |" % (r["id"], r["title"], st["shot"], st["alternative"]) for r, st in miss] + ["", "## Je Reel", ""]
    for r in reels:
        L += ["### %s · %s" % (r["id"], r["title"]), "", "**Schlüsselaufnahmen:**", ""] + ["- **%s:** %s – %s %s · **%s**%s" % (k["role"], k["motif"], k["source"], k["ref"], k["status"], (" · " + k["note"]) if k["note"] else "") for k in r["key_shots"]] + ["",
              "| Clip | Quelle | Referenz | Suchbegriffe | Lizenz | Prüfstand | Fehlt | Alternative |", "|---|---|---|---|---|---|---|---|"] + ["| %s | %s | %s | %s | %s | %s | %s | %s |" % (st["shot"], st["source"], st["ref"], st["search_terms"], st["license_status"], st["checked"], "JA" if st["missing"] else "–", st["alternative"] or "–") for st in r["stock"]] + ["", "Faktenquellen: " + " · ".join(r["facts"]["sources"]), ""]
    open(OUT+"07_STOCK_QUELLEN.md", "w", encoding="utf-8").write("\n".join(L))
    # Scorecards
    with open(OUT+"10_QUALITAET_SCORECARDS.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Reel","Datum","Titel","Entscheidung v4","Struktur","Hook 25","Visuell 25","Story 20","Share 15","DACH 5","Fakten 10","Gesamt","Freigabestatus","Überarbeitungen"])
        for r in reels:
            s = r["scorecard"]["scores"]; w.writerow([r["id"], r["date_de"], r["title"], r["decision_v3"], r["structure"], s["hook"], s["visual"], s["story"], s["share"], s["dach"], s["facts"], r["scorecard"]["total"], r["approval"]["status"], len(r["scorecard"]["iterations"])])
    avg = sum(r["scorecard"]["total"] for r in reels)/len(reels)
    L = ["# Qualitäts-Scorecards (39 Reels · Fassung v4 · Final-Audit)", "", "Gewichtung laut Final-Audit: Hook/erster Frame 25 % · Visuelle Faszination 25 % · Storytelling 20 % · Share-/Follow-Potenzial 15 % · DACH-Relevanz 5 % · Fakten/Umsetzbarkeit 10 %. Noten 1–10 sind **Einschätzungen der Redaktion nach mindestens zwei Überarbeitungsrunden** (Soll-Zustand des Konzepts), keine Messwerte und keine Erfolgsversprechen. Ein Score ersetzt keine Rechte-, Fakten- oder Materialprüfung. Ziel ≥ 9,0 – wo es nicht erreicht wird, steht der Grund im Protokoll.", "",
         "Durchschnitt: **%.2f** · ≥ 9,0: %d Reels · 8,5–8,99: %d · < 8,5: %d" % (avg, sum(1 for r in reels if r["scorecard"]["total"] >= 9), sum(1 for r in reels if 8.5 <= r["scorecard"]["total"] < 9), sum(1 for r in reels if r["scorecard"]["total"] < 8.5)), "",
         "| Reel | Titel | v3 | Str. | Hook | Vis | Story | Share | DACH | Fakt | **Gesamt** | Freigabe |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in reels:
        s = r["scorecard"]["scores"]; L.append("| %s | %s | %s | %s | %d | %d | %d | %d | %d | %d | **%.2f** | %s |" % (r["id"], r["title"], r["decision_v3"], r["structure"], s["hook"], s["visual"], s["story"], s["share"], s["dach"], s["facts"], r["scorecard"]["total"], r["approval"]["status"]))
    L += ["", "## Verbesserungsprotokoll je Reel", ""]
    for r in reels:
        L += ["### %s · %s" % (r["id"], r["title"]), ""] + ["- **Runde %d:** %s" % (i+1, it) for i, it in enumerate(r["scorecard"]["iterations"])] + ["- **Offen:** " + ("; ".join(r["open_points"]) if r["open_points"] else "nichts"), ""]
    open(OUT+"10_QUALITAET_SCORECARDS.md", "w", encoding="utf-8").write("\n".join(L))
    return avg

if __name__ == "__main__":
    import sys
    only = [a for a in sys.argv[1:] if a.startswith("r0")]
    reels = [build_reel(d) for d in load_all(only or None)]
    bad = 0
    for r in reels:
        e = lint(r)
        if e: bad += 1; print(r["id"], "LINT:", "; ".join(e))
    print("Reels:", len(reels), "Lint-Hinweise in", bad)
    if not only:
        for w in global_checks(reels): print("GLOBAL:", w)
    if "--write" in sys.argv:
        avg = write_outputs(reels); print("geschrieben; Ø Scorecard %.2f" % avg)
    for r in reels:
        ks = "/".join(k["status"][:4] for k in r["key_shots"])
        print("%s %s %2ds→%5.1fs %3dW %d Sz Hook★=%.2f QS=%.2f KS=%s %s" % (r["id"], r["structure"], r["target_sec"], r["cut"]["total_sec"], r["vo"]["words"], len(r["cut"]["scenes"]), r["hooks"][[h["winner"] for h in r["hooks"]].index(True)]["total"], r["scorecard"]["total"], ks, r["title"][:38]))
