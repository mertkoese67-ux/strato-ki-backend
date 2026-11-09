# Generator des Hauptplans v3 (reproduzierbar)

- `kalender.py` – verbindlicher 13-Wochen-Kalender mit Kuratierungsentscheidung, Struktur A–E, Themenwelt, Ziel-Länge je Reel.
- `build.py` – Kern: Timecodes (30 fps, vorläufig), Lint (Floskeln, Ziffern, Längen, Hook-Komponenten, Sieger-Konsistenz, Preisangaben), globale Prüfungen (Strukturwechsel, Einstiegsvielfalt, Längenstreuung), Ausgabe aller Lieferdateien (`python3 build.py --write`).
- `r01.py` … `r08.py` – die 39 Reel-Pakete (Sprechtext je Szene, 5 Hooks mit 4 Komponenten, 3 Cover, 3 Schlüsselaufnahmen mit Status, Stock, Fakten, Scorecard, Protokoll, Captions, Changelog).
- `SPEC_V3.md` – Spezifikation, nach der die Pakete geschrieben wurden (Regeln, Recherchemethode, gesicherte Fakten).
- `import_files.py` – flache Import-Tabellen (CSV/JSON/XLSX); `docs_v3.py` – Dokumente 02, 08, 11–13, 15–17, README; `kritik_v3.md` – handgeschriebener Teil der kritischen Bewertung.
- `../studio/src/` – `v39_patch.js` (Studio-Erweiterung, auf jede v37/v38-Fassung übertragbar), `hw_todata.js` (Umwandlung Hauptplan → Studio-Daten), `make_v39.py` (Build; enthält Pfade der Arbeitsumgebung, vor Nutzung anpassen).

Ausführen (Python 3, openpyxl): `cd generator && python3 build.py` (Lint) · `python3 build.py --write` (alle Dateien neu erzeugen) · danach `python3 import_files.py` und `python3 docs_v3.py`.
