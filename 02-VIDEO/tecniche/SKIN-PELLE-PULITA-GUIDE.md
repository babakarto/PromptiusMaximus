# Skin & Clean Skin — Guide to Skin Effects in AI Video

> Extracted from production guides. Snippets tested on Kling 3.0, Seedance 2.0, Nano Banana.

---

## PROBLEM

All AI models tend to generate skin that is too smooth, too perfect, "plasticky". This ruins realism, especially in UGC/amateur videos.

Two opposite approaches:
1. **Skin Realism Booster** — when skin comes out too smooth and you want to make it realistic
2. **Beautiful but Imperfect Face** — when you want beautiful skin that is NOT fake (for ad/beauty)

---

## SNIPPET 1: Skin Realism Booster

> Add this when skin comes out too smooth. Forces the model to generate real texture.

```
Visible pores, subtle uneven skin texture, natural sebum shine only on T-zone, slight redness around nostrils, visible peach fuzz caught by sidelight, natural under-eye darkness, lips with natural dry texture. Raw unedited skin, no facetune, no smoothing filter. NOT smooth, NOT poreless, NOT airbrushed, NOT glossy.
```

### When to use it:
- UGC videos where skin needs to look real
- Face close-ups
- Any time the model generates "plastic skin"

---

## SNIPPET 2: Beautiful but Imperfect Face (safe version for Nano Banana)

> For when you want an attractive but believable person — for ads, beauty content.

```
Her face must be detailed and beautiful but authentically real — clear smooth skin with visible pores and subtle natural texture, faint natural flush on cheeks, delicate features, striking dark eyes with natural lashes, pretty but unretouched, no makeup no filters no smoothing.
```

### When to use it:
- Video ads for beauty/skincare products
- Content where you need "beautiful but real"
- Nano Banana as generator (safe version that won't get blocked)

---

## SNIPPET 3: Amateur UGC with Natural Skin

> Full combination: UGC style + imperfect skin.

```
Low quality phone camera, digital noise and slight compression artifacts, warm tungsten overhead lighting. Natural skin texture with imperfections visible. NOT crisp, NOT sharp, NOT professional, NOT AI-generated looking.
```

---

## SNIPPET 4: Realistic Selfie with Natural Skin

> From a tested and working prompt for Nano Banana:

```
...very pale porcelain skin, naturally pink lips slightly parted, soft round face, small nose, light blonde eyebrows, subtle natural blush on cheeks, no visible makeup...natural soft daylight from a window illuminating her face evenly, slight overexposure on the skin, smartphone camera quality.
```

---

## SKIN KEYWORDS BY MODEL

### Seedance 2.0 — SKILL.md
| Keyword | Effect |
|---------|---------|
| subsurface scattering | Light penetrating the skin (realism) |
| dewy texture | Natural hydrated/glowy skin effect |
| natural pores | Visible pores |
| realistic skin | General realistic texture |
| Kodak Portra 400 | Warm skin tones, soft grain, slightly faded shadows |

### Beauty Category Keywords
| Keyword | Use |
|---------|-----|
| 85mm macro lens | Beauty close-up with shallow DOF |
| realistic skin texture | Realistic skin texture |
| dewy glow | Natural glow effect |
| 85mm f/1.8 | Portrait, beauty, shallow DOF |
| Kodak Portra 400 | Warm skin tones, soft |

### Character Description — Skin Tone Specificity
- Be hyper-specific: "warm olive" not "tan"
- "deep brown" not "dark"
- "fair with pink undertones" not "pale"
- "warm golden-brown skin with subtle freckles" not "brown skin"
- Specify: freckles, moles, scars, dimples, beauty marks

---

## GOLDEN RULES

1. **Never just say "beautiful skin"** — too generic, the model generates plastic
2. **Specify WHAT makes skin real**: pores, uneven texture, T-zone shine, natural redness
3. **Use explicit negations**: "NOT smooth, NOT poreless, NOT airbrushed, NOT glossy"
4. **For Nano Banana**: use the "safe" version (Snippet 2) that won't get blocked
5. **For Kling UGC**: add "natural skin texture with imperfections visible" in the final block
6. **For Seedance**: add "subsurface scattering, dewy texture, natural pores" in the quality suffix

---

## ADDITIONAL TRICKS

### Lighting that helps skin
- **Warm tungsten overhead**: enhances natural imperfections (good for UGC)
- **Natural soft daylight**: luminous and natural skin effect
- **Sidelight**: reveals peach fuzz and texture
- **DO NOT use** "warm tungsten" if the photo is flat/dim — it comes out too strong/orange
- For Nokia/webcam-type photos: "dim flat ambient light, low contrast, muted desaturated colors"

### Avoiding Overly Smooth Skin
| Problem | Solution |
|----------|-----------|
| Plasticky skin | Add Skin Realism Booster (Snippet 1) |
| Nano Banana blocks prompt | Use Snippet 2 (safe version) |
| Seedance video too HD/crispy | Remove "2K", add "low quality iPhone", "NOT crisp" |
| Lighting too strong on skin | DO NOT write "warm tungsten" — use "dim flat ambient, gentle warm tint" |

---

> **Sources**: HANDOFF_PROMPTS.md, SKILL.md, GAP_Reddit_Style_Anchors_Errors.md
