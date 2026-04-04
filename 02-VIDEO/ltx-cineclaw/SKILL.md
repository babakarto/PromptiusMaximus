---
name: cineclaw
description: >
  AI video generation skill for OpenClaw using LTX-2 API by Lightricks.
  Generates cinematic videos from text prompts, images, or audio.
  Use when: (1) user says "make a video", "generate video", "animate this",
  "text to video", "image to video", "audio to video", "cineclaw",
  (2) user wants to create social media content, ads, music videos, or
  cinematic clips, (3) user provides an image and wants it animated,
  (4) user provides audio and wants synced video.
  Supports: text-to-video (T2V), image-to-video (I2V), audio-to-video (A2V),
  camera presets, AI audio sync, prompt enhancement, cost estimation.
  NOT for: video editing, video trimming, adding subtitles, or screen recording.
---

# CineClaw — AI Video Generation

Generate cinematic AI videos from text, images, or audio via the LTX-2 API.

**This skill uses Python for all API calls — works on Windows, Mac, and Linux.**

For LTX-2 API details (endpoints, parameters, errors): read `references/ltx-api.md`.
For advanced prompting techniques and community tips: read `references/prompting-guide.md`.
For deep research on LTX-2 from X/Twitter community: read `references/ltx2-prompt-guide-advanced.md`.

## Important: Cost Awareness

LTX-2 API charges per second of generated video:

| Model | 1080p | 1440p | 4K |
|-------|-------|-------|-----|
| ltx-2-fast | ~$0.02/s | ~$0.04/s | ~$0.08/s |
| ltx-2-pro | ~$0.05/s | ~$0.10/s | ~$0.20/s |

**Always estimate and state cost before generating:**
- Quick draft (6s fast 1080p) ≈ $0.12
- Standard clip (10s fast 1080p) ≈ $0.20
- Pro quality (6s pro 1080p) ≈ $0.30
- 4K pro (6s pro 4K) ≈ $1.20

Tell the user the estimated cost before running. Start with `ltx-2-fast` for drafts,
switch to `ltx-2-pro` only for final output or when user requests high quality.

## Setup: Create the Generate Script

Before running any generation, ensure `ltx_generate.py` exists in the working directory.
If it doesn't exist, create it with the content from `scripts/ltx_generate.py`.

This script handles all API calls, file uploads, error handling, and output saving.
It must be created ONCE and then reused for all generations.

## Generation Modes

### 1. Text-to-Video (T2V)

User describes a scene → model generates video.

```bash
python3 scripts/ltx_generate.py --mode t2v --prompt "your prompt" --duration 6 --model ltx-2-fast
```

### 2. Image-to-Video (I2V)

User provides a still image → model animates it.

```bash
python3 scripts/ltx_generate.py --mode i2v --image /path/to/image.jpg --prompt "motion description" --duration 6
```

### 3. Audio-to-Video (A2V)

User provides audio → model generates synced video.

```bash
python3 scripts/ltx_generate.py --mode a2v --audio /path/to/audio.mp3 --prompt "visual description" --model ltx-2-pro
```

**Note:** A2V only works with `ltx-2-pro` model.

## Prompt Enhancement

The key to great LTX-2 output is prompt quality. Before sending ANY user prompt to the API,
enhance it using these rules:

### The 5 Core Elements (Official LTX Studio guide)

Every prompt should include:
1. **Scene/Environment** — WHERE it happens (describe first to avoid morphing)
2. **Subject** — WHO/WHAT is in the scene
3. **Action** — WHAT is happening (specific motion)
4. **Style** — Visual look (cinematic, anime, retro, film stock, etc.)
5. **Camera** — HOW the camera moves (optional but recommended)

### Prompt Structure

```
[Scene/Environment]. [Subject description]. [Action/Motion]. [Camera movement]. [Style/aesthetic].
```

**Critical rule:** Start with the scene description FIRST. This prevents morphing and scene changes.

### Enhancement Steps

When enhancing a user's prompt:

1. **Add scene context** if missing (time of day, weather, location details)
2. **Add camera direction** if not specified (default to slow dolly or static)
3. **Add style keywords** for cinematic quality:
   - Film look: `35mm film`, `Kodak film grain`, `halation`, `shallow depth of field`
   - Lighting: `golden hour`, `cinematic lighting`, `volumetric light`
   - Camera: `close-up`, `wide shot`, `aerial`, `tracking shot`
4. **Add era/period** if relevant: `1940s film`, `70s TV`, `80s news`, `90s sitcom`, `2000s found footage`
5. **Keep it under 200 words** — quality over quantity

### T2V Prompt Examples

**Cinematic portrait:**
```
Intimate close-up portrait. Halation. 35mm film look. High-end fashion.
Older woman with silver hair, wearing a dark velvet coat. She slowly turns
her head toward the camera, soft smile forming. Shallow depth of field,
warm studio lighting. Static camera, slight rack focus.
```

**UGC-style social video (20s):**
```
Gorilla gaming streamer. UGC style footage. Wearing headphones.
Static camera wide-shot. Gorilla is gaming using mouse and keyboard.
```

