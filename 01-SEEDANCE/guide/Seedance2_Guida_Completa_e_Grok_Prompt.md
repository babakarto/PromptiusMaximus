# Seedance 2.0 - Complete Prompt Engineering Guide + Grok.com Prompt

In-depth research from verified sources: official ByteDance website, official Dreamina/CapCut resources, tested prompt guides from creators, curated GitHub repos, Reddit, and real YouTube showcases.

---

## What is Seedance 2.0

Seedance 2.0 is ByteDance's multimodal AI video model (2026), primarily integrated on **Dreamina** (dreamina.capcut.com) and **CapCut**. It supports text + up to 9 images + 3 videos + 3 audio (max 12 files total, video/audio ≤15s). It excels at character consistency, realistic physics, cinematic camera movements, and synchronized audio. Prompts work exactly the same across all platforms using the model (Dreamina is the most direct and reliable).

---

## 1. Ideal Prompt Structure (Magic Formula)

All tested guides converge on this exact order (reduces drift and maximizes control):

```
[@References] + Subject + Action + Scene/Environment + Camera + Lighting + Style + Audio/Quality + Constraints
```

### Ready-to-Use Copy-Paste Template (WaveSpeed + ImagineArt + Dreamina official)

```
@image1 as main character / @video1 for camera movement
[Clear subject description, one person/object]
[Action verb in present tense, specific and singular]
[Environment + atmosphere]
[Camera: shot size + movement + angle + lens]
[Lighting + color grading]
[Visual style: one strong anchor (e.g. "Blade Runner cinematography", "National Geographic", "Zara campaign")]
[4K ultra HD, rich details, cinematic sharpness, stable motion]
[Constraints / negatives]
```

**Ideal length on Dreamina:** 30-100 words. Too short = vague. Too long = loses focus and quality drops.

---

## 2. Writing Tricks and Techniques (Most Powerful, Tested)

### Basic Rules
- **Always start with the subject** (lead with the subject) → the AI immediately focuses on what matters
- **One action verb per shot** → avoids chaos

### Precise Camera Vocabulary (Gold on Seedance)

| Category | Options |
|-----------|---------|
| **Shot** | wide / medium / close-up / extreme close-up |
| **Movement** | slow dolly-in, tracking shot, push-in, crane up, handheld (for UGC), gimbal-smooth, drone ascending, whip-pan (only for dynamic effect) |
| **Angle + lens** | eye-level normal lens, low-angle telephoto, high-angle wide |

### Timeline for Multi-Shot (Perfect for Stories)

```
[00-05s] Shot 1: ...
[05-10s] Shot 2: ...
```

### @References (The Most Powerful Feature)

- `@image1` as main character or `@image1 as main character reference`
- `@video1` for camera movement or `@video1's camera movement`
- `@image2` as first frame, `@image3` as last frame
- You can describe in natural language: "Use @image1 as girl with short hair and @video1 for the fluid dress movement"
- **For maximum consistency:** always upload the same character photo in every generation

### Final Quality Suffix (Always Add It)

```
4K Ultra HD, rich details, sharp clarity, cinematic texture, stable picture, no distortion, maintain face and clothing consistency
```

### Negative Prompts / Constraints (Use 3-5 max, Put Them at the End)

```
No jitter, no shake, no wobble, no warping, no elastic deformation
No extra fingers, no deformed hands, no extra characters
No text overlays, no logos, no watermarks, no captions
No snap zooms, no whip pans, no Dutch angles, no jump cuts
No temporal flicker, no blurry motion
No cartoon/anime (if you want realistic)
```

### Pro Trick
Change only one variable between generations (only lighting, only camera, only style). Avoid rewriting everything.

### Dreamina-Specific Best Practices (From Real Tests)
- Best clips under **10-12 seconds** (quality drops after)
- Always use image/video references for consistency
- For viral: **strong first 3 seconds** (visual hook)

---

## 3. Tested and Ready-to-Use Example Prompts

Selected from official/tested guides, already optimized for Dreamina/Seedance 2.0.

### Cinematic / Narrative (AtlasCloud + ImagineArt)

#### 1. Epic Drone Reveal (9/10 success rate)

```
Sweeping drone shot ascending from a misty valley floor, slowly revealing a vast mountain range at sunrise, golden light breaking through clouds, long shadows on pine forests, orchestral grandeur, National Geographic documentary quality, ultra-smooth camera movement. 4K, stable, cinematic texture.
```

> Why it works: tension + reveal + strong anchor.

#### 2. Emotional Close-Up (Blade Runner style)

```
Extreme close-up of a young woman's face, eyes slowly opening to reveal reflected city lights, single tear rolling down cheek catching light, shallow depth of field bokeh, intimate emotional, Blade Runner cinematography, warm amber and cool blue contrast. Slow push-in.
```

### Action / Combat

#### 3. Martial Arts Slow-Motion (Crouching Tiger style)

