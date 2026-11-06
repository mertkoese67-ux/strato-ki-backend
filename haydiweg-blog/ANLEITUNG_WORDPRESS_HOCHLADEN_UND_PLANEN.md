# Anleitung: Blogartikel in WordPress hochladen und planen

Für: haydiweg.de (WordPress + Rank Math) · Stand: 06.11.2026

## Was du bekommst

| Ordner / Datei | Wofür |
|---|---|
| `WORDPRESS_IMPORT/haydiweg-blog-entwuerfe.xml` | **Alle 36 Artikel auf einmal** als Entwurf importieren (empfohlen) |
| `WORDPRESS_IMPORT/haydiweg-blog-geplant.xml` | Dieselben 36 Artikel, **schon geplant** mit Datum und Uhrzeit. Sie erscheinen automatisch, siehe Schritt 4b |
| `WORDPRESS_IMPORT/haydiweg-blog-dubai-zurueckgestellt.xml` | 3 Dubai-Artikel, erst importieren, wenn das Auswärtige Amt den Reisehinweis für die VAE aufhebt |
| `ARTIKEL_ZUM_HOCHLADEN/NN-….html` | Inhalt jedes Artikels zum Einfügen von Hand (Weg B) |
| `ARTIKEL_ZUM_HOCHLADEN/STECKBRIEFE.md` | Pro Artikel alle Angaben: Titel, URL, Kategorie, Autor, Termin, Rank-Math-Felder, Beitragsbild, ALT-Text |
| `ARTIKEL_LINKS.md` | Alle Artikel-Links mit Termin und Autor |
| `VORSCHAU/NN-….html` | So sieht jeder Artikel in eurem Design aus (Datei im Browser öffnen) |
| `NACHVERLINKUNG.md` | Links, die du setzt, sobald der verlinkte Artikel online ist |

**Zum Design:** Ihr müsst nichts gestalten. Eure Website baut das Beitragsdesign automatisch aus dem Inhalt: Titelbild-Kopf, Brotkrumen „Startseite › Reise-Blog“, gelbe Kategorie-Pille, Datum, Lesezeit, Inhaltsverzeichnis, Tabellen, FAQ-Akkordeon, „Weitere Artikel“ und die Box „Lieber persönlich planen?“. Die Artikel liegen deshalb im selben schlichten HTML vor wie euer Beitrag „Türkei-Hotels mit Aquapark“.
**Wichtig:** Die Beiträge **nicht** mit Elementor öffnen („Mit Elementor bearbeiten“), sonst wird dieser Aufbau ersetzt.

**Zu den Links:** Die Adressen folgen eurer aktuellen Struktur `haydiweg.de/<kategorie>/<beitragsname>/`, genau wie `haydiweg.de/tuerkei/tuerkei-hotel-mit-aquapark/`. Ein Beispiel ist `haydiweg.de/tuerkei/side-oder-belek/`. Alle Links stehen in `ARTIKEL_LINKS.md`.

---

## Schritt 1: Sicherung anlegen (5 Minuten)

Im WordPress-Menü **All-in-One WP Migration → Exportieren → Datei** wählen. Alternativ das STRATO-Backup nutzen. So kannst du alles zurückholen, falls etwas schiefgeht.

## Schritt 2: Die drei Autoren anlegen (einmalig)

**Benutzer → Neu hinzufügen**, für jede Person:

| Benutzername | Vorname | Nachname | Rolle |
|---|---|---|---|
| `burak-mert-koese` | Burak Mert | Köse | Autor |
| `emre-koese` | Emre | Köse | Autor |
| `leon-sulemani` | Leon | Sulemani | Autor |

