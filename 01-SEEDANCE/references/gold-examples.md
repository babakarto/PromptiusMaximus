# Gold Standard Examples — Seedance 2.0 Reference

> These 30 prompts are the best from 300+ tested. Copy-paste ready.
> Organized by category with settings for each.
> Sources: Atlas Cloud, Imagine.art, TechHalla, CyberJungle, AI Search, Curious Refuge, SeaArt, Reddit, Vmake, ChatCut, GLBgpt.

---

## Cinematic (5 prompts)

### 1. Epic Drone Valley Reveal
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None (text-to-video) or upload a valley/mountain landscape as @Image1 for environment lock.
```
Sweeping drone shot ascending from a misty valley floor, slowly revealing a vast mountain range at sunrise, golden light breaking through clouds and casting long shadows across pine forests, orchestral grandeur, National Geographic documentary quality, ultra-smooth camera movement. 4K, stable, cinematic texture.
```
**Why it works:** Single continuous camera move (drone ascend) combined with one strong style anchor (National Geographic) and precise lighting (golden hour) gives the model a clear, unambiguous instruction set. The reveal structure builds tension naturally.

---

### 2. Netflix Cold Opener — Detective Ritual Forest
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 15s
**References needed:** Upload 1 character reference image as @Image1 (detective face/outfit).
```
Scene 1 Action: Detective @Image1 ducks under yellow police tape in a misty, overcast forest to enter a ritual crime scene. Camera: Low-angle tracking shot follows him from behind as he crouches under the fluttering tape. Lighting: Flat, desaturated natural light from a heavy gray sky with soft, diffused shadows. Sound: Sharp rustle of plastic tape in the wind and the crunch of damp forest floor underfoot.

Scene 2 Action: He stands still, looking down at a circle of charred remains and strange symbols carved into tree bark. Camera: Wide establishing shot from a high angle to reveal the ritualistic layout of the forest floor. Lighting: Cold, moody forest tones with natural light filtered through thick, stagnant morning fog. Sound: Low-frequency wind whistling through pine needles and the distant, rhythmic caw of a crow.

Scene 3 Action: He kneels to inspect a blood-stained artifact placed at the center of the ritualistic stone circle. Camera: Close-up of his intense eyes, followed by a macro insert shot of his gloved hand reaching for the object. Lighting: Low-contrast daylight with a subtle Tyndall effect through the rising mist and cigarette smoke. Sound: Soft, wet squelch of mud and the heavy, controlled breathing of the detective. Dialogue: 'This is new.'

Scene 4 Action: He stands up slowly, looking at a carved symbol on a nearby tree while sirens echo through the woods. Camera: Handheld wide shot to capture the scale of the forest, followed by a quick pan to the carving. Lighting: Low-contrast daylight with a subtle Tyndall effect through the rising morning fog. Sound: Distant, muffled police sirens approaching from a winding forest road and a deep, heavy sigh.
```
**Why it works:** Each scene specifies Action + Camera + Lighting + Sound independently, giving the model four complete shot descriptions. The escalating tension (tape > remains > artifact > symbol) and varied shot sizes (tracking > wide > close-up > handheld wide) prevent visual monotony. The dialogue cue "This is new" triggers natural lip movement.

---

### 3. Hollywood Racing Movie — Multi-Shot Night Rain
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 15s
**References needed:** Upload driver face/helmet as @Image1. Optionally upload a motion reference as @Video1.
```
Style: Hollywood Professional Racing Movie (Le Mans style), cinematic night, heavy rain, high-stakes sport.
@Image1 (75% weight) for veteran driver face/helmet/clothing lock. @Video1 (25% weight) for camera pacing only.

[00-05s] Shot 1: Close-up inside veteran driver's helmet. Rain lashes windshield. Calm focused expression. Dashboard lights reflect on visor. Subtle nod.
[05-10s] Shot 2: Cut to rival car interior. Younger driver grips wheel tightly, breathing heavily. Eyes wide with adrenaline.
[10-15s] Shot 3: Green light. Both cars accelerate in perfect sync on wet asphalt. Water sprays violently into camera lens. Motion blur stretches stadium lights.

Ultra-smooth 60fps motion, realistic water splash physics, natural fabric movement, consistent lighting, 2K resolution, cinematic color grading. No jitter, no deformation.
```
**Why it works:** Combines three advanced techniques — timestamped timeline, reference weighting, and physics constraints — in a single prompt. Each shot has a distinct emotional beat (calm > tense > explosive), and the water physics keywords force realistic rain interaction.

