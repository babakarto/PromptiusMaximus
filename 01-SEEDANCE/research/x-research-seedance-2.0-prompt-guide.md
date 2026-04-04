# Seedance 2.0 - Guida Completa ai Prompt per Video AI

**Data ricerca:** 2026-03-24
**Fonti:** Ricerca web approfondita (8+ fonti analizzate)

---

## 1. Cos'e Seedance 2.0

Seedance 2.0 e il modello di generazione video AI di nuova generazione di **ByteDance**, rilasciato il **10 febbraio 2026**. Non e un semplice text-to-video: e un sistema di produzione audiovisiva completo che accetta simultaneamente:

- **Testo** (prompt in linguaggio naturale)
- **Fino a 9 immagini** di riferimento
- **Fino a 3 video** di riferimento (durata totale ≤15s)
- **Fino a 3 tracce audio** (MP3, durata totale ≤15s)
- **Totale: fino a 12 file** combinabili in un singolo prompt

Output: video fino a **1080p**, durata **4-15 secondi**, con audio nativo generato.

---

## 2. Struttura Base del Prompt

### Formula Fondamentale

```
Subject + Action + Camera + Scene + Style + Constraints
```

Ogni prompt efficace deve contenere questi 6 elementi:

| Elemento | Cosa Specificare | Esempio |
|----------|-----------------|---------|
| **Subject** | Chi/cosa, eta, abbigliamento, espressione | "28-year-old female survivor in tactical gear" |
| **Action** | Verbo al presente, un'azione chiara per shot | "slowly turns toward camera and smiles" |
| **Camera** | Tipo di shot + movimento + angolo + lente | "slow dolly-in from medium to close-up, 50mm feel" |
| **Scene** | Ambientazione, atmosfera, illuminazione | "abandoned factory at dusk, volumetric fog" |
| **Style** | Estetica visiva, color grading | "cinematic, desaturated earth tones, film grain" |
| **Constraints** | Consistenza, esclusioni, durata | "maintain face consistency, no flicker, 10s" |

### Template Compatto

```
Subject: [una persona/oggetto, eta o materiale se rilevante]
Action: [frase verbale specifica, tempo presente]
Camera: [dimensione shot] + [movimento] + [angolo], [lunghezza focale]
Style: [un'ancora visiva], [illuminazione], [trattamento colore]
Constraints: [lista esclusioni], [frame rate/tempo], [durata], [note consistenza]
```

### Lunghezza Ottimale

- **Minimo:** 30 parole (sotto = risultati imprevedibili)
- **Sweet spot:** 120-280 parole
- **Massimo consigliato:** ~300 parole (oltre = il modello perde focus)
- **Regola d'oro:** Le prime 20-30 parole sono le piu importanti — il modello le pesa di piu

---

## 3. I Tre Framework di Prompting

### Framework A: Five-Segment (Principianti)

```
Subject + Scene/Atmosfera + Action/Performance + Camera Movement + Style/Lighting
```

Ideale per video single-shot o composizioni semplici.

### Framework B: CRAFT (Multi-Asset)

```
C = Context (contesto scena)
R = Reference (@asset di riferimento)
A = Action (azione e movimento)
F = Framing/Timing (inquadratura e tempistica)
T = Tone/Audio (tono e suono)
```

Ideale quando si usano piu file di riferimento (@Image, @Video, @Audio).

### Framework C: Timeline Storyboard (Narrativa)

```
0-4s: [descrizione scena 1 + camera + azione]
4-8s: [descrizione scena 2 + camera + azione]
8-12s: [descrizione scena 3 + camera + azione]
12-15s: [scena finale + risoluzione]
```

Ideale per video multi-shot con narrativa e transizioni.

---

## 4. Vocabolario Camera

### Dimensioni Shot

| Termine | Uso |
|---------|-----|
| **Wide/Establishing** | Stabilire lo spazio, mostrare ambientazione |
| **Medium** | Soggetto + contesto |
| **Close-up** | Dettaglio, emozione |
| **Macro** | Dettagli estremi (texture, gocce, particelle) |