- Für jede Person ist eine eigene E-Mail-Adresse nötig (WordPress verlangt das).
- Nach dem Speichern den Benutzer öffnen und bei **„Öffentlicher Name“** den vollen Namen auswählen, z. B. „Burak Mert Köse“.
- Optional: unter „Biografische Angaben“ 1–2 Sätze eintragen, z. B. „Reiseberater bei haydi-weg in Minden, Schwerpunkt Türkei“. Das stärkt das Vertrauen bei Google.
- Hinweis: Euer aktuelles Beitragsdesign zeigt den Autornamen nicht sichtbar an. Er erscheint in den Daten für Google (Rank Math). Soll der Name sichtbar unter dem Titel stehen, muss euer Design-Snippet angepasst werden. Sag Bescheid, wenn du das möchtest.

**Wer schreibt was** (nach Themenschwerpunkt, jederzeit änderbar):
- **Burak Mert Köse:** Türkei und Buchungsthemen (13 Artikel)
- **Emre Köse:** Ägypten, Fernreisen und Dubai (9 Artikel + 3 Dubai in Reserve)
- **Leon Sulemani:** Spanien/Kanaren/Madeira, Griechenland/Zypern, Ferien und Reiseplanung (14 Artikel)

## Schritt 3: Kategorien prüfen

**Beiträge → Kategorien.** Fehlende Kategorien legst du mit genau diesem **Titelform** (Slug) an. Der Import legt sie zwar automatisch an, aber so stimmen die Links sicher:

| Name | Titelform (Slug) |
|---|---|
| Türkei | `tuerkei` (gibt es schon) |
| Ägypten | `aegypten` |
| Spanien | `spanien` |
| Griechenland | `griechenland` |
| Zypern | `zypern` |
| Portugal | `portugal` |
| Fernreisen | `fernreisen` |
| Reiseplanung | `reiseplanung` |
| Dubai | `dubai` (erst bei den Dubai-Artikeln) |

Wichtig: Bei „Ägypten“ muss die Titelform `aegypten` lauten (mit „ae“), sonst ändern sich die Links.

---

## Schritt 4a: Alle Artikel als Entwürfe importieren (empfohlen)

1. **Werkzeuge → Daten importieren → „WordPress“ → „Jetzt installieren“**. Das ist der offizielle WordPress-Importer. Danach **„Importer ausführen“**.
2. Die Datei **`haydiweg-blog-entwuerfe.xml`** auswählen und **„Datei hochladen und importieren“** klicken.
3. **Autoren zuordnen:** Für jeden der drei Einträge (burak-mert-koese, emre-koese, leon-sulemani) im Feld **„oder Beiträge einem vorhandenen Benutzer zuweisen“** die passende Person aus Schritt 2 wählen.
4. **„Dateianhänge herunterladen und importieren“ NICHT anhaken.** Die Bilder liegen schon in eurer Mediathek.
5. **Absenden**. Unter **Beiträge → Entwürfe** stehen jetzt 36 Artikel.

Der Import bringt bereits mit:
- Titel, Inhalt und Permalink
- Kategorie und Schlagwörter
- Autor
- Rank-Math-SEO-Titel, -Beschreibung und -Fokus-Keyword
- geplantes Datum
- bei 23 Artikeln das Beitragsbild aus eurer Mediathek

Den Importer kannst du danach unter Plugins wieder deaktivieren.

## Schritt 5: Jeden Artikel kurz prüfen und planen

Pro Artikel etwa 10 Minuten. Am besten jeweils 2–3 Tage vor dem Termin, mindestens aber am Vortag.

1. **Beiträge → Entwürfe →** Artikel öffnen.
2. **Beitragsbild** (rechte Seitenleiste, Tab „Beitrag“):
   - Ist schon eins gesetzt, prüfe es. Es erscheint groß im Kopf des Artikels.
   - Fehlt es, klicke auf **„Beitragsbild festlegen“** und wähle ein Bild. Den Vorschlag und den ALT-Text findest du im Steckbrief. Ist eine Mediathek-ID angegeben, findest du das Bild unter `haydiweg.de/wp-admin/upload.php?item=ID`.
   - Nur Bilder verwenden, bei denen ihr die Rechte sicher habt: eigene Fotos und Videostills.
   - Den **ALT-Text** aus dem Steckbrief beim Bild eintragen.
