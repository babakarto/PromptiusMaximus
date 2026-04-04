# Failures & Fixes -- Seedance 2.0 Reference

> Practical diagnosis and repair guide for every documented Seedance 2.0 generation failure.
> Sources: YouTube creator tests, X/Twitter reports, GitHub prompt libraries, community troubleshooting guides.

---

## The One-Variable Rule

**The single most important principle for fixing broken prompts.**

When a generation fails, do NOT rewrite the entire prompt. Change exactly ONE element, then re-generate. Seedance 2.0 produces a clip in under 3 minutes -- you can test 10 variations in 30 minutes. Use this speed.

**Why it matters:** If you change the camera, the lighting, AND the action simultaneously and the output improves, you have no idea which change fixed it. Next time you hit the same problem, you are back to guessing.

**Priority order for isolated fixes:**
1. If framing is wrong --> adjust Camera line only
2. If mood is wrong --> adjust Style/Lighting line only
3. If motion is wrong --> adjust Action line only
4. If character drifts --> strengthen Subject line (move it earlier, add specifics)
5. If background is unstable --> add constraint suffix only

---

## Failure Diagnosis Table

| # | Symptom | Root Cause | Exact Fix | Prevention |
|---|---------|-----------|-----------|------------|
| 1 | **Jelly/wobbly background** -- background moves like jello, warps unnaturally | No camera stability constraint; model defaults to fluid motion on all elements | Append to prompt: `"no warping, no morphing, tripod, stable camera, static background"` | Always include the anti-jelly suffix on static-background shots |
| 2 | **Face changes mid-video** -- character face shifts when camera angle changes or emotions shift | Model has not "seen" the character from all angles; camera reveal exposes unanchored features | 1. Provide 2-3 reference images (front, 3/4, profile) with identical lighting. 2. Use `@Image1` consistently across all shots. 3. Add anchor text: `"maintaining face and clothing consistency"` | Pin character description in the first 20 words; use character sheet turnarounds as reference |
| 3 | **Mechanical/robotic motion** -- actions look stiff, unnatural, puppet-like | Generic action verbs without force/speed/quality adverbs; no physical description of forces | Replace vague verbs with physics-aware descriptions. BAD: `"car turns"` GOOD: `"the tires smoke as the car drifts 90 degrees, weight shifting to the outside wheels"`. Add adverbs: `slowly, powerfully, fluidly, gracefully` | Always pair action verbs with a degree adverb and at least one physical force word (friction, weight, gravity, momentum) |
| 4 | **Video too static / nothing happens** -- output is essentially a still image with micro-movement | Prompt describes a scene without any explicit action or motion verb | Add a clear action verb with timing. Example: `"she slowly raises her hand to her face, pausing mid-gesture"`. Even subtle motion needs explicit description -- the model cannot infer motion from a static scene description | Every prompt must contain at least one motion verb. Use the formula: Subject + Action + Camera |
| 5 | **Overcrowded scene / too much happening** -- chaotic output, nothing reads clearly | Multiple simultaneous camera movements, too many characters performing independent actions, prompt over 200 words | Cut to ONE primary camera move and ONE main action. Remove secondary characters or make them static (`"crowd watches silently"`). Cut prompt to under 100 words | One camera move per shot. One main action per shot. Background characters are props, not actors |
| 6 | **Style drift in multi-segment video** -- visual style changes between shots | Multiple style adjectives without a single strong anchor; no consistent style reference across segments | Replace adjective stacking (`"moody, cinematic, dramatic"`) with a single style anchor (`"Blade Runner 2049 color grade"`). Copy-paste the same style line into every segment | Use ONE style anchor per project. Reuse it verbatim in every shot prompt |
| 7 | **Content filter blocks prompt** -- generation rejected for sensitive content | ByteDance's content filter reads entire prompt as a scene and evaluates intent. Trigger words: `kill, fight, battle, destroy, blood, attack, punch, slash`. Known IP references. Faces in reference images | Substitute trigger words: `"intense power confrontation"` instead of `"fight"`, `"dramatic energy clash"` instead of `"battle"`, `"spectacular light collision"` instead of `"attack"`. Describe characters by appearance, not IP name. Try submitting the exact same prompt twice -- second attempt often passes | Write prompts as shot-list language. Ask: "Would this sentence appear on a real film shoot's shot list?" If not, remove it. Remove emotional backstory/subtext |
| 8 | **Audio not synced with action** -- dialogue waits until end of clip, sound effects misaligned | Too much dialogue for clip duration; audio cues placed after visual action in prompt order | Keep dialogue to 2-3 short sentences per 15-second clip. Embed audio cues inline with the action they accompany: `"she takes a breath, looks around, then says: 'I found it'"`. Add `"no music"` to suppress competing background score | Calibrate word count: ~15-20 spoken words per 15-second clip. Test at 5 seconds first |
| 9 | **Low detail / blurry output** -- soft 720p quality, lacks sharpness | Seedance native output is 720p; no quality suffix in prompt; low-resolution reference images | 1. Append quality suffix: `"4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture"`. 2. Upscale output with Topaz Video AI or Magnific (detail 30-50%, grain 20-30%, sharpen 5-10%). 3. Use reference images at minimum 1024px on short edge | Always include quality suffix. Always provide high-resolution reference images (2K-4K preferred) |
| 10 | **Flickering / exposure instability** -- light levels pulse, moire patterns on fabrics | Mixing color temperatures; moire-prone materials (sequins, mesh, herringbone, micro-patterns); multiple simultaneous camera moves causing frame-to-frame instability | 1. Pin lighting: `"even, diffuse lighting, steady intensity"`. 2. Ban unstable materials: change `"sequin dress"` to `"matte silk dress"`. 3. Add: `"no flickering, no moire, no morphing"`. 4. Limit to one camera move per shot | Use the flicker prevention checklist: pin camera, lock light, ban unstable materials, lock white balance, one camera move at a time |
| 11 | **Background characters distorted** -- crowd members blur into blobs or move identically | Model cannot handle multiple independent agents performing distinct actions | Make crowd static: `"crowd watches in eerie silence"`. Focus all action on one character. Use `"crowd murmur"` for audio presence without visual complexity | Never prompt crowds to perform coordinated actions. Crowds are atmosphere, not actors |
| 12 | **Dialogue timing too fast for clip** -- speech gets rushed or cut off | Written dialogue exceeds what can be spoken naturally in the clip duration | Limit to 2-3 sentences per 15-second clip (~15-20 spoken words). Generate multiple takes and select the one with best timing. Alternatively, shorten dialogue and add micro-gesture cues between lines: `"she pauses, takes a breath, then says..."` | Count words before generating. Rule of thumb: 1.3 words per second of clip length |
| 13 | **Camera movement conflicts** -- camera jerks, soup-like motion, disorienting output | Multiple simultaneous camera instructions (pan + zoom + dolly + handheld) | Remove all but ONE primary camera move. Optional: add one "flavor" modifier. BAD: `"handheld pan with dolly zoom and orbital tracking"`. GOOD: `"slow dolly in, handheld feel"` | Rule: one primary move + one optional flavor. Write camera as a mechanical instruction, not an aesthetic vibe |
| 14 | **Wrong aspect ratio composition** -- subject cut off, awkward framing, empty dead space | Aspect ratio changes generation behavior (not just cropping); prompt not adapted to format | For 9:16 (vertical): one strong subject, minimal background, faster pacing. For 16:9 (horizontal): MUST include background direction (`"clean white wall"`, `"bokeh background"`, specific environment). For 1:1: center subject, symmetrical composition | Always specify composition strategy when changing aspect ratio. 16:9 without background direction = noise |
| 15 | **Color/lighting inconsistent across shots** -- each clip has different color temperature and exposure | No color grading in Seedance; each generation resets color independently | 1. Use identical style anchor in every shot prompt. 2. Use identical lighting description verbatim. 3. Do final color grading in post-production (DaVinci Resolve). 4. Add `"film grain"` consistently to unify texture | Plan for post-production color correction. Seedance does NOT guarantee color consistency between shots |
| 16 | **Extra fingers / hand distortion** -- fused fingers, extra digits, impossible hand poses | Known persistent weakness of all video diffusion models; worse in close-ups and fast hand motion | 1. Use wide or medium shots for hand-involved scenes. 2. Slow down hand motion: `"gently raises one hand, slow deliberate movement"`. 3. Avoid extreme close-ups of finger work. 4. Generate multiple takes and select best | Never request fast hand gestures or precise finger close-ups. Wide framing + slow motion = acceptable hands |
| 17 | **Text rendering failures** -- text on signs/neon morphs, garbles, distorts | Known limitation of diffusion-based generation; small text is especially unreliable | 1. Make text large and centered: `"large centered neon sign reading OPEN"`. 2. Use close-up framing for text elements. 3. Accept that small text will be unreliable. 4. Add text in post-production for critical readability | Never rely on Seedance for critical text. Plan to overlay text in editing software |
| 18 | **IP leaking** -- unwanted brand/character elements appear | Style anchor or description too close to copyrighted material; model training data bleeding through | 1. Describe visual characteristics instead of naming IPs: height, build, hair, clothing, accessories. 2. Avoid `"Marvel-style"`, `"Disney-style"`, `"looks like [character]"`. 3. Use generic descriptors: `"a muscular figure in red and blue armor"` instead of naming the character | Describe appearance, never reference. The content filter also catches IP references |
| 19 | **Last-second character deformation** -- character warps or distorts in final 1-2 seconds of clip | Model loses coherence at the end of longer generations; attention budget depleted | Generate slightly longer than your target duration, then trim the ending in post. If targeting 10 seconds, generate 12-15 seconds and cut | Always plan to trim the last 1-2 seconds of any generation |
| 20 | **Image drift from initial frame** -- output diverges from the reference image | Prompt structure out of order; static element descriptions conflicting with reference image in I2V mode | 1. Follow strict order: Subject > Action > Camera > Style. 2. In Image-to-Video mode, describe ONLY motion -- the model already sees the static elements. Do not re-describe what is visible in the image | In I2V mode: motion only. In T2V mode: full description. Never mix the two approaches |
| 21 | **Armor/clothing symmetry error** -- model assumes symmetry when design is asymmetric | Default behavior fills in unseen details symmetrically | Explicitly anchor what the OTHER side looks like: `"no armor on the right shoulder, dark blue tribal tattoos on the exposed shoulder"` | Always describe asymmetric elements from both sides |
| 22 | **Visual style shift during emotion change** -- asking character to change expression transforms entire visual style | Emotion keyword overrides visual anchors when they are not explicitly re-stated | Re-anchor physical appearance alongside the emotion: `"the character smiles, red embers and ash still on his face, same lighting"` | Always re-state visual anchors whenever introducing emotion or expression changes |

