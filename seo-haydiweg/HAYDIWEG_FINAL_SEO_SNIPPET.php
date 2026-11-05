<?php
/**
 * ============================================================================
 *  haydi-weg – Seitenspezifische SEO-Titel & Meta-Descriptions
 *  für Rank Math PRO (Stand: 05.11.2026)
 * ============================================================================
 *
 *  WAS DIESER SNIPPET TUT
 *  - Ersetzt für die unten konfigurierten Seiten-IDs den <title> und die
 *    <meta name="description">, die Rank Math PRO ausgibt.
 *  - Nutzt dafür ausschließlich die offiziellen Rank-Math-Filter
 *    "rank_math/frontend/title" und "rank_math/frontend/description"
 *    (im Rank-Math-Quellcode geprüft: includes/frontend/paper/class-paper.php).
 *  - og:title / twitter:title / og:description übernehmen den neuen Wert
 *    automatisch, solange im Rank-Math-Reiter "Social" nichts Eigenes
 *    eingetragen ist. Eigene Social-Texte bleiben unangetastet.
 *
 *  WAS DIESER SNIPPET BEWUSST NICHT TUT
 *  - Keine eigenen <title>- oder <meta>-Tags ausgeben (=> keine Duplikate).
 *  - Keine Änderung an Canonical, robots/noindex, Schema, Sitemap, Breadcrumbs.
 *  - Keine Ausgabepufferung / kein Umschreiben der HTML-Ausgabe.
 *  - Nichts im Backend, in Elementor, in REST/AJAX, Feeds oder der Buchungs-IBE.
 *  - Ist Rank Math deaktiviert, passiert gar nichts (die Filter feuern nicht).
 *
 *  SICHERHEITSMECHANISMEN
 *  1. Modus-Schalter: 'off' | 'preview' | 'live' (Standard: 'preview').
 *     'preview' wirkt NUR für eingeloggte Administratoren und NUR mit
 *     ?hw_seo_preview=1 in der URL. Besucher und Google sehen nichts davon.
 *  2. Jede Seiten-ID ist zusätzlich an ihren URL-Pfad gebunden. Passt die
 *     ID nicht mehr zum Pfad (Seite verschoben/gelöscht/ID neu vergeben),
 *     wird der Eintrag ignoriert und Rank Math bleibt maßgeblich.
 *  3. Leere oder ungültige Werte => Rank-Math-Wert bleibt erhalten.
 *  4. Seiten ohne Eintrag (z. B. neue Seiten) => Rank Math bleibt maßgeblich
 *     (Fallback). Optional wird nur das veraltete Suffix
 *     " - haydi-weg ☀ Urlaub leicht gemacht" in " | haydi-weg" umgewandelt.
 *  5. Ab Seite 2 einer Paginierung (/page/2/) greift kein Override.
 *
 *  PLATZHALTER
 *  {saison} = kommende Reisesaison. Januar–August: aktuelles Jahr,
 *             ab September: Folgejahr (am 05.11.2026 also "2027").
 *
 *  INSTALLATION (Plugin "Code Snippets" oder "WPCode")
 *  - Neuen PHP-Snippet anlegen, Inhalt ab der Zeile NACH "<?php" einfügen,
 *    "Nur im Frontend ausführen" (Code Snippets: "Only run on site front-end")
 *    wählen, speichern und aktivieren. Modus bleibt zunächst 'preview'.
 *  - Details: SEO_TEST_UND_ROLLBACK.md
 *
 *  ROLLBACK
 *  - Sofort: Snippet deaktivieren ODER 'mode' => 'off' setzen.
 *    Danach WP Rocket → "Cache leeren".
 *
 *  KOMPATIBILITÄT
 *  - PHP 7.4 bis 8.4 (Live-Server: PHP 8.4.27), WordPress ab 5.9,
 *    Rank Math (Free/PRO) ab 1.0.200, Elementor 4.x, WP Rocket 3.x.
 * ============================================================================
 */

if ( ! defined( 'ABSPATH' ) ) {
	return; // Kein direkter Aufruf.
}

