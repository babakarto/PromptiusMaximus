# Scene 4 — Logo Reveal (dettaglio tecnico)

File: `src/scenes/LogoReveal.tsx`
Durata: 150 frames (5 secondi) — frames globali 450–600

## Timeline delle 8 fasi

| Fase | Tempo | Cosa succede | Animazione |
|------|-------|-------------|------------|
| 1 | 0.0–0.7s | Linea gold orizzontale si disegna dal centro | `interpolate` + `Easing.out(quad)` |
| 2 | 0.7–1.7s | X symbol cade dall'alto | `spring(heavy)` mass:2 damping:15 stiffness:80 |
| — | 0.93s | Impatto X: screen shake 3px + burst ring gold | 16 particelle radiali |
| 3 | 1.7–2.3s | Dash fade-in + "cite" slide da destra | `spring(snappy)` damping:20 stiffness:200 |
| 4 | 2.3–3.0s | "X·CITE VENTURES" fade + scaleX expand | `Easing.out(quad)` + glow pulse |
| 5 | 3.0–3.5s | LightLeak flash WebGL (arancione) | `<LightLeak seed={7} hueShift={30}>` |
| 6 | 3.2–4.0s | PLAY. CONNECT. DOMINATE! slam uno per uno | `spring(punch)` stiffness:220 + screen shake |
| 7 | 4.0–4.7s | Mascot Dali sbuca dal basso-destra | `spring(bouncy)` damping:8 |
| 8 | 4.7–5.0s | Fade to dark + scale up 2% | `Easing.in(quad)` |

## Spring Configs (dalla skill library)
```ts
const SPRING = {
  heavy:  { damping: 15, stiffness: 80, mass: 2 },    // X drop
  snappy: { damping: 20, stiffness: 200 },             // Cite slide
  bouncy: { damping: 8 },                              // Mascot
  punch:  { damping: 18, stiffness: 220, mass: 0.8 },  // Tagline slams
};
```

## SFX inclusi
- Whoosh (`remotion.media/whoosh.wav`) sulla caduta della X
- 3x Whip (`remotion.media/whip.wav`) su ogni tagline slam

## Crop Component (importante!)
Le immagini PSD sono 1080×1920. Il componente `Crop` mostra solo il bounding box del contenuto:
- Container dimensionato al bbox × scale, `overflow: hidden`
- Immagine posizionata con offset negativi
- **`maxWidth: "none"`** obbligatorio per overridare Tailwind CSS preflight

## Bounding box degli asset (coordinate pixel nel canvas 1080×1920)
```
x.png:          (35, 807)  → 279×267
trattino.png:   (314, 931) → 88×29
cite.png:       (435, 774) → 610×274
xciteventur.png:(35, 1102) → 1010×59
play.png:       (259, 865) → 567×157
CONENCT.png:    (48, 873)  → 1010×146
DOMINATE!.png:  (54, 882)  → 975×129
omino.png:      (87, 51)   → 573×734  [canvas 695×843]
```
