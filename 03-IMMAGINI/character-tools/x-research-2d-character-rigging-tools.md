# 2D Character Rig & Body Part Separation Tools — Research Report

**Date:** 2026-03-17
**Source:** Web research (X API not available — token 401)
**Focus:** AI tools for automatic body parts separation, pre-rigged puppet assets, templates for 2D animation

---

## 1. AI TOOLS — Auto Body Parts Separation

### KomikoAI — AI Layer Splitter ⭐ TOP PICK
- **What it does:** Upload an illustration and the AI automatically separates it into layers: characters, background, eyes, hair, limbs, props
- **How it works:** Deep learning on millions of images, recognizes edges, colors, context
- **Input:** JPG, PNG
- **Output:** Separated layers at original resolution
- **Compatibility:** Live2D, Spine, After Effects (generic "animation-ready")
- **Pricing:** Free credits (500 "Zaps") for new users, then paid plans
- **Limitations:** Complex scenes may group elements together; fine details (hair, fur) are problematic; heavily overlapping objects are difficult to separate
- **Target:** VTuber artists, Live2D riggers, indie animators
- **Link:** [komiko.app/layer_splitter](https://komiko.app/layer_splitter)
- **Blog:** [How to Instantly Split Anime Art into Layers](https://komiko.app/blog/how-to-instantly-split-anime-art-into-layers-for-animation-and-rigging)

### GodMode AI — Spine Animation Generator ⭐ TOP PICK
- **What it does:** Automatically generates Spine files with separated body parts from a 2D image
- **How it works:** 1) Generates a 3D model with idle animation to understand the skeletal structure → 2) Converts to 2D Spine format with correct layering
- **Input:** JPG, PNG, WebP (up to 10MB)
- **Output:** Spine JSON + PNG atlas — compatible with Unity, Unreal, Godot
- **Auto-rigging:** Yes, creates professional skeletal structures optimized for Spine
- **Animations:** 2000+ professional animations with one-click retargeting
- **Limitation:** Only human/humanoid characters
- **Pricing:**
  - Free: 3 credits upon registration
  - Starter: $12 for 20 credits
  - Popular: $32 for 60 credits
  - Ultimate: $100 for 250 credits
  - Subscription: $19/month (up to 200 generations)
