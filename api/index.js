const express = require("express");
const cors = require("cors");
const OpenAI = require("openai");

const app = express();
app.use(cors());
app.use(express.json({ limit: "25mb" }));

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.get("/", (req, res) => res.json({ status: "ok" }));

const PROMPT = `Du analysierst Airline-Rechnungen, Tickets und Reisebelege für ein Reisebüro.

Gib AUSSCHLIESSLICH ein JSON-Objekt zurück, ohne Markdown und ohne Erklärung, exakt in dieser Struktur:

{
  "gesamt_confidence": "hoch",
  "pnr": "",
  "airline": "",
  "buchungsstatus": "",
  "lieferant": "",
  "reisende": [
    {
      "anrede": "",
      "vorname": "",
      "nachname": "",
      "typ": "Erwachsener",
      "ticketnummer": "",
      "geburtsdatum": "",
      "gepaeck": "",
      "confidence": { "vorname": "hoch" }
    }
  ],
  "segmente": [
    {
      "abflughafen": "",
      "zielflughafen": "",
      "flugnummer": "",
      "abflugdatum": "",
      "abflugzeit": "",
      "ankunftsdatum": "",
      "ankunftszeit": "",
      "buchungsklasse": "",
      "status": "OK",
      "richtung": "Hinflug",
      "marketing_carrier": "",
      "operating_carrier": ""
    }
  ],
  "preise": [
    { "betrag": "", "preis_typ": "Gesamtpreis", "waehrung": "EUR", "confidence": "hoch" }
  ],
  "warnungen": []
}

ERLAUBTE WERTE - halte dich strikt daran:
- gesamt_confidence: "hoch" | "mittel" | "niedrig"
- richtung (Segment): "Hinflug" | "Rueckflug"
- status (Segment): "OK" | "Waitlist" | "Storniert"
- typ (Reisender): "Erwachsener" | "Kind" | "Kleinkind"
- preis_typ: "Gesamtpreis" | "Einkaufspreis" | "Verkaufspreis" | "Serviceentgelt" | "Steuer" | "Ignorieren"
- confidence (Preis): "hoch" | "mittel" | "niedrig" | "?"
- abflugdatum / ankunftsdatum: ISO-Format JJJJ-MM-TT, z.B. "2026-10-15"
- warnungen: Array aus Freitext-Strings, leer wenn keine

REGELN:
- Nicht erkennbare Felder als leeren String "" lassen, niemals erfinden.
- Bei unsicherer Zuordnung eines Preises confidence auf "?" setzen.
- Jeden Reisenden und jedes Flugsegment als eigenen Eintrag im Array.
- Auffälligkeiten (unleserliche PNR, fehlendes Rückflugsegment, widersprüchliche Beträge) in "warnungen" vermerken.
- Beträge mit deutschem Komma als Dezimaltrennzeichen, z.B. "1250,00".`;

app.post("/api/ki-analyse", async (req, res) => {
  try {
    const dateien = req.body.dateien || [];
    if (!dateien.length) {
      return res.status(400).json({ erfolg: false, fehler: "Keine Datei übergeben" });
    }

    const datei = dateien[0];

    const download = await fetch(datei.url);
    if (!download.ok) {
      return res.status(400).json({
        erfolg: false,
        fehler: `Datei konnte nicht geladen werden (HTTP ${download.status})`,
      });
    }

    const base64 = Buffer.from(await download.arrayBuffer()).toString("base64");
    const typ = datei.dateityp || "image/jpeg";

    const inhalt =
      typ === "application/pdf"
        ? [
            { type: "text", text: PROMPT },
            {
              type: "file",
              file: {
                filename: datei.dateiname || "beleg.pdf",
                file_data: `data:application/pdf;base64,${base64}`,
              },
            },
          ]
        : [
            { type: "text", text: PROMPT },
            { type: "image_url", image_url: { url: `data:${typ};base64,${base64}` } },
          ];

    const antwort = await client.chat.completions.create({
      model: "gpt-4o",
      max_tokens: 3000,
      response_format: { type: "json_object" },
      messages: [{ role: "user", content: inhalt }],
    });

    const daten = JSON.parse(antwort.choices[0].message.content);
    res.json({ erfolg: true, daten });
  } catch (error) {
    console.error("Analyse-Fehler:", error);
    res.status(500).json({ erfolg: false, fehler: error.message });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Läuft auf Port ${port}`));
