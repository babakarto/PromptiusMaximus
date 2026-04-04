# Seedance 2.0 - Advanced Vocabulary & Techniques (YouTube Deep Research)

> **Research Date:** 2026-03-28
> **Sources:** 12+ YouTube video transcripts analyzed (CyberJungle, Lennard Smith, Noble Goose, Tao Prompts, Yaroflasher, Bob Doyle Media, ComfyUI Workflow Blog, Vortex, Benji's AI Playground, AI Video School, Dom the AI Tutor, John Savage AI)
> **Focus:** Exact terms, vocabulary, syntax, and tested techniques -- NOT general advice

---

## 1. Audio Prompt Engineering (Exact Terms That Work)

### Audio Description Syntax
Seedance generates audio natively from text descriptions in the prompt. Audio is NOT a separate parameter -- it is embedded inline in the video prompt text.

**Working Pattern:** Describe sounds as part of the scene, not as technical instructions.

#### Dialogue Syntax (Tested & Working)
```
"she says: [dialogue text here]"
"car replies: [dialogue text here]"
"he whispers: [dialogue text here]"
```
- Use `[character] says:` followed by the spoken line (Source: CyberJungle)
- For non-human speakers: `car replies:` or `AI responds:` (Source: CyberJungle)
- Can switch languages mid-prompt: write dialogue in Chinese, then switch back to English -- model handles it (Source: CyberJungle)

#### Micro-Gesture Audio Cues (Tested & Working)
Embed physical/emotional beats INSIDE the spoken sentence to make dialogue realistic:
```
"she takes a breath, she looks confused, she looks around"
```
These "audio cues" inserted between dialogue lines make performances "extremely realistic and lifelike" (Source: CyberJungle)

#### Environmental Sound Terms That Work
| Term | What It Generates |
|------|------------------|
| `boots on grass` | Footstep sounds matching surface |
| `ball thud` | Impact sound synced to visual contact |
| `crowd murmur` | Low ambient crowd noise |
| `crowd swell` | Building crowd excitement |
| `crowd gasp` | Sharp collective intake |
| `crowd eruption` | Full celebration roar |
| `metallic clink of a coin hitting stone` | Specific foley effect |
| `fabric rustles softly` | Cloth movement sound |
| `tiny footsteps` | Small/light step sounds synced to motion |
| `buttons click` | Small mechanical sounds |
| `engines rev in the distance` | Spatial audio placement |
| `footsteps echo across polished floors` | Reverb-aware spatial audio |
| `doors close with a solid thump` | Impact foley |
| `indicators click` | Car indicator sound |
| `glass touches the table` | Precise foley synced to visual |
| `soft rhythmic pulses synced to jellyfish movement` | Abstract ambient sound |
| `steady breathing` | Character breath sounds |
| `deep breathing` | Heavy/dramatic breath |
| `rain` / `thunder` | Weather ambience |
| `acoustic guitar` | Instrument-specific music |
| `heartbeat` | Dramatic tension audio |

#### Music Control Terms
| Term | Effect |
|------|--------|
| `no music` | Suppresses background music generation (RECOMMENDED: add to ALL prompts, then add your own music in post) |
| `soft background music` | Low-level ambient score |
| `subtle background music` | Similar, very low presence |
| `powerful vocal climax` | Musical peak moment |
| `completely silent and quiet` | Full audio suppression |

#### Negative Audio Prompting (Tested)
```
"no gunshots, no clicking, no trigger"
"completely silent and quiet"
```
This is how you REMOVE unwanted sounds. Standard negative prompting syntax works for audio. (Source: Tao Prompts)

#### Audio Quality Insight
- Seedance generates audio that is "locked to the visuals at generation time" -- not added in post (Source: Vortex)
- Lip sync works across languages: English, Japanese, Korean, Spanish, Indonesian, Portuguese tested (Source: Vortex)
- Acoustics of environment are respected (reverb in rooms, etc.) (Source: Bob Doyle Media)
- Seedance audio is described as closest competitor to Veo 3.1 for audio quality (Source: CyberJungle)

---

## 2. Style Anchors Library (Tested References)

### What "Anchors" Are (Exact Definition)
An **anchor** is a prompt element that reminds the AI of visual details it cannot see or might forget during generation. Without anchors, the model will "transform" visual elements it considers unimportant. (Source: Tao Prompts)

### Anchor Syntax (Tested Examples)
| Anchor Type | Example Prompt Fragment | What It Preserves |
|-------------|----------------------|-------------------|
| Physical appearance | `"red embers and ash on him"` | Prevents model from cleaning up character during emotion change |
| Spatial relationship | `"the orc should be on the back riding the direwolf"` | Maintains character-mount relationship |
| Asymmetric detail | `"no armor on the right shoulder, dark blue geometric tribal tattoos on the orc's shoulder"` | Preserves off-screen details when camera reveals new angle |
| Clothing detail | `"maintaining face and clothing consistency"` | General consistency anchor |

### Style Vocabulary That Seedance Recognizes

#### Photorealism Terms
| Term | Effect |
|------|--------|
| `photorealistic` | Base realism flag |
| `lifelike` | Similar to photorealistic |
| `live-action` | Film-camera aesthetic |
| `cinematic texture` | Film-like visual quality |
| `film grain` | Adds organic noise (post-processing feel) |
| `hyperrealistic` | Maximum realism push |
| `high-fidelity video production` | Combined quality flag |

#### Genre/Aesthetic References
| Term | Effect |
|------|--------|
| `Hollywood live-action blockbuster style` | High-budget action aesthetic |
| `dystopian future` | Dark sci-fi environments |
| `steampunk` | Victorian-industrial aesthetic |
| `cyberpunk` | Neon-lit futuristic |
| `anime` | Japanese animation style |
| `surrealism` | Dream-logic compositions |
| `sci-fi` | Science fiction general |
| `high-end social campaign` | Polished brand-commercial look |
| `brand film` | Corporate cinematic aesthetic |
| `3D digital animation` | Animated/rendered look |
| `cartoonish` | Simplified stylized look |
| `documentary style` | Handheld, raw, observational |
| `vlogger style` | POV, handheld, casual |
| `high budget CGI cutscene` | Game/film VFX look |
| `game cutscene` | Video game cinematic |
| `iPhone vibe` | Consumer-camera casual aesthetic |

#### Quality Suffix (Add to EVERY Prompt)
```
"4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture"
```
This is the recommended "quality suffix" to append to all prompts (Source: Noble Goose)

#### Constraint Suffix (Add to EVERY Prompt)
```
"maintaining face and clothing consistency, without distortion or high detail, generate the video without subtitles"
```
(Source: Noble Goose)

### Reference Libraries Seedance Understands
- **Midjourney mood boards** can be used as visual style references fed into Seedance via image input
- **Specific breeds, brands, coordinates, historical moments** are understood when using image references generated from Nano Banana 2 (which browses the web for visual accuracy)
- The model recognizes cinematic conventions from film/photography but NO specific filmmaker or photographer names were confirmed as working style anchors in the transcripts reviewed

---

## 3. Transition & Effect Vocabulary

### Multi-Shot Prompting (The Core Seedance 2.0 Feature)

#### Method 1: Multi-Shot Shortcut (Director Mode)
```
"Change camera angle every 2 seconds. Alternate between wide shot, closeup, show details, show high angle and low angle."
```
This tells the model to BE the director and handle cuts automatically. (Source: CyberJungle)

#### Method 2: Detailed Multi-Shot Design (Manual Control)
Label each shot explicitly:
```
Shot 1: [action] [camera] [audio]
Shot 2: [action] [camera] [audio]
Shot 3: [action] [camera] [audio]
```
Or with timestamps:
```
0-3s: [camera zooms in towards him]
3-5s: [camera tilts down to show recording device]
5-8s: [camera tilts back up to see him looking at sky]
```
(Source: Tao Prompts, Noble Goose)

#### Method 3: Shot Switch Keyword
```
"shot switch"
```
Type this exact phrase where you want a camera cut. Used on FL.AI and other platforms hosting Seedance. (Source: Yaroflasher)

#### Method 4: Cut-To Prompting
```
"The astronaut turns and walks towards a spaceship. Cut to the boots of the astronaut walking along the terrain inside a cinematic film."
```
Use `Cut to` to define scene transitions. (Source: Tao Prompts)

**WARNING:** If the cut-to scene is too visually different from the original, style consistency breaks. Keep cuts within the same visual universe. (Source: Tao Prompts)

### Transition Terms
| Term | What Happens |
|------|-------------|
| `shot switch` | Hard camera cut between angles |
| `Cut to` | Scene transition to new angle/subject |
| `smooth transitions` | Model blends between shots instead of hard cuts |
| `The environment subtly transforms` | Morphing/transition within a continuous shot |
| `tree bark becomes smooth stone` | In-shot material transformation |
| `whip pan` | Fast violent camera rotation with motion blur |
| `rack focus` | Focus shifts from foreground subject to background (or reverse) |
| `reveal from blur fade in` | Starts out of focus, pulls to sharp |

### VFX/Effect Terms
| Term | Effect |
|------|--------|
| `transformation scene with flying metallic parts` | Object transformation VFX |
| `holographic star map` | Sci-fi HUD/hologram elements |
| `lights reflect softly through transparent displays` | Translucent UI elements |
| `mist drifts slowly` | Atmospheric particle effects |
| `lantern flames flicker gently` | Fire simulation |
| `dust floating in the light beam` | Particle/atmosphere effects |
| `sparks` | Impact/grind spark effects |
| `explosions` | Pyrotechnic VFX |
| `glowing swords` | Weapon effects |

---

## 4. Speed/Pacing Control Language

### Tested Speed/Timing Terms
| Term | Effect |
|------|--------|
| `slow dolly in` | Gradual camera approach |
| `fast dolly in` (also: `rush`) | Rapid camera approach, sense of urgency |
| `slowly becomes active` | Gradual character movement |
| `the camera slowly pushes in` | Gradual forward camera movement |
| `slowly scoops up` | Gentle, measured character action |
| `near stillness` | Minimal movement, atmospheric |
| `extreme rapid zoom` (also: `snap zoom`, `crash zoom`) | Sudden fast zoom to subject |
| `fast 360 orbit` (also: `spin`) | Rapid full-circle camera rotation |
| `slow cinematic arc` | Gentle curved camera movement |
| `violently` (in `camera whips violently to the left`) | Aggressive, fast camera motion |
| `gentle wide curve` | Slow orbital camera path |

### Time-Lapse Terms
| Term | Effect |
|------|--------|
| `time-lapse` | Accelerated time passage (tested in Midjourney animate, applicable concept) |

### Duration Control
- 15 seconds is the standard Seedance clip length for multi-shot sequences
- **Critical:** "If you write too much spoken words, some dialogue will be missed out and everything will be rushed" -- calibrate dialogue to 15-second clip window (Source: CyberJungle)
- On some platforms: 5-second, 12-second, and 15-second options available
- LTX 2.3 comparison: up to 26 seconds tested

### Pacing Through Shot Escalation
A tested technique: escalate shot size to control emotional pacing:
```
Shot 1: Wide (context - tells us WHERE we are)
Shot 2: Medium (action - shows WHAT is happening)
Shot 3: Close-up (emotion - tells us HOW it feels)
```
"This is a classic filmmaking technique that Seedance does so well." (Source: Noble Goose)

---

## 5. Color Grading Terms

### Color/Lighting Vocabulary That Works
| Term | Visual Effect |
|------|--------------|
| `warm afternoon sunlight` | Golden-hour warm tones |
| `dusk` | Twilight atmospheric lighting |
| `balanced lighting` | Even, neutral exposure |
| `at sunrise` | Dawn lighting, warm horizons |
| `during a rainstorm` | Overcast, moody, wet reflections |
| `pink tunnel` | Colored environment lighting |
| `neon signs` | Artificial colored light sources |
| `soft rhythmic lighting` | Animated/pulsing light |
| `light beam` | Directional light shaft |
| `lantern flames` | Warm point-light sources |

### Post-Processing Color Terms
| Term | When to Use |
|------|------------|
| `film grain` | Add in prompt for organic texture; also add in post-production |
| `cinematic texture` | Film-camera color science feel |
| `color correction` | Apply in DaVinci Resolve/Premiere post, not in prompt |
| `color grade` | Mentioned as something to fix in post between shots -- NOT a reliable prompt term |

### Practical Color Workflow
- Seedance does NOT have explicit color grading parameters
- Color consistency between shots is NOT guaranteed -- "the color grade isn't perfect between all of the shots" (Source: Lennard Smith)
- Best practice: do color grading in post-production (DaVinci Resolve recommended as free option)
- Adding `film grain` in post "always gives the video a more realistic feel" (Source: Yaroflasher)
- For hyperrealism: Magnific upscaler settings: `detail 30-50%, grain 20-30%, sharpen 5-10%` (Source: Yaroflasher)

---

## 6. Common Failures & Fixes

### FAILURE: Jelly/Morphing Background
**Symptom:** Background moves like jello, warps unnaturally
**Fix:** Add negative constraints at end of prompt:
```
"No warping, no morphing, tripod, stable camera, static background"
```
(Source: ComfyUI Workflow Blog)

### FAILURE: Mechanical Actions (Foot Pedals, Grinding, Complex Tools)
**Symptom:** Characters operating machinery look wrong -- wheels spin wrong direction, feet don't pedal
**Fix:**
1. Simplify the prompt -- remove the complex mechanical interaction
2. Add visual cues to the INPUT IMAGE (e.g., add sparks to a grinder image in Photoshop so the model understands what's happening)
3. Regenerate multiple times and select best take
(Source: Lennard Smith)

### FAILURE: Background Inconsistency Across Angles
**Symptom:** Side angles lose background elements (e.g., giant rib bones disappear)
**Fix:**
1. Run the same prompt multiple times
2. Mix and match shots from different generations
3. Photoshop fix the input image to make background elements more prominent
(Source: Lennard Smith)

### FAILURE: Face Changes on Camera Angle Shift
**Symptom:** Character face changes when camera reveals new angle the model hasn't seen
**Fix:**
1. Provide character reference images (full body, close-up, side view, back view)
2. Use Seedance multi-reference mode with character sheet
3. Use anchor prompts describing off-screen features
(Source: Lennard Smith, Tao Prompts)

### FAILURE: Dialog Timing Mismatch
**Symptom:** Dialog waits until last seconds of clip, then gets cut off
**Fix:**
1. Keep dialogue SHORT relative to clip duration
2. Calibrate: ~2-3 sentences max per 15-second clip
3. Run multiple generations -- usually one will nail timing
(Source: Lennard Smith)

### FAILURE: Censorship Blocking (Faces, Violence, IP)
**Symptom:** Prompts flagged as sensitive; faces blocked; fight scenes rejected
**Known Restrictions:**
- Celebrity faces: almost impossible
- Known IP characters: blocked
- `kill` keyword: flagged (even `finish` as substitute gets flagged)
- Hostage scenarios: blocked
- Blood/violence: heavily restricted
- Katana fight scenes: "very difficult to generate, constantly flagged for violence"
**Workarounds:**
- Use non-human characters for action scenes
- Avoid weapon-specific keywords
- Use platforms with fewer restrictions (varies by endpoint)
(Source: CyberJungle, Lennard Smith)

### FAILURE: Armor/Clothing Symmetry Error
**Symptom:** Model assumes symmetry -- if left shoulder has armor, right shoulder gets armor too
**Fix:** Anchor prompt describing what the OTHER side looks like:
```
"no armor on the right shoulder, dark blue geometric tribal tattoos on the orc's shoulder"
```
(Source: Tao Prompts)

### FAILURE: Crowd Animation
**Symptom:** Multiple people all move identically, or blur into blobs
**Fix:** Don't prompt for crowds performing actions. Instead:
- Have crowd be static/staring
- Focus action on single character
- Use words like "eerie silence" instead of "crowd shouting"
(Source: Tao Prompts)

### FAILURE: Visual Style Shift During Emotion Change
**Symptom:** Asking character to smile/change expression causes entire visual style to transform
**Fix:** Anchor the physical appearance:
```
"the character smiles, red embers and ash on his face"
```
Explicitly re-state visual elements alongside the emotion. (Source: Tao Prompts)

### FAILURE: 720p Resolution Limitation
**Symptom:** Seedance outputs at 720p -- looks softer than Kling's 1080p
**Fix:**
1. Take still frame from Seedance output
2. Upscale and sharpen with Nano Banana Pro / Topaz Video / Magnific
3. Optionally re-run upscaled still through Kling for polished 1080p version
4. Upscale to 4K using Topaz Video for final output
(Source: Lennard Smith)

### FAILURE: Text on Signs/Neon Morphs
**Symptom:** Background text on neon signs morphs and distorts
**Status:** Known limitation, no reliable fix. Close-up shots reduce this. (Source: ComfyUI Workflow Blog)

---

## 7. A/B Test Results

### Seedance 2.0 vs Kling 3.0 (Same Prompts, Same Start Frames)

| Category | Winner | Notes |
|----------|--------|-------|
| Character consistency | **Seedance 2.0** | "Much superior model... character consistency, control" |
| Action/fight scenes | **Seedance 2.0** | "Until Seedance 2.0, any video model isn't great at fight scenes" |
| Complex motion physics | **Seedance 2.0** | Handles sword fights, complex interactions |
| Cinematic camera movement | **Seedance 2.0** | "Dynamic cinematic camera management" |
| Dialogue performance nuance | **Kling 3.0** (slight edge) | Both good; Kling 3.0 "more nuanced and subtle performances" |
| Resolution quality | **Kling 3.0** | 1080p vs Seedance 720p |
| Native audio naturalness | **Seedance 2.0** | "Integrated native audio more natural and more accurate" |
| Sound effects accuracy | **Seedance 2.0** | "Action shots the sound effects feel really accurate and cinematic" |
| Prompt coherence | **Seedance 2.0** | "Superior prompt coherence, fewer unexpected results" |
| Multi-camera shots | **Seedance 2.0** | Built-in multi-shot system is superior |
| Direction of movement | **Kling 3.0** | Seedance sometimes "confuses direction of movement" -- cars going backwards |

(Source: CyberJungle - "Seedance 2.0 DESTROYS Kling 3.0?")

### Seedance 2.0 vs LTX 2.3 (Same Prompts)

| Category | Winner | Notes |
|----------|--------|-------|
| Close-up shots (single character, low action) | **Tie** | "Visual quality is identical" side by side |
| Complex action (samurai cats fighting) | **Seedance 2.0** | "LTX 2.3 fails completely, physics are bad, structure falls apart" |
| Audio (close-up dialogue) | **LTX 2.3** | "Beautiful cinematic audio, rain, deep breathing, thunder perfectly" |
| Audio (music/score addition) | **Seedance 2.0** | "Even adds matching background music" |
| Local/free generation | **LTX 2.3** | Runs locally on consumer hardware |
| Vertical video | **LTX 2.3** | Native 9:16 support |

**LTX 2.3 Rule:** "When you ask for heavy action and complex motion, LTX 2.3 will fail. But if you use close-up scenes with low action and only one main character, you'll get a perfect result every time." (Source: ComfyUI Workflow Blog)

### Seedance for Dialogue: Kling 3.0 vs Seedance 2.0 Mixing Strategy
In the "Bone Throne" short film:
- **Kling 3.0** was used for Kael's dialogue performance
- **Seedance 2.0** was used for Luca's dialogue performance
- Creator picked "whichever gave the best performance" per character
- Both models were run on the SAME prompt and best takes were cherry-picked

(Source: Lennard Smith)

### Generation Success Rate
- Seedance 2.0: "almost all the footage only took one or two generations to get right" (Source: Benji's AI Playground)
- Fight scenes: required running "same prompt over and over" and mixing takes
- Complex mechanical actions: 5-10+ generations typical
- Simple dialogue: 2-3 generations to get good timing

### Cost Comparison (Real Production)
For a 5-minute short film (370 generations, 100 final shots, 9 days):
- Higgsfield + Kling subscriptions: ~$270
- Extra Kling credits: ~$50 used of $200 purchased
- Seedance credits: $200 (across two $100 purchases)
- Total production cost: ~$577-$817 depending on counting method
(Source: Lennard Smith)

---

## 8. Master Prompt Formula (Compiled from All Sources)

### Noble Goose Formula (Most Complete)
```
Subject + Action + Scene + Camera + Lighting + Style + Audio + Quality Suffix + Constraints
```

### Exact Quality Suffix (Copy-Paste Ready)
```
4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture
```

### Exact Constraint Suffix (Copy-Paste Ready)
```
maintaining face and clothing consistency, without distortion, generate the video without subtitles
```

### Anti-Jelly Suffix (Copy-Paste Ready)
```
no warping, no morphing, tripod, stable camera, static background
```

### Full Template (Easy - Single Shot)
```
[image 1 as first frame]. A [subject description] [action verb + details]. [Camera movement type]. [Lighting description]. [Style description with film grain/cinematic texture]. [Audio: specific sound effects]. 4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture. Maintaining face and clothing consistency, without distortion, generate the video without subtitles. No music.
```

### Full Template (Advanced - Multi-Shot)
```
[image 1 as first frame, image 2 as last frame].

Shot 1 (0-3s): [Camera: tracking shot moving backwards]. [Action: character receives pass]. [Audio: boots on grass, ball thud].

Shot 2 (3-6s): [Camera: low angle wide, whip pan]. [Action: direction change, dribbles past defender]. [Audio: crowd swell, ball crack].

Shot 3 (6-9s): [Camera: tight side tracking with slight orbit]. [Action: nutmegs defender]. [Audio: crowd gasp].

Shot 4 (9-12s): [Camera: close-up, rack focus from face to goalkeeper]. [Action: prepares to strike]. [Audio: heartbeat].

Shot 5 (12-15s): [Camera: dolly in following ball]. [Action: ball hits back of net]. [Audio: crowd eruption].

4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture. Maintaining face and clothing consistency, without distortion, generate the video without subtitles. No music.
```

---

## 9. Camera Movement Dictionary (38 Tested Terms)

### Dolly Moves
| Prompt Term | Description |
|-------------|-------------|
| `slow dolly in` | Camera approaches subject gradually |
| `slow dolly out` | Camera retreats from subject gradually |
| `fast dolly in` / `rush` | Rapid approach, creates urgency |
| `vertigo effect` / `zolly` | Camera moves backward while lens zooms in |

### Scale/Zoom
| Prompt Term | Description |
|-------------|-------------|
| `extreme macro zoom` | Face/body to microscopic detail |
| `cosmic hyper zoom` | Space to street continuous zoom |
| `smooth optical zoom in` | Standard zoom toward subject |
| `smooth optical zoom out` | Standard zoom away from subject |
| `snap zoom` / `crash zoom` | Sudden rapid zoom to subject's eyes |

### Character-Mounted Framing
| Prompt Term | Description |
|-------------|-------------|
| `over the shoulder` / `OTS shot` | Camera behind one character looking at another |
| `fisheye` / `peephole lens` | Extreme wide-angle distortion |

### Environmental Interaction
| Prompt Term | Description |
|-------------|-------------|
| `reveal from behind` / `wipe movement` | Camera starts blocked by foreground, slides to reveal |
| `through shot` / `fly through aperture` | Camera passes through window/opening |

### Focus/Lens
| Prompt Term | Description |
|-------------|-------------|
| `reveal from blur fade in` | Starts out of focus, pulls sharp |
| `rack focus foreground to background` | Focus shifts from sharp subject to sharp background |

### Tripod Moves
| Prompt Term | Description |
|-------------|-------------|
| `tilt up` | Camera tilts from feet to head |
| `tilt down` | Camera tilts from head to feet |
| `camera truck left` | Lateral movement left |
| `camera truck right` / `lateral truck right` | Lateral movement right |

### Orbital Movements
| Prompt Term | Description |
|-------------|-------------|
| `orbit 180` | Half-circle around subject |
| `fast 360 orbit` / `spin` | Full-circle rapid orbit |
| `slow cinematic arc` | Gentle wide curved movement |
| `the camera rotates` / `the camera orbits` | General circular motion |

### Vertical Movements
| Prompt Term | Description |
|-------------|-------------|
| `pedestal down` | Camera body lowers vertically |
| `pedestal up` | Camera body rises vertically |
| `crane up` / `high angle reveal` | Crane rises with subject below |
| `crane down` / `landing` | Crane descends to subject |

### Aerial/Drone
| Prompt Term | Description |
|-------------|-------------|
| `drone fly over` | High-altitude pass over scene |
| `epic drone reveal` | Pedestal + tilt combination aerial |
| `large scale drone orbit` | Sweeping aerial circle showing scale |
| `top down` / `God's eye view` | Directly overhead pointing down |
| `FPV drone aggressive` / `drone dive` | First-person diving drone shot |

### Stylized/Dynamic
| Prompt Term | Description |
|-------------|-------------|
| `handheld documentary style` | Camera mimics person holding camera |
| `shaky handheld camera` | Chaotic, unstable camera movement |
| `whip pan` | Violent fast camera rotation with motion blur |
| `Dutch angle` / `roll` | Camera tilted sideways on Z-axis |

### Subject Tracking
| Prompt Term | Description |
|-------------|-------------|
| `leading shot` / `backward tracking` | Subject walks toward camera, camera retreats |
| `following shot` / `forward tracking` | Camera follows behind walking subject |
| `side tracking` / `parallel` | Camera moves alongside subject |
| `POV walk` / `first person walk` | Camera bobs as if walking toward subject |
| `medium tracking shot` | Standard follow at medium distance |
| `tight side tracking shot with slight orbit` | Close follow with curved path |

### Combined Camera Techniques
| Prompt Term | Description |
|-------------|-------------|
| `pull back and orbit around her` | Retreat + circular motion |
| `dolly in following the ball` | Forward camera tracking object |
| `low angle wide, whip pan following direction change` | Multiple techniques in one shot |
| `close-up, rack focus from face to goalkeeper` | Framing + focus shift combined |

---

## 10. Reference Input Modes (Seedance 2.0 Specific)

### Mode 1: Start Frame + End Frame
- Upload image 1 as first frame, image 2 as last frame
- AI fills everything between based on prompt
- **Limitation:** "gives the AI less freedom to create high motion dynamic camera work" (Source: Benji)

### Mode 2: All-Round Reference (Multi-Reference)
- Upload up to 12 reference objects (images, videos, audio, text)
- Use `@mention` syntax to reference specific uploads in prompt
- **This is the signature Seedance 2.0 feature**
- Can include: character sheets, location references, object references, audio clips
- Tag specific images: "this particular image as the start frame" even in multi-ref mode

### Mode 3: Character Sheet + Scene
- Upload character sheet (turnaround with multiple angles)
- Prompt describes scene and action
- Character sheet requirements: "full body views from head to toe facing four different directions" + "close-up shots of face including front and profile views"
- Style lock: "photorealistic, lifelike, live-action" prevents 3D render look
(Source: CyberJungle)

### Mode 4: Video-to-Video (Motion Transfer)
- Upload reference video as motion guidance
- Upload character image for visual identity
- Audio can be attached separately for lip sync
- Works for: boxing, dancing, talking, walking motion transfer

---

*Research compiled from YouTube transcripts. All terms marked as "tested" were demonstrated in video with visible results. Terms may behave differently across different Seedance access endpoints (Dreamina/CapCut, BigMotion AI, YouArt/UARY, FL.AI, Crea.ai, Art List).*
