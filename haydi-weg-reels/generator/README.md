# Generator des Hauptplans v3 (reproduzierbar)

- `kalender.py` – verbindlicher 13-Wochen-Kalender mit Kuratierungsentscheidung, Struktur A–E, Themenwelt, Ziel-Länge je Reel.
- `build.py` – Kern: Timecodes (30 fps, vorläufig), Lint (Floskeln, Ziffern, Längen, Hook-Komponenten, Sieger-Konsistenz, Preisangaben), globale Prüfungen (Strukturwechsel, Einstiegsvielfalt, Längenstreuung), Ausgabe aller Lieferdateien (`python3 build.py --write`).
- `r01.py` … `r08.py` – die 39 Reel-Pakete (Sprechtext je Szene, 5 Hooks mit 4 Komponenten, 3 Cover, 3 Schlüsselaufnahmen mit Status, Stock, Fakten, Scorecard, Protokoll, Captions, Changelog).
- `SPEC_V3.md` – Spezifikation, nach der die Pakete geschrieben wurden (Regeln, Recherchemethode, gesicherte Fakten).
- `import_files.py` – flache Import-Tabellen (CSV/JSON/XLSX); `docs_v3.py` – Dokumente 02, 08, 11–13, 15–17, README; `kritik_v3.md` – handgeschriebener Teil der kritischen Bewertung.
- `../studio/src/` – `v39_patch.js` (Studio-Erweiterung, auf jede v37/v38-Fassung übertragbar), `hw_todata.js` (Umwandlung Hauptplan → Studio-Daten), `make_v39.py` (Build; enthält Pfade der Arbeitsumgebung, vor Nutzung anpassen).

Ausführen (Python 3, openpyxl): `cd generator && python3 build.py` (Lint) · `python3 build.py --write` (alle Dateien neu erzeugen) · danach `python3 import_files.py` und `python3 docs_v3.py`.


## Fassung v4 (Final-Audit, 10.11.2026)

- `kalender.py`, `build.py`, `r01.py`–`r08.py` sind jetzt v4 (Hook-Typen mit „Emotionaler WOW-Moment“, Audit-Gewichte 25/25/20/15/5/10, Hotel-Felder `hotel_reel`/`dach_begruendung`/`dubletten`, Produktionsbereitschaft). Spezifikationen: `SPEC_V3.md` + `SPEC_V4.md`, Arbeitsanweisung `KURATIERUNG_V4.md`.
- `audit/` – Brief, Ausschlussliste und die fünf Kandidatengruppen des DACH-Hotel-Audits (99 Kandidaten, JSON + Markdown); `audit_doc.py` erzeugt daraus `19_FINAL_AUDIT_HOTELS.md`.
- `import_files_v4.py`, `docs_v4.py` (Dokumente 02, 08, 11–13, 18, 20, 21, README), `kritik_v4.md`.
- Studio: `../studio/src/make_v40.py` (nur Daten v4 einspielen, Gewichte aus Daten), `v40_patch.js`, `hw_todata.js`. Die v3-Fassungen bleiben in `backup/` bzw. in der Git-Historie.
