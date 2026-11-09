/* Playwright-Testsuite für das haydi-weg Reel-Studio v39 (Hauptplan v3)
   Aufruf: node studio.test.js [pfad-zur-html] [pfad-zur-test-wav] [pfad-zur-test-mp3]
   Erzeugt testergebnis.json neben dieser Datei. Läuft headless in Chromium. */
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const HTML = path.resolve(process.argv[2] || path.join(__dirname, '..', 'studio', 'reel-studio-v39.html'));
const WAV = path.resolve(process.argv[3] || path.join(__dirname, 'vo_test.wav'));
const MP3 = path.resolve(process.argv[4] || path.join(__dirname, 'vo_test.mp3'));
const R = []; const t0 = Date.now();
function check(id, name, ok, detail) { R.push({ id, name, ok: !!ok, detail: String(detail == null ? '' : detail).slice(0, 400) }); console.log((ok ? 'PASS' : 'FAIL') + ' ' + id + ' ' + name + (detail != null ? ' – ' + String(detail).slice(0, 160) : '')); }
const cardByTitle = (page, re) => page.locator('#panels section.card').filter({ has: page.locator('h2', { hasText: re }) }).first();
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 1000 }, acceptDownloads: true });
  const page = await ctx.newPage(); const errors = [];
  page.on('pageerror', e => errors.push('PAGEERROR ' + e.message)); page.on('console', m => { if (m.type() === 'error' && !/favicon|net::ERR|fonts\.g/i.test(m.text())) errors.push('CONSOLE ' + m.text()); });
  await page.goto('file://' + HTML); await page.waitForSelector('#list .item', { timeout: 30000 });
  check('T01', 'Studio lädt ohne JavaScript-Fehler', errors.length === 0, errors.join(' | ') || 'keine Fehler');
  // T02 Import der 39 + Specials erhalten
  const nMain = await page.locator('#list .item').count();
  await page.click('#list .chip[data-plan="special"]'); await page.waitForTimeout(200); const nSp = await page.locator('#list .item').count();
  await page.click('#list .chip[data-plan="all"]'); await page.waitForTimeout(200); const nAll = await page.locator('#list .item').count();
  await page.click('#list .chip[data-plan="main"]'); await page.waitForTimeout(200);
  check('T02', 'Hauptplan 39 Reels geladen, 51 Specials erhalten', nMain === 39 && nSp === 51 && nAll === 90, `main=${nMain} specials=${nSp} alle=${nAll}`);
  const ids = await page.evaluate(() => DATA.filter(v => v.plan === 'main').map(v => v.id).sort());
  check('T02b', 'IDs H01–H39 vollständig und eindeutig', ids.length === 39 && ids[0] === 'H01' && ids[38] === 'H39' && new Set(ids).size === 39, ids.slice(0, 3).join(',') + '…');
  // T03 Karten
  await page.click('#list .item[data-id="H03"]'); await page.waitForTimeout(600);
  const cards = (await page.locator('#panels section.card h2').allTextContents()).map(t => t.replace(/^\d+/, '').replace(/\s+/g, ' ').trim());
  const need = ['Content-Studio', 'Hook-Studio', 'CapCut-Studio', 'Sprechtext', 'Voiceover', 'Audio-Analyse', 'Hook –', 'Untertitel', 'Beschreibung', 'Qualitäts-Studio', 'Export'];
  check('T03', 'Alle Studio-Karten vorhanden', need.every(n => cards.some(c => c.startsWith(n) || c.includes(n))), cards.join(' | '));
  // T04 Hooks
  const hk = cardByTitle(page, /Hook-Studio/); const hookRows = await hk.locator('table tbody tr').count(); const winRows = await hk.locator('table tbody tr.win').count();
  const winBefore = await hk.locator('.note').first().textContent();
  await hk.locator('table tbody tr').nth(2).locator('input[type=radio]').check(); await page.waitForTimeout(300);
  const hk2 = cardByTitle(page, /Hook-Studio/); const winAfter = await hk2.locator('.note').first().textContent(); const winIdx = await page.evaluate(() => S['H03'].hw.hookPick);
  check('T04', 'Hook-Studio: 5 bewertete Hooks, Sieger wechselbar und gespeichert', hookRows === 5 && winRows === 1 && winIdx === 2 && winBefore !== winAfter, `rows=${hookRows} pick=${winIdx}`);
  const scoresOk = await page.evaluate(() => DATA.filter(v => v.plan === 'main').every(v => v.hw.hooks.length === 5 && v.hw.hooks.every(h => Object.keys(h.scores).length === 7 && h.total > 0)));
  check('T04b', '195 Hooks mit je 7 Kriterien bewertet', scoresOk, '39 × 5 = 195');
  // T05 Cover
  const covN = await hk2.locator('.hwc').count(); await hk2.locator('.hwc').nth(1).locator('button', { hasText: 'Als Hook-Overlay' }).click(); await page.waitForTimeout(300);
  const hookNow = await page.evaluate(() => S['H03'].hook); const headHook = await page.locator('#vhead .hookline q').textContent();
  check('T05', 'Cover: 3 Konzepte, Übernahme als Hook-Overlay wirkt auf Kopfzeile', covN === 3 && hookNow.replace(/\*/g, '') === headHook, `hook="${hookNow}"`);
  const covAll = await page.evaluate(() => DATA.filter(v => v.plan === 'main').reduce((a, v) => a + v.hw.covers.length, 0));
  check('T05b', '117 Cover-Konzepte insgesamt', covAll === 117, covAll);
  // T06 Sprechtexte
  const voStats = await page.evaluate(() => DATA.filter(v => v.plan === 'main').map(v => ({ id: v.id, w: words(v.vo), digits: /\d/.test(v.vo.replace(/\[[^\]]+\]/g, '')), tags: (v.vo.match(/\[[^\]]+\]/g) || []).length, ph: /___|\{\{|TODO|Platzhalter/i.test(v.vo) })));
  const badVo = voStats.filter(x => x.digits || x.tags > 3 || x.ph || x.w < 35 || x.w > 120);
  check('T06', 'Sprechtexte: 39 vollständig, Zahlen ausgeschrieben, ≤3 Tags, keine Platzhalter, 35–120 Wörter (Länge folgt der Geschichte)', badVo.length === 0, badVo.map(x => x.id).join(',') || 'alle ok');
  const copyBtn = cardByTitle(page, /Sprechtext/).locator('button', { hasText: 'Sprechtext kopieren' }); check('T06b', 'Sprechtext-Kopierknopf vorhanden', await copyBtn.count() === 1);
  // T07 CapCut-Plan
  const cc = cardByTitle(page, /CapCut-Studio/); const ccRows = await cc.locator('table.hwt tbody tr').count(); const ccCols = await cc.locator('table.hwt thead th').count();
  const tcs = await cc.locator('table.hwt tbody tr td:nth-child(2)').allTextContents(); const tcOk = tcs.every(t => /^\d{2}:\d{2}:\d{2}:\d{2}$/.test(t));
  const badge = await cc.locator('.type').first().textContent();
  check('T07', 'CapCut-Plan: 16 Felder je Szene, Timecodes HH:MM:SS:FF, Status vorläufig ohne Audio', ccRows >= 5 && ccCols === 18 && tcOk && /vorläufig/.test(badge), `rows=${ccRows} cols=${ccCols} badge=${badge}`);
  const planOk = await page.evaluate(() => DATA.filter(v => v.plan === 'main').every(v => v.hw.cut.scenes.length >= 5 && v.hw.cut.scenes.every(s => ['motif', 'place', 'cam', 'frame', 'move', 'light', 'stock', 'cut', 'trans', 'overlay', 'music', 'sfx', 'subhint', 'tc_in', 'tc_out'].every(k => s[k] != null && String(s[k]).length))));
  check('T07b', 'Alle 39 Schnittpläne mit vollständigen Feldern', planOk);
  // T08 Timecode-Mathematik
  const tcMath = await page.evaluate(() => { const a = tcCap(32.5) === '00:00:32:15', b = tcCap(0) === '00:00:00:00', c = tcCap(61.0333) === '00:01:01:01', d = tcCap(3599.99) === '00:59:59:30' || tcCap(3599.99) === '01:00:00:00'; const v = V['H03']; const sc = v.hw.cut.scenes; const cont = sc.every((s, i) => i === 0 || Math.abs(s.start_s - sc[i - 1].end_s) < .011); const sum = Math.abs(sc[sc.length - 1].end_s - v.hw.cut.total_sec) < .02; return { a, b, c, d, cont, sum, t: tcCap(61.0333) }; });
  check('T08', 'Timecode-Mathematik (30 fps, HH:MM:SS:FF, lückenlose Szenen, Summe = Gesamt)', tcMath.a && tcMath.b && tcMath.c && tcMath.cont && tcMath.sum, JSON.stringify(tcMath));
  // T09 Audio-Upload WAV
  const voIn = cardByTitle(page, /Voiceover – damit/).locator('input[type=file]').first(); await voIn.setInputFiles(WAV); await page.waitForTimeout(3000);
  const voState = await page.evaluate(() => ({ vo: S['H03'].vo, have: have.has('H03|vo'), real: voInfo(V['H03']).real, dur: voInfo(V['H03']).dur }));
  const cc2 = cardByTitle(page, /CapCut-Studio/); const badge2 = await cc2.locator('.type').first().textContent(); const lastRow = await cc2.locator('table.hwt tbody tr').last().locator('td').allTextContents();
  check('T09', 'Audio-Upload WAV: Datei gespeichert, reale Dauer erkannt, CapCut-Zeiten „aus Audio“', voState.have && voState.real && Math.abs(voState.dur - 20.04) < .3 && /Audio/.test(badge2), `dur=${voState.dur} badge=${badge2} letzte Szene Ende=${lastRow[2]}`);
  const au = cardByTitle(page, /Audio-Analyse/); const auTxt = (await au.textContent()).replace(/\s+/g, ' ');
  check('T09b', 'Audio-Analyse zeigt Segmente, Silbenkerne und Abweichung zur Schätzung', /Sprachsegmente\s*\d+ erkannt/.test(auTxt) && /Silbenkerne\s*\d+/.test(auTxt) && /Abweichung/.test(auTxt), auTxt.slice(0, 260));
  // T11 Untertitel-Sync
  const subs = await page.evaluate(() => { const v = V['H03']; const it = subTiming(v); const mono = it.every((x, i) => i === 0 || x.start >= it[i - 1].start - 1e-6); const vo = voInfo(v); return { n: it.length, first: it[0].start, last: it[it.length - 1].end, mono, dur: vo.dur, vs: st(v.id).voStart }; });
  check('T11', 'Untertitel aus Audio: Zeilen monoton, erste ≥ Stimmstart, letzte ≤ Audioende', subs.n > 5 && subs.mono && subs.first >= subs.vs - .01 && subs.last <= subs.vs + subs.dur + .5, JSON.stringify(subs));
  // T12 Manuelle Korrektur
  const sc = cardByTitle(page, /^\s*\d*\s*Untertitel\s*$/); await sc.locator('details.hwsub summary').click(); const inp = sc.locator('details.hwsub tbody tr').nth(1).locator('input').first(); const bef = +(await inp.inputValue()); await inp.fill((bef + .5).toFixed(2)); await inp.dispatchEvent('change'); await page.waitForTimeout(400);
  const man = await page.evaluate(() => ({ src: S['H03'].subSrc, n: (S['H03'].subTimes || []).length, t2: subTiming(V['H03'])[1].start }));
  check('T12', 'Manuelle Zeitkorrektur je Zeile wird übernommen und gespeichert', man.src === 'manual' && man.n > 0 && Math.abs(man.t2 - (bef + .5)) < .02, JSON.stringify(man));
  await cardByTitle(page, /^\s*\d*\s*Untertitel\s*$/).locator('button', { hasText: 'Zurück auf automatisch' }).click(); await page.waitForTimeout(300);
  check('T12b', 'Zurück auf automatische Zeiten', await page.evaluate(() => S['H03'].subTimes == null));
  // T13 Speicherung (Reload)
  await page.evaluate(() => { S['H03'].hw.notes = 'Testnotiz 123'; touch('H03'); }); await page.waitForTimeout(800);
  await page.reload(); await page.waitForSelector('#list .item'); await page.waitForTimeout(800);
  const persisted = await page.evaluate(() => ({ cur: CUR, vo: S['H03'] && S['H03'].vo && S['H03'].vo.name, notes: S['H03'] && S['H03'].hw && S['H03'].hw.notes, pick: S['H03'] && S['H03'].hw && S['H03'].hw.hookPick, have: have.has('H03|vo') }));
  check('T13', 'Speicherung: Audio, Notizen und Hook-Wahl überleben das Neuladen (localStorage + IndexedDB)', persisted.vo === 'vo_test.wav' && persisted.notes === 'Testnotiz 123' && persisted.pick === 2 && persisted.have, JSON.stringify(persisted));
  // T10 MP3
  await page.click('#list .item[data-id="H04"]'); await page.waitForTimeout(500);
  await cardByTitle(page, /Voiceover – damit/).locator('input[type=file]').first().setInputFiles(MP3); await page.waitForTimeout(3000);
  const mp3 = await page.evaluate(() => ({ real: voInfo(V['H04']).real, dur: voInfo(V['H04']).dur }));
  check('T10', 'Audio-Upload MP3: dekodiert, Dauer erkannt', mp3.real && Math.abs(mp3.dur - 20.04) < .5, JSON.stringify(mp3));
  // T14 Exporte
  const dl1 = await Promise.all([page.waitForEvent('download', { timeout: 10000 }).catch(() => null), cardByTitle(page, /CapCut-Studio/).locator('button', { hasText: /^CSV$/ }).click()]).then(a => a[0]);
  check('T14', 'Export CapCut-Schnittplan CSV', !!dl1, dl1 ? dl1.suggestedFilename() : 'kein Download-Ereignis');
  const dl2 = await Promise.all([page.waitForEvent('download', { timeout: 30000 }).catch(() => null), cardByTitle(page, /CapCut-Studio/).locator('button', { hasText: 'Produktionspaket' }).click()]).then(a => a[0]);
  let zipOk = false; if (dl2) { const p = await dl2.path(); zipOk = p && fs.statSync(p).size > 2000; }
  check('T14b', 'Export Produktionspaket ZIP (Schnittplan, Sprechtext, SRT, Hooks, Cover, Stock, Fakten, Captions, Audio)', zipOk, dl2 ? dl2.suggestedFilename() : 'kein Download');
  { const d = cardByTitle(page, /^\s*\d*\s*Untertitel\s*$/).locator('details.hwsub'); if (!(await d.evaluate(e => e.open))) await d.locator('summary').click(); }
  const dl3 = await Promise.all([page.waitForEvent('download', { timeout: 10000 }).catch(() => null), cardByTitle(page, /^\s*\d*\s*Untertitel\s*$/).locator('button', { hasText: 'SRT exportieren' }).click()]).then(a => a[0]);
  let srtOk = false; if (dl3) { const txt = fs.readFileSync(await dl3.path(), 'utf8'); srtOk = /^1\s*\n\d\d:\d\d:\d\d,\d{3} --> /.test(txt); }
  check('T14c', 'Export SRT mit Zeitstempeln', srtOk, dl3 ? dl3.suggestedFilename() : 'kein Download');
  const dl4 = await Promise.all([page.waitForEvent('download', { timeout: 60000 }).catch(() => null), cardByTitle(page, /Export/).locator('button', { hasText: 'Alle 39' }).click()]).then(a => a[0]);
  let allOk = false; if (dl4) { allOk = fs.statSync(await dl4.path()).size > 50000; }
  check('T14d', 'Export Gesamtpaket aller 39 (ZIP)', allOk, dl4 ? dl4.suggestedFilename() : 'kein Download');
  // T15 Fehlerbehandlung
  const q = cardByTitle(page, /Qualitäts-Studio/); await q.locator('select').last().selectOption('Freigegeben'); await page.waitForTimeout(300);
  const gate = await page.evaluate(() => ({ appr: S['H04'].hw && S['H04'].hw.approval, toast: document.getElementById('toast').textContent }));
  check('T15', 'Freigabe ohne Fakten-/Material-/Hook-Check wird blockiert (mit Hinweis)', gate.appr !== 'Freigegeben' && /Freigabe erst/.test(gate.toast), gate.toast);
  const badJson = path.join(require('os').tmpdir(), 'hw_bad.json'); fs.writeFileSync(badJson, '{"foo": 1}');
  await cardByTitle(page, /Export/).locator('input[data-hw="import-main"]').setInputFiles(badJson); await page.waitForTimeout(400);
  check('T15b', 'Ungültige Import-Datei wird abgewiesen', /Kein Hauptplan-Format|nicht lesbar/.test(await page.locator('#toast').textContent()), await page.locator('#toast').textContent());
  // T16 Import Hauptplan-JSON (geänderter Titel) + Reset
  const src = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'reels_hauptplan_v3.json'), 'utf8')); src.reels[3].title = 'TEST-IMPORT Matterhorn'; const impPath = path.join(require('os').tmpdir(), 'hw_import.json'); fs.writeFileSync(impPath, JSON.stringify(src));
  await cardByTitle(page, /Export/).locator('input[data-hw="import-main"]').setInputFiles(impPath); await page.waitForTimeout(1200);
  const impTitle = await page.evaluate(() => V['H04'].title); const voKept = await page.evaluate(() => S['H04'].vo && S['H04'].vo.name);
  check('T16', 'Hauptplan-JSON-Import ersetzt Inhalte, behält Studio-Zustand (Audio) je Reel-ID', impTitle === 'TEST-IMPORT Matterhorn' && voKept === 'vo_test.mp3', `title=${impTitle} vo=${voKept}`);
  await page.reload(); await page.waitForSelector('#list .item'); await page.waitForTimeout(800);
  const impPersist = await page.evaluate(() => V['H04'].title);
  await cardByTitle(page, /Export/).locator('button', { hasText: 'Importierten Hauptplan verwerfen' }).click(); await page.waitForTimeout(600);
  check('T16b', 'Importierter Hauptplan überlebt Neuladen und lässt sich auf die eingebettete Fassung zurücksetzen', impPersist === 'TEST-IMPORT Matterhorn' && (await page.evaluate(() => V['H04'].title)) !== 'TEST-IMPORT Matterhorn', impPersist);
  // T20 Themenwelt-Filter (v39)
  await page.click('#list .chip[data-plan="main"]'); await page.waitForTimeout(200);
  const twChips = await page.locator('#list .chip[data-tw]').count(); await page.click('#list .chip[data-tw="Hotel-Legenden"]'); await page.waitForTimeout(200); const twN = await page.locator('#list .item').count();
  const twExp = await page.evaluate(() => DATA.filter(v => v.plan === 'main' && v.hw.themenwelt === 'Hotel-Legenden').length);
  await page.click('#list .chip[data-tw="all"]'); await page.waitForTimeout(200);
  check('T20', 'Themenwelt-Filter (4 Themenwelten) filtert die Liste', twChips === 5 && twN === twExp && twN > 0, `chips=${twChips} Hotel-Legenden=${twN}`);
  // T21 Schlüsselaufnahmen mit Materialstatus
  await page.click('#list .item[data-id="H03"]'); await page.waitForTimeout(600);
  const ksTbl = cardByTitle(page, /Content-Studio/).locator('table').first(); const ksRows = await ksTbl.locator('tbody tr').count(); const ksBadges = await ksTbl.locator('.hwks').allTextContents();
  const ksAll = await page.evaluate(() => { const ok = ['gefunden', 'verfügbar, ungeprüft', 'nicht gefunden']; const all = DATA.filter(v => v.plan === 'main').flatMap(v => v.hw.key_shots || []); return { n: all.length, valid: all.every(k => ok.includes(k.status) && k.motif && k.role), roles: all.filter(k => k.role === 'Scroll-Stop').length, found: all.filter(k => k.status === 'gefunden').length, missing: all.filter(k => k.status === 'nicht gefunden').length, missNote: all.filter(k => k.status === 'nicht gefunden').every(k => k.note) }; });
  check('T21', 'Schlüsselaufnahmen: 3 je Reel (117) mit ehrlichem Status, Tabelle in Content-Studio', ksRows === 3 && ksBadges.length === 3 && ksAll.n === 117 && ksAll.valid && ksAll.roles === 39 && ksAll.missNote, JSON.stringify(ksAll));
  await ksTbl.locator('tbody tr').first().locator('select').selectOption('geprüft & lizenziert'); await page.waitForTimeout(300);
  check('T21b', 'Materialstatus einer Schlüsselaufnahme wird gespeichert', (await page.evaluate(() => S['H03'].hw.ksChk && S['H03'].hw.ksChk[0])) === 'geprüft & lizenziert');
  // T22 Hooks mit 4 Komponenten
  const hk3 = cardByTitle(page, /Hook-Studio/); const hkHead = (await hk3.locator('table thead th').allTextContents()).join('|');
  const hk4 = await page.evaluate(() => { const hs = DATA.filter(v => v.plan === 'main').flatMap(v => v.hw.hooks); const types = ['Visueller Schock', 'Neugierlücke', 'Überraschende Behauptung', 'Emotionaler Konflikt', 'Erwartung gegen Realität']; return { n: hs.length, comp: hs.every(h => h.spoken && h.first_frame && h.overlay && h.question), types: DATA.filter(v => v.plan === 'main').every(v => v.hw.hooks.map(h => h.typ).join('|') === types.join('|')) }; });
  await hk3.locator('table tbody tr').first().locator('button', { hasText: 'Overlay' }).click(); await page.waitForTimeout(300);
  const ovNow = await page.evaluate(() => S['H03'].hook); const ovExp = await page.evaluate(() => V['H03'].hw.hooks[0].overlay);
  check('T22', 'Hooks: 195 mit Bild + Satz + Overlay + Frage, 5 feste Typen, Overlay ins Video übernehmbar', /Text-Overlay/.test(hkHead) && /Offene Frage/.test(hkHead) && hk4.n === 195 && hk4.comp && hk4.types && ovNow === ovExp, JSON.stringify(hk4));
  // T23 Strukturen, Längenvielfalt, Serienname
  const div = await page.evaluate(() => { const m = DATA.filter(v => v.plan === 'main').sort((a, b) => a.hw.nr - b.hw.nr); const st = m.map(v => v.hw.structure); const L = m.map(v => v.hw.cut.total_sec); const mean = L.reduce((a, b) => a + b, 0) / L.length; const sd = Math.sqrt(L.reduce((a, b) => a + (b - mean) ** 2, 0) / L.length); return { structures: [...new Set(st)].sort().join(''), consecutive: st.some((x, i) => i && x === st[i - 1]), min: Math.min(...L), max: Math.max(...L), sd: +sd.toFixed(2), rw: m.find(v => v.hw.series === 'RW').hw.series_name, tw: new Set(m.map(v => v.hw.themenwelt)).size }; });
  check('T23', 'Plan v3: Strukturen A–E, nie zweimal hintereinander gleich, Längen 22–42 s variabel, 4 Themenwelten, Freitag „Reisewissen“', div.structures === 'ABCDE' && !div.consecutive && div.sd >= 3.5 && div.min >= 16 && div.max <= 48 && div.tw === 4 && div.rw === 'Reisewissen', JSON.stringify(div));
  // T24 Studio-Zustand (Schema v39)
  const dl5 = await Promise.all([page.waitForEvent('download', { timeout: 10000 }).catch(() => null), cardByTitle(page, /Export/).locator('button', { hasText: 'Studio-Zustand sichern' }).click()]).then(a => a[0]);
  let stOk = false; if (dl5) { const jj = JSON.parse(fs.readFileSync(await dl5.path(), 'utf8')); stOk = jj.meta && jj.meta.schema === 'reelstudio_state_v39'; }
  check('T24', 'Studio-Zustand als JSON (Schema v39) exportierbar', stOk, dl5 ? dl5.suggestedFilename() : 'kein Download');
  // T17 Specials-Regression
  await page.click('#list .chip[data-plan="special"]'); await page.waitForTimeout(200); const firstSp = await page.locator('#list .item').first().getAttribute('data-id'); await page.locator('#list .item').first().click(); await page.waitForTimeout(600);
  const spCards = await page.locator('#panels section.card').count(); const spHw = await page.locator('#panels section.card h2', { hasText: 'Hook-Studio' }).count();
  check('T17', 'Specials (v37-Daten) rendern unverändert, ohne Hauptplan-Karten', spCards >= 6 && spHw === 0 && errors.length === 0, `special=${firstSp} cards=${spCards}`);
  // T18 Mobile
  await page.setViewportSize({ width: 390, height: 844 }); await page.waitForTimeout(500);
  const mob = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth, pick: document.querySelectorAll('#mpick option').length }));
  check('T18', 'Mobile Ansicht (390 px): kein horizontales Scrollen, Reel-Auswahl mit allen Reels', mob.sw <= mob.iw + 1 && mob.pick === 90, JSON.stringify(mob));
  await page.setViewportSize({ width: 1440, height: 1000 });
  check('T19', 'Keine JavaScript-Fehler während der gesamten Testfahrt', errors.length === 0, errors.join(' | ') || 'keine');
  const out = { stand: new Date().toISOString(), html: HTML, passed: R.filter(x => x.ok).length, failed: R.filter(x => !x.ok).length, seconds: Math.round((Date.now() - t0) / 1000), results: R };
  fs.writeFileSync(path.join(__dirname, 'testergebnis.json'), JSON.stringify(out, null, 1)); console.log(`\n${out.passed} bestanden, ${out.failed} fehlgeschlagen (${out.seconds} s)`);
  await browser.close(); process.exit(out.failed ? 1 : 0);
})().catch(e => { console.error('TESTLAUF ABGEBROCHEN', e); fs.writeFileSync(path.join(__dirname, 'testergebnis.json'), JSON.stringify({ aborted: String(e), results: R }, null, 1)); process.exit(2); });
