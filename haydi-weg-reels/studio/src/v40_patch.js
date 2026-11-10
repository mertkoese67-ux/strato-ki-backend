/* ===================================================================================
   haydi-weg Reel-Studio – Version 39 (09.11.2026 · Content-Upgrade v3)
   Erweiterung des bestehenden Studios (v37/v38) um den Hauptplan 09.11.2026–05.02.2027 in der Fassung v3 (Strukturen A–E, Themenwelten, Schlüsselaufnahmen mit Materialstatus, Hooks mit 4 Komponenten):
   Content-Studio · Hook-Studio · CapCut-Studio · Audio-Analyse · Untertitel-Zeiten · Qualitäts-Studio · Import/Export
   Alle v37-Funktionen, Daten (51 Specials) und der Untertitel-Stil bleiben erhalten.
   =================================================================================== */
"use strict";
const HW = {
  VER: '39', STAND: '09.11.2026', PLAN: lsGet('hw-plan') || 'main', SERIE: 'all', STATUS: 'all', MONTH: 'all',
  W: Object.assign({ hook: 25, visual: 20, story: 20, share: 15, dach: 10, facts: 10 }, (HW_MAIN_RAW.reels[0] && HW_MAIN_RAW.reels[0].scorecard && HW_MAIN_RAW.reels[0].scorecard.weights) || {}),
  QS_L: { hook: 'Hook / erstes Bild', visual: 'Visuelle Stärke', story: 'Storytelling', share: 'Shareability', dach: 'DACH-Relevanz', facts: 'Fakten / Umsetzbarkeit' },
  CRIT: ['scrollstop', 'verstaendlich', 'originalitaet', 'emotion', 'visuell', 'glaubwuerdig', 'dach'],
  CRIT_L: { scrollstop: 'Scroll-Stop', verstaendlich: 'Verständlich', originalitaet: 'Originell', emotion: 'Emotion', visuell: 'Visuell', glaubwuerdig: 'Glaubwürdig', dach: 'DACH' },
  APPR: ['Entwurf', 'Vorprüfung bestanden', 'Material offen', 'Freigegeben', 'Zurückgestellt'],
  STOCK_ST: ['offen', 'geprüft & lizenziert', 'ersetzt (Alternative)', 'nicht nötig'],
  COLS: ['Szene', 'TC Start', 'TC Ende', 'Dauer s', 'Sprechtext (exakt)', 'Motiv (detailliert)', 'Ort/Hotel (exakt)', 'Kameraperspektive', 'Bildausschnitt', 'Bewegung', 'Licht/Atmosphäre', 'Stock-Suchbegriffe', 'Schnittart', 'Übergang', 'Text-Overlay', 'Musikstimmung', 'SFX', 'Untertitel-Hinweis'],
  SERIES: { FoF: 'Fakt oder Fake?', WDKS: 'Was dir keiner sagt', RW: 'Reisewissen' }, TW: 'all',
  KS_CLS: { 'gefunden': 'ok', 'verfügbar, ungeprüft': 'mid', 'nicht gefunden': 'low' }
};
const isMain = v => !!(v && v.plan === 'main' && v.hw);
const hwS = v => { const s = st(v.id); if (!s.hw || typeof s.hw !== 'object') s.hw = {}; return s.hw; };
const hwNum = x => Math.round((+x || 0) * 100) / 100;
const csvEsc = x => '"' + String(x == null ? '' : x).replace(/"/g, '""').replace(/\r?\n/g, ' ') + '"';
const hwSlug = t => slug(String(t || ''));
function hwDl(name, text, mime) { return saveFile(name, new Blob([text], { type: mime || 'text/plain;charset=utf-8' })); }

/* ---------------- Bewertung ---------------- */
function hwScores(v) { const H = v.hw; const o = Object.assign({}, H.scorecard.scores, hwS(v).score || {}); return o; }
function hwTotal(sc) { let t = 0; for (const k in HW.W) t += (+sc[k] || 0) * HW.W[k]; return Math.round(t) / 100; }
function hwApproval(v) { return hwS(v).approval || (v.hw.approval && /Vorprüfung/.test(v.hw.approval.status) ? 'Vorprüfung bestanden' : 'Entwurf'); }
function hwGate(v) {
  const H = v.hw, x = hwS(v); const pre = H.approval.pre_post_checks || []; const stock = H.stock || []; const facts = H.facts.to_check || [];
  const preOk = pre.every((_, i) => x.prepost && x.prepost[i]);
  const stockOk = stock.every((st0, i) => { const k = (x.stockChk || {})[i]; return st0.source === 'Eigene Grafik' || k === 'geprüft & lizenziert' || k === 'ersetzt (Alternative)' || k === 'nicht nötig'; });
  const factsOk = facts.every((_, i) => x.factChk && x.factChk[i]);
  return { preOk, stockOk, factsOk, hookOk: !!x.hookApproved, ok: preOk && stockOk && factsOk && !!x.hookApproved };
}

/* ---------------- Szenen-Zeiten: vorläufig (Wortzahl) oder aus der echten Audiodatei ---------------- */
function hwLinesPerScene(v) { return v.hw.cut.scenes.filter(x => String(x.vo || '').trim()).map(sc => autoSubs(sc.sub || sc.vo).split('\n').map(x => x.trim()).filter(Boolean).length); }
function hwSceneTimes(v) {
  const H = v.hw, s = st(v.id); const scs = H.cut.scenes; const vo = voInfo(v);
  const pre = scs.map(x => ({ start: +x.start_s, end: +x.end_s }));
  if (!vo.real) return { mode: 'vorläufig', real: false, label: 'VORLÄUFIG – aus der Wortzahl geschätzt (2,45 Wörter/s). Lade die ElevenLabs-Datei hoch, dann rechnet das Studio die Zeiten aus der echten Sprechdauer.', rows: pre };
  const items = subTiming(v); const per = hwLinesPerScene(v); const sum = per.reduce((a, b) => a + b, 0);
  const voiced = scs.map((x, i) => i).filter(i => String(scs[i].vo || '').trim());
  if (s.subs == null && sum === items.length && items.length) {
    let li = 0; const starts = voiced.map((si, k) => { const t = items[li].start; li += per[k]; return t; });
    const end = items[items.length - 1].end; const rows = []; let vi = 0, prevEnd = 0;
    scs.forEach((x, i) => { if (!String(x.vo || '').trim()) { rows.push({ start: prevEnd, end: prevEnd + (+x.dur_s || 1) }); prevEnd = rows[rows.length - 1].end; return; }
      const st0 = vi === 0 ? 0 : starts[vi]; const en = vi < starts.length - 1 ? starts[vi + 1] : end + (+x.hold || 0); rows.push({ start: st0, end: Math.max(st0 + .4, en) }); prevEnd = rows[rows.length - 1].end; vi++; });
    return { mode: 'audio', real: true, label: 'AUS AUDIO – Szenengrenzen = Start der ersten Untertitelzeile jeder Szene, ausgerichtet an Pausen und Silben deiner Stimme (Sprechzeit ' + fmtS(vo.dur) + '). Framegenau nach Prüfung in der Vorschau.', rows };
  }
  const W = scs.reduce((a, x) => a + (+x.words || 0), 0) || 1; const base = s.voStart || 0; let t = 0; const rows = [];
  scs.forEach((x, i) => { const d = (+x.words || 0) / W * vo.dur + (i === scs.length - 1 ? (+x.hold || 1) : 0) + (i === 0 ? base : 0); const en = t + d; rows.push({ start: t, end: en }); t = en; });
  return { mode: 'audio-anteilig', real: true, label: 'AUS AUDIO – anteilig nach Wörtern über die reale Sprechzeit (' + fmtS(vo.dur) + '). Die Untertitel wurden von Hand geändert, deshalb keine zeilengenaue Zuordnung; „Aus Sprechtext neu erzeugen“ stellt sie wieder her.', rows };
}
function hwCutRows(v) { const T = hwSceneTimes(v); return v.hw.cut.scenes.map((sc, i) => { const r = T.rows[i] || { start: sc.start_s, end: sc.end_s }; return [i + 1, tcCap(r.start), tcCap(r.end), (r.end - r.start).toFixed(1), sc.vo || '–', sc.motif, sc.place, sc.cam, sc.frame, sc.move, sc.light, (sc.stock || []).join(', '), sc.cut, sc.trans, sc.overlay, sc.music, sc.sfx, sc.subhint]; }); }
function hwCutCSV(v) { return '﻿' + [HW.COLS.map(csvEsc).join(';'), ...hwCutRows(v).map(r => r.map(csvEsc).join(';'))].join('\n'); }
function hwCutMD(v) {
  const H = v.hw, T = hwSceneTimes(v); const s = st(v.id);
  const L = ['# CapCut-Schnittplan ' + v.id + ' · ' + v.title, '', v.wd + ' ' + dateLabel(v) + (v.year || '') + ' · ' + H.series_name + ' #' + H.episode + ' · ' + H.place, '', '**Format:** ' + H.cut.format + ' · **Timecode:** HH:MM:SS:FF · **Zeiten:** ' + T.label, '', '**Hook-Overlay:** ' + String(s.hook || '').replace(/\*/g, '') + ' · **Sieger-Hook (gesprochen):** ' + hwWinner(v).text, '', '**Musik:** ' + H.cut.music + ' · **Logo:** ' + H.cut.logo + ' · **Serienkarte:** ' + H.cut.series_card, '',
    '| ' + HW.COLS.join(' | ') + ' |', '|' + HW.COLS.map(() => '---').join('|') + '|'];
  hwCutRows(v).forEach(r => L.push('| ' + r.map(x => String(x).replace(/\|/g, '/').replace(/\n/g, ' ')).join(' | ') + ' |'));
  L.push('', '## Stock & Quellen', ''); (H.stock || []).forEach((st0, i) => L.push('- **' + st0.shot + '** – ' + st0.source + ' ' + st0.ref + ' · Suche: ' + st0.search_terms + ' · Lizenz: ' + st0.license_status + ' · Prüfung: ' + st0.checked + (st0.missing ? ' · **FEHLT** – Alternative: ' + st0.alternative : '') + ' · Status im Studio: ' + ((hwS(v).stockChk || {})[i] || 'offen')));
  L.push('', '## Fakten', ''); H.facts.secured.forEach(f => L.push('- ✅ ' + f.fact + ' (' + f.source + ')')); H.facts.to_check.forEach((c, i) => L.push('- ' + ((hwS(v).factChk || {})[i] ? '☑' : '☐') + ' prüfen: ' + c));
  L.push('', 'Quellen: ' + H.facts.sources.join(' · '), '', '## Vor Posting prüfen', ''); H.approval.pre_post_checks.forEach((c, i) => L.push('- ' + ((hwS(v).prepost || {})[i] ? '[x]' : '[ ]') + ' ' + c));
  return L.join('\n');
}
function hwWinner(v) { const H = v.hw; const x = hwS(v); const i = x.hookPick != null ? x.hookPick : H.hooks.findIndex(h => h.winner); return H.hooks[i >= 0 ? i : 0]; }
function hwHooksCSV(list) { const L = [['Reel', 'Datum', 'Titel', 'Hook-Typ', 'Gesprochener Einstieg', 'Erstes Bild ohne Ton', 'Text-Overlay', 'Offene Frage', ...HW.CRIT.map(c => HW.CRIT_L[c]), 'Gesamt', 'Sieger', 'Begründung'].map(csvEsc).join(';')]; list.forEach(v => { const w = hwWinner(v); v.hw.hooks.forEach(h => L.push([v.id, dateLabel(v) + (v.year || ''), v.title, h.typ, h.text, h.first_frame, ...HW.CRIT.map(c => h.scores[c]), h.total, h === w ? '★' : '', h.reason].map(csvEsc).join(';'))); }); return '﻿' + L.join('\n'); }
function hwVoText(v) { const H = v.hw; return v.id + ' · ' + v.wd + ' ' + dateLabel(v) + (v.year || '') + ' · ' + H.series_name + ' #' + H.episode + ' · ' + v.title + '\n' + '='.repeat(60) + '\nWörter: ' + words(v.vo) + ' · geschätzt ca. ' + Math.round(estVo(v)) + ' s (vorläufig)\n\n--- GESAMTTEXT (in ElevenLabs einfügen, Stimme Mert_V2, Eleven v3) ---\n' + v.vo + '\n\n--- NACH SZENEN ---\n' + H.vo.scenes.map((t, i) => 'Szene ' + (i + 1) + ': ' + t).join('\n') + '\n'; }
function hwMainList() { return DATA.filter(isMain).sort((a, b) => vDate(a) - vDate(b)); }

/* ---------------- Export: Pakete ---------------- */
async function hwZip(v) {
  if (!window.JSZip) { toast('ZIP-Modul nicht geladen – Seite neu laden.'); return; }
  const H = v.hw; const s = st(v.id); toast('Produktionspaket wird gepackt …'); await ensureLoaded(v); const z = new JSZip(); const b = baseName(v);
  z.file('00_LIESMICH.txt', ['haydi-weg Produktionspaket · ' + v.id + ' · ' + v.title, v.wd + ' ' + dateLabel(v) + (v.year || '') + ' · ' + H.series_name + ' #' + H.episode, '', 'Timecodes: ' + hwSceneTimes(v).label, 'Freigabestatus: ' + hwApproval(v), 'Qualitäts-Score (Einschätzung): ' + hwTotal(hwScores(v)).toFixed(2), '', 'Dateien: 01_capcut_schnittplan.csv/.md · 02_sprechtext_elevenlabs.txt · 03_untertitel.srt · 04_hooks.csv · 05_cover.csv · 06_stock_quellen.csv · 07_fakten.md · 08_captions.txt · voiceover/musik (falls hochgeladen)', 'Stand ' + HW.STAND + ' · Reel-Studio v' + HW.VER].join('\n'));
  z.file('01_capcut_schnittplan.csv', hwCutCSV(v)); z.file('01_capcut_schnittplan.md', hwCutMD(v)); z.file('02_sprechtext_elevenlabs.txt', hwVoText(v));
  try { z.file('03_untertitel.srt', srt(subTiming(v))); } catch (e) { }
  z.file('04_hooks.csv', hwHooksCSV([v]));
  z.file('05_cover.csv', '﻿' + [['#', 'Headline', 'gelbes Keyword', 'Bild', 'Variante'].map(csvEsc).join(';'), ...H.covers.map((c, i) => [i + 1, c.headline, c.yellow, c.image, c.variant].map(csvEsc).join(';'))].join('\n'));
  z.file('06_stock_quellen.csv', '﻿' + [['Clip', 'Quelle', 'Referenz', 'Suchbegriffe', 'Lizenz', 'Prüfstand', 'Fehlt', 'Alternative', 'Szenen', 'Status im Studio'].map(csvEsc).join(';'), ...H.stock.map((x, i) => [x.shot, x.source, x.ref, x.search_terms, x.license_status, x.checked, x.missing ? 'JA' : '', x.alternative, x.scenes, (hwS(v).stockChk || {})[i] || 'offen'].map(csvEsc).join(';'))].join('\n'));
  z.file('07_fakten.md', ['# Fakten ' + v.id, '', '## Behauptung', H.claim, H.answer ? '\nAuflösung: ' + H.answer : '', '', '## Gesichert', ...H.facts.secured.map(f => '- ' + f.fact + ' (' + f.source + ')'), '', '## Vor Posting prüfen', ...H.facts.to_check.map(c => '- ' + c), '', 'Quellen: ' + H.facts.sources.join(' · '), 'Stand: ' + H.facts.checked_on].join('\n'));
  z.file('08_captions.txt', 'INSTAGRAM\n\n' + capOf(v, 'ig') + '\n\n\nTIKTOK-TITEL\n\n' + capOf(v, 'tt_title') + '\n\n\nTIKTOK\n\n' + capOf(v, 'tt') + '\n\n\nYOUTUBE-TITEL\n\n' + capOf(v, 'yt') + '\n');
  for (const kind of ['vo', 'music']) { const rec = have.has(fk(v.id, kind)) ? await IDB.get(fk(v.id, kind)).catch(() => null) : null; if (rec) z.file((kind === 'vo' ? 'voiceover' : 'musik') + ext(rec.name || '.mp3'), rec.blob); }
  const blob = await z.generateAsync({ type: 'blob', compression: 'DEFLATE' }); const ok = await saveFile(b + '_produktionspaket.zip', blob); if (ok) toast('Produktionspaket gespeichert');
}
async function hwZipAll() {
  if (!window.JSZip) { toast('ZIP-Modul nicht geladen.'); return; } const list = hwMainList(); toast('Hauptplan-Paket (39 Reels) wird gepackt …'); const z = new JSZip();
  z.file('00_ALLE_39_SCHNITTPLAENE.csv', '﻿' + [['Reel', 'Datum', 'Titel', ...HW.COLS].map(csvEsc).join(';'), ...list.flatMap(v => hwCutRows(v).map(r => [v.id, dateLabel(v) + (v.year || ''), v.title, ...r].map(csvEsc).join(';')))].join('\n'));
  z.file('00_HOOKS_195.csv', hwHooksCSV(list)); z.file('00_ALLE_SPRECHERTEXTE.txt', list.map(hwVoText).join('\n\n'));
  z.file('00_KALENDER.csv', '﻿' + [['Nr', 'Datum', 'Wochentag', 'Serie', 'Folge', 'Titel', 'Ort', 'Cluster', 'Status vs. Plan', 'Freigabe', 'QS'].map(csvEsc).join(';'), ...list.map(v => [v.hw.nr, v.hw.date, v.wd, v.hw.series_name, v.hw.episode, v.title, v.place, v.hw.cluster, v.hw.status_vs_plan, hwApproval(v), hwTotal(hwScores(v)).toFixed(2)].map(csvEsc).join(';'))].join('\n'));
  for (const v of list) { const f = z.folder(baseName(v)); f.file('capcut_schnittplan.csv', hwCutCSV(v)); f.file('capcut_schnittplan.md', hwCutMD(v)); f.file('sprechtext.txt', hwVoText(v)); try { f.file('untertitel.srt', srt(subTiming(v))); } catch (e) { } }
  z.file('studio_zustand.json', JSON.stringify(hwProjectJSON(), null, 1));
  const blob = await z.generateAsync({ type: 'blob', compression: 'DEFLATE' }); const ok = await saveFile('haydi-weg_hauptplan_2026-11-09_bis_2027-02-05.zip', blob); if (ok) toast('Hauptplan-Paket gespeichert');
}
function hwProjectJSON() { const out = { meta: { schema: 'reelstudio_state_v39', exported: new Date().toISOString(), version: HW.VER }, reels: {} }; DATA.forEach(v => { const s = S[v.id]; if (s) out.reels[v.id] = JSON.parse(JSON.stringify(s)); }); return out; }
async function hwImportState(file) { try { const j = JSON.parse(await file.text()); const map = j.reels || j; if (!map || typeof map !== 'object') throw 0; let n = 0; for (const id in map) { if (id === 'meta') continue; j.reels = map; if (!V[id]) continue; S[id] = merge(V[id], j.reels[id]); touch(id); n++; } subCache.key = ''; wtCache.key = ''; renderAll(true); toast(n + ' Reel-Zustände importiert'); } catch (e) { toast('Datei nicht lesbar – erwartet wird eine Studio-Zustandsdatei (JSON).'); } }
async function hwImportMain(file) {
  let j; try { j = JSON.parse(await file.text()); } catch (e) { toast('Datei nicht lesbar – erwartet wird reels_hauptplan_v2.json.'); return; }
  const reels = j && (j.reels || (Array.isArray(j) ? j : null)); if (!reels || !reels.length || !reels[0].cut || !reels[0].hooks) { toast('Kein Hauptplan-Format (reels_hauptplan_v2) erkannt.'); return; }
  const bad = reels.filter(r => !/^H\d{2}$/.test(String(r.id)) || !r.date || !r.vo || !r.vo.full); if (bad.length) { toast(bad.length + ' Reel(s) ohne gültige ID/Datum/Sprechtext – Import abgebrochen.'); return; }
  const text = JSON.stringify(j); try { await IDB.put('lib|hauptplan', { blob: new Blob([text], { type: 'application/json' }), name: file.name, type: 'application/json', json: text, at: Date.now() }); have.add('lib|hauptplan'); } catch (e) { toast('Speichern im Browser fehlgeschlagen – Import gilt nur für diese Sitzung.'); }
  hwApplyMain(reels); renderAll(true); toast(reels.length + ' Hauptplan-Reels importiert (' + file.name + ')');
}
function hwApplyMain(reels) { let n = 0; reels.forEach(r => { const d = hwToData(r); if (V[r.id]) { Object.assign(V[r.id], d); } else { DATA.push(d); V[d.id] = d; } n++; }); subCache.key = ''; wtCache.key = ''; return n; }
async function hwResetMain() { await IDB.del('lib|hauptplan').catch(() => { }); have.delete('lib|hauptplan'); hwApplyMain(HW_MAIN_RAW.reels); renderAll(true); toast('Hauptplan auf die eingebettete Fassung (Stand ' + HW_MAIN_RAW.meta.stand + ') zurückgesetzt'); }

/* ---------------- Karten ---------------- */
function hwBadge(t, cls) { return el('span', { class: 'type ' + (cls || 'info') }, t); }
function hwKsBadge(st0) { return el('span', { class: 'hwks ' + (HW.KS_CLS[st0] || 'mid') }, st0); }
function hwKeyShotTable(v) { const H = v.hw, x = hwS(v); return el('div', { class: 'ptw' }, el('table', { class: 'pt pts' }, el('thead', {}, el('tr', {}, ['Rolle', 'Motiv', 'Quelle / Referenz', 'Status laut Recherche 09.11.', 'Hinweis / Alternative', 'Status im Studio'].map(h => el('th', {}, h)))),
  el('tbody', {}, (H.key_shots || []).map((k, i) => el('tr', { class: k.status === 'nicht gefunden' ? 'miss' : '' }, el('td', {}, el('b', {}, k.role)), el('td', {}, k.motif), el('td', {}, k.source + (k.ref ? ' · ' + k.ref : '')), el('td', {}, hwKsBadge(k.status)), el('td', {}, k.note || '–'),
  el('td', {}, el('select', { 'aria-label': 'Status Schlüsselaufnahme ' + k.role, onchange: e => { x.ksChk = Object.assign({}, x.ksChk || {}, { [i]: e.target.value }); touch(v.id); renderPanels(); } }, HW.STOCK_ST.map(o => el('option', { value: o, selected: ((x.ksChk || {})[i] || 'offen') === o ? true : null }, o))))))))); }
function hwContentCard(v, s, n) {
  const H = v.hw, x = hwS(v); const arc = H.story_arc || {};
  const arcRows = [['Scroll-Stopper', arc.scrollstopper], ['Setup', arc.setup], ['Neugierlücke / Konflikt', arc.curiosity], ['Aufbau', arc.build], ['Auflösung (≥ 70 %)', arc.resolution], ['Zweites Aha', arc.second_aha], ['Starkes Ende', arc.ending]];
  const stat = [['Hauptplan', 'Reel ' + H.nr + ' von 39 · ' + H.series_name + ' #' + H.episode + ' · ' + H.weekday + ' ' + H.date_de + ' · KW ' + H.kw], ['Ort', H.place], H.cluster ? ['Cluster', H.cluster] : null, H.themenwelt ? ['Themenwelt', H.themenwelt + ' – ' + (H.themenwelt_text || '')] : null, H.structure ? ['Storytelling-Struktur', H.structure + ' · ' + (H.structure_name || '')] : null, H.decision_v3 ? ['Upgrade v3 (09.11.)', H.decision_v3 + (H.title_v2 && H.title_v2 !== H.title ? ' · vorher: „' + H.title_v2 + '“' : '') + (H.decision_reason ? ' – ' + H.decision_reason : '')] : (H.status_vs_plan ? ['Status vs. Masterplan 06.11.', H.status_vs_plan + ' · Plan-Konsens ' + H.plan_konsens] : null), H.hotel ? ['Hotel / Resort (konkret)', H.hotel] : null, H.target_sec ? ['Länge', 'Ziel ca. ' + H.target_sec + ' s · vorläufig ' + H.cut.total_sec.toFixed(1) + ' s (Timecodes erst nach Audio)'] : null, H.end_card ? ['Endkarte', H.end_card + (H.teaser_spoken ? ' · Teaser gesprochen + Grafik' : ' · Teaser nur als Grafik')] : null, ['Prüfbare Behauptung', H.claim], H.answer ? ['Auflösung', H.answer] : null, ['DACH-Anker', H.dach_anchor], ['Emotion', H.emotion]].filter(Boolean);
  const prod = [['Voiceover', s.vo ? '✓ ' + s.vo.name + ' (' + fmtS(s.vo.dur || 0) + ')' : 'fehlt – ElevenLabs-Datei unten ablegen'], ['CapCut-Video', s.final ? '✓ ' + s.final.name : 'fehlt'], ['Hook & Cover (QA)', x.hookApproved ? '✓ freigegeben' : 'offen'], ['Freigabe', hwApproval(v)], ['Export', s.exported ? '✓ Video fertig' : 'offen'], ['Veröffentlicht', (s.posted.ig ? 'Instagram ✓ ' : '') + (s.posted.tt ? 'TikTok ✓' : '') || 'noch nicht']];
  return card(n, 'Content-Studio – Konzept & Produktionsstatus', el('div', { class: 'plan pkg' },
    el('div', { class: 'row' }, hwBadge(H.series_name + ' #' + H.episode, 'wow'), hwBadge(hwApproval(v), hwApproval(v) === 'Freigegeben' ? 'wow' : 'info'), el('span', { class: 'meta' }, 'QS ' + hwTotal(hwScores(v)).toFixed(2) + ' / 10 (Einschätzung)'), H.plan_konsens ? el('span', { class: 'meta' }, 'Plan-Konsens ' + H.plan_konsens) : null),
    el('div', { class: 'psec' }, el('h3', {}, 'Konzept'), pkgRows(stat)),
    el('div', { class: 'psec' }, el('h3', {}, 'Storytelling-Bogen' + (H.structure_name ? ' – ' + H.structure_name : '')), pkgRows(arcRows)),
    (H.key_shots || []).length ? el('div', { class: 'psec' }, el('h3', {}, 'Schlüsselaufnahmen – Material zuerst'), hwKeyShotTable(v)) : null,
    el('div', { class: 'psec' }, el('h3', {}, 'Produktionsstatus'), pkgRows(prod)),
    (H.changelog_vs_plan || []).length ? el('div', { class: 'psec' }, el('h3', {}, 'Änderungen gegenüber dem Masterplan'), el('ul', { class: 'hwul' }, H.changelog_vs_plan.map(c => el('li', {}, c)))) : null,
    (H.open_points || []).length ? el('div', { class: 'note warn', style: 'margin-top:10px' }, el('b', {}, 'Offen: '), H.open_points.join(' · ')) : null,
    el('label', { class: 'f', style: 'margin-top:10px' }, 'Notizen zu diesem Reel', el('textarea', { rows: 3, value: x.notes || '', oninput: e => { x.notes = e.target.value; touch(v.id); } }))));
}
function hwHookCard(v, s, n) {
  const H = v.hw, x = hwS(v); const win = hwWinner(v); const wi = H.hooks.indexOf(win);
  const tbl = el('table', { class: 'pt pts hwt' }, el('thead', {}, el('tr', {}, ['★', 'Typ', 'Gesprochener Einstieg', 'Erstes Bild (ohne Ton)', 'Text-Overlay', 'Offene Frage', ...HW.CRIT.map(c => HW.CRIT_L[c]), 'Ø', 'Bewertung', ''].map(h => el('th', {}, h)))),
    el('tbody', {}, H.hooks.map((h, i) => el('tr', { class: i === wi ? 'win' : '' }, el('td', {}, el('input', { type: 'radio', name: 'hwhook-' + v.id, checked: i === wi, 'aria-label': 'Sieger', onchange: () => { x.hookPick = i; touch(v.id); renderPanels(); } })), el('td', {}, h.typ), el('td', { class: 'pvo' }, h.spoken || h.text), el('td', {}, h.first_frame), el('td', { class: 'pvo' }, (h.overlay || '–').replace(/\*/g, '')), el('td', {}, h.question || '–'), ...HW.CRIT.map(c => el('td', { class: 'tc' }, String(h.scores[c]))), el('td', { class: 'tc' }, el('b', {}, h.total.toFixed(2))), el('td', {}, h.reason),
      el('td', {}, h.overlay ? el('button', { class: 'btn sm', type: 'button', title: 'Text-Overlay dieses Hooks als Hook-Overlay im Video verwenden', onclick: () => { s.hook = h.overlay; touch(v.id); renderPanels(); renderHead(); if (!E.playing) seekSoon(.6); toast('Hook-Overlay übernommen: ' + h.overlay.replace(/\*/g, '')); } }, 'Overlay') : null)))));
  const covers = el('div', { class: 'hwcov' }, H.covers.map((c, i) => { const hk = c.yellow && c.headline.includes(c.yellow) ? c.headline.replace(c.yellow, '*' + c.yellow + '*') : c.headline; return el('div', { class: 'hwc' + ((x.coverPick ?? 0) === i ? ' on' : '') }, el('b', {}, 'Cover ' + (i + 1) + ' · ' + c.variant), el('div', { class: 'hwh' }, c.headline), el('small', {}, 'gelb: ' + c.yellow + ' · Bild: ' + c.image),
    el('div', { class: 'row' }, el('button', { class: 'btn sm', type: 'button', onclick: () => { s.hook = hk; x.coverPick = i; touch(v.id); renderPanels(); renderHead(); if (!E.playing) seekSoon(.6); toast('Hook-Overlay übernommen: ' + c.headline); } }, 'Als Hook-Overlay'), el('button', { class: 'btn sm ghost', type: 'button', onclick: () => { s.coverText = hk; x.coverPick = i; touch(v.id); renderPanels(); toast('Cover-Headline übernommen'); } }, 'Als Cover-Headline'))); }));
  return card(n, 'Hook-Studio – 5 Hooks (Bild · Satz · Overlay · Frage), Bewertung, Sieger & 3 Cover', el('div', { class: 'plan pkg' },
    el('p', { class: 'hint', style: 'margin:0 0 8px' }, 'Jeder Hook ist die Kombination aus erstem sichtbaren Bild (muss ohne Ton funktionieren), gesprochenem Einstieg, Text-Overlay und der offenen Frage im Kopf des Zuschauers. Fünf Typen: Visueller Schock · Neugierlücke · Überraschende Behauptung · Emotionaler Konflikt · Erwartung gegen Realität. Sieben Kriterien je 1–10 – Einschätzungen der Redaktion, keine Messwerte. Der Sieger ist der erste gesprochene Satz; „Overlay“ übernimmt das Text-Overlay des Hooks ins Video (ein *Wort* in Gelb), die Cover-Buttons setzen Cover-Headline oder Hook-Overlay aus dem Cover-Konzept. Mit dem Radio-Button wählst du einen anderen Sieger.'),
    el('div', { class: 'ptw' }, tbl),
    el('div', { class: 'note', style: 'margin-top:10px' }, el('b', {}, 'Sieger: '), win.text, ' – ', H.hook_winner_reason + (x.hookPick != null && x.hookPick !== H.hooks.findIndex(h => h.winner) ? ' (Redaktionsvorschlag war: „' + H.hook_winner + '“)' : '')),
    el('div', { class: 'psec' }, el('h3', {}, 'Cover-Konzepte (3)'), covers),
    el('div', { class: 'row', style: 'margin-top:10px' }, el('label', { class: 'ck' }, el('input', { type: 'checkbox', checked: !!x.hookApproved, onchange: e => { x.hookApproved = e.target.checked; touch(v.id); renderPanels(); renderHead(); } }), 'Hook & Cover geprüft und freigegeben (QA)'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl(baseName(v) + '_hooks.csv', hwHooksCSV([v]), 'text/csv;charset=utf-8') }, 'Hooks als CSV'))));
}
function hwCapcutCard(v, s, n) {
  const H = v.hw; const T = hwSceneTimes(v); const rows = hwCutRows(v); const vo = voInfo(v);
  const tbl = el('table', { class: 'pt hwt' }, el('thead', {}, el('tr', {}, HW.COLS.map(h => el('th', {}, h)))), el('tbody', {}, rows.map(r => el('tr', {}, r.map((x, i) => el('td', { class: i <= 3 ? 'tc' : (i === 4 ? 'pvo' : '') }, String(x)))))));
  const total = T.rows.length ? T.rows[T.rows.length - 1].end : H.cut.total_sec;
  const stockTbl = el('table', { class: 'pt pts' }, el('thead', {}, el('tr', {}, ['Clip', 'Quelle', 'Referenz', 'Suchbegriffe', 'Lizenz', 'Prüfstand', 'Szenen'].map(h => el('th', {}, h)))),
    el('tbody', {}, H.stock.map(x => el('tr', { class: x.missing ? 'miss' : '' }, el('td', {}, (x.missing ? '⚠ ' : '') + x.shot + (x.missing ? ' – FEHLT · Alternative: ' + x.alternative : '')), el('td', {}, x.source), el('td', {}, x.ref), el('td', {}, x.search_terms), el('td', {}, x.license_status), el('td', {}, x.checked), el('td', { class: 'tc' }, x.scenes || '')))));
  return card(n, 'CapCut-Studio – vollständiger Schnittplan (16 Felder je Szene)', el('div', { class: 'plan pkg' },
    el('div', { class: 'row' }, hwBadge(T.real ? 'Zeiten aus Audio' : 'Zeiten vorläufig', T.real ? 'wow' : 'akte'), el('span', { class: 'meta' }, H.cut.format), el('span', { class: 'meta' }, 'Gesamt ' + tcCap(total) + ' (' + (+total).toFixed(1) + ' s)'), el('span', { class: 'meta' }, rows.length + ' Szenen'), vo.real ? el('span', { class: 'meta' }, 'Sprechzeit ' + fmtS(vo.dur) + ' · ' + (words(v.vo) / Math.max(1, vo.dur)).toFixed(2) + ' W/s') : el('span', { class: 'meta' }, 'geschätzt ' + fmtS(estVo(v)) + ' Sprechzeit')),
    el('div', { class: 'note' + (T.real ? '' : ' warn'), style: 'margin-top:10px' }, el('b', {}, 'Timecode-Regel: '), T.label),
    el('div', { class: 'ptw', style: 'margin-top:10px' }, tbl),
    el('div', { class: 'row', style: 'margin-top:10px' },
      el('button', { class: 'btn sm primary', type: 'button', onclick: async () => { try { await navigator.clipboard.writeText(hwCutMD(v)); toast('Schnittplan kopiert'); } catch (e) { toast('Kopieren nicht möglich – CSV/MD herunterladen'); } } }, 'Schnittplan kopieren'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl(baseName(v) + '_capcut.csv', hwCutCSV(v), 'text/csv;charset=utf-8') }, 'CSV'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl(baseName(v) + '_capcut.md', hwCutMD(v), 'text/markdown;charset=utf-8') }, 'Markdown'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl(baseName(v) + '_capcut.json', JSON.stringify({ id: v.id, title: v.title, timing: T.label, scenes: H.cut.scenes.map((sc, i) => Object.assign({}, sc, { tc_in: rows[i][1], tc_out: rows[i][2], dur_s: +rows[i][3] })) }, null, 1), 'application/json') }, 'JSON'),
      el('button', { class: 'btn sm accent', type: 'button', onclick: () => hwZip(v) }, '⬇ Produktionspaket (ZIP)')),
    el('div', { class: 'psec' }, el('h3', {}, 'VO-Mapping (Sprechtext je Szene, für ElevenLabs)'), el('ol', { class: 'hwol' }, H.vo.scenes.map(t => el('li', {}, t))), el('div', { class: 'row' }, el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl(baseName(v) + '_sprechtext.txt', hwVoText(v)) }, 'Sprechtext (TXT)'))),
    el('div', { class: 'psec' }, el('h3', {}, 'Stock-Suchbegriffe & Lizenzstatus'), el('div', { class: 'ptw' }, stockTbl))));
}
function hwAudioCard(v, s, n) {
  const m = MEDIA.get(fk(v.id, 'vo')); const vo = voInfo(v); const H = v.hw; const est = estVo(v);
  if (!vo.real) return card(n, 'Audio-Analyse – reale Sprechdauer', el('div', { class: 'note warn' }, el('b', {}, 'Noch keine Audiodatei. '), 'Leg oben die ElevenLabs-MP3/WAV ab. Das Studio misst dann Dauer, Sprachsegmente, Pausen und Silbenkerne lokal im Browser (ohne API) und rechnet Szenen und Untertitel auf die echte Stimme um. Bis dahin gilt die Schätzung: ' + fmtS(est) + ' Sprechzeit, Gesamt ' + H.cut.total_tc + ' (vorläufig).'));
  const segs = m && m.segs ? m.segs : []; const nuc = m && m.nuclei ? m.nuclei : []; const pauses = m ? voPauses(m, s.voStart || 0) : []; const wps = words(v.vo) / Math.max(.1, vo.dur); const delta = vo.dur - est;
  const T = hwSceneTimes(v);
  return card(n, 'Audio-Analyse – reale Sprechdauer & Synchronisation', el('div', { class: 'plan pkg' },
    pkgRows([['Datei', s.vo ? s.vo.name : (vo.fromVideo ? 'Ton aus dem CapCut-Video' : '–')], ['Reale Sprechdauer', fmtS(vo.dur) + ' (' + vo.dur.toFixed(2) + ' s)'], ['Schätzung vorher', fmtS(est) + ' → Abweichung ' + (delta >= 0 ? '+' : '−') + Math.abs(delta).toFixed(1) + ' s'], ['Sprechtempo', wps.toFixed(2) + ' Wörter/s (' + words(v.vo) + ' Wörter)'], ['Sprachsegmente', segs.length + ' erkannt' + (segs.length ? ' · erstes ab ' + fmtS(segs[0][0]) : '')], ['Silbenkerne', nuc.length + ' erkannt (lokale Silben-Erkennung)'], ['Sprechpausen > 0,7 s', pauses.length ? pauses.map(p => fmtS(p.d) + ' bei ' + fmtS(p.t)).join(' · ') : 'keine'], ['Untertitel-Zeiten', s.subSrc === 'manual' ? 'manuell korrigiert' : s.subSrc === 'import' ? 'importiert (SRT/JSON)' : s.subSrc === 'tap' ? 'getappt' : 'automatisch an Pausen & Silben ausgerichtet'], ['Szenen-Zeiten', T.label]]),
    el('div', { class: 'row', style: 'margin-top:10px' }, el('button', { class: 'btn sm accent', type: 'button', onclick: () => { autoSync(); setTimeout(renderPanels, 50); } }, '⚡ Szenen & Untertitel aus Audio neu berechnen'), el('button', { class: 'btn sm', type: 'button', onclick: () => play(0) }, '▶ Mit Untertiteln prüfen')),
    el('p', { class: 'hint', style: 'margin:0' }, 'Was hier passiert: Hüllkurve (50-ms-Fenster) → Sprach-/Pausen-Maske → Segmente; Bandpass 300–2800 Hz → Silbenkerne; Untertitelzeilen werden per dynamischer Programmierung auf die Segmente gelegt und innerhalb eines Segments an den Silbenkernen verteilt (lokale Forced-Alignment-Näherung, kostenlos, ohne API). Für wortgenaue Zeitstempel: ElevenLabs „Speech to Text“-JSON importieren.')));
}
function hwSubTable(v, s) {
  const items = subTiming(v); const vo = voInfo(v); const off = (vo.fromVideo ? 0 : (s.voStart || 0)) + (+s.subOff || 0);
  const setT = (i, k, val) => { const it = subTiming(v); const tm = it.map(q => [q.start - off, q.end - .12 - off]); if (k === 'start') tm[i][0] = val - off; else tm[i][1] = val - .12 - off; if (tm[i][1] <= tm[i][0]) tm[i][1] = tm[i][0] + .3; s.subTimes = tm.map(([a, b]) => [Math.max(0, Math.round(a * 1000) / 1000), Math.round(b * 1000) / 1000]); s.subSrc = 'manual'; subCache.key = ''; wtCache.key = ''; touch(v.id); renderPanels(); if (!E.playing) seekSoon(Math.max(0, val - .2)); };
  const shift = d => { const it = subTiming(v); s.subTimes = it.map(q => [Math.max(0, Math.round((q.start - off + d) * 1000) / 1000), Math.round((q.end - .12 - off + d) * 1000) / 1000]); s.subSrc = 'manual'; subCache.key = ''; wtCache.key = ''; touch(v.id); renderPanels(); };
  const tbl = el('table', { class: 'pt pts hwt' }, el('thead', {}, el('tr', {}, ['#', 'Start (s)', 'Ende (s)', 'TC', 'Text', ''].map(h => el('th', {}, h)))),
    el('tbody', {}, items.map((it, i) => el('tr', {}, el('td', { class: 'tc' }, String(i + 1)),
      el('td', {}, el('input', { type: 'number', step: '0.01', min: '0', value: it.start.toFixed(2), 'aria-label': 'Start Zeile ' + (i + 1), onchange: e => setT(i, 'start', +e.target.value) })),
      el('td', {}, el('input', { type: 'number', step: '0.01', min: '0', value: it.end.toFixed(2), 'aria-label': 'Ende Zeile ' + (i + 1), onchange: e => setT(i, 'end', +e.target.value) })),
      el('td', { class: 'tc' }, tcCap(it.start) + ' – ' + tcCap(it.end)), el('td', {}, it.text.replace(/\*/g, '')),
      el('td', {}, el('button', { class: 'btn sm', type: 'button', title: 'Ab hier anhören', onclick: () => play(Math.max(0, it.start - .3)) }, '▶'))))));
  return el('details', { class: 'mp hwsub', open: s.subSrc === 'manual' ? true : null }, el('summary', {}, el('b', {}, 'Untertitel-Zeiten je Zeile prüfen und korrigieren (' + items.length + ' Zeilen' + (s.subSrc === 'manual' ? ' · manuell korrigiert' : '') + ')')),
    el('div', { class: 'row', style: 'margin:8px 0' }, el('button', { class: 'btn sm', type: 'button', onclick: () => shift(-.1) }, '− 0,1 s alle'), el('button', { class: 'btn sm', type: 'button', onclick: () => shift(.1) }, '+ 0,1 s alle'), el('button', { class: 'btn sm ghost', type: 'button', onclick: () => { s.subTimes = null; s.subSrc = null; subCache.key = ''; wtCache.key = ''; touch(v.id); renderPanels(); toast('Zeiten wieder automatisch'); } }, 'Zurück auf automatisch'), el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl(baseName(v) + '_untertitel.srt', srt(subTiming(v)), 'text/plain;charset=utf-8') }, 'SRT exportieren')),
    el('div', { class: 'ptw' }, tbl), el('p', { class: 'hint', style: 'margin:6px 0 0' }, 'Start/Ende in Sekunden (Videozeit). Änderungen gelten sofort in Vorschau, Export und SRT. „Zurück auf automatisch“ nutzt wieder die Ausrichtung an deiner Stimme.'));
}
function hwQualityCard(v, s, n) {
  const H = v.hw, x = hwS(v); const sc = hwScores(v); const tot = hwTotal(sc); const ref = H.scorecard.total; const g = hwGate(v);
  const sliders = Object.keys(HW.W).map(k => el('label', { class: 'f' }, HW.QS_L[k] + ' · ' + HW.W[k] + ' %', el('div', { class: 'rg' }, el('input', { type: 'range', min: 1, max: 10, step: 1, value: sc[k], oninput: e => { x.score = Object.assign({}, x.score || {}, { [k]: +e.target.value }); touch(v.id); const t2 = hwTotal(hwScores(v)); totEl.textContent = t2.toFixed(2); totEl.className = 'hwtot ' + (t2 >= 9 ? 'ok' : t2 >= 8.5 ? 'mid' : 'low'); e.target.nextSibling.textContent = e.target.value + ' / 10'; } }), el('output', {}, sc[k] + ' / 10'))));
  const totEl = el('span', { class: 'hwtot ' + (tot >= 9 ? 'ok' : tot >= 8.5 ? 'mid' : 'low') }, tot.toFixed(2));
  const appr = el('select', { onchange: e => { const want = e.target.value; if (want === 'Freigegeben' && !hwGate(v).ok) { e.target.value = hwApproval(v); toast('Freigabe erst, wenn Faktencheck, Materialcheck, Vortags-Prüfung und Hook-QA abgehakt sind.'); return; } x.approval = want; (x.log = x.log || []).push({ t: new Date().toISOString().slice(0, 16).replace('T', ' '), m: 'Status → ' + want }); touch(v.id); renderPanels(); renderHead(); renderList(); } }, HW.APPR.map(a => el('option', { value: a, selected: hwApproval(v) === a ? true : null }, a)));
  const logIn = el('input', { type: 'text', placeholder: 'Verbesserung notieren … (Enter)', onkeydown: e => { if (e.key === 'Enter' && e.target.value.trim()) { (x.log = x.log || []).push({ t: new Date().toISOString().slice(0, 16).replace('T', ' '), m: e.target.value.trim() }); e.target.value = ''; touch(v.id); renderPanels(); } } });
  return card(n, 'Qualitäts-Studio – Scorecard, Faktencheck, Materialcheck, Freigabe', el('div', { class: 'plan pkg' },
    el('div', { class: 'row' }, el('b', {}, 'Gewichteter Gesamtwert: '), totEl, el('span', { class: 'meta' }, '/ 10 · Ziel ≥ 9,0 · Redaktion 09.11.: ' + ref.toFixed(2)), hwBadge(hwApproval(v), hwApproval(v) === 'Freigegeben' ? 'wow' : 'info')),
    el('p', { class: 'hint', style: 'margin:6px 0 0' }, 'Gewichtung laut Auftrag: ' + Object.keys(HW.W).map(k => HW.QS_L[k] + ' ' + HW.W[k] + ' %').join(' · ') + '. Noten sind Einschätzungen – keine Messwerte, keine Erfolgsversprechen. Schwache Konzepte wurden mindestens zweimal überarbeitet (siehe Protokoll).'),
    el('div', { class: 'ctl', style: 'margin-top:10px' }, sliders),
    el('div', { class: 'psec' }, el('h3', {}, 'Faktencheck ' + (g.factsOk ? '✓' : '')), el('ul', { class: 'hwul' }, H.facts.secured.map(f => el('li', {}, '✅ ' + f.fact, el('small', {}, ' – ' + f.source)))),
      el('div', { class: 'pchk' }, H.facts.to_check.map((c, i) => el('label', { class: 'ck' }, el('input', { type: 'checkbox', checked: !!(x.factChk && x.factChk[i]), onchange: e => { x.factChk = Object.assign({}, x.factChk || {}, { [i]: e.target.checked }); touch(v.id); renderPanels(); } }), 'prüfen: ' + c))), el('p', { class: 'hint', style: 'margin:6px 0 0' }, 'Quellen: ' + H.facts.sources.join(' · ') + ' · Stand ' + H.facts.checked_on)),
    el('div', { class: 'psec' }, el('h3', {}, 'Materialcheck & Bildrechte ' + (g.stockOk ? '✓' : '')), el('div', { class: 'ptw' }, el('table', { class: 'pt pts' }, el('thead', {}, el('tr', {}, ['Clip', 'Quelle / Referenz', 'Lizenz laut Plan', 'Status im Studio'].map(h => el('th', {}, h)))),
      el('tbody', {}, H.stock.map((st0, i) => el('tr', { class: st0.missing ? 'miss' : '' }, el('td', {}, (st0.missing ? '⚠ ' : '') + st0.shot + (st0.missing ? ' – FEHLT: ' + st0.alternative : '')), el('td', {}, st0.source + ' ' + st0.ref), el('td', {}, st0.license_status),
        el('td', {}, st0.source === 'Eigene Grafik' ? 'eigene Grafik ✓' : el('select', { onchange: e => { x.stockChk = Object.assign({}, x.stockChk || {}, { [i]: e.target.value }); touch(v.id); renderPanels(); } }, HW.STOCK_ST.map(o => el('option', { value: o, selected: ((x.stockChk || {})[i] || 'offen') === o ? true : null }, o))))))))), el('p', { class: 'hint', style: 'margin:6px 0 0' }, 'Prüfstand 09.11.2026: Für die Schlüsselaufnahmen wurden die Suchergebnisseiten von Pexels bzw. Envato Elements geöffnet und passende Treffer (ID/Titel) protokolliert – „gefunden“ heißt gelistet, nicht lizenziert. Detailseiten (Ort, Urheber, Lizenz, Personen) vor jedem Download prüfen; Envato-Lizenz je Download registrieren. Keine Käufe ohne Freigabe (Budget max. 50 €/Monat).')),
    (H.key_shots || []).length ? el('div', { class: 'psec' }, el('h3', {}, 'Schlüsselaufnahmen (3) – Status'), hwKeyShotTable(v)) : null,
    el('div', { class: 'psec' }, el('h3', {}, 'Vor Posting prüfen (Vortag) ' + (g.preOk ? '✓' : '')), el('div', { class: 'pchk' }, H.approval.pre_post_checks.map((c, i) => el('label', { class: 'ck' }, el('input', { type: 'checkbox', checked: !!(x.prepost && x.prepost[i]), onchange: e => { x.prepost = Object.assign({}, x.prepost || {}, { [i]: e.target.checked }); touch(v.id); renderPanels(); } }), c))),
      el('div', { class: 'pchk', style: 'margin-top:6px' }, H.approval.requirements.map(r => el('span', { class: 'meta' }, '• ' + r)))),
    el('div', { class: 'psec' }, el('h3', {}, 'Freigabestatus'), el('div', { class: 'row' }, appr, el('span', { class: 'hint', style: 'margin:0' }, g.ok ? 'Alle Pflichtprüfungen erledigt – Freigabe möglich.' : 'Für „Freigegeben“ fehlen: ' + [!g.factsOk && 'Faktencheck', !g.stockOk && 'Materialcheck', !g.preOk && 'Vortags-Prüfung', !g.hookOk && 'Hook-QA'].filter(Boolean).join(', ')))),
    el('div', { class: 'psec' }, el('h3', {}, 'Verbesserungsprotokoll'), el('ol', { class: 'hwol' }, H.scorecard.iterations.map((it, i) => el('li', {}, el('b', {}, 'Runde ' + (i + 1) + ': '), it)), (x.log || []).map(l => el('li', {}, el('b', {}, l.t + ': '), l.m))), logIn)));
}