---

### 4. Post-Apocalyptic Survivor Reveal
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 10s
**References needed:** Upload character reference as @Image1 (rugged survivor look).
```
@Image1 (80% weight) exact survivor character reference. Sweeping drone shot ascending from sand-swept ruins of a collapsed city at golden hour. 30-year-old rugged survivor in tattered leather jacket stands on cliff edge, wind whipping sand around boots. Slow push-in as eyes scan horizon. Volumetric god rays through dust.

Camera: extreme long shot to medium tracking shot, 35mm anamorphic lens, subtle handheld shake.
Lighting: dramatic golden hour side lighting with long shadows.
Style: cinematic dystopian trailer, Blade Runner 2049 color grading. Realistic fabric physics, sand particle dynamics, high fidelity 2K.
```
**Why it works:** The 80% weight character lock plus specific lens (35mm anamorphic) and physics keywords (sand particle dynamics, fabric physics) produce a cinematic trailer look with zero drift. The Blade Runner 2049 anchor gives the model a precise color grade target.

---

### 5. Pizza Shop Single Take
**Settings:** Mode: Text-to-Video or Image-to-Video | AR: 16:9 | Duration: 15s
**References needed:** None for text-to-video. Optionally upload a pizza shop interior as @Image1.
```
Single continuous cinematic shot, no music. From outside the glass window, the dim camera slowly pushes inward into a pizza shop. A bearded white male employee is baking pizza. He removes the pizza from the oven with a metal tray, places it into a red takeaway box, closes the lid, and then hands it to a customer with a warm smile. Final shot: over-the-shoulder perspective.
```
**Why it works:** "Single continuous shot" forces no cuts, which Seedance handles well for narrative coherence. The sequence of physical actions (remove > place > close > hand) gives the model clear motion beats. The camera instruction (push inward from outside glass) is specific and achievable.

---

## Action (3 prompts)

### 6. Cyberpunk Assassin Rooftop Fight
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 15s
**References needed:** Upload character image as @Image1. Optionally upload dynamic camera reference as @Video1.
```
@Image1 (75% weight) female cybernetic assassin short neon-blue hair black tactical suit. @Video1 (25% weight) dynamic camera reference.

[00-04s] Low-angle tracking shot as she sprints across rain-soaked rooftop, neon reflections in puddles.
[04-09s] She leaps, performs spinning kick on enemy drone - slow-motion impact with sparks and realistic fabric flow.
[09-15s] Extreme close-up on glowing cybernetic eye as she lands, rain dripping down face, subtle smirk.

Blade Runner 2049 cinematic style, dramatic cyan/magenta neon lighting, realistic gravity and water physics, handheld camera shake, ultra-smooth motion.
```
**Why it works:** Timeline format with escalating intensity (run > fight > land). Micro-expression at the end ("subtle smirk") adds character depth. Physics keywords (gravity, water, fabric flow) prevent the floaty look common in action scenes.

---

### 7. Ronin vs Creature Thunderstorm
**Settings:** Mode: Text-to-Video or Image-to-Video | AR: 16:9 | Duration: 10s
**References needed:** Optionally upload ronin character as @Image1 (70% weight).
```
An intense fight scene between a masked ronin with a huge sword and a massive creature during a violent thunderstorm. The ronin causes the earth below his feet to start shattering and then he charges towards the colossal monster as black smoke and electricity surges through his sword. Handheld motion and camera shake. Cinematic wuxia style, low-angle tracking, realistic physics and fabric flow.
```
**Why it works:** Cinematic framing ("wuxia style") wraps the intense action in a film genre the model recognizes. The specific physics (earth shattering, smoke surging, electricity) give the model concrete VFX targets instead of vague "epic" descriptions.

---

