# LTX-2 MCP Server per Claude

Genera video con LTX-2 direttamente dalla chat di Claude (Claude Code / Claude Desktop).

## Setup Rapido

1. Copia `.env.example` in `.env` e inserisci la tua API key LTX-2
2. Installa dipendenze: `pip install -r requirements.txt`
3. Registra in Claude Code: `claude mcp add ltx-video -- python src/ltx_mcp_server.py`
4. Chiedi a Claude di generare un video!

## Come ottenere la API key

1. Vai su https://console.ltx.video/
2. Crea un account
3. Genera una API key
4. Compra crediti (pay-per-use)

## Pricing

| Modello | 1080p | 1440p | 4K |
|---------|-------|-------|-----|
| ltx-2-fast | $0.04/s | $0.08/s | $0.16/s |
| ltx-2-pro | $0.06/s | $0.12/s | $0.24/s |

Esempio: video 10s 1080p fast = **$0.40**

## Tools disponibili

- **text_to_video** — Genera video da testo
- **image_to_video** — Anima un'immagine
- **audio_to_video** — Video sincronizzato ad audio

## Struttura

```
ltxintegration/
├── src/
│   └── ltx_mcp_server.py    ← Server MCP (da creare con Claude Code)
├── outputs/                  ← Video generati
├── PROJECT_SPEC.md           ← Specifica progetto
├── API_REFERENCE.md          ← Documentazione API
├── CLAUDE_CODE_INSTRUCTIONS.md ← Istruzioni per Claude Code
├── .env.example              ← Template env
├── requirements.txt          ← Dipendenze
└── README.md                 ← Questo file
```