3. **Rank Math** (Symbol oben rechts oder Kasten unter dem Text → „Snippet bearbeiten“): Titel, Beschreibung und Fokus-Keyword sind eingetragen. Nur kontrollieren.
4. **Permalink** (Seitenleiste → „URL“): Er muss mit dem Steckbrief übereinstimmen, z. B. `side-oder-belek`.
5. **Autor** (Seitenleiste → „Autor“): Er ist bereits gesetzt. Nur kontrollieren.
6. **Vorschau** (oben rechts): Kurz durchscrollen, auch auf dem Handy-Symbol.
7. **Planen:**
   - Klicke oben rechts auf **„Veröffentlichen“**. In der Seitenleiste steht bei **„Veröffentlichen: Sofort“** bzw. dem Datum ein Link.
   - Klicke darauf und stelle **Datum und Uhrzeit** laut Steckbrief ein, z. B. 25.11.2026, 07:30. Das Datum ist schon vorbelegt, bitte nur kontrollieren.
   - Der Knopf heißt jetzt **„Planen…“**. Klicke darauf und bestätige mit **„Planen“**.
   - In der Beitragsliste steht jetzt **„Geplant“**. WordPress veröffentlicht den Artikel automatisch zum Termin.

**Klassischer Editor statt Block-Editor?** Der Ablauf ist derselbe. Datum und Uhrzeit stellst du im Kasten „Veröffentlichen“ bei „Sofort veröffentlichen → Bearbeiten“ ein, der Knopf heißt dann „Planen“.

**Zeitzone prüfen (einmalig):** **Einstellungen → Allgemein → Zeitzone = „Berlin“**, sonst erscheinen die Artikel zur falschen Uhrzeit.

## Schritt 4b (Alternative): Alles auf einmal planen

`haydiweg-blog-geplant.xml` importiert alle 36 Artikel **bereits als „Geplant“**. Sie gehen dann ohne weiteren Klick zum Termin online. Der Ablauf ist derselbe wie in Schritt 4a, nur mit dieser Datei.

**Nur nutzen, wenn ihr alle Artikel vorher durchgeht**, vor allem Beitragsbild und Bildrechte. Sonst erscheint ein Artikel womöglich ohne Titelbild. Bitte **nicht beide Dateien** importieren, sonst ist jeder Artikel doppelt da.

---

## Weg B: Einzelnen Artikel von Hand anlegen (ohne Import)

1. **Beiträge → Erstellen.**
2. **Titel** aus dem Steckbrief eintragen.
3. Inhalt einfügen:
   - **Block-Editor:** Oben rechts **⋮ → „Code-Editor“** (oder Strg+Umschalt+Alt+M). Den kompletten Inhalt der Datei `ARTIKEL_ZUM_HOCHLADEN/NN-….html` einfügen. Die Datei öffnest du mit einem Texteditor, nicht mit dem Browser. Danach **„Code-Editor verlassen“**. WordPress zeigt den Text dann als „Klassisch“-Block oder als einzelne Blöcke an. Beides ist in Ordnung.
   - **Klassischer Editor:** Tab **„Text“** (nicht „Visuell“) wählen und den Inhalt einfügen.
4. In der Seitenleiste ausfüllen: **Kategorie** (nur eine), **Schlagwörter**, **Autor**, **Beitragsbild**, **Permalink**, jeweils laut Steckbrief.
5. **Rank Math:** SEO-Titel, Beschreibung und Fokus-Keyword aus dem Steckbrief übernehmen.
6. **Planen** wie in Schritt 5, Punkt 7.

Am Ende jedes Inhalts steht ein unsichtbarer Block `<script type="application/ld+json">`. Das sind die FAQ-Daten für Google, genau wie im Aquapark-Beitrag. Bitte mit einfügen und nicht löschen.

---

## Nach der Veröffentlichung

