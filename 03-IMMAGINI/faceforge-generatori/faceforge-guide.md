# FaceForge Guide — Complete Face Bypass Protocol for SeedForge

> Detailed reference for the two-phase FaceForge protocol inside SeedForge.
> Phase 1 (FORGE): Generate character sheet prompts from portrait photos.
> Phase 2 (SHIELD): Apply 8x8 grid overlay -> generate Seedance prompt with anti-fantasy override.

---

## How Seedance 2.0 Face Detection Works

ByteDance's content filter runs a face detection model on every uploaded image. Key behaviors:

- Detects **single prominent realistic human faces** in photos
- Sensitivity is higher for front-facing portraits than angled/partial faces
- 3D illustrations, anime, and heavily stylized faces typically pass
- Multiple small faces in a grid layout typically pass (no single dominant face)
- The filter has been updated multiple times — techniques that worked in early 2026 may need adjustment
- Vertical (9:16) uploads are more strictly filtered (face occupies more frame area)
- The filter checks the IMAGE, not the prompt — a perfect prompt with a blocked image = rejection

---

## Phase 1: FORGE — Creating the Character Sheet

### What Claude Does

When the user uploads a portrait photo:

1. **Visual Analysis** — Read the image and extract EVERY detail:
   - Gender and approximate age range
   - Skin tone (be specific: "warm olive", "deep brown", "fair with pink undertones")
   - Face shape (oval, round, square, heart, diamond)
   - Hair: exact color, length, texture (straight/wavy/curly/coily), style (bangs, parted, tied)
   - Eyes: color, shape (round, almond, hooded, monolid), spacing
   - Eyebrows: shape, thickness, arch
   - Nose: shape, size
   - Lips: shape, fullness
   - Distinctive features: freckles, moles, dimples, scars, beauty marks
   - Facial hair: beard, mustache, stubble, clean-shaven
   - Accessories: glasses (shape, color), earrings, piercings, headwear
   - Body type (if visible): build, height impression
   - Expression and vibe

2. **Generate Sheet Prompt** — Create a prompt for the user's preferred AI image generator

3. **Provide Instructions** — Settings, generator tips, what to look for in the output

### Character Sheet Prompt Templates

#### Universal Template (works in most generators)

```
3D character reference sheet showing front view, three-quarter view, and side profile of [DETAILED DESCRIPTION].
Pixar-style 3D character illustration. Clean white background. Soft even studio lighting.
Character turnaround sheet with consistent features across all three angles.
Same face, same hair, same skin tone, same expression in every view.
High detail, sharp features, 4K resolution.
```

#### Midjourney-Optimized

```
3D character turnaround reference sheet :: front view, three-quarter view, side profile :: [DETAILED DESCRIPTION] :: Pixar 3D illustration style, clean white background, even studio lighting, character design sheet, multiple angles, perfectly consistent features, high detail --ar 16:9 --v 6.1 --s 250
```

#### DALL-E / ChatGPT-Optimized

```
Create a 3D character reference sheet with three views arranged horizontally on a clean white background:
Left: front-facing view. Center: three-quarter angle view. Right: side profile view.
The character is [DETAILED DESCRIPTION].
Style: Pixar/Disney 3D animation quality. Soft studio lighting. Every view shows the exact same person with identical features, hair, and expression. High detail, 4K quality.
```

#### Flux / Stable Diffusion-Optimized

```
character turnaround reference sheet, three views, front view, three quarter view, side profile, [DETAILED DESCRIPTION], 3d pixar illustration style, clean white background, studio lighting, character design, multiple angles, consistent appearance, same person all views, high quality, 4k, detailed
```

#### Dreamina Image Generation

```
3D animated character sheet with three angles: front, 3/4, and side view of [DETAILED DESCRIPTION]. Pixar animation quality, clean white background, studio lighting, character turnaround reference, consistent identity across all views, high detail, 4K.
```

#### Nano Banana Pro (Recommended for Photorealistic Bridge)

```
3D stylized character illustration of [DETAILED DESCRIPTION], semi-realistic Pixar quality, front-facing portrait, clean studio background, soft lighting, detailed facial features preserved, 4K
```

> **Nota:** Nano Banana Pro produce risultati piu vicini al fotorealismo mantenendo lo stile 3D — ideale per il Realism Bridge nella Phase 2.

### Description Writing Rules

