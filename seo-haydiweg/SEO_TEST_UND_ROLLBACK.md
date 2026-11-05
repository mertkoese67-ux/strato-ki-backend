# SEO-Snippet: Installation, Testplan & Rollback

> **Nichts davon ist auf der Live-Website aktiviert.** Der Snippet startet im Modus `'preview'` und ist dann für Besucher und Google unsichtbar.

---

## 0. Warum ein Snippet und nicht (nur) Rank Math direkt?

| Weg | Vorteil | Nachteil |
|---|---|---|
| **A. Rank Math nativ** (Titel/Description im Rank-Math-Feld jeder Seite eintragen, oder per Rank Math PRO → Status & Tools → Import/Export → **CSV-Import** der Felder `seo_title`/`seo_description`) | Standardweg, keine Zusatzlogik, Werte stehen dort, wo jeder sie erwartet | 56 Seiten einzeln bearbeiten oder CSV-Import ohne Vorschau; kein gesammeltes Ein/Aus; Rückgängig nur über Backup/Revisionen |
| **B. Dieser Snippet** (offizielle Rank-Math-Filter) | alle Änderungen an **einer** Stelle, **Vorschau-Modus** nur für Admins, **ein Schalter** für sofortigen Rollback, `{saison}` aktualisiert sich jedes Jahr selbst, ID+Pfad-Absicherung | eine zusätzliche Ebene „über“ Rank Math: Wer später im Rank-Math-Feld etwas ändert, sieht es nicht, solange der Snippet für diese Seite einen Wert setzt |

**Empfehlung:** Weg B zum sicheren Testen und Ausrollen, weil er eine echte Vorschau und einen Ein-Klick-Rollback bietet. Nach 8–12 Wochen, wenn die Titel sich bewährt haben, können sie optional dauerhaft in Rank Math übernommen werden (CSV-Import) und der Snippet wird deaktiviert. Beide Wege sind sicher, weil Rank Math in beiden Fällen der einzige Tag-Erzeuger bleibt.

**Was der Snippet technisch tut (im Rank-Math-Quellcode geprüft, Version 1.0.281):**
- `rank_math/frontend/title` → wird in `includes/frontend/paper/class-paper.php` (`get_title()`) aufgerufen; Rank Math escaped den Rückgabewert danach selbst.
- `rank_math/frontend/description` → `get_description()` in derselben Datei.
- og:title/twitter:title nutzen standardmäßig `Paper::get()->get_title()` und übernehmen den neuen Titel automatisch. **Eigene Social-Titel bleiben erhalten** (im Test nachgewiesen).

---

## 1. Installation (Schritt für Schritt)

**Vorher:**
1. **Backup** bei STRATO oder mit UpdraftPlus (Datenbank + Dateien).
2. In Rank Math → Status & Tools → Import/Export → **Einstellungen exportieren** (Sicherung der Rank-Math-Konfiguration).
3. Prüfen, welches Snippet-Plugin installiert ist (Code Snippets oder WPCode). Falls keines vorhanden ist: **Code Snippets** installieren.

**Einfügen:**
4. Snippets → **Neu hinzufügen** → Typ **PHP**. Titel: `haydi-weg SEO-Titel & Descriptions (Rank Math)`.
5. Inhalt von `HAYDIWEG_FINAL_SEO_SNIPPET.php` **ab der zweiten Zeile** einfügen (die erste Zeile `<?php` weglassen – das Plugin ergänzt sie selbst).
6. Ausführungsort: **„Nur im Frontend ausführen“** (Code Snippets: *Only run on site front-end*; WPCode: *Frontend only*).
   *Hinweis:* Der Backend-Hinweis „Vorschau-Modus“ erscheint dann nicht – das ist in Ordnung. Wer ihn sehen möchte, wählt „Überall ausführen“; der Snippet tut im Backend sonst nichts.
7. **Speichern und aktivieren.** Der Modus steht auf `'preview'`.

