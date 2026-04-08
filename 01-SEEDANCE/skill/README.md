<p align="center">
  <img src="assets/seedforge-logo.png" alt="SeedForge" width="800"/>
</p>

<p align="center">
  <strong>Seedance 2.0 AI Video Prompt Generator + FaceForge Face Detection Bypass</strong>
</p>

<p align="center">
  <a href="#what-it-does">What It Does</a> &middot;
  <a href="#faceforge--face-detection-bypass">FaceForge</a> &middot;
  <a href="#faceforge-test-results">Test Results</a> &middot;
  <a href="#installation">Installation</a>
</p>

---

A Claude Code skill that generates optimized, copy-paste-ready prompts for Seedance 2.0 (Dreamina / CapCut) and bypasses the platform's face detection filter using the battle-tested FaceForge protocol.

---

## What It Does

### 1. Prompt Generator
Generates professional Seedance 2.0 prompts for any content type:

- Cinematic / Narrative
- Action / Fight scenes
- Fashion / Runway
- Beauty / Skincare
- Commercial / Product
- Viral / UGC (TikTok, Reels)
- Educational / Tutorial
- Anime / Animation
- Music Video
- Drama / Dialogue
- VFX / Effects
- Landscape / Nature

Auto-detects the category from your description, applies the right template, camera vocabulary, style anchors, audio design, and quality suffixes. Outputs 2-3 variants with different camera/mood options, all copy-paste ready.

### 2. FaceForge — Face Detection Bypass

Seedance 2.0 blocks uploads containing realistic human faces. FaceForge is a two-phase protocol that gets around this:

**Phase 1: FORGE**
Upload a portrait photo to Claude Code. It analyzes every facial detail (skin tone, hair texture, eye shape, accessories, expression...) and generates a character sheet prompt optimized for your preferred image generator (Midjourney, DALL-E, Flux, Dreamina, Nano Banana Pro).

**Phase 2: SHIELD**
Upload the generated character sheet back to Claude Code. It applies an 8x8 grid overlay (the proven method), produces @Image1 (full body + grid) and @Image2 (face crop + grid), and generates the complete Seedance prompt with anti-fantasy override.

If the 8x8 grid gets blocked, it asks if you want to try alternatives — offering denser grids and different patterns in escalation order.

---

## FaceForge Test Results

Real production tests across multiple methods. These are actual results, not theory.

### Grid Overlay Tests

| Method | Grid Density | Line Width | Result |
|--------|-------------|------------|--------|
| No processing (raw photo) | — | — | BLOCKED |
| Grid overlay 6x6 | 6x6 | 4px | BLOCKED (not dense enough) |
| **Grid overlay 8x8** | **8x8** | **6px** | **PASSES** |
| Grid overlay 10x10 + noise | 10x10 | 5px | PASSES |

### Style & Processing Tests

| Method | Result | Output Quality |
|--------|--------|---------------|
| 3D / gaming style character sheet | PASSES filter | Generates **cartoon** (not realistic) |
| Heavy noise only (+-60) | PASSES filter | **Low quality** — noisy output |
| Scanlines (TV effect) | PASSES filter | **Artifacts** in output |
| Halftone dots | PASSES filter | Visible dot pattern in output |
| **Realistic sheet + 8x8 grid overlay** | **PASSES filter** | **Hyperrealistic output** |
| **Realistic sheet @Image1 + face crop with grid @Image2** | **PASSES filter** | **Best quality — proven in 7+ scenes** |

### Reference Strategy Tests

| Strategy | Result |
|----------|--------|
| Single image reference | Inconsistent face across shots |
| @Image1 (full sheet + grid) only | Good but face detail limited |
| **@Image1 (full sheet + grid) + @Image2 (face crop + grid)** | **Best consistency — face + body locked** |

### Prompt Style Tests