- **Link:** [godmodeai.co/ai-spine-animation](https://www.godmodeai.co/ai-spine-animation)

### Pixa — AI 2D Character Rigging
- **What it does:** Upload a character design → AI detects articulation points (elbows, knees, shoulders) → builds a digital skeleton
- **Input:** PNG, PSD
- **Best practice:** Image in T-pose with limbs separated from the body, transparent background
- **Output:** Rigged character + animation from text prompt
- **Pricing:** Free to try
- **Link:** [pixa.com/create/2d-character-rigging](https://www.pixa.com/create/2d-character-rigging)

### Live2D Cubism — Material Separation Plugin
- **What it does:** Official Photoshop plugin to separate materials/layers for Live2D
- **Auto-mesh:** Automatic mesh generation based on specified point density
- **Version:** R1 beta2 (June 2025)
- **Link:** [docs.live2d.com - Material Separation Plugin](https://docs.live2d.com/en/cubism-editor-manual/material-separation-ps-plugin-download/)

### Cascadeur
- **What it does:** Standalone software for AI-assisted 3D keyframe animation
- **Focus:** More 3D than 2D, but useful for movement reference
- **Link:** [cascadeur.com](https://cascadeur.com)

---

## 2. PRE-RIGGED PUPPET ASSETS

### Rive — Community Templates (FREE)
Community files with bones and constraints:
- [Character rigging and animation](https://rive.app/community/files/13636-25823-character-rigging-and-animation/) — bones + constraints
- [Marty animation](https://rive.app/community/files/52-69-marty-animation/) — binding method, bones linked to different character parts
- [Character animation](https://rive.app/community/files/10837-20734-character-animation/) — basic animation with bones
- [Joints and bones rig](https://rive.app/community/files/6082-11833-joints-and-bones-rig/) — rig test for bending joints
- [Mouth Rig Demo](https://rive.app/community/files/3216-6766-mouth-rig-demo/) — mouth rig with 3 controls

### Spine 2D — Asset Packs (PAID)
- **Hitman - Platformer** ($10) — Rigged skeleton, platformer animations (walk, run, jump, wall slide, punch), Unity 5 project
- **Gunman - Jetpack Platformer** ($10) — IK-rigged skeleton, jetpack, 4 weapons, Unity 5 project
- **Discount:** 50% off all packs after the first
- **Link:** [esotericsoftware.com/spine-asset-packs](https://esotericsoftware.com/spine-asset-packs)

### Spine 2D — Third-Party Marketplace
- **itch.io** — [Tag: 2D + Spine](https://itch.io/game-assets/newest/tag-2d/tag-spine) — indie assets
- **GraphicRiver** — [124+ Spine 2D game assets](https://graphicriver.net/spine-and-2d-graphics-in-game-assets) — including flat art characters
- **GameDev Market** — [Character Spine animation](https://www.gamedevmarket.net/asset/2d-character-spine-animation-and-item-7166)

### DragonBones — Free Assets
- [Free 2D Character + DragonBones setup](https://forum.starling-framework.org/d/20516-free-2d-character-dragonbones-set-up-and-animations-art-assets) — character with animations and setup

### Adobe Character Animator — Puppet Templates (FREE)
- **Okay Samurai** — [okaysamurai.com/puppets](https://okaysamurai.com/puppets/) — free puppet library, including packs with Limb IK (4 puppets + project file)
- **ElectroPuppet** — [85+ Free Puppets for 2026](https://electropuppet.com/free-adobe-puppet-templates/) — catalog updated Feb 2026
- **Adobe official** — [Pro mode example puppets](https://pages.adobe.com/character/en/puppets)
- **GraphicMama** — [63 Free Character Animator Puppets](https://graphicmama.com/blog/free-character-animator-puppets-2021/)
- **ReallyGoodDesigns** — [600+ Fully Rigged Puppets](https://reallygooddesigns.com/adobe-character-animator-puppets-download/)

### SVG Puppet Resources (FREE)
- **FreeSVG** — [Vector Puppet Male](https://freesvg.org/1539432292) — posable multi-part puppet
- **FreeSVG** — [Toy Clown Puppet Animation](https://freesvg.org/clown-jointtest-v4) — animated puppet with SMIL
- **Vecteezy** — [Puppet Vectors](https://www.vecteezy.com/free-vector/puppet) — free vectors
- **Vexels** — [Puppet vectors](https://www.vexels.com/free-vectors/puppet/) — AI, SVG, JPG, PNG with commercial license

---

## 3. RIGGING SOFTWARE (Non-AI, Manual)

| Software | Type | Cost | Notes |
|----------|------|------|-------|
| **Rive** | Web-based, bones & constraints | Free tier + paid | Ideal for web/app, lightweight export |
| **Spine 2D** | Desktop, skeletal animation | $69 Essential / $299 Pro | Gamedev standard |
| **DragonBones** | Desktop, open source | FREE | Free alternative to Spine |
| **Adobe Character Animator** | Desktop, motion capture | Creative Cloud sub | Auto-tag layers from PSD/AI |
| **Cartoon Animator 5** | Desktop, puppet animation | ~$99-$199 | Bone-rigging, Smart IK |
| **Duik (After Effects)** | AE plugin, rigging | FREE (open source) | Motion design standard |
| **Adobe Animate** | Desktop, vector animation | Creative Cloud sub | Native rigging since 2024 |
| **Live2D Cubism** | Desktop, mesh deformation | Free tier + Pro | Ideal for VTuber/anime style |
| **Blender (Grease Pencil)** | Desktop, 2D in 3D | FREE | Powerful but steep learning curve |

---

## 4. RECOMMENDED WORKFLOW — From Character to Animated Puppet

### Option A: Full AI (fast, less control)
1. **Draw/generate** the character in flat vector/vinyl toy style
2. **GodMode AI** → upload image → receive Spine JSON with separated body parts + automatic rig
3. Import into **Unity/Godot** and apply animations from the 2000+ catalog

### Option B: AI + Manual (balanced)
1. **Draw** the character as a complete illustration
2. **KomikoAI Layer Splitter** → separate into layers (head, body, arms, legs)
3. Import separated layers into **Spine 2D** or **Rive**
4. Manually rig with bones
5. Animate

### Option C: Manual + Template (maximum control)
1. **Draw** each body part separately in Illustrator/Figma
2. Export as SVG/PNG with named layers
3. Import into **Rive** (using community template as a base) or **After Effects + Duik**
4. Rig and animate with full control

---

## 5. SEARCHES PERFORMED

- Web queries: 9
- Pages analyzed in detail: 4
- Source: Google Web Search (X API not available)
- Estimated cost: $0 (free web search)
- Date: 2026-03-17
