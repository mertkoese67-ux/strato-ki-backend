# KPI-Dashboard und Teststrategie

Stand 09.11.2026. Grundlage: Masterplan Tab 6 „KPI & Tests“ (06.11.2026), Audit-Belegtabelle (Wettbewerber, Abruf 06.11.2026) und die Vorgaben des Auftrags. **Alle Zielwerte sind Annahmen und Szenarien, keine Prognosen.** Es gibt keine gesicherten Aussagen über den Instagram- oder TikTok-Algorithmus; gemessen wird, was die Plattform-Insights liefern.

## 1 Ausgangslage und Ziel (aus Tab 6)

| Größe | Wert | Quelle |
|---|---|---|
| Instagram-Follower am 06.11.2026 | 2.652 | Tab 6 |
| Ziel | 10.000 Follower bis 30.04.2027 (≈ 294 neue Follower pro Woche) | Tab 6 |
| Soll-Linie (Zwischenziele) | 20.11.: 3.240 · … · 05.02.2027: 6.473 | Tab 6 |
| Primärkanal | Instagram (Urlaubspiraten-Inhalte liefen dort 4–16× besser als auf TikTok) | Audit (A) |
| Steuergröße Nr. 1 | **Follower je 1.000 erreichte Nicht-Follower (F/1k)** | Tab 6 |
| Szenarien F/1k | 0,5 (schwach) · 1,5 (Basis) · 3,0 (stark) | Tab 6 |

Die Soll-Linie ist linear gerechnet; Reels wachsen nicht linear. Sie dient nur als Frühwarnung: liegt der Ist-Wert an zwei Reviews hintereinander unter der Linie, greift der Diagnosepfad (Abschnitt 4).

## 2 Dashboard-Definition (je Reel und je Woche)

Datenquelle: Instagram Insights (Reel-Ebene, nach 48 h und nach 7 Tagen), TikTok Analytics. Eintrag von Hand in die Tabelle `KPI_Tracking` (Vorlage unten) – das Studio speichert keine Plattformdaten.

| KPI | Definition | Erhebung | Warum |
|---|---|---|---|
| Reichweite | erreichte Konten | 48 h / 7 d | Grundgröße |
| Nicht-Follower-Reichweite | erreichte Konten, die nicht folgen (absolut und Anteil) | 7 d | zeigt Empfehlungsverteilung |
| Wiedergabedauer (Ø) | durchschnittliche Wiedergabezeit in s | 7 d | Retention-Basis |
| Retention | Ø Wiedergabedauer ÷ Videolänge (%) · zusätzlich: Anteil, der die ersten 3 s übersteht (sofern Insights „Hook-Rate“ zeigen) | 7 d | Hook und Story |
| Shares | Weiterleitungen | 7 d | Shareability |
| Saves | Speicherungen | 7 d | Nutzwert |
| Profilbesuche | aus dem Reel | 7 d | Interesse an der Marke |
| Neue Follower | aus dem Reel | 7 d | Ziel |
| **F/1k** | neue Follower ÷ (Nicht-Follower-Reichweite ÷ 1.000) | 7 d | Steuergröße |
| Kommentare (Zusatz) | Anzahl, davon Fragen | 7 d | Community, Staffel-2-Themen |

Wochenblick: Summe Reichweite, Summe neue Follower, Ø F/1k, bestes/schwächstes Reel, Serienvergleich (FoF / WDKS / RW).

### Vorlage `KPI_Tracking` (Spalten)

`Reel-ID · Datum · Serie · Titel · Hook-Variante · Cover-Variante · Länge s · Reichweite 48h · Reichweite 7d · Nicht-Follower 7d · Ø Wiedergabe s · Retention % · Shares · Saves · Profilbesuche · neue Follower · F/1k · Kommentare · Notiz`

## 3 Reviews (zweiwöchentlich, aus Tab 6)

Termine: 20.11., 04.12., 18.12.2026 · 04.01., 15.01., 29.01., 08.02.2027 (Abschluss Staffel 1).

Ablauf je Review (30 Minuten): 1) Tabelle vollständig? 2) Ist vs. Soll-Linie 3) Top-3 / Flop-3 nach F/1k und Retention 4) Muster: Serie, Cluster, Hook-Typ, Länge 5) Eine Entscheidung für die nächsten zwei Wochen (nicht mehr) 6) Eintrag ins Verbesserungsprotokoll der betroffenen Reels im Studio.

## 4 Diagnosepfad (wenn ein Reel schwach läuft)

