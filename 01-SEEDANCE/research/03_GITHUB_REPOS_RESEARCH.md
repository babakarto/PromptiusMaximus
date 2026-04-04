# Seedance 2.0 GitHub Repositories & Web Resources Research

**Date:** 2026-03-28

---

## TABLE OF CONTENTS

1. [Repository Index (Ranked by Stars)](#1-repository-index)
2. [REPO #1: songguoxs/seedance-prompt-skill (1,378 stars)](#2-repo-1-seedance-prompt-skill)
3. [REPO #2: ZeroLu/awesome-seedance (1,275 stars)](#3-repo-2-awesome-seedance)
4. [REPO #3: YouMind-OpenLab/awesome-seedance-2-prompts (403 stars)](#4-repo-3-youmind-openlab)
5. [REPO #4: gracech0322-cmd/seedance-2-prompt-library (23 stars)](#5-repo-4-prompt-library-6-dimension-framework)
6. [REPO #5: HuyLe82US/awesome-seedance-prompts (24 stars)](#6-repo-5-huyle82us-prompt-vault)
7. [REPO #6: Other Notable Repos](#7-repo-6-other-notable-repos)
8. [BEST EXACT PROMPTS EXTRACTED (Verbatim)](#8-best-exact-prompts)
9. [MASTER TEMPLATE FRAMEWORKS](#9-master-template-frameworks)
10. [OFFICIAL DREAMINA/SEEDANCE PROMPTS (18 Prompts)](#10-official-dreamina-prompts)
11. [NEGATIVE PROMPTS & CONSTRAINTS](#11-negative-prompts)
12. [ADVANCED TECHNIQUES & TIPS](#12-advanced-techniques)
13. [EXTERNAL WEB RESOURCES](#13-external-web-resources)
14. [COMMERCIAL USE CASE PROMPTS (Chinese)](#14-commercial-chinese-prompts)
15. [MOYIN CREATOR - Production Tool with Seedance 2.0](#15-moyin-creator)

---

## 1. REPOSITORY INDEX

| # | Repository | Stars | URL | Focus |
|---|-----------|-------|-----|-------|
| 1 | songguoxs/seedance-prompt-skill | 1,378 | https://github.com/songguoxs/seedance-prompt-skill | Claude Code skill for generating Seedance prompts |
| 2 | ZeroLu/awesome-seedance | 1,275 | https://github.com/ZeroLu/awesome-seedance | Ultimate prompt collection + API guides |
| 3 | MemeCalculate/moyin-creator | 2,506 | https://github.com/MemeCalculate/moyin-creator | AI film production tool with Seedance 2.0 |
| 4 | YouMind-OpenLab/awesome-seedance-2-prompts | 403 | https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts | 500+ curated prompts with video examples |
| 5 | HuyLe82US/awesome-seedance-prompts | 24 | https://github.com/HuyLe82US/awesome-seedance-prompts | 13-category prompt vault with individual files |
| 6 | gracech0322-cmd/seedance-2-prompt-library | 23 | https://github.com/gracech0322-cmd/seedance-2-prompt-library | 6-Dimension framework prompt library |
| 7 | ZeroLu/seedance2.0-how-to | 20 | https://github.com/ZeroLu/seedance2.0-how-to | Access guide + prompt engineering tutorial |
| 8 | EvoLinkAI/awesome-seedance-2-guide | 17 | https://github.com/EvoLinkAI/awesome-seedance-2-guide | Complete guide with use cases |
| 9 | weshopai/awesome-Seedance-2.0-prompt | 16 | https://github.com/weshopai/awesome-Seedance-2.0-prompt | Curated library with API docs |
| 10 | marsoyang1/awesome-seedance-prompts | 14 | https://github.com/marsoyang1/awesome-seedance-prompts | 20+ Chinese templates with storyboards |
| 11 | rich5000/seedance-prompt-guide | 13 | https://github.com/rich5000/seedance-prompt-guide | Prompt engineering guide (bilingual) |
| 12 | seedanceprompts/seedance-prompts | 1 | https://github.com/seedanceprompts/seedance-prompts | Curated resource aggregator |

---

## 2. REPO #1: songguoxs/seedance-prompt-skill (1,378 stars)

**URL:** https://github.com/songguoxs/seedance-prompt-skill
**Type:** Claude Code Skill for auto-generating Seedance 2.0 prompts
**Language:** Chinese output

### Ten Core Capabilities

1. **Pure Text Generation** -- Text-only descriptions without reference materials
2. **Consistency Control** -- Reference images for visual coherence
3. **Camera & Motion Replication** -- Referencing video sources for movement patterns
4. **Creative Template/VFX Replication** -- Mimicking effects from existing videos
5. **Story Completion** -- Generating narratives from storyboard images
6. **Video Extension** -- Lengthening existing clips with continuity
7. **Sound Control** -- Dialogue, voice synthesis, and audio design
8. **One-Take Long Shot** -- Seamless continuous scenes without cuts
9. **Video Editing** -- Character/plot modifications in existing footage
10. **Music Beat Sync** -- Aligning visuals to rhythmic elements

### Structural Templates

**Timestamp Storyboarding Format:**
```
"0-5 seconds: [description], 6-10 seconds: [description], 11-15 seconds: [conclusion]"
```

**Reference Material Syntax:**
- Images: `@图片1` through `@图片9`
- Videos: `@视频1` through `@视频3`
- Audio: `@音频1` through `@音频3`

### Core Prompt Formula
```
素材角色指定 + 动作/剧情描述 + 镜头语言 + 氛围/音效指令
(Material reference + Action/narrative + Camera language + Atmosphere/audio)
```

### Key Rules
- All prompts require Chinese-language descriptions
- Platform automatically blocks reference materials containing photorealistic human faces
- Max 15-second segments; longer videos require segmented generation with extension
- Always specify: aspect ratio (16:9, 9:16, 1:1), duration (4-15s), color grading, lens style

---

## 3. REPO #2: ZeroLu/awesome-seedance (1,275 stars)

**URL:** https://github.com/ZeroLu/awesome-seedance
**License:** CC BY 4.0

### 8 Primary Categories

1. **Cinematic Film Styles** -- Director-inspired approaches (Wong Kar-wai, Denis Villeneuve, Le Mans)
2. **Advertising & Commercial Branding** -- Product/brand storytelling
3. **Social Media & Viral Memes** -- Attention-grabbing content
4. **UGC Style** -- User-generated aesthetic with surreal twists
5. **Anime & Animation Styles** -- Character consistency, dynamic motion
6. **Short-form Drama & Web Series** -- Narrative structures
7. **Visual Effects & Experimental Styles** -- Advanced techniques
8. **Resources** -- API guides and workflow documentation

### Key Techniques from This Repo

**Shot-by-Shot Timeline Coding:**
```
[HH:MM-HH:MM] Shot #: [Title] (Thematic label)
```

**Emotional Performance Mapping:**
- Specifies microexpressions, restraint levels, psychological states
- Example: "The ultimate restraint and loneliness of 'wanting to touch but drawing back'"

**Physics Simulation Instructions:**
- Details debris trajectory, collision effects, liquid behavior
- Tests acceleration from stillness, high-speed dueling consistency

**Particle Continuity Transitions:**
- Shattered elements transform between scenes maintaining logical flow
- Creates smooth match-cut editing via visual element metamorphosis

### Prompt Sources
Curated from X (Twitter) creators: @johnAGI168, @op7418, @BFAVicky, @Lucy_love_AI, @Adam38363368936, @mollick, and WeChat communities.

---

## 4. REPO #3: YouMind-OpenLab/awesome-seedance-2-prompts (403 stars)

**URL:** https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts
**Claims:** 1,236 total prompts, 6 featured examples

### Featured Prompts

1. **Surreal Ronin Action Scene** (English, by Dheepan Ratnam)
2. **Luxury Car Transforming into Optimus Prime** (English, by HopefulofNFTs)
3. **Live-Action Anime Adaptation: Water vs Thunder Breathing Duel** (Chinese, by John)
4. **Anime Girl Stage Dance with Motion Capture** (Chinese, by Jackywine)
5. **Speeder Chase Across Cliff City** (English, by Umesh)
6. **Bollywood Dance Distracted Boyfriend Meme** (English)

### Additional Notable Entries
- Wedding Disaster Cinematic Sequence (30-shot, 15-second comedy)
- K-Pop Concert Video (handheld 4K 120fps)
- Streetball Wizard vs. Three Defenders (stylized 3D)
- HK Neo-noir Action Film (SPL-style martial arts)
- Porcelain-punk Martial Arts Dance (Kintsugi aesthetic)
- Cyber Wuxia Fight Sequence (four-scene storyboard)

---

## 5. REPO #4: gracech0322-cmd/seedance-2-prompt-library (23 stars)

**URL:** https://github.com/gracech0322-cmd/seedance-2-prompt-library
**Standout Feature:** The 6-Dimension Framework -- the most structured template system found

### The 6-Dimension Prompt Framework

#### Dimension 1: INPUT LAYER
```
@[Asset A] as [Use Case], @[Asset B] for [Use Case], @[Asset C] for [Use Case]
```
Example:
```
@Image1 as first frame, @Video1 for camera movement, @Video2 for character motion, @Audio1 for background music
```

#### Dimension 2: CONTENT LAYER
```
[Style]. @[Asset] [Character] in [Environment] is [Action]. [Character] with [Emotion] says "[Lines]". Background is [Sound Effects].
```

#### Dimension 3: STYLE LAYER
- **Visual Style:** Portrait, animation, Chinese style, film look
- **Lighting:** Side light, Rembrandt lighting, texture light, god rays
- **Color Tone:** Purple as main color, dark base tone, high saturation
- **Texture:** Film grain, soft blur, glowing effects
- **Atmosphere:** Elegant, mystical, healing, premium, moody, lazy
- **Music:** Rhythm, emotion, beat sync, instrument types

#### Dimension 4: CAMERA LAYER
```
From [Camera Angle], [Movement] to [Shot Size], using [Camera Rules].
```
Elements:
- **Shot Size:** Long, medium, close-up, extreme close-up
- **Angle:** Eye level, high angle, low angle, POV
- **Movement:** Zoom in/out, pan, tilt, crane shot, static
- **Rules:** One-take, no cuts, match cut, steady follow shot

#### Dimension 5: STRUCTURE LAYER (Timeline)
```
0-X seconds:
[I @Assets / II Content / III Camera]

X-Y seconds:
[I @Assets / II Content / III Camera]
(Note: Action/emotion change and camera transition?)

Y-Z seconds:
[I @Assets / II Content / III Camera]

Ending (Optional):
[Closing Method: Freeze frame / Camera stop / Lingering emotion]
```

#### Dimension 6: EDIT LAYER
```
[Action] @Video1 (Extend by [X]s / Re-plot / Replace [A] with [B]),
[New Details: I @Assets / II Content / III Camera], while keeping the
original [Style/Camera/Character].
```
Edit Types:
- **Extend** -- Add seconds to final frame
- **Partial Edit** -- Modify specific elements (hair color, clothing)
- **Replace** -- Change protagonist or product
- **Re-Plot** -- Rewrite story while keeping characters/environment

### Genre Templates (Fill-in-the-Blank)

**Cinematic:**
```
Cinematic film style. ___ (main character) in ___ (location).
Camera ___ (camera movement).
Lighting ___ (lighting style).
___ (main action happening).
Atmosphere: ___ (fog / rain / dramatic light).
End with ___ (epic final shot).
```

**Anime & Animation:**
```
Anime style animation. ___ (character description).
Location: ___ (fantasy place / city / battlefield).
The character ___ (action or attack).
Energy / effects: ___ (light, magic, particles).
End with ___ (dramatic anime pose).
```

**AI Short Series:**
```
___ style. ___ (character description) in ___ (place / time / mood).
___ (what happens / action).
___ (extra emotion or atmosphere).
Dialogue:
___ says, "___."
___ replies, "___."
End with ___ (final shot / subtitle / fade to black).
```

**Commercial & Ads:**
```
Luxury commercial style.
A ___ (product) placed on ___ (surface / environment).
Camera ___ (slow rotation / macro shot).
Lighting ___ (soft light / dramatic light).
The product ___ (main highlight moment).
End with ___ (brand style final shot).
```

---

## 6. REPO #5: HuyLe82US/awesome-seedance-prompts (24 stars)

**URL:** https://github.com/HuyLe82US/awesome-seedance-prompts
**License:** CC BY 4.0
**Standout Feature:** 13 organized categories with individual markdown files per prompt

### 13 Categories (with file count)

| # | Category | Files |
|---|----------|-------|
| 01 | Cinematic & VFX | 11 prompts |
| 02 | Commercial & Product | multiple |
| 03 | UGC & Social | multiple |
| 04 | Action & Fight | 5 prompts |
| 05 | Anime & Manga | 5 prompts |
| 06 | Drama & Romance | multiple |
| 07 | Fantasy | 4 prompts |
| 08 | Horror | 3 prompts |
| 09 | Sci-Fi & Cyberpunk | 2 prompts |
| 10 | Nature & Documentary | multiple |
| 11 | Epic & Large-Scale Spectacle | 1+ prompts |
| 12 | Superhero & Powers | 2 prompts |
| 13 | Comedy & Meme | 2 prompts |

---

## 7. OTHER NOTABLE REPOS

### marsoyang1/awesome-seedance-prompts (14 stars)
**URL:** https://github.com/marsoyang1/awesome-seedance-prompts
- 20+ Chinese templates with complete storyboards
- 8 curated prompt types: Girlfriend POV Romance, Live Commerce, CEO Drama, Suspense Comedy (Mirror), Epic Fantasy Battle, Comedic Sketch, ASMR Cooking, K-Drama Romance
- Uses audio cue notation: `【音效】` for sound effects

### MemeCalculate/moyin-creator (2,506 stars)
**URL:** https://github.com/MemeCalculate/moyin-creator
- Full film production pipeline tool with Seedance 2.0 as final output
- 5-stage pipeline: script -> characters -> environments -> storyboards -> video
- Three-layer prompt fusion: action + camera language + lip-sync alignment
- Enforces Seedance limits: max 9 images + 3 videos + 3 audio, prompt max 5000 chars

### ZeroLu/seedance2.0-how-to (20 stars)
**URL:** https://github.com/ZeroLu/seedance2.0-how-to
- Step-by-step guide to access Seedance 2.0 (Jimeng/Dreamina) outside China
- Includes prompt engineering tutorials

---

## 8. BEST EXACT PROMPTS EXTRACTED (Verbatim)

### 8.1 Islands of Thunder (Cinematic Action)
```
A surreal battlefield in the sky: floating rock islands drifting through a thunderstorm, clouds swirling below like an ocean. The masked ronin dashes across the drifting platforms, pursued by a colossal winged beast whose chest is a swirling vortex of storm clouds and lightning. The camera hurtles from island to island, struggling to keep up as rocks tilt, spin, and crumble away beneath them. Every wingbeat sends shockwaves through the air, shaking the frame and blowing debris and rain straight into the viewer's face. Rapid handheld cuts capture the ronin leaping impossible gaps, sword carving arcs of light that briefly cut through the darkness. The finale shows the camera diving behind him as he jumps off the last crumbling rock, riding a bolt of lightning directly into the monster's chest vortex with a final, all-or-nothing slash that explodes the storm from within and clears the sky in a blinding flash. 720p 16:9 15 seconds
```

### 8.2 Cathedral Beneath the Black Sea (Underwater Horror/Action)
```
A flooded subterranean megastructure, ancient stone corridors half-submerged in black water, bioluminescent algae pulsing along the walls like a heartbeat. A masked diver in scarred tactical gear, lit by a flickering wrist-mounted flare, is pulled downward through collapsing flooded chambers by the current of a colossal eyeless leviathan moving beneath the floor grates. The camera plunges after the diver as water rushes through shattering stone archways, air bubbles and debris spiraling past the lens. The diver grabs a broken pillar to stop herself, the current ripping at her body, then releases and freefalls through a vertical shaft, twisting to dodge the leviathan's translucent tendrils whipping upward through the darkness. Quick shaky frames catch her igniting a harpoon gun mid-fall, the flare illuminating the creature's massive jaw opening below. In the final movement, the camera spirals downward around her as she fires the harpoon into the creature's mouth, the bioluminescence erupts blinding white, and the camera bursts through the surface of a vast underground ocean, the diver silhouetted against the glow of a thousand pulsing organisms on a cathedral-sized cavern ceiling. 15 seconds.
```

### 8.3 Indian Bollywood Action (Exaggerated Physics)
```
【Style】 An Indian Telugu action blockbuster (Tollywood Action Blockbuster), featuring extremely exaggerated anti-gravity physics, slow-motion slow motion and fast-slow-motion transitions (Ramp-mo), dusty scenes, an epic BGM atmosphere, no gore, and a focus on impact. 【Duration】15 seconds 【Scene】A dusty abandoned quarry or construction site, with strong sunlight and a strong wind. 【Characters】 Protagonist (Hero): With a signature beard, sunglasses, and a denim jacket, he walks with a confident and domineering air. Opponents (Goons): Dozens of thugs dressed in haphazard clothes, whose main purpose is to be knocked away. 【Scene Breakdown】

[00:00-00:05] Shot 1: The Hero Entry and the Hero's Arrival Visuals: Extremely slow motion (Super Slow-mo). The protagonist walks slowly, with a whirlwind of yellow sand behind him. Action: He casually raises his hand and waves it (it doesn't seem to use much force). Special Effects: Just the palm wind causes the five thugs at the front to fly backward like kites with broken strings, defying the laws of physics (flying at least 15 meters high), spinning slowly in the air.

[00:05-00:10] Scene 2: Newton's Laws Defied (Physics Defied) Visuals: Fast and slow motion switching. The protagonist instantly accelerates and rushes into the crowd. Action: The protagonist delivers a spinning kick. The target hits instantly knocks down ten people behind him, creating a domino effect. Special Effects: A huge shockwave causes a ring of dust to explode on the ground. All the thugs, upon contact with the protagonist's fists and feet, are exaggeratedly ejected in all directions with large amounts of white dust (representing blood), smashing surrounding wooden crates and props.

[00:10-00:15] Scene 3: The Ultimate Power Move. Scene: The protagonist removes his sunglasses and gives the camera a wicked smile (Blinking Moment). Action: A jeep rushes towards him. He doesn't dodge or flinch, but kicks it head-on. Special Effects: The jeep, upon contact with his toes, is kicked vertically into the air like a toy car, tumbling and scattering parts everywhere. Amidst the falling car parts and flying thugs in the background, the protagonist calmly puts his sunglasses back on and fixes his hair.
```

### 8.4 Reflection Anomaly (15s Horror)
```
【Style】Mockumentary (Vlog Style), hyperrealism, fixed camera angle, natural lighting, with a touch of suspense and thriller. 【Duration】15 seconds 【Main Character (Remember to upload reference image)】A sexy young woman preparing to wash up and go to bed in front of the sink in her bathroom.

[00:00-00:06] Shot 1: Normalcy. Scene: In front of a large mirror in a normal bathroom. Action: The protagonist is brushing her teeth in front of the mirror, her mouth full of foam. While brushing her teeth, she makes various funny faces (winking and making faces) in the mirror. Key Detail: At this moment, the reflection in the mirror is completely normal, and the actions are synchronized.

[00:06-00:11] Shot 2: The Glitch. Action: After brushing her teeth, the protagonist bends down to spit out the foam, then turns to leave the bathroom. High-Energy Moment (Core Breakthrough): Just as the protagonist's real body has turned and left the mirror's frame, the "reflection" in the mirror **doesn't move**! The "reflection" remained in the brushing-teeth pose, even raising an eyebrow at the camera with a wicked grin, lingering for a full two seconds before suddenly and frantically "flashing" to catch up with the main body and disappearing. Director's Note: To create an extremely realistic "network latency" feel, the reflection should have an independent consciousness.

[00:11-00:15] Shot 3: The Punchline. Action: The protagonist, who had already reached the door, seemed to sense something was wrong and abruptly turned to look at the mirror. Result: The mirror had now completely returned to normal, empty except for the opposite wall. The protagonist, bewildered and frightened, looked around the room with a horrified expression. The scene freezes on the protagonist's bewildered face (horror movie effect).
```

### 8.5 Photoreal Elemental Sword Sequence (Fantasy VFX)
```
【Style】Hollywood Live-Action Blockbuster, IMAX movie quality, 8K ultra-high definition, photorealistic cinematography, dark fantasy, Unreal Engine 5 realistic rendering, no anime feel. 【Duration】15 seconds 【Scene】A realistic misty forest under the moonlight, with damp soil and real fallen leaves on the ground.

[00:00-00:05] Shot 1: Live-Action Performance - Water Breathing (Realistic Water FX). 【Close-up】An Asian young swordsman (the pores on the actor's face are visible), wearing a green and black checkered coarse cloth haori (the fabric texture is clear). Action: He holds his sword with both hands under the moonlight, lowering his center of gravity. Special Effects: As he breathes, instead of cartoonish water flow, highly realistic, transparent, and luminous pressurized high-pressure water flow (Hyper-realistic Fluid Simulation) condenses on the blade. The water, like a living dragon, coils around the realistic sword blade, water droplets splashing onto the lens and refracting moonlight.

[00:05-00:10] Shot 2: Lightning Plasma. [Medium Shot/High-Speed Photography] Opposite is a young swordsman with dyed blond hair (real hair flowing), wearing a yellow triangular-patterned fabric jacket. Action: He makes the starting stance for an iaido slash, the ground beneath his feet cracking due to the excessive force. Effects: Real, blinding blue-white electric currents (Real Plasma Arcs) erupt in the air, instead of yellow cartoon lightning. The current pierces through the surrounding real trees, leaving scorched marks.

[00:10-00:15] Shot 3: Fated Showdown - Physics Clash. [Slow Motion/Big Explosion] The two collide at high speed in the center of the frame. Action: The solid water giant sword collides violently with the lightning blade. Effects: No comic book lines, only real physical particle explosions. Large amounts of water vapor, mud, broken tree branches, and dazzling sparks flew through the air. The shockwave created realistic ripples in the water beneath their feet. The scene was incredibly powerful and destructive.
```

### 8.6 Chrome Wraith in Blue Light (Dark Fantasy Portrait)
```
A dark, fantastical female figure, with flowing long hair and an intricate metal crown topped with sharp, antler-like points, her eyes closed, her expression serene, her pale skin softly glowing. Her forearms and torso are transformed into smooth, black liquid metal with reflective chrome details, and sharp, claw-like fingers extend from the darkness. Dramatic backlighting creates a halo effect around her head, a cool blue-toned misty atmosphere, cinematic lighting, rich detail, surreal yet elegant—a dark fantasy aesthetic.
```

### 8.7 Anime Healing Girl (Copy-Paste Ready)
```
An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat, standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the camera and smiles gently. A light breeze moves her hair and dress. The camera slowly pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion, high detail.
```

### 8.8 Cyberpunk Music Video Beat Sync
```
A trendy cyberpunk girl dancing in a neon city street at night. Every strong beat triggers a cut or speed-ramped camera move. Neon signs reflecting on wet ground. Cyberpunk style, fast-paced editing, multi-shot continuity. Dance movements and character appearance remain consistent.
```

### 8.9 Lonely Robot Multi-Shot Story
```
A lonely robot wakes up in an abandoned factory (Scene 1). It walks outside and sees a sunset wasteland (Scene 2). It discovers a small flower and gently touches it (Scene 3). Finally, it looks up and smiles at the sky (Scene 4). Keep robot appearance consistent. Emotional transition from confusion to warmth. Cinematic camera, warm tones, epic mood, no flicker.
```

### 8.10 Product 360-Degree Rotation (Commercial)
```
A minimalist black matte mechanical keyboard on a pure white infinite studio background, rotating smoothly 360 degrees clockwise. RGB lighting gently breathing. Keycap text sharp and readable. Fixed macro camera, smooth turntable motion, commercial product photography style, soft high-key lighting, no noise. Logo and text remain perfectly consistent.
```

### 8.11 Wuxia Rain Fight (Action)
```
A wuxia-style male hero (based on reference video character), wearing black martial outfit, fighting enemies in a rainy bamboo forest at night. Fast sword combos with visible sword light trails and splashing water. Fast follow camera, crane shots, and quick close-ups. Cinematic camera language. Maintain character appearance and clothing consistency. Realistic physics, wet fabric, rain interaction.
```

### 8.12 Giant Monster Chase (Arcane Style)
```
Generate a video about a running scene, behind is a giant monster big as a building with 100 floor is coming close, using Arcane style.
```

### 8.13 Luxury Car Transforms into Optimus Prime
```
a luxury car transforming into Optimus Prime and battling Godzilla amidst explosions and energy blasts against the backdrop of a rainy Tokyo nightscape
```

### 8.14 Chaotic Waffle House Meme
```
An average shift at Waffle House - make sure it's chaotic and gets 50 likes.
```

### 8.15 Live Action Saiyan Battle
```
Live action Saiyan battle between Goku & Vegeta, super saiyan blue
```

### 8.16 Girlfriend POV Romance (Chinese Template)
```
极致第一人称女友视角(Ultimate Girlfriend POV)，手持自拍VLOG，竖屏(9:16)，胶片感滤镜
```
- First-person handheld format with natural lighting
- Vertical 9:16 aspect ratio
- Film grain aesthetic with golden hour lighting

### 8.17 Live Commerce Selling (Chinese Template)
```
抖音直播带货风，极速语速(Rap-like Speed)，情绪极其亢奋
```
- Rapid-fire delivery with high energy
- Split-screen comparisons of inferior vs. premium products
- Call-to-action urgency tactics

### 8.18 CEO Drama/Reversal (Chinese Template)
```
国产神豪爽剧（Viral CEO Drama），竖屏构图（Portrait Mode），高饱和度滤镜
```
- Extreme close-ups of facial expressions
- High saturation color grading
- Multiple emotional reversals within 15 seconds

---

## 9. MASTER TEMPLATE FRAMEWORKS

### Framework A: Director-Level Structure (Most Common)
```
Subject + Action + Camera + Scene + Style + Constraints
```

### Framework B: WaveSpeed 5-Part Anatomy
```
Subject: [one person/object, age or material if relevant]
Action: [specific verb phrase, present tense]
Camera: [shot size] + [movement] + [angle], [focal length]
Style: [one visual anchor: film/process/artist], [lighting], [color treatment]
Constraints: [ban list], [frame rate/tempo], [duration or beat timing], [consistency notes]
```

### Framework C: 6-Dimension System (gracech0322-cmd)
```
I. INPUT:    @Assets with use-case labels
II. CONTENT:  Style + Character + Environment + Action + Emotion + Dialogue + Sound
III. STYLE:   Visual style + Lighting + Color + Texture + Atmosphere + Music
IV. CAMERA:   Angle + Movement + Shot Size + Rules
V. STRUCTURE: Timeline segments with per-dimension detail
VI. EDIT:     Extend / Partial Edit / Replace / Re-Plot instructions
```

### Framework D: Chinese Production Formula (songguoxs)
```
素材角色指定 + 动作/剧情描述 + 镜头语言 + 氛围/音效指令
```

### Framework E: Scene Breakdown Template
```
【Style】[genre/aesthetic] 【Duration】[X] seconds 【Scene】[environment]
【Characters】[descriptions]

[00:00-00:05] Shot 1: [Title]
  Visuals: [description]
  Action: [what happens]
  Special Effects: [VFX details]

[00:05-00:10] Shot 2: [Title]
  ...

[00:10-00:15] Shot 3: [Title]
  ...
```

---

## 10. OFFICIAL DREAMINA/SEEDANCE PROMPTS (18 Prompts from dreamina.capcut.com)

### Viral Video & Social Content
1. `Create a fast-paced video of a cat knocking over objects with exaggerated reactions, meme-style captions, and quick zooms for comedic effect.`
2. `Show a morning routine of a college student with upbeat background music, jump cuts between scenes, and text overlays highlighting key moments.`
3. `Film a short recipe tutorial with close-up shots of ingredients, step-by-step instructions, and vibrant visual transitions.`

### Character & IP Consistency
4. `Animate a superhero performing a signature move across different city rooftops while keeping costume, hairstyle, and facial features consistent.`
5. `Show a brand mascot interacting with multiple environments, such as a park, office, and home, without changing its color palette or expressions.`
6. `Bring a comic book hero into a new storyline, fighting villains while maintaining outfit, posture, and animation style.`

### Style & VFX Transfer
7. `Transform a daytime city street into a neon-illuminated cyberpunk environment with rain reflections, animated signs, and moving vehicles.`
8. `Apply a dramatic cinematic style to a football highlight clip with slow-motion kicks, dynamic camera angles, and vivid color grading.`
9. `Convert a forest animation into a magical fantasy scene with glowing plants, floating lights, and mystical fog effects.`

### Brand Marketing & Campaign
10. `Show a product unboxing with close-up shots, animated text highlighting features, and smooth panning to focus on brand logos.`
11. `Create a lifestyle ad showing people using the product in different daily scenarios, keeping brand colors and logo visible.`
12. `Film a promotional offer with animated countdowns, text overlays showing discounts, and bright brand-themed visuals.`

### Film, Game, Creative Previz
13. `Storyboard a chase scene in a busy city with multiple camera angles, dynamic character movements, and realistic environmental interactions.`
14. `Visualize a fantasy battle between heroes and monsters in a forest with magic effects, detailed terrain, and animated camera sweeps.`
15. `Create a cinematic intro for a short film with a character entering a dimly lit room, dramatic camera pans, and suspenseful music.`

### Creative & Interactive Design
16. `Animate a virtual classroom where students interact with 3D objects while the AI teacher reacts in real-time to their actions.`
17. `Design an AR shopping experience where users click on products, view details, and see animated previews with realistic shadows.`
18. `Create an interactive storytelling video where viewers make choices, and characters respond differently depending on the path selected.`

---

## 11. NEGATIVE PROMPTS & CONSTRAINTS

### CRITICAL FINDING: Seedance 2.0 Does NOT Support Negative Prompts

Seedance 2.0 does not have a negative prompt field. Negative prompts can paradoxically introduce the very concepts you're trying to avoid ("no extra hands" makes the model think about hands).

### Use Positive Constraints Instead

**Instead of negative prompts, append positive constraint lines:**
```
Maintain face and clothing consistency, no distortion, high detail.
```

```
Exclude: blur, low quality, noise, watermarks, text, logo, distortion, facial collapse, stiff movements, frame jitter, proportion issues
```

**Quality boosters (positive framing):**
- `Detailed hands, Anatomically correct` -- improved anatomy
- `Physically accurate, Natural motion` -- better movement
- `Ultra sharp, Masterpiece` -- higher visual quality

### If Using Third-Party Platforms That Accept Negative Prompts
Keep them short and specific to actual failures you see:
```
no jitter, no warping, no flickering, no identity drift
```
```
no text morphing, no garbled logos, no color shift
```

### Common Exclusion Line (weshopai repo)
```
Exclude: blur, low quality, noise, watermarks, text, logo, distortion, facial collapse, stiff movements, frame jitter, proportion issues
```

---

## 12. ADVANCED TECHNIQUES & TIPS

### Keyword-Triggered Effects (EvoLinkAI)
- **Hitchcock zoom:** `"protagonist in panic with Hitchcock zoom"`
- **Circular camera:** `"robotic arm multi-angle circular movement"`
- **Accelerating speed:** `"speed accelerates like a roller coaster"`
- **Particle effects:** `"golden sand particles scatter"` or `"particle dispersion effect"`

### Camera Language Rules (gracech0322-cmd)
- Do NOT use adjectives for camera language -- use rules instead
- NOT: "cinematic camera" / USE: "one-take, no cuts"
- NOT: "beautiful angle" / USE: "low angle crane shot rising to bird's-eye view"
- Use specific rig metaphors: dolly, track, crane, handheld, gimbal
- One verb per shot prevents chaos; compound moves as sequential beats

### Physics Description for Realism
- Do NOT say "car turns" / DO say "The tires smoke as the car drifts 90 degrees"
- Replace vague language ("character is sad") with specific details ("tears slide down cheeks, mouth trembles")
- This tells the AI to calculate weight and force

### Extended Video Strategy
1. Generate a perfect 5-10 second base clip
2. Upload that clip as `@video1` reference
3. Write extension prompt with explicit continuity notes
4. Specify character positioning and environmental consistency between segments

### Input Limits (Hard Constraints)
| Type | Limit | Size |
|------|-------|------|
| Images | Max 9 | <30MB each |
| Videos | Max 3 | <50MB, 2-15s duration |
| Audio | Max 3 | <15MB, max 15s |
| Combined files | Max 12 total | -- |
| Prompt text | Max 5,000 characters | -- |
| Output duration | 4-15 seconds | -- |
| Output resolution | Up to 720p (some sources say 2K) | -- |

### Consistency Tips
- Add explicit constraints: "Keep the same character, same clothing, same hairstyle, no face changes, no flicker"
- Use larger centered text to avoid distortion
- Avoid fast hand close-ups (common failure mode)
- Reference images with detailed proportion guidance for character consistency

### Timestamp Best Practice
- Always use bracket notation: `[00:00-00:05]`
- 3-5 second segments for maximum control
- Include emotional/sensory beats integrated into action descriptions

---

## 13. EXTERNAL WEB RESOURCES

### Dedicated Prompt Websites
| Site | URL | Content |
|------|-----|---------|
| Seedance2Prompt.org | https://seedance2prompt.org/ | 500+ prompts with examples |
| SJinn AI | https://sjinn.ai/seedance-prompts | 226 prompts with video previews |
| Seedance2.tech | https://seedance2.tech/prompts | Prompt library |
| Atlas Cloud | https://www.atlascloud.ai/seedance-2-prompt | Prompt collection |

### Prompt Engineering Guides
| Guide | URL |
|-------|-----|
| Imagine.art (70 prompts) | https://www.imagine.art/blogs/seedance-2-0-prompt-guide |
| GLBgpt (5 copy-paste) | https://www.glbgpt.com/hub/seedance-2-0-prompt-guide/ |
| SeaArt (20+ examples) | https://www.seaart.ai/blog/seedance-2-0-prompt |
| Atlabs AI Guide | https://www.atlabs.ai/blog/seedance-2-prompts-guide |
| WaveSpeed Template | https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/ |
| WeShop AI Guide | https://www.weshop.ai/blog/seedance-2-0-guide-how-to-master-the-prompt-script/ |
| Redreamality Playbook | https://redreamality.com/blog/seedance-2-guide/ |
| Seedance2.today Tutorial | https://www.seedance2.today/blog/best-seedance-prompt-engineering-guide-master-multi-shot-tutorial-2026 |
| Official Dreamina (18 prompts) | https://dreamina.capcut.com/resource/seedance-2-0-prompt |
| Morphic (Flagged Prompts Fix) | https://morphic.com/resources/how-to/seedance-2-prompts-flagged-how-to-fix |
| PromeAI (Constraint Guide) | https://www.promeai.pro/blog/2026/02/11/seedance-2-0-prompt-constraints-flicker-warp/ |

---

## 14. COMMERCIAL USE CASE PROMPTS (Chinese)

These are from ZeroLu/awesome-seedance for commercial applications:

### Sports Drink Ad
```
为图中产品生成一个精美高级的运动饮料广告，注意分镜编排，明快的节奏和快剪，高级的商业广告。
```

### MUJI Brand Promotion
```
帮我生成一个讲述无印良品这个品牌的宣传片，中间植入这个台灯
```

### Fashion Showcase (Multi-Outfit)
```
让一个女生依次换上@图1 @图2 @图3 @图4 @图5 @图6 六套服装进行卡点变装展示。每套服装需要包含半身走位和整体穿搭全身的展示。运镜要求使用不同景别流畅切换，加上符合调性的广告音乐
```

### Livestream Product Demo (Face Cream)
```
生成一段 15 秒带货口播视频，产品为图中面霜。要求人物亲手涂手上，给出近景展示，侧脸转动展示细节，镜头从半身到特写切换 3 次。口播要包含卖点，最后给出强行动号召。自动生成字幕，节奏紧凑，带轻微环境音。
```

### Ad Recreation (Product Swap)
```
模仿【@视频1】的分镜设计，把视频中所有产品都替换成【@图片1】的无人机...
```
(Replaces products while maintaining original shot design)

### Anime Adaptation from Novel
```
帮我根据下面的小说剧情要求生成动漫，将画风动作打斗表现严格对齐@视频1 的风格。
```

---

## 15. MOYIN CREATOR - Production Tool with Seedance 2.0

**URL:** https://github.com/MemeCalculate/moyin-creator (2,506 stars)
**Purpose:** AI-powered film production with Seedance 2.0 as the video generation engine

### 5-Stage Pipeline
1. **Script** -- AI-assisted screenplay writing
2. **Characters** -- Character design and consistency
3. **Environments** -- Scene/location generation
4. **Storyboards** -- Shot-by-shot visual planning
5. **Video Production** -- Seedance 2.0 generation

### Three-Layer Prompt Fusion
```
动作 + 镜头语言 + 对白唇形同步
(Action descriptions + Cinematographic language + Lip-sync alignment)
```

### Auto-Enforced Constraints
- Max 9 images + 3 videos + 3 audio files
- Prompt max 5,000 characters
- Grid-based first-frame composition (NxN strategy)
- Sequential consistency from upstream creative decisions

---

## SUMMARY OF KEY FINDINGS

1. **Most Starred Prompt Resource:** songguoxs/seedance-prompt-skill (1,378 stars) -- a Claude Code skill that auto-generates Seedance prompts
2. **Largest Collection:** YouMind-OpenLab claims 1,236 total prompts
3. **Best Organized:** HuyLe82US with 13 categories and individual markdown files
4. **Best Framework:** gracech0322-cmd's 6-Dimension system is the most structured
5. **No Negative Prompts:** Seedance 2.0 does NOT support negative prompts; use positive constraints
6. **Production Tool:** MemeCalculate/moyin-creator (2,506 stars) is a full film pipeline with Seedance
7. **Key Technique:** Timestamp-based scene breakdowns `[00:00-00:05]` with style/action/VFX per segment
8. **Reference System:** `@Image1`, `@Video1`, `@Audio1` with max 12 total files
9. **Output:** 4-15 seconds, up to 720p, with sound/BGM support
10. **Best Practice:** Be specific about physics, use camera rig terms not adjectives, one verb per shot
