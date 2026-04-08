# REMOTION + HIGGSFIELD VIBE MOTION — COMPLETE GUIDE

> Compiled: April 2026
> Sources: remotion.dev docs, LogRocket guide, Tella YouTube tutorial, Medium (Remotion + Claude Code), Higgsfield blog x2

---

## 1. REMOTION — FUNDAMENTALS

### What is Remotion
Remotion = **React for video**. You write TypeScript/React components that render frame by frame into MP4. No timeline, no GUI — everything is code.

### Core Concept
> "Remotion gives you a frame number and a blank canvas, on which you can render anything using React."

- Videos are **a function of images over time**
- Changing content on each frame = animation
- Frame numbering starts from `0`
- Last frame = `durationInFrames - 1`
- Duration in seconds = `durationInFrames / fps`

### Video Properties (required)
| Property | Type | Example |
|---|---|---|
| `width` | pixels | 1080 |
| `height` | pixels | 1920 |
| `durationInFrames` | total frame count | 450 |
| `fps` | framerate | 30 |

### Main Hooks
```tsx
// Current frame (starts from 0)
const frame = useCurrentFrame();

// All video properties
const { width, height, fps, durationInFrames } = useVideoConfig();
```

### Built-in Components
| Component | Usage |
|---|---|
| `<AbsoluteFill>` | Full-screen container (like a fullscreen div) |
| `<Sequence>` | Timing control — shows a component from a certain frame |
| `<Series>` | Sequential playback — one after another |
| `<Video>` | Embed source video |
| `<Audio>` | Embed audio |
| `<Img>` | Static image |

---

## 2. PROJECT SETUP

### Installation
```bash
npm init video
```
- Choose the **blank** template
- Add **Tailwind CSS** (yes for styling)
- Add **agent skills** for Claude Code

### Project Structure
```
my-video/
├── src/
│   ├── Root.tsx          # Registers all Compositions
│   ├── index.ts          # Entry point
│   └── components/       # Your video components
├── public/               # Assets (images, videos, fonts)
├── package.json
└── remotion.config.ts
```

### Launch Remotion Studio
```bash
cd my-video
npm run dev
```
Opens Remotion in Chrome:
- **Left panel:** composition list
- **Right panel:** props editable in real-time
- **Renders tab:** video file generation

---

## 3. COMPOSITIONS

### Registering a Composition
In `src/Root.tsx`:
```tsx
import { Composition } from "remotion";
import { MyAnimation } from "./components/MyAnimation";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MyAnimation"
        component={MyAnimation}
        durationInFrames={150}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Hello World",
          color: "#ff0000",
        }}
      />
    </>
  );
};
```

### Composition with Zod Schema (typed and UI-editable props)
```tsx
import { z } from "zod";
import { zColor } from "@remotion/zod-types";

export const mySchema = z.object({
  title: z.string(),
  titleColor: zColor(),
  numberValue: z.number(),
});

export const MyComponent: React.FC<z.infer<typeof mySchema>> = ({
  title,
  titleColor,
  numberValue,
}) => {
  const frame = useCurrentFrame();
  const opacity = Math.min(1, frame / 60);

  return (
    <AbsoluteFill style={{ backgroundColor: "white" }}>
      <div style={{ opacity, color: titleColor, fontSize: 80 }}>
        {title}
      </div>
    </AbsoluteFill>
  );
};
```

Register with schema:
```tsx
<Composition
  id="MyComponent"
  component={MyComponent}
  durationInFrames={150}
  fps={30}
  width={1080}
  height={1920}
  schema={mySchema}
  defaultProps={{
    title: "Hello",
    titleColor: "#ffffff",
    numberValue: 42,
  }}
/>
```

---

## 4. ANIMATIONS

### FUNDAMENTAL RULE
> **ALWAYS animate using `useCurrentFrame()`** — never CSS transitions or browser animations. They cause flickering during render.

### Basic Frame Animation
```tsx
const frame = useCurrentFrame();

// Fade in over the first 30 frames
const opacity = Math.min(1, frame / 30);

// Slide from left
const translateX = Math.max(0, 100 - frame * 5);

// Scale from 0 to 1
const scale = Math.min(1, frame / 20);
```

### interpolate() — Value Mapping

Maps one range of values to another. 4 arguments: input value, input range, output range, options.

