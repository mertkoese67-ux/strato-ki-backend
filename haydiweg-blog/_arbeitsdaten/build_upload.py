#!/usr/bin/env python3
"""Baut aus BLOG_ARTIKEL/*.md alle Upload-Dateien im aktuellen haydi-weg-Beitragsformat.

Format = wie der Live-Beitrag „Türkei-Hotels mit Aquapark“ (ID 7586): reines HTML im Beitragsinhalt
(p, h2, h3, ul/ol, table, Links), „Häufige Fragen“ als H2 mit H3/P-Paaren und FAQPage-JSON-LD am Ende.
Kopf, Titelbild, Breadcrumb, Kategorie, Datum, Lesezeit, Inhaltsverzeichnis, FAQ-Akkordeon,
Tabellenrahmen, „Weitere Artikel“ und Schlussbox erzeugt das WPCode-Snippet (hwa-…) der Website automatisch.

Ausgabe:
  ARTIKEL_ZUM_HOCHLADEN/NN-slug.html   -> Inhalt zum Einfügen in den Code-Editor
  ARTIKEL_ZUM_HOCHLADEN/STECKBRIEFE.md -> alle Felder je Artikel (Titel, Slug, URL, Autor, Termin, Rank Math, Bild)
  ARTIKEL_ZUM_HOCHLADEN/UPLOAD_UEBERSICHT.csv
  VORSCHAU/NN-slug.html                -> Vorschau im Live-Design (braucht Internet für CSS/Fonts)
  WORDPRESS_IMPORT/haydiweg-blog-entwuerfe.xml       -> alle freigegebenen Artikel als Entwurf
  WORDPRESS_IMPORT/haydiweg-blog-geplant.xml         -> dieselben Artikel als „geplant“ (veröffentlichen automatisch!)
  WORDPRESS_IMPORT/haydiweg-blog-dubai-zurueckgestellt.xml -> Dubai-Artikel als Entwurf
  NACHVERLINKUNG.md                    -> Links, die erst nach Veröffentlichung des Zielartikels gesetzt werden
"""
import csv, glob, html, json, os, re
from datetime import datetime
import markdown, yaml
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
UP = os.path.join(ROOT, "ARTIKEL_ZUM_HOCHLADEN")
PV = os.path.join(ROOT, "VORSCHAU")
WX = os.path.join(ROOT, "WORDPRESS_IMPORT")
for d in (UP, PV, WX):
    os.makedirs(d, exist_ok=True)

WHATSAPP = "4915792326450"          # aktuelle Nummer (0157 92326450) – bei Änderung hier anpassen und neu bauen
HOLD = {"05", "10", "27"}            # Dubai: Auswärtiges Amt rät von nicht notwendigen Reisen in die VAE ab
AUTOREN = {
    "burak-mert-koese": ("Burak Mert", "Köse"),
    "emre-koese": ("Emre", "Köse"),
    "leon-sulemani": ("Leon", "Sulemani"),
}
# Zuordnung nach Themenschwerpunkt (jederzeit änderbar)
AUTOR_JE_NR = {}
for n in ["04", "06", "08", "09", "12", "14", "17", "23", "25", "28", "31", "35", "R1"]:
    AUTOR_JE_NR[n] = "burak-mert-koese"     # Türkei + Buchungsthemen
for n in ["02", "03", "05", "07", "10", "15", "19", "20", "22", "26", "27", "33"]:
    AUTOR_JE_NR[n] = "emre-koese"           # Ägypten, Dubai, Fernreisen
for n in ["01", "11", "13", "16", "18", "21", "24", "29", "30", "32", "34", "36", "R2", "R3"]:
    AUTOR_JE_NR[n] = "leon-sulemani"        # Spanien/Portugal, Griechenland/Zypern, Reiseplanung
KAT_SLUG = {"Türkei": "tuerkei", "Ägypten": "aegypten", "Spanien": "spanien", "Griechenland": "griechenland",
            "Dubai": "dubai", "Fernreisen": "fernreisen", "Reiseplanung": "reiseplanung", "Zypern": "zypern", "Portugal": "portugal"}
