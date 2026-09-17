const express = require("express");
const cors = require("cors");
const OpenAI = require("openai");

const app = express();
app.use(cors());
app.use(express.json({ limit: "25mb" }));

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

app.get("/", (req, res) => {
  res.json({ status: "ok" });
});

app.post("/api/ki-analyse", async (req, res) => {
  try {
    const { messages, image, imageMediaType } = req.body;
    const prompt = messages || "Analysiere dieses Dokument und extrahiere alle Buchhaltungsdaten.";

    const content = image
      ? [
          { type: "text", text: prompt },
          {
            type: "image_url",
            image_url: {
              url: `data:${imageMediaType || "image/jpeg"};base64,${image}`,
            },
          },
        ]
      : prompt;

    const response = await client.chat.completions.create({
      model: "gpt-4o",
      max_tokens: 1500,
      messages: [{ role: "user", content }],
    });

    res.json({
      success: true,
      message: response.choices[0].message.content,
    });
  } catch (error) {
    console.error("API Fehler:", error);
    res.status(500).json({ error: error.message });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Läuft auf Port ${port}`));