```tsx
import { interpolate } from "remotion";

// Fade in from frame 0 to 60
const opacity = interpolate(frame, [0, 60], [0, 1], {
  extrapolateRight: "clamp",
});

// Slide + hold — enters from frame 0 to 20, then stays put
const translateY = interpolate(frame, [0, 20, 50], [100, 0, 0], {
  extrapolateRight: "clamp",
});

// Fade in + fade out
const { durationInFrames } = useVideoConfig();
const fadeInOut = interpolate(
  frame,
  [0, 20, durationInFrames - 20, durationInFrames],
  [0, 1, 1, 0],
  { extrapolateRight: "clamp" }
);
```

**Extrapolation options** (what happens outside the range):
| Option | Effect |
|---|---|
| `"extend"` (default) | Continues beyond the range |
| `"clamp"` | Stops at the limit value — **USE ALMOST ALWAYS** |
| `"wrap"` | Cyclic loop |
| `"identity"` | Returns the original input value |

You can set `extrapolateLeft` and `extrapolateRight` separately.

**Easing** — interpolation curve (default = linear):
```tsx
import { Easing } from "remotion";

const opacity = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.25, 0.1, 0.25, 1), // standard ease
  extrapolateRight: "clamp",
});
```

### spring() — Natural Physics Animation

Animates from 0 to 1 with real physics (bounce, overshoot).

```tsx
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const scale = spring({
  frame,
  fps,
  config: {
    mass: 1,        // weight (low = fast)
    stiffness: 100,  // bounce (high = more bouncy)
    damping: 10,     // friction (high = less bounce)
    overshootClamping: false, // true = never exceed target
  },
});
```

**Spring parameters:**
| Parameter | Default | Effect |
|---|---|---|
| `frame` | required | Current frame |
| `fps` | required | FPS from video config |
| `from` | 0 | Start value |
| `to` | 1 | End value |
| `reverse` | false | Reverses the animation |
| `delay` | 0 | Frame delay before starting |
| `durationInFrames` | auto | Forces exact duration |
| `config.mass` | 1 | Weight — low = fast |
| `config.damping` | 10 | Friction — high = less bounce |
| `config.stiffness` | 100 | Stiffness — high = more bouncy |
| `config.overshootClamping` | false | Blocks overshoot |

**Combining spring + interpolate:**
```tsx
// Spring from 0 to 1, then map to marginLeft from 0 to 200px
const springValue = spring({ frame, fps });
const marginLeft = interpolate(springValue, [0, 1], [0, 200]);
```

**Application order:** duration → reverse → delay

### Sequence (component timing)

Controls WHEN a component appears and for HOW LONG.

```tsx
import { Sequence } from "remotion";

// Title appears at frame 0, lasts 60 frames
<Sequence from={0} durationInFrames={60}>
  <Title text="Hello" />
</Sequence>

// Subtitle appears at frame 30, lasts 90 frames
<Sequence from={30} durationInFrames={90}>
  <Subtitle text="World" />
</Sequence>
```

**Sequence Props:**
| Prop | Usage |
|---|---|
| `from` | Start frame (default 0) |
| `durationInFrames` | Duration in frames (default Infinity) |
| `name` | Name in Studio timeline |
| `layout` | `"absolute-fill"` (default) or `"none"` |
| `style` | CSS styles |

**Tricks:**
- **Delay:** `<Sequence from={30}>` — appears after 30 frames
- **Trim start:** `<Sequence from={-15}>` — skips the first 15 frames of content
- **Nesting:** Sequence inside Sequence = the from values add up (30 + 60 = 90)
- Children calling `useCurrentFrame()` receive the frame **relative** to the Sequence (starting from 0)

### Img — Images

```tsx
import { AbsoluteFill, Img, staticFile } from "remotion";

// From public/
<Img src={staticFile("hi.png")} />

// From remote URL
<Img src="https://example.com/image.jpg" />
```
- Remotion waits for the image to load before rendering the frame (no flicker)
- `maxRetries` defaults to 2 with exponential backoff
- Do NOT use for GIFs — use `@remotion/gif`

### Video — Embedding video

```tsx
import { AbsoluteFill, OffthreadVideo, staticFile } from "remotion";

// OffthreadVideo = better performance (extracts frames with FFmpeg)
<OffthreadVideo src={staticFile("video.mp4")} />

// Trim
<OffthreadVideo src={staticFile("video.mp4")} trimBefore={60} />

// Speed
<OffthreadVideo src={staticFile("video.mp4")} playbackRate={0.5} />

// Muted
<OffthreadVideo src={staticFile("video.mp4")} muted />
```

