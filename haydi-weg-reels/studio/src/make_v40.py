# -*- coding: utf-8 -*-
"""Baut das Reel-Studio v39 aus der v37-Quelle (unverändert) + v38-Logik (Datei v38/v38_patch.js, per gezielten Ersetzungen auf v39 gehoben)
+ Hauptplan v3 (reels_hauptplan_v3.json). Alle v37-Funktionen, 51 Specials, Audio-Analyse, Untertitel-Stil bleiben erhalten."""
import json, re, io, os, sys
DRY = sys.argv[1] if len(sys.argv) > 1 else None
SP = "/tmp/claude-0/-home-user-strato-ki-backend/dd35df10-9ce9-5adb-8329-fcd9786b1bcf/scratchpad/"
SRC = SP + "studio_src/reel-studio-v37.html"
OUT_REPO = "/home/user/strato-ki-backend/haydi-weg-reels/studio/reel-studio-v39.html"
OUT_PUB = SP + "v38/reel-studio-v38.html"   # gleicher Dateipfad wie beim ersten Publish → Artefakt wird in place aktualisiert
DATA = DRY or "/home/user/strato-ki-backend/haydi-weg-reels/data/reels_hauptplan_v4.json"
if DRY: OUT_REPO = SP + "v40/_dry.html"; OUT_PUB = SP + "v40/_dry_pub.html"
def must_replace(s, a, b, n=1):
    assert s.count(a) == n, (a[:70], s.count(a)); return s.replace(a, b)

# ---------- 1. Patch v38 → v39 ----------
p = open(SP + "v38/v38_patch.js", encoding="utf-8").read()
p = must_replace(p, "haydi-weg Reel-Studio – Version 38 (09.11.2026)", "haydi-weg Reel-Studio – Version 39 (09.11.2026 · Content-Upgrade v3)")
p = must_replace(p, "Erweiterung des bestehenden Studios (v37) um den Hauptplan 09.11.2026–05.02.2027:", "Erweiterung des bestehenden Studios (v37/v38) um den Hauptplan 09.11.2026–05.02.2027 in der Fassung v3 (Strukturen A–E, Themenwelten, Schlüsselaufnahmen mit Materialstatus, Hooks mit 4 Komponenten):")
p = must_replace(p, "VER: '38',", "VER: '39',")
p = must_replace(p, "SERIES: { FoF: 'Fakt oder Fake?', WDKS: 'Was dir keiner sagt', RW: 'Reisewissen in 30 Sekunden' }",
    "SERIES: { FoF: 'Fakt oder Fake?', WDKS: 'Was dir keiner sagt', RW: 'Reisewissen' }, TW: 'all',\n  KS_CLS: { 'gefunden': 'ok', 'verfügbar, ungeprüft': 'mid', 'nicht gefunden': 'low' }")
# Content-Karte: Themenwelt, Struktur, Upgrade-Entscheidung, Hotel, Endkarte, Schlüsselaufnahmen
p = must_replace(p, "['Status vs. Masterplan 06.11.', H.status_vs_plan + ' · Plan-Konsens ' + H.plan_konsens], ['Prüfbare Behauptung', H.claim]",
    "H.themenwelt ? ['Themenwelt', H.themenwelt + ' – ' + (H.themenwelt_text || '')] : null, H.structure ? ['Storytelling-Struktur', H.structure + ' · ' + (H.structure_name || '')] : null, H.decision_v3 ? ['Upgrade v3 (09.11.)', H.decision_v3 + (H.title_v2 && H.title_v2 !== H.title ? ' · vorher: „' + H.title_v2 + '“' : '') + (H.decision_reason ? ' – ' + H.decision_reason : '')] : (H.status_vs_plan ? ['Status vs. Masterplan 06.11.', H.status_vs_plan + ' · Plan-Konsens ' + H.plan_konsens] : null), H.hotel ? ['Hotel / Resort (konkret)', H.hotel] : null, H.target_sec ? ['Länge', 'Ziel ca. ' + H.target_sec + ' s · vorläufig ' + H.cut.total_sec.toFixed(1) + ' s (Timecodes erst nach Audio)'] : null, H.end_card ? ['Endkarte', H.end_card + (H.teaser_spoken ? ' · Teaser gesprochen + Grafik' : ' · Teaser nur als Grafik')] : null, ['Prüfbare Behauptung', H.claim]")
