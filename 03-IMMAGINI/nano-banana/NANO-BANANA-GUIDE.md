# Nano Banana 2.0 — Guida Completa

> Estratto dalla pipeline di produzione testata. Tutte le regole, anti-blocco, e prompt verificati.

---

## COME FUNZIONA IL FACE SWAP
- Carichi 2+ immagini, nel prompt le chiami "Image 1", "Image 2", "Image 3"
- Specifica cosa prende da ogni immagine: "Image 1 is the face reference", "Image 2 is the outfit reference"
- Prompt diretto e semplice — le reference fanno l'80% del lavoro
- Per face swap puro: basta "Swap the face on Image 1 with the face from Image 2. Keep everything else identical."

---

## ANTI-BLOCCO NANO BANANA

| Parola bloccata | Alternativa sicura |
|-----------------|-------------------|
| lingerie | garment, fashion piece |
| corset | bustier |
| stockings | hosiery, knit socks, over-the-knee socks |
| thigh-high | over-the-knee |
| mini skirt | fashion skirt |
| low neckline / hugs her figure | fitted V-neck top |
| tight + body description | fitted (senza body ref) |
| raw (skin context) | unretouched |
| "knees spread apart" | "knees wide apart in a relaxed open V position" |
| Linguaggio corpo esplicito | Linguaggio fashion/editorial |

---

## STILE LUCI/COLORI — Come Matchare una Reference

Se vuoi che Nano Banana replichi esattamente lo stile visivo di una foto:
- Usa la foto come Image 1 e specifica: "match the exact color tone, lighting, and grain from Image 1"
- **NON usare "warm tungsten"** se la foto e' flat/dim — esce troppo forte/arancione
- Per foto tipo Nokia/webcam dire: "dim flat ambient light, low contrast, muted desaturated colors, soft focus, heavy digital noise"
- Per foto sovraesposte/daylight: "natural soft daylight, slight overexposure on skin"
- Descrivere le luci in modo MORBIDO: "gentle warm tint" NON "warm tungsten glow"

---

## BACKGROUND INPAINTING

Per ottenere solo il background senza soggetto:
1. Cancella il soggetto con bianco (Paint/Photoshop)
2. Dai l'immagine a Nano Banana con prompt: "Fill the white empty area with the surrounding environment. Continue [descrizione ambiente]. No people, just the scenery continuing seamlessly."
3. Funziona benissimo per riempire con content-aware

---

## CHARACTER SHEET — Metodo Che Funziona

**PROBLEMA:** "Character reference sheet on white background" genera look da videogioco/3D.

**SOLUZIONE:** Usare "casting agency photos" + specificare camera reale:

```
Based on this reference image for exact facial likeness and outfit.

Six photographs of the same real woman taken in a photo studio for a casting agency. Front view, left 3/4 view, right 3/4 view, left profile, right profile, and back view. She is wearing [OUTFIT] in every photo.

Real casting agency photos, NOT character design, NOT 3D model, NOT game art, NOT illustration, NOT digital art, NOT concept art. These are real photographs of a real person taken with a Canon EOS R5 and 85mm portrait lens in a studio with a plain gray seamless paper backdrop.

[DESCRIZIONE DETTAGLIATA PERSONA]

Real photograph skin — visible pores, tiny peach fuzz hair on cheeks catching the light, natural slight redness around nose and chin, light sun freckles on nose bridge. Skin looks like a real girl in her 20s with good skin, not like a render. Subtle undereye texture, natural lip texture with tiny dry lines. Studio softbox lighting creates a soft catchlight in her eyes and a gentle shadow under her chin.

Six photos arranged in a grid, same person same outfit every photo, consistent across all views. Studio photography, Canon color science, shallow depth of field on the backdrop.
```

**Trigger chiave:** "casting agency photos" + "Canon" forza Nano Banana nel territorio fotografico. "Character reference sheet" + "white background" = 3D/game art.

### Correzione Faccia Troppo Rotonda
- "slim elongated oval, NOT round"
- "defined cheekbones", "slim jaw tapering to narrow chin"
- "slightly thinner and more angular than the reference"
- Se ancora troppo tonda: aggiungere "high cheekbones, V-shaped jawline"

---

## PELLE REALE — Come Evitare la Skin Perfetta