```
A martial artist performing a spinning kick in slow motion, silk ribbons trailing from wrists creating spiral patterns, ancient temple courtyard with cherry blossom petals falling, dramatic side-angle tracking shot, Crouching Tiger Hidden Dragon aesthetic, golden hour backlighting silhouette.
```

### Product / Commercial (Super Stable)

#### 4. Wristwatch Luxury

```
Premium wristwatch floating mid-air slowly rotating, water droplets suspended around it like diamonds catching light, pure black background, single dramatic spotlight from above, extreme macro detail, high-end jewelry commercial, ultra-smooth rotation.
```

#### 5. Iced Coffee Pour (Hypnotic)

```
Tall glass of iced coffee being poured in slow motion, rich dark coffee meeting swirling cream creating mesmerizing patterns, ice cubes clinking, condensation droplets, close-up to medium shot, warm cafe lighting, Starbucks commercial quality.
```

### Viral / Social (Dreamina Official)

#### 6. Cat Meme Chaos

```
Fast-paced video of a cat knocking over objects with exaggerated reactions, meme-style captions, quick zooms for comedic effect.
```

### Multi-Shot with References (Advanced Example)

#### 7. Cyberpunk Assassin Chase

```
Use @image1 as main character. @video1 as camera movement reference. A lone cyberpunk assassin sprints through rain-soaked neon streets at night, police drones and headlights blurring past, quick cuts between close-up determined eyes, boots splashing puddles, wide shots of traffic. Handheld camera with aggressive push-ins, intense motion blur, dramatic contrast, final slow-motion leap off rooftop. 4K, stable, no distortion.
```

---

## 4. Verified Resources

- Official ByteDance Seedance 2.0 website
- Dreamina official prompt guide & tips
- Tested guides: ImagineArt (70 prompts), AtlasCloud (15 best, with success %), WaveSpeed (template + negatives)
- GitHub awesome-seedance-2-prompts (500+ curated)

---

---

# Prompt to Simulate a Grok.com Research

## Main Prompt (Optimized for UI Consistency and Dynamism)

### Settings
- **Mode:** Omni Reference
- **AR:** 16:9
- **Duration:** 15s
- **1 reference Image** (real screenshot of grok.com)

### Prompt

```
@image1 as exact reference of the grok.com interface (screenshot of homepage or clean chat)

Realistic live screen recording of the official grok.com interface by xAI, dark minimalist cyber UI, clean white text on deep black background, xAI logo top left, subtle blue neon glow accents, modern sidebar with Grok avatar.

A user cursor types the query "ricerca approfondita su prompt Seedance 2.0" into the central input box with smooth typing animation. Grok responds in real-time: thinking animation with visible tool icons (web_search, x_keyword_search, browse_page) lighting up one by one. Step-by-step reasoning appears line by line in the chat ("Sto usando web_search...", "Analizzando risultati verificati...", "Citazioni inline...").

Results populate dynamically: cards with titles, summaries, inline citations [web:1], [post:3], scrolling smoothly. Grok structures the answer with bullet points, tables and bold highlights. Mouse cursor moves naturally, clicking on results and expanding details.

Slow cinematic push-in from full screen to focused chat window, subtle screen reflections and soft parallax on UI elements, futuristic yet clean digital aesthetic exactly like grok.com 2026. 4K ultra HD, razor sharp text, zero jitter, zero distortion, stable motion, cinematic screen capture style, rich UI textures, perfect consistency of interface elements.
```

### Why It Works on Seedance 2.0

- **@image1** → upload a real screenshot of grok.com to get a perfectly identical interface (95%+ consistency)
- **Starts with the subject** (the interface) → the AI doesn't get distracted
- **Single clear action** (typing → tool activation → results) → Seedance loves precise verbs
- **Camera + fluid movement** → avoids the "boring static video" effect
- **Final quality suffix** → eliminates jitter and warping typical of UI videos

---

## Quick Variants

### Cinematic / "Hacker Style" Version

Add after the base prompt:

```
... dramatic volumetric lighting from screen, subtle matrix rain in background, cyberpunk neon blue and purple accents, slow dramatic zoom on the reasoning text while tools activate.
```

### Ultra-Fast Timelapse Version (For 8-10 Second Viral Videos)

```
... fast-forward timelapse style, 3x speed, query typed instantly, tools flash rapidly, full research completed in 8 seconds, smooth speed-ramping at the end.
```

### Version with Grok "Character" (Animated Avatar)

```
... Grok AI mascot (cute robot with xAI style) appears on the left of the chat, nodding and gesturing while tools activate and results appear.
```

---

## Notes

- To change the research topic: replace only the query in the prompt (e.g. "research on Bitcoin", "research on a product", etc.)
- For vertical TikTok/Reels format: change AR to 9:16
- Always upload a real, up-to-date screenshot of grok.com as @image1 for maximum consistency
