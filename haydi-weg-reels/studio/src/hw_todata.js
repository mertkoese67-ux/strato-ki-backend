/* ---- v39: Hauptplan 09.11.2026–05.02.2027 (39 Reels, Fassung v3) – Umwandlung ins Studio-Datenformat ---- */
function hwFirstWords(t, n) { return String(t || '').replace(/\[[^\]]+\]/g, ' ').replace(/[„“"‚‘’…]/g, ' ').trim().split(/\s+/).filter(Boolean).slice(0, n).join(' '); }
function hwShortOverlay(o) { let t = String(o || '').replace(/^Hook-Overlay:\s*/i, '').replace(/\(.*?\)/g, '').replace(/·/g, ' / ').replace(/\s+/g, ' ').trim(); if (/^(–|-|keins?)$/i.test(t)) return ''; return t.length > 60 ? t.slice(0, 57) + '…' : t; }
function hwToData(r) {
  const [y, m, d] = String(r.date).split('-').map(Number);
  const cov = (r.covers || [])[0]; const win = (r.hooks || []).find(h => h.winner); let hook = win && win.overlay ? win.overlay : (cov ? cov.headline : r.title); const yel = cov && cov.yellow;
  if (!(win && win.overlay) && yel && hook.includes(yel) && !/\*/.test(hook)) hook = hook.replace(yel, '*' + yel + '*');
  const scs = (r.cut && r.cut.scenes) || [];
  const shots = scs.map((sc, i) => ({ desc: String(sc.motif || '').slice(0, 160) + (sc.place && sc.place !== '–' ? ' · ' + sc.place : ''), text: sc.role === 'hook' ? '' : hwShortOverlay(sc.overlay), badge: '', w: Math.max(.5, +sc.dur_s || 1), sfx: 'none', sfx0: 'none', anchor: i === 0 ? undefined : (sc.vo ? hwFirstWords(sc.sub || sc.vo, 3) : null) }));
  const hookDur = scs[0] ? Math.round(Math.max(2.5, +scs[0].dur_s || 2.5) * 100) / 100 : 3;
  return { id: r.id, plan: 'main', day: d, month: m, year: y, wd: r.weekday, time: '', kind: 'info', fmt: r.series + ' #' + r.episode + (r.structure ? ' · ' + r.structure : ''), num: r.nr, title: r.title, hook, vo: r.vo.full, subs: (r.subs.scenes || []).join('\n'), shots,
    notes: (r.approval && r.approval.pre_post_checks || []).join(' · '), mood: r.cut.music, target: r.cut.total_sec, len: r.cut.total_tc, rev: 2,
    cap: { ig: r.captions.ig, tt: r.captions.tt, tt_title: String(r.captions.yt_title || r.title).slice(0, 90), yt: r.captions.yt_title, ytd: r.captions.ig }, place: r.place, hookAuto: hookDur, over: { logo: 'br' }, hw: r };
}
HW_MAIN_RAW.reels.forEach(r => { if (!DATA.some(v => v.id === r.id)) DATA.push(hwToData(r)); });
DATA.forEach(v => { if (!v.plan) v.plan = v.custom ? 'custom' : 'special'; });