**Epic aerial:**
```
Epic aerial shot through rocky canyon. Camera flies through misty mountains
at dawn. Volumetric fog, golden hour light streaming through peaks.
Cinematic wide angle lens. Smooth forward dolly movement.
```

### I2V Prompt Tips

**Key difference from T2V:** I2V needs MORE specificity about motion.

**Common problem:** Unwanted camera movement. LTX-2 tends to dolly/zoom in I2V even when
you don't want it.

**Solution:** Be VERY explicit about camera:
- `"Static camera. No camera movement. Locked-off shot."`
- Describe ONLY the subject's motion, not the camera
- If you want stillness with subtle motion: `"Subtle breathing movement. Static locked camera."`

### A2V Prompt Tips

**LTX-2's killer feature** — native lip sync and audio-driven video.

Key rules:
1. **Match voice to character** — age, gender, personality alignment = better lip sync
2. **Dialogue auto-detected** — usually no prompt needed for speech, but add `"Character speaks"` if issues
3. **Match emotion** — if audio is angry, don't prompt "happy" (causes uncanny results)
4. **Start frame expression matters** — use neutral or matching emotion
5. **For music videos:** isolate vocals for best results, write actual lyrics in prompt
6. **Fix frozen first frame:** add audio buffer at start, or prompt `"Animate this image so that in the first second..."`

### Character Consistency

LTX-2 maintains consistent characters in T2V when descriptive enough:
- Describe clothing, age, hair, distinguishing features in detail
- Use the Elements system in LTX Studio for cross-generation consistency
- Tag characters with `@character_name` in LTX Studio

## Model Selection

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| ltx-2-fast | ~5-15s | Good | Drafts, iteration, previews, social content |
| ltx-2-pro | ~30-90s | Cinematic | Final output, client work, A2V |

**Decision rules:**
- First generation → always `ltx-2-fast` (cheap, fast feedback)
- User says "high quality" / "pro" / "final" → `ltx-2-pro`
- Audio-to-video → must use `ltx-2-pro`
- Iterating on prompt → `ltx-2-fast` until happy, then one `ltx-2-pro` final

## Technical Parameters

### Resolution
- Width and height must be **divisible by 32**
- Non-standard resolutions cause artifacts
- Supported: `1920x1080`, `2560x1440`, `3840x2160`

### Duration
- `ltx-2-fast` at 1080p/25fps: **6–20 seconds**
- `ltx-2-pro`: **6–10 seconds**
- For longer content: chain clips together

### Frame Rate
- 25 fps (default) or 50 fps

### Frame Count
- Must be **divisible by 8 plus 1** (e.g., 9, 17, 25 frames)

## Camera Presets

Include in prompts for consistent camera work:

| Preset | Prompt Keywords |
|--------|----------------|
| Static | `Static camera. Locked-off shot. No camera movement.` |
| Dolly In | `Slow dolly forward. Camera gradually pushes in.` |
| Dolly Out | `Camera slowly pulls back. Reverse dolly.` |
| Pan Right | `Camera pans slowly to the right.` |
| Pan Left | `Camera pans slowly to the left.` |
| Crane Up | `Camera cranes upward revealing the scene.` |
| Handheld | `Handheld camera. Slight shake. Documentary style.` |
| Aerial | `Aerial drone shot. Smooth forward movement.` |
| Tracking | `Camera tracks alongside the subject.` |
| Orbit | `Camera slowly orbits around the subject.` |

## Workflow

### Standard Generation Flow

1. **Receive user request** → understand what they want
2. **Enhance the prompt** → apply the 5 core elements
3. **Show enhanced prompt** → let user approve or modify
4. **Estimate cost** → state it clearly
5. **Generate** → run the script
6. **Deliver** → save to Desktop, send via Telegram
7. **Iterate** → ask if they want changes (adjust prompt, try pro model, etc.)

### Branded Content Workflow

1. Save logos/brand assets as Elements in LTX Studio
2. Tag Elements in prompts with `@element_name`
3. Generate with brand color palette using Color Picker
4. Use Multi-reference panel for style consistency

## Error Handling

| Error | Cause | Action |
|-------|-------|--------|
| `401 Unauthorized` | API key invalid | Check LTX_API_KEY env var |
| `402 Payment Required` | Insufficient credits | Add credits at console.ltx.video |
| `413 Payload Too Large` | Image/audio file too big | Compress or resize input |
| `429 Rate Limited` | Too many requests | Wait 60 seconds and retry |
| `500 Server Error` | LTX API issue | Wait 5 min and retry |
| Morphing/scene change | Scene not described first | Move scene description to start of prompt |
| Unwanted camera movement | I2V default behavior | Add explicit "Static camera. No camera movement." |
| Frozen first frame (A2V) | Audio sync issue | Add audio buffer, or prompt "Animate in the first second..." |

## Save Output

Save generated videos to:
```
~/Desktop/cineclaw/output-{mode}-{YYYY-MM-DD-HHmmss}.mp4
```

Include in the filename: mode (t2v/i2v/a2v), date, model used.
