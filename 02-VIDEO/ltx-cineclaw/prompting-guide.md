# LTX-2 Prompting Guide

Practical guide for writing effective LTX-2 video prompts. Based on official LTX Studio
documentation and community research from 700+ tweets spanning Oct 2024 - Feb 2026.

## The Golden Rule

**Start every prompt with the scene/environment description.**
This prevents morphing, scene changes, and inconsistencies.

## Prompt Structure

```
[Scene/Environment]. [Subject]. [Action/Motion]. [Camera movement]. [Style/Aesthetic].
```

## The 5 Core Elements

1. **Scene** — Where and when. "Interior of a dark wooden cabin at night lit by a faint lantern."
2. **Subject** — Who/what. "A 30-year-old woman in a red leather jacket, short black hair."
3. **Action** — What happens. "She slowly turns toward the window, reaching for the curtain."
4. **Camera** — How we see it. "Slow dolly in. Shallow depth of field."
5. **Style** — The look. "35mm film, warm color grading, halation, soft oval bokeh."

## Text-to-Video (T2V)

### Best Practices
- Be descriptive about characters for consistency (LTX-2 maintains same face across regens)
- Use cinematic language: lens choice, depth of field, lighting
- Specify era for period looks: "1940s film", "70s TV drama", "80s news broadcast"
- Keep prompts under 200 words
- Duration up to 20 seconds with ltx-2-fast

### Working Examples

**Cinematic Portrait:**
```
Intimate close-up portrait. Halation. 35mm film look. High-end fashion.
Older woman with silver hair wearing a dark velvet coat. She slowly turns
toward camera. Shallow depth of field, warm studio lighting. Static camera.
```

**Action Scene:**
```
Rain-soaked neon-lit Tokyo alley at night. A lone samurai in modern tactical
gear walks forward, katana at his side. Rain streams down his face. Camera
tracks alongside him at medium distance. Cyberpunk aesthetic, volumetric fog,
blue and pink neon reflections on wet pavement.
```

**Social/UGC Style:**
```
Gorilla gaming streamer. UGC style footage. Wearing headphones.
Static camera wide-shot. Gorilla is gaming using mouse and keyboard.
```

## Image-to-Video (I2V)

### Key Differences from T2V
- Needs MORE specificity about motion
- Default behavior: unwanted camera dolly/zoom (biggest community complaint)
- Focus prompt on WHAT MOVES, not the camera

### Fixing Unwanted Camera Movement
Always include: `"Static camera. No camera movement. Locked-off shot."`
Describe only the subject's motion if you want a still camera.

### Working Examples

**Subtle animation from still:**
```
Static camera. No camera movement. Locked-off shot.
Subject blinks slowly, slight head tilt. Hair moves gently with breeze.
Subtle breathing movement visible. Warm natural lighting remains constant.
```

**Dynamic from still:**
```
Dynamic aerial drone shot. Camera moves forward revealing the landscape.
Clouds drift slowly. Trees sway in wind. Cinematic wide angle.
```

## Audio-to-Video (A2V)

LTX-2's standout feature — native lip sync and audio-driven video.

### Rules for Good Results
1. **Match voice to character** — age, gender, personality alignment matters
2. **Dialogue auto-detected** — no special prompt needed, add "Character speaks" if issues
3. **Match emotion** — audio emotion must match prompt emotion (angry audio + happy prompt = bad)
4. **Start frame matters** — use neutral or matching expression
5. **Music videos** — isolate vocals, write actual lyrics in prompt for fast/effects-heavy lyrics
6. **Fix frozen first frame** — add short audio buffer at start, or: "Animate this image so that in the first second..."
7. **Only works with ltx-2-pro model**

### A2V Workflow
1. Upload or generate audio (or use Text-to-Speech)
2. Provide start image OR text prompt
3. Add prompt for emotion, action, camera
4. Generate

## Style Keywords Reference

### Film & Lens
- `35mm film`, `16mm film`, `IMAX`
- `Kodak 35mm Film. Film grain.`
- `Wide angle lens`, `Ultra-wide lens`
- `Halation` (light bloom)
- `Soft oval bokeh`
- `Shallow depth of field`
- `Anamorphic lens flare`

### Camera Framing
- `Extreme close-up`, `Close-up, tight framing`
- `Medium shot`, `Medium wide shot`
- `Wide shot`, `Extreme wide shot`
- `Low angle`, `High angle`, `Dutch angle`
- `Aerial shot`, `Bird's eye view`
- `Side profile medium-wide shot`
- `Reverse shot from behind`
- `Over-the-shoulder shot`

### Lighting
- `Golden hour`, `Blue hour`
- `Cinematic portrait light`
- `Volumetric light`, `God rays`
- `Neon lighting`, `Practical lighting`
- `Chiaroscuro`, `Rembrandt lighting`
- `Backlit silhouette`

### Movement
- `Slow dolly forward/backward`
- `Camera pans left/right`
- `Crane up/down`
- `Tracking shot alongside subject`
- `Orbit around subject`
- `Handheld, slight shake`
- `Steadicam smooth movement`
- `Static camera. Locked-off shot.`

### Era/Period
- `1920s silent film, black and white, intertitles`
- `1940s film noir, high contrast, shadows`
- `1970s TV drama, warm tones, soft focus`
- `1980s news broadcast, grainy VHS`
- `1990s sitcom, bright flat lighting`
- `2000s found footage, shaky cam, low resolution`
- `Modern cinematic, clean 4K, color graded`

## Technical Constraints

- Resolution must be divisible by 32
- Frame count must be divisible by 8 + 1
- CFG Scale: 1.0 for distilled model
- Max duration: 20s (fast@1080p), 10s (pro)
- VRAM: 16GB min, 24GB recommended (for local runs)

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Scene description buried in middle | Move to FIRST sentence |
| No camera direction specified | Add explicit camera movement or "Static camera" |
| Too vague ("make it cool") | Use specific cinematic terms |
| Conflicting emotions (A2V) | Match prompt emotion to audio emotion |
| I2V unwanted zoom | Add "Static camera. No camera movement. Locked-off shot." |
| Morphing between scenes | One scene per generation, chain clips for longer |

## Advanced Techniques

### Time-Stamping
Describe what happens at specific moments: "In the first 2 seconds... then at 4 seconds..."

### Elements System (LTX Studio)
- Save characters, logos, fonts as reusable Elements
- Tag in prompts: `@character_name`, `@brand_logo`
- Ensures total consistency across generations

### Multi-Reference
- Combine environment reference + character reference
- Lock style with a reference image (close-up for tone/lighting)
- Add in prompt: "Keep the original style"

### Color Control
- Use Color Picker in LTX Studio with FLUX/Nano Banana
- Supports hex codes and brand palettes
- Prompt: "Change the color of the [item]"

### Community LoRAs
- **I2V Adapter LoRA** by @Machinedelusion — boosts I2V motion quality (trained on 30K videos)
- **Squish LoRA** — fun effect, prompt "squish it"
- **iCLoRA** — character replacement in existing scenes

## Resources

- Official platform: https://ltx.studio
- Model info: https://ltx.io/model/ltx-2
- HuggingFace: https://huggingface.co/Lightricks/LTX-2
- ComfyUI: https://github.com/Lightricks/ComfyUI-LTXVideo
- Official prompting blog: https://ltx.video/blog/how-to-prompt-for-ltx-2
