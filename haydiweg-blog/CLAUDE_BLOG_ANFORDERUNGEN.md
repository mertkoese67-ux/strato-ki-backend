# CLAUDE_BLOG_ANFORDERUNGEN – zentrale Anforderungen für den haydi-weg-Blog

Stand: 05.11.2026 · Erstellt von Claude Code

## 1. Zugriff auf frühere Claude-Chats: Ergebnis der Prüfung

| Geprüfte Quelle | Ergebnis |
|---|---|
| Chatverläufe auf claude.ai | **Kein Zugriff.** Claude Code in dieser Cloud-Umgebung kann keine Unterhaltungen aus der claude.ai-Oberfläche lesen. Es gibt dafür weder eine Schnittstelle noch eine autorisierte Integration. Cookie- oder Login-Umwege habe ich bewusst nicht genutzt. |
| Projektdateien / Chat-Exporte im Repository `strato-ki-backend` | Nicht vorhanden. Das Repository enthält nur ein Node.js-Backend, das Airline-Rechnungen per KI ausliest (`api/index.js`). |
| Verbundene Dienste (Canva, ElevenLabs, Higgsfield, GitHub, Claude Docs) | Keiner davon enthält Chatverläufe. |

**Was ich von dir brauche:** Exportiere deine claude.ai-Daten unter *Einstellungen → Datenschutz → Daten exportieren* (ZIP mit `conversations.json`) oder kopiere die relevanten Chats als Text. Lade die Datei anschließend in diesen Ordner. Ich gleiche dann diese Datei ab und markiere Abweichungen.

Bis dahin stützen sich die Anforderungen unten auf zwei überprüfbare Quellen:
- **[M]** deinen Masterprompt vom 05.11.2026 (von dir bestätigt)
- **[W]** den aktuellen Stand von haydiweg.de. Der Beitrag vom 02.11.2026 und die überarbeiteten Seiten zeigen sehr wahrscheinlich die Ergebnisse früherer Chats. Diese Einordnung ist eine **Ableitung** und keine Bestätigung.

Eigene Empfehlungen sind mit **[V]** (Vorschlag) gekennzeichnet.

## 2. Bestätigte Anforderungen [M]

| Bereich | Anforderung |
|---|---|
| Ziel | Mehr qualifizierte organische Besucher, Marke als vertrauenswürdige Reiseinformationsquelle, langfristig mehr Buchungen |
| Frequenz | Wunsch: 3 Artikel pro Woche, kritisch zu prüfen. Qualität geht vor Menge |
| Zeitraum | 09.11.2026 bis 31.01.2027, 36 Artikel in 12 Wochen |
| Zielgebiete | Türkei (Kernkompetenz), Ägypten, Spanien/Kanaren, Griechenland, Dubai/VAE, Fernreisen (Thailand, Bali, Malediven, Dom. Republik) |
| Content-Typen | Information, Vergleich, Saisonal, buchungsnah, Evergreen |
| Sprache/Zielgruppe | Deutsch, Urlauber aus Deutschland |
| Qualität | Menschlich, hilfreich, keine KI-Floskeln, kein Keyword-Stuffing, Quellen nennen, nichts erfinden (Hotelbewertungen, Erfahrungen, Preise, Tests). Unsicheres zur redaktionellen Prüfung markieren |
| Bilder | Eigene, rechtlich nutzbare Aufnahmen bevorzugen. Keine ungeklärten Fremdbilder. Fehlt ein Bild, wird es zur Medienprüfung markiert |
| WordPress | Nur autorisierte Zugänge, nur Entwürfe, **keine Veröffentlichung ohne ausdrückliche Freigabe**, keine Plugin-, Theme- oder Datenbankänderungen. Die Buchungsstrecke (IBE) darf nicht beeinträchtigt werden |
| Daten | Keine erfundenen Suchvolumina, Rankings, CTRs oder Prognosen |

## 3. Aus der Website abgeleitete Standards [W]

Diese Punkte sind auf der Website schon umgesetzt und sehen nach bewussten Entscheidungen aus. Bitte bestätige sie oder korrigiere sie.