When converting the photo analysis into the [DETAILED DESCRIPTION] block:

1. **Lead with the most distinctive features** — what makes this person recognizable at a glance
2. **Be extremely specific** — "shoulder-length wavy auburn hair with copper highlights" not "red hair"
3. **Include ALL accessories FIRST** — "wearing round black-framed glasses and gold hoop earrings" BEFORE other features (generators often drop accessories if mentioned late)
4. **Specify skin tone precisely** — "warm golden-brown skin with subtle freckles" not "dark skin"
5. **Describe the expression** — "gentle confident smile showing slight dimples" not "smiling"
6. **Include body type if visible** — "athletic build, broad shoulders" or "slim, delicate frame"
7. **Word order matters** — most generators weight earlier words more heavily. Put the must-have features first

### Example FORGE Outputs

#### Example 1: Woman with Glasses

**Photo:** Woman, late 20s, curly dark hair, round glasses, light brown skin, gold hoop earrings

**FORGE Output:**

```
## FACEFORGE Phase 1: FORGE

**Generator:** Your preferred AI image generator
**Settings:** 16:9 aspect ratio, highest quality

### Prompt (copy-paste ready)

3D character reference sheet showing front view, three-quarter view, and side profile
of a woman in her late 20s wearing round black-framed glasses and large gold hoop earrings,
voluminous shoulder-length curly dark brown hair with natural texture,
warm light brown skin with golden undertones, almond-shaped dark brown eyes,
full lips, soft rounded face shape, subtle beauty mark on left cheek,
calm confident expression with a slight smile.
Pixar-style 3D character illustration. Clean white background. Soft even studio lighting.
Character turnaround sheet with consistent features across all three angles.
Same glasses, same earrings, same hair, same expression in every view.
High detail, sharp features, 4K resolution.

### After Generating
- Check: glasses present in ALL 3 views? If not, regenerate with "prominent round glasses" at start
- Check: earrings visible? If not, add "large gold hoop earrings clearly visible"
- Check: skin tone consistent? Should be warm light brown in all views
- Pick the generation with best consistency across angles
- Minimum resolution: 1024px on short edge
- Save as PNG (no compression artifacts)
```

#### Example 2: Man with Beard

**Photo:** Man, early 30s, short black hair, full beard, brown skin, athletic build

**FORGE Output:**

```
## FACEFORGE Phase 1: FORGE

### Prompt (copy-paste ready)

3D character reference sheet showing front view, three-quarter view, and side profile
of an athletic man in his early 30s with a well-groomed full dark beard and mustache,
short cropped black hair with subtle fade on sides, deep warm brown skin,
strong square jawline, thick straight eyebrows, dark brown eyes with intense focused gaze,
broad shoulders, muscular build visible under fitted black t-shirt.
Pixar-style 3D character illustration. Clean white background. Soft even studio lighting.
Character turnaround sheet with consistent features across all three angles.
Same beard, same hair, same build, same expression in every view.
High detail, sharp features, 4K resolution.
```

---

## Phase 2: SHIELD — Processing for Seedance

### Real Production Test Results

These are ACTUAL test results from generating 7+ scenes of a real person:

| Method Tested | Result |
|--------------|--------|
| Real photo, no processing | **BLOCKED** |
| 6x6 grid overlay on real photo | **BLOCKED** (not dense enough) |
| 3D/gaming style character sheet | Passes, but generates **cartoon** output |
| Heavy noise only (+-60) | Passes, but **low quality** output |
| Scanlines TV effect | Passes, but **artifacts** in output |
| **8x8 grid overlay on realistic sheet** | **WORKS** |
| **Realistic sheet @Image1 + face crop with grid @Image2** | **WORKS PERFECTLY** |

### Step 1: Apply 8x8 Grid Overlay (ALWAYS TRY FIRST)

Run:
```
python scripts/grid_maker.py sheet.png sheet_GRID.png
python scripts/grid_maker.py sheet.png face_GRID.png --face-crop
```

This draws thick white lines (width=6px) in an 8x8 pattern directly on the image. The grid breaks facial feature detection while Seedance still reads the character underneath.

**Produce TWO files:**
- `sheet_GRID.png` -> upload as **@Image1** (full body + poses)
- `face_GRID.png` -> upload as **@Image2** (face close-up, 1024x1024)

Give both to the user: **"Upload these to Seedance and try generating."**