| Symptom | Wahrscheinliche Ursache | Maßnahme |
|---|---|---|
| Reichweite niedrig, Retention hoch | Erstes Bild/Cover stoppt nicht | Cover-Variante B/C testen, Hook-Overlay kürzer, Startbild mit Bewegung |
| Reichweite hoch, Retention < 40 % | Auflösung zu früh oder Mitte zu lang | Auflösung Richtung 70 % schieben, Mittelteil um einen Satz kürzen (Studio: Sprechtext-Fassung) |
| Saves hoch, Follower niedrig | Nutzwert ohne Serienbindung | Serienteaser schärfen, Abbinder mit Folgennummer, Profil-Bio prüfen |
| Shares hoch, Nicht-Follower-Anteil niedrig | Inhalt wird im eigenen Kreis geteilt, aber nicht empfohlen | Thema näher an DACH-Kernziele, Hook mit Zahl/Behauptung |
| Kommentare mit Faktenzweifel | Quelle nicht im Bild | Quellen-Overlay klein ergänzen, Caption um Quelle erweitern |

## 5 Testplan (13 Wochen)

Grundsatz: **ein Test je Reel**, zwei Wochen Laufzeit, Entscheidung im Review. Varianten werden im Studio vorbereitet (Hook-Studio: 5 Hooks, 3 Cover; Sprechtext-Fassungen). Tests laufen über Reels derselben Serie, nicht als Duplikat-Posts.

| Woche | Test | Varianten | Messgröße |
|---|---|---|---|
| 1–2 | Hook-Typ | Serienfrage („Fakt oder Fake …?“) vs. überraschende Behauptung (Reel 01 vs. 04 / 07) | Reichweite, Retention 3 s |
| 2–3 | Cover | Variante A (Frage) vs. B (Zahl) – Reels 05/06 vs. 08/09 | Profilbesuche aus dem Raster, Reichweite |
| 3–4 | Länge | ≈ 30 s (Reel 11, 12) vs. ≈ 35 s (Reel 10, 13) | Retention %, Saves |
| 5–6 | Thema | Hotelkonzept (15, 18, 20) vs. Natur-WOW (13, 16) | F/1k |
| 6–7 | Erzählweise | Fakt-oder-Fake-Auflösung „Fakt“ vs. „kommt drauf an“ (16 vs. 19) | Kommentare, Shares |
| 7–8 | Posting-Zeit | 18:00 vs. 12:00 (Reels 21–24, Feiertagswoche) | Reichweite 48 h |
| 9–10 | TikTok-Hook | frecherer nativer Text (TikTok-Varianten aus dem Hook-Studio) vs. Instagram-Hook | TikTok-Reichweite |
| 10–11 | Nutzwert-Overlay | mit vs. ohne Tipp-Overlay am Ende (27, 30 vs. 29, 32) | Saves |
| 11–12 | Serienteaser | konkreter Titel vs. nur „nächsten Montag“ (31, 34) | Follower je Reel |
| 13 | Staffelfinale | Community-Frage – Auswertung der Kommentare für Staffel 2 | Kommentare, Themenwünsche |

Regeln: keine zwei Tests gleichzeitig auf demselben Reel; Varianten werden im Studio dokumentiert (Notizen je Reel); Ergebnis als Zahl, nicht als Eindruck; erst nach zwei Reviews mit gleicher Richtung wird eine Regel für den Plan daraus.

## 6 Profilmaßnahmen (aus Tab 6, verbindlich vor Reel 01)

- Profilname und Bio tragen das Follow-Versprechen; Serien als Highlights/Ordner (Fakt oder Fake? · Was dir keiner sagt · Reisewissen).
- Keine Verkaufszeile bis 31.12.2026; ab Februar 2027 höchstens „Fragen zur Reise? Wir beraten seit 2014.“ im Profil.
- Antworten auf Kommentare innerhalb von 24 h (Fragen → Themenliste Staffel 2).

## 7 Was nicht gemessen oder behauptet wird

- Keine Benchmarks aus Wettbewerberzahlen abgeleitet (die Audit-Tabelle ist Beobachtung, keine Vergleichsbasis).
- Keine Aussagen zu „Algorithmus bevorzugt …“; nur eigene Messwerte zählen.
- Higgsfield-Vorabcheck > 80 (Plan-Regel) wurde in dieser Sitzung nicht ausgeführt; er bleibt freiwillige Zusatzprüfung, keine KPI.

## 8 Ergänzung v3: Follow-Strategie messen, nicht versprechen

Die Content-Identität (vier Themenwelten, fünf Strukturen, Endkarte mit Themenwelt-Zeile) steht in `02_MASTERPLAN_FINAL.md`, Abschnitt 2. Für die Auswertung gelten zusätzlich je Reel: Themenwelt und Struktur als Spalten im `KPI_Tracking`, damit nach 4–6 Wochen sichtbar wird, welche Themenwelt Follower je 1.000 Views bringt und welche Struktur die Wiedergabedauer hält. Vergleich nur innerhalb derselben Serie und mit mindestens drei Reels je Gruppe. Keine Zielzahlen für Reichweite, Shares oder Follower – gemessen wird, dann wird der Plan nachgeschärft (Reserveliste in `01_THEMENBEWERTUNG_60plus.md`).
