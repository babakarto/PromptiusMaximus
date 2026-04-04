# Remotion + Claude Code — Xcite Ventures Ad Project
## Setup + Prompts Completi

---

## INSTALLATION

```bash
# Step 1 - Create project
npx create-video@latest
# Project name: xcite-ad
# Template: Blank
# TailwindCSS: Yes
# Install Skills: Yes

# Step 2 - Enter folder and install
cd xcite-ad
npm install

# Step 3 - Start preview (opens browser at localhost:3000)
npm run dev

# Step 4 - OPEN A SECOND TERMINAL and launch Claude Code
cd xcite-ad
claude

# Step 5 - If skills didn't auto-install
npx skills add remotion-dev/skills

# Step 6 - When done, render
npx remotion render XciteAd output.mp4
```

---

## TEST PROMPT (run this first to verify setup works)

```
Use remotion skills. Create a 1080x1920 vertical (9:16) composition 
called "XciteTest", 5 seconds at 30fps.

Dark gradient background from #1a1a2e to #16213e.

Scene: The text "XCITE" appears letter by letter with a spring bounce 
animation. Each letter enters from below with staggered timing 
(0.15s delay between letters). Font: bold sans-serif, white, 120px.

After all letters are in place (around 2s), a subtle glow pulse 
effect on the text. Then "PLAY. CONNECT. DOMINATE." fades in below 
in smaller text (40px) with a smooth opacity animation.

Add subtle particle dots floating upward in the background throughout 
the entire video. Use spring() for all animations.
```

---

## FULL AD — SCENE BY SCENE PROMPTS

### Scene 1 — The Mascot (0-3s)

```
Use remotion skills. Create a 1080x1920 vertical (9:16) composition 
called "XciteAd", 12 seconds at 30fps.

Scene 1 (frames 0-90, first 3 seconds):

Create an SVG cartoon character - a bold, rounded vinyl-toy style 
figurine with:
- Big round head, small body, stubby arms and legs
- Simple face: two dot eyes, thick eyebrows, wide mouth
- Wearing a tiny suit jacket and sneakers (corporate-meets-street style)
- Color palette: electric blue body, white shirt, dark jacket

The character enters from below with a spring bounce (overshoot).
Body does a subtle idle bounce (up-down 3px loop).
Mouth alternates between open/closed every 8 frames (simulating talking).
Right arm raises and points forward on frame 30.
Speech bubble appears with spring animation: "Still using slot machines 
for your ads?! Come on..." in bold comic-style font.

Background: dark gradient #1a1a2e to #0f0f23.
```

### Scene 2 — The Slot Machine (3-6s)

```
Use remotion skills. Add Scene 2 to the XciteAd composition.
Scene 2 (frames 90-180, seconds 3-6):

A cartoon slot machine appears center-frame with spring animation.
Machine body: rounded rectangle, metallic gradient, lever on right side.

Three vertical reels inside the machine, each containing 5 icons 
stacked vertically:
- Reel icons: megaphone, email envelope, billboard, newspaper, TV
- All icons are simple SVG shapes in muted grey/boring colors

The reels SPIN (translateY animation, fast at first then decelerating).
Reels stop one by one (left, center, right) with 0.3s delay between.
Results show: SPAM - BORING - OLD

The mascot peeks in from the left edge, shaking his head disapprovingly.
Lever pulls down with spring animation when reels start.
```

### Scene 3 — The Hammer Smash (6-7.5s)

```
Use remotion skills. Add Scene 3 to XciteAd.
Scene 3 (frames 180-225, seconds 6-7.5):

A large cartoon hammer enters from the top of frame with fast 
spring animation (high stiffness, low damping).
SMASH impact at frame 195.

On impact:
- Screen shake effect (translateX/Y random oscillation, 5px amplitude, 
  decaying over 15 frames)
- The slot machine splits into 8-12 SVG fragment pieces that fly 
  outward in random directions with rotation
- White flash overlay (opacity 1 to 0 over 5 frames)
- Small particle dots explode outward from impact point (20+ particles)
- Crack lines radiate from center

Sound effect marker at frame 195 (we'll add audio later).
All fragments continue flying off-screen with gravity (translateY 
increasing acceleration).
```

