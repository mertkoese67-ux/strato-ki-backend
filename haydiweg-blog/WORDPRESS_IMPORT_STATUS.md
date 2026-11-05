# WordPress-Import: Status und Anleitung

Stand: 05.11.2026

## 1. Ergebnis der Prüfung der WordPress-Schnittstellen

| Schnittstelle | Befund | Genutzt? |
|---|---|---|
| WordPress REST-API (`/wp-json/wp/v2/`) | öffentlich lesbar (Beiträge, Seiten, Medien, Kategorien) | **nur lesend** für die Analyse |
| Schreibzugriff über REST-API (Application Password) | **kein Zugang vorhanden** | nein |
| WordPress-MCP-Endpunkt (`/wp-json/mcp`) und Elementor-MCP-Composer | auf der Website aktiv, aber **keine autorisierte Verbindung** in dieser Umgebung | nein |
| Rank-Math-REST (`rankmath/v1`) | vorhanden, braucht Anmeldung | nein |
| STRATO-Hosting / Datenbank / FTP | kein Zugang, wurde bewusst nicht gesucht | nein |

**Entscheidung:** Ohne autorisierten Schreibzugang ist eine direkte Integration nicht sicher möglich. Deshalb gibt es, wie im Auftrag als Alternative vorgesehen, **vollständig importierbare Dateien**. Auf der Website wurde nichts angelegt, verändert oder veröffentlicht.

## 2. Gelieferte Dateien (`WORDPRESS_IMPORT/`)

| Datei | Inhalt |
|---|---|
| `haydiweg-blog-entwuerfe.xml` | WordPress-WXR-Datei (Werkzeuge → Daten importieren → WordPress) mit allen freigabefähigen Artikeln als **Entwurf** (`draft`) |
| `haydiweg-blog-entwuerfe-zurueckgestellt-dubai.xml` | die 3 Dubai-Artikel, ebenfalls als Entwurf. **Erst importieren, wenn das Auswärtige Amt den Hinweis für die VAE aufhebt** |
| `html/NN-slug.html` | jeder Artikel als HTML-Datei, z. B. zum Einfügen in ein Elementor-Text-Widget oder zur Sichtprüfung im Browser |

Pro Beitrag enthält die WXR:
- Titel (H1), Slug, Kategorie (eine Hauptkategorie), Schlagwörter (kontrolliertes Vokabular: bestehende Tags plus Tags, die in mindestens 2 Artikeln vorkommen), Auszug (= Meta-Description)
- `post_date` = geplanter Veröffentlichungstermin. Der Status bleibt aber **draft**: WordPress veröffentlicht einen Entwurf auch dann nicht automatisch, wenn das Datum erreicht ist.
- **Rank-Math-Metadaten:** `rank_math_title`, `rank_math_description`, `rank_math_focus_keyword` (Fokus-Keyword plus bis zu 4 Nebenkeywords)
- Redaktionsfelder: `_hw_redaktionsplan_nr`, `_hw_geplante_veroeffentlichung`, `_hw_beitragsbild_vorschlag`, `_hw_quellen_geprueft_am`
- **Interne Links** als absolute URLs. Links auf noch nicht veröffentlichte Artikel tragen `data-geplant="NN"`. Sie führen bis zur Veröffentlichung des Zielartikels auf eine 404-Seite und müssen vorher entfernt oder rechtzeitig veröffentlicht werden.
- **Sichtbare Redaktionsmarker:** gelbe Kästen „BILD (Redaktion)“ an den vorgesehenen Bildpositionen und markierte `[PRÜFEN: …]`-Stellen. Sie sind absichtlich sichtbar, damit kein Entwurf ungeprüft live geht.

## 3. Was ausgeführt wurde und was offen ist