p = must_replace(p, "    el('div', { class: 'psec' }, el('h3', {}, 'Storytelling-Bogen'), pkgRows(arcRows)),\n    el('div', { class: 'psec' }, el('h3', {}, 'Produktionsstatus'), pkgRows(prod)),",
    "    el('div', { class: 'psec' }, el('h3', {}, 'Storytelling-Bogen' + (H.structure_name ? ' – ' + H.structure_name : '')), pkgRows(arcRows)),\n    (H.key_shots || []).length ? el('div', { class: 'psec' }, el('h3', {}, 'Schlüsselaufnahmen – Material zuerst'), hwKeyShotTable(v)) : null,\n    el('div', { class: 'psec' }, el('h3', {}, 'Produktionsstatus'), pkgRows(prod)),")
p = must_replace(p, "function hwContentCard(v, s, n) {",
    "function hwKsBadge(st0) { return el('span', { class: 'hwks ' + (HW.KS_CLS[st0] || 'mid') }, st0); }\n"
    "function hwKeyShotTable(v) { const H = v.hw, x = hwS(v); return el('div', { class: 'ptw' }, el('table', { class: 'pt pts' }, el('thead', {}, el('tr', {}, ['Rolle', 'Motiv', 'Quelle / Referenz', 'Status laut Recherche 09.11.', 'Hinweis / Alternative', 'Status im Studio'].map(h => el('th', {}, h)))),\n"
    "  el('tbody', {}, (H.key_shots || []).map((k, i) => el('tr', { class: k.status === 'nicht gefunden' ? 'miss' : '' }, el('td', {}, el('b', {}, k.role)), el('td', {}, k.motif), el('td', {}, k.source + (k.ref ? ' · ' + k.ref : '')), el('td', {}, hwKsBadge(k.status)), el('td', {}, k.note || '–'),\n"
    "  el('td', {}, el('select', { 'aria-label': 'Status Schlüsselaufnahme ' + k.role, onchange: e => { x.ksChk = Object.assign({}, x.ksChk || {}, { [i]: e.target.value }); touch(v.id); renderPanels(); } }, HW.STOCK_ST.map(o => el('option', { value: o, selected: ((x.ksChk || {})[i] || 'offen') === o ? true : null }, o))))))))); }\n"
    "function hwContentCard(v, s, n) {")
p = must_replace(p, "['Ort', H.place], ['Cluster', H.cluster],", "['Ort', H.place], H.cluster ? ['Cluster', H.cluster] : null,")
p = must_replace(p, "el('span', { class: 'meta' }, 'Plan-Konsens ' + H.plan_konsens)),", "H.plan_konsens ? el('span', { class: 'meta' }, 'Plan-Konsens ' + H.plan_konsens) : null),")
# Hook-Karte: 4 Komponenten
p = must_replace(p, "['★', 'Typ', 'Hook (gesprochen, Satz 1)', 'Erstes Bild ohne Ton', ...HW.CRIT.map(c => HW.CRIT_L[c]), 'Ø', 'Bewertung']",
    "['★', 'Typ', 'Gesprochener Einstieg', 'Erstes Bild (ohne Ton)', 'Text-Overlay', 'Offene Frage', ...HW.CRIT.map(c => HW.CRIT_L[c]), 'Ø', 'Bewertung', '']")
p = must_replace(p, "el('td', {}, h.typ), el('td', { class: 'pvo' }, h.text), el('td', {}, h.first_frame), ...HW.CRIT.map(c => el('td', { class: 'tc' }, String(h.scores[c]))), el('td', { class: 'tc' }, el('b', {}, h.total.toFixed(2))), el('td', {}, h.reason)))));",
    "el('td', {}, h.typ), el('td', { class: 'pvo' }, h.spoken || h.text), el('td', {}, h.first_frame), el('td', { class: 'pvo' }, (h.overlay || '–').replace(/\\*/g, '')), el('td', {}, h.question || '–'), ...HW.CRIT.map(c => el('td', { class: 'tc' }, String(h.scores[c]))), el('td', { class: 'tc' }, el('b', {}, h.total.toFixed(2))), el('td', {}, h.reason),\n"
    "      el('td', {}, h.overlay ? el('button', { class: 'btn sm', type: 'button', title: 'Text-Overlay dieses Hooks als Hook-Overlay im Video verwenden', onclick: () => { s.hook = h.overlay; touch(v.id); renderPanels(); renderHead(); if (!E.playing) seekSoon(.6); toast('Hook-Overlay übernommen: ' + h.overlay.replace(/\\*/g, '')); } }, 'Overlay') : null)))));")