RECHTE_UNKLAR = {876, 878, 880, 883, 4083}   # laut Recherche wie Stock-/KI-Bilder – nicht automatisch als Beitragsbild setzen
EXISTING_TAGS = {"Aquapark", "Belek", "Familienurlaub", "Kemer", "Lara", "Side"}
MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
WT = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]


def slugify(s):
    s = s.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def cdata(s):
    return "<![CDATA[" + str(s).replace("]]>", "]]]]><![CDATA[>") + "]]>"


# ---------- Daten laden ----------
plan = {r["Slug"]: r for r in csv.DictReader(open(os.path.join(ROOT, "REDAKTIONSPLAN_3_MONATE.csv"), encoding="utf-8-sig"), delimiter=";")}
media = {}
for r in csv.DictReader(open(os.path.join(BASE, "mediathek_inventar.tsv"), encoding="utf-8"), delimiter="\t"):
    try:
        media[int(r["id"])] = r
    except (ValueError, KeyError):
        pass

arts = []
for p in sorted(glob.glob(os.path.join(ROOT, "BLOG_ARTIKEL", "*.md"))):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", open(p, encoding="utf-8").read(), re.S)
    fm, body = yaml.safe_load(m.group(1)), m.group(2)
    pl = plan[fm["slug"]]
    nr = pl["Nr"]
    if nr in HOLD:
        dt = None
    else:
        d, mth, y = pl["Datum"].split(".")
        dt = datetime.fromisoformat(f"{y}-{mth}-{d}T{pl['Uhrzeit']}:00")
    kat = fm["wp_kategorie"]
    url = f"https://haydiweg.de/{KAT_SLUG[kat]}/{fm['slug']}/"
    arts.append({"nr": nr, "fm": fm, "body": body, "dt": dt, "url": url, "kat": kat, "datei": os.path.basename(p)[:-3],
                 "autor": AUTOR_JE_NR[nr]})
by_url = {a["url"]: a for a in arts}
for a in arts:
    assert a["url"] == a["fm"]["ziel_url"], (a["nr"], a["url"], a["fm"]["ziel_url"])

nachverlinkung = []


# ---------- Markdown -> Beitrags-HTML ----------
def faq_pairs(soup):
    out, h = [], soup.find(lambda t: t.name == "h2" and t.get_text(strip=True) == "Häufige Fragen")
    if not h:
        return out
    for el in h.find_next_siblings():
        if el.name == "h2":
            break
        if el.name == "h3":
            ans = []
            for sib in el.find_next_siblings():
                if sib.name in ("h2", "h3"):
                    break
                ans.append(sib.get_text(" ", strip=True))
            out.append((el.get_text(" ", strip=True), " ".join(ans)))
    return out