### Movimenti Camera

| Movimento | Descrizione | Sintassi Prompt |
|-----------|-------------|-----------------|
| **Dolly in/out** | Movimento fisico verso/lontano dal soggetto | "slow dolly-in" / "gentle dolly-out" |
| **Track/Tracking** | Seguire il soggetto lateralmente | "tracking shot following subject" |
| **Pan** | Rotazione laterale della camera | "slow pan left/right" |
| **Crane** | Movimento verticale (alto/basso) | "crane shot rising above" |
| **Orbit/360** | Rotazione attorno al soggetto | "360-degree orbit around subject" |
| **Handheld** | Leggero tremolio naturale | "handheld with micro-shake" |
| **Gimbal** | Movimento fluido e stabilizzato | "gimbal-smooth movement" |
| **Push-pull** | Avanti-indietro ritmico | "fast camera push-pull following strike rhythm" |
| **Whip pan** | Panoramica velocissima | "whip pan on beat accents" |
| **Rack focus** | Cambio punto di fuoco | "rack focus from foreground to subject" |

### Angoli

| Angolo | Effetto |
|--------|---------|
| **Eye level** | Neutro, naturale |
| **Low angle** | Potenza, presenza, drammaticita |
| **High angle** | Vulnerabilita, overview |
| **Bird's eye** | Vista dall'alto, panoramica |
| **Dutch angle** | Tensione, instabilita |

### Riferimenti Lente

| Lente | Effetto |
|-------|---------|
| **Wide (24-28mm)** | Spazio ampio, leggera distorsione |
| **Normal (35-50mm)** | Naturale, versatile |
| **Telephoto (85mm+)** | Compressione, bokeh, intimita |
| **Macro** | Dettagli estremi |

### Velocita

La velocita funziona come scalare: **slow, medium, fast**, combinata con distanza:
- "slow dolly-in, 1-2 feet"
- "fast tracking shot"
- "medium-speed orbit"

---

## 5. Sistema di Riferimenti @Tag

### Come Funziona

Carica da 1 a 12 file di riferimento. Il sistema assegna etichette automatiche:
- `@Image1`, `@Image2`, ... (fino a 9)
- `@Video1`, `@Video2`, `@Video3`
- `@Audio1`, `@Audio2`, `@Audio3`

### Sintassi nel Prompt

```
"@Image1 as the first frame, [descrizione soggetto, azione, camera, scena]"
"Reference @Video1 for camera movement and shot language, [descrizione nuovo contenuto]"
"@Image1 as first frame, @Video1 for motion, @Audio1 for rhythm"
"@Image1 as first frame and @Image2 as last frame"  (transizione)
"Imitate the action of @Video1"  (trasferimento movimento)
"Character following @Video1 runs through..."  (consistenza personaggio)
```

### Priorita dei Riferimenti

| Tipo | Cosa Controlla |
|------|----------------|
| **@Audio** | Ancora ritmo, lip-sync, pacing musicale |
| **@Video** | Trasferisce traiettorie di movimento |
| **@Image** | Blocca aspetto personaggio, stile visivo, frame iniziale/finale |

### Regole Importanti

- Il prompt **deve essere coerente** con l'immagine di input (se l'immagine mostra un uomo, non descrivere una donna)
- Seedance 2.0 **espande automaticamente** il prompt in base all'immagine input — mantieni le descrizioni concise
- Seedance 2.0 **NON supporta prompt negativi** — descrivi cosa VUOI, non cosa non vuoi

---

## 6. Multi-Shot: Tecniche Avanzate

### Regola d'Oro

- **Sweet spot: 2-3 shot** per prompt
- Oltre 5 shot = la consistenza del soggetto inizia a deteriorarsi
- Le prime 20-30 parole devono "fissare" il soggetto, altrimenti il motore multi-shot allucinera nuovi personaggi

### Struttura Multi-Shot con Timestamp

```
"[Descrizione soggetto].
0-4s: [Shot 1 - establishing + azione iniziale].
4-8s: [Shot 2 - sviluppo + cambio camera].
8-12s: [Shot 3 - climax + azione principale].
12-15s: [Shot 4 - risoluzione + shot finale].
[Vincoli di consistenza]."
```

