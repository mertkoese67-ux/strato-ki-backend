#!/usr/bin/env python3
"""Automatische SEO-Qualitätsprüfung aller Entwürfe in BLOG_ARTIKEL/.

Aufruf:  python3 qa_check.py [--links]
  --links  prüft zusätzlich alle externen Quellen-URLs per HTTP (langsamer)

Ergebnis: _arbeitsdaten/qa_ergebnis.json und eine Markdown-Tabelle auf stdout.
"""
import csv, json, os, re, sys, glob, itertools, urllib.request
import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
ART = os.path.join(ROOT, "BLOG_ARTIKEL")

plan = {r["Nr"]: r for r in csv.DictReader(open(os.path.join(ROOT, "REDAKTIONSPLAN_3_MONATE.csv"), encoding="utf-8-sig"), delimiter=";")}
allowed = set(l.strip() for l in open(os.path.join(BASE, "interne_url_liste.txt")) if l.strip())
planned = {r["Ziel-URL"] for r in plan.values()}

FLOSKELN = ["in der heutigen zeit", "tauche ein", "taucht ein", "atemberaubend", "ein wahres paradies", "unvergesslich",
            "zusammenfassend lässt sich sagen", "egal ob du", "es kommt darauf an.", "ultimative", "perfekte urlaub", "traumhaft schön"]
REQ = ["nr", "titel_h1", "seo_title", "meta_description", "slug", "ziel_url", "wp_kategorie", "schlagwoerter", "fokus_keyword",
       "veroeffentlichung", "status", "beitragsbild", "quellen_geprueft_am"]


def tokens(s):
    return [t for t in re.findall(r"[a-zäöüß0-9]+", s.lower()) if len(t) > 2 and t not in {"und", "oder", "für", "der", "die", "das", "mit", "im", "in"}]


def covers(kw, text):
    t = text.lower().replace("-", " ")
    return all(tok in t for tok in tokens(kw))


def parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        return None, raw
    return yaml.safe_load(m.group(1)), m.group(2)


def shingles(text, k=6):
    w = re.findall(r"\w+", text.lower())
    return {" ".join(w[i:i + k]) for i in range(max(0, len(w) - k))}


def check_url(u):
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (haydi-weg QA)"}, method="GET")
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)[:40]