### Step 2: If Blocked — Ask and Offer Alternatives

If the 8x8 grid doesn't pass, ask:
> "The 8x8 grid didn't pass. Want to try a denser grid or different pattern?"

Escalation order:

| # | Style | Command | How it works |
|---|-------|---------|-------------|
| 1 | Grid 10x10 + noise | `--style grid10_noise` | Denser grid + random noise disruption |
| 2 | Hexagonal grid | `--style hexgrid` | Non-rectangular pattern, harder to detect |
| 3 | Diagonal crosshatch | `--style crosshatch` | Pencil sketch effect over the image |
| 4 | Oil paint + grid | `--style oilpaint` | Median filter + posterize + grid |
| 5 | Blueprint technical | `--style blueprint` | Blue tint + measurement grid |
| 6 | Heavy noise | `--style noise` | Last resort, passes but lower quality |

Generate ALL at once: `python scripts/grid_maker.py sheet.png output.png --style all`

### Step 3: Generate the Seedance Prompt

The proven prompt structure uses TWO references + an anti-fantasy override:

```
@Image1 is the full character reference sheet showing body, outfit, and poses from multiple angles.
@Image2 is the close-up face reference — use it for exact facial likeness.

Raw handheld footage shot on Sony FX3 with a 35mm prime lens wide open. NOT 3D, NOT cartoon,
NOT CGI, NOT animation. This looks like behind-the-scenes documentary footage someone filmed
casually [WHERE/HOW].

[Subject description — age, build, clothing, distinctive features].
[Environment description].

[00-05s] Shaky medium shot, [action]. The autofocus hunts briefly then locks on [subject].
[Light detail]. [Camera imperfection].

[05-10s] The camera steps [where], handheld sway increases. [Action]. Rack focus misses slightly
then corrects. Real skin, [physical detail]. The camera operator shifts weight and the framing wobbles.

[10-15s] [Final action]. The camera operator adjusts framing slightly too late. Shallow depth
of field, messy bokeh from [light source].

Muted natural color, [light description]. Visible ISO noise in [where]. Subtle motion blur,
rolling shutter wobble. No color grading, no filters — straight out of camera look. 16:9, cinematic quality.
```

### Two Approaches — When to Use Which

**Approach A — Grid Overlay on Realistic Sheet (PROVEN BEST for hyperrealism):**
- Input: Realistic character sheet + 8x8 grid overlay
- Prompt uses: `NOT 3D, NOT cartoon, NOT CGI, NOT animation`
- Prompt uses: Camera imperfection language (Sony FX3, autofocus hunt, rack focus miss)
- Output: Documentary/film quality hyperrealistic video
- **Use this when:** You want maximum realism, mockumentary style, raw footage feel

**Approach B — 3D Illustration + Realism Bridge (CyberJungle method):**
- Input: 3D Pixar-style character sheet (non-photorealistic)
- Prompt uses: `4K, photorealistic, liveaction, lifelike, realistic skin texture`
- Output: Cinematic quality, slightly polished/clean look
- **Use this when:** You want cinematic/commercial style, polished look, or the grid method keeps failing

**DO NOT mix the approaches.** Using "NOT 3D" with a 3D illustration input contradicts itself. Using "photorealistic, liveaction" with a grid-overlaid realistic sheet is redundant — the anti-fantasy override is enough.

### Camera Imperfection Keywords (Proven to Sell Realism)

These specific phrases force Seedance into documentary/raw footage mode:

| Phrase | What it does |
|--------|-------------|
| `Raw handheld footage shot on Sony FX3 with a 35mm prime lens wide open` | Sets the overall indie/doc camera aesthetic |
| `NOT 3D, NOT cartoon, NOT CGI, NOT animation` | Explicit anti-fantasy override |
| `The autofocus hunts briefly then locks on his face` | Real autofocus imperfection |
| `Rack focus misses slightly then corrects` | Human error from focus puller |
| `The camera operator shifts weight and the framing wobbles` | Natural handheld wobble |
| `Adjusts framing slightly too late` | Operator reaction delay |
| `Visible ISO noise in shadows` | Real sensor noise |
| `Rolling shutter wobble` | CMOS sensor artifact |
| `No color grading, no filters — straight out of camera look` | Forces raw, unprocessed look |
| `Digital zoom pushes in closer — the image gets grainy` | Paparazzi/surveillance feel |

