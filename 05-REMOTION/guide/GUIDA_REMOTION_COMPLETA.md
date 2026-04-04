# GUIDA REMOTION + HIGGSFIELD VIBE MOTION — Progetto Candy

> Compilata: 2 Aprile 2026
> Fonti: remotion.dev docs, LogRocket guide, Tella YouTube tutorial, Medium (Remotion + Claude Code), Higgsfield blog x2

---

## 1. REMOTION — FONDAMENTALI

### Cos'e' Remotion
Remotion = **React per video**. Scrivi componenti TypeScript/React che renderizzano frame per frame in MP4. Niente timeline, niente GUI — tutto e' codice.

### Concetto Base
> "Remotion ti da un numero di frame e un canvas vuoto, su cui puoi renderizzare qualsiasi cosa usando React."

- I video sono **una funzione di immagini nel tempo**
- Cambiare il contenuto ad ogni frame = animazione
- Frame numbering parte da `0`
- Frame finale = `durationInFrames - 1`
- Durata in secondi = `durationInFrames / fps`

### Proprieta' Video (obbligatorie)
| Proprieta' | Tipo | Esempio |
|---|---|---|
| `width` | pixels | 1080 |
| `height` | pixels | 1920 |
| `durationInFrames` | numero frame totali | 450 |
| `fps` | framerate | 30 |

### Hook Principali
```tsx
// Frame corrente (parte da 0)
const frame = useCurrentFrame();

// Tutte le proprieta' video
const { width, height, fps, durationInFrames } = useVideoConfig();
```

### Componenti Built-in
| Componente | Uso |
|---|---|
| `<AbsoluteFill>` | Container a tutto schermo (come un div fullscreen) |
| `<Sequence>` | Timing control — mostra un componente da un certo frame |
| `<Series>` | Playback sequenziale — uno dopo l'altro |
| `<Video>` | Incorpora video sorgente |
| `<Audio>` | Incorpora audio |
| `<Img>` | Immagine statica |

---

## 2. SETUP PROGETTO

### Installazione
```bash
npm init video
```
- Scegli template **blank**
- Aggiungi **Tailwind CSS** (si per lo styling)
- Aggiungi **agent skills** per Claude Code

### Struttura Progetto
```
my-video/
├── src/
│   ├── Root.tsx          # Registra tutte le Composition
│   ├── index.ts          # Entry point
│   └── components/       # I tuoi componenti video
├── public/               # Assets (immagini, video, font)
├── package.json
└── remotion.config.ts
```

### Avviare Remotion Studio
```bash
cd my-video
npm run dev
```
Apre Remotion in Chrome:
- **Pannello sinistro:** lista composizioni
- **Pannello destro:** props editabili in real-time
- **Tab Renders:** generazione file video

---

## 3. COMPOSIZIONI

### Registrare una Composizione
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

### Composizione con Zod Schema (props tipizzati e editabili in UI)
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

Registra con schema:
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

## 4. ANIMAZIONI

### REGOLA FONDAMENTALE
> **Anima SEMPRE usando `useCurrentFrame()`** — mai CSS transitions o animazioni browser. Causano flickering durante il render.

### Animazione Base con Frame
```tsx
const frame = useCurrentFrame();

// Fade in nei primi 30 frame
const opacity = Math.min(1, frame / 30);

// Slide da sinistra
const translateX = Math.max(0, 100 - frame * 5);

// Scala da 0 a 1
const scale = Math.min(1, frame / 20);
```

### interpolate() — Mappatura valori

Mappa un range di valori su un altro. 4 argomenti: valore input, range input, range output, opzioni.

```tsx
import { interpolate } from "remotion";

// Fade in dal frame 0 al 60
const opacity = interpolate(frame, [0, 60], [0, 1], {
  extrapolateRight: "clamp",
});

// Slide + hold — entra dal frame 0 al 20, poi fermo
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

**Opzioni extrapolation** (cosa succede fuori dal range):
| Opzione | Effetto |
|---|---|
| `"extend"` (default) | Continua oltre il range |
| `"clamp"` | Si ferma al valore limite — **USARE QUASI SEMPRE** |
| `"wrap"` | Loop ciclico |
| `"identity"` | Ritorna il valore input originale |

Puoi settare `extrapolateLeft` e `extrapolateRight` separatamente.

**Easing** — curva di interpolazione (default = lineare):
```tsx
import { Easing } from "remotion";

