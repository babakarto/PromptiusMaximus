# Seedance 2.0 - Latest Updates & Advanced Techniques (Web Research March 2026)

> Research conducted March 28, 2026. Sources include TechCrunch, CapCut Newsroom, fal.ai, GitHub repos, Zhihu, and multiple prompt engineering guides.

---

## 1. Latest Model Updates & New Features

### Release Timeline
- **February 2026**: Seedance 2.0 officially launched on Jimeng (即梦) platform in China
- **March 26, 2026**: Global rollout begins via CapCut (Brazil, Indonesia, Malaysia, Mexico, Philippines, Thailand, Vietnam first)
- **Platforms**: CapCut (AI Video + Video Studio), Dreamina, Pippit (marketing platform)

### What Changed from 1.5 to 2.0

| Feature | Seedance 1.5 | Seedance 2.0 |
|---------|--------------|--------------|
| Inputs | Text + single first/last frame image | Text + up to 9 images + 3 videos + 3 audio files (12 total) |
| Audio | Basic generation | Dual-channel stereo, spatial positioning, multi-layer (music + foley + dialogue) |
| Editing | Generate only | Targeted modifications to specific scenes/characters + video extension |
| Physics | Basic motion | Enhanced fabric, light refraction, micro-expressions, limb stability |
| Multi-shot | Limited | Native multi-shot with natural cuts and transitions within single generation |
| Lip-sync | Basic | Enhanced multi-language lip-sync (EN, CN, JP, KR, ES, PT, ID + CN dialects) |
| Chinese dialects | Not supported | Cantonese, Sichuanese, Shaanxi dialect recognition |