### Esempi di Sequenze Multi-Shot

**Fantasy Quest (3 shot):**
```
Wide shot entering cave with torch → close-up nervous eyes →
glowing sword drawn with low-angle tracking
```

**Sci-Fi Noir (3 shot):**
```
Bird's-eye neon city view → detective lighting cigarette under
flickering light → examining holographic photo
```

**Narrativa Robot (4 scene):**
```
"Robot wakes in abandoned factory (Scene 1). Walks outside seeing
sunset wasteland (Scene 2). Discovers small flower, gently touches it
(Scene 3). Looks up and smiles at sky (Scene 4). Keep robot appearance
consistent. Emotional transition from confusion to warmth. Cinematic
camera, warm tones, epic mood, no flicker."
```

---

## 7. Linguaggio Fisico e Audio

### Fisica e Movimento

NON scrivere descrizioni generiche. Specifica la **meccanica fisica**:

| Invece di... | Scrivi... |
|-------------|-----------|
| "car turns" | "The tires smoke as the car drifts 90 degrees" |
| "walks in rain" | "rain slides down face, wet fabric clings to body" |
| "sword fight" | "metal clangs spark realistically, sword light trails" |
| "drops object" | "object falls under gravity with natural bounce" |

### Keyword Audio Nativi

Seedance 2.0 genera audio sincronizzato. Usa keyword specifiche:

| Keyword | Contesto |
|---------|----------|
| **"muffled"** | Scene subacquee |
| **"echoing"** | Grandi sale, caverne |
| **"crunchy"** | Camminata su ghiaia |
| **"metallic clink"** | Impatto metallo |
| **"crisp tapping"** | Dita su superfici |
| **"soft plop"** | Liquido che cade |

### Illuminazione

Specifica SEMPRE la qualita della luce:

| Termine | Effetto |
|---------|---------|
| **God rays** | Raggi di luce volumetrici |
| **Volumetric fog** | Nebbia con profondita |
| **Rim light** | Luce di contorno |
| **Three-point lighting** | Illuminazione professionale studio |
| **Soft key + rim** | Product shot |
| **Warm/cool tones** | Temperatura colore |
| **High-key** | Luminoso, commerciale |
| **Low-key** | Drammatico, noir |
| **Flickering** | Candele, luce instabile |
| **Neon** | Cyberpunk, notturno urbano |

---

## 8. Problemi Comuni e Soluzioni

### Inconsistenza Personaggio/Volto

**Soluzione:** Aggiungi al prompt:
```
"Keep the same character, same clothing, same hairstyle, no face
changes, no flicker, high consistency"
```
Oppure usa `@Image1` per bloccare l'aspetto.

### Distorsione Mani

**Soluzioni:**
- Evita close-up veloci delle mani
- Aggiungi: `"hands with perfect anatomy"`
- Usa movimenti delle mani piu lenti e ampi

### Testo Distorto

**Soluzioni:**
- Usa testo piu grande e centrato
- Aggiungi: `"text clear and readable"`
- Riduci la quantita di testo nella scena

### Artefatti di Movimento

**Soluzioni:**
- Sostituisci "fast" con "medium speed"
- Usa riferimenti video (`@Video1`) per bloccare il pattern di movimento
- Specifica la fisica: "natural body mechanics"

### Randomness Eccessiva

**Soluzioni:**
- Carica piu file di riferimento
- Abbassa il livello di creativita nei settings
- Aggiungi vincoli espliciti in tutto il prompt

### Stile che Deriva

**Soluzione:** Sostituisci aggettivi vaghi con un singolo riferimento visivo forte:
- NO: "cool, dreamy, magical vibes"
- SI: "Wes Anderson color palette, pastel symmetry, centered framing"

### Soggetto che Muta

**Soluzione:** Semplifica i descrittori a un singolo nome chiaro nelle prime parole.

### Artefatti Persistenti

**Soluzione:** Cambia il piano di shot invece di accumulare vincoli.

---

