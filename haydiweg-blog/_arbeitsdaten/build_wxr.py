#!/usr/bin/env python3
"""Erzeugt eine WordPress-Importdatei (WXR 1.2) mit allen Artikeln als ENTWURF.

- post_status = draft (nie publish/future). Veröffentlichung erst nach Freigabe in WordPress.
- Geplantes Datum wird als post_date gesetzt, damit es beim späteren Planen übernommen wird.
- Rank-Math-Metadaten: rank_math_title, rank_math_description, rank_math_focus_keyword.
- Bild-Platzhalter und [PRÜFEN]-Marker bleiben im Entwurf sichtbar (gelber Hinweis), damit nichts
  ungeprüft live geht. Vor Veröffentlichung entfernen.
- Links auf noch nicht veröffentlichte Artikel werden als <a ... data-geplant="NN"> markiert.

Aufruf: python3 build_wxr.py  ->  ../WORDPRESS_IMPORT/haydiweg-blog-entwuerfe.xml + ../WORDPRESS_IMPORT/html/NN-slug.html
"""
import glob, html, os, re
from datetime import datetime
import markdown, yaml

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
OUT = os.path.join(ROOT, "WORDPRESS_IMPORT")
os.makedirs(os.path.join(OUT, "html"), exist_ok=True)

CATS = {"Türkei": "tuerkei", "Ägypten": "aegypten", "Spanien": "spanien", "Griechenland": "griechenland",
        "Dubai": "dubai", "Fernreisen": "fernreisen", "Reiseplanung": "reiseplanung"}


def slugify(s):
    s = s.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def cdata(s):
    return "<![CDATA[" + str(s).replace("]]>", "]]]]><![CDATA[>") + "]]>"