**What does NOT work for realism:**
- Tripod/cavalletto = too static/clean
- 200mm telephoto = wrong look (use 35mm + digital zoom instead)
- Gimbal/steadicam = too smooth, loses raw feel
- ARRI Alexa = too polished for documentary style (use Sony FX3)
- "Low angle from the bottom" = generates fisheye distortion

### Example SHIELD Output (Production-Tested Style)

```
## FACEFORGE Phase 2: SHIELD

I've processed your character sheet with the 8x8 grid overlay.

**Files ready:**
1. `sheet_GRID.png` — upload as @Image1 (full body reference)
2. `face_GRID.png` — upload as @Image2 (face close-up reference)

Upload both to Seedance and try generating with this prompt:

---

**Mode:** Omni Reference | **Ratio:** 16:9 | **Duration:** 12s

@Image1 is the full character reference sheet showing body, outfit, and poses from multiple angles.
@Image2 is the close-up face reference — use it for exact facial likeness.

Raw handheld footage shot on Sony FX3 with a 35mm prime lens wide open. NOT 3D, NOT cartoon,
NOT CGI, NOT animation. This looks like behind-the-scenes documentary footage someone filmed
casually in a cozy European cafe.

A woman in her late 20s with curly dark hair, round glasses, gold hoop earrings, wearing a cream
knit sweater. She's sitting at a small cafe table by the window.

[00-04s] Shaky medium shot, slight camera drift. She picks up a ceramic coffee cup, steam rising.
The autofocus hunts briefly then locks on her face. Warm afternoon light through the window.

[04-08s] The camera steps closer, handheld sway increases. She takes a slow sip and smiles softly,
looking out the window. Rack focus misses slightly then corrects. Real skin, natural warmth. The
camera operator shifts weight and the framing wobbles.

[08-12s] She puts the cup down, looks directly at the camera with a calm half-smile. The camera
operator adjusts framing slightly too late. Shallow depth of field, messy bokeh from the window light.

Muted natural color, warm afternoon side light. Visible ISO noise in shadows under the table.
Subtle motion blur, rolling shutter wobble. No color grading, no filters — straight out of camera look.
16:9, cinematic quality.

---

**If blocked:** Let me know and I'll try a denser grid or different pattern.
**If output looks too CGI:** Make sure "NOT 3D, NOT cartoon, NOT CGI" is at the start of the prompt.
```

---

## Gotchas & Edge Cases

### FORGE Gotchas

1. **Glasses often disappear** in character sheets — put "wearing [X] glasses" at the VERY BEGINNING of the description, before any other feature
2. **Earrings/piercings get lost** — specify them explicitly: "gold hoop earrings visible in all three views"
3. **Skin tone drift** — different generators interpret skin tone differently. Be extremely specific: "warm medium brown skin with golden undertones" not just "brown skin". Compare the sheet to the original and adjust if off
4. **Hair texture simplification** — curly/coily hair often gets smoothed by generators. Add "detailed individual curls, natural texture, no smoothing, volumetric hair"
5. **Expression matching** — if the original photo has a specific expression, describe it precisely. Generators default toward neutral/smiling if you're vague
6. **Background bleed** — some generators add random objects. Always specify "clean white background, no objects, no environment, no props"
7. **Tattoos and body art** — must be described with exact placement: "small butterfly tattoo on right inner wrist". Generators often mirror or move tattoos
8. **Asymmetric features** — describe BOTH sides: "left eyebrow slightly higher than right, mole on right cheek near nose"

### SHIELD Gotchas (from real production tests)

1. **6x6 grid is NOT enough** — tested and BLOCKED. Minimum 8x8 with thick lines (width=5-6px)
2. **3D style sheets pass the filter BUT generate cartoon** — if you want hyperrealism, use a REALISTIC sheet + grid overlay, NOT a 3D illustration
3. **Two references beat one** — @Image1 (full body sheet + grid) + @Image2 (face crop + grid) produces much better face consistency than a single reference
4. **"NOT 3D, NOT cartoon, NOT CGI"** is mandatory in the prompt when using realistic sheets with grid overlay. Without it, Seedance may drift toward stylized output
5. **Sony FX3 + 35mm prime** produces better documentary realism than ARRI Alexa (too clean/polished)
6. **Camera imperfections sell realism** — autofocus hunt, rack focus miss, rolling shutter, ISO noise. Without these, output looks "too perfect" even with realistic references
7. **Brand names in prompts get blocked** — real company names, country names tied to specific organizations, etc. trigger content filter. Describe visually instead
8. **9:16 is stricter than 16:9** — for vertical videos, use denser grid (10x10) or add noise
9. **Noise alone passes but quality drops** — grid overlay preserves quality better than noise
10. **Chinese prompts pass filters easier** — same prompt in Chinese triggers less. Consider translating if English is blocked
11. **Multi-shot consistency decay** — by shot 4-5, face attention fades. Re-inject face lock: "maintaining exact @Image1 and @Image2 features"

