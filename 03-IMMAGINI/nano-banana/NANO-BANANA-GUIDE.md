# Nano Banana 2.0 — Complete Guide

> All rules, anti-block techniques, and verified prompts from tested production pipelines.

---

## HOW FACE SWAP WORKS
- Upload 2+ images, in the prompt refer to them as "Image 1", "Image 2", "Image 3"
- Specify what to take from each image: "Image 1 is the face reference", "Image 2 is the outfit reference"
- Direct and simple prompt — references do 80% of the work
- For pure face swap: just "Swap the face on Image 1 with the face from Image 2. Keep everything else identical."

---

## NANO BANANA ANTI-BLOCK

| Blocked word | Safe alternative |
|-----------------|-------------------|
| lingerie | garment, fashion piece |
| corset | bustier |
| stockings | hosiery, knit socks, over-the-knee socks |
| thigh-high | over-the-knee |
| mini skirt | fashion skirt |
| low neckline / hugs her figure | fitted V-neck top |
| tight + body description | fitted (without body ref) |
| raw (skin context) | unretouched |
| "knees spread apart" | "knees wide apart in a relaxed open V position" |
| Explicit body language | Fashion/editorial language |

---

## LIGHTING/COLOR STYLE — How to Match a Reference

If you want Nano Banana to replicate exactly the visual style of a photo:
- Use the photo as Image 1 and specify: "match the exact color tone, lighting, and grain from Image 1"
- **DO NOT use "warm tungsten"** if the photo is flat/dim — it comes out too strong/orange
- For Nokia/webcam-type photos say: "dim flat ambient light, low contrast, muted desaturated colors, soft focus, heavy digital noise"
- For overexposed/daylight photos: "natural soft daylight, slight overexposure on skin"
- Describe lighting in a SOFT way: "gentle warm tint" NOT "warm tungsten glow"

---

## BACKGROUND INPAINTING

To get only the background without the subject:
1. Erase the subject with white (Paint/Photoshop)
2. Give the image to Nano Banana with prompt: "Fill the white empty area with the surrounding environment. Continue [environment description]. No people, just the scenery continuing seamlessly."
3. Works great for content-aware fill

---

## CHARACTER SHEET — Method That Works

**PROBLEM:** "Character reference sheet on white background" generates a video game/3D look.

**SOLUTION:** Use "casting agency photos" + specify a real camera:

```
Based on this reference image for exact facial likeness and outfit.

Six photographs of the same real woman taken in a photo studio for a casting agency. Front view, left 3/4 view, right 3/4 view, left profile, right profile, and back view. She is wearing [OUTFIT] in every photo.

Real casting agency photos, NOT character design, NOT 3D model, NOT game art, NOT illustration, NOT digital art, NOT concept art. These are real photographs of a real person taken with a Canon EOS R5 and 85mm portrait lens in a studio with a plain gray seamless paper backdrop.

[DETAILED PERSON DESCRIPTION]

Real photograph skin — visible pores, tiny peach fuzz hair on cheeks catching the light, natural slight redness around nose and chin, light sun freckles on nose bridge. Skin looks like a real girl in her 20s with good skin, not like a render. Subtle undereye texture, natural lip texture with tiny dry lines. Studio softbox lighting creates a soft catchlight in her eyes and a gentle shadow under her chin.

Six photos arranged in a grid, same person same outfit every photo, consistent across all views. Studio photography, Canon color science, shallow depth of field on the backdrop.
```

**Key trigger:** "casting agency photos" + "Canon" forces Nano Banana into photographic territory. "Character reference sheet" + "white background" = 3D/game art.

### Face Too Round Correction
- "slim elongated oval, NOT round"
- "defined cheekbones", "slim jaw tapering to narrow chin"
- "slightly thinner and more angular than the reference"
- If still too round: add "high cheekbones, V-shaped jawline"

---

## REAL SKIN — How to Avoid Perfect Skin

