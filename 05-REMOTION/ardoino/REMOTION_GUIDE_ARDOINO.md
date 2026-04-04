# REMOTION GUIDE — Paolo Ardoino News Video Project

> Remotion project for animated text overlay on the Paolo Ardoino mockumentary video.
> Created: March 31, 2026
> Source video: `popo.mp4` (1280x720, 29.97fps, ~2 minutes, H.264 + AAC)

---

## PROJECT STRUCTURE

```
remotion-news/
  src/
    index.ts          <- Entry point, registers RemotionRoot
    Root.tsx           <- Composition "NewsVideo" (1280x720, 29.97fps, 3622 frames)
    NewsVideo.tsx      <- Main layer: Video + Captions + Locations
    Captions.tsx       <- Caption overlay with typewriter (bottom-left)
    Locations.tsx      <- Location title overlay with live clock (top-left/right)
  public/
    popo.mp4           <- Source video (copied from news/)
  package.json
  tsconfig.json
```

---

## COMMANDS

```bash
# Launch the studio (browser preview)
cd remotion-news
npx remotion studio

# The studio opens at http://localhost:3000
# Automatic hot reload — every file change updates in real-time
```

---

## COMPONENT 1: CAPTIONS (`Captions.tsx`)

### What it does
Animated text with typewriter effect appearing at the bottom-left of the video.
They serve as visual counterpoint to the news audio — first the numbers of accusations, then the evidence that they won.

### Style
- **Font:** `dec_terminal_modern` (installed on system), monospace
- **Position:** bottom-left, padding 60px from bottom, 40px from left
- **Color:** white with dark text-shadow (`0 0 10px rgba(0,0,0,0.8), 0 0 20px rgba(0,0,0,0.5)`)
- **Size:** 24px during typing, shrinks to 15px when the next line starts

### Typewriter animation
- Each line types out letter by letter at the speed defined in the `speed` field (chars per frame)
- Blinking cursor `▌` every 15 frames, visible only during the typing phase
- The cursor disappears when all lines are typed

### Shrink animation
- When the next line starts typing, the previous line shrinks smoothly:
  - Font: 24px → 15px
  - Opacity: 1 → 0.7
  - Duration: 15 frames with `Easing.out(cubic)`
- The last line of each caption stays large (no line after it)

### Fade out
- In the last 10 frames of each caption, the entire block fades to opacity 0
- Easing: `Easing.out(cubic)`

### Per-line parameters
Each line has 3 configurable parameters:
- `text` — the text to display
- `speed` — characters per frame (1 = slow/readable, 2 = fast)
- `pauseAfter` — pause frames after the line finishes typing (before the next one starts)

The `pauseAfter` controls how long each line stays "large" before shrinking.
Longer/more important lines → higher pauseAfter. Short lines → low pauseAfter.

### The 4 current captions

**Caption 1 — The accusations (frame 325-625, 300 frames)**
```
Line 1: "6 lawsuits filed. 19 federal investigations opened."
        speed: 1, pauseAfter: 20
Line 2: "$61 million in fines paid. $1.4 trillion in damages claimed against Tether."
        speed: 1, pauseAfter: 20
Line 3: "Every single case was dismissed or settled. Zero findings of fraud."
        speed: 1, pauseAfter: 0
```

**Caption 2 — The short sellers (frame 970-1170, 200 frames)**
```
Line 1: '"Fir Tree" bet billions on Tether's collapse. Shut down 2025.'
        speed: 1, pauseAfter: 35
Line 2: "Hindenburg offered $1M bounty for proof of fraud."
        speed: 1.5, pauseAfter: 25
Line 3: "No report. They shut down too."
        speed: 2, pauseAfter: 0
```
Note: line 1 is the slowest (longest), line 3 is the fastest (shortest).
pauseAfter decreasing: 35 → 25 → 0 (line 1 stays large the longest).

**Caption 3 — The numbers (frame 1444-1628, 184 frames)**
```
Line 1: "$10B redeemed in two weeks during the 2022 crash. Every dollar honored."
        speed: 1.5, pauseAfter: 45
Line 2: "$13 billion profit in 2024. Fewer than 200 employees."
        speed: 1.5, pauseAfter: 0
```

**Caption 4 — The origins (frame 2504-2683, 179 frames)**
```
Line 1: "A family of farmers from a village of 1,900 people."
        speed: 1, pauseAfter: 30
Line 2: "Two Italians from small towns built the largest stablecoin on Earth."
        speed: 1, pauseAfter: 0
```

