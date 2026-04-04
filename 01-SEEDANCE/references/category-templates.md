# Category Templates — Seedance 2.0 Reference

> Each template is a ready-to-adapt structure. Replace [bracketed] items with specific content.
> All templates assume Seedance 2.0 video generation. Combine with style anchors, camera grammar, and lighting vocabulary from other reference files.

---

## 1. Cinematic / Narrative

### Template

```
[Style anchor: e.g., "Shot on ARRI Alexa Mini, Cooke S7 anamorphic lenses, 2.39:1 aspect ratio."]

Scene opens on [location description — time of day, weather, atmosphere].
[Lighting direction: e.g., "Golden hour backlight rakes across the scene, deep amber fill from camera-left."]

0:00–0:02 — [Opening composition]. Camera holds a [wide/medium/close] shot of [subject]. [Atmospheric detail: dust, fog, rain, light shafts].
0:02–0:05 — [Camera movement: e.g., "Slow dolly-in from medium-wide to medium close-up"]. [Subject action: what they do, how they move]. [Emotional tone: contemplative, tense, euphoric].
0:05–0:08 — [Second beat: new angle or action]. [Cut or continuous move]. [Detail that grounds the scene: texture, reflection, environmental reaction].
0:08–0:10 — [Closing composition]. Camera [final movement: e.g., "cranes up and away"]. [Final atmospheric detail]. [Emotional landing].

Color grade: [palette description — e.g., "Teal shadows, warm amber highlights, crushed blacks, filmic grain"].
Sound design: [ambient layers — e.g., "Distant wind, muffled footsteps on wet stone, low cello drone"].
```

### Settings
- **Mode:** Standard or Fast (Standard for maximum quality)
- **Aspect Ratio:** 16:9 (cinematic default) or 21:9 (anamorphic widescreen)
- **Duration:** 5s or 10s (10s preferred for narrative arc)

### Key Rules
1. Always open with a style anchor referencing real camera + lens combinations to lock in the cinematic look.
2. Structure the prompt as a timeline with specific second markers — this gives the model temporal guidance.
3. Separate lighting, color grade, and sound design into their own lines; bundling them into action descriptions weakens each.
4. Use atmospheric micro-details (dust motes, breath vapor, lens flares) to sell realism.
5. End every cinematic prompt with a defined emotional landing — the model generates more coherent endings when told how the scene should feel at the close.

---

## 2. Action / Combat

### Template

```
Cinematic action sequence from a [genre: war film / martial arts epic / sci-fi thriller / heist film].
[Style anchor: e.g., "Shot on RED V-Raptor, 120fps overcranked, Zeiss Supreme Prime lenses. Directed by [reference director]."]

Context: [Brief narrative wrapper — e.g., "A lone samurai faces three attackers in a rain-soaked courtyard at dusk."]

First Frame: [Precise description of the opening composition — pose, expression, environment, lighting].

0:00–0:02 — [Tension beat: anticipation before action]. Camera holds [shot type]. [Atmospheric detail: wind, rain, silence].
0:02–0:04 — [Primary action burst]. [Choreography description using specific movement vocabulary: "lunges," "pivots," "deflects," "rolls"]. Camera [tracking method: Steadicam orbit / whip-pan / crash-zoom]. [Impact detail: sparks, debris, fabric ripple].
0:04–0:07 — [Escalation or counter-move]. [Slow-motion moment at key impact — "overcranked to 120fps as..."]. [Environmental reaction: objects scatter, surface cracks, water splashes].
0:07–0:10 — [Resolution beat]. [Final stance or aftermath]. Camera [pulls back / pushes in]. [Settling atmosphere: dust falling, echo fading].

Last Frame: [Precise description of final composition — decisive pose, aftermath, emotional state].

Choreography note: All movements serve the narrative of [conflict context]. This is a cinematic action scene depicting stylized, consequence-driven conflict.
```

### Settings
- **Mode:** Standard (for motion fidelity)
- **Aspect Ratio:** 16:9 or 21:9
- **Duration:** 5s–10s (longer durations for multi-beat choreography)
- **Consider:** First+Last frame image inputs for pose control

### Key Rules
1. Always wrap combat in a cinematic narrative context — "a scene from a film" or "cinematic action sequence" — never describe violence as standalone.
2. Use first-frame and last-frame image inputs when precise poses matter; the model follows endpoints better than mid-sequence choreography descriptions alone.
3. Describe impacts through environmental reactions (sparks, debris, water displacement) rather than injury; this maintains generation compliance and looks better.
4. Include at least one speed variation (slow-motion beat) to add rhythm and give the model a clear temporal anchor.
5. Use specific choreography verbs (deflects, pivots, vaults, rolls) instead of vague terms (fights, attacks) — precision yields better motion.

---

## 3. Fashion / Runway

### Template

