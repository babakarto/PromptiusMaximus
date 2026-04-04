# Project File Structure

```
REMOTION XCITE/
├── src/
│   ├── index.ts              <- Entry point (registerRoot)
│   ├── Root.tsx               <- Composition "XciteShowreel" (1920x1080, 30fps, 600f)
│   ├── XciteShowreel.tsx      <- Main timeline with 4 Sequences
│   ├── config.ts              <- Brand colors + video constants + tagline
│   ├── styles.css             <- Tailwind CSS v4 import
│   ├── scenes/
│   │   ├── BaseScene.tsx      <- Background gradient + floating particles (reusable)
│   │   └── LogoReveal.tsx     <- SCENE 4: complete logo reveal with 8 animated phases
│   ├── components/            <- (empty) for future reusable elements
│   └── characters/            <- (empty) for future SVG characters
├── public/
│   ├── logos/                 <- All logo PNG assets
│   │   ├── x.png             <- Orange X symbol (1080x1920 PSD layer)
│   │   ├── trattino.png      <- White dash "-"
│   │   ├── cite.png          <- White "cite" text
│   │   ├── xciteventur.png   <- "X·CITE VENTURES" text
│   │   ├── play.png          <- "PLAY."
│   │   ├── CONENCT.png       <- "CONNECT." (yes, typo in filename)
│   │   ├── DOMINATE!.png     <- "DOMINATE!"
│   │   ├── omino.png         <- Dali Mascot (695x843, standalone)
│   │   ├── TOTALE.png        <- Assembled logo (reference)
│   │   ├── sfondo ffa700.png <- Gold background
│   │   └── sfondo 00000.png  <- Black background
│   ├── audio/                 <- (empty) for local voiceover/SFX
│   └── characters/dali/      <- (empty) for mascot SVG parts
├── guida/                     <- THIS FOLDER — complete documentation
├── remotion.config.ts         <- Remotion config + TailwindCSS v4
├── tsconfig.json
├── package.json
└── .agents/skills/            <- Remotion best practices skills installed
    └── remotion-best-practices/
```

## Notes on PNG assets
The logo assets (x.png, cite.png, etc.) are **PSD layers exported at 1080x1920 (portrait)**.
Each layer has a transparent background with the content positioned where it was in the PSD.
To use them in the landscape 1920x1080 video, the `Crop` component in LogoReveal.tsx:
1. Places the full image in a container with overflow:hidden
2. Offsets the image with negative left/top to show only the content bounding box
3. CRITICAL: `maxWidth: "none"` on the Img to override Tailwind preflight