## 9. Parametri di Generazione

| Parametro | Valore Consigliato |
|-----------|-------------------|
| **Durata** | 5s per test, 10-30s per produzione |
| **Aspect Ratio** | 9:16 (verticale/social), 16:9 (orizzontale/cinema) |
| **Risoluzione** | 720p (velocita), 1080p/2K (qualita) |
| **Seed** | -1 (random) oppure numero fisso (riproducibile) |
| **Creativita** | Bassa = piu vicino ai riferimenti; Alta = piu liberta |

---

## 10. Prompt Completi Pronti all'Uso

### A. Anime Character (Single Shot)

```
18-year-old Japanese anime girl with short hair, white dress and
straw hat, standing on forest path in warm summer afternoon sunlight.
She slowly turns toward camera and smiles gently. Light breeze moves
hair and dress. Camera slowly pushes from medium shot to close-up.
Soft natural lighting, film grain, healing mood, cinematic quality.
Maintain face and clothing consistency, no distortion, high detail.
```

### B. Product Rotation (Commerciale)

```
Minimalist black matte mechanical keyboard on pure white infinite
studio background, rotating smoothly 360 degrees clockwise. RGB
lighting gently breathing. Keycap text sharp and readable. Fixed
macro camera, smooth turntable motion, commercial photography style,
soft high-key lighting, no noise. Logo and text remain perfectly
consistent.
```

### C. Action Wuxia (Multi-Shot con Riferimenti)

```
Wuxia-style male hero [based on reference video character], black
martial outfit, fighting enemies in rainy bamboo forest at night.
Fast sword combos with visible sword light trails and splashing water.
Fast follow camera, crane shots, quick close-ups. Cinematic camera
language. Maintain character appearance and clothing consistency.
Realistic physics, wet fabric, rain interaction.
```

### D. Music Video Cyberpunk

```
Trendy cyberpunk girl dancing in neon city street at night. Every
strong beat triggers cut or speed-ramped camera move. Neon signs
reflecting on wet ground. Cyberpunk style, fast-paced editing,
multi-shot continuity. Dance movements and character appearance
remain consistent.
```

### E. ASMR Skincare (Verticale, con Audio)

```
Create a vertical ASMR video with no music, focusing on macro details.
A light blue skincare gel bottle sits on glass. A pale, elegant hand
gently taps the glass, producing crisp fingernail tapping sounds. The
hand picks up the bottle and slowly twists the cap, with the rotation
sound clearly audible. A spoon scoops a portion of gel and drops it
onto the glass with a soft "plop," showing dense gel with tiny air
bubbles.
```

### F. Latin Dance (Timeline con Audio)

```
Latin couple in tropical night setting—red dress, black shirt.
0-5s: Close spin at slow tempo; dress flows softly.
5-10s: Rhythm intensifies with fast spins, leg lift, exchanged glances.
10-13s: Crossed-step sequence.
13-15s: Final embrace pose.
Camera transitions from circular medium shot to gradual close-up
synchronized with footwork.
```

### G. Pizza Shop (Realistico)

```
From outside the glass window, the dim camera slowly pushes inward
into a pizza shop. A bearded white male employee is baking pizza. He
removes the pizza from the oven with a metal tray, places it into a
red takeaway box, closes the lid, and then hands it to a customer
with a warm smile.
```

### H. Post-Apocalyptic (Cinematic Trailer)

```
Wind whips sand across ruins. A 28-year-old female survivor stands
on crumbling structure. Desaturated earth tones, realistic wind
physics, fabric movement. Camera pushes from medium to close-up.
Tactical gear, determined expression, dust particles in volumetric
light. Cinematic grain, shallow depth of field.
```

### I. Smartphone Product Video (Timeline)

```
Premium smartphone from @Image1 in diffused studio.
0-3s: Product floats, slowly rotating 360 against gradient background.
3-7s: Macro shot drifting to side panel as light glides across
metallic surface.
7-10s: Screen gently illuminates with animated fingerprint sensor.
10-15s: Camera slowly drifts into screen center where UI elements
breathe subtly.
Minimalist tech aesthetic, realistic metallic reflections and glass
refraction.
```