---

## Iterative Refinement Workflow

Follow this exact sequence. Do not skip steps.

### Step 1: Start with a 5-second test clip
Generate a 5-second clip with your initial prompt. This conserves credits and gives fast feedback. Do NOT start with 15 seconds.

### Step 2: Evaluate the test
Watch the 5-second clip and ask:
- Is the subject correct? (face, clothing, proportions)
- Is the action readable? (motion happening as described)
- Is the camera behaving? (correct movement, stable)
- Is the style right? (lighting, color, mood)
- Is audio acceptable? (sounds present, dialogue timed)

### Step 3: If concept works, extend to target duration
If the 5-second test looks right, run the same prompt at 10-15 seconds. Minor issues may appear at longer durations that were not visible at 5 seconds.

### Step 4: If concept fails, diagnose using the table above
Match the symptom to the diagnosis table. Identify the single root cause.

### Step 5: Change ONE variable
Apply the specific fix from the table. Change nothing else.

### Step 6: Re-test at 5 seconds
Generate another 5-second clip with the single change applied.

### Step 7: Repeat
Continue the cycle until quality is acceptable. Then extend duration.

### Step 8: Generate 2-4 takes of the final prompt
Never judge from a single generation. Run 2-4 takes and select the best. For complex action scenes, expect 5-10+ generations to get one good take.