p = must_replace(p, "'Sieben Kriterien je 1–10 (Scroll-Stop, Verständlichkeit, Originalität, Emotion, visuelle Umsetzbarkeit, Glaubwürdigkeit, DACH-Fit) – Einschätzungen der Redaktion, keine Messwerte. Der Sieger ist der erste gesprochene Satz; das Hook-Overlay im Bild ist die kurze Cover-Headline (Manrope ExtraBold, ein *Wort* in Gelb). Mit dem Radio-Button wählst du einen anderen Sieger.'",
    "'Jeder Hook ist die Kombination aus erstem sichtbaren Bild (muss ohne Ton funktionieren), gesprochenem Einstieg, Text-Overlay und der offenen Frage im Kopf des Zuschauers. Fünf Typen: Visueller Schock · Neugierlücke · Überraschende Behauptung · Emotionaler Konflikt · Erwartung gegen Realität. Sieben Kriterien je 1–10 – Einschätzungen der Redaktion, keine Messwerte. Der Sieger ist der erste gesprochene Satz; „Overlay“ übernimmt das Text-Overlay des Hooks ins Video (ein *Wort* in Gelb), die Cover-Buttons setzen Cover-Headline oder Hook-Overlay aus dem Cover-Konzept. Mit dem Radio-Button wählst du einen anderen Sieger.'")
p = must_replace(p, "return card(n, 'Hook-Studio – 5 Hooks, Bewertung, Sieger & 3 Cover',", "return card(n, 'Hook-Studio – 5 Hooks (Bild · Satz · Overlay · Frage), Bewertung, Sieger & 3 Cover',")
# Hooks-CSV mit 4 Komponenten
p = must_replace(p, "function hwHooksCSV(list) { const L = [['Reel', 'Datum', 'Titel', 'Hook-Typ', 'Hook', 'Erstes Bild ohne Ton', ...HW.CRIT.map(c => HW.CRIT_L[c]),",
    "function hwHooksCSV(list) { const L = [['Reel', 'Datum', 'Titel', 'Hook-Typ', 'Gesprochener Einstieg', 'Erstes Bild ohne Ton', 'Text-Overlay', 'Offene Frage', ...HW.CRIT.map(c => HW.CRIT_L[c]),")
# Qualitäts-Karte: Materialhinweis + Schlüsselaufnahmen
p = must_replace(p, "'Pexels-/Pixabay-IDs stammen aus der Plan-Recherche vom 06.11.2026 und wurden am 09.11.2026 nicht erneut geöffnet – vor dem Download jede Detailseite prüfen (Ort, Urheber, Lizenz, Personen). Envato-Treffer sind Suchbegriffe, keine geprüften Clips.'",
    "'Prüfstand 09.11.2026: Für die Schlüsselaufnahmen wurden die Suchergebnisseiten von Pexels bzw. Envato Elements geöffnet und passende Treffer (ID/Titel) protokolliert – „gefunden“ heißt gelistet, nicht lizenziert. Detailseiten (Ort, Urheber, Lizenz, Personen) vor jedem Download prüfen; Envato-Lizenz je Download registrieren. Keine Käufe ohne Freigabe (Budget max. 50 €/Monat).'")
p = must_replace(p, "    el('div', { class: 'psec' }, el('h3', {}, 'Vor Posting prüfen (Vortag) ' + (g.preOk ? '✓' : '')),",
    "    (H.key_shots || []).length ? el('div', { class: 'psec' }, el('h3', {}, 'Schlüsselaufnahmen (3) – Status'), hwKeyShotTable(v)) : null,\n    el('div', { class: 'psec' }, el('h3', {}, 'Vor Posting prüfen (Vortag) ' + (g.preOk ? '✓' : '')),")
# Kopfzeile: Themenwelt + Struktur
p = must_replace(p, "el('span', { class: 'type ' + (ap === 'Freigegeben' ? 'wow' : 'info') }, ap), el('span', { class: 'meta' }, 'QS ' + hwTotal(hwScores(v)).toFixed(2))),",
    "el('span', { class: 'type ' + (ap === 'Freigegeben' ? 'wow' : 'info') }, ap), el('span', { class: 'meta' }, 'QS ' + hwTotal(hwScores(v)).toFixed(2)), H.themenwelt ? el('span', { class: 'type info' }, H.themenwelt) : null, H.structure ? el('span', { class: 'meta', title: H.structure_name }, 'Struktur ' + H.structure) : null),")
