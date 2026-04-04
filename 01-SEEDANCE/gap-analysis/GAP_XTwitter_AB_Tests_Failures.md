# Seedance 2.0 - A/B Tests, Failures & Creator Discoveries (X/Twitter Research)

> Research compiled March 28, 2026 from X/Twitter posts, creator threads, and GitHub prompt libraries
> Focus: Specific gaps -- failure examples, A/B tests, exact prompts, and advanced tips from real creators testing the model

---

## 1. A/B Prompt Comparisons (What Works vs What Doesn't)

### Seedance 2.0 vs Sora 2 -- Same Prompt Physics Test
**Creator:** @Dheepanratnam
**Test:** Ran the exact same prompt on both Sora 2 and Seedance 2.0.
**Result:** "The difference in physics understanding is actually shocking. Seedance nailed the fluid dynamics and condensation vortices in one shot. Sora... well, see the reply."
**Key Finding:** Seedance 2.0 wins on physics simulation; Sora 2 auto-adds music which makes output feel polished superficially.
- Source: [Dheepan Ratnam](https://x.com/Dheepanratnam/status/2025724576882159876)

### Seedance 2.0 vs Sora 2 -- Shot Breakdown & Pacing
**Creator:** @underwoodxie96
**Test:** Exact same prompt on both models.
**Result:** "Sora 2 automatically adds music, which instantly makes the video feel polished. But Seedance 2.0 handles shot breakdown and pacing better -- it feels more like a professionally edited sequence."
**Key Finding:** Seedance excels at multi-shot structure; Sora excels at audio polish.
- Source: [underwood](https://x.com/underwoodxie96/status/2020819034426708042)

### Seedance 2.0 vs Grok Imagine -- Storm Scene
**Creator:** @lexx_aura
**Prompt used:** "Stormy night ocean, massive waves under lightning flashes. The sea churns violently as a colossal feline titan rises from the depths, water cascading off its fur in slow motion. Low-angle cinematic..."
**Test:** Same prompt on both Seedance 2.0 and Grok Imagine.
- Source: [Lex](https://x.com/lexx_aura/status/2029201125560217751)

### Seedance 2.0 vs Kling 2.1 Pro -- Same First Frame
**Creator:** @aaronadler
**Test:** Same first frame, two different models.
**Result:** "Kling's output feels realtime. Seedance output feels slow motion."
**Key Finding:** Seedance defaults to more cinematic, slower pacing even without explicit slow-mo instruction.
- Source: [Aaron Adler](https://x.com/aaronadler/status/1943323365336306108)

### Four-Way Comparison: Kling 3.0 vs Seedance 2.0 vs Sora 2 vs VEO 3.1
**Creator:** @wavespeed_ai
**Test:** "One prompt. Four models. Who delivers the best results?"
- Source: [WaveSpeedAI](https://x.com/wavespeed_ai/status/2020921891163152571)

### Same Prompt, Three Different Outputs
**Creator:** @gavinpurcell
**Prompt:** "A woman tensely asks the man in the shadows to come out. Slow push in as she tells him she knows everything he's done and he's going to pay. Deep in the shadows, we see the figure as he responds."
**Result:** Three distinct but coherent interpretations from the same prompt. Demonstrates Seedance 2.0's variance control -- each run produces meaningfully different creative choices while maintaining prompt fidelity.
- Source: [Gavin Purcell](https://x.com/gavinpurcell/status/2021732810554507352)

### "Cinematic" vs No "Cinematic" -- Quality Modifier Test
**Creator:** @alex_prompter
**Finding:** "Adding 'cinematic' or '4K' at the end consistently improves output quality."
**Implication:** These aren't empty tokens -- they activate specific quality pathways in the model.
- Source: [Alex Prompter](https://x.com/alex_prompter/status/2025633828459389023)

### Vague Aesthetic vs Specific Camera Instruction
**From GitHub prompt library (gracech0322-cmd):**
- **FAILS:** "cinematic feel", "high-quality", "stunning visuals"
- **WORKS:** "slow push-in", "static medium shot", "one-take steady follow shot"
- **Rule:** "Use rules, not aesthetics" -- camera language should specify mechanical actions, not adjective-laden vibes.
- Source: [seedance-2-prompt-library](https://github.com/gracech0322-cmd/seedance-2-prompt-library)

### Single Style Anchor vs Multiple Adjectives
**From seedance2prompt.org:**
- **FAILS:** "moody, cinematic, dramatic" (multiple vague adjectives)
- **WORKS:** "Blade Runner color grade" (single strong reference)
- **Rule:** One strong visual reference outperforms stacking adjectives.
- Source: [Seedance 2 Prompts](https://seedance2prompt.org/)

---

## 2. Documented Failures & Root Causes

### FAILURE: Content Filter Blocking Normal Prompts
**Creator:** @javilopen
**Report:** "Bad news is that Seedance 2.0 is getting ABSOLUTELY nerfed. Random normal images and super naive things in the prompt, like just writing 'gun', will block your generations. The experience is getting worse and worse every day inside Dreamina."
**Root Cause:** ByteDance's progressive content filter tightening post-launch.
- Source: [Javi Lopez](https://x.com/javilopen/status/2028168975138574757)

### FAILURE: Last-Second Character Deformation
**Creator:** @TheoMediaAI
**Report:** "Character consistency is rock solid here, but -- in the last few seconds? Well... you'll see. Amazing? Yes. But you'll still need to edit."
**Root Cause:** Model loses coherence in final frames of longer generations. Character features can warp/deform near the clip end.
**Workaround:** Generate slightly longer than needed, trim the ending.
- Source: [Theoretically Media](https://x.com/TheoMediaAI/status/2021625694846169141)

### FAILURE: Realism Quality Nerfed Over Time
**Creator:** @JSFILMZ0412
**Report:** "I think they nerfed Seedance 2.0 as far as realism goes. RIP"
**Root Cause:** Post-launch model adjustments reduced photorealism quality, likely to address IP/deepfake concerns.
- Source: [JSFILMZ](https://x.com/JSFILMZ0412/status/2022594350601912692)

### FAILURE: Negative Prompts Don't Work
**From seedance2prompt.org documentation:**
**Issue:** "Seedance 2.0 does not respond to negative prompts." Writing "no blur, no noise" produces zero effect.
**Fix:** Replace with positive descriptors: "sharp focus, crisp clean details, pristine quality."
- Source: [Seedance 2 Prompts](https://seedance2prompt.org/)

### FAILURE: Character Morphing/Deformation
**Root Cause:** Complex character descriptions without image reference.
**Fix:** "Simplify Subject to one noun. Upload reference image and use @Image1 to lock the character. Avoid describing what the character looks like in I2V mode -- the model already sees the image."
- Source: [Seedance 2 Prompts](https://seedance2prompt.org/)

### FAILURE: Image Drift from Initial Frame
**Root Cause:** Mixing structural elements out of order.
**Fix:** Strict formula order: Subject -> Action -> Camera -> Style.
- Source: [Seedance 2 Prompts](https://seedance2prompt.org/)

### FAILURE: Prompt/Image Contradiction in I2V Mode
**Issue:** Describing static elements that are already visible in the reference image creates conflicts.
**Fix:** "In Image-to-Video mode, describe only motion. The model sees what's in the image. Describing static elements creates conflicts."
- Source: [Seedance 2 Prompts](https://seedance2prompt.org/) / [Alex Prompter](https://x.com/alex_prompter/status/2025633828459389023)

### FAILURE: Camera Goes Haywire
**Root Cause:** Multiple motion verbs per shot segment.
**Fix:** One motion verb per beat; sequential descriptions only.
- Source: [Seedance 2 Prompts](https://seedance2prompt.org/)

### FAILURE: Style Inconsistency Across Multi-Shot
**Root Cause:** Using multiple style adjectives instead of a single anchor.
**Fix:** Single anchor reference (e.g., "Blade Runner 2049 color grade") instead of adjective lists.

### FAILURE: Fake Physics / Unrealistic Motion
**Root Cause:** Generic action descriptions.
**Bad:** "car turns"
**Good:** "the tires smoke as the car drifts 90 degrees"
**Rule:** "Describe physical forces explicitly. Mention friction, weight, gravity, momentum."

### FAILURE: Overloading Input Files
**Issue:** Throwing too many reference files degrades quality.
**Limit:** Maximum 12 files mixed (9 images + 3 videos + 3 audio). Prioritize high-impact materials.

### FAILURE: Credits Burned on Failed Generations
**Creator:** @AlphaSignalAI
**Report:** Credits are deducted even with failed generation.
**Workaround:** Start with 5-second test clips during iteration, extend only when prompt is locked.
- Source: [AlphaSignal AI](https://x.com/AlphaSignalAI/status/2021807640641515841)

### Content Filter Workaround Guide
**Creator:** @ClonizerAi
**Specific word substitutions that bypass the filter:**
- AVOID: fight, battle, destroy, kill, blood, brutal, attack, punch, slash
- USE INSTEAD: "intense power confrontation," "dramatic energy clash," "spectacular light collision," "powerful forces meeting," "epic visual impact"
- AVOID: Direct character names (Marvel, Disney, anime IPs)
- USE INSTEAD: Detailed visual appearance descriptions (height, build, hair, clothing, facial features, accessories)
- **Re-submit trick:** "Try the exact same prompt twice -- the second attempt often passes when the first one doesn't."
- **Structure tip:** Keep scenes 10-15 seconds, break complex scenes into 3 clear shots, add "No spoken dialogue" when there is no talking.
- Source: [Clonizer](https://x.com/ClonizerAi/status/2026069700632019271)

---

## 3. Audio Prompt Discoveries

### Native Audio Generation
Seedance 2.0 generates audio natively alongside video -- no separate pipeline needed. This includes lip-synced speech, music, and sound effects.

### Audio Keyword Vocabulary That Works
From seedance2prompt.org documentation, these sound keywords trigger specific audio generation:
```
reverb, echo, muffled, sharp, high-pitched, deep bass, metallic clink,
crackling fire, rushing water, wind howling, footsteps on gravel,
thunder rumbling, glass shattering, engine roaring, whispered voice,
crisp dialogue, ambient noise, environmental sound, beat-synced rhythm,
music tempo
```

### Beat-Sync Audio Technique
**Exact prompt pattern:** "Video rhythm references @Audio1. A street dancer moves through parking garage, hitting poses precisely on each beat drop."
**Method:** Upload an audio file as @Audio1 and explicitly tell the model to sync motion to it.

### Audio File Constraints
- Upload up to 3 audio files (15 seconds total, under 15MB each)
- Reference as `@Audio1` for background music, voice, or effects
- MP3 format supported

### Audio + Mood Shift Example
From the "cat revenge drama" prompt:
**Pattern:** "Calm piano before outfit change; classical music with beat sync after"
This demonstrates mood-driven audio transitions within a single generation.

### @levelsio Discovery
**Creator:** @levelsio
**Finding:** "What's interesting is how Seedance 2.0 lets you attach any type of media to your prompt -- like a reference photo of each actor, a pic of their clothes, an audio track of..." The multimodal input system treats audio as a creative direction channel alongside visual references.
- Source: [levelsio](https://x.com/levelsio/status/2021403820702552331)

### Phoneme-Level Lip Sync
Seedance 2.0 supports phoneme-level lip-sync in 8+ languages. This works natively without post-processing when dialogue is included in the prompt.

---

## 4. Style Anchor Discoveries

### Confirmed Working Style References
From multiple creator tests and the GitHub prompt libraries:

**Film Directors/Styles:**
| Reference | Effect |
|-----------|--------|
| "Denis Villeneuve Style, IMAX 70mm Film" | Epic scale, desaturated, gritty realism |
| "Wong Kar-wai, 90s Hong Kong Art Cinema" | Retro film feel, high ISO grain, emotional micro-expressions |
| "Christopher Nolan IMAX quality" | Large-format cinematic feel |
| "Wes Anderson symmetrical framing" | Precise compositional symmetry |
| "Blade Runner 2049 color grade" | Moody neon-meets-orange palette |
| "Hitchcock" | Suspense pacing and framing (Crystal tested Psycho shower scene) |

**Animation Styles:**
| Reference | Effect |
|-----------|--------|
| "Studio Ghibli watercolor" | Soft painted animation aesthetic |
| "Arcane Netflix cel-shading" | Bold graphic animation style |
| "Spider-Verse halftone comic style" | Comic book dots and graphic novel feel |
| "retro pixel art 16-bit" | Pixel art video game aesthetic |
| "Disney-style animation" | Classic Disney character animation |

**Photography/Film Stock:**
| Reference | Effect |
|-----------|--------|
| "Kodak Portra 400 film grain" | Warm, slightly desaturated analog look |
| "35mm anamorphic bokeh" | Oval bokeh, cinematic lens character |
| "Polaroid instant camera warm tones" | Vintage instant photo aesthetic |
| "infrared photography surreal palette" | False-color surreal look |
| "35mm Panavision lens" | Classic cinema lens characteristics |

### Arcane Style Transfer Discovery
**Creator:** @ProperPrompter
**Technique:** v2v style transferring with reference video + text prompt.
**Exact prompt:** "change every frame in the entire scene to match the art style of the arcane animation, style transfer"
**Method:** Upload a reference video, then use text to command style transfer to Arcane's aesthetic.
- Source: [ProperPrompter](https://x.com/ProperPrompter/status/2024135643350311256)

### Stop-Motion / Claymation Style Anchor
**Creator:** @AleRVG (AlexandrIA)
**Exact prompt:** "Hyperrealistic miniature diorama, stop-motion clay animation, handcrafted tactile materials, real fabric, professional studio animation style -- miniature bedroom, Friday night, clay figure stumbles through the door with enormous hollowed-out face..."
**Finding:** Stacking material descriptors ("handcrafted tactile materials, real fabric") strongly anchors the tactile/physical quality.
- Source: [AlexandrIA](https://x.com/AleRVG/status/2030344419560264015)

### Manga-to-Anime Discovery
**Creator:** @underwoodxie96
**Finding:** "WTF, I uploaded a screenshot from the One Piece manga and asked Seedance 2.0 to generate a video for me, and it actually worked!"
**Exact prompt:** "Video generated from reference text, with automatic coloring."
**Key:** The model can interpret black-and-white manga panels and auto-colorize + animate them.
- Source: [underwood](https://x.com/underwoodxie96/status/2020015660483649991)

### Old Prompts Now Work
**Creator:** @maxescu (Alex Patrascu)
**Finding:** "It's absolutely beautiful to see old prompts you kept in your database finally coming to life with Seedance 2.0. Seeing these prompts that never worked in any other models come to life flawlessly on the first try is enough to make me shed a tear of happiness."
**Implication:** Prompts that failed on Kling, Sora, Runway etc. may succeed on Seedance 2.0 without modification.
- Source: [Alex Patrascu](https://x.com/maxescu/status/2022287151623193067)

---

## 5. Transition & Effect Findings

### Multi-Shot in a Single Prompt
**Creator:** @bstuartTI (Brett Stuart)
**Finding:** "This is 1 detailed prompt with 5 cuts specified and a single starter image. That's it. It's time to start directing."
**Technique:** Specify multiple shots with explicit "cut" language in a single prompt. The model handles transitions natively.
- Source: [Brett Stuart](https://x.com/bstuartTI/status/2021299278455681206)

### "Shot Switch" / "Camera Switch" Language
**From prompt library documentation:**
Use "shot switch" or "camera switch" as explicit connectors between scenes. This is more reliable than "cut to" for multi-shot prompts.

**Example:**
```
Shot 1: Wide shot -- character enters dimly lit cafe, looking around curiously. Shot switch.
Shot 2: Medium shot -- sitting down, ordering coffee with warm smile. Shot switch.
Shot 3: Close-up -- eyes reacting to someone entering.
```

### "Cut to" Works for Simple Transitions
**Creator:** @janekm (Janek Mann)
**Exact prompt:** "fast action movie scene, hand-held camera, the woman notices the pilots have disappeared and races to take control of the plane, cut to outside shot showing her inside the cockpit at the controls"
**Finding:** Simple "cut to" language successfully transitions between interior and exterior shots.
- Source: [Janek Mann](https://x.com/janekm/status/2020888750285332526)

### First + Last Frame for Seamless Transitions
**Platform:** fal.ai
**Technique:** Seedance Pro supports first + last frame generation -- upload two keyframes and the model generates a smooth transition between them.
**Best for:** Ads, storyboards, cinematic flows.
- Source: [fal](https://x.com/fal/status/1972396802784502240)

### Video Extension / Continuation Prompts
**Seamless continuation pattern:**
```
Continue the scene naturally from where @Video1 ends. The character continues
walking forward through forest path. Camera maintains same tracking speed
and distance.
```

**Scene transition pattern:**
```
Continue @Video1 as character walks through doorway into completely new
environment -- from warm indoor cafe into rainy nighttime street. Maintain
character appearance and walking pace.
```

### Video Reference for Transition Style Cloning
**Creator:** @geesehowardt7
**Exact prompt:** "Refer to the camera movement in Video1 and the character's poses and actions..."
**Finding:** You can upload ANY video as a reference and the model will replicate its transition style, camera movements, and editing rhythm.
- Source: [geesehowardt7](https://x.com/geesehowardt7/status/2022958568820146686)

---

## 6. Speed/Pacing Control Tips

### "Slow Motion" = Quality Booster
**Creator:** @alex_prompter
**Finding:** "'Slow motion' = smoother, more controlled movement." This is not just a speed modifier -- it actually increases motion quality and reduces artifacts.
- Source: [Alex Prompter](https://x.com/alex_prompter/status/2025633828459389023)

### Degree Adverbs are MANDATORY for Motion Control
**From seedance2prompt.org:**
**Critical rule:** "Seedance 2 cannot infer motion intensity from an image. You must explicitly state it."

**Speed adverbs:** quickly, slowly, rapidly, leisurely, instantaneously
**Force adverbs:** powerfully, gently, forcefully, effortlessly, violently
**Rhythm adverbs:** vigorously, frantically, rhythmically, continuously, sporadically
**Scale adverbs:** dramatically, subtly, enormously, imperceptibly, sweepingly
**Quality adverbs:** smoothly, fluidly, mechanically, organically, gracefully

**Example transformation:**
- BAD: "walks" (generic, uncontrolled)
- GOOD: "walks briskly" (controlled intensity)

### Seedance Defaults to Slow-Mo Feel
**Creator:** @aaronadler
**Discovery:** When comparing Seedance vs Kling with the same first frame, "Kling's output feels realtime. Seedance output feels slow motion." The model has an inherent bias toward cinematic pacing.
**Implication:** If you want fast-paced/real-time feel, you need to explicitly specify speed with adverbs like "rapidly" or "at full speed."

### Speed Without Blur
**Creator:** @Dheepanratnam
**Finding:** "The sense of speed here without the background turning into a blur mess is the real win."
**Key:** Seedance 2.0 can render high-speed motion while keeping backgrounds sharp -- a common failure point for other models.
- Source: [Dheepan Ratnam](https://x.com/Dheepanratnam/status/2022593118055334090)

### BPM-Synced Motion
**From Emily2040 GitHub toolkit:**
**Pattern:** "Movement matches the 120 BPM music beat"
**Method:** Include context clues about music tempo to control motion rhythm. Combine with @Audio1 reference for precise sync.

### Duration Testing Strategy
**Rule:** "Start at 5 seconds while iterating prompts, then extend final version." This conserves credits during the refinement phase.

---

## 7. Color Grading Tricks

### Lighting & Atmosphere Vocabulary That Works

| Condition | Working Keywords |
|-----------|-----------------|
| **Golden Hour** | warm sunlight, long soft shadows, amber lens flare, backlit |
| **Moonlight** | cool blue tones, silver highlights, deep shadows, mysterious |
| **Candlelight** | warm flickering, dancing shadows, intimate glow, flame movement |
| **Neon** | pink/blue reflections, wet surfaces, urban night, rain-soaked |
| **Overcast** | soft diffused light, no harsh shadows, muted palette, even illumination |
| **Dramatic Rim** | strong outline light, dark background, high contrast, volumetric haze |
| **Dappled Forest** | sunlight through leaves, green-tinted ambient, canopy shadows |
| **Studio** | three-point lighting, clean key, soft fill, gradient backdrop |

### Film Stock References as Color Grade Anchors
- "Kodak Portra 400 film grain" = warm, desaturated analog
- "35mm anamorphic bokeh" = oval bokeh, cinematic character
- "Polaroid instant camera warm tones" = vintage warmth
- "infrared photography surreal palette" = false-color surreal

### Cinematic Grade Pattern
**Creator:** @ZaraIrahh (exact prompt excerpt)
**Working color description:** "IMAX film look with a 35mm Panavision lens. Low-saturation grey tones, compressed shadows with preserved detail, subtle film grain and edge vignetting. Heavy, oppressive atmosphere with realistic lighting and physical presence."
- Source: [Zara](https://x.com/ZaraIrahh/status/2036646067475722298)

### Wong Kar-wai Color Pattern
**From awesome-seedance GitHub:**
**Working style block:** "[Film Style]: 90s Hong Kong Art Cinema style, retro film feel, high ISO grain"
**Effect:** High-grain, emotionally saturated color with step-printing feel.

### Denis Villeneuve Desert Pattern
**From awesome-seedance GitHub:**
**Working style block:** "IMAX 70mm Film, Denis Villeneuve Style, Gritty Realism, Epic Scale, Desaturated"
**Effect:** Epic-scale, muted palette, monumental environmental cinematography.

### Neon Cyberpunk Full Prompt
**Creator:** @LudovicCreator
**Opening of prompt:** "A man in his early 30s, tan skin..." in a cyberpunk chase with "Neon lights. Wet pavement. Zero limits."
**Finding:** "Neon lights + wet pavement" as environmental combo reliably produces reflective rain-soaked cyberpunk look.
- Source: [LudovicCreator](https://x.com/LudovicCreator/status/2031086401610002631)

### Lighting with Narrative Purpose
**Creator:** @saniaspeaks_
**Exact prompt excerpt:** "A young teenage boy inside a dark mystical cave filled with stalactites and glowing blue crystals. The boy wearing a blue hoodie reaches out and touches a bright glowing crystal. Suddenly intense blue energy bursts out, lighting up..."
**Finding:** Describing light sources as part of the narrative (character touches crystal -> light burst) produces more natural-looking lighting transitions than specifying lighting technically.
- Source: [Sania](https://x.com/saniaspeaks_/status/2025726548330881425)

### Time Code + Environmental Light Changes
**From @Seedance_Pro account:**
**Pattern:** "0:03 mist rolls in, 0:07 eyes glance left, 0:12 neon buzz rises"
**Finding:** Embedding time-stamped environmental cues that include light changes creates more dynamic, evolving atmosphere.

---

## 8. Iterative Refinement Examples

### The One-Variable Rule
**From seedance2prompt.org:**
**Method:** "Don't rewrite the entire prompt if results aren't perfect. Change one element at a time. Seedance 2's speed lets you test 10 versions in 5 minutes."
**Priority fixing order:** If framing is wrong but action is correct -- fix camera first. Isolated variable changes prevent compounding errors.

### 200+ Video Iteration System
**Creator:** @Mho_23 (Miko)
**Process:** "i spent the last 24 hours generating over 200 seedance 2.0 videos to figure out the best prompting framework system for AI UGC"
**Result:** Developed a "v2 AI UGC prompting system" that produces videos needing zero editing.
**Key insight:** High-volume iteration with systematic framework development, not random prompting.
- Source: [Miko](https://x.com/Mho_23/status/2021310507584807389)

### Simple Prompt Produces Complex Results
**Creator:** @Mho_23 (Miko)
**Exact prompt:** "generate a review video on a restaurant from a menu i found online"
**Result:** Full AI UGC restaurant review video from a single sentence + menu image.
**Finding:** For UGC-style content, simpler prompts with clear intent outperform elaborate descriptions.
- Source: [Miko](https://x.com/Mho_23/status/2020492666538950832)

### Two-Line Prompt Achievement
**Creator:** @RuairiRobinson (professional filmmaker)
**Finding:** "This was a 2 line prompt in seedance 2. If the hollywood is cooked guys are right maybe the hollywood is cooked guys are cooked too idk."
**Key insight:** Short, well-crafted prompts can outperform long elaborate ones. Quality of instruction matters more than quantity.
- Source: [Ruairi Robinson](https://x.com/RuairiRobinson/status/2021394940757209134)

### First 20-30 Words Matter Most
**Creator:** @alex_prompter
**Finding:** "First 20-30 words carry the most weight. Put your subject there."
**Practical rule:** Front-load the most important information (subject, key action, style) in the opening of your prompt.
- Source: [Alex Prompter](https://x.com/alex_prompter/status/2025633828459389023)

### Start Short, Extend Later
**Creator:** @alex_prompter
**Method:** "Start with 5-10 second clips and lock one shot before expanding."
**Rationale:** This conserves credits and lets you validate your prompt approach before committing to longer generations.

### Prompt Length Sweet Spot
**From Emily2040 GitHub toolkit:**
- **30-100 words is the sweet spot** -- longer prompts degrade coherence
- Short prompts in Chinese outperform English equivalents (model was trained primarily on Chinese data)
- Use compression to enforce discipline

### Image-First Workflow
**Creator:** @chatcutapp
**Finding:** "You can improve Seedance 2.0's result drastically by using Nano Banana as a first prompt, and get a great image as a starting point."
**Method:** Generate a high-quality image first (via Seedream/Nano Banana), then use it as a reference frame for Seedance video generation.
- Source: [ChatCut](https://x.com/chatcutapp/status/2021659906827596262)

---

## 9. Multi-Clip Consistency Methods

### @Tag Identity Locking System
**From Emily2040 GitHub toolkit:**
- Assign @Tag identifiers to each character (e.g., @Hero, @Villain)
- Reference tags consistently in every shot prompt
- Use multi-character scene management to maintain consistent appearance, clothing, and positioning across cuts

### @Image Reference for Face Consistency
**From seedance2prompt.org:**
**Rule:** "Never switch reference images between shots. This prevents face drift, the most common consistency issue."
**Method:** Use identical @Image reference across all shots:
```
Reference @Image1 for the character's facial features and appearance
```
Include this line in every subsequent shot description.

### The Omni Reference System
**Creator:** @heydin_ai (Dinda Prasetyo)
**Finding:** "Seedance 2.0 with the Omni Reference feature honestly feels like a total game changer... for the first time, it genuinely feels like I'm directing."
**Method:** Upload multiple reference files and the model treats each as a specific creative direction:
- @Image for character appearance
- @Video for motion/camera reference
- @Audio for rhythm/music reference
**Limits:** Up to 9 reference images, 3 video clips (15s total), 3 audio clips.
- Source: [Dinda Prasetyo](https://x.com/heydin_ai/status/2028916615744749929)

### Agent Mode Auto-Assignment
**Creator:** @laszlogaal_
**Finding:** "Seedance 2.0 has an Agent mode where it takes Omni references, but the way it works it's so much more natural to use. You can throw images, videos, sounds, but you don't have to reference them specifically, the agent will try to figure it out and usually it works perfectly."
**Key:** In Agent mode, you don't need explicit @tags -- the model infers what each reference is for.
- Source: [Laszlo Gaal](https://x.com/laszlogaal_/status/2026247586395427261)

### Anime Consistency via Costume + Element Anchoring
**From awesome-seedance-2-prompts GitHub:**
**Method (Water vs Thunder Breathing Duel):**
- Divide 15-second sequence into timed segments [00:00-05], [05:10], [10:15]
- Anchor character identity through costume: "young samurai wearing green and black checkered haori"
- Anchor character identity through consistent elemental associations: "blue water dragon" for character A, "golden lightning" for character B

### Emotional State Tracking for Consistency
**From prompt library documentation:**
**Method:** Document mood shifts tied to specific seconds.
**Example (cat revenge drama):** heartbreak (rainy, 0-5s) -> transformation (elegant, 5-10s) -> triumph (ballroom, 10-15s)
The character remains consistent while emotions evolve through costume/environment changes.

### Character Sheet Pre-Generation
**Creator:** @madpencil_
**Method for consistent chibi anime characters:**
1. Make your character with Nano Banana 2, change hair style, eye colour, attire/costume
2. Make a character sheet (turnaround)
3. Use the character sheet as reference in Seedance for all clips
- Source: [madpencil_](https://x.com/madpencil_/status/2030563167240081567)

---

## 10. Platform-Specific Differences

### Dreamina (Official Platform)
- **URL:** dreamina.capcut.com
- **Pros:** Full Omni Reference support, all features unlocked, direct ByteDance integration
- **Cons:** Strict content filtering (getting stricter over time), originally China-only (VPN needed), 2-10 hour queue times during peak
- **Limits:** 9 reference images, 3 videos (15s total), 3 audio files, output up to 15 seconds
- Source: [Dreamina AI](https://x.com/dreamina_ai/status/2036292154671374493)

### CapCut (Official Partner)
- **Features:** Dreamina Seedance 2.0 integrated into CapCut app, desktop, and web
- **New Feature:** CapCut Video Studio -- a timeline-free, canvas-based AI production workspace
- **Access Points:** Quick try (AI Lab & AI Generator in app), Generate + edit workflow (Media -> AI Video), Video Studio (web)
- **Availability:** Rolling out in Indonesia, Philippines, Thailand, Vietnam, Malaysia, Brazil, Mexico first
- Source: [CapCut](https://x.com/capcutapp/status/2036202286809227635)

### Topview (@TopviewAIhq)
- **Features:** Seedance 2.0 with Image to Video, Text to Video, Omnireference
- **Pricing:** 365 days of unlimited use offered
- **Popular with:** @Artedeingenio (OscarAI) uses this as primary platform
- Source: [OscarAI](https://x.com/Artedeingenio/status/2036099957870977363)

### Yapper (@yapper_so)
- **Features:** Seedance 2.0 Live access, AI creative studio
- **Notable:** Shared a "200 IQ method" for making Seedance 2.0 videos actually generate (filter workarounds)
- Source: [Yapper](https://x.com/yapper_so/status/2030778186594922565)

### Open-Higgsfield-AI (Open Source)
- **Features:** Free with BYOK (Bring Your Own Key), open-source, no subscription
- **Notable:** "First in the world to integrate Seedance 2.0" per @matchaman11
- **Extra Features:** Character swapping in clips, video editing, infinite variations from one video
- Source: [Anil Chandra](https://x.com/matchaman11/status/2028438646886441247)

### BytePlus (API Access)
- **Features:** Seedream available in "Playground" with rate limits for free signups
- **Note:** Reference generation was not live at time of report, only first/last frame mode
- Source: [karim_yourself](https://x.com/karim_yourself/status/2021294776880943198)

### Platform Choice Summary
| Need | Best Platform |
|------|--------------|
| Full feature access | Dreamina |
| Integrated editing workflow | CapCut |
| Unlimited generation | Topview |
| Open source / BYOK | Open-Higgsfield-AI |
| Filter flexibility | Yapper (reported less strict) |
| API integration | BytePlus |

---

## Appendix A: Full Prompt Examples from Creators

### Racing Movie Multi-Shot (by @johnAGI168)
```
Style: Hollywood Professional Racing Movie (Le Mans Style), Cinematic Night,
Rain, High Stakes Sport.
Duration: 15s.
[00-05s] Shot 1: The Veteran (Interior/Close-up). Rain lashes the windshield
of a high-tech race car on a track. The veteran driver in helmet looks calm
and focused. Dashboard lights reflect on his visor.
```
- Source: [John](https://x.com/johnAGI168/status/2020515830874636716)

### Surreal Ronin Action (by @Dheepanratnam)
```
A surreal battlefield in the sky: floating rock islands drifting through a
thunderstorm, clouds swirling below like an ocean. The masked ronin dashes
across the drifting platforms, pursued by a colossal winged beast whose chest
is a swirling vortex of storm clouds and lightning. The camera hurtles from
island to island, struggling to keep up as rocks tilt, spin, and crumble away
beneath them. Every wingbeat sends shockwaves through the air, shaking the
frame and blowing debris and rain straight into the viewer's face. Rapid
handheld cuts capture the ronin leaping impossible gaps, sword carving arcs
of light that briefly cut through the darkness.
```
- Source: [Dheepan Ratnam](https://x.com/Dheepanratnam/status/2021689626092589532)

### Macro Cinematic 6-Shot Structure (by @Dheepanratnam)
```
FORMAT: 15s / 6 SHOTS / single continuous chase energy / no dialogue
STYLE: Macro jungle floor, towering grass blades, dew drops, damp earth vs
neon pink cyber-implants, photorealistic macro cinematic

Shot 01 (0:00-0:02): Dive from the canopy of a giant fern down to a
cybernetically enhanced rhinoceros beetle sprinting across a fallen,
moss-covered log.

Shot 02 (0:02-0:04): Camera tracks parallel to the beetle's mechanical legs,
sweeps under its glowing pink thorax, and snaps to the spinning micro-rotors
on its back.

Shot 03 (0:04-0:07): A heavy rain droplet dislodges a pebble from above;
the beetle initiates a thruster-assisted sidestep, scraping its metallic horn
against a fungal stalk.

Shot 04 (0:07-0:10): The path dives into a dense thicket of thorny briars,
spiderwebs, and overlapping leaves; the camera seamlessly navigates the
micro-labyrinth.
```
- Source: [Dheepan Ratnam](https://x.com/Dheepanratnam/status/2036576414418305172)

### Cinematic Portrait (from seedance2prompt.org)
```
A young woman with flowing auburn hair slowly raises her gaze toward the
camera. Soft golden hour light casts warm shadows across her face. A gentle
breeze moves strands of hair. Slow dolly-in from medium shot to close-up.
Cinematic film grain, shallow depth of field, warm amber tones.
```

### Product Showcase (from seedance2prompt.org)
```
A luxury watch rotating slowly on a black marble surface. Light rays catch
polished steel bezel, creating sparkle reflections. Extreme close-up macro
shot with smooth 360-degree orbit. Studio lighting with soft gradient
background. High-end commercial photography style, crisp details.
```

### Water vs Thunder Breathing Duel (from awesome-seedance-2-prompts)
```
[00:00-05] Young samurai wearing green and black checkered haori, lowering
his center of gravity, blue water dragon condensed from high-pressure water flow.
[05:10] Second warrior unleashes golden lightning counterattack.
[10:15] Final clash. Hollywood live-action anime adaptation film quality, 4K.
```

### IMAX Apocalyptic Character (by @ZaraIrahh)
```
Character & Setup: Full-body based on reference image (upper-body reference),
with face, hairstyle, and features matched exactly. She wears a hat.
Expression is tense and restrained, slightly painful, with a faint frown --
carrying a strong sense of despair and intensity in his eyes.
Clothing: Dark grey coat, dark inner layer, no belt, wearing heavy black-tech
gauntlets.
Environment: Apocalyptic wasteland, grey-blue sky, strong winds, smoke and
debris in the air. Meteors streak across the sky with faint flames and trails
of smoke.
IMAX film look with a 35mm Panavision lens. Low-saturation grey tones,
compressed shadows with preserved detail, subtle film grain and edge
vignetting. Heavy, oppressive atmosphere with realistic lighting and physical
presence. One continuous handheld shot with subtle breathing motion.
```
- Source: [Zara](https://x.com/ZaraIrahh/status/2036646067475722298)

### Simple Restaurant UGC (by @Mho_23)
```
generate a review video on a restaurant from a menu i found online
```
(Plus uploaded menu image as reference. Produced full UGC review video.)
- Source: [Miko](https://x.com/Mho_23/status/2020492666538950832)

### Anime Tournament of Power (by @NACHOS2D_)
```
A massive cosmic arena forms in a blinding void, Tournament-of-Power scale.
Crowds from countless universes roar. At the center stands the narrator:
Gintoki Sakata, relaxed, wooden sword on his shoulder, bored eyes, sharp
tongue. He announces the rules casually, almost mocking fate: 'This tournament
decides the strongest. Winner gets a harem.' Beat. The crowd explodes.
Gintoki sighs. 'Yeah, yeah. Don't look at me like that. I didn't write the
rules.'
```
- Source: [nachos2d](https://x.com/NACHOS2D_/status/2021295886978908547)

---

## Appendix B: The 6-Dimension Prompt Framework

From the seedance-2-prompt-library GitHub, the most effective prompt structure uses 6 dimensions:

1. **Input** -- `@image`, `@video`, `@audio` tags referencing uploaded assets
2. **Content** -- Narrative core: character, environment, action, mood
3. **Style** -- Visual aesthetics, lighting, color tone, texture, atmosphere, music
4. **Camera** -- Shot composition, angles, movements (specific mechanics, not adjectives)
5. **Structure** -- Timeline breakdowns: "0-3s:", "3-6s:", "6-9s:" with segment transitions
6. **Edit** -- Modification requests: Extend, Partial Edit, Replace, Re-Plot

### Content Layer Pattern
```
[Style]. [Character] in [Environment] is [Action]. [Character] with [Emotion]
says '[Lines]'. Background is [Sound Effects].
```

### Asset Tagging Format
```
@Image1 as first frame, @Video1 for camera movement, @Audio1 for background music
```

---

## Appendix C: Kimi K2.5 + Seedance Workflow

**Creator:** @crystalsssup (Crystal)
**Discovery:** "Kimi K2.5 + Seedance 2 is a perfect workflow."
**Process:**
1. One prompt to Kimi K2.5 generates a full Excel storyboard with images and prompts
2. Kimi splits the task into 3 stages: detailed storyboard breakdown, preview images for each shot, compiled Excel with embedded images
3. Take the generated storyboard directly into Seedance for video production
**Test case:** Hitchcock's Psycho iconic shower scene
**Build time:** 2 minutes for complete storyboard
- Source: [Crystal](https://x.com/crystalsssup/status/2021149326290956353)

---

## Appendix D: Key Creator Accounts to Follow

| Account | Specialty |
|---------|-----------|
| @Dheepanratnam | Physics tests, A/B comparisons, cinematic prompts |
| @gavinpurcell | Creative experimentation, multi-output variance testing |
| @alex_prompter | Practical tips, prompt optimization rules |
| @ProperPrompter | Style transfer, v2v techniques |
| @Mho_23 (Miko) | UGC prompting frameworks, high-volume iteration |
| @heydin_ai (Dinda Prasetyo) | Omni Reference, AI directing techniques |
| @TheoMediaAI | Honest failure documentation, artifact spotting |
| @ClonizerAi | Content filter workarounds, community guides |
| @javilopen (Javi Lopez) | Nerfing documentation, filter tracking |
| @laszlogaal_ | Agent mode discovery, Omni Reference |
| @LudovicCreator | Cyberpunk aesthetics, neon prompts |
| @ZaraIrahh | IMAX/cinematic character prompts |
| @AleRVG (AlexandrIA) | Stop-motion/claymation style |
| @crystalsssup (Crystal) | Kimi + Seedance workflow |
| @Artedeingenio (OscarAI) | Topview platform, cyberpunk anime via Omni Reference |
| @bstuartTI (Brett Stuart) | Multi-cut single-prompt directing |
| @madpencil_ | Character sheet workflow for consistency |

---

## Appendix E: Common Mistakes Quick Reference

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Using negative prompts ("no blur") | Model ignores negatives entirely | Use positive: "sharp focus, crisp details" |
| Describing image contents in I2V mode | Creates prompt/image conflict | Describe ONLY motion and camera |
| Multiple style adjectives | Style inconsistency | Single anchor: "Blade Runner grade" |
| Vague camera ("cinematic feel") | Camera goes random | Specific mechanic: "slow dolly-in" |
| Multiple camera moves per shot | Camera haywire | One motion verb per beat |
| Switching @Image refs between shots | Face drift / morphing | Same @Image1 in every shot |
| Complex character descriptions (no ref image) | Deformation | Simplify to one noun + @Image1 |
| Prompt over 100 words | Coherence degrades | Keep 30-100 words sweet spot |
| Not specifying motion intensity | Flat/unpredictable motion | Add degree adverbs: "briskly", "gently" |
| Re-submitting once after filter block | Wasted time | Try exact same prompt twice (often passes 2nd time) |
| Testing at full 15s duration | Wasted credits | Start at 5s, extend when prompt is locked |
| Using trigger words (fight, kill, gun) | Content filter blocks | Use euphemisms: "dramatic energy clash" |