| Prompt Approach | Result |
|----------------|--------|
| Standard cinematic prompt + "photorealistic" | Output leans CGI/polished |
| "NOT 3D, NOT cartoon, NOT CGI" + camera imperfections | **Hyperrealistic documentary feel** |
| Sony FX3 + 35mm prime + autofocus hunt + rack focus miss | **Best raw footage look** |
| ARRI Alexa reference | Too clean/polished for documentary |
| Tripod / steadicam / gimbal | Too smooth — loses raw feel |
| 200mm telephoto | Wrong look (use 35mm + digital zoom) |

### Key Finding

The winning combination is:
1. **Realistic** character sheet (not 3D/cartoon)
2. **8x8 white grid overlay** with thick lines (width 6px)
3. **Two references**: @Image1 (full body) + @Image2 (face crop)
4. **Anti-fantasy override** in prompt: `NOT 3D, NOT cartoon, NOT CGI, NOT animation`
5. **Camera imperfection language**: autofocus hunt, rack focus miss, rolling shutter, ISO noise

This produced 7+ successful scenes with consistent hyperrealistic output.

---

## Escalation System

If the default 8x8 grid gets blocked, the skill offers alternatives in order:

| Priority | Style | Description |
|----------|-------|-------------|
| 1 | `grid8x8` | **Default** — 8x8 white grid overlay, proven winner |
| 2 | `grid10_noise` | 10x10 denser grid + random noise |
| 3 | `hexgrid` | Hexagonal non-rectangular pattern |
| 4 | `crosshatch` | Diagonal pencil sketch lines |
| 5 | `oilpaint` | Oil paint filter + grid combo |
| 6 | `blueprint` | Blue tint + technical measurement grid |
| 7 | `noise` | Heavy noise only (last resort) |

Generate all variants at once:
```bash
python scripts/grid_maker.py input.png output.png --style all
```

---

## Skill Structure

```
seedforge/
├── SKILL.md                              # Main skill file (800+ lines)
├── references/
│   ├── faceforge-guide.md                # FaceForge complete guide + real test data
│   ├── camera-dictionary.md              # 44+ camera movements & lens vocabulary
│   ├── style-anchors-library.md          # 50+ confirmed style anchors
│   ├── audio-engineering.md              # 4-layer audio prompt system
│   ├── color-lighting-vocabulary.md      # Color grading + 3-layer lighting
│   ├── category-templates.md             # Templates for 12+ content categories
│   ├── gold-examples.md                  # 30+ battle-tested gold standard prompts
│   └── failures-fixes.md                # 22 failure patterns + exact fixes + A/B tests
├── scripts/
│   ├── grid_maker.py                     # 7 overlay styles + face crop + batch mode
│   └── requirements.txt                  # Pillow + numpy
└── README.md
```

## Installation

### As a Claude Code Skill

Copy the skill folder to your Claude Code skills directory:

```bash
# Clone
git clone https://github.com/babakarto/seedforge.git

# Copy to Claude Code skills
cp -r seedforge ~/.claude/skills/seedforge
```

Or add it directly in your project's `.claude/skills/` directory.

### Grid Maker Script

```bash
pip install Pillow numpy
python scripts/grid_maker.py input.png output.png              # Default 8x8 grid
python scripts/grid_maker.py input.png face.png --face-crop    # Face crop + grid
python scripts/grid_maker.py input.png output.png --style all  # All variants
```

---

## Usage

### Generate a Seedance Prompt
Just describe what video you want:
> "Make me a cinematic drone shot of a mountain at sunrise, 12 seconds, 16:9"

### FaceForge — Bypass Face Detection
**Phase 1:** Upload a portrait photo and say:
> "I want to use this face as a Seedance reference"

**Phase 2:** Come back with the generated character sheet and say:
> "Process this sheet for Seedance"

---

## Built With

- [Seedance 2.0](https://dreamina.capcut.com) — ByteDance's quad-modal AI video model
- [Claude Code](https://claude.ai/code) — Anthropic's CLI for Claude
- Real production data from 7+ successfully generated scenes

## License

MIT