# Liste: Themenwelt-Filter + Strukturkürzel
p = must_replace(p, "[['all', 'Alle Serien'], ['FoF', 'Mo · Fakt oder Fake?'], ['WDKS', 'Mi · Was dir keiner sagt'], ['RW', 'Fr · Reisewissen']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'aria-pressed': String(HW.SERIE === k), onclick: () => { HW.SERIE = k; renderList(); } }, l))),",
    "[['all', 'Alle Serien'], ['FoF', 'Mo · Fakt oder Fake?'], ['WDKS', 'Mi · Was dir keiner sagt'], ['RW', 'Fr · Reisewissen']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'aria-pressed': String(HW.SERIE === k), onclick: () => { HW.SERIE = k; renderList(); } }, l))),\n      el('div', { class: 'filters', role: 'group', 'aria-label': 'Themenwelt' }, [['all', 'Alle Themenwelten'], ['Natur-Wunder', 'Natur-Wunder'], ['Hotel-Legenden', 'Hotel-Legenden'], ['Regeln & Realität', 'Regeln & Realität'], ['Alte Welten', 'Alte Welten']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'data-tw': k, 'aria-pressed': String(HW.TW === k), onclick: () => { HW.TW = k; renderList(); } }, l))),")
p = must_replace(p, "if (isMain(v)) { if (HW.SERIE !== 'all' && v.hw.series !== HW.SERIE) return;", "if (isMain(v)) { if (HW.SERIE !== 'all' && v.hw.series !== HW.SERIE) return; if (HW.TW !== 'all' && v.hw.themenwelt !== HW.TW) return;")
p = must_replace(p, "el('small', {}, isMain(v) ? (v.hw.series) : v.time)),", "el('small', {}, isMain(v) ? (v.hw.series + (v.hw.structure ? ' · ' + v.hw.structure : '')) : v.time)),")
# Import-Hinweis
p = must_replace(p, "'Import: Die Datei reels_hauptplan_v2.json (oder eine überarbeitete Fassung im selben Format)", "'Import: Die Datei reels_hauptplan_v3.json (oder eine überarbeitete Fassung im selben Format; v2-Dateien werden weiterhin gelesen)")
p = must_replace(p, "lsGet('hw-rs-v38seen')", "lsGet('hw-rs-v39seen')").replace("lsSet('hw-rs-v38seen', '1')", "lsSet('hw-rs-v39seen', '1')")
p = must_replace(p, "schema: 'reelstudio_state_v38'", "schema: 'reelstudio_state_v39'")
p = must_replace(p, "W: { hook: 25, visual: 20, story: 20, share: 15, dach: 10, facts: 10 },", "W: Object.assign({ hook: 25, visual: 20, story: 20, share: 15, dach: 10, facts: 10 }, (HW_MAIN_RAW.reels[0] && HW_MAIN_RAW.reels[0].scorecard && HW_MAIN_RAW.reels[0].scorecard.weights) || {}),")
p = must_replace(p, "'Gewichtung laut Auftrag: Hook/erstes Bild 25 % · Visuell 20 % · Storytelling 20 % · Shareability 15 % · DACH 10 % · Fakten/Umsetzbarkeit 10 %. Noten sind Einschätzungen", "'Gewichtung laut Auftrag: ' + Object.keys(HW.W).map(k => HW.QS_L[k] + ' ' + HW.W[k] + ' %').join(' · ') + '. Noten sind Einschätzungen")
p = must_replace(p, "lsGet('hw-rs-v39seen')", "lsGet('hw-rs-v40seen')").replace("lsSet('hw-rs-v39seen', '1')", "lsSet('hw-rs-v40seen', '1')")
open(SP + "v40/v40_patch.js", "w", encoding="utf-8").write(p)

# ---------- 2. hw_todata v39: Hook-Overlay des Siegers als Video-Hook ----------
td = open(SP + "v38/hw_todata.js", encoding="utf-8").read()
td = must_replace(td, "/* ---- v38: Hauptplan 09.11.2026–05.02.2027 (39 Reels) – Umwandlung ins Studio-Datenformat ---- */", "/* ---- v39: Hauptplan 09.11.2026–05.02.2027 (39 Reels, Fassung v3) – Umwandlung ins Studio-Datenformat ---- */")
td = must_replace(td, "const cov = (r.covers || [])[0]; let hook = cov ? cov.headline : r.title; const yel = cov && cov.yellow;\n  if (yel && hook.includes(yel) && !/\\*/.test(hook)) hook = hook.replace(yel, '*' + yel + '*');",
    "const cov = (r.covers || [])[0]; const win = (r.hooks || []).find(h => h.winner); let hook = win && win.overlay ? win.overlay : (cov ? cov.headline : r.title); const yel = cov && cov.yellow;\n  if (!(win && win.overlay) && yel && hook.includes(yel) && !/\\*/.test(hook)) hook = hook.replace(yel, '*' + yel + '*');")