### 8. Close-Quarters Combat — Snow Base
**Settings:** Mode: Text-to-Video or Image-to-Video | AR: 16:9 | Duration: 10s
**References needed:** Optionally upload agent character as @Image1.
```
A short-haired female agent in tactical winter gear engages in close-quarters combat with a mercenary at a snowy military base. The mercenary throws a punch; she dodges swiftly and counters with a powerful elbow strike to his face mask, followed by a heavy knee to the stomach. Dynamic low-angle tracking shot, realistic gravity and fabric response, cinematic action movie style, 2K resolution.
```
**Why it works:** Choreography is described beat-by-beat (punch > dodge > elbow > knee) which gives the model a clear motion sequence instead of generic "fighting." The specific physical moves prevent the AI from defaulting to static poses.

---

## Fashion (3 prompts)

### 9. Classic Runway — Black Silk Dress
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 12s
**References needed:** Upload dress/outfit reference as @Image1 (80% weight).
```
@Image1 (80% weight) long black silk dress reference.
A model wearing a long black silk dress based on @Image1 on a high-end runway stage.
0-4s: Side-angle tracking shot following her steps; the dress moves naturally with her body's center of gravity.
4-8s: The camera gradually orbits the model, showcasing the fabric's sheen under the lights as it flows smoothly.
8-12s: The model holds a confident gaze and steady stride; when she turns, the skirt forms an elegant curve.
Realistic fabric simulation, dramatic runway lighting, high-fashion editorial style, ultra-smooth motion.
```
**Why it works:** High weight (80%) on garment reference locks the outfit. Fabric physics keywords ("center of gravity," "sheen," "elegant curve") force realistic silk behavior. The orbit camera on shot 2 shows the dress from multiple angles.

---

### 10. Zara Editorial — White Cyclorama
**Settings:** Mode: Omni Reference or Text-to-Video | AR: 9:16 | Duration: 10s
**References needed:** Optionally upload outfit reference as @Image1.
```
Model walking on an infinite white cyclorama, wearing an oversized camel wool coat, fabric flowing with each step, camera tracking alongside at hip height, wind machine creating gentle fabric movement, clean editorial fashion photography style, soft diffused studio lighting, Zara campaign aesthetic.
```
**Why it works:** "Infinite white cyclorama" + "hip height tracking" is the exact e-commerce fashion formula. The wind machine keyword adds subtle fabric motion without chaos. "Zara campaign aesthetic" is a strong, specific style anchor the model understands.

---

### 11. Rainy Street Fashion — Night Shoot
**Settings:** Mode: Omni Reference or Text-to-Video | AR: 9:16 | Duration: 10s
**References needed:** Optionally upload model/outfit as @Image1.
```
Model in red windbreaker sprints through rainy street at night, neon reflections on wet fabric, water droplets sliding off coat, dynamic handheld tracking shot, motion blur on background, high-fashion campaign style.
```
**Why it works:** Combines action (sprint) with fashion (outfit detail) in a way that showcases the garment dynamically. Water interaction keywords ("droplets sliding off coat") test and demonstrate fabric physics, which is exactly what fashion video needs.

---

## Beauty (3 prompts)

### 12. ASMR Skincare Gel Macro
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 12s
**References needed:** Upload product bottle + hand close-up as @Image1 (80% weight).
```
@Image1 (80% weight) light blue skincare gel bottle and hand reference.
Vertical ASMR video with no music, extreme macro details. A light blue skincare gel bottle sits on glass surface. Hand presses onto the gel, spreading it in slow circular motions causing tiny bubbles to swirl and thinning it into a semi-transparent oily film. Dramatic cool lighting from behind makes the gel glow like a gemstone. Realistic liquid viscosity and skin absorption glow, 85mm macro lens, shallow depth of field.
```
**Why it works:** "No music" + ASMR framing triggers clean ambient audio. Macro lens + shallow DOF focuses entirely on the product. The specific gel behavior ("tiny bubbles," "semi-transparent oily film") gives the model concrete visual targets for liquid physics.

---

