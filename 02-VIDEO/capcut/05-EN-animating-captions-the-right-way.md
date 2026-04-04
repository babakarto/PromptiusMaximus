# You're Animating Captions the Wrong Way — The Correct System

> **Author:** Patrik Key
> **Video:** https://www.youtube.com/watch?v=hjNH5JUVgEw
> **Key takeaway:** The exact system to build pro-level animated captions using 2 fonts and 3 master movements you reuse throughout the entire video

---

## The 3 Main Steps

If you don't master these 3 steps, you won't get the same results.

---

## Step 1: The Base — Your Two Fonts

You need to choose **2 fonts** and decide their roles:

| Type | Role | Use |
|------|------|-----|
| **Primary Font** | Context | Main content words |
| **Secondary Font** | Emotion | Highlighting keywords and emotional words |

> **Trick:** If you treat every word the same, nothing really stands out. Primary font handles context, secondary font handles emotions and highlighting keywords.

---

## Step 2: Stylize Your Text BEFORE Generating Captions

### Primary Font Settings (Helvetica):
1. Font: **Helvetica**
2. Enable **Bold**
3. Enable **Uppercase**
4. **Character Level** (character spacing): **-2**
5. **Stroke**: around **4**
6. **Shadow**: opacity around **70**

### Animation:
1. Go to **Animation**
2. Set **Blur** on both **In** and **Out**
3. Duration: **0.6 seconds**

> These settings create a professional, cinematic look.

---

## Step 3: Build the 3 Master Movements

These 3 movements are reused throughout the entire video. Build them once, replicate forever.

### Initial Setup:
1. Click **Generate Captions**
2. Take the layer and bring it above
3. Hide the layer with **V**
4. Position the layer slightly below the chin

---

### Movement 1: Slide Left (From Left to Center)

1. Go to the **beginning** of the layer
2. Activate **keyframe on Transform**
3. Activate **keyframe on Blend** (opacity)
4. Hold **Shift** + press **right arrow 10 times** (= 10 frames forward)
5. Activate another keyframe on Transform and Blend
6. Go back to the **first keyframe**:
   - **Opacity** = 0 (creates fade in)
   - **Position X** = **-600** (starts from the left)
7. **Smoothing:** Open Variable Speed Animation > select both keyframes > **Shift + W** (shortcut to smooth out keyframes)
8. Do the same for opacity

> **Shortcut Shift + W** = automatic smooth on selected keyframes

---

### Movement 2: Slide Right (From Right to Center)

1. **Duplicate** the Slide Left layer
2. Go to the first keyframe
3. Change **Position X** from -600 to **+600**

> Everything else stays exactly the same.

---

### Movement 3: Slide Up (From Bottom to Top)

1. **Duplicate** the layer
2. Hide with **V**
3. Go to the first keyframe
4. **Position X** = **0** (no horizontal movement)
5. **Position Y** = **-1200** (starts from the bottom)
6. Open the **Graph Editor** and smooth all keyframes

> Different direction = you need to re-smooth in the graph editor.

---

### Organizing the Movements:

1. Rename the 3 layers:
   - `Slide Left`
   - `Slide Right`
   - `Slide Up`
2. **Copy all 3** and paste them at the **end of the clip** (backup so you don't lose them)

---

## Creating Captions with the Movements

### Procedure:
1. Create a **Compound Clip** for each of the 3 layers (separately)
2. Type the first word in the appropriate layer
3. Position it visually below the previous caption

### Practical Example ("If you buy make smooth captions in CapCut"):

| Word | Movement | Notes |
|------|----------|-------|
| "if" | Slide Up | Primary font |
| "you" | Slide Left | Primary font |
| "buy" | Slide Left | Primary font, layer 3 |
| "make" | Slide Left | Compound, font size ~18 |
| "smooth" | Slide Up | Font size ~20 |
| "captions" | Slide Right | **Secondary font** (Shell), title case, no bold, character level 0 |

### For Each Word:
1. Duplicate the movement you want to use
2. Position on the timeline
3. Change the text
4. Adjust font size if needed
5. Create **Compound Clip**
6. Position visually in the frame

### Timing:
- Select all layers
- **Offset** each layer to align with the spoken words
- Each word appears when it's being said

---

## Highlighting Keywords

1. Open the compound of the word you want to highlight
2. Select the **text layer** inside
3. **Change the color** of the word

> This makes important keywords pop against the rest of the captions.

---

## Secondary Font — Settings

When using the secondary font (e.g., for "captions"):

| Setting | Value |
|---------|-------|
| Font | Shell (or your chosen secondary) |
| Bold | **Disabled** |
| Character Level | **0** (reset) |
| Title Case | **Enabled** |
| Font Size | Larger than primary |

---

## Full Workflow Summary

```
1. STYLIZE text (Helvetica, bold, uppercase, -2 char, stroke 4, shadow 70)
2. ANIMATE with Blur in/out at 0.6s
3. CREATE the 3 master movements (Left, Right, Up)
4. RENAME and SAVE the movements as backup
5. For each word:
   a. Duplicate the right movement
   b. Change the text
   c. Create compound
   d. Position in the frame
   e. Offset for timing
6. HIGHLIGHT keywords with secondary font + different color
7. REPEAT for the entire video
```

---

## Important Shortcuts

| Shortcut | Action |
|----------|--------|
| **V** | Hide/Show layer |
| **Shift + Arrow** | Advance 10 frames |
| **Shift + W** | Smooth selected keyframes |
| **Option + G** (Mac) | Create Compound Clip |
| **S** | Split All |

---

## Final Notes

- It takes a little time at the beginning, but it becomes **muscle memory**
- The 3 master movements are the key: build them once, use them forever
- Mix movements for visual variety
- Secondary font creates **visual hierarchy** in your captions
- Recommended CapCut version: **6.40+**