**OffthreadVideo vs Html5Video:**
| | OffthreadVideo | Html5Video |
|---|---|---|
| Performance | Better (FFmpeg) | Browser-based |
| Rendering | Frames extracted as images | Native video tag |
| Transparency | `transparent={true}` | No |
| Client-side | NO | YES |
| Recommended for | Final render | Preview in Studio |

### fitText() — Auto-fitting text

```tsx
import { fitText } from "@remotion/layout-utils";

const { fontSize } = fitText({
  text: "Hello World",
  withinWidth: 600,
  fontFamily: "Arial",
  fontWeight: "bold",
});

// Use in style
<div style={{ fontSize }}>Hello World</div>
```
- The font MUST be loaded before calling `fitText()`
- Use `outline` instead of `border` (border shrinks the container due to box-sizing)

---

## 5. RENDERING

### From Remotion Studio
1. Click **Render video** in the Renders tab
2. Configure output (quality, format)
3. Click **Render video** to generate MP4
4. FFmpeg is already embedded — no separate installation needed

### From CLI
```bash
# Render MP4
npx remotion render src/index.ts MyComposition out/video.mp4

# Render PNG sequence (for compositing in Premiere/ffmpeg)
npx remotion render src/index.ts MyComposition --sequence --image-format=png out/frames

# Render ProRes (maximum quality)
npx remotion render src/index.ts MyComposition --codec=prores --prores-profile=4444 out/video.mov
```

### Compositing PNG + Video with ffmpeg
```bash
# YouTube quality
ffmpeg -y -i public/source.mp4 \
  -framerate 30000/1001 -start_number 0 -i out/frames/element-%04d.png \
  -filter_complex "[0:v][1:v]overlay=0:0:format=auto[out]" \
  -map "[out]" -map 0:a? \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
  -profile:v high -level 4.1 -movflags +faststart \
  -r 30000/1001 -c:a aac -b:a 320k out/youtube.mp4
```

---

## 6. WORKFLOW WITH CLAUDE CODE

### How It Works
1. **Find inspiration** — Pinterest, YouTube screenshots, static images
2. **Give the image to Claude** — drag & drop into the terminal
3. **Simple prompt** — "animate this", "recreate this as a motion graphic"
4. **Claude writes the code** — creates the React component + registers it
5. **Preview in Remotion Studio** — see the result in real-time in Chrome
6. **Iterate** — "make the font smaller", "change colors", "make it horizontal"
7. **Render** — export as MP4 or ProRes

### Tips from the Video Tutorial (Tella)
- **Start simple** — don't overcomplicate the first prompt
- **Give only the image first** — let Claude interpret, then correct
- **Arrows are tricky** — avoid them initially
- **You can provide Excel data** — Claude transforms it into animated charts
- **For inspiration videos** — use ffmpeg to analyze frame by frame:
  ```
  "Use ffmpeg to analyze [file] and create a similar animation where words come in one by one"
  ```
- **Each composition** automatically appears in the left panel of Remotion Studio
- **Render ProRes** for maximum quality when exporting

### Effective Prompts for Claude + Remotion
```
# From static image
"Animate this diagram as a Remotion composition. Make the bars grow from bottom to top."

# From video screenshot
"Use ffmpeg to analyze this video and recreate the animation where text appears word by word."

# Modification
"Make the diagram horizontal and make sure the center font isn't yellow."

# Custom data
"Make this an upward graph showing newsletter subscriber growth to 12,500 subscribers."
```

---

## 7. HIGGSFIELD VIBE MOTION

### What it is
AI motion design via chat — you create motion graphics, presentations, and visuals with a conversational interface instead of a timeline editor.

### Workflow
1. **Concept** — describe the idea in words ("Create a kinetic typography intro")
2. **Assets** — upload images, videos, logos, PDFs
3. **Template** (optional) — choose a template with pre-built motion logic
4. **Refine in UI** — adjust fonts, colors, animation speed manually
5. **Iterate** — changes are visible in real-time

### Use Cases
- **Animated infographics** — growing numbers, sections appearing in sequence
- **Presentations** — investor decks, sales, product walkthroughs
- **Logo/Brand animations** — reusable animations from uploaded logos

### Tips for Better Animations

**Sketches and Input**
- Simple drawings with clear outlines
- Avoid cluttered backgrounds or crowded scenes
- One main action per frame

**Easing Styles**
| Type | When to use |
|---|---|
| Linear | Robots, machines, tech |
| Ease In | Character movement start |
| Ease Out | Gentle stops |
| Ease In-Out | Natural, dynamic movement |

