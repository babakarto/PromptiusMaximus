# SEEDANCE 2.0 - COMPLETE GUIDE TO PERFECT PROMPTS

> Complete collection of guides, techniques, templates and 100+ ready-to-use prompts for creating cinematic videos with Seedance 2.0.

---

## TABLE OF CONTENTS

1. [What is Seedance 2.0](#what-is-seedance-20)
2. [Perfect Prompt Structure](#perfect-prompt-structure)
3. [The 3 Main Frameworks](#the-3-main-frameworks)
4. [Camera and Shot Vocabulary](#camera-and-shot-vocabulary)
5. [Multimodal @Reference System](#multimodal-reference-system)
6. [Copy-Paste Templates by Category](#copy-paste-templates-by-category)
7. [Negative Prompts and What to Avoid](#negative-prompts-and-what-to-avoid)
8. [Advanced Tips and Troubleshooting](#advanced-tips-and-troubleshooting)
9. [70+ Ready-to-Use Prompts by Category](#70-ready-to-use-prompts-by-category)
10. [Resources and Useful Links](#resources-and-useful-links)

---

# 1. WHAT IS SEEDANCE 2.0

Seedance 2.0 is ByteDance's next-generation AI video generation model, released in February 2026. It is the first model that supports simultaneous quad-modal input (image, video, audio, text).

### Key Capabilities

- **Multimodal Input**: Text + up to 9 images + 3 videos + 3 reference audio tracks
- **Director-Level Control**: Camera movements, facial expressions, gestures, lighting, pacing via natural language
- **Native Audio-Video Sync**: Generates complete videos with integrated audio; dialogues synchronized with lip-sync
- **Advanced Physical Realism**: DiT architecture with stable hands, natural fabric movement, accurate gravity and collisions
- **Character Consistency**: Faces, clothing, body type and visual style remain consistent across angles and scenes
- **Resolution**: Up to 1080p, duration 4-30 seconds
- **Access**: Currently via Jimeng/Dreamina

---

# 2. PERFECT PROMPT STRUCTURE

## Basic Formula

```
SUBJECT + ACTION + CAMERA + SCENE + STYLE + CONSTRAINTS
```

## 5-Part Anatomy (WaveSpeed Framework)

| # | Element | What It Does | Example |
|---|---------|--------------|---------|
| 1 | **Subject** | Who or what appears in the scene | "30s ceramic mug on a workbench, matte white" |
| 2 | **Action** | What the subject does (present tense verb, single) | "Steam rises as a hand slides the mug into frame" |
| 3 | **Camera** | How we see the scene (shot + movement + lens) | "Medium close-up, slow dolly-in, eye level, normal lens" |
| 4 | **Style** | The visual look (one anchor reference) | "Soft morning window light, subtle film grain, muted palette" |
| 5 | **Constraints** | What to keep fixed, what to exclude, timing | "No logos, no text overlays, hold on hand steady for 2s" |

### Why This Order Works

- **Subject first** anchors the model to a central point
- **Action** is the kinetic anchor for movement
- **Camera** sets the framing logic
- **Style** adds character without interfering with the action
- **Constraints** act as guardrails

### Golden Rules

- **Optimal length**: 100-280 words (too short = vague results, too long = dilutes focus)
- **One movement verb per shot** — combining two verbs creates chaos
- **The model prioritizes elements that appear first** in the prompt
- **Specific prompts > vague prompts**: "The tires smoke as the car drifts 90 degrees" >> "car turns"
- **Positive framing**: Seedance responds better to affirmative instructions
  - `Detailed hands`, `Anatomically correct` → better anatomy
  - `Physically accurate`, `Natural motion` → better movement
  - `Ultra sharp`, `Masterpiece` → superior visual quality

---

# 3. THE 3 MAIN FRAMEWORKS

## Framework 1: Five-Segment Structure (Beginners)

**Logic**: Subject + Scene/Atmosphere + Action/Performance + Camera Movement + Style/Lighting

Ideal for single-shot videos with simple compositions.

**Example - Man with Red Umbrella:**

> A serious man in a black overcoat, expression firm but tinged with melancholy. He slowly opens a red umbrella as raindrops slide along its edge. He stands on a neon-lit urban street; water splashes around him. The camera performs a slow push from a wide shot to a medium shot. Strong cinematic style, film grain, teal-orange color grading, 4K ultra HD, realistic physical simulation.

---

## Framework 2: CRAFT (Multi-Asset Projects)

**C**ontext + **R**eference (@assets) + **A**ction + **F**raming/Timing + **T**one/Audio

Ideal when working with multiple references (images, video, audio).

**Example - Film Noir Detective Scene:**

> Context: 1940s film noir detective office, heavy with smoke. Reference: Character face and wardrobe strictly follow @Image1; movement pacing is based on @Video1. Action: The detective steps out of the shadows, moves to the desk, and picks up a photograph, studying it with a grave expression. Framing: Dutch Angle composition with a tracking camera shot. Tone: Tense and melancholic atmosphere, classic film grain, background music @Audio1.

---

## Framework 3: Timeline Storyboard (Multi-Shot Narrative)

Split the video into specific time segments (0-4s, 4-9s...) and describe what happens in each.

**Example - Epic Samurai Duel:**

> 0-4s: Wide shot. The samurai walks forward from a distance through a bamboo forest; wind ripples his clothing; morning mist fills the scene. Style: @Image1.
> 4-9s: Medium tracking shot. He draws his sword and takes his opening stance; leaves fall around him.
> 9-13s: Close-up. The blade cuts through the air; slow-motion water splashes.
> 13-15s: Whip pan. Sword flashes, Japanese-inspired epic atmosphere.

### Which Framework to Use?

| Goal | Framework |
|------|-----------|
| Multi-shot narrative | Timeline Storyboard |
| Multiple reference assets | CRAFT |
| Single shot or beginner | Five-Segment Structure |

---

# 4. CAMERA AND SHOT VOCABULARY

## Shot Types

| Type | Use | Notes |
|------|-----|-------|
| **Wide** | Establishes space and context | Pair with slow dolly or static camera; avoid fast pans |
| **Medium** | Subject + context, dialogue | Handheld = personal; gimbal = professional |
| **Close-up** | Detail and emotion | Small push-ins work best; pans can feel annoying |

## Movement Types

| Movement | Effect | Notes |
|----------|--------|-------|
| **Pan** | Lateral rotation to reveal info | Keep slow to avoid smearing |
| **Tilt** | Pan up/down to reveal vertically | Tilt up = grandeur; Tilt down = discovery |
| **Dolly/Track** | Physical movement toward/from/along the subject | Cinematic at any speed |
| **Crane** | Vertical movement | Implies grandeur |
| **Handheld** | Light sway and micro-shake | Perfect for UGC; risky near text |
| **Gimbal** | Smooth stabilized movement | Professional look |
| **Steadicam** | Smooth long take | Ideal for following characters |

## Special Shots

| Shot | Description |
|------|-------------|
| **POV** | First person |
| **360 orbit** | Wrapping movement around the subject |
| **Rack focus** | Focus shift between foreground and background |
| **Whip pan** | Ultra-fast dynamic transition |
| **Dutch angle** | Tilted angle for tension |

## Lens Descriptors (Avoid Exact Millimeters)

| Type | Equivalent |
|------|------------|
| **Wide** | 24-28mm feel |
| **Normal** | 35-50mm feel |
| **Telephoto** | 85mm+ feel |

## Speed and Distance

Use scalars with approximate distance:
- `slow dolly-in, 1-2 feet`
- `medium pan right`
- `fast whip pan left`

### CRITICAL RULE
**One verb per shot.** Compound movements work better as sequential beats:
> "Start: slow dolly-in. Then: gentle pan right for final 2 seconds"

---

# 5. MULTIMODAL @REFERENCE SYSTEM

## Reference Hierarchy

| Type | Function | Priority |
|------|----------|----------|
| **@Audio** | Lip-sync and beat matching, edit timing | Rhythmic anchor |
| **@Video** | Transfer of movement trajectories and camera language | Motion anchor |
| **@Image** | Lock character appearance (face, wardrobe, style) | Visual anchor |

## Limits

- Up to **9 reference images**
- Up to **3 reference videos**
- Up to **3 audio tracks**
- **Maximum total: 12 assets** in a single prompt

## How to Use References

### Basic Generation
```
@image1 as the first frame, [describe subject, action, camera, scene]
```

### Lock Reference Video
```
Reference @video1 for camera movement and shot language, [describe new content]
```

### Multi-Modal Combination
```
@image1 as the first frame, reference @video1 for motion,
@audio1 for rhythm and mood, [describe complete scene]
```

### Motion Imitation
```
Imitate the action of @Video1
```
> The model will take the character from your image and make it move like the person in the video, tracking physics and timing perfectly.

### Video Editing
```
Replace [element A] in @video1 with [element B], [additional constraints]
```

### Video Extension
```
Extend @video1 by [X] seconds, [describe new content]
```

## Best Practices for References

- **@Image**: Use half-body portraits with simple composition for best results
- **Character consistency**: Always add "Maintain facial features and wardrobe fully consistent with @Image1"
- **Textual reinforcement**: Reiterate key traits in text even with a reference image (e.g. "short silver hair", "mole under left eye")
- **Visual anchor**: Always use the same face reference (@Image1) across all prompts in a project

---

# 6. COPY-PASTE TEMPLATES BY CATEGORY

## Template 1: UGC (Phone-in-Hand Style)

```
Subject: [person, age range, setting]

Action: [casually talks about X while doing Y]

Camera: Medium, handheld phone perspective, slight sway, eye level, normal lens feel

Style: Natural indoor light, ungraded look, light motion blur

Constraints: No captions, no snap zooms, keep hands natural, 8-10s, keep background simple
```

---

## Template 2: Product Ad (Clean and Stable)

```
Subject: [product name/material/color]

Action: [rotates slowly / slides into frame / subtle hero movement]

Camera: Close-up to medium close-up, slow dolly-in, locked horizon, normal-to-tele feel

Style: Soft key light + gentle rim, neutral color grade, light film grain

Constraints: No logos/labels, no flares, hold final frame 2s, 6-8s total
```

---

## Template 3: Cinematic (Mood-First)

```
Subject: [character or location]

Action: [specific beat: waits, turns, breathes, steps into the light]

Camera: Wide establishing for 2s then slow push to medium, gimbal-smooth, eye level

Style: [single anchor reference, e.g. "overcast natural light, muted blues"]

Constraints: No Dutch angles, no crowd, no neon, maintain overcast look, 10-12s
```

---

## Template 4: Talking Head (Stable and Readable)

```
Subject: [speaker description]

Action: [delivers a clear sentence]

Camera: Medium close-up, locked tripod or very subtle dolly-in, eye level

Style: Soft key from 45deg, clean background separation, neutral grade

Constraints: No auto captions, no whip pans, skin tones natural, 12-15s, keep eyeline centered
```

---

## Template 5: Montage (Fast Beats Without Chaos)

```
Subject: [theme, e.g. "morning coffee ritual"]

Action: Beat 1 [wide context], Beat 2 [close-up hands], Beat 3 [steam detail], Beat 4 [sip]

Camera: Each beat 2s, clear shot size per beat, no compound moves: transitions by cut

Style: Consistent light and palette across beats

Constraints: No text overlays, no speed ramps, keep tempo steady, 8-10s total
```

---

## Template 6: 360 Product Rotation (E-commerce)

```
Subject: [product] on a pure white infinite studio background

Action: rotating smoothly 360 degrees clockwise. [specific visible product details]

Camera: Fixed macro camera, smooth turntable motion

Style: commercial product photography style, soft high-key lighting, no noise

Constraints: Logo and text remain perfectly consistent. No flicker.
```

---

## Template 7: Music Video Beat Sync (Audio Driven)

```
Subject: [character] dancing in [setting]

Action: Every strong beat triggers a cut or speed-ramped camera move.
[specific setting details]

Camera: [specific style], fast-paced editing, multi-shot continuity

Style: [visual style], neon reflections

Constraints: Dance movements and character appearance remain consistent.
Reference: @Audio1 for beat sync + @Video1 for dance reference
```

---

## Template 8: Digital Avatar / Explainer

```
Subject: [person/avatar description, clothing, age]

Action: [pauses, breathes, begins to speak: "PHRASE"]. Lip-sync aligns with @Audio1.
[natural gestures accompanying speech]

Camera: Frontal medium shot, gentle push-in

Style: [lighting], [color tone], [atmosphere]

Constraints: Consistent eye contact with camera. Expressions follow speech flow
without feeling mechanical or repetitive. 12-15s.
```

---

# 7. NEGATIVE PROMPTS AND WHAT TO AVOID

## Negative Prompt Checklist

### Visual Noise to Ban
- No text overlays, watermarks, floating UI, lens flares (unless specified)

### Identity Drift Prevention
- No extra characters, crowds, mirrors reflecting others

### Camera Chaos Control
- No snap zooms, whip pans, Dutch angles, jump cuts (unless intentional)

### Body Artifact Prevention
- No extra fingers, deformed hands, warped handles, melting edges

### Branding
- No logos, labels, recognizable brands

### Color/Grading
- No neon lighting, heavy teal/orange, cartoon saturation (unless intentional)

### Environment
- No rain/fog/smoke (unless specified), confetti, dust particles

### Audio/Text
- Ban auto captions if adding voiceover in post-production

### Strategic Note
Use **3-5 negatives per prompt**. Too many bans make the image flat. If artifacts persist after two attempts, modify the subject text or simplify the camera notes rather than adding more constraints.

---

# 8. ADVANCED TIPS AND TROUBLESHOOTING

## Writing Tips

### Physicality and Weight
Rather than "car turns", specify:
> "The tires smoke as the car drifts 90 degrees."

This tells the AI to calculate friction and force, producing realistic results in 2K.

### Native Audio
Include specific sound terminology: "reverb", "muffled", "high-pitched" to activate the native audio engine.
> "metallic clink of a coin" generates a sharp sound synchronized with the visual vibration.

### Lighting
Specify the light quality: "God rays", "Volumetric fog", "Cyberpunk neon" -- these calculate light bounce on surfaces. Always indicate if the light is "soft", "harsh" or "flickering".

### Timestamps for Pacing
When the scene has multiple moments, timestamps give much more control:
> 00:00-00:04 – Wide Tracking Shot: [description]
> 00:04-00:07 – Cockpit / Tight Action Shot: [description]
> 00:07-00:10 – Epic Pull-Back: [description]

## Troubleshooting

### Problem: Character Consistency Break
**Solution:** Add constraint: "Keep the same character, same clothing, same hairstyle, no face changes, no flicker, high consistency."

### Problem: Hand and Text Distortion
**Solutions:**
- Avoid fast close-ups of hands
- Use larger, centered text
- Add: "hands with perfect anatomy, text clear and readable"

### Problem: Movement Artifacts
**Solutions:**
- Change "fast" to "medium speed"
- Use video reference to lock the movement

### Problem: Too Much Randomness
**Solutions:**
- Upload more references
- Lower the creativity settings
- Add more constraints in the prompt

### Problem: Long Videos
**Solution:** Generate perfect 5-10s clips, then use the video extension function to continue.

## Re-Prompting Decision Tree

| Problem | Action |
|---------|--------|
| Wrong framing, action OK | Re-prompt: fix Camera first. Keep Subject and Action identical |
| Movement too shaky/fast | Re-prompt: swap "handheld" with "gimbal", set speed |
| Style/color drift, movement OK | Re-prompt: replace the Style line with a stronger anchor, remove adjectives |
| Subject mutating (extra people/objects) after 2 attempts | Change reference: simplify Subject with fewer descriptors |
| Repeated artifacts after 3 attempts | Change constraints or shot plan; consider moving away from close-up |

**Time management**: Give 2 quick re-prompts (under 5 minutes total). If you keep correcting the same error, change the reference or shot type.

---

# 9. 70+ READY-TO-USE PROMPTS BY CATEGORY

---

## CATEGORY 1: Cinematic - Narrative and Drama

### 1. Pizza Shop Cinematic Sequence
> Single continuous cinematic shot, no music. From outside the glass window, the dim camera slowly pushes inward into a pizza shop. A bearded white male employee is baking pizza. He removes the pizza from the oven with a metal tray, places it into a red takeaway box, closes the lid, and then hands it to a customer with a warm smile. Final shot: over-the-shoulder perspective.

### 2. Indoor Volleyball Match Scene
> A women's volleyball match in a spacious indoor gym with an arched wooden ceiling and large windows. The stands are full of cheering spectators, and colorful banners hang on the back wall. The blue and green teams exchange intense rallies while players shout to communicate. The green team fails to save the ball, and an off-screen whistle blows. Cut to a close-up of a middle-aged female coach with short blonde hair, metal-framed glasses, and a green jacket. She watches intently, then lowers her head in frustration. Background music: energetic rhythmic track.

### 3. Street Dance Battle
> Generate a 15-second photorealistic street dance battle at night. The urban street has reflective wet pavement, neon lights, and a thin mist. A group of young dancers forms a semicircle. The first 5 seconds focus on one dancer performing challenging solo floor moves. The remaining 10 seconds show the full group performing synchronized choreography combining breaking, popping, locking, and hip-hop. Use a smooth, stable cinematic camera with realistic physics and accurate body proportions.

### 4. Cave Exploration POV
> First-person POV handheld footage with slight natural shake. The only light comes from a headlamp, illuminating damp mossy walls. The camera moves through a narrow tunnel; the hand occasionally enters the frame. Audio captures heavy breathing, footsteps on wet soil, and raw on-location sounds. When the tunnel opens, the camera pauses, then pans slowly left to right over glowing semi-transparent crystals. Footsteps hit rocks with sharp clacks that echo through the cavern. The explorer exhales in awe as the sound swirls and fades.

### 5. Knight in the Cave
> A multi-shot sequence of a knight in silver armor. Shot 1: Wide shot as he enters a dark cave with a torch. Shot 2: Close-up of his nervous eyes. Shot 3: He draws his sword, which glows blue. Low-angle tracking shot, 2K resolution. Sound of crackling fire and echoing footsteps.

### 6. Butterfly Lighting Pianist
> Cinematic butterfly lighting. Medium shot of a handsome pianist wearing a simple, elegant black suit. His audience noise from a concert hall.

### 7. Steadicam Cafe to Subway
> Steadicam long take following a man from a warm, yellow-lit cafe into a cool-toned, busy street. He pushes the door open, walks through traffic with cars creating light trails, and finally descends a dim subway staircase. The lighting transitions smoothly from warm indoor light to natural outdoor light, then to fluorescent subway lighting, all in a single continuous shot.

### 8. Hong Kong Retro Film
> 90s Hong Kong art cinema style with retro grain, yellow-green tint, and step-printing effect. A man or woman in a khaki trench coat listens silently at a rain-soaked red phone booth. Extreme close-ups capture subtle lip trembles and restrained emotion as neon reflections flicker across the face. The character hangs up and walks into the rainy night crowd, with motion blur and step-printing creating a smeared, dreamlike effect. Handheld camera simulation, shallow depth of field, and color shifts emphasize melancholy and intimacy.

---

## CATEGORY 2: Action, Combat and Chases

### 9. Green-Screen Fight Scene
> Make the characters from Image 1 and Image 2 fight using the movements from the green-screen reference video. Setting: abandoned parking lot. Add visual effects during combat.

### 10. Close-Quarters Combat Scene
> A short-haired female agent in tactical winter gear engages in close-quarters combat with a mercenary at a snowy military base. The mercenary throws a punch; she dodges swiftly and counters with a powerful elbow strike to his face mask, followed by a heavy knee to the stomach. Impact shows visible shockwave ripples, and sweat and saliva fly through the air as the enemy's body folds from the blow. The camera follows the action with dynamic handheld movement. Cold breath vapor rises, textures are gritty, and high-contrast lighting emphasizes the intensity.

### 11. Nordic Snow Chase
> Realistic Nordic snowy night. A man runs fast through deep snow, tracked closely from behind at foot level. A wolf chases him, maintaining a strong sense of speed. The man trips and rolls; the wolf lunges at him. A border collie jumps in, knocking the wolf aside. The animals wrestle; the wolf breaks free and howls. Multiple wolves slowly surround the man and dog. Close-up on the dog as the owner slowly sits up. Background music: tense and evolving with the action.

### 12. Cyberpunk Assassin Fight
> Cyberpunk style, game CGI, dark city corner. A young assassin fights multiple enemies with a lightsaber. The camera rapidly pulls back to show the surrounding foes. The assassin moves fluidly, defeating enemies one by one. Enemies collapse as the sequence stays fast but smooth. Teleportation-style visual effects blend with cinematic transitions. The assassin ends by looking directly at the camera.

### 13. Shibuya Parkour Sprint
> Single continuous cinematic shot in Shibuya. A schoolgirl sprints at extreme speed, weaving along crosswalks and walls. The camera moves low and close to the ground, following her every leap, roll, and jump. City lights streak below as she lands and rolls forward. Sound mixes daytime street noise, 8-bit video sounds, and shamisen strings. The sequence emphasizes fluid motion, fast choreography, and dynamic camera movement.

### 14. Neon City Action Chase
> High-energy cinematic chase at night in a neon-lit city. A lone character sprints through rain-soaked streets while police drones and headlights blur past. Quick cuts show close-ups of eyes, boots splashing puddles, and wide traffic shots. The character vaults barriers, slides across car hoods, and dodges explosions. Handheld camera style with motion blur and dynamic lighting. The sequence ends in slow motion as he leaps off a rooftop with city lights streaking beneath him.

### 15. AAA Game-Style Fight
> They meet in the dead of night and engage in a fight. The fighting style is incredibly flashy, the atmosphere is tense, and the camera work is cinematic. It's like a promotional trailer for a AAA game, featuring CG and Unreal Engine 5.

### 16. Mirror Breakdown Scene (with @Reference)
> The woman in @Image1 walks up to the mirror and looks at her reflection. Her pose should reference @Image2. After a moment of contemplation, she suddenly breaks down and starts screaming. The action of grabbing the mirror, as well as the emotions and facial expressions during the breakdown and scream, should fully reference @Video1.

### 17. Battlefield Tactical Action
> The man from reference image 1 as the protagonist, agile and athletic, running through a battlefield under a hail of bullets while engaging in intense tactical shooting. Visual Style: Cinematic quality with strong Orange and Teal color grading, high contrast, and visible film grain. Dynamic Details: Distinct muzzle flashes from the gun. Bullets striking surrounding objects create flying rubble and sparks. Smoke and shockwaves from explosions fill the background. Camera Movement: Handheld Camera style tracking shot, shaking violently alongside the character, with occasional snap zooms to create extreme tension and a chaotic sense of presence. Character Performance: The protagonist has determined eyes; his actions are filled with power and speed, perfectly replicating the vibe of a Hollywood action superstar.

### 18. Cyber City Chase (Timeline)
> A character following the reference of @Video1 runs at high speed through rainy neon city streets, with minor visible injuries. 0-4s: Wide tracking shot - fast but grounded steps, realistic splashes through puddles. 4-9s: Slow motion as the character leaps over obstacles; prosthetic leg grazes the ground, generating mechanical sparks. 9-13s: Sharp turn, neon lights reflecting dynamically on wet pavement. 13-15s: Character stops, looks back - breathing heavy but alert, rain streaming down the face. Camera rhythm: tracking → slow-motion jump → circling turn → tense close.

### 19. Swordsman Duel (Timeline)
> Two swordsmen based on @Video1, standing in a forest clearing, facing each other. 0-5s: Static medium shot - held breaths, eyes scanning for weakness. 5-10s: The clash erupts suddenly. Fast camera with push-pull following the rhythm of strikes; metal clangs spark realistically; slow-motion blood droplets fly. 10-15s: Camera circles the victor. The opponent falls; the winner sheathes the sword. Dust settles slowly.

### 20. Futuristic Hand-to-Hand Combat (Timeline)
> Two futuristic warriors based on @Video1 engage in close-quarters combat in a high-tech arena. 0-5s: Medium standoff shot - assessing weaknesses; mechanical arms charge up energy gradually. 5-10s: High-speed exchange of blows; contact points generate electric arcs with real physical feedback. 10-15s: Slow motion of a blow that sends the opponent down. Armor fragments fly.

### 21. Explosive Escape (Timeline)
> A tactical soldier based on @Image1, covered in dust, wearing a tactical vest with minor wounds. 0-4s: Advances cautiously through a burning industrial zone, constantly scanning for threats. 4-8s: A lateral explosion - instinctively ducks, protecting his head from the blast. 8-12s: Slow motion moving through fire and flying debris, gaze focused. 12-15s: Exits the burning area, stops and looks back.

---

## CATEGORY 3: Sports, Racing and Martial Arts

### 22. Competitive Pairs Figure Skating
> A live performance of competitive pairs figure skating. A low-angle camera follows the skaters, showing ice chips and reflections. During the spin section, the male skater miscalculates briefly, and the female skater adjusts to guide him back into rhythm. They perform a seamless lift with clean, stable lines, followed by synchronized jumps with straight postures, decisive landings, and perfect audio-visual sync. The female wears a dark blue skirt, and the male wears competitive sportswear.

### 23. Hollywood Racing Scene (Timeline)
> Hollywood professional racing style at night in the rain. Shot 1 (00-05s): Close-up inside the veteran driver's car as rain lashes the windshield. He stays calm, nods, and mouths 'Let's go.' Shot 2 (05-10s): Close-up inside the rival car; the younger driver grips the wheel tightly, breathing heavily, whispering 'Focus.' Shot 3 (10-15s): Wide action shot as the green lights trigger both cars to accelerate on wet asphalt, spraying water into the camera.

### 24. Wuxia Duel (Multi-Shot)
> An Eastern Wuxia-style duel between a grandmaster in white and a grandmaster in black on an ancient stone platform. Shot 1: Both clash at high speed, leaving afterimages as sparks and a ring-shaped shockwave erupt. Shot 2: They soar into the air, striking amid falling boulders and shattered pillars. Shot 3: Both release ultimate moves, cyan and red energy orbs collide, triggering an earth-shattering explosion.

### 25. Martial Arts Epic Duel
> A white-clad swordsman faces a straw-cloaked swordsman in a bamboo forest under heavy rain. The camera slowly pans, shifting focus between raindrops and sword hilts, building tension. Thunder flashes, and they charge simultaneously. Side-view shot captures mud-splattered footsteps, then a slow-motion weapon clash shows circular shockwaves scattering raindrops and bamboo leaves. Both landing back-to-back as the straw-cloaked swordsman's hat splits open.

### 26. Kite Flying Action Long Take
> A Chinese youth flies a kite through crowded streets, leaps up steps, flips, lands, and dashes toward a high platform for a difficult jump. A drumbeat erupts as he lands. The entire sequence is a single continuous shot with fluid movements, realistic weight, inertia, and landing cushioning. Style transition: 0-5s in Makoto Shinkai style; 6-10s in ink-wash style.

### 27. Horseback Flower Offering
> A man in orange rides a brown horse toward a large tree blooming with orange flowers. He plucks two flowers, then other riders follow. The camera pushes in and circles as he dismounts swiftly, then approaches a woman in white on a white horse to present the flowers. Style: classical Chinese 'court lady painting' aesthetic. Music: cheerful traditional Chinese folk instrumental.

---

## CATEGORY 4: ASMR, Macro and Sensory

### 28. ASMR Skincare Macro
> Create a vertical ASMR video with no music, focusing on macro details. A light blue skincare gel bottle sits on glass. A pale, elegant hand gently taps the glass, producing crisp fingernail tapping sounds. The hand picks up the bottle and slowly twists the cap, with the rotation sound clearly audible. A spoon scoops a portion of gel and drops it onto the glass with a soft 'plop,' showing dense gel with tiny air bubbles. Dramatic cool lighting from behind makes the gel glow like a gemstone.

### 29. Hands ASMR POV
> A first-person ASMR video featuring hands. Close-up shots show a pair of slender hands gently interacting with different objects in sequence: scratching frosted glass, rubbing plush fabric, tapping an acrylic board, squeezing bubble wrap, and brushing a wooden comb. The finger movements are slow and gentle, and the trigger sounds are purely natural with no background music.

### 30. Miniature Cooking Sequence
> A miniature cooking video on a pure black background with dramatic top lighting. Show full-sized hands carefully placing a tiny cutting board and a fingernail-sized knife. Use elegant classical music as background. The hands slice a tiny garlic clove precisely, add a micro drop of olive oil to a mini frying pan over a tea candle, and crack a small quail egg into the pan. Use a tiny spatula to nudge the egg, then plate a miniature sunny-side-up egg with a slice of garlic mushroom and a tiny scallion garnish on a coin.

### 31. Sizzling Wagyu Steak
> Close-up of a wagyu steak hitting a hot cast-iron skillet. You can see the fat rendering and bubbles of oil. 2K resolution, shallow depth of field. Sound of loud, aggressive sizzling.

---

## CATEGORY 5: Commercial and Product

### 32. Luxury Perfume Commercial
> An ultra-luxury perfume commercial with a dreamy electronic soundtrack and steady drum beats. Begin with a macro shot of a transparent rectangular glass bottle surrounded by violently swirling purple liquid. Capture the churning liquid with bubbles and splashes, accompanied by crisp water sounds. Dissolve into surface ripples of the purple liquid, then show a close-up of delicate iris flowers floating underwater. Cut to the perfume bottle tilted on a textured light surface, refracting dreamy halos. Shift style: a Latina female model elegantly lifts the perfume bottle to her neck and shoulder in a pure white high-end studio, gazing into the camera.

### 33. Coke Interaction Story
> A narrative Coke interaction scene. A figure looks guilty, glancing left and right before peering out of frame. He quickly reaches, grabs the Coke, takes a sip, and shows a satisfied expression. Footsteps are heard as he hurriedly puts the Coke back. A cowboy then picks up the Coke and walks away. End with a close-up of the top-lit Coke against a completely black background.

### 34. Sketch to 3D Car Transformation
> A car sketch on paper. The camera pushes in. The sketch lines rise off the paper, gaining dimensionality and color, transforming into a photorealistic 3D car driving on a road.

### 35. Living Room Renovation Time-Lapse
> Based on the reference image, generate a time-lapse animation showing the living room transforming from an unfinished, raw concrete interior to a fully renovated space. Final shot: all the lights switch on instantly, accompanied by a realistic light-switch sound effect.

### 36. Hollywood Sci-Fi Blockbuster (Timeline)
> Create a 10-second cinematic sequence in a Hollywood sci-fi style with cyberpunk aesthetics.
> 00:00-00:04 - Wide Tracking Shot: Futuristic Megacity canyon at night, rain falling. An anti-gravity vehicle weaves between skyscrapers. Neon reflections shimmer on glass curtain walls. Blue light trails behind.
> 00:04-00:07 - Cockpit / Tight Action Shot: Vehicle drifts sharply. Sparks and mist as fuselage grazes a building. Rain hits camera lens. Camera shake emphasizes speed.
> 00:07-00:10 - Epic Pull-Back / Crane Shot: Vehicle bursts into open city plaza through low clouds. Massive lens flare.
> Technical: 8K Ultra HD, teal-and-orange grading, HDR, complex particle effects, realistic motion blur.

### 37. Fashion Runway
> A model wearing a long black silk dress based on @Image1, on a high-end runway stage. 0-4s: Side-angle tracking shot; dress moves naturally with body's center of gravity. 4-8s: Camera orbits the model, showcasing fabric sheen under lights. 8-12s: Model holds confident gaze; when she turns, skirt forms elegant curve. 12-15s: Camera pushes in to frontal close-up.

### 38. Smartphone Product Video
> A premium smartphone based on @Image1, metallic body and glass edges. 0-3s: Product floats against gradient background, rotating 360. 3-7s: Macro shot of side panel - light glides across metallic surface. 7-10s: Screen illuminates, animated fingerprint sensor. 10-15s: Camera drifts into center of screen, UI elements breathe subtly.

### 39. Coffee Machine Promo
> A coffee machine on a wooden table based on @Image1. 0-4s: Machine powers on; steam rises slowly. 4-8s: Macro shot of coffee drops falling, creating natural ripples. 8-12s: Steam envelops cup, visually suggesting aroma. 12-15s: Camera drifts toward coffee surface, reflecting fine crema layer.

---

## CATEGORY 6: Lifestyle, Culture and Characters

### 40. Girlfriend POV Vlog
> Create a 15-second vertical (9:16) handheld vlog in natural golden-hour light, with film grain and slight camera shake. Protagonist: A Taiwanese girl with long, slightly curled hair, wearing a soft knit cardigan. Scene: Taipei Tamsui riverbank at sunset. Shot 1: She walks quickly, looking back pretending to be annoyed. Shot 2: She stops, shows the golden sunset, smiling. Shot 3: She holds ice cream to the camera, licks it, giggles as some lands on her nose.

### 41. 1920s Jazz Club Charleston
> Create a Charleston dance sequence in a 1920s jazz club style. A female dancer in a gold-fringed dress and a male dancer in a striped suit perform rapid, syncopated steps, aerial tosses, and large arm swings. The camera tracks dynamically, with close-ups on feet to show fringe movement and sweat details. Smoky atmosphere and vintage film grain.

### 42. Lunar New Year Family Album
> The Year of the Horse Lunar New Year family video quickly scans through individual family photos, like flipping through an album. Each photo 'comes to life' the moment the lens passes: grandparents, parents, and children perform unique actions with micro-expressions. Different figures are seamlessly connected through rapid panning. Red lanterns and Spring Festival couplets dynamically light up, converging into a lively family portrait.

---

## CATEGORY 7: Creative, Multi-Reference and R2V Workflow

### 43. Traversing Famous Paintings
> @Image 1 The girl breaks the fourth wall, traversing multiple worlds of famous paintings while retaining realistic textures. She stands under the rotating starry sky in @Image 2; watches the couple embracing in @Image 3; takes a selfie with the Girl with a Pearl Earring in @Image 4; enters @Image 5 and passes between two samurai; makes faces with @Image 6; the Mona Lisa in @Image 7 pats her head; she exchanges greetings with the woman in @Image 8; paints with Van Gogh in @Image 9; finally turns to the camera and smiles sweetly. High contrast, cinematic quality, smooth transitions.

### 44. Healing Storyboard Video
> Refer to the storyboard of @Image 1, including its shot composition, framing, camera movement, visuals, and text. The characters are @Image 2, the scenes are @Image 3, and the props are @Image 4. Create a 15-second healing video.

---

## CATEGORY 8: Comedy and Concept

### 45. Avengers Alternate Scene
> Avengers Endgame big fight scene, cinematic style. Thanos suddenly freezes the battle and holds up his hands, looking genuinely apologetic. The superheroes pause, looking surprised, and slowly start to nod and walk away, accepting his apology. Then Spider-Man shouts, 'Oh no, he literally killed a bajillion people!' Everyone immediately turns back and rushes at Thanos, comically tackling and kicking him. Add expressive facial reactions, dynamic poses, and humorous timing.

### 46. Otter Pilot Documentary
> A nature documentary scene showing an otter piloting a small airplane. The otter wears aviator goggles and a tiny scarf, paws on the controls, looking focused yet playful. Camera follows from a dynamic low-angle tracking shot over rivers, forests, and mountains. Style: vibrant, slightly whimsical, photorealistic with cinematic framing.

### 47. Friends x Game of Thrones
> The cast of Friends in a Game of Thrones-style sitcom. Chandler as King Joffrey wearing a crown, acting dramatically spoiled. Joey as the Hand, in medieval attire, looking confused but loyal. Camera alternates between wide shots of the throne room and medium shots of expressions. Style: vibrant, humorous, sitcom-meets-fantasy aesthetic.

---

## CATEGORY 9: Fantasy and Sci-Fi

### 48. Alien Jungle Exploration
> A team of explorers moves cautiously through a dense alien jungle, bioluminescent plants glowing softly around them. The camera pans and tilts to reveal enormous alien trees, mist rising from the ground, and strange creatures watching from a distance. The explorers wear advanced exosuits.

### 49. Steampunk Airship Battle
> A massive steampunk airship engages in battle above a city. Smoke and steam fill the sky, with smaller airships darting around. Explosions throw sparks into the air. Crew members operate mechanical weaponry, levers, and pulleys with precision. Camera angles shift dynamically.

### 50. Samurai Duel at Dawn
> Two samurai face each other at the crest of a misty mountain at dawn. The first light hits their blades as they bow, eyes locked. Close-up on hands gripping hilts, then a wide shot showing the mist rolling over the valley below. The duel begins with a flurry of precise strikes, sparks flying.

### 51. Post-Apocalyptic City Chase
> A lone survivor sprints through a crumbling cityscape. Debris falls as buildings lean precariously. Neon signs flicker intermittently. Fast cuts show tension and near-misses. Sound: echoing footsteps, distant explosions, creaking metal.

### 52. Magical Library Discovery
> A young mage enters a colossal, enchanted library. Endless shelves stretch into misty heights. Floating candles and glowing books illuminate the space. The camera sweeps upward, revealing spiraling staircases. Books flutter like birds. The mage reaches for a levitating tome, triggering a cascade of sparkling light.

### 53. Cyberpunk Rooftop Showdown
> Two augmented warriors face off on a neon-lit rooftop. Rain pours, reflecting lights off slick surfaces. The camera rotates around them as they launch attacks, blades and cybernetic limbs glowing. Sparks fly on contact. The cityscape stretches into the distance with hovercars streaking past.

### 54. Giant Mech vs Dragon
> A towering mech engages in battle with a massive dragon atop a crumbling city. Flames and smoke billow. The mech fires energy beams; the dragon dodges with agile flips. Lightning crackles as their powers clash, creating dramatic lighting and cinematic tension.

---

## CATEGORY 10: Quiet Moments and Slice of Life

### 55. Rainy Night Convenience Store
> Single continuous shot. A young woman in an oversized hoodie pushes open a convenience store door. Rain streaks the glass behind her. Warm fluorescent light floods over her face. She walks slowly down the snack aisle, trailing one finger along the shelves. She stops, picks up cup noodles, reads the label, puts it back. She stands still. Camera holds on her face - neutral expression, eyes slightly distant. She grabs the noodles again and walks to the counter. Wide shot from outside as she pays, rain blurring the frame. No music. Only ambient store sounds and rain.

### 56. Rooftop Sunrise Yoga
> A woman practices yoga alone on a high rooftop at sunrise. City skyline behind her, golden hour light catching her silhouette. Camera begins on a slow crane shot from below the roofline, rising until the full cityscape is revealed. She moves through a sun salutation sequence. Shallow depth of field, warm light bokeh. No music. Only wind and distant city hum.

### 57. Ramen Shop Late Night
> Single continuous Steadicam shot. A ramen shop at 1am - near empty. One salaryman sits at the counter, hunched over his bowl. Steam rises. The chef moves behind the counter with practiced economy. Camera tracks along the counter. Close-up: the salaryman lifts chopsticks, takes his first bite. He exhales. His shoulders drop slightly. Camera holds. A tiny moment of relief. Background: low exhaust fan hum, distant rain, faint sound of a late train.

### 58. Rainy Day Home Vlog (Timeline)
> A 20-year-old in an oversized sweater, curled up on a couch reading. 0-5s: Wide shot of living room, rain sound. 5-10s: Camera pushes into medium shot; she turns a page and smiles softly. 10-15s: Close-up of raindrops sliding down glass, steam rising from hot cocoa.

### 59. Japanese Sushi (Timeline)
> Delicate sushi spread on a wooden tray. 0-4s: Wide overhead shot; a hand adjusts chopsticks. 4-8s: Chopsticks pick up sushi, pausing mid-air with natural wrist adjustment. 8-12s: Lightly dipping in soy sauce, creating subtle ripples. 12-15s: Chopsticks exit frame; soup shifts gently, steam continues to rise.

---

## CATEGORY 11: Nature, Landscapes and Weather

### 60. Deep Sea Bioluminescence Dive
> First-person POV dive footage. A scuba diver descends into pitch-black ocean. Only the diver's torch cuts a narrow beam. At depth, the torch clicks off. Total darkness for two seconds. Then - faint blue pulses. Bioluminescent jellyfish drifts past trailing light. A school of fish materialises as a glowing spiral. The diver reaches out; fish scatter like sparks. Camera pans to reveal vast glowing coral below. Slow exhale. No music.

### 61. Time-Lapse City Day to Night
> Locked-off wide shot from high vantage point overlooking dense city. Time-lapse: morning light sweeps skyline, shadows rotate, clouds roll fast, afternoon haze settles, city lights ignite cluster by cluster at dusk. Final ten seconds slow to real time: fully lit city at night, helicopter tracking slowly across frame. No cuts.

### 62. Storm Chaser POV Dashcam
> Handheld dashcam-style footage driving toward a massive tornado on flat American plain. Sky is yellow-green. The funnel is fully formed. Radio chatter over wind noise. Driver's hand enters frame to adjust camera. Rain begins, then heavy. Wipers struggle. Lightning strikes ahead. Cut to exterior wide: vehicle small against vast sky, continuing toward storm. Audio: raw wind, static radio, rain building.

### 63. Northern Lights Time-lapse
> Locked-off wide shot, Iceland/Norway, winter. Foreground: lone cabin with single amber window. Background: dark sky, snow-covered plain. Time-lapse: aurora emerges - first pale green ribbon, then sheets of green and violet ripple, fold and expand. Stars visible behind curtains of light. Silhouetted figure steps out and looks up. Time-lapse slows to real time for final five seconds. Complete silence except low ambient wind.

### 64. Mountain Summit Moment
> Documentary wide shot. Solo hiker crests mountain ridge at dawn, silhouetted against enormous orange sky. She stops. Locked-off, distant camera. She sets down her pack. Raises both arms. Camera holds. Wind moves through the frame. Slow push-in from wide to medium over-the-shoulder shot. No music. Only wind and crunch of boots settling into stillness.

---

## CATEGORY 12: Craftsmanship, Art and Live Performance

### 65. Elderly Hands Crafting
> Close-up, intimate documentary-style footage. An elderly craftsman's hands work clay on a potter's wheel. Extreme close-ups alternate: fingers pressing into clay, water spreading across the spinning surface, the form rising under steady pressure. Never cuts to his face. Only hands. Natural window light from one side. Audio: low hum of the wheel, wet clay sounds, distant birdsong. No music.

### 66. Ballet Rehearsal Behind the Scenes
> Documentary-style inside a ballet rehearsal studio. Mirrors line one wall. A female principal dancer marks through a solo at half speed, then runs it full out. Camera follows with slow handheld push. Close-up: feet in pointe shoes, floor scuffed with rosin marks. Wide shot: she stops, breathes, speaks quietly to the rehearsal director. Natural studio light. No music.

### 67. Neon Calligraphy Artist
> Medium shot, dark studio. A calligraphy artist sits at a lit table. She dips a large brush and begins writing a Chinese character on white paper. Camera pushes slowly in. As the brush moves, the ink trails begin to glow - deep red and gold. The strokes lift fractionally off the paper, hovering with faint luminescence. When the final stroke completes, all strokes glow at once, then settle back to ordinary ink. Camera holds on her face - quiet satisfaction. No music. Only brush on paper.

### 68. Underwater Ballet Sequence
> A female dancer performs underwater in a large pool. Flowing white fabric moves around her in slow, unpredictable ways. Camera circles at medium distance. She rises slowly from pool floor toward the surface, arms extended. Light filters down in shifting columns. She emerges, hair fanning in an arc of water droplets. Slow motion throughout. No music. Only muffled, resonant silence of deep water.

### 69. Sand Animation Performance
> Overhead locked-off shot, lit table surface. An artist's hands work sand on backlit glass surface. She sweeps, pinches, and drags the sand in rapid fluid gestures - each movement forming and dissolving images: a wave becomes a face, a face dissolves into a forest, the forest becomes a city skyline, the skyline scatters into stars. Continuous sequence, no resets. Only the artist's hands and the sand. Natural breath and ambient room tone.

---

## CATEGORY 13: Magic, Wonder and Transformation

### 70. Children's Chalk Drawing Comes to Life
> A child crouches on a sunlit pavement, drawing with chalk. Camera slowly pushes in on the drawing. The chalk lines shimmer and lift off the ground, animating: the dog wags its tail, birds take flight, the house glows. The child sits back, delighted. Camera pulls to wide overhead shot showing the chalk world fully surrounding her. Style: warm, soft Miyazaki-inspired palette. Light orchestral music builds.

### 71. Abandoned Theme Park Exploration
> A solo urban explorer walks through an abandoned theme park at dusk. Camera follows from behind at medium distance - steadicam, slow and steady. Overgrown carousel. He stops. Camera circles slowly. A rusted seat sways in the wind. Close-up: peeling paint, a child's handprint fossilized in grime. Wide: full park stretches behind, roller coaster sagging in distance. Low ambient drone. No dialogue.

### 72. Glassmorphic Product Reveal
> Pure white studio. A perfume bottle or tech device sits centered on a frosted glass plinth. Camera begins tight - extreme close-up on product surface. Slow rotation begins. Camera eases back in smooth dolly-out. Light refracts through product, casting shifting color halos. Final shot: product fully revealed, centered, rotating slowly. Camera locks. No music - single low ambient tone. No text, labels, or voiceover.

---

## CATEGORY 14: Food, Beverages and Urban Culture

### 73. Street Food Night Market
> Handheld camera weaves through a crowded Southeast Asian night market. Golden light from hanging bulbs reflects off wet pavement. Tight tracking shots between stalls: a wok erupts in flame, skewers char on grill, a vendor's hands fold a banana leaf around sticky rice. Medium shot: young couple shares noodles at a plastic table, steam rising between them. Camera pulls back to wide shot of the whole market. No narration. Only ambient sound.

### 74. Whisky Macro Pour
> Extreme macro commercial shot. A crystal whisky glass on dark textured surface. A slow pour from above: amber liquid streams into the glass, splashing in extreme slow motion. Droplets hang in the air catching backlight. Liquid settles, sloshing against crystal walls, tiny bubbles forming. Camera eases back to reveal full glass and bottle. Warm amber and brown color grade. Deep, low ambient hum. No voiceover.

---

## CATEGORY 15: Cinematic Trailers (from SeaArt)

### 75. Post-Apocalyptic Survivor
> Wind whips sand across the ruins of a collapsed city. A 28-year-old female survivor stands on a crumbling structure. Her torn gray cape billows in the wind; face covered in dust and old scars. She tilts her head against the gust. Something shifts on the horizon - the blurred silhouette of a mechanical creature. She raises her gaze. Her breathing steadies. Eyes shift from confusion to resolve. Camera pushes from medium shot to close-up. Sandstorm softens, light breaks through dust. Post-apocalyptic sci-fi style, desaturated earth tones. Realistic wind physics, light diffusion, fabric movement.

### 76. Retired Soldier in the Rain
> Heavy rain hammers the roof of an abandoned factory. A hard-faced man in his early 30s stands at the edge. Worn dark-gray military coat clings to soaked frame. Faint scar on right cheek flickers under distant neon glow. He looks down, lighting his last cigarette with trembling hand. Smoke barely rises before rain scatters it. Camera drifts from rear-side shot to frontal medium shot. Dark realism, high-contrast cool blue palette, cinematic film texture.

### 77. Cyberpunk Assassin
> On a rain-soaked skyscraper rooftop, a 27-year-old cyberpunk assassin crouches on one knee. Short silver hair plastered to face. Left eye - red cybernetic implant - emits faint glow. She holds a luminous dagger reflecting neon lights. The eye activates a subtle scan. Camera begins 360 orbit driven by city's shifting light. During rotation, neon reflections glide across wet metal and suit surface. Motion stops at low frontal angle. Eye glow intensifies. Cyberpunk aesthetic, high-contrast purple and red neon.

### 78. Gunslinger at Dusk
> Desert at sunset, light wind stirs fine sand. A 42-year-old cowboy stands motionless. Hat brim shadows his eyes. Gray beard sways in wind. No movement at first. Wind picks up. The moment the sun disappears below horizon, he slowly raises his hand and draws his weapon. Camera pushes from medium shot to chest-level close-up guided by light shift. Dust grows more visible, shadows lengthen. Classic Western aesthetic, warm orange tones, film grain.

### 79. Steampunk Inventor
> On the deck of a massive airship, gears turn slowly, steam vents in rhythmic bursts. A 29-year-old inventor stands at center. Copper goggles on forehead. Curly brown hair tossed by wind. She adjusts a mechanical device. Steam intensifies. She looks up. Camera moves from side angle to frontal shot driven by mechanical rhythm. Behind her, cloud sea pierced by steam columns. Steampunk aesthetic, warm copper and gold tones.

---

## CATEGORY 16: Dance

### 80. Latin Dance
> A Latin dance couple in a nocturnal tropical setting - she in a red dress, he in black shirt. 0-5s: Close spin at slow tempo; dress flows softly. 5-10s: Rhythm of @Audio1 intensifies - fast spins, leg lift, exchange of glances. 10-13s: Crossed-step sequence at denser beat. 13-15s: Musical pause and final pose in embrace. Camera transitions from circular medium shot to gradual close-up.

### 81. Neon Street Dance
> A street dancer based on @Image1, black hoodie, rainy night street lit by neon. Blurred crowd, wet ground reflecting lights. 0-3s: Subtle warm-up, shoulders following beat. 3-7s: Beat from @Audio1 drops - footwork and jumps. 7-10s: Rhythm intensifies, fast spin and landing. 10-15s: On beat drop, final freeze. Camera: handheld tracking → whip pan on accents → slow push for closing. Color particles burst on beat hits.

### 82. Cyber Electronic Dance
> A dancer floats in cyberspace environment, movements synced to @Audio1 electronic beats. 0-4s: Light floating; body vibrates with low frequencies. 4-8s: Beat starts - segmented popping moves. 8-12s: Acrobatic jump on heavy hit. 12-15s: Suspended in air during beat drop. Quick camera cuts with whip pans on accents. Neon lights pulse with rhythm, particle explosions accompany music.

---

## CATEGORY 17: Digital Avatars / Explainer

### 83. Professional Speaker
> A male speaker in his early 30s, navy suit, clean short hairstyle. Frontal medium shot, modern glass-wall office, softly blurred urban skyline. Gentle push-in. He pauses, takes soft breath, begins to speak: "AI is redefining the way we live." Lip-sync aligns with @Audio1. Hands accompany speech with natural gestures; occasional nod or slight smile. Consistent eye contact. Soft cinematic lighting, warm neutral tones.

### 84. Animated Cartoon Girl
> Cartoon-style girl with pink pigtails and large round eyes in rainbow-colored animated room. Medium shot with slight camera sway. She blinks, leans forward, says with enthusiasm: "This little trick is super useful!" Lip-sync with @Audio1. Lively expressions, gestures shifting with vocal rhythm. Warm, bright, saturated lighting.

### 85. On-Camera Host
> Polished host with long straight black hair, red lip makeup, white blouse. Medium-close frontal shot, high-end studio. Three-point lighting. Camera advances slowly. She begins: "This product will transform your daily efficiency." Precise lip-sync with @Audio1. Subtle, refined gestures. Firm eye contact. Premium aesthetic.

### 86. Veteran Historian
> Elderly historian with white hair, round glasses, gray sweater. Medium shot in ancient library, flickering candlelight. Camera slowly moves in. He looks down in reflection, raises eyes: "A thousand years ago, that battle..." Lip-sync with @Audio1. Measured gestures, occasional nod. Wisdom and calm. Warm tones, subtle cinematic grain.

---

## CATEGORY 18: Featured Prompts from the Community (GitHub)

### 87. Surreal Ronin Action Scene
> A surreal battlefield in the sky: floating rock islands drifting through a thunderstorm. A masked ronin fighting a colossal winged beast. Cinematic, 720p, 16:9, 15 seconds.
> [Watch on YouMind](https://youmind.com/en-US/seedance-2-0-prompts?id=133)

### 88. Luxury Car → Optimus Prime vs. Godzilla
> A luxury car transforming into Optimus Prime and battling Godzilla amidst explosions and energy blasts in rainy Tokyo nightscape. CGI style.
> [Watch on YouMind](https://youmind.com/en-US/seedance-2-0-prompts?id=210)

### 89. Water vs. Thunder Breathing Duel
> 15-second live-action anime adaptation. Water Breathing (blue dragon) vs. Thunder Breathing (golden lightning) duel in misty forest under moonlight. Hollywood live-action, dark samurai, 4K. Three shots with specific visual/action details.
> [Watch on YouMind](https://youmind.com/en-US/seedance-2-0-prompts?id=189)

### 90. Speeder Chase Across Cliff City
> High-speed speeder chase through monumental cliffside city in single continuous shot, culminating in waterfall-fed valley reveal.
> [Watch on YouMind](https://youmind.com/en-US/seedance-2-0-prompts?id=393)

---

## CATEGORY 19: Multi-Shot Storytelling

### 91. Robot Story (4 Scenes)
> A lonely robot wakes up in an abandoned factory (Scene 1). It walks outside and sees a sunset wasteland (Scene 2). It discovers a small flower and gently touches it (Scene 3). Finally, it looks up and smiles at the sky (Scene 4). Keep robot appearance consistent. Emotional transition from confusion to warmth. Cinematic camera, warm tones, epic mood, no flicker.

### 92. Anime Girl Healing Entrance
> An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat, standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the camera and smiles gently. A light breeze moves her hair and dress. Camera slowly pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion, high detail.

### 93. Action Fight Scene (Wuxia + Reference)
> A wuxia-style male hero (based on reference video character), wearing black martial outfit, fighting enemies in a rainy bamboo forest at night. Fast sword combos with visible sword light trails and splashing water. Fast follow camera, crane shots, and quick close-ups. Cinematic camera language. Maintain character appearance and clothing consistency. Realistic physics, wet fabric, rain interaction.

---

# 10. RESOURCES AND USEFUL LINKS

## Complete Online Guides

| Resource | Link |
|---------|------|
| Imagine.art - 70 Prompts | https://www.imagine.art/blogs/seedance-2-0-prompt-guide |
| SeaArt - 20+ Examples | https://www.seaart.ai/blog/seedance-2-0-prompt |
| GLBGPT - From Zero to Cinematic | https://www.glbgpt.com/hub/seedance-2-0-prompt-guide/ |
| WeShop - Master Prompt Script | https://www.weshop.ai/blog/seedance-2-0-guide-how-to-master-the-prompt-script/ |
| Freepik - How to Write Prompts | https://www.freepik.com/blog/how-to-write-prompts-for-seedance-2-0/ |
| WaveSpeed - Template Framework | https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/ |
| Vmake - 10 Prompt Multi-Shot | https://vmake.ai/blog/seedance-2-0-prompts |
| Atlabs - Guide 2026 | https://www.atlabs.ai/blog/seedance-2-prompts-guide |
| VideoWeb - Tutorial + Prompt | https://videoweb.ai/blog/detail/Seedance-2-0-Video-Generation-Guide-Tutorial-Prompts-578fb91b8f46/ |

## GitHub Repositories

| Repo | Link | Prompts |
|------|------|---------|
| awesome-seedance-2-prompts | https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts | 1078+ prompts |
| awesome-seedance | https://github.com/ZeroLu/awesome-seedance | Curated collection |

## Interactive Galleries

| Platform | Link |
|-------------|------|
| YouMind Gallery (video playback) | https://youmind.com/en-US/seedance-2-0-prompts |
| Seedance 2 Prompt Gallery | https://seedance2prompt.org/ |

## Access Platforms

- **Jimeng / Dreamina** (official ByteDance platform): direct access to Seedance 2.0
- **SeaArt AI**: integrates advanced video models including Kling 3.0 and Wan 2.6

---

# QUICK CHEAT SHEET

```
PERFECT PROMPT FORMULA:
Subject + Action + Camera + Scene + Style + Constraints

LENGTH: 100-280 words
ONE VERB PER SHOT
SUBJECT FIRST
POSITIVE > NEGATIVE ("detailed hands" not "no bad hands")
3-5 NEGATIVES MAXIMUM
TIMESTAMPS FOR MULTI-BEAT

REFERENCES:
@Audio = rhythm and lip-sync
@Video = movement and camera
@Image = character appearance
Max: 9 img + 3 video + 3 audio = 12 total

CAMERA VOCABULARY:
Wide = context | Medium = dialogue | Close = emotion
Dolly = cinematic | Handheld = personal | Gimbal = professional
Slow pan | One movement per shot | Lens: wide/normal/tele
```

---

---

# APPENDIX A: VIDEO TUTORIAL - Character Consistency Secrets (DeepWhite)

> **Video**: [Seedance 2.0 Advanced: Character Consistency Secrets + 3 Ideas & Prompt Templates](https://www.youtube.com/watch?v=I5xk9QiP7QM)
> **Author**: DeepWhite

## The 3 Key Lessons

### 1. Image References Are Fundamental
- Whether or not you upload a reference image has a **huge impact** on the result
- A single frontal photo is recognized, but facial features are not always maintained 100%

### 2. Use the 4 Character Views (Four Views)
- Uploading **4 character views on white background** (front, back, side, close-up) produces a **quality leap** in consistency
- The character becomes identical to the reference image
- Dynamic expressions and storyboards turn out perfect
- Even 3 views work, but 4 are recommended

### 3. Detailed Prompts for Total Control
- The model is so powerful that even simple keywords produce good results
- But if you have a precise idea in mind, detailed prompts allow you to express your vision with precision
- With detailed prompts + four views = the video perfectly follows your idea

## The 3 Production Methods

All three start from the base of **4 character views on white background**.

### Method 1: Single Image (First Frame) + Prompt

1. Think about the story and plot
2. Determine the style (photorealistic, anime, cartoon, etc.)
3. Generate or find an image representing the first frame
4. Write the detailed prompt using a template
5. Upload the 4 character views + the first frame
6. **IMPORTANT**: After uploading, verify that the image order (@Image1, @Image2...) matches the one in the prompt

**When to use**: Good for most situations

### Method 2: 4-Grid Storyboard + Prompt

1. Create a storyboard with 4 panels showing key scenes
2. Combine with the prompt template
3. Upload the 4 views + the storyboard
4. Write a general description of the story

**When to use**: Ideal for scenes with many changes, battle scenes, intense scenes. For emotional or literary dramas, it may be "too much".

**Recommended duration**: 10 or 15 seconds (shorter is not worth it with a storyboard)

### Method 3: Multimodal Approach

1. Start from the character references (4 views)
2. Optionally add: scene diagram, music, voice, etc.
3. Use the multimodal prompt template
4. The character reference is mandatory; the scene can be described via keywords only

**When to use**: When you want maximum control over all aspects (visual, audio, movement)

## Important Notes from DeepWhite

- **Jimeng/Dreamina is the fastest** for generation
- The prompt template is based on the **official Jimeng 2.0 user manual**
- To generate the 4 character views, you can use an AI image generator
- **Pay attention to the image order** when uploading: they must match the @Image1, @Image2, etc. tags in the prompt

---

# APPENDIX B: VIDEO TUTORIAL - 10 Tested Viral Prompts (Dom the AI Tutor)

> **Video**: [I Tested 10 BRUTAL Viral Seedance 2.0 Prompts!](https://www.youtube.com/watch?v=KnyrIp9qRuU)
> **Author**: Dom the AI Tutor | Tech Tutor Zones

## Lessons from the Tests

### Recommended Setup
- Model: **Seedance 2.0** (not the "fast" version -- more quality)
- Duration: **15 seconds**
- Format: **16:9**
- Prompt limit: up to **5,000 characters**

### Test 1: Multi-Shot Text-to-Video
- Complex prompt with multiple transitions
- Transitions between scenes are extremely smooth
- Comparison with Veo 3.1: Seedance wins decisively

### Test 2: Transformer (Bus that Transforms)
- Vehicle → robot transformation prompt
- Fun and convincing result

### Test 3: Omni Reference (Image + Video)
- Uploaded a creature image as reference
- Used a video as reference for movement
- **Simple prompt**: "Image one doing the same as video one"
- **Result**: Excellent character consistency, sword from the video replicated perfectly
- Facial feature consistency and sword detail are "top-notch"

### Test 4: Image-to-Video with First Frame
- Used a low-quality image as first frame
- **Prompt**: "A cinematic and chaotic tracking shot with handheld camera motion and camera shakes"
- The result improves the original image and produces an impressive video

### Test 5: Omni Reference Anime
- Two anime images + a dance video as reference
- **Prompt**: "Create a two model frame video where @Image1 and @Image2 dance and move completely the same as in @Video1"
- The anime characters replicate the movements from the reference video

### Test 6: Realism + Motion Reference
- Same technique but with a realistic person
- Added a specific action at the end ("she does a split")
- The model executes both the reference movements and the added action

### Test 7: Emotions in Multi-Shot (Text-to-Video)
- Test of facial expressions and camera movements
- Emotions are incredibly realistic
- **Perfect hands**: all finger details are correct
- The motion is fantastic

### Test 8: Complex Battle Scene
- Prompt of nearly **3,000 characters**
- Specified "without cuts" → result without cuts, continuous camera transition
- The spaceship appears cinematically

### Test 9: Airplane → Transformer Transformation
- Airplane landing + transformation into transformer
- "Brutal" and convincing result

### Test 10: First Frame + Last Frame
- Used first and last frame
- Character consistency between the two frames is excellent

### Bonus: Cat Kung Fu (Viral)
- Text-to-video prompt of cats fighting kung fu
- Model comparison:
  - **Seedance 2.0**: BEST overall
  - **Kling 3.0**: Good, but not at Seedance level
  - **Grok**: Better than Veo, worse than Seedance
  - **Sora**: Mediocre results, unrequested slow motion
  - **Veo 3.1**: The worst in the comparison

## Model Ranking (from the video)

1. **Seedance 2.0** — The best
2. **Kling 3.0** — Good
3. **Grok** — Decent
4. **Sora** — Mediocre
5. **Veo 3.1** — The worst (surprisingly)

## Platform Used
- **LumaFlow AI**: Has Seedance 2.0 available globally + all other video/image models in one place

---

> Document compiled on March 24, 2026 from 9 web sources + 2 YouTube videos.
> Sources: Imagine.art, SeaArt, GLBGPT, WeShop, WaveSpeed, Vmake, GitHub/YouMind-OpenLab, Atlabs, VideoWeb, DeepWhite (YouTube), Dom the AI Tutor (YouTube).
