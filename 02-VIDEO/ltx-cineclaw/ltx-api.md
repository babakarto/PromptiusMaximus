# LTX-2 API Reference

## Authentication

API key from environment variable `LTX_API_KEY`.
Get your key at: https://console.ltx.video

## Base URL

```
https://api.ltx.video/v1
```

## Endpoints

### Text-to-Video
```
POST /generations/text-to-video
```

Parameters:
- `prompt` (string, required) — Video description
- `model` (string) — `ltx-2-fast` or `ltx-2-pro` (default: `ltx-2-fast`)
- `resolution` (string) — `1920x1080`, `2560x1440`, `3840x2160` (default: `1920x1080`)
- `duration` (int) — Seconds. Fast@1080p: 6-20. Pro: 6-10. (default: 6)
- `fps` (int) — 25 or 50 (default: 25)
- `seed` (int, optional) — For reproducibility

### Image-to-Video
```
POST /generations/image-to-video
```

Parameters:
- `prompt` (string, required) — Motion/animation description
- `image` (file or URL, required) — Start image (jpg, png, webp, gif)
- `model` (string) — `ltx-2-fast` or `ltx-2-pro`
- `resolution` (string) — `1920x1080`, `2560x1440`, `3840x2160`
- `duration` (int) — 6-10 seconds
- `fps` (int) — 25 or 50
- `seed` (int, optional)

### Audio-to-Video
```
POST /generations/audio-to-video
```

Parameters:
- `prompt` (string, required) — Visual scene description
- `audio` (file or URL, required) — Audio file (mp3, wav, ogg, m4a, aac)
- `model` (string) — **Only `ltx-2-pro` supported**
- `resolution` (string) — `1920x1080` only for A2V

## Response Format

```json
{
  "id": "gen_abc123",
  "status": "completed",
  "video_url": "https://cdn.ltx.video/...",
  "duration": 6,
  "model": "ltx-2-fast",
  "resolution": "1920x1080",
  "cost": 0.12
}
```

Async: if `status` is `processing`, poll with:
```
GET /generations/{id}
```

## Pricing (per second of video)

| Model | 1080p | 1440p | 4K |
|-------|-------|-------|-----|
| ltx-2-fast | ~$0.02 | ~$0.04 | ~$0.08 |
| ltx-2-pro | ~$0.05 | ~$0.10 | ~$0.20 |

Typical costs:
- 6s fast 1080p ≈ $0.12
- 10s fast 1080p ≈ $0.20
- 6s pro 1080p ≈ $0.30
- 6s pro 4K ≈ $1.20

Monitor balance at console.ltx.video.

## Models

| Model | Parameters | Speed | Quality | Notes |
|-------|-----------|-------|---------|-------|
| ltx-2-fast | 19B (distilled) | ~5-15s | Good | Best for drafts, iteration |
| ltx-2-pro | 19B (full) | ~30-90s | Cinematic | Best for final output, A2V |

## Technical Constraints

- **Resolution:** Width and height must be divisible by 32
- **Frame count:** Must be divisible by 8 + 1 (9, 17, 25...)
- **Duration limits:**
  - ltx-2-fast @ 1080p/25fps: 6-20 seconds
  - ltx-2-pro: 6-10 seconds
- **A2V:** Only ltx-2-pro, only 1920x1080
- **CFG Scale:** 1.0 recommended for distilled model

## Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Bad request / invalid params | Check resolution divisible by 32, valid model name |
| 401 | Invalid API key | Check LTX_API_KEY environment variable |
| 402 | Insufficient credits | Add credits at console.ltx.video |
| 413 | File too large | Compress image/audio before upload |
| 422 | Invalid file format | Check supported formats (jpg/png/webp/gif, mp3/wav/ogg) |
| 429 | Rate limited | Wait 60 seconds and retry |
| 500 | Server error | Wait 5 min and retry once |
| 503 | Service unavailable | API down, wait and retry |

## Rate Limits

Standard tier: 10 concurrent requests, 100 requests per minute.
If rate limited, `Retry-After` header indicates when to retry.

## File Requirements

### Images (I2V)
- Formats: jpg, jpeg, png, webp, gif
- Max size: 20MB
- Recommended: match target aspect ratio

### Audio (A2V)
- Formats: mp3, wav, ogg, m4a, aac
- Max size: 50MB
- Max duration: matches video duration setting
- Best results: isolated vocals for lip sync, clean audio

## Platforms Running LTX-2

- [LTX Studio](https://ltx.studio) — official web platform
- [WaveSpeed AI](https://wavespeed.ai) — API
- [APIFree](https://www.apifree.ai) — API
- [GamerHash AI](https://gamerhash.com) — local GPU
- [ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo) — local workflows
- [Pinokio](https://pinokio.computer) — local, beginner-friendly
