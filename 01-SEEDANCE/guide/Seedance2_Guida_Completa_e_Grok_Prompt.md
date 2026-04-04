# Seedance 2.0 - Guida Completa Prompt Engineering + Prompt Grok.com

Ricerca approfondita su fonti verificate: sito ufficiale ByteDance, risorse ufficiali Dreamina/CapCut, guide con prompt testati da creator, GitHub curati, Reddit e showcase YouTube reali.

---

## Cos'e Seedance 2.0

Seedance 2.0 e il modello video AI multimodale di ByteDance (2026), integrato principalmente su **Dreamina** (dreamina.capcut.com) e **CapCut**. Supporta testo + fino a 9 immagini + 3 video + 3 audio (totale max 12 file, video/audio ≤15s). E fortissimo su coerenza personaggio, fisica realistica, movimenti di camera cinematici e audio sincronizzato. I prompt funzionano esattamente uguali su tutte le piattaforme che usano il modello (Dreamina e la piu diretta e affidabile).

---

## 1. Struttura Prompt Ideale (Formula Magica)

Tutte le guide testate convergono su questo ordine preciso (riduce drift e massimizza controllo):

```
[@Riferimenti] + Soggetto + Azione + Scena/Ambiente + Camera + Illuminazione + Stile + Audio/Qualita + Constraints
```

### Template Copy-Paste Pronto (WaveSpeed + ImagineArt + Dreamina official)

```
@image1 come personaggio principale / @video1 per movimento camera
[Descrizione soggetto chiaro, una persona/oggetto]
[Verbo azione al presente, specifica e singola]
[Ambiente + atmosfera]
[Camera: shot size + movimento + angolo + lente]
[Lighting + color grading]
[Stile visivo: un solo anchor forte (es. "cinematografia Blade Runner", "National Geographic", "Zara campaign")]
[4K ultra HD, dettagli ricchi, nitidezza cinematografica, motion stabile]
[Constraints / negative]
```

**Lunghezza ideale su Dreamina:** 30-100 parole. Troppo corto = vago. Troppo lungo = perde focus e qualita cala.

---

## 2. Trick e Modi di Scrittura (I Piu Potenti, Testati)

### Regole Base
- **Inizia sempre col soggetto** (lead with the subject) → l'AI focalizza subito su quello che conta
- **Un verbo d'azione per shot** → evita caos

### Camera Vocabulary Preciso (Oro su Seedance)

| Categoria | Opzioni |
|-----------|---------|
| **Shot** | wide / medium / close-up / extreme close-up |
| **Movimento** | slow dolly-in, tracking shot, push-in, crane up, handheld (per UGC), gimbal-smooth, drone ascending, whip-pan (solo se vuoi effetto dinamico) |
| **Angolo + lente** | eye-level normal lens, low-angle telephoto, high-angle wide |

### Timeline per Multi-Shot (Perfetto per Storie)

```
[00-05s] Shot 1: ...
[05-10s] Shot 2: ...
```

### @Riferimenti (La Feature Piu Potente)

- `@image1` come personaggio principale o `@image1 as main character reference`
- `@video1` per movimento camera o `@video1's camera movement`
- `@image2` come primo frame, `@image3` come ultimo frame
- Puoi descrivere in linguaggio naturale: "Usa @image1 come ragazza con capelli corti e @video1 per il movimento fluido del vestito"
- **Per coerenza massima:** carica sempre la stessa foto del personaggio in ogni generazione

### Quality Suffix Finale (Aggiungilo Sempre)

```
4K Ultra HD, rich details, sharp clarity, cinematic texture, stable picture, no distortion, maintain face and clothing consistency
```

### Negative Prompts / Constraints (Usa 3-5 max, Mettili alla Fine)

```
No jitter, no shake, no wobble, no warping, no elastic deformation
No extra fingers, no deformed hands, no extra characters
No text overlays, no logos, no watermarks, no captions
No snap zooms, no whip pans, no Dutch angles, no jump cuts
No temporal flicker, no blurry motion
No cartoon/anime (se vuoi realistico)
```

### Trucco Pro
Cambia una sola variabile tra una generazione e l'altra (solo lighting, solo camera, solo stile). Evita di riscrivere tutto.

### Best Practice Dreamina Specifiche (Da Test Reali)
- Clip migliori sotto i **10-12 secondi** (qualita cala dopo)
- Usa sempre riferimenti immagine/video per coerenza
- Per viral: **primi 3 secondi fortissimi** (hook visivo)

---

## 3. Esempi Prompt Testati e Pronti

Selezionati da guide ufficiali/testate, gia ottimizzati per Dreamina/Seedance 2.0.

### Cinematic / Narrative (AtlasCloud + ImagineArt)

#### 1. Epic Drone Reveal (9/10 successo)

```
Sweeping drone shot ascending from a misty valley floor, slowly revealing a vast mountain range at sunrise, golden light breaking through clouds, long shadows on pine forests, orchestral grandeur, National Geographic documentary quality, ultra-smooth camera movement. 4K, stable, cinematic texture.
```

> Perche funziona: tensione + reveal + anchor forte.

#### 2. Emozionale Close-Up (Blade Runner style)

```
Extreme close-up of a young woman's face, eyes slowly opening to reveal reflected city lights, single tear rolling down cheek catching light, shallow depth of field bokeh, intimate emotional, Blade Runner cinematography, warm amber and cool blue contrast. Slow push-in.
```

