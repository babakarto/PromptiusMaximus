# UGC Style Guide — Amateur Video Effect with AI

> Extracted from production guides. Techniques tested on Kling 3.0 and Seedance 2.0.

---

## KLING 3.0 — UGC Rules

### UGC Video Prompt Structure
- EVERYTHING in ONE single block — zero separate paragraphs for dialogue
- Dialogue merged into action: "she says [text] in a [tone] voice then [action]"
- Always specify: "Continuous unbroken single take, no cuts, no transitions"
- Character format: `[Character A: description]`
- Voice tone inline: "calm confident voice", "breathless excited voice", "slow whisper"

### Forbidden Words in Kling
| NEVER write | Why | Alternative |
|-------------|--------|-------------|
| phone | It renders it in the frame | DO NOT mention it |
| camera | It renders it | Use "framing" or "lens" |
| holding the camera | Generates phone in hand | "the framing moves/tilts/follows" |
| brings the camera closer | Generates phone | "the framing moves closer to her face" |
| camera lying on bed | Generates visible phone | "at mattress level pointing upward" |
| selfie | Can generate phone | Only describe the framing from above |

### How to Achieve Selfie Effect WITHOUT Generating a Phone
- Only describe how the FRAMING moves, not the camera
- "the framing moves closer to her face" = moves closer
- "the whole framing tilts and follows her movement" = follows the body
- "the framing drops to pillow level" = drops down
- "the framing shifts slightly" = slight movement
- The subject does NOT hold/touch/move anything — the framing moves on its own

### Opening Hook (first 3 sec)
- Sudden movement toward the camera/lens
- Pointing finger toward the lens
- Wide eyes + impactful opening line
- Quick step forward / lean forward
- Sudden expression change (from serious to smile)

### Mini DJI Microphone
To add a wireless mini mic like a content creator:
- "holding a small black wireless lavalier microphone with grey fluffy windscreen in her left hand close to her lips"
- "keeping the microphone near her lips the whole time"
- DO NOT say "DJI" or "TikTok"

---

## SEEDANCE 2.0 — UGC Keywords

- "low quality iPhone footage, slight compression artifacts, soft focus, motion blur, grainy sensor noise"
- "NOT crisp, NOT sharp, NOT professional"

### Prompt Structure for UGC
- **30-100 words max** (sweet spot)
- Structure: Subject → Action → Camera → Style
- Use `@Image1 (75% weight)` for face/character lock
- Use `@Video1 (25% weight)` for motion/camera only
- Use `@Audio1` for lipsync

---

## REUSABLE SNIPPETS (copy/paste)

### Amateur UGC Style (add to the end of any prompt)
```
Low quality phone camera, digital noise and slight compression artifacts, warm tungsten overhead lighting. Natural skin texture with imperfections visible. NOT crisp, NOT sharp, NOT professional, NOT AI-generated looking.
```

### Nokia/Webcam Style (for goth/dark look)
```
Dim flat ambient light, very low contrast, muted desaturated colors, soft blurry focus, heavy digital noise and blocky compression artifacts, slightly underexposed and washed out, muddy blacks, dull browns beiges and blacks only. NOT contrasty, NOT colorful, NOT bright, NOT sharp, NOT AI-looking.
```

### Selfie Effect Without Phone (for Kling)
```
the framing moves closer to her face / the framing pulls back out / the whole framing tilts and follows her movement / the framing drops to pillow level
```

### Pose: Kneeling + Low Angle (copy/paste into any prompt)
```
She is kneeling on the floor sitting back on her heels with her knees spread apart shoulder-width, torso straight and upright, shoulders back, chest forward, arms resting at her sides, head straight with chin slightly raised looking directly into the camera. Shot from an extremely low angle with the camera placed on the ground at floor level pointing upward, vertical 9:16 format, perfectly centered in frame, slight wide-angle lens distortion from smartphone front camera, the ceiling is visible at the top of the frame.
```

---

## CAMERA IMPERFECTION KEYWORDS (sell the realism)
- `autofocus hunts briefly then locks on his face`
- `rack focus misses slightly then corrects`
- `camera operator shifts weight and the framing wobbles`
- `adjusts framing slightly too late`
- `visible ISO noise in shadows`
- `rolling shutter wobble`
- `no color grading, no filters — straight out of camera look`

---

## FROM SKILL.MD — UGC Camera Table

| Keyword | Effect |
|---------|---------|
| handheld | UGC style, realism, chaos |
| Sony FX3 + 35mm prime + autofocus hunt + rack focus miss | Best raw footage look |

### Categories Where UGC Works Best
| Category | Keywords | Notes |
|-----------|----------|------|
| Viral/UGC | TikTok, Reels, meme, funny, UGC | Hook in 2 seconds + short format |
| Viral/UGC | authentic handheld feel, natural expressions | |

---

## COMPLETE UGC WORKFLOW (from Kling 3.0 guide — @heyrobinai)

### Technical Parameters for UGC
- Start frame: selfie created in NanoBanana
- Prompt: the woman <<<element_1>>> taking a POV selfie style video and says
- **Arcads** (for UGC): arcads.ai

### UGC/Advertising Template
```
[Character A: woman around 25, brown hair, green eyes, wearing [outfit]]
She starts looking directly at the lens with a natural smile and says "[HOOK]" 
in a warm excited voice, then [NATURAL ACTION], continues saying "[BODY COPY]" 
while [CASUAL GESTURE], then leans closer and says "[CTA]" with a playful grin.
Continuous unbroken single take, no cuts, authentic UGC amateur energy, 
low quality compression artifacts, warm ambient lighting.
```

---

## EXTERNAL RESOURCES
- **Arcads** (for UGC): arcads.ai
- **NanoBanana** — for generating realistic start frames/selfies
- **Higgsfield** — platform for Kling 3.0 with unlimited access

---

> **Sources**: HANDOFF_PROMPTS.md, SKILL.md, x-research-kling-3-prompt-guide.md, x-research-seedance-2.0-prompt-guide.md
