#!/usr/bin/env python3
"""Erzeugt BLOG_SEO_KEYWORD_MAP.csv – maschinenlesbare Übergabe an das SEO-Projekt (Projekt 2).
Eine Zeile pro Blog-Entwurf: URL, SEO-Title (+ Pixelbreite), Meta, Fokus-/Nebenkeywords, Pillar, Status.
"""
import csv, glob, os, re, sys
import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, BASE)
from seo_abgleich import px  # gleiche Pixel-Näherung wie im Abgleich

plan = {}
for r in csv.DictReader(open(os.path.join(ROOT, "REDAKTIONSPLAN_3_MONATE.csv"), encoding="utf-8-sig"), delimiter=";"):
    plan[r["Slug"]] = r

rows = []
for p in sorted(glob.glob(os.path.join(ROOT, "BLOG_ARTIKEL", "*.md"))):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", open(p, encoding="utf-8").read(), re.S)
    if not m:
        continue
    fm, body = yaml.safe_load(m.group(1)), m.group(2)
    pl = plan.get(fm["slug"], {})
    pillar = next((u.strip() for u in pl.get("Interne Links (bestehend)", "").split(";") if "/urlaubsziele/" in u or u.strip().endswith(("/pauschalreisen/", "/familienurlaub/"))), "")
    rows.append({
        "Plan-Nr": pl.get("Nr", fm["nr"]),
        "Ziel-URL": fm["ziel_url"],
        "Geplant": pl.get("Datum", ""),
        "Status": pl.get("Status", ""),
        "Kategorie": fm["wp_kategorie"],
        "H1": fm["titel_h1"],
        "SEO-Title": fm["seo_title"],
        "Title Zeichen": len(fm["seo_title"]),
        "Title px (Näherung)": px(fm["seo_title"]),
        "Meta-Description": fm["meta_description"],
        "Meta Zeichen": len(fm["meta_description"]),
        "Fokus-Keyword": fm["fokus_keyword"],
        "Nebenkeywords": "; ".join(fm.get("nebenkeywords") or []),
        "Suchintention": pl.get("Suchintention", ""),
        "Pillar-Seite": pillar,
        "Offene [PRÜFEN]": len(re.findall(r"\[PRÜFEN", body)),
    })

out = os.path.join(ROOT, "BLOG_SEO_KEYWORD_MAP.csv")
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
    w.writeheader(); w.writerows(rows)
print(len(rows), "Zeilen ->", out)