### Scene 4 — The Xcite Reveal (7.5-12s)

```
Use remotion skills. Add Scene 4 to XciteAd.
Scene 4 (frames 225-360, seconds 7.5-12):

From the center where the slot machine was destroyed:
- Particles converge inward (reverse explosion)
- The XCITE logo assembles from the particles with spring animation
- Logo: bold geometric text "XCITE" in white, 140px
- Subtle glow/bloom effect around the logo

After logo settles (0.5s pause):
- "PLAY. CONNECT. DOMINATE." types in below, letter by letter
- Background shifts to a vibrant gradient (deep purple to electric blue)

Behind the logo: 6-8 silhouette figures (simple SVG human outlines) 
fade in with staggered timing, representing the team.
Standing in a row, different heights, casual confident poses.

The mascot returns from bottom-right corner with a thumbs-up gesture 
and a wink (one eye smaller). Spring bounce entrance.

Final 1s: everything holds with subtle floating animation.
```

---

## REFINEMENT PROMPTS (use after each scene to polish)

```
Make the mascot's body bounce more naturally - use spring with 
damping: 12, stiffness: 100, mass: 0.8

Slow down the reel spinning deceleration - make it feel more 
mechanical and satisfying

Make the hammer impact more dramatic - bigger screen shake, 
more particles, add a radial shockwave ring that expands outward

Add motion blur to the flying fragments

Make the logo reveal more premium - add a subtle lens flare effect 
and golden accent particles

Adjust timing: give Scene 3 more impact by adding a 0.2s pause 
right before the hammer hits (anticipation)
```

---

## AUDIO (add after visuals are done)

Put audio files in the `public/` folder:

```
Use remotion skills. Add audio to XciteAd:

1. Voiceover file: public/voiceover.mp3 - starts at frame 0
2. Slot machine spinning sound: public/slot-spin.mp3 - starts at frame 95
3. Glass shatter SFX: public/shatter.mp3 - starts at frame 195
4. Whoosh/reveal sound: public/reveal.mp3 - starts at frame 225
5. Background music: public/bgm.mp3 - starts at frame 0, volume 0.3

Use <Audio> component for each, with startFrom prop matching the frames.
```

---

## RENDER COMMANDS

```bash
# Render 9:16 vertical (TikTok/Reels)
npx remotion render XciteAd xcite-vertical.mp4

# If you need 1:1 (Instagram feed) - create a square version
npx remotion render XciteAdSquare xcite-square.mp4

# If you need 16:9 (presentation/YouTube)  
npx remotion render XciteAdWide xcite-wide.mp4
```

---

## REFERENCE POSTS FROM X (best examples found)

- **Mascot animation**: @paulo_kombucha https://x.com/paulo_kombucha/status/2013968352864034883
- **3D cartoon style**: @hasan_ab_hasan https://x.com/hasan_ab_hasan/status/2015852487131980040
- **Multi-scene complex**: @brentbrookler https://x.com/brentbrookler/status/2019861800217628725
- **Official demo + prompt gist**: @Remotion https://x.com/Remotion/status/2013626968386765291
- **Best prompt strategy**: @GogHeng https://x.com/GogHeng/status/2020875190234923227
- **Team mode workflow**: @xiaoerzhan https://x.com/xiaoerzhan/status/2019705769449668726

---

## KEY TIPS FROM COMMUNITY

1. Start with Skills (`npx skills add remotion-dev/skills`)
2. Use pre-made assets for character (PNG/SVG transparent)
3. Iterate scene by scene, not all at once
4. Be ultra-specific with timeline (frame numbers or seconds)
5. Always say "use remotion skills" at start of prompt
6. Use spring() for everything - it looks more natural
7. Keep individual scenes simple, combine them after
8. For complex: describe scenes as temporal sequence
9. Framer Motion works inside Remotion
10. Three.js for 3D mascot is supported via @remotion/three