**Vorschau prüfen** (Abschnitt 2), dann **live schalten:**
8. Im Snippet `'mode' => 'preview'` in `'mode' => 'live'` ändern → speichern.
9. **WP Rocket → Cache leeren** (sonst sehen Besucher noch die alten Titel aus dem Cache).
10. Optional: in der Google Search Console die 10 wichtigsten URLs mit dem URL-Prüftool „Indexierung beantragen“.

---

## 2. Testplan

### 2.1 Vorschau-Test (Modus `preview`)
Als Administrator eingeloggt jede URL mit `?hw_seo_preview=1` öffnen, dann **Rechtsklick → Seitenquelltext anzeigen** (nicht den Elementor-Editor nutzen) und mit `Strg+F` prüfen:

| # | URL (mit `?hw_seo_preview=1`) | Erwarteter `<title>` | Description |
|---|---|---|---|
| 1 | `https://haydiweg.de/` | Urlaub buchen mit persönlicher Beratung \| haydi-weg | neu |
| 2 | `/urlaubsziele/tuerkei-urlaub-buchen/` | Türkei Urlaub 2027: Regionen, Hotels & Preise \| haydi-weg | neu |
| 3 | `/urlaubsziele/aegypten-urlaub-buchen/` | Ägypten Urlaub 2027: Hurghada & All Inclusive \| haydi-weg | neu |
| 4 | `/urlaubsziele/spanien-urlaub-buchen/` | Spanien Urlaub 2027: Mallorca & Kanaren \| haydi-weg | neu |
| 5 | `/reise-blog/checkliste-urlaub/` | Checkliste Urlaub: Packliste & To-dos vor Abreise \| haydi-weg | **unverändert** (Rank Math) |
| 6 | `/reise-blog/sehenswuerdigkeiten-tuerkei/` | Sehenswürdigkeiten Türkei: Kappadokien bis Side \| haydi-weg | neu |
| 7 | `/kontakt/` | Kontakt: WhatsApp, Termin & Reisebüro Minden \| haydi-weg | neu |
| 8 | `/cashback/` | Urlaub mit Cashback: 30 bis 1.000 € zurück \| haydi-weg | neu |
| 9 | `/buchen/` | Reise online buchen: Veranstalter vergleichen \| haydi-weg | neu |
| 10 | `/reisebuero-minden-urlaub-buchen/` | Reisebüro Minden: persönliche Beratung seit 2014 \| haydi-weg | neu |
| 11 | `/hotel/mardan-palace/` | **unverändert:** Mardan Palace Lara: Hotelvideo & Erfahrungen \| haydi-weg | unverändert |
| 12 | `/hotel/hotel-acapulco-lloret/` | Hotel Acapulco Lloret de Mar: Angebote & Beratung \| haydi-weg | neu |
| 13 | `/reise-blog/beste-reiseziele-2024/` | **unverändert** (Eintrag vorbereitet, aber auskommentiert) | unverändert |
| 14 | `/reise-blog/page/2/` | **unverändert** (Paginierung wird übersprungen) | – |

**Bei jeder URL zusätzlich prüfen:**
- [ ] genau **1×** `<title>` und genau **1×** `<meta name="description"` (Suche nach `<title` bzw. `name="description"` → je 1 Treffer)
- [ ] `<link rel="canonical"` **unverändert** (gleicher Wert wie ohne `?hw_seo_preview=1`)
- [ ] `<meta name="robots"` **unverändert**
- [ ] `og:title` = neuer Titel (außer die Seite hat im Rank-Math-Reiter „Social“ einen eigenen Titel – dann bleibt dieser)
- [ ] Kommentar `<!-- hw-seo preview: Eintrag aktiv fuer /… -->` vorhanden (bzw. „kein Eintrag, Rank-Math-Wert“ bei Nr. 5, 11, 13, 14)
- [ ] Seite sieht normal aus, Elementor-Layout unverändert