**Keyframe Spacing**
- Close keyframes = fast movement
- Far keyframes = slow movement

**Cinematic Effects**
- Motion blur: minimal for slow scenes, strong for fast action
- Depth of field: focus on subject, blur on background
- Subtle details: hair bounce, clothing flutter, blink

**Prompt Engineering for Higgsfield**
- Detailed descriptions = better results
- Use **negative prompts**: "no blur, no noise, no extra limbs"
- Avoid impossible requests ("square shaped sphere")

**Quality Check Before Export**
- Minimum resolution 1024x1024
- Preview frame by frame
- Verify motion blur and depth of field
- Choose the right format (MP4 for video, GIF for loops)

---

## 8. LESSONS FROM THE ARDOINO PROJECT (Remotion)

From the previous project in the `ardoino/remotion-news/` folder:

### Setup That Worked
- Remotion 4.0.267 + React 19 + TypeScript 5.7
- 1280x720, 30000/1001 fps (29.97 NTSC)
- Source video in `public/`

### Transparent Overlay Pattern
Two compositions:
| ID | Usage |
|---|---|
| `NewsVideo` | Video + overlay (complete export) |
| `OverlayOnly` | Text only on transparent (for compositing in Premiere/ffmpeg) |

### Typewriter Effect
- Monospace terminal font
- Variable speed (1-2 chars/frame)
- Blinking cursor `▌` (15 frames on/off)
- Previous lines shrink with opacity fade
- Subtle white glow via text-shadow

### Final Export (NO direct render, YES PNG sequence)
```bash
# Step 1: PNG sequence
npx remotion render src/index.ts OverlayOnly --sequence --image-format=png --concurrency=4 out/frames

# Step 2: ffmpeg composite
ffmpeg -y -i public/video.mp4 \
  -framerate 30000/1001 -start_number 0 -i out/frames/element-%04d.png \
  -filter_complex "[0:v][1:v]overlay=0:0:format=auto[out]" \
  -map "[out]" -map 0:a? \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
  -r 30000/1001 out/final.mp4
```

### Mistakes to Avoid
1. **Never `fps={29.97}`** → use `fps={30000/1001}` to avoid frame drift
2. **ProRes 4444 + glow = white blobs** → the premultiplied alpha channel makes text-shadows opaque
3. **PNG sequence + ffmpeg >> direct Remotion render** → zero stutter
4. **`yuvj420p` causes problems in Premiere** → force `-pix_fmt yuv420p`
5. **CRF 16** for YouTube, **CRF 20** for Twitter

---

## 9. MOTION DESIGN — AFTER EFFECTS PRINCIPLES APPLIED TO REMOTION

> Source: "Motion Graphics Tutorials in After Effects" playlist by Dope Motions (85 videos)
> Every AE concept is mapped to its Remotion equivalent

---

### 9.1 EASING AND SPEED GRAPH (Timing vs Spacing)

**In AE:** The Speed Graph controls acceleration/deceleration. "Timing" = WHEN things happen (distance between keyframes). "Spacing" = HOW they move (the curve between keyframes). Ease High/Ease Low control the acceleration ramp.

**In Remotion:**
```tsx
import { Easing, interpolate } from 'remotion';

// Smooth ease-in-out (equivalent to F9 in AE)
const value = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.42, 0, 0.58, 1),
});

// Strong ease-out (equivalent to dragging handle left in AE)
const value = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0, 0.55, 0.45, 1),
});

// Strong ease-in + light ease-out (Ease High=80, Ease Low=15)
const value = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.7, 0, 0.3, 1),
});

// Bounce / overshoot with spring()
const scale = spring({ frame, fps, config: {
  mass: 0.5, damping: 8, stiffness: 150, overshootClamping: false
}});
```

**Key rule:** Never use linear animations. Everything should have an easing curve.

---

### 9.2 TEXT ANIMATOR (Position + Opacity + Blur)

**In AE:** Text Animator with Position, Opacity, Blur + Range Selector with "Ramp Up" shape + Based On "Words/Characters". Creates word-by-word or character-by-character text reveals with blur on entry.