### Action / Combat

#### 3. Martial Arts Slow-Motion (Crouching Tiger style)

```
A martial artist performing a spinning kick in slow motion, silk ribbons trailing from wrists creating spiral patterns, ancient temple courtyard with cherry blossom petals falling, dramatic side-angle tracking shot, Crouching Tiger Hidden Dragon aesthetic, golden hour backlighting silhouette.
```

### Product / Commercial (Super Stabili)

#### 4. Wristwatch Luxury

```
Premium wristwatch floating mid-air slowly rotating, water droplets suspended around it like diamonds catching light, pure black background, single dramatic spotlight from above, extreme macro detail, high-end jewelry commercial, ultra-smooth rotation.
```

#### 5. Iced Coffee Pour (Ipnotico)

```
Tall glass of iced coffee being poured in slow motion, rich dark coffee meeting swirling cream creating mesmerizing patterns, ice cubes clinking, condensation droplets, close-up to medium shot, warm cafe lighting, Starbucks commercial quality.
```

### Viral / Social (Dreamina Official)

#### 6. Cat Meme Chaos

```
Fast-paced video of a cat knocking over objects with exaggerated reactions, meme-style captions, quick zooms for comedic effect.
```

### Multi-Shot con Riferimenti (Esempio Avanzato)

#### 7. Cyberpunk Assassin Chase

```
Use @image1 as main character. @video1 as camera movement reference. A lone cyberpunk assassin sprints through rain-soaked neon streets at night, police drones and headlights blurring past, quick cuts between close-up determined eyes, boots splashing puddles, wide shots of traffic. Handheld camera with aggressive push-ins, intense motion blur, dramatic contrast, final slow-motion leap off rooftop. 4K, stable, no distortion.
```

---

## 4. Risorse Verificate

- Sito ufficiale ByteDance Seedance 2.0
- Dreamina official prompt guide & tips
- Guide testate: ImagineArt (70 prompt), AtlasCloud (15 best, con % successo), WaveSpeed (template + negatives)
- GitHub awesome-seedance-2-prompts (500+ curati)

---

---

# Prompt per Simulare una Ricerca Grok.com

## Prompt Principale (Ottimizzato per Coerenza UI e Dinamismo)

### Settings
- **Mode:** Omni Reference
- **AR:** 16:9
- **Duration:** 15s
- **1 reference Image** (screenshot reale di grok.com)

### Prompt

```
@image1 come riferimento esatto dell'interfaccia grok.com (screenshot della homepage o chat pulita)

Realistic live screen recording of the official grok.com interface by xAI, dark minimalist cyber UI, clean white text on deep black background, xAI logo top left, subtle blue neon glow accents, modern sidebar with Grok avatar.

A user cursor types the query "ricerca approfondita su prompt Seedance 2.0" into the central input box with smooth typing animation. Grok responds in real-time: thinking animation with visible tool icons (web_search, x_keyword_search, browse_page) lighting up one by one. Step-by-step reasoning appears line by line in the chat ("Sto usando web_search...", "Analizzando risultati verificati...", "Citazioni inline...").

Results populate dynamically: cards with titles, summaries, inline citations [web:1], [post:3], scrolling smoothly. Grok structures the answer with bullet points, tables and bold highlights. Mouse cursor moves naturally, clicking on results and expanding details.

Slow cinematic push-in from full screen to focused chat window, subtle screen reflections and soft parallax on UI elements, futuristic yet clean digital aesthetic exactly like grok.com 2026. 4K ultra HD, razor sharp text, zero jitter, zero distortion, stable motion, cinematic screen capture style, rich UI textures, perfect consistency of interface elements.
```

### Perche Funziona su Seedance 2.0

- **@image1** → carica uno screenshot reale di grok.com per avere l'interfaccia perfettamente identica (coerenza 95%+)
- **Inizia col soggetto** (l'interfaccia) → l'AI non si distrae
- **Azione singola e chiara** (typing → tool activation → risultati) → Seedance ama verbi precisi
- **Camera + movimento fluido** → evita il "video statico noioso"
- **Quality suffix finale** → elimina jitter e warping tipici dei video UI

---

## Varianti Rapide

### Versione Cinematografica / "Hacker Style"

Aggiungi dopo il prompt base:

```
... dramatic volumetric lighting from screen, subtle matrix rain in background, cyberpunk neon blue and purple accents, slow dramatic zoom on the reasoning text while tools activate.
```

### Versione Timelapse Ultra-Veloce (Per Video Virali 8-10 secondi)

```
... fast-forward timelapse style, 3x speed, query typed instantly, tools flash rapidly, full research completed in 8 seconds, smooth speed-ramping at the end.
```

### Versione con Grok "Personaggio" (Avatar Animato)

```
... Grok AI mascot (cute robot with xAI style) appears on the left of the chat, nodding and gesturing while tools activate and results appear.
```

---

## Note

- Per cambiare argomento di ricerca: sostituisci solo la query nel prompt (es. "ricerca su Bitcoin", "ricerca su un prodotto", ecc.)
- Per formato verticale TikTok/Reels: cambia AR a 9:16
- Carica sempre uno screenshot reale e aggiornato di grok.com come @image1 per massima coerenza