- **Nachverlinkung:** In `NACHVERLINKUNG.md` steht, welcher ältere Artikel einen Link auf den neuen bekommt, sobald dieser online ist. In Summe sind es 45 Links. Dazu den Ankertext markieren, **Strg+K** drücken, die URL einfügen und **„Aktualisieren“** klicken. So gibt es nie Links auf Seiten, die noch nicht existieren.
- Optional in der Google Search Console: **URL-Prüfung → „Indexierung beantragen“** für den neuen Link.

## WhatsApp-Nummer später ändern

In allen Artikeln steht aktuell **0157 92326450** (Link `wa.me/4915792326450`). Wenn sich die Nummer ändert:

- **Noch nicht hochgeladene Artikel:** Sag mir die neue Nummer, dann erzeuge ich alle Dateien neu. Es ist nur eine Stelle im Generator.
- **Schon hochgeladene Artikel:** Mit einem Suchen-und-Ersetzen-Plugin, z. B. „Better Search Replace“, `4915792326450` durch die neue Nummer ersetzen (Format: 49 + Nummer ohne 0). Vorher den Probelauf („Dry Run“) nutzen und eine Sicherung machen.
- **Achtung, schon heute:**
  - Die automatische Box „Lieber persönlich planen? → Beratung anfragen“ unter jedem Beitrag nutzt noch die Nummer **0155 63462222** (`wa.me/4915563462222`). Sie steckt in eurem Design-Snippet unter **Code Snippets (WPCode)**. Dort einmal die Nummer anpassen, dann gilt sie für alle Beiträge.
  - Dieselbe alte Nummer steht außerdem in WhatsApp-Links auf etwa 60 Seiten, z. B. Hotelseiten und Reisethemen.

## Cashback

Alle Artikel nennen einheitlich **„bis zu 1.000 € Cashback“** mit Link auf https://haydiweg.de/cashback/ und dem Zusatz „gemäß Teilnahmebedingungen“.

## Dubai-Artikel

Mit Stand 05.11.2026 rät das Auswärtige Amt von nicht notwendigen Reisen in die VAE ab. Die drei Dubai-Artikel sind fertig, liegen aber in einer eigenen Datei. Ihre Termine haben Alanya, Zypern und Madeira übernommen. Sobald der Hinweis aufgehoben ist: AA-Seite prüfen, Datei importieren, Termin wählen.

## Wenn etwas nicht aussieht wie erwartet

| Problem | Lösung |
|---|---|
| FAQ erscheint nicht als Akkordeon | Die Überschrift muss exakt „Häufige Fragen“ lauten (H2) und die Fragen H3 sein. Nicht umbenennen |
| Kein Bild im Kopf | Beitragsbild setzen (Schritt 5.2) |
| Link führt auf 404 | Zielartikel ist noch nicht online. Link entfernen und später laut Nachverlinkung setzen |
| Adresse lautet anders als im Steckbrief | Permalink in der Seitenleiste korrigieren. Kategorie-Titelform prüfen (Schritt 3) |
| Beitrag wurde zur falschen Uhrzeit veröffentlicht | Zeitzone prüfen (Einstellungen → Allgemein) |
| Geplanter Beitrag erscheint nicht („Planung verpasst“) | Kommt bei wenig Besucherverkehr vor, weil WordPress-Termine erst bei einem Seitenaufruf ausgelöst werden. Beitrag öffnen und „Veröffentlichen“ klicken. Dauerhafte Lösung: einen STRATO-Cronjob für `wp-cron.php` einrichten lassen |

## Checkliste pro Artikel (vor dem Planen)

- [ ] Beitragsbild gesetzt, Rechte geklärt, ALT-Text eingetragen
- [ ] Titel, Permalink und Kategorie wie im Steckbrief
- [ ] Autor richtig
- [ ] Rank Math: Titel, Beschreibung und Fokus-Keyword vorhanden
- [ ] Vorschau am Handy kurz angesehen
- [ ] Datum und Uhrzeit laut Steckbrief, Status „Geplant“
- [ ] Bei Einreise- oder Sicherheitsthemen: Seite des Auswärtigen Amts am Vortag noch einmal geöffnet