**In Remotion:**
```tsx
const TextReveal: React.FC<{text: string; startFrame: number}> = ({text, startFrame}) => {
  const frame = useCurrentFrame();
  const words = text.split(' ');
  const staggerDelay = 4; // frames between each word

  return (
    <div style={{display: 'flex', gap: 8, flexWrap: 'wrap'}}>
      {words.map((word, i) => {
        const localFrame = frame - startFrame - i * staggerDelay;
        const progress = interpolate(localFrame, [0, 15], [0, 1], {
          extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
          easing: Easing.bezier(0.25, 0.1, 0.25, 1),
        });
        const y = interpolate(progress, [0, 1], [50, 0]);
        const opacity = progress;
        const blur = interpolate(progress, [0, 1], [10, 0]);

        return (
          <span key={i} style={{
            transform: `translateY(${y}px)`,
            opacity,
            filter: `blur(${blur}px)`,
          }}>
            {word}
          </span>
        );
      })}
    </div>
  );
};
```

**Variants:**
- `Based On Characters`: change `text.split(' ')` to `text.split('')` and reduce `staggerDelay` to 1-2
- `Randomize Order`: add a shuffled index array for appearance order
- `Ramp Up / Ramp Down`: controls reveal direction (left→right vs right→left)

---

### 9.3 STAGGER / LAYER DISPLACEMENT

**In AE:** Offsetting layers by 10-15 frames from each other to create cascading animations. A fundamental motion design principle — never animate everything at once.

**In Remotion:**
```tsx
// Simple stagger: each element starts N frames after the previous one
const elements = ['Title', 'Subtitle', 'CTA'];
const staggerOffset = 10; // frames between each element

return (
  <AbsoluteFill>
    {elements.map((el, i) => (
      <Sequence key={i} from={i * staggerOffset}>
        <AnimatedElement>{el}</AnimatedElement>
      </Sequence>
    ))}
  </AbsoluteFill>
);
```

**Key rule:** Ideal stagger is 8-15 frames at 30fps. Too little = looks simultaneous. Too much = feels slow.

---

### 9.4 REPEATER (Procedural Patterns)

**In AE:** The Repeater duplicates and transforms elements procedurally. Two nested repeaters create grids. Combined with Trim Path it creates complex patterns from a single shape layer.

**In Remotion:**
```tsx
// Procedural grid with double repeater
const PatternGrid: React.FC = () => {
  const frame = useCurrentFrame();
  const cols = 8;
  const rows = 6;
  const size = 60;
  const gap = 80;

  return (
    <AbsoluteFill>
      {Array.from({length: rows}).map((_, row) =>
        Array.from({length: cols}).map((_, col) => {
          const delay = (row + col) * 3;
          const scale = interpolate(frame - delay, [0, 20], [0, 1], {
            extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
            easing: Easing.out(Easing.cubic),
          });
          const rotation = interpolate(frame, [0, 150], [0, 360]);

          return (
            <div key={`${row}-${col}`} style={{
              position: 'absolute',
              left: col * gap + 100,
              top: row * gap + 100,
              width: size, height: size,
              borderRadius: '50%',
              border: '2px solid rgba(255,255,255,0.3)',
              transform: `scale(${scale}) rotate(${rotation}deg)`,
            }} />
          );
        })
      )}
    </AbsoluteFill>
  );
};
```

**Tip:** For symmetrical rotating patterns (CC Kaleidoscope style), duplicate and rotate the same component N times:
```tsx
{Array.from({length: 6}).map((_, i) => (
  <div key={i} style={{
    position: 'absolute', inset: 0,
    transform: `rotate(${i * 60}deg)`,
  }}>
    <PatternSlice frame={frame} />
  </div>
))}
```

---

### 9.5 TRIM PATH (SVG Stroke Animation)

**In AE:** Trim Paths animates the start/end of a stroke. Widely used for line art, logos, and decorations.

**In Remotion:**
```tsx
const AnimatedStroke: React.FC = () => {
  const frame = useCurrentFrame();
  const pathLength = 500; // total path length
  const progress = interpolate(frame, [0, 40], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.65, 0, 0.35, 1),
  });

  return (
    <svg width={400} height={400} viewBox="0 0 400 400">
      <circle cx={200} cy={200} r={150}
        fill="none" stroke="white" strokeWidth={3}
        strokeDasharray={pathLength}
        strokeDashoffset={pathLength * (1 - progress)}
      />
    </svg>
  );
};
```

**For animated offset** (equivalent to the Offset property in Trim Paths):
```tsx
const offset = interpolate(frame, [0, 150], [0, pathLength]);
// strokeDashoffset={pathLength * (1 - progress) + offset}
```

---

### 9.6 DROP SHADOW WITH NOISE (Anti-Banding)

**In AE:** Adding 2-5% noise to drop shadows prevents color banding in renders. Shadows add depth and separation between elements.