def build_content(a):
    body = a["body"]
    body = re.sub(r"^# .+\n", "", body, count=1, flags=re.M)                # H1 = Beitragstitel
    body = re.sub(r"<!--\s*BILD:.*?-->\s*\n?", "", body, flags=re.S)        # Bilder stehen im Steckbrief
    # „Das Wichtigste in Kürze“-Kasten (Blockquote) -> Absatz + Liste wie im Live-Design
    def bq(mm):
        lines = [re.sub(r"^>\s?", "", l) for l in mm.group(0).splitlines()]
        return "\n".join(lines) + "\n"
    body = re.sub(r"(?:^>.*\n?)+", bq, body, flags=re.M)
    body = re.sub(r"^\*\*Das Wichtigste in Kürze\*\*\s*$", "**Das Wichtigste in Kürze**\n", body, flags=re.M)
    h = markdown.markdown(body, extensions=["tables", "sane_lists"])
    soup = BeautifulSoup(h, "html.parser")
    for c in soup.find_all(string=lambda t: isinstance(t, type(soup.new_string(""))) and False):
        pass
    # Kommentare entfernen
    from bs4 import Comment
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    # Links prüfen und formatieren
    for link in soup.find_all("a", href=True):
        href = link["href"].strip()
        if href.startswith("https://wa.me/"):
            href = re.sub(r"wa\.me/\d+", f"wa.me/{WHATSAPP}", href)
            link["href"] = href
            link["target"] = "_blank"; link["rel"] = "noopener"
        elif "haydiweg.de" in href:
            tgt = by_url.get(href.split("#")[0])
            if tgt is not None:
                ok = tgt["dt"] is not None and a["dt"] is not None and tgt["dt"] <= a["dt"]
                if not ok:
                    nachverlinkung.append((a, tgt, link.get_text(" ", strip=True)))
                    link.unwrap()
        else:
            link["target"] = "_blank"; link["rel"] = "noopener"
    # Quellen: nackte URLs verlinken
    q = soup.find(lambda t: t.name == "h2" and t.get_text(strip=True) == "Quellen")
    if q:
        ul = q.find_next_sibling(["ul", "ol"])
        if ul:
            for li in ul.find_all("li"):
                if not li.find("a"):
                    txt = str(li.decode_contents())
                    txt = re.sub(r"(https?://[^\s,<]+[^\s,.<;)])", r'<a href="\1" target="_blank" rel="noopener">\1</a>', txt)
                    li.clear(); li.append(BeautifulSoup(txt, "html.parser"))
    # Fokus-Keyword im ersten Absatz fett (wie im Live-Beitrag), nur bei exakter Übereinstimmung
    first = soup.find("p")
    kw = str(a["fm"]["fokus_keyword"])
    if first and not first.find("strong"):
        s = str(first)
        i = s.lower().find(kw.lower())
        if i > 0:
            s = s[:i] + "<strong>" + s[i:i + len(kw)] + "</strong>" + s[i + len(kw):]
            first.replace_with(BeautifulSoup(s, "html.parser"))
    faqs = faq_pairs(soup)
    out = str(soup).strip()
    out = re.sub(r"\n{3,}", "\n\n", out)
    if faqs:
        ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q_, "acceptedAnswer": {"@type": "Answer", "text": a_}} for q_, a_ in faqs]}
        out += '\n\n<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + "\n</script>\n"
    return out, faqs


# ---------- Vorschau im Live-Design ----------
TPL = open(os.path.join(BASE, "design_vorlage_beitrag.html"), encoding="utf-8").read()


def bild_info(a):
    bb = a["fm"].get("beitragsbild") or {}
    q = str(bb.get("quelle", ""))
    mid = re.search(r"Mediathek-ID\s*(\d+)", q)
    mid = int(mid.group(1)) if mid else None
    rec = media.get(mid) if mid else None
    auto = bool(rec) and mid not in RECHTE_UNKLAR and str(rec.get("mime", "")).startswith("image/")
    return {"id": mid if rec else None, "url": rec["url"] if rec else "", "alt": bb.get("alt", ""), "datei": bb.get("datei", ""),
            "auto": auto, "quelle": q}