```
[Style anchor: e.g., "Vogue Italia editorial. Shot on Hasselblad H6D-100c, 80mm lens, f/2.8."]

[Model description: gender, build, skin tone, hair — keep specific but respectful]. Wearing [garment description: fabric, cut, color, designer reference if relevant. e.g., "a floor-length ivory silk charmeuse gown with a dramatic cowl back, fabric pooling at the hem"].

Setting: [Environment — e.g., "minimalist concrete runway, 200 meters long, low fog at ankle height"].
Lighting: [Fashion-specific lighting — e.g., "Overhead strip softboxes creating a cathedral of light, hard specular highlights on the fabric, deep shadows flanking the runway"].

0:00–0:03 — Camera positioned at hip height, 24mm wide angle. [Model] walks toward camera with [gait description: confident stride, languid pace, editorial stomp]. Fabric [physics description: "catches air and billows behind," "clings and shifts with each step," "swings in a heavy pendulum arc"].
0:03–0:06 — Camera shifts to [side tracking / 3/4 angle / low angle at foot level]. [Detail moment: fabric texture catches light, jewelry glints, hair moves]. Wind [direction and intensity].
0:06–0:08 — [Pose moment or turn]. [Model] pauses, [pose description with weight and attitude]. Camera slowly orbits [direction].
0:08–0:10 — [Exit or final composition]. [Fabric settling, silhouette against light].

Post-processing: [Color treatment — e.g., "Desaturated earth tones, high contrast, film grain reminiscent of Peter Lindbergh"].
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 9:16 (vertical / portrait editorial) or 16:9 (runway wide)
- **Duration:** 5s–10s

### Key Rules
1. Camera at hip height is the default fashion camera — it elongates the figure and matches editorial convention. Specify this explicitly.
2. Fabric physics must be described in detail: how the material moves, catches light, and responds to motion. Use textile vocabulary (charmeuse, organza, gabardine, bouclé, crepe, tulle).
3. Reference real fashion photographers or magazines as style anchors — the model responds to these aesthetic associations.
4. Describe the model's attitude and gait, not just their appearance — walk style is half the fashion story.
5. Always include at least one fabric-specific light interaction (specular highlight on silk, matte absorption on wool, translucency of chiffon against backlight).

---

## 4. Beauty / Skincare / Makeup

### Template

```
[Style anchor: e.g., "Glossier campaign aesthetic. Shot on Canon EOS R5, 100mm macro lens, f/2.0. Ring light + diffused beauty dish."]

Extreme close-up on [face zone: lips, eye, cheekbone, full face from nose to forehead]. [Skin description: dewy, porcelain, sun-kissed, glass-skin finish — be specific about texture and sheen].

Product: [Product name/type, color, finish — e.g., "a rose-quartz liquid blush with a luminous satin finish"].

Lighting: [Beauty-specific lighting — e.g., "Butterfly lighting from directly above, soft fill below chin to eliminate shadows, catch light centered in both irises"].

