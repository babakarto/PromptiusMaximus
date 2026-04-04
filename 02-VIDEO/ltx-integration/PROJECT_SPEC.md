# LTX-2 MCP Server — Project Specification

## Obiettivo
Creare un MCP (Model Context Protocol) server in Python con FastMCP che wrappa l'API cloud di LTX-2 (Lightricks), permettendo di generare video direttamente dalla chat di Claude (Claude Code o Claude Desktop).

## Architettura

```
User prompt in Claude
        ↓
   Claude chiama il tool MCP
        ↓
   MCP Server (Python/FastMCP)
        ↓
   POST a API LTX-2 (cloud, sui server Lightricks)
        ↓
   Attesa risposta sincrona (~1-3 min)
        ↓
   Risposta = file MP4 diretto → salva in cartella locale
        ↓
   Ritorna path del video a Claude
```

## Stack Tecnico
- **Python 3.12+**
- **FastMCP** (`pip install fastmcp`)
- **httpx** per le chiamate HTTP async
- **python-dotenv** per gestire la API key
- Il video viene generato sui server cloud LTX (H100), NON sulla GPU locale

## Tools MCP da Esporre

### 1. `text_to_video`
Genera un video da un prompt testuale.
- **Parametri:**
  - `prompt` (str, required): Descrizione della scena
  - `model` (str, default "ltx-2-fast"): "ltx-2-fast" o "ltx-2-pro"
  - `resolution` (str, default "1920x1080"): "1920x1080", "2560x1440", "3840x2160"
  - `duration` (int, default 6): Durata in secondi (6-20)
  - `fps` (int, default 25): Frame rate (25 o 50)
  - `seed` (int, optional): Seed per riproducibilità
- **Ritorna:** Path locale del video scaricato + URL di download

### 2. `image_to_video`
Anima un'immagine statica.
- **Parametri:**
  - `prompt` (str, required): Descrizione del movimento/animazione
  - `image_path` (str, required): Path locale dell'immagine di input
  - `model` (str, default "ltx-2-fast"): "ltx-2-fast" o "ltx-2-pro"
  - `resolution` (str, default "1920x1080")
  - `duration` (int, default 6)
  - `fps` (int, default 25)
  - `seed` (int, optional)
- **Ritorna:** Path locale del video + URL

### 3. `audio_to_video`
Genera video sincronizzato all'audio.
- **Parametri:**
  - `prompt` (str, required): Descrizione visiva
  - `audio_path` (str, required): Path locale del file audio
  - `model` (str, default "ltx-2-pro"): Solo "ltx-2-pro" supportato
  - `resolution` (str, default "1920x1080")
- **Ritorna:** Path locale del video + URL

### 4. `check_status`
Controlla lo stato di una generazione in corso.
- **Parametri:**
  - `task_id` (str, required)
- **Ritorna:** Stato attuale del task

## Configurazione

### File `.env`
```
LTXV_API_KEY=your_api_key_here
LTX_OUTPUT_DIR=./outputs
```

### Struttura Cartelle
```
ltxintegration/
├── PROJECT_SPEC.md          # Questa spec
├── API_REFERENCE.md          # Documentazione API LTX-2
├── CLAUDE_CODE_INSTRUCTIONS.md  # Istruzioni per Claude Code
├── src/
│   └── ltx_mcp_server.py    # Il server MCP principale
├── .env.example              # Template per le variabili d'ambiente
├── requirements.txt          # Dipendenze Python
├── outputs/                  # Cartella dove vengono salvati i video
└── README.md                 # Documentazione d'uso
```

## Flusso di Generazione (Dettaglio)

**IMPORTANTE: L'API è SINCRONA** — restituisce il file MP4 direttamente nel body della risposta HTTP.
Non c'è polling, non c'è task_id. La connessione resta aperta finché il video non è pronto (1-3 minuti tipicamente).

1. L'utente chiede a Claude di generare un video
2. Claude invoca il tool MCP appropriato (es. `text_to_video`)
3. Il server MCP:
   a. Valida i parametri
   b. Invia POST a `https://api.ltx.video/v1/text-to-video` con Bearer token
   c. Attende la risposta (timeout 300 secondi) — l'API restituisce direttamente il file MP4
   d. Salva il video in `outputs/` con nome `ltx_{timestamp}.mp4`
   e. Ritorna a Claude: path locale + metadata (durata, risoluzione, costo stimato)

## Gestione Errori
- Timeout HTTP dopo 5 minuti → errore con messaggio chiaro
- API key mancante → errore immediato con istruzioni
- Rate limit (429) → retry con backoff esponenziale
- Generazione fallita → riporta l'errore dell'API

## Integrazione con Claude Code
Una volta costruito, il server va registrato in Claude Code con:
```bash
claude mcp add ltx-video -- python src/ltx_mcp_server.py
```

Oppure per Claude Desktop, aggiungere in `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "ltx-video": {
      "command": "python",
      "args": ["C:\\Users\\prova\\Desktop\\ltxintegration\\src\\ltx_mcp_server.py"],
      "env": {
        "LTXV_API_KEY": "your_key_here"
      }
    }
  }
}
```

## Pricing Reminder
| Modello | 1080p | 1440p | 4K |
|---------|-------|-------|-----|
| ltx-2-fast | $0.04/s | $0.08/s | $0.16/s |
| ltx-2-pro | $0.06/s | $0.12/s | $0.24/s |
| audio-to-video | $0.10/s | — | — |

Esempio: video 10s 1080p fast = $0.40
