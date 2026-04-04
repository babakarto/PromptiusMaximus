# Istruzioni per Claude Code

## Cosa deve fare Claude Code

Leggi PRIMA `PROJECT_SPEC.md` e `API_REFERENCE.md` nella stessa cartella — contengono tutte le specifiche del progetto e dell'API LTX-2.

Poi costruisci un MCP server Python usando FastMCP che wrappa l'API cloud LTX-2 per generare video dalla chat di Claude.

## Passi

### 1. Setup ambiente
```bash
cd C:\Users\prova\Desktop\ltxintegration
python -m venv .venv
.venv\Scripts\activate
pip install fastmcp httpx python-dotenv
```

### 2. Crea il server MCP (`src/ltx_mcp_server.py`)

Il server deve esporre 4 tools:
- `text_to_video` — genera video da prompt testuale
- `image_to_video` — anima un'immagine (supporta path locale → converte in base64)
- `audio_to_video` — genera video da audio
- `check_balance` — (opzionale) mostra crediti rimanenti se endpoint disponibile

**DETTAGLIO CRITICO:** L'API LTX-2 è **SINCRONA**. La risposta HTTP contiene direttamente il file MP4 nel body. Non c'è task_id, non c'è polling. Usare un timeout HTTP di almeno 300 secondi.

**Flusso per ogni tool:**
1. Leggere la API key da env `LTXV_API_KEY`
2. Validare i parametri (model, resolution, duration devono essere combinazioni supportate — vedi API_REFERENCE.md)
3. Fare POST a `https://api.ltx.video/v1/{endpoint}` con header `Authorization: Bearer {key}`
4. Attendere la risposta (può richiedere 1-3 minuti)
5. Salvare i bytes della risposta come `.mp4` nella cartella `outputs/`
6. Ritornare a Claude il path del file salvato + metadata utili (durata, modello, risoluzione, costo stimato)

**Per image_to_video con immagine locale:**
- Se `image_path` è un path locale (non URL), leggere il file, convertirlo in base64 data URI
- Formato: `data:image/{ext};base64,{base64_data}`
- Passare come campo `image_uri` nella richiesta API

### 3. Gestione errori
- Se API key non è settata → errore chiaro con istruzioni
- Se la risposta non è 200 → parsare il JSON errore e ritornare messaggio leggibile
- Se timeout → messaggio che spiega che la generazione è fallita per timeout
- Calcolo costo stimato: `duration * costo_per_secondo` basato su modello e risoluzione

### 4. Registrazione in Claude Code
Una volta completato il server, registrarlo con:
```bash
claude mcp add ltx-video -- python C:\Users\prova\Desktop\ltxintegration\src\ltx_mcp_server.py
```

Oppure per Claude Desktop, aggiungere a `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "ltx-video": {
      "command": "python",
      "args": ["C:\\Users\\prova\\Desktop\\ltxintegration\\src\\ltx_mcp_server.py"],
      "env": {
        "LTXV_API_KEY": "la_tua_key"
      }
    }
  }
}
```

### 5. Test
Testare con:
```
"Genera un video di 6 secondi di un'aquila che vola sopra le montagne al tramonto, modello fast, 1080p"
```

## File di riferimento nella cartella
- `PROJECT_SPEC.md` — Specifica completa del progetto
- `API_REFERENCE.md` — Documentazione API LTX-2 con tutti gli endpoint, parametri, e codici errore
- `.env.example` — Template per le variabili d'ambiente
- `requirements.txt` — Dipendenze Python
