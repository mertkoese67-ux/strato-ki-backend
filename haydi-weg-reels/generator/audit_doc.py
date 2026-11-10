# -*- coding: utf-8 -*-
"""Erzeugt 19_FINAL_AUDIT_HOTELS.md: Dubletten-Check, 99 Kandidaten (5 Gruppen), Auswahl und Reserve."""
import json, os
SP = os.path.dirname(os.path.abspath(__file__)) + "/../audit/"
OUT = "/home/user/strato-ki-backend/haydi-weg-reels/"
GR = [("tuerkei","Türkei"),("griechenland","Griechenland & Zypern"),("spanien_alpen","Spanien, Portugal & Alpen"),("aegypten_vae","Ägypten & VAE"),("malediven_fern","Malediven & Fernziele")]
chosen = {"Vilamendhoo":"H02","Bahía del Duque":"H06","Atlantis The Royal":"H07","Lara-Palastmeile":"H10","Hubertus":"H14","Emirates Palace":"H19","Angsana Velavaru":"H21","Ikos Odisia":"H22","Address Beach Resort":"H26","Domes of Elounda":"H30","Landaa Giraavaru":"H31","Hilton Marsa Alam":"H32","Rixos Premium Belek":"H33","Cap Rocat":"H37"}
def pick(h):
    for k, v in chosen.items():
        if k.lower() in h.lower(): return v
    return ""
tot = 0; st = {"gefunden":0,"verfügbar, ungeprüft":0,"nicht gefunden":0}
L = ["# Final-Audit: Dubletten-Check und DACH-Hotel-Audit (Stand 10.11.2026)", "",
     "Auftrag: ausschließlich für Urlauber aus D/A/CH relevante Hotels und Resorts mit außergewöhnlichem visuellem Potenzial; keine bereits behandelten Häuser (Regnum The Crown ausgeschlossen); jedes Hotel mit Footage-Nachweis, sonst nicht produktionsbereit. Fünf Recherche-Gruppen, 99 Kandidaten, Suchseiten von Envato Elements und Pexels am 09./10.11.2026 geöffnet (Detailseiten/Lizenzen nicht einsehbar; Envato-Vorschau nur mit Konto). Datei „haydi-weg Reel-Studio(3).html“ lag nicht vor – Basis ist das v39-Studio dieser Übergabe.", "",
     open(SP + "ausschlussliste.md", encoding="utf-8").read(), "",
     "## Ergebnis der Auswahl", "",
     "14 Hotel-/Resort-Reels neu im Plan (Spalte „Plan v4“), 25 Reels behalten. Auswahlkriterien in dieser Reihenfolge: Footage-Nachweis (gefunden > verfügbar, ungeprüft > nicht gefunden) · visuelle Faszination · echte Geschichte mit Wendung · DACH-Relevanz (Veranstalter, Direktflüge, Nachfrage) · Dubletten-Status · Länder- und Strukturwechsel im Kalender. Bewusst nicht gewählt trotz Spitzenbild: Stella Island (kein Footage), Maxx Royal Bodrum/Belek, Cullinan, Soneva Jani, Krallerhof, Bürgenstock, Conrad Rangali (nur generischer Clip) – alle als Reserve mit Status gelistet; sie werden produktionsbereit, sobald Pressematerial vorliegt.", ""]
for g, name in GR:
    d = json.load(open(SP + "kandidaten_%s.json" % g, encoding="utf-8")); tot += len(d)
    L += ["## %s (%d Kandidaten)" % (name, len(d)), "", "| Hotel | Ort | Außergewöhnlich (belegt) | DACH-Relevanz | Dubletten | Footage Hotel | Score H/V/S/D | Plan v4 | Empfehlung |", "|---|---|---|---|---|---|---|---|---|"]
    for k in sorted(d, key=lambda k: -(sum((k.get("score") or {}).values()) if isinstance(k.get("score"), dict) else 0)):
        sc = k.get("score") or {}; s0 = (k.get("footage_hotel_status") or "").strip()
        if s0 in st: st[s0] += 1
        L.append("| %s | %s | %s | %s | %s | **%s** – %s | %s/%s/%s/%s | %s | %s |" % (k.get("hotel",""), k.get("ort",""), str(k.get("besonderheit",""))[:260].replace("|","/"), str(k.get("dach",""))[:160].replace("|","/"), str(k.get("dubletten_status",""))[:90].replace("|","/"), s0, str(k.get("footage_hotel_belege",""))[:160].replace("|","/"), sc.get("hook","–"), sc.get("visual","–"), sc.get("story","–"), sc.get("dach","–"), pick(k.get("hotel","")) or "Reserve", str(k.get("empfehlung",""))[:160].replace("|","/")))
    L.append("")
L.insert(7, "| Kandidaten gesamt | Footage gefunden | verfügbar, ungeprüft | nicht gefunden |\n|---|---|---|---|\n| %d | %d | %d | %d |\n" % (tot, st["gefunden"], st["verfügbar, ungeprüft"], st["nicht gefunden"]))
L += ["## Lehre aus dem Material-Check", "", "- Für türkische und ägyptische Resorts gibt es auf Envato/Pexels praktisch kein Bewegtbild mit Hotelnamen im Titel; Dubai, Abu Dhabi, Kreta/Korfu, Malediven-Resorts und einzelne kanarische Häuser sind dagegen belegt. Deshalb trägt der v4-Plan die Türkei über Natur (Düden, Pamukkale), Legenden (Çırağan, Kappadokien) und zwei Resort-Reels mit plausiblem Material (Lara-Palastmeile, Rixos/Land of Legends), und Ägypten über Old Cataract, Mena House und ein ehrlich als „nicht produktionsbereit“ markiertes Marsa-Alam-Reel.",
      "- Produktionsweg für Hotels ohne Stock: Pressematerial über den Veranstalter/Hotelvertrieb anfragen (haydi-weg ist Reisebüro) – Nutzungsrecht schriftlich, Credit im Reel. Bis dahin bleibt das Reel im Studio auf „Material offen“.",
      "- Kein Kandidat wurde wegen Preis gewählt; Preise erscheinen nirgends."]
open(OUT + "19_FINAL_AUDIT_HOTELS.md", "w", encoding="utf-8").write("\n".join(L))
print("19_FINAL_AUDIT_HOTELS.md:", tot, "Kandidaten", st)
