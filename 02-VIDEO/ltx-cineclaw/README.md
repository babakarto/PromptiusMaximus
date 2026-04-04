# 🎬 CineClaw — AI Video Generation Skill for OpenClaw

Generate cinematic AI videos from text, images, or audio directly from your OpenClaw bot. Powered by [LTX-2](https://ltx.io/model) by Lightricks.

## What It Does

Tell your bot to make a video. It handles the rest — prompt enhancement, API calls, file saving.

```
You: "Make me a cinematic video of a samurai walking through rain in Tokyo at night"
Bot: *enhances your prompt, generates video, saves to Desktop*
```

Supports:
- **Text-to-Video** — Describe a scene, get a video
- **Image-to-Video** — Animate a still image
- **Audio-to-Video** — Generate video synced to audio (lip sync, music videos)
- **Camera presets** — dolly, pan, crane, handheld, orbit, tracking
- **AI audio** — synchronized sound effects, dialog, ambient
- **Prompt enhancement** — turns basic ideas into cinematic prompts

## Quick Install

### Option 1: ClawHub (recommended)
```bash
npx clawdhub@latest install cineclaw
```

### Option 2: Manual
```bash
cp -r cineclaw ~/.openclaw/workspace/skills/cineclaw
```

### Option 3: Just paste the GitHub link to your bot
```
Install the skill from https://github.com/babakarto/cineclaw
```

## Setup

1. Get an API key at [console.ltx.video](https://console.ltx.video)
2. Set it as an environment variable:
```bash
echo 'export LTX_API_KEY="your_key_here"' >> ~/.bashrc
source ~/.bashrc
```
3. Done. Start generating.

## Usage Examples

### Basic
```
"Generate a quick video of ocean waves at sunset"
"Make a 10-second cinematic video of a cyberpunk street"
```

### With specifics
```
"Create a pro quality 4K video of a coffee being poured in slow motion"
"Animate this photo with a slow camera dolly forward"
"Generate a video synced to this audio track"
```

### The bot will:
1. Enhance your prompt (adding camera, lighting, audio cues)
2. Show you the enhanced prompt for approval
3. Estimate the cost before generating
4. Generate and save the video
5. Ask if you want to iterate or upscale

## Models

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| ltx-2-fast | ~5-15s | Good | Drafts, iteration, previews |
| ltx-2-pro | ~30-90s | Cinematic | Final output, client work, A2V |

## Pricing

Per second of generated video:

| Model | 1080p | 1440p | 4K |
|-------|-------|-------|-----|
| fast | ~$0.02 | ~$0.04 | ~$0.08 |
| pro | ~$0.05 | ~$0.10 | ~$0.20 |

A typical 6-second fast preview costs about $0.12. The bot always estimates cost before generating.

## Skill Structure

```
cineclaw/
├── SKILL.md                              # Main skill (OpenClaw reads this)
├── references/
│   ├── ltx-api.md                        # API endpoints, params, errors
│   ├── prompting-guide.md                # How to write great video prompts
│   └── ltx2-prompt-guide-advanced.md     # Deep research from X/Twitter community
├── scripts/
│   └── ltx_generate.py                   # Python script for all API calls
├── README.md                             # This file
└── LICENSE                               # MIT
```

## Prompting Tips (Quick Reference)

**Structure:** `[Scene]. [Subject]. [Action]. [Camera]. [Style].`

**Always start with the scene** — prevents morphing and inconsistencies.

**Key style keywords:** `35mm film`, `halation`, `shallow depth of field`, `golden hour`, `cinematic lighting`

**I2V tip:** Always add `"Static camera. No camera movement."` to prevent unwanted dolly/zoom.

**A2V tip:** Match audio emotion to prompt emotion. Isolate vocals for music videos.

See `references/prompting-guide.md` for the full guide with examples.

## Roadmap

- [ ] Batch generation (multiple videos from a script)
- [ ] Video-to-video (style transfer, retakes)
- [ ] LoRA support for custom styles
- [ ] Storyboard mode (multi-shot sequences)
- [ ] Multi-provider support (Runway, Kling, Sora)
- [ ] Telegram inline preview (send video directly in chat)

## Contributing

PRs welcome. If you add support for another video API, keep the same interface pattern — the bot shouldn't need to learn a new workflow.

## License

MIT

## Credits

- [LTX-2](https://ltx.io/model) by [Lightricks](https://www.lightricks.com/) — the video generation model
- [OpenClaw](https://openclaw.ai) — the AI agent platform
- Prompting guide based on [official LTX docs](https://ltx.video/blog/how-to-prompt-for-ltx-2), community research (700+ tweets analyzed), and [walterlow/ltx-2-prompt](https://github.com/walterlow/ltx-2-prompt)