td = must_replace(td, "fmt: r.series + ' #' + r.episode,", "fmt: r.series + ' #' + r.episode + (r.structure ? ' · ' + r.structure : ''),")
open(SP + "v40/hw_todata.js", "w", encoding="utf-8").write(td)

# ---------- 3. HTML zusammenbauen ----------
html = open(SRC, encoding="utf-8").read(); orig_len = len(html)
html = must_replace(html, "Plan 04.11.2026–30.01.2027 · 17 Videos pro Monat · Zeiten im CapCut-Format (30 fps)",
                    "Hauptplan 09.11.2026–05.02.2027 (Fassung v4 · Final-Audit) · 39 Reels Mo/Mi/Fr · 51 Specials · Zeiten im CapCut-Format (30 fps)")
html = must_replace(html, "Version 37 · Hooks 05.11.", "Version 39 · Plan v4 09.11.")
html = must_replace(html, "const baseName = v => v.custom ? 'haydi-weg_' + slug(v.title) : 'haydi-weg_2026-10-' + String(v.day).padStart(2, '0') + '_' + slug(v.title.replace('WOW-Edit: ', 'wow-'));",
                    "const baseName = v => v.custom ? 'haydi-weg_' + slug(v.title) : 'haydi-weg_' + (v.year || 2026) + '-' + String(v.month || 10).padStart(2, '0') + '-' + String(v.day).padStart(2, '0') + '_' + (v.plan === 'main' ? v.id + '_' : '') + slug(v.title.replace('WOW-Edit: ', 'wow-'));")
j = json.load(open(DATA, encoding="utf-8"))
assert j["meta"]["schema"] in ("reels_hauptplan_v3", "reels_hauptplan_v4") and (DRY or len(j["reels"]) == 39)
raw = json.dumps(j, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
lines = html.split("\n"); idx = [i for i, l in enumerate(lines) if l.startswith("const DATA = [")]; assert len(idx) == 1
lines.insert(idx[0] + 1, "const HW_MAIN_RAW = " + raw + ";\n" + td); html = "\n".join(lines)
css = """
/* v38/v39 */
.plan .pt.hwt{min-width:1500px;font-size:12.5px}
.plan .pt tr.win td{background:var(--accentSoft)}
.plan .pt tr.miss td{background:var(--dangerSoft)}
.hwcov{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.hwc{border:1px solid var(--line);border-radius:12px;padding:10px;display:grid;gap:6px;background:var(--surface)}
.hwc.on{border-color:var(--accent);box-shadow:0 0 0 2px var(--accentSoft)}
.hwc .hwh{font-family:'Manrope',sans-serif;font-weight:800;font-size:17px;line-height:1.2}
.hwc small{color:var(--muted)}
.hwtot{font-weight:800;font-size:20px;font-variant-numeric:tabular-nums}
.hwtot.ok{color:var(--ok)}.hwtot.mid{color:var(--accentInk)}.hwtot.low{color:var(--danger)}
.hwul,.hwol{margin:6px 0 0;padding-left:20px;font-size:13px;line-height:1.5}
.hwul li,.hwol li{margin:2px 0}
.hwsub{margin-top:10px}
.hwsub input[type=number]{width:84px}
.hwks{display:inline-block;padding:2px 8px;border-radius:999px;font-size:12px;font-weight:700;white-space:nowrap;border:1px solid var(--line)}
.hwks.ok{background:var(--okSoft,#E3F5E8);color:var(--ok)}.hwks.mid{background:var(--accentSoft);color:var(--accentInk)}.hwks.low{background:var(--dangerSoft);color:var(--danger)}
"""
k = html.rfind("</style>"); html = html[:k] + css + html[k:]
k = html.rfind("</body>"); html = html[:k] + "<script>\n" + p + "\n</script>\n" + html[k:]
io.open(OUT_REPO, "w", encoding="utf-8").write(html)
print("written", OUT_REPO, len(html), "bytes (v37:", orig_len, ")")
# Publish-Fassung (ohne Dokument-Skelett – wird vom Artefakt-Server ergänzt), gleicher Pfad wie v38-Publish
m = re.search(r"<title>.*", html, flags=re.S); body = m.group(0); body = body[:body.rfind("</body>")] if "</body>" in body else body
io.open(OUT_PUB, "w", encoding="utf-8").write(body)
print("publish file", OUT_PUB, len(body))
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
for i, sc in enumerate(scripts): open(SP + "v40/_check%d.js" % i, "w", encoding="utf-8").write(sc)
print("scripts:", len(scripts))