1. **Du-Ansprache** auf allen Seiten.
2. **Ehrlichkeit als Markenkern:** Formulierungen wie „ehrlich beraten“, „Wir sagen dir ehrlich, ob das günstige Hotel passt“ und „eigene Eindrücke statt Katalogtext“.
3. **Eigene Hotelvideos** als Alleinstellungsmerkmal: 19 Hotelseiten unter /hotel/, überwiegend Türkische Riviera. Im Aquapark-Beitrag ist klar getrennt, was „von uns gefilmt“ ist und was „laut Hotel“ gilt. Der Stand der Angaben wird genannt (z. B. „Stand Oktober 2026“).
4. **Quellen** werden im Text verlinkt, etwa die Ferienordnung NRW und das Auswärtige Amt.
5. **Conversion-Elemente:** IBE (/buchen/), „bis zu 1.000 € Cashback“ (/cashback/), WhatsApp-Links mit vorausgefülltem Text, Reisebüro in Minden.
6. **Beitragsaufbau:** Inhaltsverzeichnis, Vergleichstabelle, Abschnitte nach Zielgruppe, Checkliste, FAQ (FAQPage-Schema), CTA-Box, Lesezeit.
7. **SEO-Plugin:** Rank Math. Title-Format „Thema: Nutzen | haydi-weg“ mit ca. 50–60 Zeichen.
8. **Permalinks für Beiträge:** `/%category%/%postname%/`, z. B. /tuerkei/tuerkei-hotel-mit-aquapark/.
9. Tag- und Autorenarchive stehen auf `noindex`, Kategoriearchive sind indexierbar.

## 4. Widersprüche und offene Entscheidungen

| # | Widerspruch / Unklarheit | Empfehlung [V] | Status |
|---|---|---|---|
| W1 | Die bisherigen „Blogartikel“ sind **WordPress-Seiten** (/reise-blog/…, /reisethemen/…), nur ein Text ist ein echter **Beitrag**. Damit gibt es zwei Systeme mit unterschiedlichen URL-Mustern, Schemas (Article vs. BlogPosting) und Archiven. | Neue Artikel als **Beiträge** anlegen. Bestehende Seiten **nicht** umziehen, weil URL-Änderungen ohne Not Rankings kosten. Die /reise-blog/-Übersicht sollte künftig zusätzlich die neuen Beiträge zeigen. | Entscheidung offen |
| W2 | Kategorie im Permalink (`/tuerkei/…`): Wer später die Kategorie ändert, ändert auch die URL. | Kategorien aus dem Plan festlegen und danach nicht mehr ändern. Pro Beitrag gibt es genau eine Hauptkategorie. | Vorschlag |
| W3 | Wunsch „3 pro Woche“ gegen „Qualität vor Menge“ | Siehe BLOG_STRATEGIE: 3 pro Woche nur für die Startphase bis Ende Januar, weil die Entwürfe vorbereitet sind. Danach 2 pro Woche plus Aktualisierungen. | Vorschlag |
| W4 | Autor wird als „admin“ ausgegeben (Schema, Autorenlink). Das passt nicht zur Marke und schwächt die Expertise-Signale (E-E-A-T). | Autorenprofil „Hatice Köse, Reisebüro haydi-weg Minden“ mit kurzer Bio anlegen, oder einen anderen tatsächlichen Autor nennen. | Freigabe nötig |
| W5 | „Beste Reiseziele 2024“ ist noch indexiert und veraltet. | Auf 2027 aktualisieren (URL beibehalten oder auf neue URL umleiten). | Vorschlag |
| W6 | Mehrere Seiten bedienen ähnliche Winter-Suchintentionen (/winterurlaub/, /reise-blog/reiseziele-im-winter/, /reisethemen/reiseziele-dezember|januar/). | Kannibalisierung in der Search Console prüfen. Falls sie sich bestätigt, Rollen schärfen oder Inhalte zusammenführen. | Datenprüfung nötig |
| W7 | Vorhandenes Bildmaterial: Bei 5 Mediendateien deutet der Name auf Instagram-Downloads hin („Snapinsta“). 52 Dateien heißen „Screenshot“ oder „Unbenannt“. | Rechte klären, bevor die Dateien weiter verwendet werden. In den neuen Entwürfen sind sie ausgeschlossen. | Prüfung nötig |

## 5. Verbindliche Arbeitsregeln für alle Entwürfe

Die Regeln stehen vollständig in `_arbeitsdaten/STYLEGUIDE_UND_ARTIKELVORLAGE.md`. Die wichtigsten:

- Die Antwort steht im ersten Absatz. Danach folgen Struktur, Tabelle bei Vergleichen, FAQ, CTA und Quellen.
- Belegpflicht für Einreise, Ferien, Gebühren, Klima und Hotelangaben. Ist etwas unsicher, kommt `[PRÜFEN: …]` dazu.
- „Von uns gefilmt“ darf nur bei Hotels mit eigener /hotel/-Seite stehen.
- Keine Euro-Preise. Bei Kosten werden die Kostenfaktoren erklärt und es gibt einen Verweis auf Live-Preise in der IBE.
- Interne Links nur auf existierende URLs. Links auf geplante Artikel sind mit `<!-- geplant #NN -->` markiert.
