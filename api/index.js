import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.OPENAI_API_KEY,
});

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Nur POST erlaubt" });
  }

  try {
    const { messages, image } = req.body;

    if (image) {
      const response = await client.messages.create({
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1024,
        messages: [
          {
            role: "user",
            content: [
              {
                type: "text",
                text: messages || "Analysiere dieses Dokument und extrahiere alle Buchhaltungsdaten",
              },
              {
                type: "image",
                source: {
                  type: "base64",
                  media_type: "image/jpeg",
                  data: image,
                },
              },
            ],
          },
        ],
      });

      return res.status(200).json({
        success: true,
        message: response.content[0].text,
      });
    }

    const response = await client.messages.create({
      model: "claude-3-5-sonnet-20241022",
      max_tokens: 1024,
      messages: [{ role: "user", content: messages }],
    });

    return res.status(200).json({
      success: true,
      message: response.content[0].text,
    });
  } catch (error) {
    console.error("API Fehler:", error);
    return res.status(500).json({
      error: error.message || "Unbekannter Fehler",
    });
  }
}