---

## Prompt Length Optimization

| Word Count | Quality Assessment | Use Case |
|---|---|---|
| **Under 30 words** | Too vague. Generic, unfocused output. Model fills gaps with defaults | Never. Even "simple" prompts need 30+ words |
| **30-50 words** | Good for single-shot, single-subject, minimal action | Quick UGC-style content, product showcases, simple portraits |
| **50-70 words** | Optimal sweet spot. Best balance of control and coherence | Standard single-shot generation. Recommended default |
| **70-100 words** | Good for timeline/multi-beat prompts with timed segments | Multi-shot sequences with `[0-3s]`, `[3-6s]` structure |
| **100-200 words** | Acceptable for complex multi-shot with many cuts. Start losing focus | Detailed 5-shot cinematic sequences. Use with caution |
| **Over 200 words** | Quality degrades. Model ignores details. Motion drift increases. Scattered output | Avoid. Cut ruthlessly. If you need 200+ words, split into separate generations |
| **Over 260 words** | Maximum useful range exceeded. Output becomes incoherent | Never. Rewrite from scratch |

**Key finding:** Short prompts in Chinese outperform English equivalents of the same content (model was primarily trained on Chinese data). Use compression to enforce discipline regardless of language.

---

## A/B Test Results (What We Learned)

These are documented findings from real creator comparisons, not theoretical advice.