if ( ! function_exists( 'hw_seo_settings' ) ) :

	/**
	 * Zentrale Einstellungen.
	 *
	 * @return array
	 */
	function hw_seo_settings() {
		return array(
			// 'off'     = Snippet komplett wirkungslos.
			// 'preview' = nur Admins mit ?hw_seo_preview=1 sehen die neuen Werte.
			// 'live'    = für alle Besucher und Suchmaschinen aktiv.
			'mode'              => 'preview',

			// Veraltetes Suffix " - haydi-weg ☀ Urlaub leicht gemacht" bei Seiten
			// OHNE eigenen Eintrag in " | haydi-weg" umwandeln (z. B. Archive, Suche).
			'fix_legacy_suffix' => true,
		);
	}

	/**
	 * Konfiguration: Seiten-ID => Pfad, Titel, Description.
	 * 'title' oder 'description' leer lassen ('') = Rank-Math-Wert behalten.
	 * Texte als normalen Text schreiben (& statt &amp;) – Rank Math escaped selbst.
	 *
	 * @return array
	 */
	function hw_seo_overrides() {
		return array(
			'post' => array(

				// ---- Startseite ----
				// Vorher: Urlaub online buchen mit Beratung | haydi-weg Reisebüro
				982 => array(
					'path'        => '/',
					'title'       => 'Urlaub buchen mit persönlicher Beratung | haydi-weg',
					'description' => 'Urlaub online buchen oder persönlich planen: per WhatsApp oder im Reisebüro in Minden. Türkei-Spezialist seit 2014, Hotels selbst gefilmt, 5,0 bei Google.',
				),

				// ---- Buchungsseite (IBE) ----
				// Vorher: Reise suchen und online buchen | haydi-weg
				6793 => array(
					'path'        => '/buchen/',
					'title'       => 'Reise online buchen: Veranstalter vergleichen | haydi-weg',
					'description' => 'Pauschalreisen und Last-Minute-Angebote vieler Veranstalter vergleichen und direkt online buchen. Ab 700 € Reisepreis gibt es 30 bis 1.000 € Cashback.',
				),

				// ---- Cashback-Informationsseite ----
				// Vorher: Bis zu 1.000 € Cashback auf deine Online-Buchung | haydi-weg
				7365 => array(
					'path'        => '/cashback/',
					'title'       => 'Urlaub mit Cashback: 30 bis 1.000 € zurück | haydi-weg',
					'description' => 'Online auf haydiweg.de buchen und nach der Rückreise 30 bis 1.000 € zurückbekommen, ohne Gutscheincode. Alle Stufen ab 700 € Reisepreis im Überblick.',
				),

				// ---- Kontaktseite ----
				// Vorher: Kontakt: WhatsApp, E-Mail & Reisebüro Minden | haydi-weg
				1379 => array(
					'path'        => '/kontakt/',
					'title'       => 'Kontakt: WhatsApp, Termin & Reisebüro Minden | haydi-weg',
					'description' => 'Schreib uns per WhatsApp, buch einen Beratungstermin oder komm ins Reisebüro in der Königstraße 52 in Minden. Mo–Fr 14–19 Uhr, Sa 10–15 Uhr.',
				),

				// ---- Lokale Reisebüroseite ----
				// Vorher: Reisebüro Minden: Urlaub persönlich planen | haydi-weg
				2941 => array(
					'path'        => '/reisebuero-minden-urlaub-buchen/',
					'title'       => 'Reisebüro Minden: persönliche Beratung seit 2014 | haydi-weg',
					'description' => 'Reisebüro haydi-weg, Königstraße 52 in Minden: persönliche Urlaubsberatung seit 2014, Hotels selbst gefilmt, 5,0 bei Google. Mo–Fr 14–19, Sa 10–15 Uhr.',
				),

				// ---- Angebots-/Themenseite ----
				// Vorher: Pauschalreise buchen: Flug & Hotel | haydi-weg
				2002 => array(
					'path'        => '/pauschalreisen/',
					'title'       => 'Pauschalreisen buchen: Flug, Hotel & Transfer | haydi-weg',
					'description' => 'Pauschalreisen vieler Veranstalter vergleichen: Flug, Hotel und Transfer im Paket, mit gesetzlicher Insolvenzabsicherung. Online buchen oder beraten lassen.',
				),
				// Vorher: Last Minute Urlaub buchen – kurzfristig weg | haydi-weg
				1431 => array(
					'path'        => '/last-minute-urlaub/',
					'title'       => 'Last Minute Urlaub: kurzfristig & ehrlich beraten | haydi-weg',
					'description' => 'Kurzfristig in die Sonne: Last-Minute-Reisen vieler Veranstalter mit Abflug in den nächsten Wochen. Wir sagen dir ehrlich, ob das günstige Hotel passt.',
				),

				// ---- Hotel-Übersicht (Hub) ----
				// Vorher: Türkei-Hotelvideos & eigene Eindrücke | haydi-weg
				613 => array(
					'path'        => '/urlaub-empfehlungen/',
					'title'       => 'Türkei-Hotels im Video: selbst besucht | haydi-weg',
					'description' => 'Türkei-Hotels im Video: eigene Eindrücke statt Katalogtext, sortiert nach Region und Urlaubsart. Hotel gefunden? Per WhatsApp fragen oder online buchen.',
				),

				// ---- Zielgebiets-Hub ----
				// Vorher: Urlaubsziele weltweit: Reisezeit & Tipps | haydi-weg
				1771 => array(
					'path'        => '/urlaubsziele/',
					'title'       => 'Urlaubsziele: 30 Länder mit Reisezeit & Flugzeit | haydi-weg',
					'description' => 'Von der Türkei bis in die Karibik: 30 Urlaubsziele mit Flugzeit, bester Reisezeit und ehrlicher Einordnung. Finde dein Ziel und buche online oder mit Beratung.',
				),

				// ---- Zielgebietsseite ----
				// Vorher: Türkei Urlaub buchen – All Inclusive & Regionen | haydi-weg
				2012 => array(
					'path'        => '/urlaubsziele/tuerkei-urlaub-buchen/',
					'title'       => 'Türkei Urlaub {saison}: All Inclusive, Regionen & Hotels | haydi-weg',
					'description' => 'Side, Alanya, Belek oder Kemer? Regionen, beste Reisezeit und All Inclusive im Überblick, dazu 14 Hotels, die wir selbst getestet haben.',
				),
				// Vorher: Ägypten Urlaub buchen – Hurghada & Rotes Meer | haydi-weg
				2022 => array(
					'path'        => '/urlaubsziele/aegypten-urlaub-buchen/',
					'title'       => 'Ägypten Urlaub {saison}: Hurghada & All Inclusive | haydi-weg',
					'description' => 'Hurghada, Makadi Bay oder Marsa Alam? Regionen, beste Reisezeit und was All Inclusive am Roten Meer kostet. Online buchen oder beraten lassen.',
				),
				// Vorher: Griechenland Urlaub buchen – Inseln & Reisezeit | haydi-weg
				2014 => array(
					'path'        => '/urlaubsziele/griechenland-urlaub-buchen/',
					'title'       => 'Griechenland Urlaub {saison}: Inseln im Vergleich | haydi-weg',
					'description' => 'Kreta, Rhodos, Kos oder Korfu? Inseln, beste Reisezeit und All-Inclusive-Preise in Griechenland im Überblick. Online buchen oder persönlich beraten lassen.',
				),
				// Vorher: Spanien Urlaub buchen – Mallorca & Kanaren | haydi-weg
				2018 => array(
					'path'        => '/urlaubsziele/spanien-urlaub-buchen/',
					'title'       => 'Spanien Urlaub {saison}: Mallorca & Kanaren | haydi-weg',
					'description' => 'Balearen im Sommer, Kanaren im Winter: Regionen, beste Reisezeit und All-Inclusive-Preise in Spanien. Online buchen oder persönlich beraten lassen.',
				),
				// Vorher: Dubai Urlaub buchen – Stadt & Strand | haydi-weg
				2028 => array(
					'path'        => '/urlaubsziele/dubai-urlaub-buchen/',
					'title'       => 'Dubai Urlaub: Stadt, Strand & beste Reisezeit | haydi-weg',
					'description' => 'Stadt und Strand in einer Reise: Emirate, Viertel und Hotels, dazu die beste Reisezeit von November bis April. Dubai Urlaub online buchen oder beraten lassen.',
				),
				// Vorher: Malediven Urlaub buchen – Insel & Resort finden | haydi-weg
				2024 => array(
					'path'        => '/urlaubsziele/malediven-urlaub-buchen/',
					'title'       => 'Malediven Urlaub: Insel & Resort richtig wählen | haydi-weg',
					'description' => 'Auf den Malediven entscheidet die Insel: Hausriff, Transfer und Verpflegung im Vergleich, dazu die beste Reisezeit. Ideal auch für die Hochzeitsreise.',
				),
				// Vorher: Dominikanische Republik Urlaub buchen | haydi-weg
				2020 => array(
					'path'        => '/urlaubsziele/dom-republik-urlaub-buchen/',
					'title'       => 'Dominikanische Republik: Urlaub & Reisezeit | haydi-weg',
					'description' => 'Karibik mit All Inclusive: Punta Cana und weitere Regionen, beste Reisezeit und Preise für deinen Urlaub in der Dominikanischen Republik. Online buchen.',
				),
				// Vorher: Zypern Urlaub buchen – Strände & Reisezeit | haydi-weg
				2026 => array(
					'path'        => '/urlaubsziele/zypern-urlaub-buchen/',
					'title'       => 'Zypern Urlaub: Strände, Regionen & Reisezeit | haydi-weg',
					'description' => 'Baden von April bis November: Zyperns Küstenabschnitte, beste Reisezeit und All-Inclusive-Preise im Überblick. Online buchen oder persönlich beraten lassen.',
				),
				// Vorher: Kroatien Urlaub buchen – Küste & Inseln | haydi-weg
				2016 => array(
					'path'        => '/urlaubsziele/kroatien-urlaub-buchen/',
					'title'       => 'Kroatien Urlaub: Küste, Inseln & Reisezeit | haydi-weg',
					'description' => '',
				),
				// Vorher: Italien Urlaub buchen – Sardinien & Sizilien | haydi-weg
				7250 => array(
					'path'        => '/urlaubsziele/italien-urlaub-buchen/',
					'title'       => 'Italien Urlaub: Sardinien & Sizilien im Vergleich | haydi-weg',
					'description' => '',
				),
				// Vorher: Portugal Urlaub buchen – Algarve & Madeira | haydi-weg
				7251 => array(
					'path'        => '/urlaubsziele/portugal-urlaub-buchen/',
					'title'       => 'Portugal Urlaub: Algarve & Madeira im Vergleich | haydi-weg',
					'description' => '',
				),
				// Vorher: Malta Urlaub buchen – Valletta & Gozo | haydi-weg
				7241 => array(
					'path'        => '/urlaubsziele/malta-urlaub-buchen/',
					'title'       => 'Malta Urlaub: Valletta, Gozo & beste Reisezeit | haydi-weg',
					'description' => '',
				),
				// Vorher: Montenegro Urlaub buchen – Budva & Kotor | haydi-weg
				7233 => array(
					'path'        => '/urlaubsziele/montenegro-urlaub-buchen/',
					'title'       => 'Montenegro Urlaub: Budva, Kotor & Reisezeit | haydi-weg',
					'description' => '',
				),
				// Vorher: Albanien Urlaub buchen – Riviera & Ksamil | haydi-weg
				7249 => array(
					'path'        => '/urlaubsziele/albanien-urlaub-buchen/',
					'title'       => 'Albanien Urlaub: Riviera, Ksamil & Reisezeit | haydi-weg',
					'description' => '',
				),
				// Vorher: Bulgarien Urlaub buchen – All Inclusive am Meer | haydi-weg
				7238 => array(
					'path'        => '/urlaubsziele/bulgarien-urlaub-buchen/',
					'title'       => 'Bulgarien All Inclusive: Urlaub am Schwarzen Meer | haydi-weg',
					'description' => '',
				),

				// ---- Ratgeber (Türkei) ----
				// Vorher: Beste Reisezeit für die Türkei: Klima & Wetter | haydi-weg
				5510 => array(
					'path'        => '/urlaubsziele/tuerkei-urlaub-buchen/beste-reisezeit-tuerkei/',
					'title'       => 'Beste Reisezeit Türkei: Klima & Wetter je Region | haydi-weg',
					'description' => '',
				),
				// Vorher: Istanbul: 12 Insidertipps für deinen Urlaub | haydi-weg
				4776 => array(
					'path'        => '/urlaubsziele/tuerkei-urlaub-buchen/istanbul-urlaub-insidertipps/',
					'title'       => 'Istanbul Insidertipps: 12 Tipps abseits der Massen | haydi-weg',
					'description' => '',
				),
				// Vorher: Istanbul: Die 10 schönsten Sehenswürdigkeiten | haydi-weg
				5525 => array(
					'path'        => '/urlaubsziele/tuerkei-urlaub-buchen/sehenswuerdigkeiten-in-istanbul/',
					'title'       => 'Sehenswürdigkeiten Istanbul: die 10 schönsten | haydi-weg',
					'description' => '',
				),

				// ---- Zielgebietsseite (Region) ----
				// Vorher: Urlaub in Side: Hotels, Ausflüge & Tipps | haydi-weg
				5134 => array(
					'path'        => '/tuerkei-urlaub-side/',
					'title'       => 'Side Urlaub: Hotels, Strände & Ausflüge | haydi-weg',
					'description' => 'Urlaub in Side an der Türkischen Riviera: antike Altstadt, Strände, Hotels und Resorts, Ausflüge und Tipps für die Planung – vom Türkei-Spezialisten.',
				),

				// ---- Themen-/Saisonseite ----
				// Vorher: Familienurlaub planen & buchen: Tipps für Eltern | haydi-weg
				5202 => array(
					'path'        => '/familienurlaub/',
					'title'       => 'Familienurlaub planen & buchen: Tipps & Ziele | haydi-weg',
					'description' => 'Familienurlaub entspannt planen: worauf du bei Ziel, Hotel und Flug achten solltest, Schritt für Schritt zur passenden Reise und Tipps für Ferien mit Kindern.',
				),
				// Vorher: Sommerurlaub All Inclusive: Ziele & Tipps | haydi-weg
				5098 => array(
					'path'        => '/sommerurlaub-all-inclusive/',
					'title'       => 'Sommerurlaub {saison} All Inclusive: Ziele & Tipps | haydi-weg',
					'description' => 'Sommerurlaub All Inclusive: was dich erwartet, beliebte Strandziele und Tipps zur Buchung. Wer früh plant, hat mehr Auswahl bei Zimmern und Flügen.',
				),
				// Vorher: Winterurlaub: Sonne oder Schnee – Ziele & Tipps | haydi-weg
				4966 => array(
					'path'        => '/winterurlaub/',
					'title'       => 'Winterurlaub {saison}: Sonne oder Schnee? | haydi-weg',
					'description' => 'Winterurlaub in der Sonne oder im Schnee: Reiseziele für die kalte Jahreszeit, Tipps zur Buchung und zur Ausrüstung. Online buchen oder beraten lassen.',
				),
				// Vorher: Urlaub über Weihnachten: Sonne oder Schnee | haydi-weg
				5362 => array(
					'path'        => '/urlaub-ueber-weihnachten/',
					'title'       => 'Urlaub über Weihnachten: Sonne oder Schnee? | haydi-weg',
					'description' => 'Weihnachten im Warmen oder im Schnee: Reiseziele für die Feiertage, Tipps für entspannte Festtage und Hilfe bei der Buchung, per WhatsApp oder im Büro.',
				),
				// Vorher: Herbstferien Urlaub: warme Ziele & Tipps | haydi-weg
				5395 => array(
					'path'        => '/herbstferien-urlaub/',
					'title'       => 'Herbstferien Urlaub: warme Ziele für Familien | haydi-weg',
					'description' => 'Wo es in den Herbstferien noch warm ist: Reiseziele, beste Reisezeit und Tipps für Familien. Angebote vergleichen und online buchen oder beraten lassen.',
				),
				// Vorher: Urlaub über Ostern: Reiseziele & Tipps | haydi-weg
				5441 => array(
					'path'        => '/ostern-urlaub/',
					'title'       => 'Osterurlaub {saison}: Reiseziele & Tipps | haydi-weg',
					'description' => 'Urlaub über Ostern: warum sich die Feiertage für eine Reise lohnen, beliebte Ziele für den Osterurlaub und Tipps zur Planung – frühzeitig buchen lohnt sich.',
				),
				// Vorher: Urlaub zu Pfingsten: Reiseziele & Tipps | haydi-weg
				5452 => array(
					'path'        => '/pfingsten-urlaub/',
					'title'       => 'Pfingsturlaub {saison}: Reiseziele & Tipps | haydi-weg',
					'description' => '',
				),
				// Vorher: Singlereisen: Reiseziele & Tipps für Solo-Urlaub | haydi-weg
				5227 => array(
					'path'        => '/singlereisen/',
					'title'       => 'Singlereisen buchen: Ziele für Alleinreisende | haydi-weg',
					'description' => 'Singlereisen buchen: welche Reiseziele sich allein lohnen, wie du passende Angebote ohne hohen Einzelzimmerzuschlag findest und wie wir dich beraten.',
				),
				// Vorher: Santorini Urlaub: Tipps für deine Reise | haydi-weg
				5118 => array(
					'path'        => '/santorini-urlaub/',
					'title'       => 'Santorini Urlaub planen: Tipps & Buchung | haydi-weg',
					'description' => '',
				),

				// ---- Monatsratgeber ----
				// Vorher: Reiseziele im Januar: Wohin im Winter? | haydi-weg
				4153 => array(
					'path'        => '/reisethemen/reiseziele-januar/',
					'title'       => 'Reiseziele im Januar: Wo ist es im Januar warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Februar: Wo es schon warm ist | haydi-weg
				4224 => array(
					'path'        => '/reisethemen/reiseziele-februar/',
					'title'       => 'Reiseziele im Februar: Wo ist es im Februar warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im März: 10 Ziele für den Frühling | haydi-weg
				4268 => array(
					'path'        => '/reisethemen/reiseziele-maerz/',
					'title'       => 'Reiseziele im März: Wo ist es im März warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im April: Strand, Natur & Kultur | haydi-weg
				4314 => array(
					'path'        => '/reisethemen/reiseziele-april/',
					'title'       => 'Reiseziele im April: Wo ist es im April warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Mai: Wo ist es im Mai warm? | haydi-weg
				4345 => array(
					'path'        => '/reisethemen/reiseziele-mai/',
					'title'       => 'Reiseziele im Mai: Wo ist es im Mai warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Juni: Ideen zum Sommerbeginn | haydi-weg
				4371 => array(
					'path'        => '/reisethemen/reiseziele-juni/',
					'title'       => 'Reiseziele im Juni: Strand, Städte & Abenteuer | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Juli: Ideen für den Sommerurlaub | haydi-weg
				4442 => array(
					'path'        => '/reisethemen/reiseziele-juli/',
					'title'       => 'Reiseziele im Juli: Strand, Natur & Städte | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im August: Ideen für den Hochsommer | haydi-weg
				4482 => array(
					'path'        => '/reisethemen/reiseziele-august/',
					'title'       => 'Reiseziele im August: Strand, Kultur & Natur | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im September: Urlaub im Spätsommer | haydi-weg
				4558 => array(
					'path'        => '/reisethemen/reiseziele-september/',
					'title'       => 'Reiseziele im September: Warm & weniger voll | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Oktober: Urlaub im Herbst | haydi-weg
				4587 => array(
					'path'        => '/reisethemen/reiseziele-oktober/',
					'title'       => 'Reiseziele im Oktober: Wo ist es im Oktober warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im November: Ideen für den Spätherbst | haydi-weg
				4621 => array(
					'path'        => '/reisethemen/reiseziele-november/',
					'title'       => 'Reiseziele im November: Wo ist es warm? | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Dezember: Ideen für den Winter | haydi-weg
				4637 => array(
					'path'        => '/reisethemen/reiseziele-dezember/',
					'title'       => 'Reiseziele im Dezember: Wo ist es warm? | haydi-weg',
					'description' => '',
				),

				// ---- Blogartikel ----
				// Vorher: Checkliste Urlaub: Packliste & Reisevorbereitung | haydi-weg
				4722 => array(
					'path'        => '/reise-blog/checkliste-urlaub/',
					'title'       => 'Checkliste Urlaub: Packliste & To-dos vor Abreise | haydi-weg',
					'description' => '',
				),
				// Vorher: Kurzurlaub-Ideen: Städtetrip, Natur & Wellness | haydi-weg
				3638 => array(
					'path'        => '/reise-blog/kurzurlaub-ideen/',
					'title'       => 'Kurzurlaub-Ideen fürs lange Wochenende | haydi-weg',
					'description' => '',
				),
				// Vorher: Reiseziele im Winter: warm, kühl oder exotisch | haydi-weg
				4039 => array(
					'path'        => '/reise-blog/reiseziele-im-winter/',
					'title'       => 'Warme Reiseziele im Winter & weitere Ideen | haydi-weg',
					'description' => '',
				),
				// Vorher: Sehenswürdigkeiten in der Türkei: Highlights | haydi-weg
				3434 => array(
					'path'        => '/reise-blog/sehenswuerdigkeiten-tuerkei/',
					'title'       => 'Sehenswürdigkeiten Türkei: Kappadokien bis Side | haydi-weg',
					'description' => 'Kappadokien, Pamukkale, Istanbul und die Riviera von Antalya bis Alanya: die schönsten Sehenswürdigkeiten der Türkei, mit Geheimtipps vom Spezialisten.',
				),

				// ---- Hotelseite (dünn, ohne Video) ----
				// Vorher: Hotel Acaplco - haydi-weg ☀ Urlaub leicht gemacht
				5644 => array(
					'path'        => '/hotel/hotel-acapulco-lloret/',
					'title'       => 'Hotel Acapulco Lloret de Mar: Angebote & Beratung | haydi-weg',
					'description' => 'Hotel Acapulco in Lloret de Mar an der Costa Brava: Angebote vieler Veranstalter vergleichen und persönlich beraten lassen, per WhatsApp oder in Minden.',
				),
				// Vorher: Hotel htop amatista - haydi-weg ☀ Urlaub leicht gemacht
				5633 => array(
					'path'        => '/hotel/hotel-htop-amatista/',
					'title'       => 'Hotel htop Amatista: Angebote & Beratung | haydi-weg',
					'description' => 'Hotel htop Amatista: aktuelle Angebote vieler Veranstalter vergleichen und persönlich beraten lassen – per WhatsApp oder im Reisebüro in Minden.',
				),
				// Vorher: L´Azure Hotel - haydi-weg ☀ Urlaub leicht gemacht
				5687 => array(
					'path'        => '/hotel/l-azure-hotel/',
					'title'       => 'L\'Azure Hotel: Angebote & Beratung | haydi-weg',
					'description' => 'L\'Azure Hotel: aktuelle Angebote vieler Veranstalter vergleichen und persönlich beraten lassen – per WhatsApp oder im Reisebüro in Minden.',
				),

				// ---- VORBEREITET, noch deaktiviert: erst nach Inhalts-Update auf {saison} einkommentieren ----
				// Vorher: Beste Reiseziele 2024 - Inspiration & Urlaubstipps ✅
				// 2811 => array( 'path' => '/reise-blog/beste-reiseziele-2024/', 'title' => 'Beste Reiseziele {saison}: 9 Ziele & Reisezeit | haydi-weg', 'description' => 'Wohin geht es {saison}? Neun Reiseziele von der Türkei über Griechenland bis Dubai und Malediven – mit bester Reisezeit und Tipps aus dem Reisebüro.' ),
			),
			'term' => array(

				// ---- Kategorie-Archiv ----
				// Vorher: Türkei - haydi-weg ☀ Urlaub leicht gemacht
				35 => array(
					'path'        => '/category/tuerkei/',
					'title'       => 'Türkei-Ratgeber: Hotels & Tipps | haydi-weg',
					'description' => 'Alle Beiträge zur Türkei: Hotelvergleiche, Familienhotels mit Aquapark und Tipps für deinen Urlaub an der Türkischen Riviera.',
				),
			),
		);
	}

	/**
	 * Kommende Reisesaison für den Platzhalter {saison}.
	 *
	 * @return string
	 */
	function hw_seo_season() {
		$year  = (int) wp_date( 'Y' );
		$month = (int) wp_date( 'n' );
		return (string) ( $month >= 9 ? $year + 1 : $year );
	}

	/**
	 * Ist der Snippet für diesen Request aktiv?
	 *
	 * @return bool
	 */
	function hw_seo_is_active() {
		static $active = null;
		if ( null !== $active ) {
			return $active;
		}
		$active = false;

		if ( is_admin() || wp_doing_ajax() || wp_doing_cron() || is_feed() || is_embed() ) {
			return $active;
		}
		if ( ( defined( 'REST_REQUEST' ) && REST_REQUEST ) || ( defined( 'XMLRPC_REQUEST' ) && XMLRPC_REQUEST ) ) {
			return $active;
		}
		if ( isset( $_GET['elementor-preview'] ) || is_customize_preview() ) { // phpcs:ignore WordPress.Security.NonceVerification
			return $active;
		}

		$settings = hw_seo_settings();
		$mode     = isset( $settings['mode'] ) ? (string) $settings['mode'] : 'off';

		if ( 'live' === $mode ) {
			$active = true;
		} elseif ( 'preview' === $mode ) {
			$active = isset( $_GET['hw_seo_preview'] ) // phpcs:ignore WordPress.Security.NonceVerification
				&& is_user_logged_in()
				&& current_user_can( 'manage_options' );
		}

		return $active;
	}

	/**
	 * Pfad normalisieren: "/foo/bar" => "/foo/bar/".
	 *
	 * @param string $path Pfad.
	 * @return string
	 */
	function hw_seo_normalize_path( $path ) {
		$path = '/' . trim( (string) $path, '/' ) . '/';
		return ( '//' === $path ) ? '/' : strtolower( $path );
	}

	/**
	 * Eintrag für die aktuell aufgerufene Seite ermitteln (oder null).
	 *
	 * @return array|null
	 */
	function hw_seo_current_entry() {
		static $entry = false;
		if ( false !== $entry ) {
			return $entry;
		}
		$entry = null;

		if ( ! hw_seo_is_active() || is_paged() || is_search() || is_404() ) {
			return $entry;
		}

		$config = hw_seo_overrides();
		$link   = '';
		$item   = null;

		if ( is_front_page() && 'page' === get_option( 'show_on_front' ) ) {
			$id = (int) get_option( 'page_on_front' );
			if ( $id && isset( $config['post'][ $id ] ) ) {
				$item = $config['post'][ $id ];
				$link = get_permalink( $id );
			}
		} elseif ( is_singular() ) {
			$id = (int) get_queried_object_id();
			if ( $id && isset( $config['post'][ $id ] ) ) {
				$item = $config['post'][ $id ];
				$link = get_permalink( $id );
			}
		} elseif ( is_category() || is_tag() || is_tax() ) {
			$term = get_queried_object();
			if ( $term instanceof WP_Term && isset( $config['term'][ (int) $term->term_id ] ) ) {
				$item = $config['term'][ (int) $term->term_id ];
				$link = get_term_link( $term );
			}
		}

		if ( ! is_array( $item ) || ! is_string( $link ) || '' === $link || empty( $item['path'] ) ) {
			return $entry;
		}

		// Sicherung: ID muss noch zum erwarteten Pfad passen (relativ zur Startseite,
		// funktioniert daher auch bei WordPress in einem Unterverzeichnis).
		$actual = hw_seo_normalize_path( (string) wp_parse_url( $link, PHP_URL_PATH ) );
		$base   = hw_seo_normalize_path( (string) wp_parse_url( home_url( '/' ), PHP_URL_PATH ) );
		if ( '/' !== $base && 0 === strpos( $actual, $base ) ) {
			$actual = hw_seo_normalize_path( substr( $actual, strlen( $base ) - 1 ) );
		}
		if ( hw_seo_normalize_path( $item['path'] ) !== $actual ) {
			return $entry;
		}

		$entry = $item;
		return $entry;
	}

	/**
	 * Text bereinigen und Platzhalter ersetzen. Gibt '' zurück, wenn unbrauchbar.
	 *
	 * @param mixed $text Rohtext.
	 * @return string
	 */
	function hw_seo_clean( $text ) {
		if ( ! is_string( $text ) ) {
			return '';
		}
		$text = str_replace( '{saison}', hw_seo_season(), $text );
		$text = wp_strip_all_tags( $text, true );
		$text = html_entity_decode( $text, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
		$text = trim( preg_replace( '/\s+/u', ' ', $text ) );
		return $text;
	}

	/**
	 * Filter: SEO-Titel.
	 *
	 * @param string $title Titel von Rank Math.
	 * @return string
	 */
	function hw_seo_filter_title( $title ) {
		if ( ! hw_seo_is_active() ) {
			return $title;
		}
		$entry = hw_seo_current_entry();
		if ( $entry && ! empty( $entry['title'] ) ) {
			$new = hw_seo_clean( $entry['title'] );
			if ( '' !== $new ) {
				return $new;
			}
		}

		$settings = hw_seo_settings();
		if ( ! empty( $settings['fix_legacy_suffix'] ) && is_string( $title ) ) {
			$fixed = preg_replace( '/\s+[-–|]\s+haydi-weg\s*☀\s*Urlaub leicht gemacht\s*$/u', ' | haydi-weg', $title );
			if ( is_string( $fixed ) && '' !== trim( $fixed ) ) {
				return $fixed;
			}
		}
		return $title;
	}

	/**
	 * Filter: Meta-Description.
	 *
	 * @param string $description Description von Rank Math.
	 * @return string
	 */
	function hw_seo_filter_description( $description ) {
		if ( ! hw_seo_is_active() ) {
			return $description;
		}
		$entry = hw_seo_current_entry();
		if ( $entry && ! empty( $entry['description'] ) ) {
			$new = hw_seo_clean( $entry['description'] );
			if ( '' !== $new ) {
				return $new;
			}
		}
		return $description;
	}

	/**
	 * Im Vorschau-Modus: unsichtbarer HTML-Kommentar im <head> (nur für Admins),
	 * damit man im Quelltext sieht, ob ein Eintrag gegriffen hat.
	 */
	function hw_seo_preview_marker() {
		$settings = hw_seo_settings();
		if ( 'preview' !== $settings['mode'] || ! hw_seo_is_active() ) {
			return;
		}
		$entry = hw_seo_current_entry();
		echo "\n<!-- hw-seo preview: " . ( $entry ? 'Eintrag aktiv fuer ' . esc_html( $entry['path'] ) : 'kein Eintrag, Rank-Math-Wert' ) . " -->\n";
	}

	/**
	 * Hinweis im Backend: Modus anzeigen und fehlendes Rank Math melden.
	 */
	function hw_seo_admin_notice() {
		if ( ! current_user_can( 'manage_options' ) ) {
			return;
		}
		$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;
		if ( $screen && ! in_array( $screen->id, array( 'dashboard', 'plugins', 'snippets', 'code-snippets', 'toplevel_page_snippets' ), true ) ) {
			return;
		}
		$settings = hw_seo_settings();
		if ( ! defined( 'RANK_MATH_VERSION' ) ) {
			echo '<div class="notice notice-warning"><p><strong>haydi-weg SEO-Snippet:</strong> Rank Math ist nicht aktiv – der Snippet ist wirkungslos.</p></div>';
		} elseif ( 'preview' === $settings['mode'] ) {
			echo '<div class="notice notice-info"><p><strong>haydi-weg SEO-Snippet:</strong> Vorschau-Modus. Testen mit <code>?hw_seo_preview=1</code> an einer Seiten-URL (nur als Admin sichtbar).</p></div>';
		}
	}

	add_filter( 'rank_math/frontend/title', 'hw_seo_filter_title', 20 );
	add_filter( 'rank_math/frontend/description', 'hw_seo_filter_description', 20 );
	add_action( 'wp_head', 'hw_seo_preview_marker', 0 );
	add_action( 'admin_notices', 'hw_seo_admin_notice' );

endif;
