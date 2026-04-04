# LTX-2 API Reference (Ufficiale docs.ltx.video)

## Base URL
```
https://api.ltx.video
```

## Autenticazione
Header `Authorization: Bearer YOUR_API_KEY` su ogni richiesta.
API key si crea su https://console.ltx.video/

## IMPORTANTE: Risposta Sincrona
L'API restituisce il file video MP4 DIRETTAMENTE nel body della risposta.
NON è asincrona, NON c'è polling. La richiesta resta aperta finché il video non è pronto.
- Headers risposta: `Content-Type: video/mp4`, `x-request-id: <tracking_id>`
- Il timeout può essere lungo (1-3 minuti) — usare timeout generosi nelle chiamate HTTP.

---

## Endpoint 1: Text-to-Video

```
POST /v1/text-to-video
```

### Parametri (JSON body)

| Parametro | Tipo | Required | Default | Descrizione |
|-----------|------|----------|---------|-------------|
| `prompt` | string | ✅ | — | Descrizione della scena (max 5000 chars) |
| `model` | enum | ✅ | — | `"ltx-2-fast"` o `"ltx-2-pro"` |
| `duration` | integer | ✅ | — | Durata in secondi |
| `resolution` | string | ✅ | — | Es. `"1920x1080"`, `"2560x1440"`, `"3840x2160"` |
| `fps` | integer | ❌ | 25 | 25 o 50 |
| `camera_motion` | enum | ❌ | — | Effetto camera opzionale |
| `generate_audio` | boolean | ❌ | true | Se generare audio sincronizzato (Beta) |

### Esempio cURL
```bash
curl -X POST https://api.ltx.video/v1/text-to-video \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A majestic eagle soaring through clouds at sunset",
    "model": "ltx-2-pro",
    "duration": 8,
    "resolution": "1920x1080"
  }' \
  -o video.mp4
```

### Esempio Python
```python
import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.ltx.video/v1/text-to-video",
    headers=headers,
    json={
        "prompt": "A majestic eagle soaring through clouds at sunset",
        "model": "ltx-2-pro",
        "duration": 8,
        "resolution": "1920x1080"
    },
    timeout=300  # 5 min timeout, la generazione può richiedere tempo
)

# La risposta è direttamente il file MP4
with open("video.mp4", "wb") as f:
    f.write(response.content)
```

---

## Endpoint 2: Image-to-Video

```
POST /v1/image-to-video
```

### Parametri (JSON body)

| Parametro | Tipo | Required | Default | Descrizione |
|-----------|------|----------|---------|-------------|
| `image_uri` | string | ✅ | — | URL HTTPS dell'immagine OPPURE base64 data URI |
| `prompt` | string | ✅ | — | Descrizione del movimento/animazione |
| `model` | enum | ✅ | — | `"ltx-2-fast"` o `"ltx-2-pro"` |
| `duration` | integer | ✅ | — | Durata in secondi |
| `resolution` | string | ✅ | — | Risoluzione output |
| `fps` | integer | ❌ | 25 | 25 o 50 |
| `generate_audio` | boolean | ❌ | true | Audio sincronizzato |

### Esempio
```bash
curl -X POST https://api.ltx.video/v1/image-to-video \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "image_uri": "https://example.com/sunset.jpg",
    "prompt": "Clouds drifting across the sky as the sun sets slowly",
    "model": "ltx-2-pro",
    "duration": 8,
    "resolution": "1920x1080"
  }' \
  -o video.mp4
```

Per immagini locali, usare base64 data URI:
```
"image_uri": "data:image/jpeg;base64,/9j/4AAQ..."
```

---

## Endpoint 3: Audio-to-Video

```
POST /v1/audio-to-video
```

Genera video sincronizzato all'audio. Solo modello `ltx-2-pro`.

---

## Endpoint 4: Retake (Video Editing)

```
POST /v1/retake
```

Edita e rigenera porzioni di un video esistente. Solo `ltx-2-pro`.

---

## Model Support Matrix

| Model | Resolution | FPS | Duration (secondi) |
|-------|-----------|-----|---------------------|
| ltx-2-fast | 1920x1080 | 25 | 6, 8, 10, 12, 14, 16, 18, 20 |
| ltx-2-fast | 1920x1080 | 50 | 6, 8, 10 |
| ltx-2-fast | 2560x1440 | 25, 50 | 6, 8, 10 |
| ltx-2-fast | 3840x2160 | 25, 50 | 6, 8, 10 |
| ltx-2-pro | 1920x1080 | 25, 50 | 6, 8, 10 |
| ltx-2-pro | 2560x1440 | 25, 50 | 6, 8, 10 |
| ltx-2-pro | 3840x2160 | 25, 50 | 6, 8, 10 |

**Nota:** `ltx-2-fast` a 1080p/25fps supporta durate fino a 20 secondi. Tutti gli altri combo max 10 secondi.

---

## Codici Errore

| Codice | Significato |
|--------|-------------|
| 400 | Bad Request — parametri non validi |
| 401 | Unauthorized — API key mancante o errata |
| 422 | Unprocessable Entity — combinazione parametri non supportata |
| 429 | Too Many Requests — rate limit raggiunto |
| 500 | Internal Server Error |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

---

## Pricing (per secondo di video output)

| Modello | 1080p | 1440p | 4K |
|---------|-------|-------|-----|
| ltx-2-fast | $0.04 | $0.08 | $0.16 |
| ltx-2-pro | $0.06 | $0.12 | $0.24 |
| audio-to-video (pro) | $0.10 | — | — |
| retake (pro) | $0.10 | — | — |