def preview(a, content):
    soup = BeautifulSoup(TPL, "html.parser")
    for el in soup.select(".hwcc, #hwcc, [class^=hwcc]"):
        el.decompose()
    root = soup.select_one("div.hwa.hwa--beitrag")
    kopf = root.select_one("header.hwa-kopf")
    b = bild_info(a)
    img = kopf.select_one("figure.hwa-kopfbild img")
    for k in ("srcset", "sizes", "width", "height"):
        img.attrs.pop(k, None)
    if b["url"]:
        img["src"] = b["url"]; img["alt"] = b["alt"]
    else:
        img["src"] = "data:image/svg+xml;utf8," + html.escape(
            "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='700'><rect width='100%' height='100%' fill='#dfe6ee'/>"
            "<text x='50%' y='50%' font-family='sans-serif' font-size='42' fill='#51607a' text-anchor='middle'>Beitragsbild: "
            + html.escape(b["datei"] or "noch auswählen") + "</text></svg>")
        img["alt"] = b["alt"]
    kopf.select("nav.hwa-pfad span")[-1].string = a["fm"]["titel_h1"]
    kopf.select_one(".hwa-pille").string = a["kat"]
    kopf.select_one("h1").string = a["fm"]["titel_h1"]
    words = len(BeautifulSoup(content, "html.parser").get_text(" ").split())
    datum = f"{a['dt'].day}. {MONATE[a['dt'].month - 1]} {a['dt'].year}" if a["dt"] else "Termin offen"
    kopf.select_one("p.hwa-meta").clear()
    kopf.select_one("p.hwa-meta").append(f"{datum} · {max(1, round(words / 230))} Min. Lesezeit")
    # Inhalt + automatische Elemente nachbilden
    cs = BeautifulSoup(content, "html.parser")
    for s in cs.find_all("script"):
        s.decompose()
    toc = []
    for h2 in cs.find_all("h2"):
        t = h2.get_text(" ", strip=True)
        hid = "fragen" if t == "Häufige Fragen" else slugify(t)
        h2["id"] = hid; toc.append((hid, t))
    for t in cs.find_all("table"):
        w = cs.new_tag("div", attrs={"class": "hwa-tabelle"}); t.wrap(w)
    fh = cs.find(id="fragen")
    if fh:
        sec = cs.new_tag("section", attrs={"class": "hwa-faq", "aria-label": "Häufige Fragen"})
        fh.insert_before(sec)
        els = [fh] + [e for e in list(fh.find_next_siblings()) if True]
        stop = False; cur = None
        sec.append(fh.extract())
        for e in els[1:]:
            if e.name == "h2":
                break
            if e.name == "h3":
                cur = cs.new_tag("details"); sm = cs.new_tag("summary"); sm.string = e.get_text(" ", strip=True)
                cur.append(sm); ans = cs.new_tag("div", attrs={"class": "hwa-faq-antwort"}); cur.append(ans)
                sec.append(cur); e.decompose()
            elif cur is not None:
                cur.select_one(".hwa-faq-antwort").append(e.extract())
    text = root.select_one(".hwa-text")
    text.clear(); text.append(cs)
    ol = root.select_one("details.hwa-inhalt ol")
    ol.clear()
    for hid, t in toc:
        li = soup.new_tag("li"); aa = soup.new_tag("a", href="#" + hid); aa.string = t; li.append(aa); ol.append(li)
    knopf = soup.select_one(".hwa-schluss a.hwa-knopf")
    if knopf:
        from urllib.parse import quote
        knopf["href"] = f"https://wa.me/{WHATSAPP}?text=" + quote(f"Hallo haydi-weg, ich habe euren Artikel „{a['fm']['titel_h1']}“ gelesen und hätte eine Frage:")
    soup.title.string = f"VORSCHAU – {a['fm']['seo_title']}"
    banner = BeautifulSoup('<div style="position:sticky;top:0;z-index:99999;background:#fff3c4;color:#222;padding:8px 14px;'
                           'font:14px/1.4 sans-serif;border-bottom:2px solid #f2c200">Vorschau (lokal erzeugt) – so stellt das '
                           'haydi-weg-Beitragsdesign diesen Artikel dar. Kopfzeile, Footer und „Weitere Artikel“ stammen vom '
                           'Live-Beitrag.</div>', "html.parser")
    soup.body.insert(0, banner)
    return str(soup)


