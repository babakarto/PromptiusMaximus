# Scene 4 — Logo Reveal (technical detail)

File: `src/scenes/LogoReveal.tsx`
Duration: 150 frames (5 seconds) — global frames 450-600

## Timeline of the 8 phases

| Phase | Time | What happens | Animation |
|-------|------|-------------|-----------|
| 1 | 0.0-0.7s | Gold horizontal line draws from center | `interpolate` + `Easing.out(quad)` |
| 2 | 0.7-1.7s | X symbol drops from above | `spring(heavy)` mass:2 damping:15 stiffness:80 |
| — | 0.93s | X impact: screen shake 3px + gold burst ring | 16 radial particles |
| 3 | 1.7-2.3s | Dash fade-in + "cite" slides from right | `spring(snappy)` damping:20 stiffness:200 |
| 4 | 2.3-3.0s | "X·CITE VENTURES" fade + scaleX expand | `Easing.out(quad)` + glow pulse |
| 5 | 3.0-3.5s | LightLeak flash WebGL (orange) | `<LightLeak seed={7} hueShift={30}>` |
| 6 | 3.2-4.0s | PLAY. CONNECT. DOMINATE! slam one by one | `spring(punch)` stiffness:220 + screen shake |
| 7 | 4.0-4.7s | Dali mascot pops up from bottom-right | `spring(bouncy)` damping:8 |
| 8 | 4.7-5.0s | Fade to dark + scale up 2% | `Easing.in(quad)` |

## Spring Configs (from the skill library)
```ts
const SPRING = {
  heavy:  { damping: 15, stiffness: 80, mass: 2 },    // X drop
  snappy: { damping: 20, stiffness: 200 },             // Cite slide
  bouncy: { damping: 8 },                              // Mascot
  punch:  { damping: 18, stiffness: 220, mass: 0.8 },  // Tagline slams
};
```

## Included SFX
- Whoosh (`remotion.media/whoosh.wav`) on the X drop
- 3x Whip (`remotion.media/whip.wav`) on each tagline slam

## Crop Component (important!)
The PSD images are 1080x1920. The `Crop` component shows only the content bounding box:
- Container sized to bbox x scale, `overflow: hidden`
- Image positioned with negative offsets
- **`maxWidth: "none"`** required to override Tailwind CSS preflight

## Asset bounding boxes (pixel coordinates in the 1080x1920 canvas)
```
x.png:          (35, 807)  -> 279x267
trattino.png:   (314, 931) -> 88x29
cite.png:       (435, 774) -> 610x274
xciteventur.png:(35, 1102) -> 1010x59
play.png:       (259, 865) -> 567x157
CONENCT.png:    (48, 873)  -> 1010x146
DOMINATE!.png:  (54, 882)  -> 975x129
omino.png:      (87, 51)   -> 573x734  [canvas 695x843]
```