| Schritt | Status |
|---|---|
| Artikel als WordPress-Entwürfe erstellen | ✅ als Importdatei vorbereitet. ❌ nicht auf der Website ausgeführt (kein autorisierter Zugang, keine Freigabe) |
| SEO-Metadaten über Rank Math hinterlegen | ✅ in der Importdatei enthalten (Rank-Math-Metafelder) |
| Kategorien und Schlagwörter | ✅ in der Importdatei. Neue Kategorien entstehen beim Import automatisch: Ägypten, Spanien, Griechenland, Dubai*, Fernreisen, Reiseplanung, Zypern, Portugal |
| Interne Verlinkung | ✅ im Inhalt. Geplante Links sind markiert |
| Beitragsbilder | ❌ nicht zugeordnet. Die Vorschläge stehen im Frontmatter bzw. im Feld `_hw_beitragsbild_vorschlag`. Rechte und Auswahl müssen freigegeben werden |
| Redaktionskalender separat | ✅ REDAKTIONSKALENDER.md und REDAKTIONSPLAN_3_MONATE.csv |
| Darstellung in Elementor und auf Mobilgeräten prüfen | ❌ offen. Ohne Zugang zum Elementor-Beitrags-Template nicht prüfbar. Der bestehende Beitrag (Aquapark) nutzt ein Template mit Inhaltsverzeichnis, Lesezeit und CTA-Box, das sich auf die Gutenberg-/HTML-Inhalte der Entwürfe anwenden sollte |
| Probeimport in einer Test-WordPress-Installation | ❌ **nicht durchgeführt.** Die Sicherheitsprüfung dieser Umgebung hat das Aufsetzen einer lokalen WordPress-Testinstallation abgelehnt. Ich habe nur die Struktur geprüft: gültiges XML, alle Items `draft`, Pflichtfelder vorhanden |

\* Die Kategorie Dubai entsteht nur, wenn die Datei mit den zurückgestellten Artikeln importiert wird.

## 4. Empfohlener Ablauf für den Import (durch dich oder mit deiner Freigabe)

1. **Backup** anlegen. All-in-One WP Migration ist installiert, alternativ das STRATO-Backup.
2. Den Import möglichst zuerst auf einer **Staging-Kopie** testen (STRATO bietet je nach Tarif Staging an, sonst eine lokale Kopie über die ai1wm-Datei).
3. Das Plugin „WordPress Importer“ installieren. Es ist ein offizielles WordPress.org-Plugin und **braucht deine Freigabe**, weil es eine Plugin-Installation ist. Nach dem Import kann es wieder deaktiviert werden.
4. Werkzeuge → Daten importieren → WordPress → `haydiweg-blog-entwuerfe.xml`. Autor zuordnen: den künftigen Autor wählen (Empfehlung: Profil „Hatice Köse“ statt „admin“). **Anhänge nicht importieren** (es sind keine enthalten).
5. Prüfen: Beiträge → Entwürfe. Alle Artikel sind als Entwurf vorhanden. In Rank Math stimmen Titel, Beschreibung und Fokus-Keyword.
6. Pro Artikel vor der Freigabe: Bilder einsetzen, `[PRÜFEN]` auflösen, Redaktionskästen entfernen, geplante Links prüfen. Dann **„Planen“** auf den Termin aus dem Kalender.
7. Nicht über den Import, sondern nur nach Freigabe: das Loop-Grid für neue Beiträge auf /reise-blog/ und der Startseite einbauen.

**Wichtig wegen Projekt 2 (SEO-Snippet):** Bevor der Snippet aus Projekt 2 aktiviert wird, muss an einem importierten Entwurf geprüft werden, dass er die Rank-Math-Titel der Beiträge **nicht überschreibt** (siehe SEO_ABSTIMMUNG_MIT_PROJEKT_2.md, Punkt 3.1).

## 5. Neu erzeugen

```bash
python3 haydiweg-blog/_arbeitsdaten/build_wxr.py   # nach jeder Änderung an BLOG_ARTIKEL/*.md
```
