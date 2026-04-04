# LTX 2.0 Prompt Guide: Deep Research Report (Image-to-Video & Text-to-Video)

**Date:** 2026-02-12
**Source:** X/Twitter deep research
**Queries run:** 12+ | **Tweets scanned:** ~700+ | **Threads followed:** 5 | **External links deep-dived:** 1
**Time range:** Oct 2024 - Feb 2026 | **Estimated cost:** ~$4.50

---

## Table of Contents
1. [What is LTX-2?](#what-is-ltx-2)
2. [Text-to-Video Prompt Guide](#text-to-video-prompt-guide)
3. [Image-to-Video Prompt Guide](#image-to-video-prompt-guide)
4. [Audio-to-Video Prompt Guide](#audio-to-video-prompt-guide)
5. [Official LTX Studio Workflows](#official-ltx-studio-workflows)
6. [Advanced Tips from Power Users](#advanced-tips-from-power-users)
7. [Technical Parameters & Settings](#technical-parameters--settings)
8. [Community LoRAs & Extensions](#community-loras--extensions)
9. [Key Resources & Links](#key-resources--links)
10. [Expert Voices to Follow](#expert-voices-to-follow)

---

## What is LTX-2?

LTX-2 is a **19B parameter DiT-based foundation model** by Lightricks. It's the first truly open-source audio-video model, generating synchronized video AND audio from text/image prompts.

**Key capabilities:**
- Text-to-Video (T2V)
- Image-to-Video (I2V)
- Audio-to-Video (A2V)
- Video-to-Video (V2V)
- Text-to-Audio+Video (T2AV)
- Image+Audio-to-Video

**Runs locally** on consumer GPUs (16-24GB VRAM recommended). Available via:
- [LTX Studio](https://ltx.studio) (web platform)
- [ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo) (local)
- [Pinokio](https://pinokio.computer) + WAN2GP (local, beginner-friendly)
- [HuggingFace](https://huggingface.co/Lightricks/LTX-2)

> *"2,000,000 downloads on Hugging Face"* - @yoavhacohen (LTX co-founder), Jan 23 2026

---

## Text-to-Video Prompt Guide

### The 5 Core Elements (Official from @LTXStudio)

A complete motion prompt includes:
1. **Subject** - Who/what is in the scene
2. **Action** - What is happening
3. **Context** - Where and when (environment, time of day)
4. **Style** - Visual look (cinematic, anime, retro, etc.)
5. **Camera motion** (optional) - How the camera moves

> Source: [@LTXStudio thread](https://x.com/LTXStudio/status/1915428056526733728) - 125 likes, 295K impressions

### Prompt Structure Best Practices

**Start with the scene description FIRST:**
> *"Make sure to describe the scene at the very beginning of the prompt. That way you'll avoid any morphing or scene changes."*
> - @LTXStudio (official tip)

**Example prompt structure:**
```
[Scene/Environment description]. [Subject description]. [Action]. [Camera movement]. [Style/aesthetic details].
```

### Actual Working Prompts from @LTXStudio

**UGC-Style Social Video (20s):**
```
Gorilla gaming streamer. UGC style footage. Wearing headphones.
Static camera wide-shot. Gorilla is gaming using mouse and keyboard.
```

**Opening Sequence:**
```
Epic arial shot through rocks. Camera flys though [scene description]...
```

**Cinematic Portrait:**
```
Intimate close-up portrait. halation. 35mm film look. High-end fashion.
Older [character description]...
```

**Time Period Styles:**
LTX-2 understands how video looked across decades. Just add the era:
```
1940s film, 70s TV dramas, 80s news broadcasts, 90s sitcoms, grainy 2000s found footage
```
> Source: [@LTXStudio style thread](https://x.com/LTXStudio/status/1981758790858055776) - **691 likes, 1.5M impressions** (viral thread)

### Text-to-Video Character Consistency

User @EndFolding79421 discovered LTX-2 maintains **consistent characters** in T2V when you're descriptive:
```
Interior of a dark, old wooden cabin at night lit only by a faint lantern.
A beautiful 21 year old woman wearing a [detailed clothing description]...
```
> *"Most of the time when I redo a text to video I get different characters, but with LTX, I got basically the same person"*

### Duration Setting
- LTX-2 Fast supports up to **20 seconds** in a single generation
- For longer content, chain clips together in the Storyboard/Editor

---

## Image-to-Video Prompt Guide

### Key Differences from T2V

> *"LTX-2 needs more specificity when it comes to image to video than it does text to video."*
> - @BrentLynch (2,418 followers)

### Common Issue: Unwanted Camera Movement

This is the #1 complaint from users:
> *"It does not give a sh*t about the prompt. It only knows 4-5 camera movements... It rotates the camera or moves right or left even if you write NO CAMERA MOVEMENT."*
> - @Serkanbaday

> *"Why does it always dolly in or zoom when I try to create video with a start image!?"*
> - @Serkanbaday

**Solution from community:**
- Be VERY explicit about camera: `"Static camera. No camera movement. Locked-off shot."`
- If you want stillness, describe ONLY the subject's motion, not the camera

### Image-to-Video Workflow (Official)

From @LTXStudio's official workflow thread:
1. **Generate/upload your start image** (using FLUX Premium or Nano Banana Pro)
2. **Select LTX-2 Fast or Pro** as the video model
3. **Set duration** (up to 20s)
4. **Write your motion prompt** - describe what should MOVE in the scene
5. **Add dialogue/camera moves/performance direction** as needed

### Working I2V Prompts

**Adding motion to a still:**
```
Dynamic aerial drone shot. Camera moves.
```

**Music video from image + audio:**
```
Character sings the [lyrics]...
```

**Color change:**
```
Change the color of the [YOUR ITEM]
```
(use the Color Picker tool alongside this prompt)

---

## Audio-to-Video Prompt Guide

This is LTX-2's killer feature - native lip sync and audio-driven video.

### The Complete Audio-to-Video Guide (from @LTXStudio official thread)

> Source: [Audio-to-Video master thread](https://x.com/LTXStudio/status/2013973820835795003) - 9 tips in one thread

#### 1. Start frames and voice choice
- Audio-to-Video works from a **prompt** or a **start frame**
- **Align your voice with the character** - matching personality, age, and gender leads to better lip sync
- Voice + character mismatch = uncanny results

#### 2. Dialogue just works
- Speech is usually **detected automatically** from audio
- **No prompt needed** for basic dialogue
- If issues: add `"Character speaks"` or `"The person talks"`

#### 3. Match performance cues to audio
- If audio sounds angry but prompt says "happy" = bad results
- **Start frame expression matters** - use neutral or matching emotion
- Keep prompt emotion aligned with audio emotion

#### 4. Use sound intentionally
- Layer music or sound effects to drive timing and motion
- **Always guide with a prompt** to help the model understand intent

#### 5. Music videos and timing
- **Isolate vocals** for best results
- Instrument stems help too (rhythm, dance)
- For fast lyrics/heavy vocal effects: **write out the words in your prompt**
- Example: `"Character sings the [actual lyrics here]..."`

#### 6. Fix frozen first frame
Community tip from @matze2001:
> *"If you notice a frozen first frame or lip sync that feels off, try adding a short audio buffer at the beginning."*
>
> Also: *Start prompt with: "Animate this image so that in the first second... [my_subject/action]..."*

### Audio-to-Video Workflow

From @LTXStudio:
1. Select **Audio-to-Video** from the dropdown
2. Upload your audio OR use Text-to-Speech feature
3. Add a prompt to guide **emotion, action, and camera movement**
4. Generate

From @dbenyamin's practical workflow:
```
1. Take image of person, make new looks with Nano Banana
2. Clone voice with ElevenLabs from audio clip
3. Make narration with cloned voice
4. Take image + audio to LTX audio->video
```

---

## Official LTX Studio Workflows

### The Complete Ad Production Workflow (Feb 7, 2026)

From [@LTXStudio's latest thread](https://x.com/LTXStudio/status/2020163754181509201) - full ad creation:

**Step 1: Create your characters**
- Generate or upload characters, save each as an **Element**
- This locks appearance for consistency across shots

**Step 2: Explore coverage with a grid**
- Tag characters in prompt with `@character_name`
- Generate using **3x3 grid** for different angles/framings
- Use **2x2 grid** when character likeness matters most

**Step 3: Turn scene into an Element**
- Save chosen grid result as an Element
- Extract specific frames: `"Extract frame middle right"`

**Step 4: Add motion with LTX-2 or Veo 3.1**
- Click 'Create Video'
- Add dialogue, camera moves, or performance direction

**Step 5: Assemble and review**
- Add shots to Storyboard
- Import to Video Editor for pacing
- Export timeline for final cut

### Branded Product Workflow (@AmirMushich - 45K followers)

One of the most prolific LTX creators on X:

1. **Save logos/brand assets as Elements** in LTX
2. **Tag Elements in prompts** with `@element_name`
3. Use **Nano Banana Pro** for image generation
4. Animate with **LTX-2 or Veo 3.1**

> *"Build any branded products in <60 sec"* - @AmirMushich

### Storyboard Builder Speed Workflow (@AmirMushich)

1. Go to LTX > Create new project
2. Type in ANY idea (even 5-10 words works)
3. Click "Next" - LTX generates a full script
4. Review/edit scenes, shots, and prompts in Storyboard
5. Add scenes to Timeline or download for external editing

---

## Advanced Tips from Power Users

### Use Cinematic Language (@LTXStudio)
> *"Prompt like you're directing a shot. Specify lens choice, depth of field, and lighting."*
> Example keywords: `extreme wide-angle, soft oval bokeh, cinematic portrait light`

### Camera Framing Keywords
Include these in your prompts:
- `Close-up, tight framing`
- `Medium shot`
- `Wide shot`
- `Low angle`
- `Aerial shot`
- `Side profile medium-wide shot`
- `Reverse shot from behind`

### Lens & Film Look Keywords
- `Shot on 35mm film`
- `Wide angle lens`
- `Ultra-wide lens`
- `Kodak 35mm Film. Film grain.`
- `halation` (light bloom effect)
- `soft oval bokeh`
- `shallow depth of field`

### Style Transfer & Consistency
- Use **Multi-reference** panel to combine environment + character
- **Lock style with a reference image** - upload close-up to keep tone/lighting consistent
- To avoid style switching: *"Include a line in your prompt like [keep the original style]"* - @LTXStudio

### Time-Stamping Technique
@TexasCoachMike discovered using **time-stamping in prompts** for T2V:
> *"I used a time stamping technique in the prompt"* - describing what happens at specific moments in the video

### Elements System (Game-Changer)
- Save **characters, logos, fonts, scenes** as reusable Elements
- Tag in prompts with `@element_name`
- Ensures **total consistency** across all generations

### Color Picker
- Available in Gen Space with FLUX.2 or Nano Banana
- Write prompt, pick color, it's added automatically
- Supports **hex codes** and brand palettes

### Negative Prompt for A2V (Community Tip)
@matze2001 suggests using negative prompts when doing Audio-to-Video to avoid frozen frames and unnatural eye movements.

---

## Technical Parameters & Settings

### Resolution
- Width and height must be **divisible by 32**
- Non-standard resolutions cause dimension mismatch artifacts

### Frame Count
- Must be **divisible by 8 plus 1** (e.g., 9, 17, 25 frames)
- Padding to divisible values = cleaner outputs

### Model Variants
| Variant | Parameters | Best For | Speed |
|---------|-----------|----------|-------|
| LTX-2 19B (Full) | 19B | Highest quality | Slower |
| LTX-2 Distilled 8-step | 19B | Fast generation | ~18x faster |
| LTX-2 Fast (Studio) | - | Quick iterations | Fast |
| LTX-2 Pro (Studio) | - | Production quality | Moderate |

### VRAM Requirements
- **16GB minimum** (4060 Ti level - expect slow at 480p)
- **24GB recommended** for comfortable generation
- **GGUF quantized versions** available (Q4_K_M, Q6_K) for lower VRAM

### Generation Speed Benchmarks
- **10 seconds of video in ~1 minute** (via Pinokio/WAN2GP) - @zast57
- **7 second video on M4 Max** (native Metal/MPS) - @jc50000000
- **5 second 480p on 16GB 4060 Ti** takes ~20 min - @GWil112

### CFG Scale
- Distilled model works best with **CFG 1.0**

---

## Community LoRAs & Extensions

### LTX-2 Image-to-Video Adapter LoRA (@Machinedelusion)
- **565 likes, 35K impressions** - major community release
- Trained on **30,000 videos**
- General-purpose enhancer (not style-specific)
- Boosts motion quality for I2V
- [HuggingFace link](https://huggingface.co/MachineDelusions/LTX-2_Image2Video_Adapter_LoRa)

### LTX-2 Squish LoRA (@1Views66845)
- Fun LoRA: upload image + prompt `"squish it"` to get squish video
- [HuggingFace link](https://huggingface.co/ovi054/LTX-2-19b-Squish-LoRA)

### iCLoRA Flow (Character Replacement)
- @athianandam's workflow for recreating scenes with different characters
- [ComfyUI workflow on GitHub](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/LTX-2_ICLoRA_All_Distilled.json)

---

## Key Resources & Links

### Official
- **LTX Studio Platform:** https://ltx.studio
- **LTX-2 on HuggingFace:** https://huggingface.co/Lightricks/LTX-2
- **ComfyUI Integration:** https://github.com/Lightricks/ComfyUI-LTXVideo
- **LTX-2 Model Info:** https://ltx.io/model/ltx-2

### Tutorials & Guides
- **HackerNoon LTX-2 Guide** (text-to-video, image-to-video, LoRA tips, BF16 training): https://hackernoon.com/the-creators-shortcut-to-sounded-ai-video-ltx-2-distilled-and-deployable
  - Shared by @hackernoon (89K followers) and @lexdavid42
- **NVIDIA RTX Blog** (run LTX-2 + FLUX locally with ComfyUI): Shared by @NVIDIA_AI_PC (24K followers) - **281 likes, 1.2M impressions**
- **Pinokio + WAN2GP Tutorial** by @zast57: https://youtu.be/Jd841i7MR64
  - Covers T2V, I2V, A2V, lip sync, motion transfer
- **@FurkanGozukara** (142K followers) - SwarmUI + ComfyUI presets for LTX-2 (1-click install)

### Platforms Running LTX-2
- [LTX Studio](https://ltx.studio) (official web platform)
- [GamerHash AI](https://gamerhash.com) (local GPU-based)
- [Mitte](https://mitte.ai) (API)
- [WaveSpeed AI](https://wavespeed.ai/models/wavespeed-ai/ltx-2-19b/text-to-video) (API)
- [APIFree](https://www.apifree.ai/model/lightricks/ltx-2-pro/text-to-video) (API)
- [Freepik](https://freepik.com) (web)

---

## Expert Voices to Follow

| Account | Followers | Why Follow |
|---------|-----------|------------|
| [@LTXStudio](https://x.com/LTXStudio) | 29K | Official account, regular prompt guides & workflows |
| [@ltx_model](https://x.com/ltx_model) | 8.4K | Open-source model updates |
| [@AmirMushich](https://x.com/AmirMushich) | 45K | Prolific prompt engineer, daily LTX prompts & brand workflows |
| [@yoavhacohen](https://x.com/yoavhacohen) | 2K | LTX co-founder, milestone updates |
| [@FurkanGozukara](https://x.com/FurkanGozukara) | 142K | ComfyUI/SwarmUI presets, tutorials |
| [@wildmindai](https://x.com/wildmindai) | 5.2K | AI video news & LTX coverage |
| [@Machinedelusion](https://x.com/Machinedelusion) | 6.8K | LoRA creator, I2V adapter |
| [@cocktailpeanut](https://x.com/cocktailpeanut) | 32K | Pinokio creator, LTX-2 local setup |
| [@NerdyRodent](https://x.com/NerdyRodent) | 10K | AI video experiments |
| [@carolletta](https://x.com/carolletta) | 12.8K | LTX Ambassador, A2V workflows |
| [@zast57](https://x.com/zast57) | 790 | Excellent tutorials for beginners |
| [@BrentLynch](https://x.com/BrentLynch) | 2.4K | A2V music video workflows |
| [@gokayfem](https://x.com/gokayfem) | 5.4K | Open-source pipeline expert |
| [@manishkumar_dev](https://x.com/manishkumar_dev) | 55K | LTX workflow breakdowns |

---

## Community Sentiment Summary

### Consensus
- LTX-2 is the **best open-source video model** available (as of Feb 2026)
- Audio-to-Video is the **standout feature** that differentiates it
- Running locally is practical with 24GB+ VRAM
- Quality is "impressive" but not yet at Seedance 2.0/Sora 2/Veo 3 level for raw output

### Debate
- **LTX-2 vs Seedance 2.0:** Seedance is higher quality but closed/expensive; LTX-2 is open-source and free
- **Camera control in I2V:** Still frustrating for many users (unwanted movement)
- **VRAM barrier:** 16GB users struggle; 24GB is the sweet spot

### Trending (Feb 2026)
- Community is training **custom LoRAs** for specific use cases
- **Audio-to-video music videos** are the hot creative use case
- Requests for Seedance 2.0 integration into LTX Studio
- GGUF quantized models making it more accessible

---

*Report generated by Claude Code X-Research Skill*
*12 queries | ~700 tweets scanned | Oct 2024 - Feb 2026 | Est. cost: ~$4.50*
