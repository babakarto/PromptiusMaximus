# UGC Style Guide — Effetto Video Amatoriale con AI

> Estratto dalle guide di produzione. Tecniche testate su Kling 3.0 e Seedance 2.0.

---

## KLING 3.0 — Regole UGC

### Struttura Prompt Video UGC
- TUTTO in UN blocco unico — zero paragrafi separati per il dialogo
- Dialogo fuso nell'azione: "she says [testo] in a [tono] voice then [azione]"
- Sempre specificare: "Continuous unbroken single take, no cuts, no transitions"
- Character format: `[Character A: descrizione]`
- Tono voce inline: "calm confident voice", "breathless excited voice", "slow whisper"

### Parole VIETATE in Kling
| MAI scrivere | Perche | Alternativa |
|-------------|--------|-------------|
| phone | Lo renderizza nel frame | NON nominarlo |
| camera | Lo renderizza | Usa "framing" o "lens" |
| holding the camera | Genera telefono in mano | "the framing moves/tilts/follows" |
| brings the camera closer | Genera telefono | "the framing moves closer to her face" |
| camera lying on bed | Genera telefono visibile | "at mattress level pointing upward" |
| selfie | Puo generare telefono | Descrivi solo il framing dall'alto |

### Come Fare Effetto Selfie SENZA Generare Telefono
- Descrivi solo come si muove il FRAMING, non la camera
- "the framing moves closer to her face" = si avvicina
- "the whole framing tilts and follows her movement" = segue il corpo
- "the framing drops to pillow level" = scende
- "the framing shifts slightly" = leggero movimento
- Il soggetto NON tiene/tocca/muove niente — e' il framing che si muove da solo

### Hook Iniziale (primi 3 sec)
- Movimento improvviso verso la camera/lens
- Puntare il dito verso il lens
- Occhi spalancati + frase d'impatto
- Step forward / lean forward rapido
- Cambio espressione improvviso (da seria a sorriso)

### Mini Microfono DJI
Per aggiungere il mini mic wireless tipo content creator:
- "holding a small black wireless lavalier microphone with grey fluffy windscreen in her left hand close to her lips"
- "keeping the microphone near her lips the whole time"
- NON dire "DJI" o "TikTok"

---

## SEEDANCE 2.0 — Keywords UGC

- "low quality iPhone footage, slight compression artifacts, soft focus, motion blur, grainy sensor noise"
- "NOT crisp, NOT sharp, NOT professional"

### Prompt Structure per UGC
- **30-100 parole max** (sweet spot)
- Struttura: Subject → Action → Camera → Style
- Usa `@Image1 (75% weight)` per face/character lock
- Usa `@Video1 (25% weight)` per motion/camera only
- Usa `@Audio1` per lipsync

---

## SNIPPET RIUTILIZZABILI (copia/incolla)

### Stile UGC Amatoriale (aggiungi alla fine di qualsiasi prompt)
```
Low quality phone camera, digital noise and slight compression artifacts, warm tungsten overhead lighting. Natural skin texture with imperfections visible. NOT crisp, NOT sharp, NOT professional, NOT AI-generated looking.
```

### Stile Nokia/Webcam (per look goth/dark)
```
Dim flat ambient light, very low contrast, muted desaturated colors, soft blurry focus, heavy digital noise and blocky compression artifacts, slightly underexposed and washed out, muddy blacks, dull browns beiges and blacks only. NOT contrasty, NOT colorful, NOT bright, NOT sharp, NOT AI-looking.
```

### Effetto Selfie Senza Telefono (per Kling)
```
the framing moves closer to her face / the framing pulls back out / the whole framing tilts and follows her movement / the framing drops to pillow level
```

### Posa: Kneeling + Low Angle (copia/incolla in qualsiasi prompt)
```
She is kneeling on the floor sitting back on her heels with her knees spread apart shoulder-width, torso straight and upright, shoulders back, chest forward, arms resting at her sides, head straight with chin slightly raised looking directly into the camera. Shot from an extremely low angle with the camera placed on the ground at floor level pointing upward, vertical 9:16 format, perfectly centered in frame, slight wide-angle lens distortion from smartphone front camera, the ceiling is visible at the top of the frame.
```

---

## CAMERA IMPERFECTION KEYWORDS (vendono il realismo)
- `autofocus hunts briefly then locks on his face`
- `rack focus misses slightly then corrects`
- `camera operator shifts weight and the framing wobbles`
- `adjusts framing slightly too late`
- `visible ISO noise in shadows`
- `rolling shutter wobble`
- `no color grading, no filters — straight out of camera look`

---

## DA SKILL.MD — Tabella Camera UGC

| Keyword | Effetto |
|---------|---------|
| handheld | UGC style, realism, chaos |
| Sony FX3 + 35mm prime + autofocus hunt + rack focus miss | Best raw footage look |

### Categorie dove UGC funziona meglio
| Categoria | Keywords | Note |
|-----------|----------|------|
| Viral/UGC | TikTok, Reels, meme, funny, UGC | Hook in 2 secondi + short format |
| Viral/UGC | authentic handheld feel, natural expressions | |

---

## WORKFLOW UGC COMPLETO (da Kling 3.0 guide — @heyrobinai)

### Parametri Tecnici per UGC
- Start frame: selfie created in NanoBanana
- Prompt: the woman <<<element_1>>> taking a POV selfie style video and says
- **Arcads** (per UGC): arcads.ai

### Template UGC/Pubblicita
```
[Character A: donna sui 25 anni, capelli castani, occhi verdi, indossa [outfit]]
She starts looking directly at the lens with a natural smile and says "[HOOK]" 
in a warm excited voice, then [AZIONE NATURALE], continues saying "[BODY COPY]" 
while [GESTO CASUAL], then leans closer and says "[CTA]" with a playful grin.
Continuous unbroken single take, no cuts, authentic UGC amateur energy, 
low quality compression artifacts, warm ambient lighting.
```

---

## RISORSE ESTERNE
- **Arcads** (per UGC): arcads.ai
- **NanoBanana** — per generare start frame/selfie realistici
- **Higgsfield** — piattaforma per Kling 3.0 con accesso illimitato

---

> **Fonti**: HANDOFF_PROMPTS.md, SKILL.md, x-research-kling-3-prompt-guide.md, x-research-seedance-2.0-prompt-guide.md