**PROBLEMA:** Nano Banana fa pelle troppo perfetta anche con "real skin".

**SOLUZIONE:** Spingere molto sulle imperfezioni + chiedere qualità bassa senza dire "telefono":

```
Shot on a cheap phone camera in mediocre indoor lighting. Heavy visible grain and noise everywhere. The skin is real and imperfect — uneven skin tone, slight redness on cheeks and around nose, a couple of small blemishes, visible pores especially on nose and forehead, dark circles under eyes, dry patch on chin, tiny bumps on forehead. Skin looks like a real 22 year old girl who is NOT wearing foundation or concealer — bare face with all the normal imperfections that come with that. Peach fuzz on cheeks catching the light. Lips slightly chapped and dry, not glossy.

NOT smooth, NOT even, NOT glowing, NOT dewy, NOT porcelain. This is what real skin looks like on a bad phone camera — every imperfection amplified by the grain and flat harsh light. Think bathroom mirror selfie skin, not Instagram skin.

Grainy, noisy, low quality, casual. 9:16 vertical.
```

**Trigger chiave:** "bathroom mirror selfie skin, not Instagram skin"

### Versione Safe — Faccia Bella ma Imperfetta
```
Her face must be detailed and beautiful but authentically real — clear smooth skin with visible pores and subtle natural texture, faint natural flush on cheeks, delicate features, striking dark eyes with natural lashes, pretty but unretouched, no makeup no filters no smoothing.
```

---

## QUALITA BASSA SENZA DIRE "TELEFONO"

Non scrivere mai "phone" o "iPhone" — Nano Banana puo interpretarlo letteralmente. Descrivere solo le caratteristiche tecniche:

```
Heavy visible grain and digital noise across the entire image. Soft focus, slightly muddy, low resolution, flat colors, no sharpness. The image quality is bad on purpose — noisy, compressed, washed out. Nothing looks clean or crisp.
```

---

## FACE SWAP / BLEND — Metodo Corretto

**NON usare** "replace" o "swap" → spiaccica la faccia sopra.

**Usare** "seamlessly blend" + matchare luci:

```
@Image1 is the character reference — face, features, identity.
@Image2 is the scene — keep this photo exactly as it is.

Seamlessly blend the face from @Image1 onto the woman in @Image2. The face must merge naturally into the existing scene — match the exact lighting direction, shadow angles, skin warmth, sun backlight glow, and color grade of @Image2. The face should look like it was always part of this photo — same soft focus, same slight overexposure from the backlight, same ambient light on the skin. No hard edges, no pasting, no difference in sharpness or tone between face and body. Everything else in @Image2 stays identical — same pose, same dress, same grass, same angle, same quality.
```

---

## TEMPLATE PROMPT — Face Swap Semplice
```
Swap the face on the girl in Image 1 with the face from Image 2. Keep everything else from Image 1 exactly the same — same pose, same outfit, same room, same lighting, same angle. Only replace the face. The face must match Image 2 exactly — same features, same [dettagli specifici]. Same [qualita visiva] as both images.
```

---

## LEZIONI IMPARATE

| Problema | Soluzione |
|----------|-----------|
| Nano Banana blocca il prompt | Usare linguaggio fashion: "bustier", "garment", "hosiery" — vedi tabella anti-blocco |
| Nano Banana blocca la reference | Croppare solo la faccia e dare outfit separato |
| Nano Banana non matcha luci/colori | Dare foto come ref e dire "match exact color tone, lighting, grain from Image 1" |
| Nano Banana luci troppo forti | NON scrivere "warm tungsten" — usare "dim flat ambient, gentle warm tint" |
| Faccia troppo rotonda | Aggiungere "slim elongated oval, NOT round, defined cheekbones" |
| Pelle troppo perfetta | Usare snippet "bathroom mirror selfie skin" |
| Face swap spiaccicato | Usare "seamlessly blend" NON "swap/replace" |
| Background senza soggetto | Bianco sul soggetto → inpaint "fill the white empty area" |
| Output troppo 3D/game art | Usare "casting agency photos" + "Canon" NON "character sheet" |

---

> **Fonte**: HANDOFF_PROMPTS_PIPELINE.md — tutti i prompt testati e verificati in produzione.