### Style anchor vs adjective stacking --> Anchor wins
- **FAILS:** `"moody, cinematic, dramatic"` (multiple vague adjectives)
- **WORKS:** `"Blade Runner 2049 color grade"` (single strong reference)
- One strong visual reference outperforms stacking three or more adjectives every time.

### One action vs multiple actions --> One wins
- Multiple simultaneous actions produce chaos. One primary action per shot produces clean, readable output.
- Removing the second camera move (from `"pan + zoom"` to just `"slow dolly in"`) consistently fixes overcrowded shots.

### Short prompt vs long prompt --> Short wins
- A professional filmmaker produced cinematic-quality output from a 2-line prompt.
- 50-70 words empirically outperforms 150+ words in extensive testing.
- Over 260 words, the model actively ignores content.

### With reference image vs without --> Reference wins
- Using a high-quality starting image (generated via Nano Banana 2 or Seedream) drastically improves Seedance output quality.
- Image quality is the ceiling: blurry input = degraded output. Minimum 1024px on the short edge.

### First + last frame vs text only for action --> First + last wins
- Uploading both start and end frames produces smoother, more controlled transitions than text-only action descriptions.
- Trade-off: gives the AI less freedom for high-motion dynamic camera work.
- Best for: ads, storyboards, precise cinematic flows where you know exactly what you want.

### "Cinematic" / "4K" quality keywords vs without --> With wins
- Adding `"cinematic"` or `"4K"` at the end of prompts consistently improves output quality.
- These are not empty tokens -- they activate specific quality pathways in the model.

### Specific camera instruction vs vague aesthetic --> Specific wins
- **FAILS:** `"cinematic feel"`, `"high-quality"`, `"stunning visuals"`
- **WORKS:** `"slow push-in"`, `"static medium shot"`, `"one-take steady follow shot"`
- Camera language should specify mechanical actions, not adjective-laden vibes.

### Seedance vs Kling same-prompt pacing --> Seedance defaults slower
- Seedance inherently produces slower, more cinematic pacing than Kling with identical prompts.
- If you want real-time speed, you MUST explicitly specify: `"rapidly"`, `"at full speed"`, `"real-time pace"`.

### "Slow motion" as quality booster
- `"Slow motion"` does not just slow the clip -- it actually increases motion quality and reduces artifacts.
- Use it as a quality trick even when you do not specifically need slow-mo.

---

## Platform-Specific Issues

| Platform | Known Issues | Workarounds |
|---|---|---|
| **Dreamina** | Content filter is the strictest and getting stricter over time. Queue times of 2-10 hours during peak (9AM-5PM EST). Credits deducted on failed generations. No error differentiation (server overload and content rejection show same generic message) | Generate during off-peak hours. Use 5-second tests to validate prompts before committing to long clips. Re-submit rejected prompts -- second attempt often passes. Use shot-list language, not narrative language |
| **CapCut** | Rolling regional availability (Indonesia, Philippines, Thailand, Vietnam, Malaysia, Brazil, Mexico first). Same underlying model as Dreamina but different UI wrapper | Same prompt strategies as Dreamina. Check availability for your region. Use the Video Studio web interface for canvas-based workflow |
| **SeaArt** | 1500-character prompt limit. Auto-generates dynamic effects from image if no prompt provided. Different prompt structure expectations | Keep prompts under 1500 characters (~250 words). Use their Subject > Scene > Motion > Aesthetic structure. Always provide a prompt -- do not rely on auto-generation |
| **ImagineArt** | May apply platform-specific pre/post-processing that changes output. Different parameter defaults | Test the same prompt on Dreamina to compare. Adjust for platform-specific behavior |
| **Topview** | Unlimited generation model (365-day plans) | Good for high-volume iteration where credit conservation is not a concern |
| **Yapper** | Reported less strict content filtering | Consider for prompts that get blocked on Dreamina |
| **fal.ai / API** | Developer-focused. Parameters exposed differently. First+last frame mode but reference generation may be limited | Good for programmatic workflows. Check current feature parity with Dreamina |

### Cross-Platform Rule
Ambiguous prompts produce the most variance across platforms. Specific, structured prompts converge on similar results regardless of platform. If you are working across platforms, write precise prompts.

---

## Recovery Prompts

When a prompt is failing, try appending one of these recovery modifiers before rewriting from scratch.

### Recovery 1: The Stability Lock
Append when output is wobbly, flickering, or morphing:
```
Locked tripod, zero camera shake, even diffuse lighting, steady intensity,
no flickering, no moire, no morphing, no warping, static background.
```