**Gegenprobe:**
- [ ] Gleiche URL **ohne** `?hw_seo_preview=1` → alter Titel (Besuchersicht)
- [ ] Gleiche URL **mit** Parameter in einem **privaten Fenster** (nicht eingeloggt) → alter Titel
- [ ] Elementor-Editor einer Seite öffnen und speichern → funktioniert normal
- [ ] `/buchen/`: Reisesuche durchführen, ein Angebot öffnen, bis zur Buchungsmaske klicken → IBE funktioniert normal
- [ ] Backend (Seiten, Rank Math, Elementor) lädt ohne Fehlermeldung

### 2.2 Live-Test (nach Umschalten auf `live` + Cache leeren)
- [ ] Die URLs 1–14 in einem **privaten Fenster** prüfen → neue Titel für Besucher sichtbar
- [ ] Kein `hw-seo preview`-Kommentar mehr im Quelltext
- [ ] [Rich-Results-Test](https://search.google.com/test/rich-results) für Startseite und eine Hotelseite → keine neuen Fehler
- [ ] Search Console → URL-Prüfung → „Live-URL testen“ für Startseite → gerendertes HTML zeigt neuen Titel
- [ ] Vorschau in einem SERP-Simulator (z. B. Rank Math Snippet-Vorschau, oder ein beliebiges Online-SERP-Vorschau-Tool) für die 10 wichtigsten Seiten → keine Kürzung mitten im Wort
- [ ] Nach 24 h: PHP-Fehlerprotokoll bei STRATO (bzw. `wp-content/debug.log`, falls aktiv) → keine Einträge mit `hw_seo_`

### 2.3 Prüfung auf ungewolltes Überschreiben
- Der Snippet ändert **nur** Seiten, deren **ID und Pfad** in der Konfiguration stehen (56 Seiten + 1 Kategorie). Alle anderen Seiten behalten den Rank-Math-Titel.
- Einzige globale Änderung (abschaltbar mit `'fix_legacy_suffix' => false`): Ein Titel, der auf **„ - haydi-weg ☀ Urlaub leicht gemacht“** endet, wird zu **„ | haydi-weg“**. Betroffen sind laut Crawl nur Seiten ohne eigenen Rank-Math-Titel (z. B. Suche, Archive, neue Seiten).
- Wird eine Seite verschoben (andere URL), greift ihr Eintrag nicht mehr (Pfadprüfung) → Rank Math übernimmt. Dann den `'path'` im Snippet anpassen.

---

## 3. Bereits durchgeführter Test (Testumgebung)

**Umgebung:** WordPress 7.1.4, Rank Math 1.0.281 (Free-Kern), PHP 8.3, SQLite, Seiten mit den **echten Live-IDs** (982, 2012, 5963, 7365, 1379, 2811, 5644, Kategorie 35) und den echten Pfaden nachgebaut. Rank-Math-Standardvorlage erzeugte wie live „Titel - haydi-weg ☀ Urlaub leicht gemacht“. Der Snippet lief als Must-Use-Plugin (entspricht „Nur Frontend“ in Code Snippets).

| Test | Ergebnis |
|---|---|
| PHP-Syntax (`php -l`) | ✔ keine Fehler |
| Besucher (nicht eingeloggt), Modus `preview`, mit `?hw_seo_preview=1` | ✔ **keine** Änderung an irgendeiner Seite |
| Admin ohne Parameter | ✔ keine Änderung |
| Admin mit Parameter | ✔ neue Titel/Descriptions auf allen konfigurierten Seiten, `{saison}` → **2027** |
| Anzahl `<title>` / Description pro Seite | ✔ immer genau 1 / höchstens 1 |
| Canonical / robots | ✔ in allen Modi identisch |
| Eigener Rank-Math-Social-Titel (Kontakt: „EIGENER OG TITEL“) | ✔ bleibt erhalten |
| Bestehende Rank-Math-Description wird durch neue ersetzt, nur wo konfiguriert | ✔ |
| **Falsche ID/Pfad-Kombination** (ID 2002 unter anderer URL) | ✔ Eintrag ignoriert, Rank-Math-Wert bleibt |
| Neue Seite ohne Eintrag | ✔ Rank-Math-Wert, nur Suffix „☀ Urlaub leicht gemacht“ → „\| haydi-weg“ |
| Paginierung `/reise-blog/page/2/`, Suche `/?s=` | ✔ kein Override, noindex der Suche unverändert |
| Kategorie (Term-ID 35) | ✔ Override greift |
| Modus `live` (Besucher) | ✔ neue Werte, kein Vorschau-Kommentar |
| Modus `off` | ✔ Ausgabe **byte-identisch** zum Zustand ohne Snippet |
| Rank Math deaktiviert | ✔ Website läuft (HTTP 200), Snippet wirkungslos, Backend-Hinweis „Rank Math ist nicht aktiv“ |
| Backend, Feed, REST-API | ✔ HTTP 200, unbeeinflusst |
| PHP-Notices/Warnings (`WP_DEBUG`) | ✔ keine vom Snippet |

**Nicht in der Testumgebung prüfbar** (daher Teil der Prüfliste in 2.1/2.2): Elementor-Editor, WP Rocket, die Schmetterling-IBE, Rank Math **PRO**-Zusatzfunktionen, das konkrete Snippet-Plugin auf dem Live-System.

---

## 4. Rollback-Anleitung

**Sofort (unter 1 Minute), Variante 1 – Snippet ausschalten:**
1. WordPress-Backend → **Snippets** → beim Snippet „haydi-weg SEO-Titel …“ auf **Deaktivieren** klicken.
2. **WP Rocket → Cache leeren.**
→ Rank Math gibt wieder exakt die alten Titel/Descriptions aus (im Test byte-identisch).

**Variante 2 – Modus umstellen (Snippet bleibt für später erhalten):**
1. Im Snippet `'mode' => 'live'` → `'mode' => 'off'` (oder zurück auf `'preview'`) → speichern.
2. WP Rocket → Cache leeren.

**Variante 3 – nur eine Seite zurücknehmen:**
- Im Snippet beim betreffenden Eintrag `'title' => ''` und/oder `'description' => ''` setzen (oder den ganzen Eintrag löschen) → speichern → Cache leeren.

**Notfall – Backend nicht erreichbar** (sehr unwahrscheinlich, da der Snippet im Test fehlerfrei lief):
- Code Snippets: in `wp-config.php` die Zeile `define( 'CODE_SNIPPETS_SAFE_MODE', true );` ergänzen (per STRATO-Dateimanager/FTP) → Backend öffnen → Snippet deaktivieren → Zeile wieder entfernen.
- WPCode: Ordner `wp-content/plugins/insert-headers-and-footers` per FTP kurz umbenennen.
- Danach WP Rocket → Cache leeren.

**Nach einem Rollback in Google:** Google übernimmt die alten Titel beim nächsten Crawl (Tage bis wenige Wochen). Es entsteht kein Indexierungsschaden, weil Canonical, robots und URLs nie verändert wurden.

---

## 5. Pflege

| Situation | Was tun |
|---|---|
| Neue Seite erstellt | nichts – Rank Math-Wert gilt. Optional Eintrag mit ID + Pfad ergänzen. |
| Seite umbenannt/verschoben | `'path'` im Snippet anpassen (sonst greift der Eintrag nicht mehr – sicherer Ausfall) |
| Seite gelöscht | Eintrag kann bleiben (wird ignoriert) oder gelöscht werden |
| Jahreswechsel | nichts – `{saison}` springt am **1. September** automatisch aufs Folgejahr. Inhalte (H1, Intro) mit Jahreszahl müssen aber im Elementor-Text von Hand aktualisiert werden. |
| Titel in Rank Math ändern, obwohl Snippet-Eintrag existiert | Snippet-Eintrag hat Vorrang → im Snippet ändern **oder** dort `''` setzen |
| „Beste Reiseziele“ aktualisiert | im Snippet die auskommentierte Zeile für ID 2811 einkommentieren (vorher ggf. `'path'` auf neue URL setzen) |