const opacity = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.25, 0.1, 0.25, 1), // ease standard
  extrapolateRight: "clamp",
});
```

### spring() — Animazione fisica naturale

Anima da 0 a 1 con fisica reale (rimbalzo, overshoot).

```tsx
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const scale = spring({
  frame,
  fps,
  config: {
    mass: 1,        // peso (basso = veloce)
    stiffness: 100,  // rimbalzo (alto = piu' bouncy)
    damping: 10,     // freno (alto = meno rimbalzo)
    overshootClamping: false, // true = mai oltre il target
  },
});
```

**Parametri spring:**
| Parametro | Default | Effetto |
|---|---|---|
| `frame` | required | Frame corrente |
| `fps` | required | FPS dal video config |
| `from` | 0 | Valore iniziale |
| `to` | 1 | Valore finale |
| `reverse` | false | Inverte l'animazione |
| `delay` | 0 | Frame di ritardo prima di partire |
| `durationInFrames` | auto | Forza durata esatta |
| `config.mass` | 1 | Peso — basso = veloce |
| `config.damping` | 10 | Freno — alto = meno bounce |
| `config.stiffness` | 100 | Rigidita' — alto = piu' bouncy |
| `config.overshootClamping` | false | Blocca overshoot |

**Combinare spring + interpolate:**
```tsx
// Spring da 0 a 1, poi mappa su marginLeft da 0 a 200px
const springValue = spring({ frame, fps });
const marginLeft = interpolate(springValue, [0, 1], [0, 200]);
```

**Ordine applicazione:** duration → reverse → delay

### Sequence (timing dei componenti)

Controlla QUANDO un componente appare e per QUANTO.

```tsx
import { Sequence } from "remotion";

// Titolo appare al frame 0, dura 60 frame
<Sequence from={0} durationInFrames={60}>
  <Title text="Hello" />
</Sequence>

// Sottotitolo appare al frame 30, dura 90 frame
<Sequence from={30} durationInFrames={90}>
  <Subtitle text="World" />
</Sequence>
```

**Props Sequence:**
| Prop | Uso |
|---|---|
| `from` | Frame di inizio (default 0) |
| `durationInFrames` | Durata in frame (default Infinity) |
| `name` | Nome nel timeline di Studio |
| `layout` | `"absolute-fill"` (default) o `"none"` |
| `style` | CSS styles |

**Tricks:**
- **Delay:** `<Sequence from={30}>` — appare dopo 30 frame
- **Trim inizio:** `<Sequence from={-15}>` — salta i primi 15 frame del contenuto
- **Nesting:** Sequence dentro Sequence = i from si sommano (30 + 60 = 90)
- I figli che chiamano `useCurrentFrame()` ricevono il frame **relativo** alla Sequence (partono da 0)

### Img — Immagini

```tsx
import { AbsoluteFill, Img, staticFile } from "remotion";

// Da public/
<Img src={staticFile("hi.png")} />

// Da URL remoto
<Img src="https://example.com/image.jpg" />
```
- Remotion aspetta che l'immagine carichi prima di renderizzare il frame (no flicker)
- `maxRetries` default 2 con exponential backoff
- NON usare per GIF — usa `@remotion/gif`

### Video — Incorporare video

```tsx
import { AbsoluteFill, OffthreadVideo, staticFile } from "remotion";

// OffthreadVideo = migliore performance (estrae frame con FFmpeg)
<OffthreadVideo src={staticFile("video.mp4")} />

// Trim
<OffthreadVideo src={staticFile("video.mp4")} trimBefore={60} />

// Velocita'
<OffthreadVideo src={staticFile("video.mp4")} playbackRate={0.5} />