# ---------- Build ----------
rows, items_draft, items_future, items_hold, steck = [], [], [], [], []
tags_all = {}
from collections import Counter
tc = Counter(t for a in arts for t in set(a["fm"].get("schlagwoerter") or []))
ALLOWED = {t for t, n in tc.items() if n >= 2} | EXISTING_TAGS
for a in sorted(arts, key=lambda x: (x["dt"] is None, x["dt"] or datetime.max)):
    fm = a["fm"]
    content, faqs = build_content(a)
    if "PRÜFEN" in content and not os.environ.get("HW_TEST"):
        raise SystemExit(f"{a['nr']}: offene PRÜFEN-Marker – erst Endredaktion abschließen")
    open(os.path.join(UP, a["datei"] + ".html"), "w", encoding="utf-8").write(content + "\n")
    open(os.path.join(PV, a["datei"] + ".html"), "w", encoding="utf-8").write(preview(a, content))
    vor, nach = AUTOREN[a["autor"]]
    tags = [t for t in (fm.get("schlagwoerter") or []) if t in ALLOWED]
    for t in tags:
        tags_all[slugify(t)] = t
    b = bild_info(a)
    termin = a["dt"].strftime("%d.%m.%Y %H:%M") if a["dt"] else "zurückgestellt (Dubai)"
    kw = [str(fm["fokus_keyword"])] + [str(x) for x in (fm.get("nebenkeywords") or [])][:4]
    rows.append({"Nr": a["nr"], "Termin": termin, "Wochentag": WT[a["dt"].weekday()] if a["dt"] else "", "Titel": fm["titel_h1"],
                 "URL": a["url"], "Slug": fm["slug"], "Kategorie": a["kat"], "Kategorie-Slug": KAT_SLUG[a["kat"]],
                 "Autor": f"{vor} {nach}", "Schlagwörter": ", ".join(tags), "Rank Math SEO-Titel": fm["seo_title"],
                 "Rank Math Beschreibung": fm["meta_description"], "Fokus-Keyword": ", ".join(kw),
                 "Beitragsbild": (f"Mediathek-ID {b['id']}" + ("" if b["auto"] else " (Rechte prüfen)")) if b["id"] else "neu auswählen",
                 "Bild-URL": b["url"], "ALT-Text": b["alt"], "Inhalt-Datei": f"ARTIKEL_ZUM_HOCHLADEN/{a['datei']}.html",
                 "Vorschau": f"VORSCHAU/{a['datei']}.html"})
    weitere = "".join(f"\n    - {w.get('datei','')} – ALT: „{w.get('alt','')}“ – {w.get('quelle','')}" for w in (fm.get("weitere_bilder") or []))
    offen = "".join(f"\n- {x}" for x in (fm.get("redaktionelle_pruefung") or [])) or "\n- keine"
    steck.append(f"""
## {a['nr']} · {fm['titel_h1']}

| Feld | Wert |
|---|---|
| **Termin** | {(WT[a['dt'].weekday()] + ', ' + termin) if a['dt'] else '**zurückgestellt** – erst veröffentlichen, wenn das Auswärtige Amt den Reisehinweis für die VAE aufhebt'} |
| **Titel** | {fm['titel_h1']} |
| **URL** | {a['url']} |
| **Permalink/Slug** | `{fm['slug']}` |
| **Kategorie** | {a['kat']} (Slug `{KAT_SLUG[a['kat']]}`) – nur diese eine Kategorie anhaken |
| **Schlagwörter** | {', '.join(tags) or '–'} |
| **Autor** | {vor} {nach} |
| **Inhalt** | `ARTIKEL_ZUM_HOCHLADEN/{a['datei']}.html` → im Code-Editor einfügen |
| **Rank Math: SEO-Titel** | {fm['seo_title']} |
| **Rank Math: Beschreibung** | {fm['meta_description']} |
| **Rank Math: Fokus-Keyword** | {', '.join(kw)} |
| **Auszug (optional)** | {fm['meta_description']} |
| **Beitragsbild** | {('Mediathek-ID ' + str(b['id']) + ' – ' + b['url']) if b['id'] else 'neues Bild: ' + str(b['datei'])}{'' if b['auto'] or not b['id'] else ' – **Rechte/Herkunft vorher prüfen**'} |
| **ALT-Text Beitragsbild** | {b['alt']} |
| **Vorschau** | `VORSCHAU/{a['datei']}.html` |

Weitere Bildideen (optional, im Text nach Bedarf):{weitere or ' –'}

Vor dem Planen klären:{offen}
""")
    # WXR-Item
    meta = {"rank_math_title": fm["seo_title"], "rank_math_description": fm["meta_description"],
            "rank_math_focus_keyword": ",".join(kw), "_hw_redaktionsplan_nr": a["nr"],
            "_hw_beitragsbild_vorschlag": f"{b['datei']} | ALT: {b['alt']} | {b['quelle']}"}
    if b["auto"]:
        meta["_thumbnail_id"] = str(b["id"])
    pm = "".join(f"\n\t\t<wp:postmeta><wp:meta_key>{k}</wp:meta_key><wp:meta_value>{cdata(v)}</wp:meta_value></wp:postmeta>" for k, v in meta.items())
    cats = f'\n\t\t<category domain="category" nicename="{KAT_SLUG[a["kat"]]}">{cdata(a["kat"])}</category>'
    cats += "".join(f'\n\t\t<category domain="post_tag" nicename="{slugify(t)}">{cdata(t)}</category>' for t in tags)
    pdate = (a["dt"] or datetime(2027, 12, 31, 7, 30)).strftime("%Y-%m-%d %H:%M:%S")

    def item(status):
        return f"""
	<item>
		<title>{cdata(fm['titel_h1'])}</title>
		<dc:creator>{cdata(a['autor'])}</dc:creator>
		<description></description>
		<content:encoded>{cdata(content)}</content:encoded>
		<excerpt:encoded>{cdata(fm['meta_description'])}</excerpt:encoded>
		<wp:post_date>{cdata(pdate)}</wp:post_date>
		<wp:post_date_gmt>{cdata('0000-00-00 00:00:00')}</wp:post_date_gmt>
		<wp:comment_status>{cdata('closed')}</wp:comment_status>
		<wp:ping_status>{cdata('closed')}</wp:ping_status>
		<wp:post_name>{cdata(fm['slug'])}</wp:post_name>
		<wp:status>{cdata(status)}</wp:status>
		<wp:post_parent>0</wp:post_parent>
		<wp:menu_order>0</wp:menu_order>
		<wp:post_type>{cdata('post')}</wp:post_type>
		<wp:post_password>{cdata('')}</wp:post_password>
		<wp:is_sticky>0</wp:is_sticky>{cats}{pm}
	</item>"""
    if a["nr"] in HOLD:
        items_hold.append(item("draft"))
    else:
        items_draft.append(item("draft"))
        items_future.append(item("future"))

