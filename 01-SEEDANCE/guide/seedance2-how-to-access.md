# How to access and use Seedance 2? (Updated)

> **Source:** [@seedance2_news](https://x.com/seedance2_news/status/2025274331379761456) — Feb 21, 2026

---

Seedance 2 just dropped — and it's the greatest video model ever made. But there's just one problem: it's region-locked, anyone outside China can't access it.

The best way to access Seedance 2 is [Mitte.ai](https://mitte.ai/). It's fast, stable and consistent.

That means you can start generating Seedance 2 videos right now on [mitte.ai/flow/seedance-2](https://mitte.ai/flow/seedance-2), no VPN needed, no workarounds, no waitlists.

Here's exactly how to start creating films with Seedance 2 on Mitte, step by step.

---

## How to get access to Seedance 2?

Head to [mitte.ai](https://mitte.ai/) and create an account if you haven't already.

Once you're in, select Seedance 2 from the available models or click this link: [mitte.ai/flow/seedance-2](https://mitte.ai/flow/seedance-2)

---

## How to create films with Seedance 2?

Seedance 2 has two modes:
- **Omni mode**
- **Frame mode**

To create our first scene, we'll stick with default omni mode. If you want to set first and last frames, click the square button in the controlbar.

### Step 1. Adding references

If you're creating a product film or want visual consistency, upload a reference image. This could be a product photo, a character reference, or any visual you want the model to work from.

For my film, I'll add a Spice deodorant product photo. Because I want to create a commercial film for it.

### Step 2. Write Prompt

Write a detailed prompt describing what you want to see. If you uploaded a reference image, refer to it as "attached image" in your prompt. The more specific you are about camera angles, lighting, mood, and action — the better your results.

**Pro tip:** You can write your initial idea, then ask ChatGPT to expand it into a more cinematic, detailed prompt. Seedance 2 responds incredibly well to rich descriptions.

Note that, Seedance 2 supports JSON prompts. And they're very powerful; you can control the entire film, frame by frame.

You can copy this JSON prompt and ask ChatGPT to adjust it for your own film with custom scenes and transitions.

<details>
<summary><strong>Example JSON Prompt</strong> (click to expand)</summary>

```json
{
  "title": "Deodorant Product Film about a boxer using the deodorant in the attached image",
  "duration": "15 seconds",
  "concept": "A man pushes his body to the absolute edge. Every frame drips with intensity. Through all of it — the sweat, the impact, the heat — the deodorant holds. This is not a hygiene ad. This is a pressure test disguised as cinema.",
  "format": "16:9 and 9:16 deliverables",
  "fps": 24,
  "film_stock_emulation": "Kodak Vision3 500T, 35mm with heavy grain, shot wide open",
  "color_grade": "crushed blacks, teal midtones, burnt amber highlights, skin always warm and textured, everything else cold",
  "overall_energy": "HIGH BLOOD PRESSURE — every cut hits like a punch. No breathing room. The pacing is relentless. Cuts land on beat. Nothing soft. Nothing slow. The film should feel like your heart rate is climbing the entire 15 seconds.",

  "transition_rules": {
    "style": "SMASH CUTS ONLY. Every cut is hard, violent, percussive. Cuts sync to impacts — fist hitting bag, rope hitting floor, feet hitting pavement.",
    "forbidden": ["dissolves", "fades", "cross fades", "morph transitions", "wipes", "slow transitions of any kind"],
    "pacing": "cuts get FASTER as the film progresses. Shot 1 is longest. Final shots are 0.5 sec or less. The rhythm accelerates like a heartbeat under stress."
  },

  "audio": {
    "backbone": "deep sub-bass heartbeat that accelerates throughout the entire 15 seconds — starts at 60bpm, ends at 160bpm",
    "layers": "every impact is foley-heavy: rope snap, glove crack, breath burst, feet slapping concrete",
    "music": "dark minimal trap or industrial percussion, no melody, just pressure",
    "final_beat": "at 14 sec — everything cuts to silence. One single clean tone. Logo."
  },

  "shot_list": [
    {
      "shot": 1,
      "timecode": "00:00 — 00:02",
      "duration_sec": 2,
      "type": "PRODUCT INTRO",
      "description": "Extreme close-up: hand grabs the deodorant stick from a gym bench. No hesitation. Pulls cap off. Quick hard cut to applying it under arm — tight macro shot, we see skin texture, the product leaving its mark. This is the ritual before war.",
      "lens": "100mm macro",
      "movement": "static, two cuts within the shot",
      "lighting": "hard side light, deep shadow on opposite side"
    },
    {
      "shot": 2,
      "timecode": "00:02 — 00:03.5",
      "duration_sec": 1.5,
      "description": "Wide shot. Boxer jumping rope in concrete gym. Haze in the air. Fast footwork. Camera locked off. The rope is a blur. Sweat already visible.",
      "lens": "35mm anamorphic",
      "movement": "locked tripod",
      "lighting": "single overhead fluorescent, rim light from behind"
    },
    {
      "shot": 3,
      "timecode": "00:03.5 — 00:05",
      "duration_sec": 1.5,
      "description": "SMASH CUT. Close-up of fist hitting heavy bag. Sweat explodes off the leather on impact. 96fps slow motion but only for 1.5 seconds — the impact stretches, then we snap back to real time.",
      "lens": "85mm",
      "movement": "handheld, micro-shake on impact",
      "lighting": "backlit, sweat particles catch light"
    },
    {
      "shot": 4,
      "timecode": "00:05 — 00:06.5",
      "duration_sec": 1.5,
      "description": "Tracking shot. Running through empty streets at dawn. Camera is LOW, almost ground level, shooting up at him. He is a machine. Breath clouds in the cold. City blurred behind him.",
      "lens": "24mm wide",
      "movement": "car mount tracking, aggressive low angle",
      "lighting": "backlit golden hour, flare cutting across lens"
    },
    {
      "shot": 5,
      "timecode": "00:06.5 — 00:07.5",
      "duration_sec": 1,
      "description": "INSERT — extreme close-up of underarm MID-WORKOUT. Skin is covered in sweat but the deodorant is doing its job. Not clinical — raw and real. This is proof under pressure. Quick cut, almost subliminal.",
      "lens": "macro",
      "movement": "static",
      "lighting": "same gym lighting, no special treatment — the product lives in the grit"
    },
    {
      "shot": 6,
      "timecode": "00:07.5 — 00:08.5",
      "duration_sec": 1,
      "description": "Sparring. Getting hit. Head snaps. Mouthguard visible. He takes it. Comes back harder. Two rapid cuts within this one second — hit, recover, counter.",
      "lens": "50mm",
      "movement": "handheld in the ring, chaotic",
      "lighting": "overhead gym fluorescents, crowd in dark background"
    },
    {
      "shot": 7,
      "timecode": "00:08.5 — 00:09.5",
      "duration_sec": 1,
      "description": "Shadowboxing close-up. Fists flying toward camera. Eyes locked in. Not performing — surviving. Sweat dripping off brow.",
      "lens": "85mm",
      "movement": "static, subject moves toward and away from lens",
      "lighting": "single hard source camera left"
    },
    {
      "shot": 8,
      "timecode": "00:09.5 — 00:10.5",
      "duration_sec": 1,
      "description": "RAPID MONTAGE BEGINS — cuts now every 0.5 sec. Lacing shoes tight. Wrapping hands. Rope hitting floor. Exhale. Bag swinging. Each cut lands on a beat.",
      "lens": "mixed — macro, wide, close-up",
      "movement": "mixed",
      "speed": "all real time, speed comes from editing not slow-mo"
    },
    {
      "shot": 9,
      "timecode": "00:10.5 — 00:12",
      "duration_sec": 1.5,
      "description": "Arena entrance. Walking through the crowd. Overhead spots. Anamorphic flares everywhere. People reaching out. He doesn't see them. Eyes forward. Red gloves at his sides.",
      "lens": "35mm anamorphic",
      "movement": "steadicam walking backward",
      "lighting": "arena spots, practical flares"
    },
    {
      "shot": 10,
      "timecode": "00:12 — 00:13",
      "duration_sec": 1,
      "description": "In the ring. Bell rings. First punch thrown. SMASH CUT on the impact.",
      "lens": "50mm",
      "movement": "handheld ringside",
      "lighting": "high contrast arena"
    },
    {
      "shot": 11,
      "timecode": "00:13 — 00:14",
      "duration_sec": 1,
      "description": "VICTORY. Arms raised. Crowd erupting. But we only see it for ONE second. Not a celebration — a release. Then —",
      "lens": "35mm wide",
      "movement": "low angle looking up at him",
      "lighting": "backlit halo, arena spots"
    },
    {
      "shot": 12,
      "timecode": "00:14 — 00:15",
      "duration_sec": 1,
      "description": "HARD CUT TO BLACK. Silence. The deodorant product packshot fades in. Clean. Still. After 14 seconds of chaos, this single second of calm is deafening. Product is hero lit on black. Tagline appears.",
      "lens": "macro product photography",
      "movement": "static",
      "lighting": "soft overhead beauty light, subtle rim",
      "end_card": {
        "product": "[Deodorant — as shown in reference image]",
        "tagline": "Won't break under pressure.",
        "typography": "bold condensed sans-serif, all caps, tracked wide, white on black",
        "logo": "bottom center"
      }
    }
  ],

  "product_integration_strategy": {
    "appearances": 3,
    "philosophy": "The deodorant appears exactly THREE times: once at the start (the ritual), once mid-film (the proof), once at the end (the payoff). It is never the focus for more than 2 seconds. It earns its place by surviving the same 15 seconds the athlete does.",
    "shot_1": "RITUAL — he applies it before everything begins. It's part of gearing up.",
    "shot_5": "PROOF — quick insert mid-workout. Sweat everywhere but the product holds. Almost subliminal.",
    "shot_12": "PAYOFF — clean packshot after the storm. The product outlasted the pressure."
  },

  "directing_notes": {
    "intensity_curve": "The film should feel like a panic attack in the best way. Start strong, build relentlessly, never plateau. The viewer should feel physically tense by second 10.",
    "cuts_are_everything": "This film lives and dies on editing rhythm. Every cut is a heartbeat. Cuts accelerate like a heart under load. By the final third, we are cutting every half second.",
    "sweat_is_the_visual_motif": "Sweat is in every frame. Flying off punches, dripping down faces, glistening on skin under lights. The entire film is WET. This is what makes the deodorant's survival impressive.",
    "never_clinical": "The product moments are raw and embedded in the action. No white background. No hand model. No clean studio cutaway. The deodorant exists inside the sweat and chaos.",
    "the_silence_at_the_end": "The final second of silence after 14 seconds of relentless noise is the most powerful moment in the film. It is the exhale. The product lives in that exhale."
  },

  "post_production": {
    "grain": "heavy 35mm scan grain, pushed two stops",
    "halation": "aggressive on arena lights and backlit shots",
    "letterbox": "2.39:1 anamorphic",
    "transitions": "SMASH CUTS ONLY — no exceptions",
    "sound_design": "heartbeat is the metronome. it starts slow. it ends fast. when it stops, the product appears."
  }
}
```

</details>

### Step 3. Choose aspect ratio, duration, and quality

Pick your settings — aspect ratio (16:9, 9:16, 1:1, etc.), video duration, and quality level.

Once everything looks good, hit the blue "Generate" button on the right.

### Step 4. Wait for your video to generate

Sit back for a moment while Seedance 2 works its magic. Generation times vary depending on duration and quality settings.

Once it's finished, you'll see your completed video ready for review.

### Step 5. Extend your video from any frame

Want to make your film longer? Here's the trick: place your cursor at any point on the video timeline, then click **Frames → Current Frame → Add as First Frame**.

This lets you pick the exact moment you want to continue from — giving you precise creative control over your narrative.

Now write a new prompt to continue the video from that exact frame. The model will pick up seamlessly from where you left off, maintaining visual consistency.

---

## Start creating now

Seedance 2 is the real deal, and Mitte is the easiest way to access it from anywhere in the world. No region locks, no hacks — just open [mitte.ai](https://mitte.ai/) and start making films.