### J. Explosive Escape (Action con @Image)

```
Tactical soldier from @Image1, dust-covered, minor wounds, cold
expression.
0-4s: Cautiously advances through burning industrial zone.
4-8s: Lateral explosion causes instinctive ducking.
8-12s: Slow motion moving through fire and debris.
12-15s: Exits burning area, confirms safety before breathing.
Raw survival instinct, no heroic poses. Realistic fire physics and
debris trajectory.
```

---

## 11. Checklist Veloce Pre-Generazione

- [ ] Il soggetto e definito nelle **prime 20-30 parole**?
- [ ] C'e **un solo verbo/azione principale** per shot?
- [ ] La **camera** e specificata (shot size + movimento)?
- [ ] L'**illuminazione** e definita esplicitamente?
- [ ] Lo **stile** usa un'ancora specifica (non aggettivi vaghi)?
- [ ] I **vincoli di consistenza** sono inclusi?
- [ ] Il prompt e tra **120-280 parole**?
- [ ] Il prompt e **coerente con le immagini** di riferimento?
- [ ] Usi **linguaggio affermativo** (no prompt negativi)?
- [ ] La **fisica** e specificata dove serve?

---

## 12. Workflow Consigliato

1. **Scegli un prompt** dalla libreria o scrivi il tuo
2. **Genera 2-4 variazioni** con lo stesso prompt
3. **Identifica un problema** (camera, pacing, stile, drift)
4. **Correggi quel singolo problema** nel prompt
5. **Rigenera** e confronta
6. **Ripeti** fino a consistenza
7. **Scala:** aumenta durata, risoluzione, complessita

> "Una volta che fai questo processo alcune volte, il prompting per Seedance smette di sembrare fortuna e inizia a sembrare mestiere."

---

## 13. Funzionalita Avanzate

### Estensione Video
```
"Extend @video1 by [X] seconds, [descrizione nuovo contenuto]"
```

### Editing/Sostituzione
```
"Replace [elemento A] in @video1 with [elemento B], [vincoli aggiuntivi]"
```

### Lip-Sync con Audio
```
"[Descrizione speaker]...speaks: '[testo dialogo]'. Precise lip-sync
with @Audio1, natural hand gestures, visible breathing."
```

---

## Fonti

- [GLBgpt - Seedance 2.0 Prompt Guide: From Zero to Cinematic AI Videos](https://www.glbgpt.com/hub/seedance-2-0-prompt-guide/)
- [WaveSpeed AI - Seedance 2.0 Prompt Template Framework](https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/)
- [WeShop AI - How To Master the Prompt Script](https://www.weshop.ai/blog/seedance-2-0-guide-how-to-master-the-prompt-script/)
- [SeaArt - 20+ Copy-Paste Examples](https://www.seaart.ai/blog/seedance-2-0-prompt)
- [Imagine.art - 70 Ready-To-Use AI Video Prompts](https://www.imagine.art/blogs/seedance-2-0-prompt-guide)
- [GitHub - awesome-seedance-2-prompts (1099+ prompts)](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)
- [Vmake AI - 10 Advanced Multi-Shot Prompts](https://vmake.ai/blog/seedance-2-0-prompts)
- [Atlas Cloud - How to Use Seedance 2.0](https://www.atlascloud.ai/blog/guides/How-to-Use-Seedance-2.0-for-Video-Generation)
- [ByteDance Official - Seedance 2.0](https://seed.bytedance.com/en/seedance2_0)
- [DataCamp - What Is Seedance 2.0?](https://www.datacamp.com/blog/seedance-2-0)
- [Freepik - How to Write Prompts for Seedance 2.0](https://www.freepik.com/blog/how-to-write-prompts-for-seedance-2-0/)
- [ChatCut - Seedance 2.0 Prompt Guide](https://chatcut.io/blog/seedance-2-prompt-guide)

---

*Ricerca condotta il 2026-03-24 | ~6 query web + 5 deep-dive su fonti | Costo stimato: $0 (ricerca web, non X API)*