### 13. Luxury Serum Drop on Skin
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 10s
**References needed:** Upload serum bottle as @Image1 (75% weight).
```
@Image1 (75% weight) premium serum bottle reference. Extreme close-up of golden serum droplet falling slowly onto flawless dewy skin, absorbing with visible glow and subtle subsurface scattering. Soft ring light creates beautiful reflections. Slow-motion 120fps, luxury skincare commercial aesthetic, realistic viscosity and skin physics.
```
**Why it works:** "Subsurface scattering" is a rendering term the model recognizes and executes beautifully on skin. The single action (drop falling > absorbing) is simple enough for perfect execution. "120fps slow-motion" stretches the moment for maximum visual impact.

---

### 14. UGC Lipstick Ad
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 10s
**References needed:** Upload lipstick product + model face as @Image1 (80% weight).
```
@Image1 (80% weight) lipstick tube and model lips reference.
UGC-style beauty ad: young woman with flawless skin applies vibrant red lipstick in front of mirror. Natural hand movement, precise lip contouring, slight smile at the end. Close-up on lips with glossy finish catching light. Soft natural window lighting, realistic lipstick texture and shine, vertical 9:16.
```
**Why it works:** "UGC-style" tells the model to use natural, relatable framing. The specific action sequence (apply > contour > smile) creates a complete narrative arc. Ending on a glossy close-up is the classic beauty money shot.

---

## Product / Commercial (3 prompts)

### 15. Luxury Watch Floating Macro
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 10s
**References needed:** Upload product photo as @Image1 (70% weight).
```
@Image1 (70% weight) premium wristwatch exact reference. Slow 360 orbital macro shot of the watch floating in mid-air, water droplets suspended around it catching light like diamonds. Pure black background, single dramatic spotlight from above. Extreme macro detail on every texture and reflection.

Camera: smooth orbiting shot, 85mm portrait lens, shallow depth of field.
Style: high-end jewelry commercial aesthetic. Realistic water refraction physics, ultra-smooth rotation, 2K.
```
**Why it works:** The 360 orbital on black background is the gold standard for product video. Suspended water droplets add visual drama while the macro lens captures texture detail. Single spotlight creates professional studio lighting without complexity.

---

### 16. Iced Coffee Pour — Starbucks Style
**Settings:** Mode: Text-to-Video | AR: 9:16 | Duration: 10s
**References needed:** None (text-to-video) or upload coffee glass as @Image1.
```
Tall glass of iced coffee being poured in slow motion, rich dark coffee meeting swirling cream creating mesmerizing patterns, ice cubes clinking, condensation droplets, close-up to medium shot, warm cafe lighting, Starbucks commercial quality.
```
**Why it works:** Liquid-meets-liquid interaction (coffee + cream) is visually mesmerizing and Seedance handles it well. The sensory details (clinking, condensation) trigger audio generation. "Starbucks commercial quality" is an instantly recognizable style anchor.

---

### 17. Holographic App Interface Commercial
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 15s
**References needed:** Upload interface screenshot as @Image1 (visual reference) and logo as @Image2.
```
@image1 as visual reference for the interface style and scene mood
@image2 as logo reference for the final frame

0-5s: Camera glides just above dark water. A holographic colored drop falls in, bursting into soft fluid that turns into floating dark frosted-glass cards. The cards flip to reveal album art in a layered 3D arrangement.
Sound: clear water drop, then soft atmospheric bass fades in.

5-10s: Camera focuses on one card. A fluorescent green progress bar stretches into a ribbon of light, flowing through 3D rocks, then into a floating phone and minimalist laptop. The interface glows gently.
Sound: music grows stronger with smooth technology swooshes.

10-15s: Camera passes through the laptop screen into a bright liquid space. Glowing title text pulses with the beat, then all light converges into the logo from @image2.
Constraint: all English text must be correctly spelled and visually intact.
```
**Why it works:** The water > cards > interface > logo progression creates a complete brand story in 15 seconds. Sound cues at each timestamp synchronize audio to visuals. The text constraint prevents garbled typography which is a common failure mode.

---

## Viral / UGC (3 prompts)