// Muto
<OffthreadVideo src={staticFile("video.mp4")} muted />
```

**OffthreadVideo vs Html5Video:**
| | OffthreadVideo | Html5Video |
|---|---|---|
| Performance | Migliore (FFmpeg) | Browser-based |
| Rendering | Frame estratti come immagini | Video tag nativo |
| Trasparenza | `transparent={true}` | No |
| Client-side | NO | SI |
| Consigliato per | Render finale | Preview in Studio |

### fitText() — Testo che si adatta

```tsx
import { fitText } from "@remotion/layout-utils";

const { fontSize } = fitText({
  text: "Hello World",
  withinWidth: 600,
  fontFamily: "Arial",
  fontWeight: "bold",
});

// Usa in style
<div style={{ fontSize }}>Hello World</div>
```
- Il font DEVE essere caricato prima di chiamare `fitText()`
- Usa `outline` invece di `border` (border rimpicciolisce il container per box-sizing)

---

## 5. RENDERING

### Da Remotion Studio
1. Click **Render video** nel tab Renders
2. Configura output (qualita', formato)
3. Click **Render video** per generare MP4
4. FFmpeg e' gia' embedded — nessuna installazione separata

### Da CLI
```bash
# Render MP4
npx remotion render src/index.ts MyComposition out/video.mp4

# Render PNG sequence (per compositing in Premiere/ffmpeg)
npx remotion render src/index.ts MyComposition --sequence --image-format=png out/frames

# Render ProRes (massima qualita')
npx remotion render src/index.ts MyComposition --codec=prores --prores-profile=4444 out/video.mov
```

### Compositing PNG + Video con ffmpeg
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

## 6. WORKFLOW CON CLAUDE CODE

### Come Funziona
1. **Trova ispirazione** — Pinterest, screenshot da YouTube, immagini statiche
2. **Dai l'immagine a Claude** — drag & drop nel terminale
3. **Prompt semplice** — "animate this", "recreate this as a motion graphic"
4. **Claude scrive il codice** — crea il componente React + lo registra
5. **Preview in Remotion Studio** — vedi il risultato in tempo reale in Chrome
6. **Itera** — "make the font smaller", "change colors", "make it horizontal"
7. **Render** — esporta in MP4 o ProRes

### Tips dal Video Tutorial (Tella)
- **Inizia semplice** — non complicare il primo prompt
- **Dai prima solo l'immagine** — lascia che Claude interpreti, poi correggi
- **Le frecce sono difficili** — evitale inizialmente
- **Puoi dare dati Excel** — Claude li trasforma in grafici animati
- **Per video di ispirazione** — usa ffmpeg per analizzare frame per frame:
  ```
  "Use ffmpeg to analyze [file] and create a similar animation where words come in one by one"
  ```
- **Ogni composizione** appare automaticamente nel pannello sinistro di Remotion Studio
- **Render ProRes** per massima qualita' quando esporti

### Prompt Efficaci per Claude + Remotion
```
# Da immagine statica
"Animate this diagram as a Remotion composition. Make the bars grow from bottom to top."

# Da screenshot video
"Use ffmpeg to analyze this video and recreate the animation where text appears word by word."

# Modifica
"Make the diagram horizontal and make sure the center font isn't yellow."