**In Remotion:**
```tsx
// CSS drop shadow + noise overlay for anti-banding
<div style={{
  boxShadow: '0 20px 60px rgba(0,0,0,0.4)',
  position: 'relative',
}}>
  {children}
  {/* Noise overlay anti-banding */}
  <div style={{
    position: 'absolute', inset: 0, pointerEvents: 'none',
    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")`,
    opacity: 0.03,
    mixBlendMode: 'overlay',
  }} />
</div>
```

**Inner Shadow** (cut-out / engraving effect):
```tsx
<div style={{
  boxShadow: 'inset 0 4px 30px rgba(0,0,0,0.5)',
  borderRadius: 20,
}}>
```

---

### 9.7 DISPLACEMENT MAP / WAVE WARP

**In AE:** Displacement Map distorts the image based on a map. Wave Warp adds undulations. Turbulent Displace creates organic distortions.

**In Remotion (SVG Filter):**
```tsx
const DisplacementEffect: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const turbulence = interpolate(frame, [0, 60], [0.01, 0.03], {
    extrapolateRight: 'clamp',
  });

  return (
    <>
      <svg width={0} height={0}>
        <defs>
          <filter id="displace">
            <feTurbulence
              type="fractalNoise"
              baseFrequency={turbulence}
              numOctaves={3}
              seed={42}
            />
            <feDisplacementMap in="SourceGraphic" scale={20} />
          </filter>
        </defs>
      </svg>
      <div style={{filter: 'url(#displace)'}}>
        {children}
      </div>
    </>
  );
};
```

**Simple wave effect without SVG:**
```tsx
// Undulation via transform
const wave = Math.sin(frame * 0.1) * 10;
<div style={{transform: `translateY(${wave}px) skewX(${wave * 0.5}deg)`}}>
```

---

### 9.8 ALPHA MATTE / TRACK MATTE (Masking)

**In AE:** Track Matte Alpha uses a layer's transparency to mask another. Used everywhere: text revealing images, shape reveal, parallax with mask.

**In Remotion:**
```tsx
// Image revealed through text (like Alpha Matte)
<div style={{
  fontSize: 200, fontWeight: 900,
  backgroundImage: 'url(/media/photo.jpg)',
  backgroundSize: 'cover',
  backgroundClip: 'text',
  WebkitBackgroundClip: 'text',
  color: 'transparent',
}}>
  CANDY
</div>

// Shape reveal with overflow hidden (Stencil Alpha)
const ShapeReveal: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const scale = spring({frame, fps: 30, config: {damping: 12}});

  return (
    <div style={{overflow: 'hidden', position: 'relative'}}>
      <div style={{
        position: 'absolute', inset: 0,
        background: 'white',
        borderRadius: '50%',
        transform: `scale(${scale})`,
        transformOrigin: 'center',
      }} />
      <div style={{position: 'relative'}}>{children}</div>
    </div>
  );
};