### 18. NBA Highlights — Self-Insert
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 15s
**References needed:** Upload your face/body photo as @Image1.
```
Action: @Image1 wearing a Lakers jersey with number 39 executes a crossover against a Celtics defender, drives into the paint, and aggressively dunks over a towering center.
Camera: Continuous side-court broadcast camera panning smoothly to follow the live action in a single uncut TV shot.
Lighting: Even and bright arena floodlights typical of professional high-definition sports television broadcasts.
Sound: Sneaker squeaks, ball bouncing, the massive metallic crash of the rim, and a deafening continuous crowd roar.
Dialogue: 'He breaks his man and destroys the rim! A monster poster jam!'
```
**Why it works:** "Broadcast camera" + "single uncut TV shot" replicates authentic sports coverage. Specific audio cues (sneaker squeaks, rim crash) create immersive sound design. The commentary dialogue adds viral shareability. Perfect for self-insert content.

---

### 19. Zombie Scene with Dialogue
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 15s
**References needed:** Upload 2 character face references as @Image1 (guy) and @Image2 (girl).
```
The guy is @image1. The girl is @image2.
Dimly lit room, boarded up windows, moans and scratching outside from zombies.
Close-up of the couple huddled in a corner. The girl whispers, voice trembling: "They're right outside."
The guy grips her hand, subtle fear in eyes: "We just have to stay quiet. Don't move."
Zombie breaks through a weak board. They scream.
The guy yells, grabbing a chair to push it away: "Get back. Get the hell back."
The girl screams too, panic overtaking her, hitting a zombie with a lamp.
Wide shot of the room in chaos. Shadows of zombies press against walls. The couple barricading with whatever they can find, breathing hard.
Girl sobbing: "We're not going to make it."
Guy, fierce and protective: "Yes, we will. Just hold on together."
```
**Why it works:** Dialogue-driven prompts with emotional direction ("voice trembling," "fierce and protective") trigger natural lip-sync and acting. The escalation from whisper to scream gives dramatic range. Multiple character references maintain identity throughout.

---

### 20. Mobile Phone POV — Highway Chaos
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 15s
**References needed:** Upload 1 character face reference as @Image1.
```
Action: (CONTINUOUS MOBILE PHONE POV) In a shaky, erratic handheld shot from a car window, an elderly woman is tracked riding a mini-bike on the highway with an orange cat perched on the gas tank. A few men are visible in the car, watching her. The camera fumbles slightly, attempting to stay focused. The driver speaks quietly, and the passenger filming leans out, shouting.

Camera: Continuous handheld shot, highly erratic and unstable, with constant micro-shakes and jerky panning. Rapid digital zoom-ins and zoom-outs executed fumbling and unsteadily, often losing focus.
Lighting: Overexposed, harsh midday sun with high-contrast shadows and bright reflections from passing cars and the highway asphalt.
Sound: Low-fidelity, muffled wind buffeting against the phone microphone, a loud thrum of the car interior, and high-pitched engine whine piercing through the wind noise.
```
**Why it works:** "CONTINUOUS MOBILE PHONE POV" with deliberately imperfect camera instructions (shaky, erratic, losing focus) produces authentic UGC-style footage that looks real. The absurd scenario (grandma + cat + highway) creates viral potential. Low-fi audio sells the realism.

---

## Anime / Animation (2 prompts)

### 21. Anime Girl Healing Entrance
**Settings:** Mode: Text-to-Video or Image-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None for text-to-video. Optionally upload anime character as @Image1.
```
An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat, standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the camera and smiles gently. A light breeze moves her hair and dress. The camera slowly pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion, high detail.
```
**Why it works:** The "healing" aesthetic is a recognized anime genre that Seedance renders beautifully. Single gentle action (turn + smile) avoids motion artifacts. The breeze adds subtle movement to hair and dress without chaos. Film grain anchors the style.

---

### 22. Pixar Princess Dragon Chase
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None (text-to-video).
```
3D Pixar animation. A princess wearing a glittery white dress running away from a massive dragon with glowing red eyes. The dragon breathes fire, which ignites the ground and foliage behind her. Then, she reaches a river and quickly jumps onto drifting debris to cross. The princess then looks back to see the dragon roaring in frustration as it can't cross the river.
```
**Why it works:** "3D Pixar animation" is one of the strongest style anchors — the model knows exactly what this looks like. The three-beat story (chase > river crossing > safe) creates a complete narrative arc. Fire and water VFX showcase the model's physics engine.

---

## Drama / Dialogue (2 prompts)