### Recovery 2: The Consistency Anchor
Append when character or style drifts between shots or mid-clip:
```
Maintaining face and clothing consistency, without distortion, high detail,
keep facial features unchanged, maintain original materials and geometry.
```

### Recovery 3: The Simplifier
Replace your camera line with this when motion is chaotic:
```
Static medium shot, locked-off camera, subject centered in frame.
```
Then re-add camera movement one element at a time after the static version works.

### Recovery 4: The Physics Grounding
Append when motion looks fake, floaty, or robotic:
```
Realistic weight and momentum, natural gravity, smooth organic movement,
physical forces visible in motion.
```

### Recovery 5: The Content Filter Bypass
Rewrite flagged action descriptions using these substitutions:
```
"fight" --> "intense power confrontation"
"battle" --> "dramatic energy clash"
"attack" --> "spectacular light collision"
"destroy" --> "powerful forces meeting"
"kill" --> (remove entirely, describe the visual outcome instead)
"blood" --> "crimson particles" or remove
```
Also: remove all emotional backstory. Write purely as a shot list. Re-submit the exact same prompt a second time if the first attempt is rejected.

### Recovery 6: The Slow-Motion Quality Trick
Append when output has motion artifacts, jitter, or unnatural movement:
```
Slow motion, smooth fluid movement, cinematic pacing.
```
"Slow motion" in Seedance is not just a speed modifier -- it activates higher-quality motion rendering and reduces artifacts. Use it even when you do not specifically need slow-mo, then speed up in post if needed.

### Recovery 7: The Background Tamer (16:9 Specific)
Append when horizontal compositions have noisy or distracting backgrounds:
```
Clean background, soft bokeh, minimal background movement, shallow depth of field.
```
In 16:9 format, the model fills empty horizontal space unpredictably unless you give explicit background direction.

---

## When to Start Over

Not every prompt can be saved. Here are the signs that tweaking will not work and the concept itself needs rethinking.

### Start over when:
1. **You have changed 5+ variables and output is still broken.** The prompt structure is fundamentally flawed. Rewrite from Subject > Action > Camera > Style using the master formula.

2. **The content filter blocks every variation of your concept.** The scene itself is in restricted territory. Re-imagine the scene with different subjects or framing that avoids trigger categories entirely.

3. **The prompt exceeds 200 words and you cannot cut it below 100.** The concept is too complex for a single generation. Split it into 2-3 separate clips and edit together in post.

4. **You are asking for something that is a known persistent weakness.** Precise finger close-ups, reliable text rendering, crowds performing coordinated actions, complex mechanical interactions -- these are structural limitations, not prompt problems. Redesign the shot to avoid the weakness.

5. **The starting reference image is low quality or conflicting.** If your reference image is blurry, has mixed lighting, or contradicts your prompt description, no amount of prompt refinement will fix the output. Go back and generate or find a better reference image first.

6. **You are combining conflicting instructions.** `"Fixed tripod"` + `"handheld shaky feel"`. `"Bright sunlight"` + `"film noir"`. `"Fast pan"` + `"slow dolly"` + `"zoom in"`. These are irreconcilable. Pick one direction.

7. **Three consecutive generations show completely different interpretations.** High variance means your prompt is too ambiguous. The model is guessing. Add specificity to the subject, action, and camera lines until outputs converge.

### Expected generation counts (so you know when you are beyond normal)
- **Simple dialogue or portrait:** 2-3 generations to get a good take. If you are past 5, the prompt is broken.
- **Standard action scenes:** 3-5 generations typical. Past 8 means rethink.
- **Complex mechanical interactions:** 5-10+ generations is normal. This is a model limitation, not a prompt problem.
- **Fight scenes / multi-character action:** Expect to run the same prompt many times and mix-and-match best takes from different generations.
- **Overall baseline:** One creator reports "almost all footage only took one or two generations to get right" with well-structured prompts.

### The rebuild process:
1. Write a fresh prompt in exactly this order: Subject (first 20 words) > Action (one verb with adverb) > Camera (one move) > Style (one anchor) > Constraints
2. Keep it under 70 words
3. Test at 5 seconds
4. Build back complexity one element at a time using the one-variable rule

---

## Quick-Reference: The Three Suffixes

Copy-paste these to the end of prompts as needed.

**Quality Suffix (use on every prompt):**
```
4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture.
```

**Constraint Suffix (use on every prompt):**
```
Maintaining face and clothing consistency, without distortion, generate the video without subtitles.
```

**Anti-Jelly Suffix (use on static-background shots):**
```
No warping, no morphing, tripod, stable camera, static background.
```