def to_html(body):
    body = re.sub(r"^# .+\n", "", body, count=1, flags=re.M)  # H1 = Beitragstitel
    def bild(m):
        parts = [p.strip() for p in m.group(1).split("|")]
        return ('\n<p class="hw-redaktion" style="background:#fff7d6;border-left:4px solid #f2c200;padding:8px 12px">'
                '<strong>BILD (Redaktion):</strong> ' + html.escape(" · ".join(parts)) + '</p>\n')
    body = re.sub(r"<!--\s*BILD:(.*?)-->", bild, body, flags=re.S)
    body = re.sub(r"\]\((https://haydiweg\.de/[^)]+)\)<!--\s*geplant #(\d+)\s*-->", r"](\1){: data-geplant=\"\2\"}", body)
    h = markdown.markdown(body, extensions=["tables", "attr_list", "toc", "sane_lists"], extension_configs={"toc": {"slugify": lambda v, sep: slugify(v)}})
    h = re.sub(r"\[PRÜFEN:?([^\]]*)\]", lambda m: '<mark class="hw-pruefen">[PRÜFEN:' + m.group(1) + ']</mark>', h)
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    h = h.replace('<a href="https://wa.me', '<a rel="nofollow noopener" target="_blank" href="https://wa.me')
    h = re.sub(r'<a href="(https?://(?!haydiweg\.de)[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    return h


items, terms_cat, terms_tag = [], {}, {}
items_hold = []
HOLD = {5, 10, 27}  # Dubai: AA rät von Reisen in die VAE ab (Stand 05.11.2026)
# Kontrolliertes Schlagwort-Vokabular: bestehende Tags + Tags, die in mind. 2 Artikeln vorkommen
from collections import Counter
EXISTING_TAGS = {"Aquapark", "Belek", "Familienurlaub", "Kemer", "Lara", "Side"}
_tc = Counter()
for _p in glob.glob(os.path.join(ROOT, "BLOG_ARTIKEL", "*.md")):
    _m = re.match(r"^---\n(.*?)\n---\n", open(_p, encoding="utf-8").read(), re.S)
    if _m:
        for _t in set(yaml.safe_load(_m.group(1)).get("schlagwoerter") or []):
            _tc[_t] += 1
ALLOWED_TAGS = {t for t, n in _tc.items() if n >= 2} | EXISTING_TAGS
for path in sorted(glob.glob(os.path.join(ROOT, "BLOG_ARTIKEL", "*.md"))):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        continue
    fm, body = yaml.safe_load(m.group(1)), m.group(2)
    nr = int(fm["nr"])
    content = to_html(body)
    open(os.path.join(OUT, "html", os.path.basename(path).replace(".md", ".html")), "w", encoding="utf-8").write(
        f"<!doctype html><meta charset=utf-8><title>{html.escape(fm['titel_h1'])}</title><h1>{html.escape(fm['titel_h1'])}</h1>\n" + content)
    cat = fm["wp_kategorie"]
    terms_cat[CATS.get(cat, slugify(cat))] = cat
    tags = [t for t in (fm.get("schlagwoerter") or []) if t in ALLOWED_TAGS]
    for t in tags:
        terms_tag[slugify(t)] = t
    dt = datetime.fromisoformat(str(fm["veroeffentlichung"]))
    kw = [str(fm["fokus_keyword"])] + [str(x) for x in (fm.get("nebenkeywords") or [])][:4]
    bb = fm.get("beitragsbild") or {}
    meta = {
        "rank_math_title": fm["seo_title"],
        "rank_math_description": fm["meta_description"],
        "rank_math_focus_keyword": ",".join(kw),
        "_hw_redaktionsplan_nr": f"{nr:02d}",
        "_hw_geplante_veroeffentlichung": dt.strftime("%Y-%m-%d %H:%M"),
        "_hw_beitragsbild_vorschlag": f"{bb.get('datei','')} | ALT: {bb.get('alt','')} | {bb.get('quelle','')}",
        "_hw_quellen_geprueft_am": str(fm.get("quellen_geprueft_am", "")),
    }
    pm = "".join(f"\n\t\t<wp:postmeta><wp:meta_key>{k}</wp:meta_key><wp:meta_value>{cdata(v)}</wp:meta_value></wp:postmeta>" for k, v in meta.items())
    cats = f'\n\t\t<category domain="category" nicename="{CATS.get(cat, slugify(cat))}">{cdata(cat)}</category>'
    cats += "".join(f'\n\t\t<category domain="post_tag" nicename="{slugify(t)}">{cdata(t)}</category>' for t in tags)
    excerpt = fm["meta_description"]
    (items_hold if nr in HOLD else items).append(f"""
	<item>
		<title>{cdata(fm['titel_h1'])}</title>
		<dc:creator>{cdata('admin')}</dc:creator>
		<description></description>
		<content:encoded>{cdata(content)}</content:encoded>
		<excerpt:encoded>{cdata(excerpt)}</excerpt:encoded>
		<wp:post_date>{cdata(dt.strftime('%Y-%m-%d %H:%M:%S'))}</wp:post_date>
		<wp:post_date_gmt>{cdata('0000-00-00 00:00:00')}</wp:post_date_gmt>
		<wp:comment_status>{cdata('closed')}</wp:comment_status>
		<wp:ping_status>{cdata('closed')}</wp:ping_status>
		<wp:post_name>{cdata(fm['slug'])}</wp:post_name>
		<wp:status>{cdata('draft')}</wp:status>
		<wp:post_parent>0</wp:post_parent>
		<wp:menu_order>0</wp:menu_order>
		<wp:post_type>{cdata('post')}</wp:post_type>
		<wp:post_password>{cdata('')}</wp:post_password>
		<wp:is_sticky>0</wp:is_sticky>{cats}{pm}
	</item>""")

cat_xml = "".join(f"\n\t<wp:category><wp:category_nicename>{cdata(n)}</wp:category_nicename><wp:category_parent>{cdata('')}</wp:category_parent><wp:cat_name>{cdata(c)}</wp:cat_name></wp:category>" for n, c in sorted(terms_cat.items()))
tag_xml = "".join(f"\n\t<wp:tag><wp:tag_slug>{cdata(n)}</wp:tag_slug><wp:tag_name>{cdata(t)}</wp:tag_name></wp:tag>" for n, t in sorted(terms_tag.items()))
def wxr(its, note):
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<!-- haydi-weg Blog-Entwürfe – {note} Alle Beiträge mit Status ENTWURF. Erzeugt {datetime.now():%Y-%m-%d %H:%M}. -->
<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">
<channel>
	<title>haydi-weg</title>
	<link>https://haydiweg.de</link>
	<description>Blog-Entwürfe Redaktionsplan 09.11.2026–31.01.2027</description>
	<language>de-DE</language>
	<wp:wxr_version>1.2</wp:wxr_version>
	<wp:base_site_url>https://haydiweg.de</wp:base_site_url>
	<wp:base_blog_url>https://haydiweg.de</wp:base_blog_url>
	<wp:author><wp:author_login>{cdata('admin')}</wp:author_login><wp:author_display_name>{cdata('admin')}</wp:author_display_name></wp:author>{cat_xml}{tag_xml}
{''.join(its)}
</channel>
</rss>
"""
open(os.path.join(OUT, "haydiweg-blog-entwuerfe.xml"), "w", encoding="utf-8").write(wxr(items, "Redaktionsplan 09.11.2026-31.01.2027."))
open(os.path.join(OUT, "haydiweg-blog-entwuerfe-zurueckgestellt-dubai.xml"), "w", encoding="utf-8").write(wxr(items_hold, "ZURUECKGESTELLT (Dubai, AA-Hinweis) - erst nach Aufhebung importieren."))
print(f"{len(items)} Entwürfe (+{len(items_hold)} zurückgestellt), {len(terms_cat)} Kategorien, {len(terms_tag)} Schlagwörter -> {OUT}")