def main():
    do_links = "--links" in sys.argv
    results, bodies, kws = [], {}, {}
    for path in sorted(glob.glob(os.path.join(ART, "*.md"))):
        fn = os.path.basename(path)
        fm, body = parse(path)
        issues, warns = [], []
        if fm is None:
            results.append({"datei": fn, "status": "FEHLER", "issues": ["Kein Frontmatter"]}); continue
        for k in REQ:
            if k not in fm or fm[k] in (None, "", []):
                issues.append(f"Feld fehlt: {k}")
        nr = f"{int(fm.get('nr', 0)):02d}"
        p = plan.get(nr, {})
        st, md = str(fm.get("seo_title", "")), str(fm.get("meta_description", ""))
        if len(st) > 60: issues.append(f"SEO-Title {len(st)} Zeichen (>60)")
        if not 120 <= len(md) <= 160: issues.append(f"Meta-Description {len(md)} Zeichen (Soll 130–155)")
        elif not 130 <= len(md) <= 155: warns.append(f"Meta-Description {len(md)} Zeichen")
        kw = str(fm.get("fokus_keyword", ""))
        kws.setdefault(kw.lower(), []).append(nr)
        h1 = re.search(r"^# (.+)$", body, re.M)
        h1t = h1.group(1) if h1 else ""
        if not h1: issues.append("Keine H1 im Body")
        h2s = re.findall(r"^## (.+)$", body, re.M)
        paras = [b for b in re.split(r"\n\s*\n", body) if b.strip() and not b.strip().startswith(("#", "<!--", "|", ">", "-", "*"))]
        first = paras[0] if paras else ""
        kwc = {"H1": covers(kw, h1t), "Einstieg": covers(kw, " ".join(paras[:2])), "H2": any(covers(kw, h) for h in h2s), "Meta": covers(kw, md)}
        miss = [k for k, v in kwc.items() if not v]
        if len(miss) >= 2: issues.append("Fokus-Keyword fehlt in: " + ", ".join(miss))
        elif miss: warns.append("Fokus-Keyword fehlt in: " + ", ".join(miss))
        text = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        wc = len(re.findall(r"\w+", text))
        soll = int(p.get("Geplante Länge (Wörter)", 0) or 0)
        if soll and not (0.8 * soll <= wc <= 1.3 * soll):
            (issues if wc < 0.7 * soll else warns).append(f"Wortzahl {wc} (Plan {soll})")
        links = re.findall(r"\]\((https?://[^)\s]+)\)", body)
        internal = [l for l in links if "haydiweg.de" in l]
        external = [l for l in links if "haydiweg.de" not in l and "wa.me" not in l]
        bad = [l for l in internal if l.split("#")[0] not in allowed and l.split("#")[0] not in planned]
        if bad: issues.append("Unbekannte interne URLs: " + ", ".join(bad))
        uniq_int = {l.split("#")[0] for l in internal if "/buchen/" not in l}
        if not 4 <= len(uniq_int) + (1 if any("/buchen/" in l for l in internal) else 0) <= 14:
            warns.append(f"{len(uniq_int)} unterschiedliche interne Links")
        planned_links = sorted({l for l in internal if l in planned and l not in allowed})
        if not any("wa.me" in l for l in links): warns.append("Kein WhatsApp-Link")
        faq = re.search(r"^## Häufige Fragen\s*$(.*?)(?=^## )", body, re.M | re.S)
        nfaq = len(re.findall(r"^### ", faq.group(1), re.M)) if faq else 0
        if not 4 <= nfaq <= 7: issues.append(f"FAQ-Fragen: {nfaq}")
        q = re.search(r"^## Quellen\s*$(.*)", body, re.M | re.S)
        nq = len(re.findall(r"https?://", q.group(1))) if q else 0
        if nq < 2: issues.append(f"Quellen: {nq}")
        pruef = len(re.findall(r"\[PRÜFEN", body))
        medien = len(re.findall(r"MEDIENPRÜFUNG", body + json.dumps(fm, ensure_ascii=False, default=str)))
        low = text.lower()
        fl = [f for f in FLOSKELN if f in low]
        if fl: warns.append("Floskeln: " + ", ".join(fl))
        euros = [m for m in re.findall(r"[^\n]{0,30}\d[\d.,]*\s?(?:€|Euro)[^\n]{0,10}", text) if "1.000" not in m and "Cashback" not in m]
        if euros: warns.append(f"Euro-Beträge prüfen ({len(euros)}): " + " | ".join(e.strip()[:50] for e in euros[:3]))
        if "snapinsta" in body.lower() or "screenshot" in json.dumps(fm, default=str).lower(): issues.append("Bild mit ungeklärten Rechten referenziert")
        if fm.get("slug") != p.get("Slug"): warns.append(f"Slug weicht vom Plan ab ({fm.get('slug')})")
        bodies[nr] = shingles(text)
        ext_status = {}
        if do_links:
            for u in sorted(set(external)):
                ext_status[u] = check_url(u)
            dead = {u: s for u, s in ext_status.items() if not (isinstance(s, int) and s < 400)}
            if dead: warns.append(f"Externe Links nicht erreichbar/blockiert ({len(dead)}): " + ", ".join(f"{u} [{s}]" for u, s in list(dead.items())[:4]))
        results.append({"datei": fn, "nr": nr, "titel": fm.get("titel_h1"), "woerter": wc, "soll": soll, "seo_title_len": len(st),
                        "meta_len": len(md), "kw_abdeckung": kwc, "interne_links": len(uniq_int), "geplante_links": planned_links,
                        "externe_quellen": nq, "faq": nfaq, "pruefen_marker": pruef, "medienpruefung": medien,
                        "issues": issues, "warnungen": warns, "ext_status": ext_status,
                        "status": "BESTANDEN" if not issues else "ÜBERARBEITEN"})
    # Duplikate / Kannibalisierung
    dups = []
    for a, b in itertools.combinations(sorted(bodies), 2):
        sa, sb = bodies[a], bodies[b]
        if sa and sb:
            j = len(sa & sb) / len(sa | sb)
            if j > 0.08: dups.append((a, b, round(j, 3)))
    kwdup = {k: v for k, v in kws.items() if len(v) > 1}
    out = {"artikel": results, "textueberschneidung": dups, "fokus_keyword_doppelt": kwdup}
    json.dump(out, open(os.path.join(BASE, "qa_ergebnis.json"), "w"), ensure_ascii=False, indent=1)
    print("| Nr | Wörter (Soll) | Title | Meta | KW H1/Einst./H2/Meta | int. Links | Quellen | FAQ | [PRÜFEN] | Medienprüf. | Status |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        if "nr" not in r: print(f"| {r['datei']} | – | – | – | – | – | – | – | – | – | {r['status']} |"); continue
        k = r["kw_abdeckung"]; kk = "/".join("✓" if k[x] else "✗" for x in ["H1", "Einstieg", "H2", "Meta"])
        print(f"| {r['nr']} | {r['woerter']} ({r['soll']}) | {r['seo_title_len']} | {r['meta_len']} | {kk} | {r['interne_links']} | {r['externe_quellen']} | {r['faq']} | {r['pruefen_marker']} | {r['medienpruefung']} | {r['status']} |")
    print("\nTextüberschneidungen (Jaccard 6-Wort-Shingles > 0,08):", dups or "keine")
    print("Doppelte Fokus-Keywords:", kwdup or "keine")
    for r in results:
        if r.get("issues") or r.get("warnungen"):
            print(f"\n{r['datei']}:")
            for i in r.get("issues", []): print("  FEHLER:", i)
            for w in r.get("warnungen", []): print("  Hinweis:", w)


if __name__ == "__main__":
    main()