### How to add a new caption
Add an object to the `CAPTIONS` array in `Captions.tsx`:
```tsx
{
  start: START_FRAME,
  end: END_FRAME,
  lines: [
    { text: "Line 1 text", speed: 1, pauseAfter: 20 },
    { text: "Line 2 text", speed: 1.5, pauseAfter: 0 },
  ],
},
```

### How to modify speed and timing
- `speed: 1` = 1 character per frame (slow, ~30 chars/sec)
- `speed: 1.5` = 1.5 chars/frame (medium)
- `speed: 2` = 2 chars/frame (fast)
- `pauseAfter: 20` = 20 frames (~0.67 sec) pause before the next line
- The higher the `pauseAfter`, the longer the line stays large and visible

---

## COMPONENT 2: LOCATIONS (`Locations.tsx`)

### What it does
Documentary-style location titles that appear at the top. Typewriter effect on entry,
hold with a real-time ticking clock, reverse typewriter (backspace) on exit.

### Style
- **Font:** `Inter` / `Helvetica Neue`, weight 300 (thin), sans-serif
- **Size:** 16px, all UPPERCASE, letter-spacing 3px
- **Color:** white, opacity 0.85
- **Text-shadow:** `0 0 8px rgba(0,0,0,0.6)`
- **Position:** top-left by default (40px top, 40px left), configurable top-right per individual location

### Animation
1. **Type in** — letters appear one by one, 2 chars/frame, blinking cursor `▌`
2. **Hold** — 90 frames (~3 sec), full text visible, ticking clock
3. **Type out (reverse)** — letters disappear from the end, like backspace, 2 chars/frame

### Live clock
- Seconds advance in real-time (1 increment every 30 frames)
- The colon `:` blinks every half second (15 frames visible, 15 frames empty space)
- Each location has a different starting time with different seconds
- The clock ticks during both hold and typing (if the time characters are already visible)

### The 6 current locations

| Frame | Location | Time | Position |
|-------|----------|------|----------|
| 0 | El Salvador, Central America | 4:48:03 AM | top-left |
| 214 | El Salvador, Central America | 5:30:14 AM | top-left |
| 1154 | Undisclosed Dojo | 6:00:37 PM | **top-right** |
| 2170 | Private Residence | 11:47:52 PM | top-left |
| 2501 | Cisano sul Neva, North Italy — Population: 1,900 | (none) | top-left |
| 3176 | Washington D.C., United States | (none) | top-left |

### How to add a new location
```tsx
// With clock:
{ startFrame: 500, location: "Location Name", time: { hour: 3, minute: 15, startSecond: 42, ampm: "PM" } },

// Without clock:
{ startFrame: 500, location: "Location Name" },

// Top-right position:
{ startFrame: 500, location: "Location Name", position: "top-right" },
```

### How to change the timing
- `HOLD_FRAMES = 90` — how long the text stays visible (in frames)
- `CHARS_PER_FRAME = 2` — typewriter in/out speed
- Total duration is calculated automatically: type_in + hold + type_out

---

## COMPOSITION (`NewsVideo.tsx`)

```tsx
<AbsoluteFill style={{ backgroundColor: "black" }}>
  <Video src={staticFile("popo.mp4")} />   <- Video underneath
  <Captions />                              <- Text bottom-left
  <Locations />                             <- Location top-left/right
</AbsoluteFill>
```

The layers are stacked: video at the bottom, captions above, locations on top.
They don't visually overlap because captions are at the bottom and locations are at the top.

---

## EXPORT FOR PREMIERE PRO

To export ONLY the text (without video) with transparent background:

1. Create an alternate composition without the `<Video>`, only `<Captions />` and `<Locations />`
   with `backgroundColor: "transparent"`
2. Render as WebM with transparency:
   ```bash
   npx remotion render src/index.ts OverlayOnly out/overlay.webm --codec=vp8
   ```
3. Or as transparent PNG sequence:
   ```bash
   npx remotion render src/index.ts OverlayOnly out/frames --image-format=png
   ```
4. Import in Premiere as a layer over the original video

---

## GLOBAL CONSTANTS TO REMEMBER

| Constant | Captions | Locations |
|----------|----------|-----------|
| Font | dec_terminal_modern | Inter / Helvetica Neue |
| Size | 24px (big) / 15px (small) | 16px |
| Position | bottom 60px, left 40px | top 40px, left/right 40px |
| Cursor | `▌` blink every 15 frames | `▌` blink every 15 frames |
| Video FPS | 29.97 | 30 (approximated for clock) |
| Fade out | 10 frames, easeOut cubic | none (reverse typewriter) |
| Shrink | 15 frames, 24→15px, 1→0.7 opacity | none |