### 23. Hospital Bedside — Emotional Scene
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 12s
**References needed:** None for text-to-video. Optionally upload 2 character references as @Image1 and @Image2.
```
Two people sit beside a hospital bed, sunlight filtering through blinds. Person A holds person B's hand, voice barely a whisper: "I don't know what I'll do without you."
B smiles faintly, trying to hide pain: "You'll be fine. Just promise me something."
A suddenly breaks down, leaning over the bed, sobs uncontrolled: "I can't... I can't lose you."
B squeezes their hand with a soft, reassuring smile: "You'll never lose me. I'm still here."
```
**Why it works:** Emotional direction embedded in dialogue cues ("voice barely a whisper," "sobs uncontrolled") triggers micro-expressions and natural acting. The escalating emotion (whisper > faint smile > breakdown > reassurance) gives the model clear performance beats. Seedance's lip-sync handles multi-character dialogue well.

---

### 24. Mockumentary Interview — True Crime Style
**Settings:** Mode: Omni Reference | AR: 16:9 | Duration: 15s
**References needed:** Upload interviewee face reference as @Image1.
```
Scene 1 Action: The elderly woman in @Image1 sits in a dimly lit interrogation room, looking off-camera with a nostalgic smirk. Camera: Medium close-up, static shot, shallow depth of field with a dark, blurred background for a true crime aesthetic. Lighting: Low-key cinematic lighting, soft key light on her face, heavy atmospheric shadows surrounding her. Sound: Low-frequency room tone, the faint hum of a ventilation system, and the crisp clarity of her voice. Dialogue: 'Truth is, I had a hell of a time. There was chemistry right from the start.'

Scene 2 Action: She leans in slightly, her expression turning more intense as she recalls the climax of the story. Camera: Sharp cut to a tight close-up, focusing on the micro-expressions around her eyes and mouth. Lighting: High-contrast side lighting, emphasizing the textures of her skin and the gravity of her words. Sound: The subtle rustle of her sweater against the chair and a sharp intake of breath. Dialogue: 'But the final scene... damn! It was so intense.'
```
**Why it works:** The static camera + shallow DOF is the documentary interview formula that Seedance executes perfectly. Micro-expression focus ("nostalgic smirk," "expression turning more intense") produces subtle, realistic acting. The true crime aesthetic is a highly recognizable style anchor.

---

## Music Video (2 prompts)

### 25. Cyberpunk Beat-Sync Dance
**Settings:** Mode: Omni Reference | AR: 9:16 | Duration: 10s
**References needed:** Upload dancer/character as @Image1. Upload music track as @Audio1.
```
A trendy cyberpunk girl dancing in a neon city street at night. Every strong beat triggers a cut or speed-ramped camera move. Neon signs reflecting on wet ground. Cyberpunk style, fast-paced editing, multi-shot continuity. Dance movements and character appearance remain consistent.
```
**Why it works:** "Every strong beat triggers a cut" explicitly tells the model to sync edits to music. Neon + wet ground creates reflective surfaces that amplify visual energy. The consistency constraint prevents the character from morphing between cuts.

---

### 26. 1920s Jazz Club Charleston
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None for text-to-video. Optionally upload @Audio1 for jazz music sync.
```
Create a Charleston dance sequence in a 1920s jazz club style. A female dancer in a gold-fringed dress and a male dancer in a striped suit perform rapid, syncopated steps, aerial tosses, and large arm swings. Warm golden spotlight, film grain, vintage sepia tone, cinematic quality.
```
**Why it works:** The 1920s jazz club is a visually distinctive era the model renders with strong authenticity. Specific dance moves (syncopated steps, aerial tosses, arm swings) prevent generic swaying. Gold-fringed dress creates dynamic fabric movement that showcases physics.

---

## Landscape / Nature (2 prompts)

### 27. Deep Sea Bioluminescence Dive
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None (text-to-video).
```
First-person POV dive footage. A scuba diver descends into a pitch-black ocean. The only light is the diver's torch cutting a narrow beam into the dark. At depth, the torch clicks off. Total darkness for two seconds. Then - faint blue pulses. Bioluminescent creatures slowly emerge from every direction, turning the water into a living light show. Camera: continuous descent, no cuts. Cinematic underwater documentary style.
```
**Why it works:** The darkness-to-light reveal is one of the most powerful visual structures. Two seconds of total black builds anticipation. Bioluminescence gives the model a clear VFX target (glowing particles in dark water). First-person POV with "no cuts" keeps the shot coherent.