# Dati custom
"Make this an upward graph showing newsletter subscriber growth to 12,500 subscribers."
```

---

## 7. HIGGSFIELD VIBE MOTION

### Cos'e'
AI motion design tramite chat — crei motion graphics, presentazioni, e visual con interfaccia conversazionale invece di timeline editor.

### Workflow
1. **Concept** — descrivi l'idea a parole ("Create a kinetic typography intro")
2. **Assets** — carica immagini, video, loghi, PDF
3. **Template** (opzionale) — scegli un template con logica di motion gia' pronta
4. **Refine in UI** — aggiusta font, colori, velocita' animazione manualmente
5. **Iterate** — cambiamenti si vedono in tempo reale

### Casi d'Uso
- **Infografiche animate** — numeri che crescono, sezioni che appaiono in sequenza
- **Presentazioni** — investor deck, sales, product walkthrough
- **Logo/Brand animations** — animazioni riutilizzabili da loghi caricati

### Tips per Animazioni Migliori

**Sketch e Input**
- Disegni semplici con contorni chiari
- Evita sfondi disordinati o scene affollate
- Un'azione principale per frame

**Easing Styles**
| Tipo | Quando usarlo |
|---|---|
| Linear | Robot, macchine, tech |
| Ease In | Inizio movimento personaggio |
| Ease Out | Stop dolci |
| Ease In-Out | Movimento naturale e dinamico |

**Keyframe Spacing**
- Keyframe vicini = movimento veloce
- Keyframe distanti = movimento lento

**Effetti Cinematici**
- Motion blur: minimo per scene lente, forte per azione veloce
- Depth of field: focus sul soggetto, blur sullo sfondo
- Dettagli sottili: rimbalzo capelli, flutter vestiti, blink

**Prompt Engineering per Higgsfield**
- Descrizioni dettagliate = risultati migliori
- Usa **negative prompts**: "no blur, no noise, no extra limbs"
- Evita richieste impossibili ("square shaped sphere")

**Quality Check Pre-Export**
- Risoluzione minima 1024x1024
- Preview frame per frame
- Verifica motion blur e depth of field
- Scegli formato giusto (MP4 per video, GIF per loop)

---

## 8. LEZIONI DAL PROGETTO ARDOINO (Remotion)

Dal progetto precedente nella cartella `ardoino/remotion-news/`:

### Setup che Funzionava
- Remotion 4.0.267 + React 19 + TypeScript 5.7
- 1280x720, 30000/1001 fps (29.97 NTSC)
- Video sorgente in `public/`

### Pattern Overlay Trasparente
Due composizioni:
| ID | Uso |
|---|---|
| `NewsVideo` | Video + overlay (export completo) |
| `OverlayOnly` | Solo testo su trasparente (per compositing in Premiere/ffmpeg) |

### Typewriter Effect
- Font monospace terminale
- Velocita' variabile (1-2 chars/frame)
- Cursore `▌` lampeggiante (15 frame on/off)
- Linee precedenti si rimpiccioliscono con opacity fade
- Glow bianco sottile via text-shadow

### Export Definitivo (NO render diretto, SI PNG sequence)
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

### Errori da Evitare
1. **Mai `fps={29.97}`** → usare `fps={30000/1001}` per evitare frame drift
2. **ProRes 4444 + glow = blob bianchi** → il canale alpha premoltiplicato rende i text-shadow opachi
3. **PNG sequence + ffmpeg >> Remotion render diretto** → zero stutter
4. **`yuvj420p` causa problemi in Premiere** → forzare `-pix_fmt yuv420p`
5. **CRF 16** per YouTube, **CRF 20** per Twitter

---

## 9. MOTION DESIGN — PRINCIPI DA AFTER EFFECTS APPLICATI A REMOTION

> Fonte: playlist "Motion Graphics Tutorials in After Effects" di Dope Motions (85 video)
> Ogni concetto AE e' mappato al suo equivalente Remotion

---

### 9.1 EASING E SPEED GRAPH (Timing vs Spacing)

**In AE:** Il Speed Graph controlla l'accelerazione/decelerazione. "Timing" = QUANDO succedono le cose (distanza tra keyframe). "Spacing" = COME si muovono (la curva tra i keyframe). Ease High/Ease Low controllano la rampa di accelerazione.

**In Remotion:**
```tsx
import { Easing, interpolate } from 'remotion';

// Ease-in-out morbido (equivalente di F9 in AE)
const value = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.42, 0, 0.58, 1),
});

// Ease-out forte (equivalente di drag handle a sinistra in AE)
const value = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0, 0.55, 0.45, 1),
});

// Ease-in forte + ease-out leggero (Ease High=80, Ease Low=15)
const value = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.7, 0, 0.3, 1),
});