### Technical Specifications (API)
- **Model string**: `"seedance-2.0"`
- **Duration**: 4-15 seconds (default 8s)
- **Aspect ratios**: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21` (6 options)
- **Resolution**: `480p`, `720p`, `1080p`, `2K` (2560x1440)
- **Style presets**: `"cinematic"`, `"anime"`, `"realistic"`, `"3d_render"`
- **Audio toggle**: `true` / `false`
- **Seed**: Integer for reproducible outputs
- **Negative prompt**: Supported
- **Camera lock**: Option to lock camera lens to reduce motion blur
- **References array**: Up to 12 items, each with `type` and `role` (`"subject"`, `"environment"`, `"motion"`, `"audio"`)
- **Output**: MP4, H.264 encoding, 48 kHz AAC audio
- **Async workflow**: Submit → poll (5s intervals) → download (30-120s total)

### Safety Restrictions (Current)
- Cannot generate from images/videos containing real faces (initial rollout)
- Invisible watermarking on all outputs
- C2PA Content Credentials embedded
- IP protection systems block unauthorized generation

---

## 2. Color Grading Vocabulary (Comprehensive)

### Film Stock Emulation Terms
| Term | Color Palette | Mood |
|------|---------------|------|
| **Kodachrome** | Rich reds, yellows, deep blues | Warm vintage, archival |
| **Technicolor** | Hyper-saturated primaries (bright red, green, blue) | Classic cinema, vibrant |
| **CineStill 800T** | Tungsten balanced, red halation in highlights | Cinematic night, urban |
| **Bleach bypass** | Metallic grays, washed-out colors, deep blacks | Gritty, desaturated, war film |
| **Kodak Aerochrome / Infrared** | Bubblegum pink trees, white foliage, deep blue skies | Surreal, dreamlike |
| **Cross-processed** | High contrast with shifted greens/yellows | Lomo, experimental, chemical |
| **Sepia** | Browns, tans, creams | Western, nostalgic, aged |

### Cinematic Color Grade Terms
| Term | Description | Use Case |
|------|-------------|----------|
| **Teal & orange** | Cyan/teal shadows + orange/amber highlights | Blockbuster, Hollywood action |
| **Wes Anderson palette** | Pastel pinks, mint greens, soft yellows, flat lighting | Quirky, symmetrical, whimsical |
| **Film noir** | Black & white, chiaroscuro, high contrast monochrome | Detective, thriller, mystery |
| **Nordic noir** | Desaturated blues, greys, muted greens | Bleak, overcast, Scandinavian crime |
| **Cyberpunk** | Neon pink, magenta, cyan, deep black | Dystopian, futuristic, night |
| **Solarpunk** | Bright whites, lush greens, soft gold sunlight | Eco-futurism, utopian |
| **Steampunk** | Brass, copper, brown leather, steam gray | Victorian industrial |
| **Matrix green** | Monochromatic computer green gradients | Digital, dystopian |

### Atmospheric & Experimental Grades
| Term | Color Palette | Effect |
|------|---------------|--------|
| **Bioluminescence** | Glowing blues, electric greens on dark backgrounds | Magical, underwater, alien |
| **Sodium vapor** | Sickly orange, yellow-brown, black shadows | Urban night, industrial |
| **Thermal imaging** | Rainbow gradient (red=hot, blue=cold) | Surveillance, sci-fi |
| **Night vision** | Monochromatic bright green and black | Military, horror, found footage |
| **Duotone** | Two contrasting colors | Pop art, graphic, bold |
| **Selective color** | Grayscale + one vibrant color (Sin City style) | Dramatic emphasis |
| **Ultraviolet/Blacklight** | Deep purple background + glowing neon accents | Party, rave, forensic |

### Color Grading Adjective Pairs for Prompts
- `warm tones, lifted shadows` → cozy, inviting
- `cool-warm contrast, moody shadows` → cinematic tension
- `desaturated, high contrast` → gritty realism
- `high key, low contrast, clean white` → commercial, airy
- `deep shadows, golden highlights` → dramatic, premium
- `muted earth tones, film grain` → indie, organic
- `neon reflections, wet textures` → cyberpunk, rain-soaked
- `pastel, soft focus` → dreamy, romantic
- `cold blue-green tones, gritty textures` → thriller, horror
- `gold-white light, warm neutral tones` → luxury, aspirational

---

## 3. Audio/Sound Description Guide

### Four-Layer Audio Prompt Structure (Seedance-Specific)
```
Layer 1: AMBIENT BED — continuous environmental sound
Layer 2: FOREGROUND SFX — 1-2 event-locked sounds
Layer 3: MUSIC CUE — entry time + arc description
Layer 4: SILENCE DESIGN — deliberate absence for impact
```

### Audio Description Vocabulary

**Environmental/Ambient Sounds:**
- `footsteps on marble` / `gravel crunch` / `snow crunch`
- `rain pelting windows` / `wind howling through trees`
- `distant traffic hum` / `city ambiance`
- `flowing water` / `waves lapping`
- `crickets chirping` / `birds singing at dawn`
- `soft house sounds, the creak of a closet door, and a ticking clock`
- `electrical crackle` / `machinery hum`

**Action-Synchronized Foley:**
- `knife striking cutting board rhythmically, sizzling as ingredients hit hot pan`
- `the metallic clink of a coin`
- `glass shattering` / `sword impacts` / `weapon clashes`
- `thunder cracking overhead`
- `bridge collapse thunder` / `stone grinding`
- `fabric rustling` / `paper crinkling`

**Audio Quality Modifiers:**
- `reverb` → adds spatial depth
- `muffled` → suggests distance or barrier
- `high-pitched` → sharp, alerting
- `deep bass` → cinematic weight
- `echo` → large empty space
- `crisp` → close-proximity clarity
- `distorted` → mechanical, damaged

**Dialogue Formatting:**
- Enclose speech in double quotes: `The scientist turns to the camera and says: "We changed everything today."`
- Specify emotion: `whispers nervously`, `shouts firmly`, `speaks with wry humor`
- Specify language for lip-sync: `speaks in Mandarin`, `speaks in Japanese`

**Music Description Terms:**
- `soft ambient music` / `orchestral epic timing`
- `upbeat electronic beat` / `melancholic piano`
- `beat-synced editing` → visuals cut on musical beats
- `every strong beat triggers a cut or speed-ramped camera move`
- `no background music, only subtle tick` → selective sound isolation

### Audio API Parameter
- `audio: true` enables native audio generation
- `generate_audio: false` creates silent video
- Output: 48 kHz AAC stereo

---

## 4. Transition & Effect Control

### Transition Keywords That Work in Prompts
| Term | Effect |
|------|--------|
| `Cut to` | Hard scene change (most reliable) |
| `Flash cut` | Abrupt bright transition |
| `Quick cut` | Fast scene change with energy |
| `Match cut` | Visual match between two scenes (e.g., `match cut on sword`) |
| `Fade black` / `fade to black` | Gradual darken transition |
| `Cross-dissolve` | One image fades while next emerges |
| `Whip pan` | Fast horizontal blur transition |
| `Zoom into face, then flash cut` | Rapid focus transition |
| `Seamless transition` | Imperceptible shift maintaining continuity |
| `Shot switch` / `camera switch` | Signal scene transitions in multi-shot prompts |

### Multi-Shot Structure in Prompts
```
Shot 1: [Description] → Cut to →
Shot 2: [Description] → Cut to →
Shot 3: [Description]
```

Or timeline-based:
```
[0-5s] Setup: wide shot establishing scene...
[5-10s] Conflict: close-up, character reacts...
[10-15s] Climax: dynamic action, camera follows...
```

### VFX & Visual Effects Terms
- `shockwave propagation` / `explosive energy storm`
- `heat haze / shimmer` / `debris spray`
- `lightning arcs` / `particle light effects`
- `disintegrate to ash` / `elemental collision`
- `light trails` / `speed lines` (motion emphasis)
- `blinding flash finale`
- `confetti falls` (sound + visual sync)
- `mist-to-rainbow transition`

### Nine-Panel Structure (for action content)
```
Line 1 (0-5s):  Panel 1 | Panel 2 | Panel 3
Line 2 (5-10s): Panel 4 | Panel 5 | Panel 6
Line 3 (10-15s): Panel 7 | Panel 8 | Panel 9
```

---

## 5. Speed & Pacing Techniques

### Speed Control Terms for Prompts
| Term | Effect | Notes |
|------|--------|-------|
| `slow motion` | Temporal stretching, dramatic emphasis | Works reliably |
| `slow-mo 1 second` | Specific slow-motion moment | Pin to a specific beat |
| `time-lapse` / `time-lapse feel` | Accelerated temporal passage | Clouds, city, growth |
| `freeze frame` | Pause on key moment | Use with dramatic reveal |
| `speed ramp` | Variable speed within shot | `every strong beat triggers a speed-ramped camera move` |
| `fast-paced` | Rapid cuts and movements | Energy and urgency |
| `deliberately slow` / `contemplative` | Slow, intentional pacing | Art-house, emotional |
| `quick zoom` | Rapid focal length change | Emphasis, surprise |
| `speeds past at 120 mph` | Quantified velocity | More specific = better |

### Motion Speed Adverbs
- `slowly` / `gently` / `gracefully` → slow, elegant motion
- `quickly` / `frantically` / `vigorously` → fast, energetic motion
- `dramatically` / `powerfully` → impactful, weighted motion
- `smoothly` / `fluidly` → continuous, no jerks

### Pacing Architecture (Timeline Structure)
```
Setup (0-5s):    Slow, establishing — wide shot, ambient sounds
Conflict (5-10s): Medium speed, tension builds — tracking shot, music rises
Climax (10-15s):  Fast/slow-mo contrast — dynamic camera, peak audio
```

### Speed-Related Camera Modifiers
- `motion blur` → implies high speed
- `smooth stabilized` → implies controlled medium speed
- `handheld shaky` → implies urgency, documentary speed
- `slow dolly-in, 1-2 feet` → precise speed + distance specification

### Pro Tip: Reference Video for Pacing
Upload a reference video with `@Video1` to lock pacing:
```
Reference @Video1 for camera movement and pacing, [describe new content with different subject]
```

---

## 6. Mood → Camera + Light + Color Mapping

### Comprehensive Mood-to-Technical Mapping

| Mood/Emotion | Camera | Lighting | Color Grade | Movement |
|-------------|--------|----------|-------------|----------|
| **Power / Dominance** | Low angle, wide lens | Hard light, dramatic side lighting | High contrast, deep blacks | Slow push-in, steady |
| **Vulnerability / Isolation** | High angle, wide shot | Soft, diffused overhead | Desaturated, cool tones | Static or slow pull-out |
| **Hope / Warmth** | Eye-level, medium shot | Golden hour, backlight | Warm amber, lifted shadows | Slow dolly, gentle crane up |
| **Melancholy / Sadness** | High angle, shallow DoF | Overcast, flat lighting | Monochromatic blue, desaturated | Slow pan, static holds |
| **Mystery / Intrigue** | Dutch angle, shadows | Low key, rim lighting | Deep shadows, cold tones | Slow reveal pan, rack focus |
| **Urgency / Chaos** | Handheld, close-up | Harsh, flickering | High saturation, contrast | Whip pans, fast tracking |
| **Romance / Intimacy** | Close-up, shallow DoF | Golden hour, candlelight | Warm pastels, soft focus | Slow orbit, gentle push-in |
| **Fear / Dread** | Low angle, Dutch tilt | Underlit, single source | Desaturated green, cold blue | Slow push-in, subtle shake |
| **Joy / Energy** | Eye-level, wide | High key, bright | Vibrant saturated | Dynamic tracking, fast cuts |
| **Nostalgia** | Medium shot, deep focus | Soft warm light | Sepia, Kodachrome, film grain | Slow, contemplative |
| **Tension / Suspense** | Close-up alternating | Low key, contrast | Teal & orange, deep shadows | Slow dolly-in, hold |
| **Awe / Epic** | Wide shot, crane | Volumetric god rays | Rich, cinematic grade | Crane up, slow reveal |
| **Unease / Disorientation** | Dutch angle | Flickering, uneven | Color shift, cross-processed | Roll, unstable handheld |

### Camera Angle → Psychological Effect
- **Low angle** → subject appears powerful, dominant, threatening
- **High angle** → subject appears vulnerable, small, subordinate
- **Eye level** → neutral, relatable, documentary
- **Dutch angle** → unease, disorientation, instability
- **Bird's eye** → omniscient, detached, godlike perspective
- **Worm's eye** → extreme vulnerability or extreme power depending on subject

### Lighting → Emotional Tone
- **High key** (bright, minimal shadows) → comedy, optimism, commercial
- **Low key** (dramatic shadows) → thriller, noir, drama
- **Soft lighting** (diffused) → warmth, intimacy, romance
- **Hard lighting** (direct) → drama, harshness, truth
- **Backlighting** → mystery, divinity, separation from background
- **Rim lighting** → isolation, drama, futuristic
- **Volumetric fog** → atmospheric depth, mystery, epic scale
- **Dull fluorescent** → institutional, oppressive, mundane
- **Candlelight** → intimate, warm, historical, vulnerable
- **Three-point lighting** → professional, controlled, studio

---

## 7. Lens & Focal Length Simulation

### Do AI Video Models Understand Focal Length? YES.

Adding `lens + aperture + path language` improved output consistency from ~55% to ~72% across test clips (source: bonega.ai testing).

### Focal Length Reference Table
| Focal Length | Field of View | Visual Effect | Best For |
|-------------|---------------|---------------|----------|
| **14-20mm** | Ultra-wide | Dramatic distortion, exaggerated foreground, vast space | Landscapes, architecture, VFX |
| **24mm** | Wide | Slight distortion, spacious feel, environmental context | Establishing shots, action |
| **28mm** | Moderate wide | Natural wide perspective, minimal distortion | Street, documentary |
| **35mm** | Natural wide | "Normal" wide, cinematic standard | General cinematic, natural feel |
| **50mm** | Standard | Mimics human vision, no distortion | Documentary, dialogue, natural |
| **85mm** | Short telephoto | Background compression, subject isolation, flattering | Portraits, emotional close-ups |
| **100-135mm** | Medium telephoto | Strong compression, shallow DoF, intimate | Portrait, detail, beauty |
| **200mm+** | Telephoto | Heavy compression, flattened depth, distant subjects | Sports, surveillance, voyeuristic |
| **Macro** | Extreme close | Tiny subjects fill frame, extreme detail | Product, nature, texture |

### Aperture Terms
| Term | Effect |
|------|--------|
| `f/1.4` or `f/1.8` | Extremely shallow depth of field, pronounced bokeh, dreamy |
| `f/2.8` | Moderate separation, professional look |
| `f/4` | Balanced depth, slightly soft background |
| `f/8` | Sharp throughout, landscape clarity |
| `f/11-f/16` | Maximum sharpness, everything in focus |

### Lens Effect Terms
| Term | Visual Effect |
|------|---------------|
| `anamorphic lens` | Horizontal lens flares, oval bokeh, widescreen cinematic |
| `shallow depth of field` | Blurred background, subject isolation |
| `deep focus` | Multiple planes sharp simultaneously |
| `bokeh` | Aesthetic out-of-focus highlights |
| `lens flare` | Light artifacts from direct source |
| `rack focus` | Shift focus between foreground and background |
| `tilt-shift` | Miniature effect, selective focus band |

### Optimal Prompt Pattern
```
[shot type], [subject doing action], [setting], [focal length]mm lens, f/[aperture],
[lighting], [color grade], [camera movement]
```

Example:
```
Medium tracking shot of a woman in a flowing red dress walking through a sunlit
Victorian garden, 35mm lens, f/2.8, golden hour lighting, warm Kodachrome grade,
gentle camera movement following her from the side, shallow depth of field
```

---

## 8. Character Consistency (Latest Methods)

### The @Reference System Architecture

Seedance 2.0 uses `@` tags to create persistent pointers in the model's latent space:

**Slot Allocation Strategy:**
| Slots | Purpose | Priority |
|-------|---------|----------|
| @Image1-3 | **Face/Identity** (biological anchor) | HIGHEST — always include |
| @Image4-5 | **Outfit/Costume** references | HIGH — reduce wardrobe drift |
| @Image6-7 | **Style/Lighting** references | MEDIUM — visual consistency |
| @Image8-9 | **Environment/Background** | LOWER — scene-specific |
| @Video1-3 | **Motion/Camera/Pacing** references | Workflow-dependent |
| @Audio1-3 | **Rhythm/Dialogue/Ambient** | Workflow-dependent |

### Anchor-First Prompt Architecture

Split every prompt into two blocks:

**Block 1 — Immutable Character Anchor (never changes):**
```
Character: Mara, female-presenting barista, olive skin, short dark hair with
green beanie, small left nostril ring, left-handed, wry smile.
Keep these features unchanged.
```

**Block 2 — Variable Scene Block (changes per shot):**
```
Shot 3: Medium shot, Mara pours latte art in busy cafe, warm overhead lighting,
camera slowly orbits 45 degrees, soft ambient noise of espresso machine.
```

### Negative Anchors
Include explicit exclusions: `No mirrored features, no missing piercings, no outfit changes`

### Reference Image Rules (Reducing Drift ~60%)
1. Use maximum 2 consistent face reference images
2. Match angle, lighting temperature, and wardrobe across all references
3. NEVER mix full-frontal with profile shots (model invents features to reconcile)
4. Use 2K+ resolution reference images
5. Annotate references with metadata: `ref1_3q_warm_2026-02-03`

### Attention Fatigue Problem
The model weakens character consistency by Shot 4-5 in multi-shot sequences.

**Solution — Keyframe Injection:**
- Upload `@Character1` reference as "Start Frame" of every new scene
- Re-state the character anchor text at the beginning of every shot prompt
- The model weighs the **first 20-30 words** most heavily — always pin character there

### Seed Consistency
- Reuse the same `seed` value across shots to maintain underlying geometric structure
- Track seeds in a shot ledger: `Shot ID | Character Block | Seed | Timestamp`

### Consistency Prompt Additions
```
Keep the same character, same clothing, same hairstyle, no face changes, no flicker
Maintain facial features and wardrobe fully consistent with @Image1
Character from @Image1 must stay identical. Same face, hair, outfit.
Hands with perfect anatomy, text clear and readable
```

### Drift Recovery Protocol
1. **Recut**: Trim shots; hide mismatches with cutaways
2. **Composite**: Fix small losses (earrings, piercings) in post-production
3. **Regenerate**: Use fixed seed + strict character block for systemic drift

### QA Checklist Per Shot
- [ ] All immutable anchors present in prompt
- [ ] Accessories not lost (piercings, rings, glasses)
- [ ] No pose flips or lighting jumps
- [ ] Fixed seeds not overwritten
- [ ] Cross-shot color/specular consistency
- [ ] Micro-expression continuity

---

## 9. Chinese/Mandarin Prompt Techniques

### Language Support
Seedance 2.0 natively handles both English and Chinese prompts. The model was trained on massive Chinese-language datasets via ByteDance, meaning Chinese natural language descriptions can be highly effective.

### Jimeng (即梦) Access
- Platform: `jimeng.jianying.com` or `xyq.jianying.com`
- Select Seedance 2.0 model → upload references (@image / @video / @audio) → paste prompt → generate
- "Seedance 2.0" and "Seedance 2.0 fast" options available
- New accounts receive trial credits

### Chinese Prompt Formula (8 Dimensions)
```
主体 + 动作 + 场景 + 光影 + 镜头语言 + 风格 + 画质 + 约束
Subject + Action + Scene + Lighting + Camera Language + Style + Image Quality + Constraints
```

### Chinese Template Example
```
一位穿淡蓝色连衣裙的年轻女生，在林间小路缓慢行走，微风轻拂头发，自然微笑，
暖色阳光透过树叶洒下斑驳光影。中景，缓慢推镜，画面流畅稳定，无抖动。
治愈清新风格，4K高清，电影感，面部清晰不变形，人体结构正常，细节丰富。
```

Translation:
```
A young woman in a light blue dress, walking slowly on a forest path, breeze
gently blowing hair, natural smile, warm sunlight filtering through leaves casting
dappled shadows. Medium shot, slow push-in, smooth and stable image, no shake.
Healing fresh style, 4K HD, cinematic feel, face clear without distortion,
normal human structure, rich details.
```

### Five Counter-Intuitive Principles (from Chinese community)
1. **Avoid negative prompts** — positive framing works better (`detailed hands` > `no deformed hands`)
2. **Slower movement is better** — reducing camera speed reduces artifacts
3. **Avoid the word "好看" (nice/pretty)** — too vague, use specific aesthetic terms instead
4. **One event per video** — focus on a single action/moment per generation
5. **@reference is the killer feature** — leverage reference files heavily instead of relying on text alone

### Chinese-Specific Vocabulary

**场景词汇 (Scene Vocabulary):**
- 林间小路 (forest path) / 竹林 (bamboo forest) / 古城墙 (ancient city wall)
- 霓虹街道 (neon street) / 日式庭院 (Japanese garden) / 废墟 (ruins)

**光影词汇 (Lighting Vocabulary):**
- 暖色阳光 (warm sunlight) / 斑驳光影 (dappled light and shadow)
- 逆光剪影 (backlit silhouette) / 冷色调月光 (cool-toned moonlight)
- 霓虹灯光 (neon lighting) / 烛光 (candlelight)

**镜头语言 (Camera Language):**
- 缓慢推镜 (slow push-in) / 跟拍 (tracking shot) / 环绕拍摄 (orbit shot)
- 俯拍 (overhead shot) / 仰拍 (low angle) / 航拍 (drone shot)
- 特写 (close-up) / 中景 (medium shot) / 远景 (wide shot)

**风格词汇 (Style Vocabulary):**
- 电影感 (cinematic feel) / 治愈清新 (healing/fresh) / 赛博朋克 (cyberpunk)
- 水墨画风 (ink wash painting style) / 动漫风 (anime style)
- 复古胶片 (vintage film) / 写实风格 (realistic style)

**约束词汇 (Constraint Vocabulary):**
- 面部清晰不变形 (face clear without distortion)
- 人体结构正常 (normal human body structure)
- 画面流畅稳定 (smooth and stable image)
- 无抖动 (no shake) / 无闪烁 (no flicker)
- 细节丰富 (rich in detail) / 4K高清 (4K HD)

### When to Use Chinese vs English
- **Chinese works best for**: Cultural scenes (古风/古装), food content, Chinese landscape descriptions, emotional nuance in Chinese contexts, Jimeng platform
- **English works best for**: Western cinematic terminology, specific Hollywood lighting terms, technical camera vocabulary, Dreamina/CapCut international platform
- **Both work equally for**: Basic subject/action descriptions, color terms, general style terms
- **Bilingual trick**: Use English for technical camera/lighting terms within a Chinese prompt for maximum precision

### Doubao Access Tip
When using Doubao (抖包) interface: explicitly state `"Generate a video not an image, [prompt]"` — the platform defaults to image generation unless explicitly directed.

---

## Appendix A: Master Prompt Template (Copy-Paste)

### 5-Part Spine Structure
```
SUBJECT:      [Who/what — singular if possible]
ACTION:       [What they're doing — plain language, physics-based]
CAMERA:       [Shot size] + [movement] + [lens cue] + [speed]
STYLE:        [Single visual anchor reference] + [lighting] + [color grade]
CONSTRAINTS:  [Bans] + [timing] + [consistency notes]
```

### CRAFT Framework
```
C — Context:    Setting, time, atmosphere
R — Reference:  @Image1 as character, @Video1 for motion, @Audio1 for rhythm
A — Action:     What happens, with physics details
F — Framing:    Shot type, camera movement, lens, timing
T — Tone:       Audio cues, mood, music, silence
```

### Optimal Prompt Length
- **Sweet spot**: 120-280 words
- **Information hierarchy**: Subject → Action → Camera → Style (model weighs early words more)
- **First 20-30 words**: CRITICAL — pin subject and character identity here

### Reference Lock Template
```
@Image1 as first frame, @Image2 as character reference.
Reference @Video1 for camera movement and pacing.
@Audio1 for background music rhythm.
[Scene description with subject, action, camera, lighting, style]
Maintain facial features and wardrobe consistent with @Image1.
```

---

## Appendix B: Camera Movement Quick Reference

| Movement | Prompt Term | Effect |
|----------|-------------|--------|
| Approach subject | `slow dolly-in` | Intimacy, tension |
| Retreat from subject | `dolly-out` / `pull back` | Reveal context, isolation |
| Side movement | `truck left/right` / `crab` | Follow action laterally |
| Vertical lift | `crane up` / `pedestal up` | Dramatic reveal, power |
| Vertical lower | `crane down` | Discovery, grounding |
| Circle subject | `orbit` / `360 orbit` / `camera orbits` | Dynamic showcase |
| Follow behind | `tracking shot` / `camera follows` | Journey, pursuit |
| Horizontal sweep | `pan left/right` | Environmental reveal |
| Vertical sweep | `tilt up/down` | Scale reveal |
| Rapid direction change | `whip pan` | Energy, surprise, transition |
| Focus shift | `rack focus` | Attention redirect |
| Unstable movement | `handheld` | Documentary, urgency, raw |
| Smooth stabilized | `gimbal` / `steadicam` | Professional, polished |
| Subject-locked | `lock-on tracking` | Intimate follow |
| Aerial | `drone shot` / `aerial` / `航拍` | Establishing, epic |
| First person | `POV` / `POV dive` | Immersion |
| Reverse direction | `slingshot motion` | Dramatic reveal |
| Angular rotation | `dynamic camera rotation` / `roll` | Disorientation |
| Burst | `zoom burst` | Dynamic intensity |

---

## Appendix C: Complete Lighting Look Index

| # | Lighting Look | Key Prompt Terms | Palette |
|---|--------------|------------------|---------|
| 1 | Golden Hour | `sun-drenched, warm orange haze, backlit, long shadows` | Golds, oranges, soft yellows |
| 2 | Blue Hour | `twilight, cold tones, deep blue sky, melancholic` | Deep blues, cool cyans, soft purples |
| 3 | High Key | `bright and airy, low contrast, clean white` | Whites, light pastels |
| 4 | Silhouette | `backlit subject, high contrast, pitch black foreground` | Black vs bright background |
| 5 | Nordic Noir | `desaturated blue-grey, overcast, bleak, muted` | Desaturated blues, greys |
| 6 | Kodachrome | `vintage warm tones, analog look` | Rich reds, yellows, blues |
| 7 | Technicolor | `hyper-saturated, vintage cinema` | Bright primaries |
| 8 | Sepia | `monochromatic brown tint, Western aesthetic` | Browns, tans, creams |
| 9 | Film Noir | `chiaroscuro, high contrast monochrome` | Black, white, gray |
| 10 | CineStill 800T | `red halation, tungsten balance, cinematic night` | Warm tungsten + red glow |
| 11 | Bleach Bypass | `silver retention, desaturated, gritty` | Metallic grays, deep blacks |
| 12 | Teal & Orange | `blockbuster complementary, cyan-orange` | Teal shadows, orange highlights |
| 13 | Wes Anderson | `flat lighting, symmetrical, 35mm look` | Pastel pinks, mint greens |
| 14 | Solarpunk | `eco-futurism, lush greenery, bright sunlight` | Whites, greens, soft gold |
| 15 | Cyberpunk | `neon lighting, magenta-cyan, reflective, wet` | Neon pink, magenta, cyan |
| 16 | Steampunk | `brass-copper, Victorian industrial, golden steam` | Brass, copper, brown |
| 17 | Matrix Green | `fluorescent green, dystopian` | Computer green gradients |
| 18 | Candlelight | `fire glow, warm, deep shadows, chiaroscuro` | Warm oranges, deep blacks |
| 19 | Sodium Vapor | `orange streetlights, urban night, industrial` | Sickly orange, black shadows |
| 20 | Bioluminescence | `glowing plants, deep blue, magical, organic neon` | Glowing blues, electric greens |
| 21 | UV/Blacklight | `fluorescent glow, UV reactive, deep purple` | Purple + neon accents |
| 22 | Infrared | `Aerochrome, pink trees, surreal, false color` | Pink, white, deep blue sky |
| 23 | Thermal | `heat map, infrared camera, predator vision` | Rainbow gradients |
| 24 | Night Vision | `monochromatic green, surveillance, grainy` | Bright green and black |
| 25 | Duotone | `double color, pop art` | Two contrasting colors |
| 26 | Cross-Processed | `color shift, lomo, chemical imbalance` | Shifted greens/yellows |
| 27 | Selective Color | `monochrome with color splash, Sin City` | Grayscale + one vibrant color |

---

## Appendix D: Physics-Based Prompting Tips

Seedance 2.0 understands physics. Describe the physics, not just the action:

| Instead of... | Write... |
|---------------|----------|
| `car turns` | `The tires smoke as the car drifts 90 degrees` |
| `person walks in rain` | `Realistic rain physics, wet fabric clinging to skin` |
| `silk moves` | `Natural silk inertia, fabric catches light as it flows` |
| `explosion` | `Shockwave propagation, debris spray, heat haze shimmer` |
| `sand blows` | `Realistic sand dynamics, natural light transition through particles` |
| `steam rises` | `Steam expansion, mechanical inertia, condensation on surfaces` |
| `hair moves` | `Wind-driven hair physics, individual strands catching light` |
| `water splashes` | `Water surface tension breaks, droplets arc with gravity` |

---

*Sources: TechCrunch, CapCut Newsroom, fal.ai, Impakter, Vmake.ai, WaveSpeedAI, SeaArt, SeedanceTips, CrePal, Atlabs.ai, bonega.ai, venice.ai, Zhihu (知乎), GitHub (YouMind-OpenLab, ZeroLu, Emily2040), Adobe Firefly Docs, Promptomania, NxCode, BigPromptHub, ruvnet/Sora Prompts GitHub Gist*