---

### 28. Northern Lights Time-Lapse
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None (text-to-video). Optionally upload a cabin/landscape photo as @Image1.
```
Locked-off wide shot, Iceland or Norway, winter. Foreground: a lone cabin with a single amber window glowing. Background: dark sky over a snow-covered plain. Time-lapse begins. The aurora emerges - first a pale green ribbon, then expanding into waves of green, purple, and cyan dancing across the entire sky. Stars wheel slowly behind. National Geographic documentary quality, 2K resolution.
```
**Why it works:** "Locked-off wide shot" removes camera movement complexity so the model focuses entirely on the aurora animation. The static cabin provides a grounding reference point against the moving sky. Time-lapse is a format Seedance understands and executes well.

---

## VFX / Fantasy (2 prompts)

### 29. Magical Library Discovery
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None (text-to-video). Optionally upload character or library concept art as @Image1.
```
A young mage enters a colossal, enchanted library. Endless shelves stretch into the misty heights. Floating candles and glowing books illuminate the space. The camera sweeps upward, revealing a spiraling staircase and floating staircases. Volumetric light shafts through high windows, dust particles drifting in beams. Unreal Engine 5 cinematic render style, 2K resolution.
```
**Why it works:** "Unreal Engine 5 cinematic render" is one of the strongest VFX style anchors. The upward camera sweep naturally reveals scale. Multiple light sources (candles, glowing books, window shafts) create layered visual depth. Floating objects give the model clear physics targets.

---

### 30. Steampunk Airship Battle
**Settings:** Mode: Text-to-Video | AR: 16:9 | Duration: 10s
**References needed:** None (text-to-video). Optionally upload concept art as @Image1.
```
A massive steampunk airship engages in battle above a city. Smoke and steam fill the sky, with smaller airships darting around. Explosions throw sparks into the air. Crew members operate mechanical weaponry, levers, and pulleys with precision. Dynamic tracking shot following the main airship, cinematic color grading with warm amber and cool steel blue, Unreal Engine 5 style, 2K resolution.
```
**Why it works:** Steampunk is a visually rich genre with clear mechanical elements (gears, steam, brass) that the model renders with high detail. Multiple layers of action (main ship, smaller ships, crew, explosions) create depth. The warm/cool color contrast gives cinematic polish.

---

## Quick Reference: Settings Cheat Sheet

| Category | Best Mode | Best AR | Best Duration |
|----------|-----------|---------|---------------|
| Cinematic | Omni Reference | 16:9 | 10-15s |
| Action | Omni Reference | 16:9 | 10-15s |
| Fashion | Omni Reference | 9:16 | 10-12s |
| Beauty | Omni Reference | 9:16 | 10-12s |
| Product | Omni Reference | 16:9 or 1:1 | 8-10s |
| Viral / UGC | Omni Reference | 9:16 | 10-15s |
| Anime | Text-to-Video | 16:9 | 8-10s |
| Drama | Omni Reference | 16:9 | 12-15s |
| Music Video | Omni Reference + Audio | 9:16 | 10-15s |
| Landscape | Text-to-Video | 16:9 | 8-10s |
| VFX / Fantasy | Text-to-Video | 16:9 | 8-10s |

## Key Patterns Across All 30 Prompts

1. **One camera move per shot.** Never stack multiple movements.
2. **Physics keywords** (gravity, fabric flow, water refraction, subsurface scattering) elevate realism.
3. **One style anchor** (Blade Runner 2049, National Geographic, Pixar, UE5) beats listing five styles.
4. **Dialogue with emotional direction** triggers natural lip-sync and micro-expressions.
5. **Timestamped timelines** [00-05s] force clean multi-shot structure.
6. **Reference weighting** (@Image1 70-85% for character, @Video1 25-30% for motion) locks consistency.
7. **Quality suffix** (2K, ultra-smooth, no jitter, no deformation) belongs at the end, always.
