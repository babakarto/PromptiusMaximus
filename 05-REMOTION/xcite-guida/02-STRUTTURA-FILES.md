# Struttura del Progetto

```
REMOTION XCITE/
├── src/
│   ├── index.ts              ← Entry point (registerRoot)
│   ├── Root.tsx               ← Composition "XciteShowreel" (1920×1080, 30fps, 600f)
│   ├── XciteShowreel.tsx      ← Timeline principale con 4 Sequence
│   ├── config.ts              ← Brand colors + video constants + tagline
│   ├── styles.css             ← Tailwind CSS v4 import
│   ├── scenes/
│   │   ├── BaseScene.tsx      ← Background gradient + floating particles (riutilizzabile)
│   │   └── LogoReveal.tsx     ← SCENE 4: logo reveal completo con 8 fasi animate
│   ├── components/            ← (vuoto) per elementi riutilizzabili futuri
│   └── characters/            ← (vuoto) per SVG character futuri
├── public/
│   ├── logos/                 ← Tutti gli asset PNG del logo
│   │   ├── x.png             ← Simbolo X arancione (1080×1920 PSD layer)
│   │   ├── trattino.png      ← Dash "-" bianco
│   │   ├── cite.png          ← Testo "cite" bianco
│   │   ├── xciteventur.png   ← Testo "X·CITE VENTURES"
│   │   ├── play.png          ← "PLAY."
│   │   ├── CONENCT.png       ← "CONNECT." (sì, typo nel filename)
│   │   ├── DOMINATE!.png     ← "DOMINATE!"
│   │   ├── omino.png         ← Mascot Dali (695×843, standalone)
│   │   ├── TOTALE.png        ← Logo assemblato (reference)
│   │   ├── sfondo ffa700.png ← Background gold
│   │   └── sfondo 00000.png  ← Background nero
│   ├── audio/                 ← (vuoto) per voiceover/SFX locali
│   └── characters/dali/      ← (vuoto) per SVG parts del mascot
├── guida/                     ← QUESTA CARTELLA — documentazione completa
├── remotion.config.ts         ← Config Remotion + TailwindCSS v4
├── tsconfig.json
├── package.json
└── .agents/skills/            ← Remotion best practices skills installate
    └── remotion-best-practices/
```

## Note sugli asset PNG
Gli asset del logo (x.png, cite.png, ecc.) sono **layer PSD esportati a 1080×1920 (portrait)**.
Ogni layer ha sfondo trasparente con il contenuto posizionato dove stava nel PSD.
Per usarli nel video landscape 1920×1080, il componente `Crop` in LogoReveal.tsx:
1. Mette l'immagine intera in un container con overflow:hidden
2. Offset l'immagine con left/top negativi per mostrare solo il content bbox
3. FONDAMENTALE: `maxWidth: "none"` sull'Img per overridare Tailwind preflight