// Clip-path reveal (more flexible)
const clipProgress = interpolate(frame, [0, 30], [0, 100], {
  extrapolateRight: 'clamp',
});
<div style={{clipPath: `inset(0 ${100 - clipProgress}% 0 0)`}}>
```

---

### 9.9 RGB SPLIT + WIGGLE (Glitch)

**In AE:** Duplicate the layer 3 times, isolate R/G/B per channel, blend mode Screen, add wiggle expression for random movement. Optics Compensation for lens distortion.

**In Remotion:**
```tsx
const RGBGlitch: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  // Wiggle: sin with different frequencies for randomness
  const offsetR = Math.sin(frame * 0.3) * 4 + Math.sin(frame * 0.7) * 2;
  const offsetB = Math.sin(frame * 0.4 + 1) * 4 + Math.cos(frame * 0.6) * 2;

  return (
    <div style={{position: 'relative'}}>
      {/* Red channel */}
      <div style={{
        position: 'absolute', inset: 0,
        transform: `translate(${offsetR}px, ${-offsetR * 0.5}px)`,
        mixBlendMode: 'screen',
        filter: 'grayscale(1) brightness(0.5) sepia(1) hue-rotate(-30deg) saturate(5)',
      }}>{children}</div>
      {/* Green channel (base) */}
      <div style={{
        position: 'relative',
        mixBlendMode: 'screen',
        filter: 'grayscale(1) brightness(0.5) sepia(1) hue-rotate(90deg) saturate(5)',
      }}>{children}</div>
      {/* Blue channel */}
      <div style={{
        position: 'absolute', inset: 0,
        transform: `translate(${offsetB}px, ${offsetB * 0.3}px)`,
        mixBlendMode: 'screen',
        filter: 'grayscale(1) brightness(0.5) sepia(1) hue-rotate(200deg) saturate(5)',
      }}>{children}</div>
    </div>
  );
};
```

---

### 9.10 MOTION TRAIL / ECHO

**In AE:** The Echo effect creates motion trails by duplicating previous frames with decreasing opacity. Combined with motion blur, it creates cinematic trails.

**In Remotion:**
```tsx
// Motion trail: render N copies at previous positions
const MotionTrail: React.FC<{getPosition: (f: number) => number; trailLength?: number}> = ({
  getPosition, trailLength = 6
}) => {
  const frame = useCurrentFrame();

  return (
    <>
      {Array.from({length: trailLength}).map((_, i) => {
        const trailFrame = Math.max(0, frame - i * 2);
        const opacity = interpolate(i, [0, trailLength], [0.8, 0]);
        const pos = getPosition(trailFrame);
        return (
          <div key={i} style={{
            position: 'absolute',
            transform: `translateX(${pos}px)`,
            opacity,
            filter: `blur(${i * 0.5}px)`,
          }}>
            <MyElement />
          </div>
        );
      })}
    </>
  );
};
```

---

### 9.11 PARENTING + NULL OBJECT CONTROLLER

**In AE:** Parenting links layers to a parent — move the parent, all children move. Null Object is an invisible controller for animating groups.

**In Remotion:** This is native — React components are already nested. A wrapper div with animated transform moves all children:
```tsx
const GroupController: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const y = interpolate(frame, [60, 90], [0, -500], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    easing: Easing.bezier(0.65, 0, 0.35, 1),
  });

  return (
    <div style={{transform: `translateY(${y}px)`}}>
      {children}  {/* Everything moves together */}
    </div>
  );
};
```

---

### 9.12 TIME REMAPPING / SPEED RAMP

**In AE:** Time Remapping allows speeding up/slowing down video at specific points. The Speed Graph curve controls the transition between speeds.

**In Remotion:**
```tsx
// Speed ramp on video: variable playbackRate
// Note: OffthreadVideo accepts a fixed playbackRate, not variable.
// For complex speed ramps, use interpolate to map non-linear frames:

const timeRemap = interpolate(frame, [0, 30, 45, 90], [0, 30, 60, 90], {
  // 0-30: normal speed (1x)
  // 30-45: double speed (30 frames compressed into 15)
  // 45-90: normal speed again
});

// Use timeRemap as the "remapped" frame for any animation
const position = interpolate(timeRemap, [0, 90], [0, 1000]);
```

---

### 9.13 LOOP EXPRESSIONS

**In AE:** `loopOut("cycle")` repeats keyframes infinitely. `loopOut("pingpong")` repeats them back and forth.

**In Remotion:**
```tsx
// Loop cycle: use modulo
const loopDuration = 60; // frames
const loopFrame = frame % loopDuration;
const value = interpolate(loopFrame, [0, 30, 60], [0, 100, 0]);

// Loop pingpong
const pingPongFrame = (() => {
  const cycle = frame % (loopDuration * 2);
  return cycle < loopDuration ? cycle : loopDuration * 2 - cycle;
})();

// Continuous wiggle (equivalent to wiggle(freq, amp))
const wiggle = (f: number, freq: number, amp: number) =>
  Math.sin(f * freq * 0.1) * amp +
  Math.sin(f * freq * 0.23 + 1.5) * amp * 0.5 +
  Math.cos(f * freq * 0.37 + 3.0) * amp * 0.25;
```

---

### 9.14 FLICKER REVEAL

**In AE:** Rapidly alternating opacity between 0% and 100% over 2 frames each to create a cinematic "flicker" reveal effect.

**In Remotion:**
```tsx
const FlickerReveal: React.FC<{children: React.ReactNode; startFrame: number}> = ({
  children, startFrame
}) => {
  const frame = useCurrentFrame();
  const localFrame = frame - startFrame;

  // Flicker pattern: [on, off, on, off, on, on, on...]
  const flickerPattern = [0, 1, 0.5, 0.1, 0.8, 0.3, 1, 0.1, 0.5, 1, 1, 1, 1];
  const flickerIndex = Math.min(localFrame, flickerPattern.length - 1);
  const opacity = localFrame < 0 ? 0 :
    localFrame >= flickerPattern.length ? 1 :
    flickerPattern[Math.floor(flickerIndex)];

  return <div style={{opacity}}>{children}</div>;
};
```

---

### 9.15 ANIMATED BACKGROUND PATTERNS

**In AE:** Venetian Blinds + Wave Warp for wavy stripes. Gradient Ramp + Turbulent Displace for organic backgrounds. Motion Tile for infinite repeating patterns.

**In Remotion:**
```tsx
// Animated stripes (equivalent to Venetian Blinds + Wave Warp)
const AnimatedStripes: React.FC = () => {
  const frame = useCurrentFrame();
  const offset = interpolate(frame, [0, 300], [0, 100]);

  return (
    <div style={{
      width: '100%', height: '100%',
      background: `repeating-linear-gradient(
        45deg,
        #1a1a2e 0px, #1a1a2e 20px,
        #16213e 20px, #16213e 40px
      )`,
      backgroundPosition: `${offset}px 0`,
    }} />
  );
};