/* ---------------- Überschreibungen der v37-Renderer ---------------- */
const hw_renderPanels = renderPanels, hw_renderHead = renderHead, hw_renderList = renderList, hw_renderStats = renderStats, hw_renderExport = renderExport;
function hwRenumber() { let i = 1; $('#panels').querySelectorAll('section.card > h2 > .n').forEach(nn => nn.textContent = String(i++)); }
function hwCardByTitle(re) { return [...$('#panels').querySelectorAll('section.card')].find(c => re.test(c.querySelector('h2') ? c.querySelector('h2').textContent : '')); }
renderPanels = function () {
  hw_renderPanels(); const v = V[CUR]; if (!isMain(v)) return; const s = st(v.id); const p = $('#panels');
  const mp = hwCardByTitle(/Material-Plan/); if (mp) mp.remove();
  const first = p.firstElementChild && p.firstElementChild.classList.contains('modebar') ? p.firstElementChild.nextElementSibling : p.firstElementChild;
  p.insertBefore(hwContentCard(v, s, 0), first); p.insertBefore(hwHookCard(v, s, 0), first); p.insertBefore(hwCapcutCard(v, s, 0), first);
  const voCard = hwCardByTitle(/Voiceover/); const subs = hwCardByTitle(/^\s*\d*\s*Untertitel\s*$/) || hwCardByTitle(/Untertitel/);
  const audio = hwAudioCard(v, s, 0); if (voCard && voCard.nextSibling) p.insertBefore(audio, voCard.nextSibling); else if (subs) p.insertBefore(audio, subs); else p.append(audio);
  if (subs) subs.append(hwSubTable(v, s));
  const exp = hwCardByTitle(/Export/); const q = hwQualityCard(v, s, 0); if (exp) p.insertBefore(q, exp); else p.append(q);
  hwRenumber();
};
renderHead = function () {
  const v = V[CUR]; if (!isMain(v)) { hw_renderHead(); return; } const s = st(v.id); const H = v.hw; const tl = TL(v); const h = $('#vhead'); h.innerHTML = ''; const date = vDate(v); const ap = hwApproval(v);
  h.append(el('div', { class: 'eyebrow' }, el('span', { class: 'type wow' }, H.series_name + ' #' + H.episode), MON[date.getDay()] + ', ' + v.day + '. ' + MONN[(v.month || 10) - 1] + ' ' + (v.year || 2026) + ' · Hauptplan 09.11.2026–05.02.2027 · Reel ' + H.nr + '/39 · Instagram + TikTok + YouTube Shorts', el('span', { class: 'type ' + (ap === 'Freigegeben' ? 'wow' : 'info') }, ap), el('span', { class: 'meta' }, 'QS ' + hwTotal(hwScores(v)).toFixed(2)), H.themenwelt ? el('span', { class: 'type info' }, H.themenwelt) : null, H.structure ? el('span', { class: 'meta', title: H.structure_name }, 'Struktur ' + H.structure) : null),
    el('h1', {}, v.title), el('div', { class: 'hookline' }, el('span', { class: 'hand' }, 'Hook:'), el('q', {}, String(s.hook || '').replace(/\*/g, '').replace(EMOJI_ALL, '').trim())),
    el('div', { class: 'metas' }, el('span', { class: 'meta', id: 'mLen' }, 'Länge ' + fmtS(tl.total) + (tl.vo.real ? '' : ' (geschätzt)')), el('span', { class: 'meta' }, 'Plan ' + H.cut.total_tc + ' (vorläufig)'), el('span', { class: 'meta' }, '9:16 · 1080 × 1920 · 30 fps'), el('span', { class: 'meta' }, H.place), finalMode(v) ? el('span', { class: 'meta' }, s.final ? 'CapCut-Video: ' + s.final.name : 'CapCut-Video fehlt') : el('span', { class: 'meta' }, s.shots.length + ' Szenen')));
};
renderList = function () {
  const box = $('#list'); box.innerHTML = ''; const nSp = DATA.filter(v => v.plan === 'special').length, nMain = DATA.filter(isMain).length;
  const plans = el('div', { class: 'filters', role: 'group', 'aria-label': 'Plan' }, [['main', 'Hauptplan ' + nMain], ['special', 'Specials ' + nSp], ['all', 'Alle']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'aria-pressed': String(HW.PLAN === k), 'data-plan': k, onclick: () => { HW.PLAN = k; lsSet('hw-plan', k); renderList(); } }, l)));
  box.append(plans);
  if (HW.PLAN === 'main') {
    box.append(el('div', { class: 'filters', role: 'group', 'aria-label': 'Serie' }, [['all', 'Alle Serien'], ['FoF', 'Mo · Fakt oder Fake?'], ['WDKS', 'Mi · Was dir keiner sagt'], ['RW', 'Fr · Reisewissen']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'aria-pressed': String(HW.SERIE === k), onclick: () => { HW.SERIE = k; renderList(); } }, l))),
      el('div', { class: 'filters', role: 'group', 'aria-label': 'Themenwelt' }, [['all', 'Alle Themenwelten'], ['Natur-Wunder', 'Natur-Wunder'], ['Hotel-Legenden', 'Hotel-Legenden'], ['Regeln & Realität', 'Regeln & Realität'], ['Alte Welten', 'Alte Welten']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'data-tw': k, 'aria-pressed': String(HW.TW === k), onclick: () => { HW.TW = k; renderList(); } }, l))),
      el('div', { class: 'filters', role: 'group', 'aria-label': 'Status' }, [['all', 'Alle'], ['11', 'Nov'], ['12', 'Dez'], ['1', 'Jan'], ['2', 'Feb'], ['open', 'Offen'], ['frei', 'Freigegeben'], ['novo', 'ohne Audio']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'aria-pressed': String(HW.STATUS === k), onclick: () => { HW.STATUS = k; renderList(); } }, l))));
  } else box.append(el('div', { class: 'filters', role: 'group', 'aria-label': 'Filter' }, [['all', 'Alle'], ['11', 'November'], ['12', 'Dezember'], ['1', 'Januar'], ['open', 'Offen']].map(([k, l]) => el('button', { class: 'chip', type: 'button', 'aria-pressed': String(FILTER === k), onclick: () => { FILTER = k; renderList(); } }, l))));
  box.append(el('button', { class: 'btn sm', type: 'button', style: 'width:100%;justify-content:center;margin-bottom:4px', onclick: openNewProject }, '＋ Neues Projekt'));
  const list = DATA.filter(v => HW.PLAN === 'all' ? true : HW.PLAN === 'main' ? (isMain(v) || v.custom) : (!isMain(v))).slice().sort((a, b) => (a.custom ? 1 : 0) - (b.custom ? 1 : 0) || vDate(a) - vDate(b));
  let lastKw = '';
  list.forEach(v => {
    const pr = progress(v); const s = st(v.id);
    if (isMain(v)) { if (HW.SERIE !== 'all' && v.hw.series !== HW.SERIE) return; if (HW.TW !== 'all' && v.hw.themenwelt !== HW.TW) return; const st0 = HW.STATUS; if (st0 === 'open' ? hwApproval(v) === 'Freigegeben' : st0 === 'frei' ? hwApproval(v) !== 'Freigegeben' : st0 === 'novo' ? !!s.vo : (st0 !== 'all' && String(v.month) !== st0)) return; }
    else if (!v.custom && HW.PLAN !== 'main') { if (FILTER === 'open' ? pr.done === pr.of : (FILTER !== 'all' && String(v.month || 10) !== FILTER)) return; }
    const k = kw(v); if (k !== lastKw) { box.append(el('div', { class: 'kw' }, k)); lastKw = k; }
    const ap = isMain(v) ? hwApproval(v) : null;
    box.append(el('button', { class: 'item', type: 'button', 'aria-current': String(v.id === CUR), 'data-id': v.id, onclick: () => select(v.id) },
      el('div', { class: 'd' }, el('small', {}, v.wd), el('b', {}, dateLabel(v)), el('small', {}, isMain(v) ? (v.hw.series + (v.hw.structure ? ' · ' + v.hw.structure : '')) : v.time)),
      el('div', {}, el('div', { class: 't' }, v.kind === 'wow' ? v.title.replace('WOW-Edit: ', '') : v.title),
        el('div', { class: 'm' }, el('span', { class: 'type ' + (isMain(v) ? 'wow' : v.kind) }, v.fmt || (v.kind === 'wow' ? 'WOW' : 'Info')),
          el('div', { class: 'bar', title: pr.done + ' von ' + pr.of + ' Schritten' }, el('i', { class: pr.done === pr.of ? 'full' : '', style: 'width:' + (100 * pr.done / pr.of) + '%' })),
          ap ? el('span', { class: 'posted' + (ap === 'Freigegeben' ? ' on' : ''), title: 'Freigabe: ' + ap }, ap === 'Freigegeben' ? 'OK' : 'QS') : null,
          el('span', { class: 'posted' + (s.posted.ig ? ' on' : ''), title: 'Instagram' }, 'IG'), el('span', { class: 'posted' + (s.posted.tt ? ' on' : ''), title: 'TikTok' }, 'TT')))));
  });
  const mp = $('#mpick'); mp.innerHTML = ''; DATA.slice().sort((a, b) => (a.custom ? 1 : 0) - (b.custom ? 1 : 0) || vDate(a) - vDate(b)).forEach(v => mp.append(el('option', { value: v.id, selected: v.id === CUR ? true : null }, (isMain(v) ? '★ ' : '') + v.wd + ' ' + dateLabel(v) + ' · ' + (v.fmt || 'Info') + ' · ' + v.title.replace('WOW-Edit: ', '')))); mp.value = CUR;
  renderStats();
};
renderStats = function () {
  const main = DATA.filter(isMain); let vo = 0, frei = 0, ex = 0, ig = 0; main.forEach(v => { const s = st(v.id); if (s.vo) vo++; if (hwApproval(v) === 'Freigegeben') frei++; if (s.exported) ex++; if (s.posted.ig) ig++; });
  const b = $('#stats'); b.innerHTML = ''; b.append(el('span', {}, el('b', {}, String(main.length)), ' Hauptplan-Reels'), el('span', {}, el('b', {}, String(vo)), ' mit Audio'), el('span', {}, el('b', {}, String(frei)), ' freigegeben'), el('span', {}, el('b', {}, String(ex)), ' exportiert'), el('span', {}, el('b', {}, String(ig)), ' gepostet'), el('span', {}, el('b', {}, String(DATA.filter(v => v.plan === 'special').length)), ' Specials'));
};
renderExport = function () {
  hw_renderExport(); const v = V[CUR]; const box = $('#exp'); if (!box || !isMain(v)) return;
  box.append(el('div', { class: 'track' }, el('h3', {}, '📦 Hauptplan-Exporte & Import'),
    el('div', { class: 'row' },
      el('button', { class: 'btn sm accent', type: 'button', onclick: () => hwZip(v) }, '⬇ Produktionspaket dieses Reels (ZIP)'),
      el('button', { class: 'btn sm', type: 'button', onclick: hwZipAll }, '⬇ Alle 39: Schnittpläne, Hooks, Sprechtexte, SRT (ZIP)'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl('haydi-weg_alle_39_schnittplaene.csv', '﻿' + [['Reel', 'Datum', 'Titel', ...HW.COLS].map(csvEsc).join(';'), ...hwMainList().flatMap(w => hwCutRows(w).map(r => [w.id, dateLabel(w) + (w.year || ''), w.title, ...r].map(csvEsc).join(';')))].join('\n'), 'text/csv;charset=utf-8') }, 'Alle Schnittpläne (CSV)'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl('haydi-weg_195_hooks.csv', hwHooksCSV(hwMainList()), 'text/csv;charset=utf-8') }, '195 Hooks (CSV)'),
      el('button', { class: 'btn sm', type: 'button', onclick: () => hwDl('haydi-weg_studio_zustand.json', JSON.stringify(hwProjectJSON(), null, 1), 'application/json') }, 'Studio-Zustand sichern (JSON)')),
    el('div', { class: 'row', style: 'margin-top:8px' },
      el('label', { class: 'btn sm' }, 'Hauptplan-JSON importieren …', el('input', { type: 'file', accept: '.json,application/json', hidden: true, 'data-hw': 'import-main', onchange: e => { if (e.target.files[0]) hwImportMain(e.target.files[0]); e.target.value = ''; } })),
      el('label', { class: 'btn sm' }, 'Studio-Zustand wiederherstellen …', el('input', { type: 'file', accept: '.json,application/json', hidden: true, 'data-hw': 'import-state', onchange: e => { if (e.target.files[0]) hwImportState(e.target.files[0]); e.target.value = ''; } })),
      have.has('lib|hauptplan') ? el('button', { class: 'btn sm ghost', type: 'button', onclick: hwResetMain }, 'Importierten Hauptplan verwerfen (eingebettete Fassung)') : null),
    el('p', { class: 'hint', style: 'margin:6px 0 0' }, 'Import: Die Datei reels_hauptplan_v3.json (oder eine überarbeitete Fassung im selben Format; v2-Dateien werden weiterhin gelesen) ersetzt Texte, Hooks, Schnittpläne und Fakten der 39 Reels; hochgeladene Dateien, Häkchen und Korrekturen bleiben je Reel-ID erhalten. Eingebettete Fassung: Stand ' + HW_MAIN_RAW.meta.stand + '.')));
};
const hw_baseName_fix = 1;

/* ---------------- Start ---------------- */
(async () => {
  try { const rec = await IDB.get('lib|hauptplan').catch(() => null); if (rec && rec.json) { const j = JSON.parse(rec.json); const reels = j.reels || j; if (reels && reels.length) { hwApplyMain(reels); have.add('lib|hauptplan'); } } } catch (e) { console.warn('Hauptplan-Import', e); }
  if (!lsGet('hw-rs-v40seen')) { const today = new Date(); const t0 = new Date(today.getFullYear(), today.getMonth(), today.getDate()); const nxt = hwMainList().find(v => vDate(v) >= t0) || hwMainList()[0]; if (nxt) { CUR = nxt.id; lsSet('hw-rs-cur', CUR); } lsSet('hw-rs-v40seen', '1'); HW.PLAN = 'main'; lsSet('hw-plan', 'main'); }
  renderAll(true);
})();
