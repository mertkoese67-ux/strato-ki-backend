// Baut Angebots-Deeplinks auf https://haydiweg.de/buchen/ fuer die eingebettete
// Amadeus Leisure IBE (Schmetterling, Agentur taid=46850).
// Reine Funktion, keine Netzwerkzugriffe. Parameter am 04.11.2026 lesend verifiziert
// (siehe docs/IBE-Analyse-2026-11.md).
//
// Wichtig: Kinder muessen IMMER zusaetzlich als `child` (Alter, kommagetrennt)
// uebergeben werden. Nur `talloc` reicht nicht - die IBE ignoriert dann das Kind.

const BASIS = "https://haydiweg.de/buchen/";

function isoDatum(d) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) throw new Error(`Datum nicht im Format JJJJ-MM-TT: ${d}`);
  return d;
}

/**
 * @param {object} a
 * @param {string} a.hotelId       IFF-Hotelcode der IBE (URL-Parameter aid), z.B. "156021"
 * @param {string} a.von           fruehester Hinreisetag, JJJJ-MM-TT (ddate)
 * @param {string} a.bis           spaetester Rueckreisetag, JJJJ-MM-TT (rdate)
 * @param {number|string} [a.naechte]  Anzahl Uebernachtungen (dur), z.B. 7 = "8 Tage, 7 Uebernachtungen";
 *                                     Spanne als "6,9"
 * @param {string[]} [a.abflug]    IATA-Codes (depap), z.B. ["PAD","HAJ"]
 * @param {number} a.erwachsene    Anzahl Erwachsene (adult)
 * @param {number[]} [a.kinder]    Kinderalter am Rueckreisetag (child)
 * @param {string} [a.veranstalter] Veranstaltercode (brand), z.B. "ANEX" - optional
 * @param {object} [a.utm]         utm_* fuer die eigene Auswertung auf haydiweg.de
 *                                 (werden vom Loader NICHT an die IBE weitergegeben)
 */
function baueAngebotsLink(a) {
  if (!a || !/^\d+$/.test(String(a.hotelId || ""))) throw new Error("hotelId (aid) fehlt oder ist nicht numerisch");
  const erw = Number(a.erwachsene);
  if (!(erw >= 1 && erw <= 6)) throw new Error("erwachsene muss 1-6 sein");
  const kinder = (a.kinder || []).map(Number);
  if (kinder.some((k) => !(k >= 0 && k <= 17))) throw new Error("Kinderalter muss 0-17 sein");

  const p = new URLSearchParams();
  p.set("aid", String(a.hotelId));
  p.set("ddate", isoDatum(a.von));
  p.set("rdate", isoDatum(a.bis));
  if (a.naechte !== undefined && a.naechte !== "") p.set("dur", String(a.naechte));
  if (a.abflug && a.abflug.length) p.set("depap", a.abflug.map((c) => c.toUpperCase()).join(","));
  p.set("adult", String(erw));
  if (kinder.length) p.set("child", kinder.join(","));
  p.set("talloc", `${erw}-${kinder.join(",")}`);
  if (a.veranstalter) p.set("brand", a.veranstalter);
  Object.entries(a.utm || {}).forEach(([k, v]) => p.set(k, v));
  return `${BASIS}?${p.toString()}`;
}

module.exports = { baueAngebotsLink };

if (require.main === module) {
  // Beispiel = verifizierter Testfall 1
  console.log(
    baueAngebotsLink({
      hotelId: "156021",
      von: "2027-06-01",
      bis: "2027-06-30",
      naechte: 7,
      abflug: ["PAD"],
      erwachsene: 2,
      kinder: [8],
      utm: { utm_source: "flyer", utm_medium: "print", utm_campaign: "flyer-2026-11-04-01" },
    })
  );
}