0:00–0:02 — Macro lens focused on [skin surface / lip texture / lash line]. [ASMR-satisfying detail: visible skin texture at pore level, light refracting through product sheen]. Shallow depth of field, background melts to a [color] bokeh.
0:02–0:05 — [Application moment or reveal: e.g., "Fingertip gently presses product onto the apple of the cheek, pigment blooms outward in a natural flush"]. Camera [micro-movement: barely perceptible drift, gentle rack focus].
0:05–0:08 — [Pull back to medium close-up revealing full effect]. [Expression: subtle smile, eyes open to camera, slow blink]. [Light interaction with product: dewy highlight catches on cheekbone, lip gloss refracts a prismatic flare].
0:08–0:10 — [Final beauty shot]. Perfect stillness. [One micro-detail: a single catch light, a strand of hair across the brow, the sheen on the cupid's bow].

Color: [Clean, skin-true palette — e.g., "Warm neutral grade, skin tones protected, whites slightly creamy"].
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 9:16 (vertical for social) or 1:1 (square for beauty grids)
- **Duration:** 5s–10s

### Key Rules
1. Macro lens specification is essential — it tells the model to render skin texture, pore-level detail, and product sheen at extreme close range.
2. Describe product application as a sensory, ASMR-satisfying moment: the press, the bloom, the blend. Avoid clinical language.
3. Catch lights in the eyes must be specified — they are the hallmark of professional beauty photography and the model will include them if asked.
4. Keep camera movement minimal and smooth; beauty content demands near-stillness with only micro-drifts or gentle rack focuses.
5. Maintain product coherence: if the product is rose-toned, the lighting, grade, and surrounding palette should harmonize, not clash.

---

## 5. Product / Commercial

### Template

```
[Style anchor: e.g., "Apple product launch film. Shot on RED Komodo, 50mm macro, controlled studio lighting."]

Product: [Detailed product description — material, color, finish, size, distinguishing features. e.g., "A matte black titanium wristwatch with a sapphire crystal dial, brushed lugs, and a midnight blue leather strap"].

Setting: [Environment — e.g., "Infinite black void" / "White cyclorama" / "Contextual lifestyle setting: marble countertop with morning light"].
Lighting: [Product-specific lighting — e.g., "Single overhead softbox with a hard kicker from camera-right creating an edge highlight along the case. Subtle gradient on the background from charcoal to pure black"].

0:00–0:03 — Product enters frame via [method: rising from shadow, rotating into view, placed by a hand, revealed by light sweep]. Camera holds a [shot type: hero angle, 3/4 elevated, straight-on profile]. [Key material detail catches light: brushed metal gleams, glass refracts, fabric texture becomes visible].
0:03–0:06 — [Orbit or macro transition]. Camera [360-degree orbit at product height / slow push-in to macro detail / smooth arc from side to top-down]. [Highlight a specific feature: the clasp mechanism, the texture of the surface, the logo engraving]. Lighting shifts subtly to [reveal a new surface quality].
0:06–0:08 — [Detail macro beat]. Extreme close-up on [signature detail]. [Material interaction with light: anodized aluminum scatters soft blue reflections, leather grain creates micro-shadows, glass surface shows environment reflection].
0:08–0:10 — [Hero landing shot]. Product settles into [final composition: centered, rule-of-thirds, floating]. [Tagline-ready frame]. Background [treatment: gradient, environmental context, pure void].

Post: [Premium grade — e.g., "High contrast, deep blacks, color-accurate product tones, no color cast on whites"].
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 16:9 (landscape commercial) or 1:1 (social/e-commerce)
- **Duration:** 5s–10s

### Key Rules
1. Material description is paramount — the model needs to know if a surface is brushed, polished, matte, anodized, translucent, or textured to render it correctly.
2. Lighting must be described in terms of what it reveals on the product, not just its position. "A kicker that traces the edge" is better than "a light from the right."
3. Include at least one macro detail beat — this is the "hero moment" that sells premium feel.
4. Avoid putting the product in motion unless the motion reveals something (a mechanism, a pour, an unfolding). Stillness with moving light/camera reads as more premium.
5. End on a "poster frame" — a composition clean enough to freeze as a print ad.

---

## 6. Viral / UGC / Social Media

### Template

```
[Style anchor: e.g., "iPhone 16 Pro handheld footage. Slightly shaky, natural lighting, raw and unpolished."]
[Format: TikTok / Instagram Reels / YouTube Shorts]

Hook (0:00–0:02): [Immediate visual hook — the thing that stops the scroll. e.g., "A hand flips a pancake three meters into the air" / "Close-up of a satisfying peel" / "Someone turns around to reveal an unexpected transformation"]. This is the ENTIRE reason someone watches. Front-load the spectacle.

0:02–0:04: [Payoff or escalation of the hook]. [Reaction beat: genuine surprise, laughter, awe]. Camera [handheld, selfie-angle, POV, over-the-shoulder]. [Authentic detail: imperfect framing, natural background noise implication, real-world environment].

0:04–0:05: [Closing beat — either a punchline, a reveal, or a loop point that connects back to the opening frame for seamless replay].

[Optional text overlay direction: "TEXT APPEARS: '[viral caption]' in bold white Impact font, center frame"]

Environment: [Everyday setting — bedroom, kitchen, street, car, office. Mundane = relatable].
Talent: [Natural, unposed. Describe as a real person, not a model. e.g., "A twentysomething in an oversized hoodie and messy bun"].
```

### Settings
- **Mode:** Fast (matches the raw, unpolished feel; quick iteration)
- **Aspect Ratio:** 9:16 (vertical — mandatory for Reels/TikTok/Shorts)
- **Duration:** 5s (short, punchy, replayable)

### Key Rules
1. The hook must land in the first 2 seconds — describe the most visually arresting moment first. If the scroll-stopping moment is at second 4, restructure so it opens the video.
2. One concept per video. Do not try to tell a story with a twist AND a product reveal AND a reaction. Pick one.
3. Imperfection is the aesthetic — specify handheld camera, natural light, slightly off-center framing. Overproduced = ignored on social feeds.
4. Design for the loop: the last frame should visually or conceptually connect to the first, encouraging replay.
5. Keep it short. 5 seconds is the ideal Seedance length for viral content. If it can be said in 5 seconds, do not use 10.

---

## 7. Educational / Science

### Template

```
[Style anchor: e.g., "Kurzgesagt-inspired CGI visualization" / "National Geographic documentary" / "Medical animation, photorealistic subsurface rendering."]

Subject: [The concept, process, or structure being explained. e.g., "Mitochondrial ATP synthesis" / "Tectonic plate subduction" / "How mRNA vaccines trigger immune response"].

0:00–0:03 — [Establishing context]. Camera [smooth dolly or crane] reveals [the macro environment: a cell interior, a geological cross-section, a circuit board landscape]. [Scale reference to orient the viewer: "We are at 10,000x magnification inside a human cell" / "Aerial view of a continental plate boundary spanning 500 kilometers"].

0:03–0:06 — [Process visualization]. [The key mechanism in action, described step by step]. [Structures described with transparency and cutaway: "The ribosome, rendered as a translucent blue-green molecular structure, slides along the mRNA strand"]. Camera [follows the process: tracking alongside a molecule, orbiting a structure, dollying through a cross-section].

0:06–0:08 — [Detail or consequence]. [Zoom into a critical sub-process or pull out to show the result]. [Color-coding or highlighting: "The ATP molecules glow amber as they release from the synthase complex"]. [Annotation-friendly composition: clean framing with space for labels].

0:08–0:10 — [Resolution or wider context]. Camera [pulls back to show the full system / the cycle repeating / the real-world implication]. [Sense of wonder beat: scale shift, beautiful rendering, "the elegance of the mechanism revealed"].

Rendering style: [e.g., "Photorealistic molecular rendering with subsurface scattering, ambient occlusion, depth-of-field at macro scale. Color palette: deep navy background, structures in cyan, amber, and soft white"].
```

### Settings
- **Mode:** Standard (complex rendering benefits from quality mode)
- **Aspect Ratio:** 16:9 (landscape — standard for educational content)
- **Duration:** 10s (processes need time to unfold)

### Key Rules
1. Use transparency and cutaway descriptions liberally — the model renders "translucent cell membrane" or "cross-sectioned engine block" far better when explicitly told.
2. Include a scale reference early so the viewer (and the model) knows the spatial context.
3. Describe processes as sequential steps with cause and effect — "the enzyme binds, which triggers a conformational change, which releases the substrate."
4. Color-code functional elements (energy = amber, structure = blue, signal = green) for clarity, and state this in the prompt.
5. Keep camera movements smooth and deliberate (dolly, crane, orbit) — jerky or fast movements undermine the educational authority of the piece.

---

## 8. Anime / Animation

### Template

```
[Style anchor: e.g., "Studio Ghibli hand-painted animation style" / "Makoto Shinkai — Your Name color palette and lighting" / "Mappa studio action animation, Jujutsu Kaisen fluidity" / "Cel-shaded anime, 24fps on twos"].

Character: [Detailed character description — hair color/style, eye color, outfit, distinguishing features, expression. e.g., "A young woman with waist-length silver hair, violet eyes, wearing a dark blue military coat with gold epaulettes, expression of quiet determination"].

Scene: [Environment in anime terms — e.g., "A rooftop overlooking a neon-lit Tokyo cityscape at twilight, cherry blossom petals drifting across the frame"].

0:00–0:03 — [Opening beat]. [Character pose or action in anime visual language: "wind catches her hair as she turns toward camera"]. [Signature anime lighting: rim light separating character from background, lens flare, god rays through clouds]. [Animation-specific detail: "hair animated with fluid secondary motion, 12 distinct strands moving independently"].

0:03–0:06 — [Primary action or emotional beat]. [Movement described in animation terms: "smear frames on the sword swing," "speed lines radiate from the point of impact," "slow-motion mid-air with clothes rippling"]. [Background treatment: parallax scrolling, painted sky, bokeh city lights].

0:06–0:08 — [Reaction or consequence]. [Close-up on face: eye animation detail, "pupils contract, a single tear catches the light"]. [Atmospheric particles: petals, embers, snow, dust motes]. [Color shift to match emotional tone].

0:08–0:10 — [Closing composition]. [Iconic pose or wide shot that could be a key visual / poster frame]. [Final atmospheric detail]. [Hold on the composition for emotional weight].

Animation notes: Maintain consistent [style anchor] throughout. [Frame rate feel: "smooth 24fps on ones for action, on twos for dialogue moments"]. Avoid 3D-feeling camera moves — keep to anime-conventional pans, tilts, and push-ins.
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 16:9 (standard anime) or 9:16 (anime-style vertical content)
- **Duration:** 5s–10s

### Key Rules
1. The style anchor is the single most important line — it must name a specific studio, director, or series to lock the visual style. Generic "anime style" yields inconsistent results.
2. Describe animation-specific motion language: smear frames, speed lines, secondary motion on hair/fabric, on-twos vs. on-ones timing. The model responds to these as visual cues.
3. Anime lighting has its own conventions — strong rim lights, dramatic color shifts for mood, lens flares that are stylized rather than photorealistic. Describe these explicitly.
4. Maintain character consistency by front-loading detailed character description. If generating multiple clips of the same character, repeat the description verbatim.
5. Avoid describing camera movements that break anime convention (Steadicam, handheld shake) — use pans, tilts, zooms, and push-ins that feel hand-animated.

---

## 9. Music Video / Dance / Beat-Sync

### Template

```
[Style anchor: e.g., "Hype Williams 90s music video aesthetic, fisheye lens, high-contrast lighting" / "Spike Jonze single-take dance film" / "K-pop MV — high production, rapid cuts, neon lighting"].

@Audio: [Audio reference file or description — e.g., "Uploaded track: 128 BPM, drop at 0:03, synth hook at 0:05"]

Performer: [Description — appearance, outfit, energy level. e.g., "A dancer in a reflective silver bodysuit, face partially obscured by dramatic shadow, moving with sharp isolations and fluid transitions"].

Setting: [Music video environment — e.g., "An infinite mirror room with magenta and cyan LED strips reflecting infinitely" / "A rooftop at golden hour with the city below"].

Beat map:
0:00–0:02 (BPM: [tempo], pre-drop buildup) — [Slow, tension-building movement]. Camera [static or slow push-in]. Performer [contained movement: subtle body roll, head turn, hand gesture]. Lighting [minimal, building].
0:02–0:04 (beat drop) — [Explosive movement synced to the drop]. Camera [dynamic: whip-pan, crash-zoom, orbit acceleration]. Performer [full choreography burst: "hits the beat with a sharp chest pop into a full-body wave"]. Lighting [peaks: strobes, color wash shift, practical lights flash].
0:04–0:07 (hook/chorus) — [Sustained energy]. Camera [dynamic tracking: Steadicam circle, drone pull-up, low-angle tracking backward as performer advances]. [Choreography description with beat-sync markers: "on every downbeat, a sharp arm extension; on every upbeat, a fluid recovery"]. [Environmental sync: lights pulse with rhythm].
0:07–0:10 (outro/breakdown) — [Energy shift: either peak climax or sudden stillness]. Camera [final dramatic move]. Performer [final pose or continued movement fading]. [Atmospheric punctuation: confetti drop, smoke burst, lights cut to silhouette].

Edit rhythm: Cuts [on-beat / off-beat / continuous single-take]. Visual rhythm matches audio rhythm throughout.
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 16:9 (cinematic MV) or 9:16 (vertical dance content)
- **Duration:** 10s (needs length for beat-sync payoff)
- **Audio:** Upload reference track or use @Audio tag

### Key Rules
1. Map choreography to specific beats — describe what happens on the downbeat, upbeat, and at the drop. Vague "dances to the music" yields generic motion.
2. Use the @Audio reference tag if uploading a track; describe the BPM and key musical moments (drop, hook, break) in the prompt as redundant guidance.
3. Camera movement should mirror musical energy: slow during build-up, dynamic during drops, still during breakdowns.
4. Specify whether the video is a single continuous take or uses cuts — this fundamentally changes the generation approach.
5. Lighting should react to the music: strobes on beats, color washes on chord changes, darkness during quiet moments. State this explicitly.

---

## 10. Drama / Dialogue

### Template

```
[Style anchor: e.g., "A24 indie drama. Shot on 16mm film, Panavision Ultra Speed lenses, natural window light. Directed in the style of [reference director]."]

Characters:
- Character A: [Name/label], [appearance], [emotional state — e.g., "barely holding composure, jaw tight, eyes wet"].
- Character B: [Name/label], [appearance], [emotional state — e.g., "quiet fury masked by stillness, hands gripping the chair arm"].

Setting: [Intimate environment — e.g., "A small kitchen, late afternoon. Warm light from a single window. Cluttered countertops, a half-empty bottle of wine between them."]

Scene description (visual, non-dialogue):
0:00–0:03 — Medium two-shot. Both characters seated at [location]. [Spatial relationship: facing each other, side by side, one standing over the other]. Character A [physical action: looks down, swallows, fingers trace the rim of a glass]. Character B [reaction: watches, unmoving, breath visible]. [Ambient detail: clock ticking, fridge humming].

0:03–0:06 — [Shot change: close-up on Character A]. [Micro-expression beat: "the corner of their mouth tightens, eyes narrow almost imperceptibly, then look away"]. [Background shifts to soft bokeh]. [Lighting detail: a shadow crosses their face as a cloud passes the window].

0:06–0:08 — [Reverse to Character B or return to two-shot]. [Reaction: physical, not verbal — a hand withdraws, a chair pushes back, eyes close briefly]. [Environmental shift: the light dims, the room feels smaller].

0:08–0:10 — [Resolution beat]. [One character breaks the tableau: stands, reaches out, turns away]. [Final composition: the space between them — literal and emotional — is the subject of the frame].

Dialogue guidance (if using speech): Character A says: "[Line]" — tone: [whispered / strained / flat / breaking]. Character B responds: "[Line]" — tone: [cold / tender / deflecting].

Mood: [Overall emotional tenor — e.g., "The weight of words unsaid. Quiet devastation."]
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 16:9 (cinematic) or 4:3 (intimate, indie feel)
- **Duration:** 10s (drama needs room to breathe)

### Key Rules
1. Separate the scene description (visual) from dialogue. The model processes visual staging and speech differently — keep them in distinct blocks.
2. Drama lives in micro-expressions. Describe face and hand movements at a granular level: "jaw tightens," "finger taps once then stops," "eyes dart left then back."
3. Use the environment as emotional metaphor — light dimming as tension rises, space between characters widening, an object between them as a barrier.
4. If including dialogue, always specify tone and delivery (whispered, flat, breaking) alongside the words. The same line delivered differently is a different scene.
5. Less camera movement, more shot composition. Let the actors (and the space) do the work. Locked-off shots and slow pushes read as intentional and controlled.

---

## 11. VFX / Fantasy / Sci-Fi

### Template

```
[Style anchor: e.g., "Industrial Light & Magic VFX, photorealistic compositing" / "Weta Digital creature work" / "Denis Villeneuve Dune-scale epic, IMAX format"].
[Quality anchor: "Photorealistic VFX, physically accurate light transport, volumetric atmospheric rendering, 8K texture detail."]

World: [Environment at epic scale — e.g., "A shattered planet hangs in a violet nebula, debris rings orbiting slowly. On the surface below, a crystalline citadel rises from black sand dunes, its spires refracting starlight into prismatic beams."]

Subject: [Character or entity — e.g., "A colossal guardian entity, 200 meters tall, formed of molten obsidian and veined with glowing amber magma, ancient runes carved into its shoulders."]

0:00–0:03 — [Epic establishing shot]. Camera [sweeping crane / orbital drone / IMAX-scale wide]. [Scale reference: tiny figures, vehicles, or structures against the massive environment/entity]. [Atmospheric layers: volumetric fog, particle systems, light scattering through atmosphere]. [One awe-inducing detail that sells the scale].

0:03–0:06 — [Action or revelation beat]. [The VFX centerpiece moment: portal opens, creature moves, structure transforms, energy discharge]. Described with physical plausibility: [light behaves correctly around the effect, environment reacts — dust lifts, water ripples, air shimmers with heat distortion]. Camera [responds to the event: shakes subtly, adjusts exposure, pulls focus].

0:06–0:08 — [Consequence or detail]. [Cut to ground level or character perspective showing the scale/impact]. [Particle effects: embers, energy sparks, crystalline fragments]. [Sound-design-implying visuals: shockwave ripple, bass-drop dust lift].

0:08–0:10 — [Final epic composition]. [Wide or ultra-wide shot placing everything in context]. [Atmospheric coherence: all lighting, particles, and effects unified]. [Awe beat: hold on the composition to let the scale register].

VFX notes: All effects [physically motivated / stylized-but-consistent]. Lighting [unified — single dominant light source plus atmospheric scatter]. Atmosphere [thick/thin, color, particle density].
```

### Settings
- **Mode:** Standard (VFX demands maximum render quality)
- **Aspect Ratio:** 16:9 or 21:9 (epic widescreen)
- **Duration:** 10s (scale needs time to register)

### Key Rules
1. Open with a quality anchor that specifies rendering approach — "photorealistic VFX," "physically accurate lighting," "volumetric rendering." This sets the fidelity bar.
2. Scale requires reference: always include something of known size (a human figure, a vehicle, a building) next to the fantastical element. Without scale reference, nothing looks big.
3. Describe how light interacts with every VFX element — energy glows illuminate nearby surfaces, translucent materials scatter light, metallic surfaces reflect the environment. Unlit VFX looks composited-on.
4. Atmospheric coherence is non-negotiable: fog, haze, and particles must exist consistently across the entire frame, not just around the hero element.
5. Let the camera respond to VFX events — subtle shake on impacts, exposure adjustment for bright flashes, rack focus as scale shifts. A passive camera feels disconnected from the world.

---

## 12. Landscape / Nature / Travel

### Template

```
[Style anchor: e.g., "BBC Planet Earth III. Shot on RED V-Raptor 8K with Fujinon Premista zooms. Aerial unit: DJI Inspire 3."]
[Sub-style: Aerial establishing / Ground-level intimate / Golden hour atmospheric / Storm documentary]

Location: [Specific or evocative location — e.g., "The Lofoten Islands, Norway — a jagged granite archipelago rising from an arctic sea under the midnight sun."]

0:00–0:03 — [Grand establishing shot]. [Aerial or elevated perspective]. Camera [drone ascending from valley floor / helicopter tracking along coastline / crane rising above treeline]. [Scale: "mountains stretch to every horizon, their peaks catching the last amber light while valleys below fill with blue shadow"]. [Atmospheric condition: "low clouds thread through the passes like rivers of cotton"].

0:03–0:06 — [Transition to ground level or mid-scale]. [Nature detail: "the camera pushes through a canopy of moss-covered birch, revealing a turquoise glacial stream below"]. [Textural richness: water surface, rock grain, foliage movement]. [Wildlife if applicable: "an arctic fox pauses on a ridge, fur ruffling in the wind, then continues across the snow"].

0:06–0:08 — [Intimate detail or temporal shift]. [Macro nature moment: "dew on a spider web catches morning light like a string of diamonds" / "time-lapse: wildflowers open as the shadow of a cloud crosses the meadow"]. [Atmospheric shift: light changes, weather moves in or out, golden hour deepens].

0:08–0:10 — [Final panoramic or emotional closure]. [The iconic postcard shot: "wide-angle silhouette of the mountain range against a sky burning through layers of orange, magenta, and indigo"]. Camera [holds or executes a final slow move: tilt up to sky, pull back to reveal full scope]. [Sense of place crystallized in a single frame].

Color: [Nature-true or stylized — e.g., "Rich, saturated earth tones. Shadows lean cool blue, highlights warm amber. No artificial color grading — let the landscape speak."]
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 16:9 (landscape default) or 21:9 (ultra-wide panoramic)
- **Duration:** 10s (landscapes reward patient pacing)

### Key Rules
1. Open with the widest, most impressive perspective, then narrow to details. The reverse order (starting small) works for mystery/reveal but is unconventional for landscape.
2. Name or evoke specific locations — "Norwegian fjords" generates different results than "mountainous coastline." Geographic specificity drives visual accuracy.
3. Atmospheric conditions are the landscape's lighting setup: describe clouds, haze, golden hour, storms, mist, and fog as precisely as you would describe studio lighting.
4. Include at least one scale transition (aerial to ground, wide to macro) to create visual depth and narrative progression within the landscape.
5. Nature footage demands slow, smooth camera movement — drone glides, dolly pushes, gentle cranes. Anything fast or jerky feels like amateur footage rather than professional documentary.

---

## 13. Food / ASMR

### Template

```
[Style anchor: e.g., "Bon Appetit test kitchen aesthetic. Shot on Sony FX6, 90mm macro lens, f/2.5. Overhead rig + 45-degree hero angle."]

Dish/Subject: [Detailed food description — e.g., "A thick-cut ribeye steak, reverse-seared, resting on a black slate board. The surface is a deep mahogany crust with visible Maillard reaction, juices pooling around the base. A sprig of rosemary and a pat of compound butter melting on top."]

Lighting: [Food-specific lighting — e.g., "Large softbox at 10 o'clock creating a gentle fall-off across the plate. Hard backlight at 2 o'clock catching steam and creating a rim on the butter. Dark, moody background."]

0:00–0:02 — [Hero shot: the money angle]. Camera at [45 degrees / overhead / eye-level with the plate]. [Initial spectacle: "steam rises in a lazy curl from the steak surface, backlit to a golden haze"]. [Texture detail at this distance: crust granularity, sauce viscosity, garnish freshness].

0:02–0:05 — [The satisfying action — the ASMR moment]. [e.g., "A knife cuts slowly through the steak, revealing a perfect medium-rare gradient from rosy pink center to seared edge. Juices bead along the cut surface and run onto the slate."]. [Sound-implying visuals: the resistance of the knife, the give of the flesh, the sizzle of butter]. Camera [tight macro, following the action].

0:05–0:08 — [Secondary detail or plating moment]. [e.g., "A spoon drizzles chimichurri across the sliced steak in a controlled zigzag, bright green herbs contrasting against the dark crust"]. [Movement: sauce flowing, cheese pulling, bread tearing, chocolate pouring — always with visible texture and viscosity]. Camera [slow orbit or gentle pull-back].

0:08–0:10 — [Final beauty shot]. [Complete composition: the full dish in its final plated form, garnished, lit perfectly]. [One final sensory detail: a wisp of steam, a bubble popping in a sauce, butter still melting]. [Frame holds — poster-worthy food photography].

Color: [Warm, appetite-driven palette — e.g., "Rich warm tones, deep shadows, saturated reds and ambers. Greens kept vibrant and natural. No blue cast."]
```

### Settings
- **Mode:** Standard
- **Aspect Ratio:** 9:16 (vertical for social food content) or 16:9 (horizontal for cooking shows) or 1:1 (Instagram food grid)
- **Duration:** 5s–10s

### Key Rules
1. The "satisfying moment" is the centerpiece — the cut, the pour, the pull, the drizzle, the sizzle. Identify it and build the entire prompt around it.
2. Food lighting has strict conventions: backlight catches steam and creates depth, side light reveals texture, overhead eliminates harsh shadows on flat dishes. Specify these interactions.
3. Describe texture with sensory vocabulary: crispy, gooey, caramelized, glistening, flaky, molten, charred, velvety. These words drive the model's rendering of surface quality.
4. Temperature cues matter: steam, melting butter, condensation on a cold glass — these signal freshness and make food feel alive rather than plastic.
5. Color palette must stay warm. Blue-toned food looks unappetizing. Specify warm white balance and appetite-driven color grading.

---

## 14. E-commerce / Product Showcase

### Template

```
[Style anchor: e.g., "Apple.com product page hero video. Shot on [camera], [lens], controlled studio environment."]

Product: [Precise product description — type, material, color, size, key selling points. e.g., "A pair of over-ear wireless headphones in matte pearl white. Memory foam ear cushions covered in protein leather. Brushed aluminum hinges. The brand logo is subtly embossed on the outer cup."]

Background: [Clean, conversion-optimized — e.g., "Pure white cyclorama, seamless horizon" / "Soft warm gray gradient" / "Contextual lifestyle flat-lay with complementary props"].

Lighting: [E-commerce-specific: even, flattering, product-true color — e.g., "Two large strip softboxes at 45-degree angles for even coverage, one overhead hair light for edge definition, white bounce below to fill shadows. No colored gels — accurate product colors are mandatory."]

0:00–0:02 — [Product reveal]. Product [enters frame: descends from above, slides in from side, assembles from deconstructed parts, or simply fades in from white]. Camera at [standard e-commerce angle: slightly elevated 3/4 view]. [First impression: clean, aspirational, premium].

0:02–0:04 — [360-degree rotation or key-angle showcase]. Product rotates [clockwise, smooth, 180 degrees over 2 seconds] OR camera [orbits the product at a fixed height]. [Each angle reveals a feature: side shows the button layout, back shows the adjustable headband, bottom shows the charging port].

0:04–0:07 — [Feature callout sequence]. [Macro push-in to hero feature: "Close-up on the brushed aluminum hinge mechanism as it smoothly folds, light catching each machined groove"]. Then [pull back or cut to second feature]. [Optional: deconstructed/exploded view showing internal components separating and floating in space].

0:07–0:10 — [Hero landing with lifestyle context or clean packshot]. Product [settles into final position / is shown in use context: on a person's head, on a desk, next to a phone]. [Final frame is the "buy now" image: centered, clean, high-resolution, color-accurate]. [Optional: product variants appear alongside — showing available colors].

Post: [Color-accurate, no stylization. Product colors must match real-world appearance. Clean whites, true blacks, accurate hues.]
```

### Settings
- **Mode:** Standard (for clean, sharp rendering) or Fast (for rapid A/B variant testing)
- **Aspect Ratio:** 1:1 (product grid/listing) or 16:9 (product page hero) or 9:16 (social shopping ads)
- **Duration:** 5s–10s

### Key Rules
1. Color accuracy is non-negotiable in e-commerce. Specify "product colors must match real-world appearance" and avoid stylized color grading that misrepresents the item.
2. The 360-degree rotation or multi-angle showcase is the core e-commerce motion pattern — include it in every product prompt. Customers expect to see all sides.
3. Show at least one feature in macro detail — this replaces the "zoom on hover" experience of static product pages and builds purchase confidence.
4. End on a "packshot" or "hero" frame that could be extracted as a still for the product listing page. The last frame should be the cleanest composition.
5. If the product comes in variants (colors, sizes), mention this in the closing beat — showing the range in a single video increases engagement and reduces the need for multiple assets.

---

## Quick-Reference: Settings Matrix

| Category | Preferred Mode | Preferred AR | Preferred Duration | Special Input |
|---|---|---|---|---|
| 1. Cinematic / Narrative | Standard | 16:9 / 21:9 | 10s | -- |
| 2. Action / Combat | Standard | 16:9 / 21:9 | 5–10s | First+Last Frame |
| 3. Fashion / Runway | Standard | 9:16 / 16:9 | 5–10s | -- |
| 4. Beauty / Skincare | Standard | 9:16 / 1:1 | 5–10s | -- |
| 5. Product / Commercial | Standard | 16:9 / 1:1 | 5–10s | -- |
| 6. Viral / UGC | Fast | 9:16 | 5s | -- |
| 7. Educational / Science | Standard | 16:9 | 10s | -- |
| 8. Anime / Animation | Standard | 16:9 / 9:16 | 5–10s | -- |
| 9. Music Video / Dance | Standard | 16:9 / 9:16 | 10s | @Audio |
| 10. Drama / Dialogue | Standard | 16:9 / 4:3 | 10s | -- |
| 11. VFX / Fantasy / Sci-Fi | Standard | 16:9 / 21:9 | 10s | -- |
| 12. Landscape / Nature | Standard | 16:9 / 21:9 | 10s | -- |
| 13. Food / ASMR | Standard | 9:16 / 1:1 | 5–10s | -- |
| 14. E-commerce / Showcase | Standard / Fast | 1:1 / 16:9 | 5–10s | -- |

---

## Usage Notes

- **Combining templates:** Many real projects blend categories. A fashion e-commerce video might use the Fashion template structure with E-commerce Settings. A sci-fi music video would merge VFX world-building with Music Video beat-sync structure. Start with the primary category template, then layer in elements from secondary categories.
- **Placeholder discipline:** Replace ALL [bracketed] items before submission. Leaving placeholders in the final prompt degrades generation quality — the model interprets brackets as uncertainty.
- **Template length:** These templates are intentionally detailed. For 5-second generations, you can trim to the first two timeline blocks. For 10-second generations, use the full template. Never submit a prompt longer than the generation can meaningfully visualize.
- **Style anchor consistency:** If generating multiple clips for the same project, copy the style anchor line verbatim across all prompts to maintain visual consistency.