authors_xml = "".join(
    f"\n\t<wp:author><wp:author_login>{cdata(l)}</wp:author_login><wp:author_email>{cdata('')}</wp:author_email>"
    f"<wp:author_display_name>{cdata(v + ' ' + n)}</wp:author_display_name><wp:author_first_name>{cdata(v)}</wp:author_first_name>"
    f"<wp:author_last_name>{cdata(n)}</wp:author_last_name></wp:author>" for l, (v, n) in AUTOREN.items())
used_cats = sorted({(KAT_SLUG[a["kat"]], a["kat"]) for a in arts})
cat_xml = "".join(f"\n\t<wp:category><wp:category_nicename>{cdata(s)}</wp:category_nicename><wp:category_parent>{cdata('')}</wp:category_parent><wp:cat_name>{cdata(c)}</wp:cat_name></wp:category>" for s, c in used_cats)
tag_xml = "".join(f"\n\t<wp:tag><wp:tag_slug>{cdata(s)}</wp:tag_slug><wp:tag_name>{cdata(t)}</wp:tag_name></wp:tag>" for s, t in sorted(tags_all.items()))


def wxr(items, note):
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<!-- haydi-weg Blog – {note} Erzeugt {datetime.now():%d.%m.%Y %H:%M}. -->
<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">
<channel>
	<title>haydi-weg</title>
	<link>https://haydiweg.de</link>
	<description>haydi-weg Reise-Blog</description>
	<language>de-DE</language>
	<wp:wxr_version>1.2</wp:wxr_version>
	<wp:base_site_url>https://haydiweg.de</wp:base_site_url>
	<wp:base_blog_url>https://haydiweg.de</wp:base_blog_url>{authors_xml}{cat_xml}{tag_xml}
{''.join(items)}
</channel>
</rss>
"""


open(os.path.join(WX, "haydiweg-blog-entwuerfe.xml"), "w", encoding="utf-8").write(wxr(items_draft, "alle Artikel als ENTWURF."))
open(os.path.join(WX, "haydiweg-blog-geplant.xml"), "w", encoding="utf-8").write(wxr(items_future, "alle Artikel als GEPLANT – sie erscheinen automatisch zum Termin!"))
open(os.path.join(WX, "haydiweg-blog-dubai-zurueckgestellt.xml"), "w", encoding="utf-8").write(wxr(items_hold, "Dubai-Artikel, zurückgestellt (Entwurf)."))
for old in ("haydiweg-blog-entwuerfe-zurueckgestellt-dubai.xml",):
    if os.path.exists(os.path.join(WX, old)):
        os.remove(os.path.join(WX, old))
if os.path.isdir(os.path.join(WX, "html")):
    import shutil
    shutil.rmtree(os.path.join(WX, "html"))

with open(os.path.join(UP, "UPLOAD_UEBERSICHT.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";"); w.writeheader(); w.writerows(rows)
open(os.path.join(UP, "STECKBRIEFE.md"), "w", encoding="utf-8").write(
    "# Steckbriefe: alle Angaben zum Hochladen je Artikel\n\nSortiert nach Veröffentlichungstermin. "
    "Anleitung: `ANLEITUNG_WORDPRESS_HOCHLADEN_UND_PLANEN.md`.\n" + "".join(steck))

# Nachverlinkung
nv = ["# Nachverlinkung: Links, die später gesetzt werden", "",
      "Ein Link auf einen noch nicht veröffentlichten Beitrag würde bis zu dessen Termin auf eine Fehlerseite (404) führen. "
      "Deshalb sind diese Links in den Upload-Dateien **noch nicht** gesetzt, der Text steht schon da. Sobald der Zielartikel "
      "live ist, im genannten Artikel den Ankertext markieren und den Link einfügen (Strg+K).", "",
      "| Wann (Zielartikel live) | Im Artikel | Ankertext verlinken | Link auf |", "|---|---|---|---|"]
for a, t, txt in sorted(nachverlinkung, key=lambda x: (x[1]["dt"] is None, x[1]["dt"] or datetime.max)):
    when = t["dt"].strftime("%d.%m.%Y") if t["dt"] else "nach Reaktivierung Dubai"
    nv.append(f"| {when} | {a['nr']} {a['fm']['titel_h1'][:60]} | „{txt}“ | {t['url']} |")
open(os.path.join(ROOT, "NACHVERLINKUNG.md"), "w", encoding="utf-8").write("\n".join(nv) + "\n")
print(f"{len(arts)} Artikel | Entwürfe {len(items_draft)} | geplant {len(items_future)} | Dubai {len(items_hold)} | Nachverlinkungen {len(nachverlinkung)}")

# Linkliste aller Artikel (URL-Struktur wie der bestehende Beitrag: /<kategorie>/<slug>/)
ll = ["# Alle Artikel-Links", "",
      "Die URLs folgen der aktuellen Struktur eurer Beiträge: `haydiweg.de/<kategorie>/<beitragsname>/` – "
      "genau wie der bestehende Beitrag https://haydiweg.de/tuerkei/tuerkei-hotel-mit-aquapark/. "
      "Im Design steht darüber automatisch die Brotkrumen-Navigation „Startseite › Reise-Blog › Titel“. "
      "Die Links funktionieren ab dem jeweiligen Veröffentlichungstermin.", "",
      "| Nr | Termin | Titel | Link | Autor |", "|---|---|---|---|---|"]
for r in rows:
    ll.append(f"| {r['Nr']} | {r['Wochentag'][:2]} {r['Termin']} | {r['Titel']} | {r['URL']} | {r['Autor']} |")
open(os.path.join(ROOT, "ARTIKEL_LINKS.md"), "w", encoding="utf-8").write("\n".join(ll) + "\n")
