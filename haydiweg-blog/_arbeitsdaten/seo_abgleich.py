#!/usr/bin/env python3
"""Abgleich der Blog-Entwürfe mit den Seiten-SEO-Vorgaben (Projekt 2) bzw. dem Live-Stand.

Prüft:
  1. Doppelte oder fast identische SEO-Titel (Blog vs. Seiten, Blog vs. Blog)
  2. Doppelte Meta-Descriptions
  3. Konkurrierende Fokus-Keywords (Blog-Fokus-Keyword deckt sich mit Titel/H1 einer Seite)
  4. Geschätzte Pixelbreite der Titel (Google-Desktop ca. 580–600 px, Arial 20 px Näherung)

Aufruf:
  python3 seo_abgleich.py                         # gegen Live-Stand vom 05.11.2026
  python3 seo_abgleich.py <pfad/SEO_TITEL_VORHER_NACHHER.csv> [<pfad/SEO_META_DESCRIPTIONS.csv>]
     -> gegen die finalen Titel aus Projekt 2 (Spaltennamen werden automatisch erkannt)

Ausgabe: _arbeitsdaten/seo_abgleich_ergebnis.csv + Zusammenfassung auf stdout.
"""
import csv, glob, os, re, sys, difflib
import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

# Näherungsweise Zeichenbreiten in px für Arial 20px (Google-Titel), Rest = 11 px
W = {**{c: 6 for c in "ijlI.,:;!|'"}, **{c: 7 for c in "frt()-[] "}, **{c: 10 for c in "cksvxyzJ"},
     **{c: 11 for c in "abdeghnopquäöüß0123456789?€&"}, **{c: 15 for c in "mwMW"}, **{c: 14 for c in "ABCDEFGHKNOPQRSTUVXYZÄÖÜ"}, "–": 11, "/": 6}


def px(s):
    return sum(W.get(c, 11) for c in s)


def load_blog():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "BLOG_ARTIKEL", "*.md"))):
        m = re.match(r"^---\n(.*?)\n---\n", open(p, encoding="utf-8").read(), re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1))
        out.append({"quelle": "Blog", "id": f"#{int(fm['nr']):02d}", "url": fm.get("ziel_url", ""), "title": fm.get("seo_title", ""),
                    "desc": fm.get("meta_description", ""), "h1": fm.get("titel_h1", ""), "kw": fm.get("fokus_keyword", "")})
    return out


def pick(row, *names):
    for n in names:
        for k in row:
            if k and k.strip().lower() == n:
                return row[k]
    for n in names:
        for k in row:
            if k and n in k.strip().lower():
                return row[k]
    return ""


def load_pages(title_csv=None, desc_csv=None):
    pages = {}
    if title_csv:
        sample = open(title_csv, encoding="utf-8-sig").read(4096)
        d = csv.Sniffer().sniff(sample, delimiters=";,\t")
        for r in csv.DictReader(open(title_csv, encoding="utf-8-sig"), dialect=d):
            u = pick(r, "url")
            if u:
                pages[u] = {"quelle": "Projekt 2", "id": u, "url": u, "title": pick(r, "finaler titel", "final", "empfohlen"), "desc": "", "h1": pick(r, "h1"), "kw": pick(r, "hauptkeyword", "keyword")}
        if desc_csv:
            d = csv.Sniffer().sniff(open(desc_csv, encoding="utf-8-sig").read(4096), delimiters=";,\t")
            for r in csv.DictReader(open(desc_csv, encoding="utf-8-sig"), dialect=d):
                u = pick(r, "url")
                if u in pages:
                    pages[u]["desc"] = pick(r, "finale meta", "final", "neu", "meta")
    else:
        for r in csv.DictReader(open(os.path.join(BASE, "live_seo_stand_2026-11-05.csv"), encoding="utf-8-sig"), delimiter=";"):
            pages[r["url"]] = {"quelle": "Live 05.11.", "id": r["url"], "url": r["url"], "title": r["title"], "desc": r["meta_description"], "h1": r["h1"], "kw": ""}
    return list(pages.values())


def norm(s):
    s = re.sub(r"\|\s*haydi-weg.*$", "", (s or "").lower())
    return re.sub(r"[^a-zäöüß0-9 ]", " ", s).split()


def toks(kw):
    return [t for t in re.findall(r"[a-zäöüß0-9]+", (kw or "").lower()) if len(t) > 2 and t not in {"und", "oder", "mit", "für", "der", "die", "das"}]


def main():
    blog = load_blog()
    pages = load_pages(*(sys.argv[1:3] if len(sys.argv) > 1 else []))
    rows = []
    for b in blog:
        p_w = px(b["title"])
        if p_w > 580:
            rows.append([b["id"], "Titel-Pixelbreite", f"{p_w}px > 580px (Kürzung wahrscheinlich)", b["title"], ""])
        for o in pages + [x for x in blog if x is not b]:
            r = difflib.SequenceMatcher(None, " ".join(norm(b["title"])), " ".join(norm(o["title"]))).ratio()
            if r > 0.8:
                rows.append([b["id"], "Titel ähnlich", f"{r:.2f}", b["title"], f"{o['id']}: {o['title']}"])
            if b["desc"] and o.get("desc") and b["desc"].strip() == o["desc"].strip():
                rows.append([b["id"], "Meta doppelt", "", b["desc"], o["id"]])
            if o["quelle"] != "Blog":
                t = toks(b["kw"])
                hay = " ".join(norm(o["title"]) + norm(o["h1"]) + toks(o.get("kw", "")))
                if t and all(x in hay for x in t):
                    rows.append([b["id"], "Keyword-Überschneidung", f"Fokus '{b['kw']}' steckt vollständig in Seitentitel/H1", b["title"], f"{o['id']}: {o['title']}"])
    seen = set(); uniq = []
    for r in rows:
        k = (r[0], r[1], r[4][:60])
        if k not in seen:
            seen.add(k); uniq.append(r)
    with open(os.path.join(BASE, "seo_abgleich_ergebnis.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["Blog-Nr", "Befund", "Detail", "Blog-Wert", "Konflikt mit"]); w.writerows(uniq)
    print(f"Geprüft: {len(blog)} Blog-Entwürfe gegen {len(pages)} Seiten ({pages[0]['quelle'] if pages else '-'}). Befunde: {len(uniq)}")
    for r in uniq:
        print(" | ".join(r))


if __name__ == "__main__":
    main()