**PROBLEM:** Nano Banana makes skin too perfect even with "real skin".

**SOLUTION:** Push hard on imperfections + ask for low quality without saying "phone":

```
Shot on a cheap phone camera in mediocre indoor lighting. Heavy visible grain and noise everywhere. The skin is real and imperfect — uneven skin tone, slight redness on cheeks and around nose, a couple of small blemishes, visible pores especially on nose and forehead, dark circles under eyes, dry patch on chin, tiny bumps on forehead. Skin looks like a real 22 year old girl who is NOT wearing foundation or concealer — bare face with all the normal imperfections that come with that. Peach fuzz on cheeks catching the light. Lips slightly chapped and dry, not glossy.

NOT smooth, NOT even, NOT glowing, NOT dewy, NOT porcelain. This is what real skin looks like on a bad phone camera — every imperfection amplified by the grain and flat harsh light. Think bathroom mirror selfie skin, not Instagram skin.

Grainy, noisy, low quality, casual. 9:16 vertical.
```

**Key trigger:** "bathroom mirror selfie skin, not Instagram skin"

### Safe Version — Beautiful but Imperfect Face
```
Her face must be detailed and beautiful but authentically real — clear smooth skin with visible pores and subtle natural texture, faint natural flush on cheeks, delicate features, striking dark eyes with natural lashes, pretty but unretouched, no makeup no filters no smoothing.
```

---

## LOW QUALITY WITHOUT SAYING "PHONE"

Never write "phone" or "iPhone" — Nano Banana can interpret it literally. Only describe the technical characteristics:

```
Heavy visible grain and digital noise across the entire image. Soft focus, slightly muddy, low resolution, flat colors, no sharpness. The image quality is bad on purpose — noisy, compressed, washed out. Nothing looks clean or crisp.
```

---

## FACE SWAP / BLEND — Correct Method

**DO NOT use** "replace" or "swap" — it slaps the face on top.

**Use** "seamlessly blend" + match lighting:

```
@Image1 is the character reference — face, features, identity.
@Image2 is the scene — keep this photo exactly as it is.

Seamlessly blend the face from @Image1 onto the woman in @Image2. The face must merge naturally into the existing scene — match the exact lighting direction, shadow angles, skin warmth, sun backlight glow, and color grade of @Image2. The face should look like it was always part of this photo — same soft focus, same slight overexposure from the backlight, same ambient light on the skin. No hard edges, no pasting, no difference in sharpness or tone between face and body. Everything else in @Image2 stays identical — same pose, same dress, same grass, same angle, same quality.
```

---

## TEMPLATE PROMPT — Simple Face Swap
```
Swap the face on the girl in Image 1 with the face from Image 2. Keep everything else from Image 1 exactly the same — same pose, same outfit, same room, same lighting, same angle. Only replace the face. The face must match Image 2 exactly — same features, same [specific details]. Same [visual quality] as both images.
```

---

## LESSONS LEARNED

| Problem | Solution |
|----------|-----------|
| Nano Banana blocks the prompt | Use fashion language: "bustier", "garment", "hosiery" — see anti-block table |
| Nano Banana blocks the reference | Crop just the face and provide outfit separately |
| Nano Banana doesn't match lighting/colors | Provide photo as ref and say "match exact color tone, lighting, grain from Image 1" |
| Nano Banana lighting too strong | DO NOT write "warm tungsten" — use "dim flat ambient, gentle warm tint" |
| Face too round | Add "slim elongated oval, NOT round, defined cheekbones" |
| Skin too perfect | Use "bathroom mirror selfie skin" snippet |
| Face swap looks pasted on | Use "seamlessly blend" NOT "swap/replace" |
| Background without subject | White over subject then inpaint "fill the white empty area" |
| Output too 3D/game art | Use "casting agency photos" + "Canon" NOT "character sheet" |

---

> **Source**: HANDOFF_PROMPTS_PIPELINE.md — all prompts tested and verified in production.