// Animated gradient (equivalent to Gradient Ramp + Turbulent Displace)
const AnimatedGradient: React.FC = () => {
  const frame = useCurrentFrame();
  const hue1 = interpolate(frame, [0, 300], [200, 320]);
  const hue2 = interpolate(frame, [0, 300], [300, 200]);
  const angle = interpolate(frame, [0, 300], [0, 360]);

  return (
    <div style={{
      width: '100%', height: '100%',
      background: `linear-gradient(${angle}deg, hsl(${hue1},70%,50%), hsl(${hue2},70%,50%))`,
    }} />
  );
};
```

---

### 9.16 SUMMARY TABLE: AE → REMOTION

| AE Concept | Remotion Equivalent |
|---|---|
| Keyframe + Easy Ease (F9) | `interpolate()` + `Easing.bezier()` |
| Speed Graph / Influence Handles | `Easing.bezier(x1,y1,x2,y2)` parameters |
| Spring / Overshoot | `spring({config: {damping, stiffness, mass}})` |
| Text Animator + Range Selector | `.map()` over words/characters + staggered `interpolate()` |
| Stagger / Layer Offset | `<Sequence from={i * delay}>` in a loop |
| Repeater | `.map()` + index-based transform |
| Trim Paths | SVG `strokeDasharray` + `strokeDashoffset` |
| Drop Shadow | CSS `box-shadow` |
| Inner Shadow / Bevel | CSS `box-shadow: inset` |
| Noise (anti-banding) | SVG feTurbulence overlay at 0.03 opacity |
| Displacement Map | SVG `feDisplacementMap` filter |
| Wave Warp | `Math.sin()` on transform, or SVG feTurbulence |
| Alpha Matte / Track Matte | `overflow: hidden` / `clip-path` / `backgroundClip: text` |
| Stencil Alpha | Container with `overflow: hidden` + animated shape |
| RGB Split | 3 copies with offset + `mixBlendMode: screen` |
| Wiggle Expression | `Math.sin(f * freq) * amp` (sum of sinusoids) |
| Echo / Motion Trail | N copies at previous frames with decreasing opacity |
| Time Remapping | `interpolate()` with non-linear mapping |
| Motion Blur | `filter: blur()` conditional during fast movements |
| Parenting | React component nesting |
| Null Object | Wrapper div with animated transform |
| Pre-Compose | Extract into a separate React component |
| Loop Out (Cycle) | `frame % loopDuration` |
| Loop Out (Ping Pong) | Modulo + inversion in the second half |
| CC Kaleidoscope | N copies rotated by 360/N degrees |
| Venetian Blinds | Animated `repeating-linear-gradient` |
| Flicker | Opacity array + frame index |

---

## 10. RESOURCES

| Resource | URL |
|---|---|
| Remotion Docs | remotion.dev/docs |
| Remotion Fundamentals | remotion.dev/docs/the-fundamentals |
| LogRocket Guide | blog.logrocket.com/guide-remotion-studio/ |
| Video Tutorial (Tella) | youtube.com/watch?v=PrGYLd7yu1s |
| Higgsfield Vibe Motion Guide | higgsfield.ai/blog/Higgsfield-Vibe-Motion-Guide-AI-Motion-Design |
| Higgsfield Animation Tips | karavideo.ai/blog/top-tips-for-creating-stunning-animations-with-higgsfield-vibe-motion/ |
| Medium (Remotion + Claude) | medium.com/@creativeaininja (paywall) |
| Dope Motions AE Playlist (85 videos) | youtube.com/playlist?list=PLpWEtUjzDQ2PJtxONnqYMEnJ_au6H4aIK |
