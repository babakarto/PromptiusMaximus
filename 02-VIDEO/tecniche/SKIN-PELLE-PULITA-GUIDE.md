# Skin & Pelle Pulita — Guida Effetti Pelle nei Video AI

> Estratto dalle guide di produzione. Snippet testati su Kling 3.0, Seedance 2.0, Nano Banana.

---

## PROBLEMA

Tutti i modelli AI tendono a generare pelle troppo liscia, troppo perfetta, "plastificata". Questo rovina il realismo, specialmente nei video UGC/amatoriali.

Due approcci opposti:
1. **Skin Realism Booster** — quando la pelle esce troppo liscia e vuoi renderla realistica
2. **Faccia Bella ma Imperfetta** — quando vuoi pelle bella MA non finta (per ad/beauty)

---

## SNIPPET 1: Skin Realism Booster

> Aggiungi quando la pelle esce troppo liscia. Forza il modello a generare texture reale.

```
Visible pores, subtle uneven skin texture, natural sebum shine only on T-zone, slight redness around nostrils, visible peach fuzz caught by sidelight, natural under-eye darkness, lips with natural dry texture. Raw unedited skin, no facetune, no smoothing filter. NOT smooth, NOT poreless, NOT airbrushed, NOT glossy.
```

### Quando usarlo:
- Video UGC dove la pelle deve sembrare vera
- Close-up del viso
- Qualsiasi volta che il modello genera "plastic skin"

---

## SNIPPET 2: Faccia Bella ma Imperfetta (versione safe per Nano Banana)

> Per quando vuoi una persona attraente ma credibile — per ad, beauty content.

```
Her face must be detailed and beautiful but authentically real — clear smooth skin with visible pores and subtle natural texture, faint natural flush on cheeks, delicate features, striking dark eyes with natural lashes, pretty but unretouched, no makeup no filters no smoothing.
```

### Quando usarlo:
- Video ad per prodotti beauty/skincare
- Contenuti dove serve "bella ma vera"
- Nano Banana come generatore (versione safe che non viene bloccata)

---

## SNIPPET 3: UGC Amatoriale con Skin Naturale

> Combinazione completa: stile UGC + pelle imperfetta.

```
Low quality phone camera, digital noise and slight compression artifacts, warm tungsten overhead lighting. Natural skin texture with imperfections visible. NOT crisp, NOT sharp, NOT professional, NOT AI-generated looking.
```

---

## SNIPPET 4: Selfie Realistico con Pelle Naturale

> Da un prompt testato e funzionante per Nano Banana:

```
...very pale porcelain skin, naturally pink lips slightly parted, soft round face, small nose, light blonde eyebrows, subtle natural blush on cheeks, no visible makeup...natural soft daylight from a window illuminating her face evenly, slight overexposure on the skin, smartphone camera quality.
```

---

## KEYWORDS SKIN PER MODELLO

### Seedance 2.0 — SKILL.md
| Keyword | Effetto |
|---------|---------|
| subsurface scattering | Luce che penetra la pelle (realismo) |
| dewy texture | Effetto pelle idratata/lucida naturale |
| natural pores | Pori visibili |
| realistic skin | Texture realistica generale |
| Kodak Portra 400 | Warm skin tones, soft grain, slightly faded shadows |

### Beauty Category Keywords
| Keyword | Uso |
|---------|-----|
| 85mm macro lens | Close-up beauty con shallow DOF |
| realistic skin texture | Texture pelle realistica |
| dewy glow | Effetto glow naturale |
| 85mm f/1.8 | Portrait, beauty, shallow DOF |
| Kodak Portra 400 | Warm skin tones, soft |

### Character Description — Skin Tone Specificity
- Be hyper-specific: "warm olive" non "tan"
- "deep brown" non "dark"
- "fair with pink undertones" non "pale"
- "warm golden-brown skin with subtle freckles" non "brown skin"
- Specificare: freckles, moles, scars, dimples, beauty marks

---

## REGOLE D'ORO

1. **Mai dire solo "beautiful skin"** — troppo generico, il modello genera plastica
2. **Specificare COSA rende la pelle reale**: pori, texture irregolare, lucidita T-zone, rossore naturale
3. **Usare negazioni esplicite**: "NOT smooth, NOT poreless, NOT airbrushed, NOT glossy"
4. **Per Nano Banana**: usare la versione "safe" (Snippet 2) che non viene bloccata
5. **Per Kling UGC**: aggiungere "natural skin texture with imperfections visible" nel blocco finale
6. **Per Seedance**: aggiungere "subsurface scattering, dewy texture, natural pores" nel quality suffix

---

## TRUCCHI AGGIUNTIVI

### Luce che aiuta la pelle
- **Warm tungsten overhead**: esalta le imperfezioni naturali (buono per UGC)
- **Natural soft daylight**: effetto pelle luminosa e naturale
- **Sidelight**: rivela il peach fuzz e la texture
- **NON usare** "warm tungsten" se la foto e' flat/dim — esce troppo forte/arancione
- Per foto tipo Nokia/webcam: "dim flat ambient light, low contrast, muted desaturated colors"

### Evitare Skin Troppo Liscia
| Problema | Soluzione |
|----------|-----------|
| Pelle plastificata | Aggiungere Skin Realism Booster (Snippet 1) |
| Nano Banana blocca prompt | Usare Snippet 2 (versione safe) |
| Seedance video troppo HD/crispy | Togliere "2K", aggiungere "low quality iPhone", "NOT crisp" |
| Luci troppo forti su pelle | NON scrivere "warm tungsten" — usare "dim flat ambient, gentle warm tint" |

---

> **Fonti**: HANDOFF_PROMPTS.md, SKILL.md, GAP_Reddit_Style_Anchors_Errors.md