### When FaceForge Fails — Full Escalation Ladder

Try in this exact order:

1. **8x8 grid overlay** -> the proven winner
2. **10x10 grid + noise** -> denser disruption
3. **Hexagonal grid** -> non-rectangular, harder to detect
4. **Crosshatch / Oil paint + grid** -> heavier style disruption
5. **Switch to 3D illustration approach** -> Nano Banana Pro sheet + Realism Bridge keywords instead of grid
6. **Try on SeaArt.ai or Yapper** -> less strict filters than Dreamina
7. **Generate a NEW AI face** with similar features -> describe features in text-to-image without any real photo reference
8. **Celebrity/public figure** -> face detection may include recognition, not just detection. Use original AI character that shares general attributes only

---

## Advanced Techniques

### Technique: Multi-Sheet Ensemble

For maximum character consistency across a long video:

1. FORGE 3 separate character sheets (different expressions: neutral, smiling, intense)
2. SHIELD all 3 with the grid method
3. Use different sheets for different emotional beats:
   - @Image1: neutral expression sheet (default)
   - @Image2: smiling sheet (for happy scenes)
   - @Image3: intense sheet (for dramatic scenes)
4. In each shot prompt: `@Image1 (60% weight) base character, @Image2 (20% weight) expression reference`

### Technique: Outfit Swap

The character sheet captures the person's face but may show generic clothing. To change outfits:

1. FORGE the character sheet (face reference)
2. Separately generate/find the outfit reference image
3. In Seedance prompt:
   ```
   @Image1 (75% weight) as character face and identity reference.
   @Image2 (50% weight) as outfit and wardrobe reference.
   The character wears the exact outfit from @Image2.
   ```

### Technique: The Double Bridge (Highest Quality)

For maximum realism in the final video:

1. FORGE -> character sheet (3D illustration)
2. Use the character sheet in Dreamina's IMAGE generation (not video) with prompt:
   ```
   Photorealistic portrait photograph of the character from @Image1,
   natural lighting, shot on Canon EOS R5, 85mm lens, shallow DOF.
   4K, lifelike, realistic skin texture.
   ```
3. The result is a semi-realistic image that's harder to detect (it was generated, not uploaded)
4. Use THIS as the final @Image1 for Seedance video generation

This adds an extra step but produces the most realistic results because the input to Seedance is already closer to photorealistic while still being AI-generated (and thus passing the filter).

---

## Quick Reference: Complete FaceForge Flow

```
STEP 1: User uploads portrait photo
  |
STEP 2: Claude runs FORGE
  |- Analyzes photo (every visual detail)
  |- Generates character sheet prompt (copy-paste ready)
  |- User copies prompt to preferred image generator
  |
STEP 3: User generates character sheet externally
  |- Midjourney / DALL-E / Flux / Dreamina / Nano Banana Pro
  |- Generates 2-3 versions, picks best consistency
  |
STEP 4: User uploads generated sheet back to Claude
  |
STEP 5: Claude runs SHIELD
  |- Applies 8x8 grid overlay (DEFAULT — try first)
  |- Produces @Image1 (full sheet + grid) and @Image2 (face crop + grid)
  |- Generates Seedance prompt with "NOT 3D, NOT cartoon, NOT CGI" + camera imperfections
  |- Gives files + prompt to user
  |
STEP 6: User uploads to Seedance and tries generating
  |
  |- SUCCESS -> done!
  |- BLOCKED -> Claude asks "want to try alternative grid/pattern?"
      |- Offers: grid10_noise, hexgrid, crosshatch, oilpaint, blueprint, noise
      |- Processes with next style, gives new files
      |- Repeat until one passes
  |
RESULT: Hyperrealistic video with the person's likeness, face detection bypassed
```
