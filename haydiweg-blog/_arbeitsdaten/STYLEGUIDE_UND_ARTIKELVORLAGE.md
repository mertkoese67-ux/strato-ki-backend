# Styleguide und Artikelvorlage für haydi-weg

Verbindlich für alle 36 Entwürfe. Abgeleitet aus dem bestehenden Beitrag „Türkei-Hotels mit Aquapark“ (02.11.2026) und den aktuellen Seiten von haydiweg.de.

## 1. Wer wir sind (nur diese Fakten verwenden)

- haydi-weg ist ein Reisebüro in Minden (Königstraße 52, 32423 Minden), Inhaberin Hatice Köse. Es vermittelt Pauschalreisen verschiedener Veranstalter und berät online, per WhatsApp und vor Ort.
- Das Reisebüro hat eine Online-Buchungsstrecke (IBE) unter https://haydiweg.de/buchen/ und bietet **„bis zu 1.000 € Cashback“ für berechtigte Online-Buchungen gemäß Teilnahmebedingungen**: https://haydiweg.de/cashback/. Die Teilnahmebedingungen werden nicht ausgeschmückt und es werden keine Beträge pro Reise genannt.
- WhatsApp: `https://wa.me/4915792326450?text=<URL-kodierter Text>` (Nummer laut Kontaktseite: 0157 92326450. Auf vielen Inhaltsseiten steht noch 4915563462222. Welche Nummer gilt, klärt die Inhaberin)
- Wir haben **eigene Hotelvideos** von den Hotels, die auf haydiweg.de eine Seite unter /hotel/ haben (Liste in `interne_url_liste.txt`). Nur bei diesen Hotels darfst du schreiben „haben wir gefilmt“ oder „unser Hotelvideo“. Fakten zu diesen Hotels nimmst du von unserer Hotelseite (WebFetch) und kennzeichnest sie als „laut Hotel“.
- **Verboten:** erfundene Besuche, persönliche Erlebnisse („Als wir in Hurghada waren …“), Kundenstimmen, Bewertungen, Preise in Euro, Rabattprozente, Rankings („Platz 1“), Suchvolumina, Behauptungen wie „Testsieger“.

## 2. Tonalität

- Deutsch, **du-Ansprache** wie auf der Website. Freundlich, ruhig und ehrlich, wie eine erfahrene Reiseberaterin, die auch sagt, wann etwas *nicht* passt.
- Antwort zuerst: Der erste Absatz beantwortet die Suchfrage in 2–3 Sätzen konkret. Das ist wichtig für Featured Snippets und KI-Suche.
- Kurze Absätze (2–4 Sätze), aktive Sprache, konkrete Zahlen mit Quelle.
- Keine KI-Floskeln. Vermeide: „In der heutigen Zeit“, „Egal ob … oder …“, „Tauche ein“, „atemberaubend“, „ein wahres Paradies“, „unvergesslich“, „Fazit: Es kommt darauf an“, „Zusammenfassend lässt sich sagen“, Häufungen von Ausrufezeichen und Emojis.
- Kein Keyword-Stuffing. Das Fokus-Keyword steht in H1, im ersten Absatz, in einer H2 und in der Meta-Description, sonst nur dort, wo es natürlich passt.
- Hinweise wie „Reiseveranstalter und Fluggesellschaften können abweichende Regeln haben“ dort einsetzen, wo es fachlich nötig ist, aber nicht in jedem Absatz.

## 3. Fakten und Quellen

- Zeitabhängige Fakten (Einreise, Visum, Ferien, Gebühren, Klima, Feiertage) **müssen** mit einer Quelle belegt werden. Bevorzugte Quellen:
  - Einreise/Sicherheit: Auswärtiges Amt (auswaertiges-amt.de), offizielle Regierungsseiten des Ziellandes (z. B. visa2egypt.gov.eg, u.ae, tdac.immigration.go.th)
  - Ferien: Kultusministerkonferenz (kmk.org, Ferienkalender) und Kultusministerien der Länder
  - Feiertage: Gesetze/Landesregierungen bzw. bundesweit anerkannte Übersichten mit Primärquellenverweis
  - Klima: Deutscher Wetterdienst (DWD), nationale Wetterdienste, WMO; Wassertemperaturen nur als Spanne mit Quelle und dem Hinweis „langjährige Mittelwerte, schwanken von Jahr zu Jahr“
  - Pauschalreiserecht: BGB §§ 651a ff. (gesetze-im-internet.de), Verbraucherzentrale
  - Gesundheit: Auswärtiges Amt (Gesundheit), RKI/STIKO, CRM nur sekundär
  - Hotels: unsere Hotelseite oder die offizielle Hotelwebsite (Stand angeben)
- Prüfe jede Quelle mit WebFetch oder WebSearch. Zitiere nichts, was du nicht abgerufen hast.
- Wenn eine verlässliche Quelle fehlt oder widersprüchlich ist, schreibe den Satz vorsichtig und markiere ihn inline mit `[PRÜFEN: Grund]`. Nimm den Punkt außerdem in `redaktionelle_pruefung` im Frontmatter auf.
- Bei Klima: Formuliere Spannen („meist um 22 bis 24 °C“) statt Scheingenauigkeit.
- Unter „Stand“ steht das Abrufdatum (November 2026).

## 4. Aufbau jedes Artikels