// Bounce / overshoot con spring()
const scale = spring({ frame, fps, config: {
  mass: 0.5, damping: 8, stiffness: 150, overshootClamping: false
}});
```

**Regola chiave:** Mai usare animazioni lineari. Tutto deve avere una curva di easing.

---

### 9.2 TEXT ANIMATOR (Posizione + Opacita' + Blur)

**In AE:** Text Animator con Position, Opacity, Blur + Range Selector con shape "Ramp Up" + Based On "Words/Characters". Crea rivelazioni testo parola per parola o carattere per carattere con blur in entrata.

**In Remotion:**
```tsx
const TextReveal: React.FC<{text: string; startFrame: number}> = ({text, startFrame}) => {
  const frame = useCurrentFrame();
  const words = text.split(' ');
  const staggerDelay = 4; // frame tra ogni parola

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

**Varianti:**
- `Based On Characters`: cambia `text.split(' ')` con `text.split('')` e riduci `staggerDelay` a 1-2
- `Randomize Order`: aggiungi un array di indici shufflati per l'ordine di apparizione
- `Ramp Up / Ramp Down`: controlla la direzione della rivelazione (sinistra→destra vs destra→sinistra)

---

### 9.3 STAGGER / DISPLACEMENT DI LAYER

**In AE:** Spostare layer di 10-15 frame l'uno dall'altro per creare animazioni a cascata. Principio fondamentale del motion design — mai animare tutto insieme.

**In Remotion:**
```tsx
// Stagger semplice: ogni elemento parte N frame dopo il precedente
const elements = ['Titolo', 'Sottotitolo', 'CTA'];
const staggerOffset = 10; // frame tra ogni elemento

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

**Regola chiave:** Lo stagger ideale e' 8-15 frame a 30fps. Troppo poco = sembra simultaneo. Troppo = sembra lento.

---

### 9.4 REPEATER (Pattern Procedurali)

**In AE:** Il Repeater duplica e trasforma elementi proceduralmente. Due repeater annidati creano griglie. Combinato con Trim Path crea pattern complessi da un singolo shape layer.

**In Remotion:**
```tsx
// Griglia procedurale con doppio repeater
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

**Tip:** Per pattern rotanti simmetrici (stile CC Kaleidoscope), duplica e ruota lo stesso componente N volte:
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

### 9.5 TRIM PATH (Animazione Stroke SVG)

**In AE:** Trim Paths anima l'inizio/fine di uno stroke. Usatissimo per line art, loghi, e decorazioni.

**In Remotion:**
```tsx
const AnimatedStroke: React.FC = () => {
  const frame = useCurrentFrame();
  const pathLength = 500; // lunghezza totale del path
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

**Per offset animato** (equivalente dell'Offset property in Trim Paths):
```tsx
const offset = interpolate(frame, [0, 150], [0, pathLength]);
// strokeDashoffset={pathLength * (1 - progress) + offset}
```

---

### 9.6 DROP SHADOW CON NOISE (Anti-Banding)

**In AE:** Aggiungere 2-5% di noise alla drop shadow previene il color banding nei render. Le ombre danno profondita' e separazione tra elementi.

**In Remotion:**
```tsx
// Drop shadow CSS + noise overlay per anti-banding
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

**Inner Shadow** (effetto cut-out / intaglio):
```tsx
<div style={{
  boxShadow: 'inset 0 4px 30px rgba(0,0,0,0.5)',
  borderRadius: 20,
}}>
```

---

### 9.7 DISPLACEMENT MAP / WAVE WARP

**In AE:** Displacement Map distorce l'immagine basandosi su una mappa. Wave Warp aggiunge ondulazioni. Turbulent Displace crea distorsioni organiche.

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

**Wave effect semplice senza SVG:**
```tsx
// Ondulazione via transform
const wave = Math.sin(frame * 0.1) * 10;
<div style={{transform: `translateY(${wave}px) skewX(${wave * 0.5}deg)`}}>
```

---

### 9.8 ALPHA MATTE / TRACK MATTE (Masking)

**In AE:** Track Matte Alpha usa la trasparenza di un layer per mascherare un altro. Usato ovunque: testo che rivela immagini, shape reveal, parallax con mask.

**In Remotion:**
```tsx
// Immagine rivelata attraverso testo (come Alpha Matte)
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

// Shape reveal con overflow hidden (Stencil Alpha)
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

// Clip-path reveal (piu' flessibile)
const clipProgress = interpolate(frame, [0, 30], [0, 100], {
  extrapolateRight: 'clamp',
});
<div style={{clipPath: `inset(0 ${100 - clipProgress}% 0 0)`}}>
```

---

### 9.9 RGB SPLIT + WIGGLE (Glitch)

**In AE:** Duplicare il layer 3 volte, isolare R/G/B per canale, blend mode Screen, aggiungere wiggle expression per movimento casuale. Optics Compensation per distorsione lente.

**In Remotion:**
```tsx
const RGBGlitch: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  // Wiggle: sin con frequenze diverse per casualita'
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

**In AE:** L'effetto Echo crea scie di movimento duplicando frame precedenti con opacita' decrescente. Combinato con motion blur crea trails cinematici.

**In Remotion:**
```tsx
// Motion trail: renderizza N copie a posizioni precedenti
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

**In AE:** Parenting collega layer a un parent — muovi il parent, si muovono tutti i figli. Null Object e' un controller invisibile per animare gruppi.

**In Remotion:** E' nativo — i componenti React sono gia' annidati. Un div wrapper con transform animato muove tutti i figli:
```tsx
const GroupController: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const y = interpolate(frame, [60, 90], [0, -500], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    easing: Easing.bezier(0.65, 0, 0.35, 1),
  });

  return (
    <div style={{transform: `translateY(${y}px)`}}>
      {children}  {/* Tutto si muove insieme */}
    </div>
  );
};
```

---

### 9.12 TIME REMAPPING / SPEED RAMP

**In AE:** Time Remapping permette di accelerare/rallentare il video in punti specifici. La curva dello Speed Graph controlla la transizione tra velocita'.

**In Remotion:**
```tsx
// Speed ramp su video: playbackRate variabile
// Nota: OffthreadVideo accetta playbackRate fisso, non variabile.
// Per speed ramp complessi, usa interpolate per mappare frame non-lineari:

const timeRemap = interpolate(frame, [0, 30, 45, 90], [0, 30, 60, 90], {
  // 0-30: velocita' normale (1x)
  // 30-45: velocita' doppia (compressi 30 frame in 15)
  // 45-90: velocita' normale di nuovo
});

// Usa timeRemap come frame "remappato" per qualsiasi animazione
const position = interpolate(timeRemap, [0, 90], [0, 1000]);
```

---

### 9.13 LOOP EXPRESSIONS

**In AE:** `loopOut("cycle")` ripete i keyframe all'infinito. `loopOut("pingpong")` li ripete avanti-indietro.

**In Remotion:**
```tsx
// Loop cycle: usa modulo
const loopDuration = 60; // frame
const loopFrame = frame % loopDuration;
const value = interpolate(loopFrame, [0, 30, 60], [0, 100, 0]);

// Loop pingpong
const pingPongFrame = (() => {
  const cycle = frame % (loopDuration * 2);
  return cycle < loopDuration ? cycle : loopDuration * 2 - cycle;
})();

// Wiggle continuo (equivalente di wiggle(freq, amp))
const wiggle = (f: number, freq: number, amp: number) =>
  Math.sin(f * freq * 0.1) * amp +
  Math.sin(f * freq * 0.23 + 1.5) * amp * 0.5 +
  Math.cos(f * freq * 0.37 + 3.0) * amp * 0.25;
```

---

### 9.14 FLICKER REVEAL

**In AE:** Alternare rapidamente opacity tra 0% e 100% su 2 frame ciascuno per creare un effetto "flicker" cinematico di rivelazione.

**In Remotion:**
```tsx
const FlickerReveal: React.FC<{children: React.ReactNode; startFrame: number}> = ({
  children, startFrame
}) => {
  const frame = useCurrentFrame();
  const localFrame = frame - startFrame;

  // Pattern flicker: [on, off, on, off, on, on, on...]
  const flickerPattern = [0, 1, 0.5, 0.1, 0.8, 0.3, 1, 0.1, 0.5, 1, 1, 1, 1];
  const flickerIndex = Math.min(localFrame, flickerPattern.length - 1);
  const opacity = localFrame < 0 ? 0 :
    localFrame >= flickerPattern.length ? 1 :
    flickerPattern[Math.floor(flickerIndex)];

  return <div style={{opacity}}>{children}</div>;
};
```

---

### 9.15 BACKGROUND PATTERNS ANIMATI

**In AE:** Venetian Blinds + Wave Warp per strisce ondulate. Gradient Ramp + Turbulent Displace per sfondi organici. Motion Tile per pattern ripetuti infiniti.

**In Remotion:**
```tsx
// Strisce animate (equivalente Venetian Blinds + Wave Warp)
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

// Gradiente animato (equivalente Gradient Ramp + Turbulent Displace)
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

### 9.16 TABELLA RIASSUNTIVA: AE → REMOTION

| Concetto AE | Equivalente Remotion |
|---|---|
| Keyframe + Easy Ease (F9) | `interpolate()` + `Easing.bezier()` |
| Speed Graph / Influence Handles | Parametri di `Easing.bezier(x1,y1,x2,y2)` |
| Spring / Overshoot | `spring({config: {damping, stiffness, mass}})` |
| Text Animator + Range Selector | `.map()` su parole/caratteri + `interpolate()` staggerato |
| Stagger / Layer Offset | `<Sequence from={i * delay}>` in un loop |
| Repeater | `.map()` + transform basato su index |
| Trim Paths | SVG `strokeDasharray` + `strokeDashoffset` |
| Drop Shadow | CSS `box-shadow` |
| Inner Shadow / Bevel | CSS `box-shadow: inset` |
| Noise (anti-banding) | SVG feTurbulence overlay a opacity 0.03 |
| Displacement Map | SVG `feDisplacementMap` filter |
| Wave Warp | `Math.sin()` su transform, o SVG feTurbulence |
| Alpha Matte / Track Matte | `overflow: hidden` / `clip-path` / `backgroundClip: text` |
| Stencil Alpha | Container con `overflow: hidden` + shape animata |
| RGB Split | 3 copie con offset + `mixBlendMode: screen` |
| Wiggle Expression | `Math.sin(f * freq) * amp` (somma di sinusoidi) |
| Echo / Motion Trail | N copie a frame precedenti con opacity decrescente |
| Time Remapping | `interpolate()` con mapping non-lineare |
| Motion Blur | `filter: blur()` condizionale durante movimenti rapidi |
| Parenting | Nesting di componenti React |
| Null Object | Div wrapper con transform animato |
| Pre-Compose | Estrarre in componente React separato |
| Loop Out (Cycle) | `frame % loopDuration` |
| Loop Out (Ping Pong) | Modulo + inversione nella seconda meta' |
| CC Kaleidoscope | N copie ruotate di 360/N gradi |
| Venetian Blinds | `repeating-linear-gradient` animato |
| Flicker | Array di opacity + frame index |

---

## 10. RISORSE

| Risorsa | URL |
|---|---|
| Remotion Docs | remotion.dev/docs |
| Remotion Fundamentals | remotion.dev/docs/the-fundamentals |
| LogRocket Guide | blog.logrocket.com/guide-remotion-studio/ |
| Tutorial Video (Tella) | youtube.com/watch?v=PrGYLd7yu1s |
| Higgsfield Vibe Motion Guide | higgsfield.ai/blog/Higgsfield-Vibe-Motion-Guide-AI-Motion-Design |
| Higgsfield Animation Tips | karavideo.ai/blog/top-tips-for-creating-stunning-animations-with-higgsfield-vibe-motion/ |
| Medium (Remotion + Claude) | medium.com/@creativeaininja (paywall) |
| Dope Motions AE Playlist (85 video) | youtube.com/playlist?list=PLpWEtUjzDQ2PJtxONnqYMEnJ_au6H4aIK |