1. `# H1` (= titel_h1)
2. Einstieg: 2–4 Absätze, mit der Antwort zuerst. **Keine** Überschrift „Einleitung“.
3. Optional ein Kasten „Das Wichtigste in Kürze“ als Liste mit 3–5 Punkten. Er bietet sich bei Info- und Vergleichsartikeln an.
4. 4–8 `##`-Abschnitte mit `###`-Unterpunkten, wo sinnvoll. Bei Vergleichen gehört eine Markdown-**Tabelle** dazu.
5. Ein Abschnitt mit unserer ehrlichen Empfehlung („Für wen passt was?“), ohne Superlative.
6. `## Häufige Fragen` mit 4–6 `###`-Fragen, die echte Nutzerfragen sind (aus Nebenkeywords oder Autocomplete). Antworten haben je 2–4 Sätze.
7. Abschlussabschnitt mit CTA (H2, z. B. „Deinen Winterurlaub auf den Kanaren finden“): Er verweist auf IBE/Cashback und WhatsApp mit vorausgefülltem Text. Der Abschluss ist nicht aufdringlich.
8. `## Quellen`: eine Liste mit Titel, Herausgeber, URL und „abgerufen am …“.

Bildplatzhalter setzt du im Text als HTML-Kommentar an der passenden Stelle:
`<!-- BILD: dateiname-vorschlag.webp | ALT: beschreibender Alt-Text | QUELLE: Mediathek-ID 1234 oder MEDIENPRÜFUNG -->`

Interne Links schreibst du als normale Markdown-Links mit absoluter URL. Links auf noch nicht veröffentlichte neue Artikel schreibst du als
`[Ankertext](https://haydiweg.de/kategorie/slug/)<!-- geplant #NN -->`
Nutze nur URLs aus `interne_url_liste.txt` oder aus der Spalte „Interne Links (neue Artikel)“ des Redaktionsplans. **Erfinde keine URLs.** Setze 4–10 interne Links pro Artikel mit beschreibendem Ankertext (nicht „hier klicken“).

Länge: Die Zielwörter aus dem Plan gelten mit ±20 %. Zähle nicht künstlich hoch, Inhalt geht vor.

## 5. Frontmatter (YAML, exakt diese Felder)

```yaml
---
nr: 1
titel_h1: "…"
seo_title: "… | haydi-weg"          # max. 60 Zeichen inkl. Marke; Marke darf entfallen, wenn es zu lang wird
meta_description: "…"                # 130–155 Zeichen, mit Nutzen und Fokus-Keyword, ohne Emojis
slug: "…"
ziel_url: "https://haydiweg.de/<kategorie>/<slug>/"
wp_kategorie: "Türkei"
schlagwoerter: ["…", "…"]            # 3–6 Schlagwörter; vorhandene Tags bevorzugen: Aquapark, Belek, Familienurlaub, Kemer, Lara, Side
fokus_keyword: "…"
nebenkeywords: ["…"]
veroeffentlichung: "2026-11-09T07:30:00+01:00"
status: "draft"
lesezeit_min: 8
beitragsbild:
  datei: "…webp"
  alt: "…"
  quelle: "Mediathek-ID 1234 | MEDIENPRÜFUNG"
weitere_bilder:
  - datei: "…"
    alt: "…"
    quelle: "…"
quellen_geprueft_am: "2026-11-05"
redaktionelle_pruefung:
  - "…"
schema: ["BlogPosting", "FAQPage"]
---
```

## 6. Bilder

- Bevorzuge Bilder aus unserer Mediathek (`mediathek_inventar.tsv`, Spalten id/mime/url/alt). Hotelbilder gibt es dort für die gefilmten Türkei-Hotels. Gib dann `quelle: "Mediathek-ID <id>"` an.
- Dateien mit „snapinsta“, „screenshot“ oder „unbenannt“ im Namen **nicht** verwenden, weil ihre Rechte ungeklärt sind.
- Gibt es kein passendes eigenes Bild, schreibst du `quelle: "MEDIENPRÜFUNG"` mit einem konkreten Motivvorschlag. Verlinke keine fremden Bilder und keine Stockfoto-URLs.
- Dateinamen bestehen aus Kleinbuchstaben, Bindestrichen und der Endung `.webp`, sind beschreibend und enthalten keine Umlaute (ae/oe/ue/ss).
- ALT-Texte beschreiben in 8–15 Wörtern, was zu sehen ist, und nennen den Ort. Kein Keyword-Stuffing.

## 7. Abgrenzung (Kannibalisierung vermeiden)

Bestehende Seiten, die NICHT dupliziert werden dürfen (nur verlinken):
- /urlaubsziele/tuerkei-urlaub-buchen/beste-reisezeit-tuerkei/ (Ganzjahres-Reisezeit Türkei)
- /tuerkei/tuerkei-hotel-mit-aquapark/ (Aquapark-Hotels)
- /reisethemen/reiseziele-<monat>/ (Monatsübersichten mehrerer Ziele)
- /ostern-urlaub/, /pfingsten-urlaub/, /winterurlaub/, /familienurlaub/, /sommerurlaub-all-inclusive/, /pauschalreisen/
- Zielgebietsseiten /urlaubsziele/<land>-urlaub-buchen/ (allgemeine Länderübersicht). Neue Artikel vertiefen eine konkrete Frage und verlinken auf die Zielgebietsseite als Pillar.
