# Seedance 2.0 - Guide Web Complete (GLBgpt + ChatCut + Imagine.art)

Estratto da 3 guide web verificate (Marzo 2026). Freepik ha bloccato l'accesso (403).

---

# FONTE 1: GLBgpt.com - Seedance 2.0 Prompt Guide

## Formula Core

```
Subject + Action + Camera + Scene + Style + Constraints
```

## 5 Prompt Esatti

### 1. Anime Girl Healing Entrance

```
An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat, standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the camera and smiles gently. A light breeze moves her hair and dress. The camera slowly pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion, high detail.
```

### 2. Product 360 Rotation (Ecommerce)

```
A minimalist black matte mechanical keyboard on a pure white infinite studio background, rotating smoothly 360 degrees clockwise. RGB lighting gently breathing. Keycap text sharp and readable. Fixed macro camera, smooth turntable motion, commercial product photography style, soft high-key lighting, no noise. Logo and text remain perfectly consistent.
```

### 3. Action Fight Scene (Video Reference)

```
A wuxia-style male hero (based on reference video character), wearing black martial outfit, fighting enemies in a rainy bamboo forest at night. Fast sword combos with visible sword light trails and splashing water. Fast follow camera, crane shots, and quick close-ups. Cinematic camera language. Maintain character appearance and clothing consistency. Realistic physics, wet fabric, rain interaction.
```

### 4. Music Video Beat Sync (Audio Driven)

```
A trendy cyberpunk girl dancing in a neon city street at night. Every strong beat triggers a cut or speed-ramped camera move. Neon signs reflecting on wet ground. Cyberpunk style, fast-paced editing, multi-shot continuity. Dance movements and character appearance remain consistent.
```

### 5. Multi-Shot Storytelling (Robot)

```
A lonely robot wakes up in an abandoned factory (Scene 1). It walks outside and sees a sunset wasteland (Scene 2). It discovers a small flower and gently touches it (Scene 3). Finally, it looks up and smiles at the sky (Scene 4). Keep robot appearance consistent. Emotional transition from confusion to warmth. Cinematic camera, warm tones, epic mood, no flicker.
```

## Template Structures

### Basic Generation
```
@image1 as the first frame, [describe subject, action, camera, and scene]
```

### Reference Video Lock
```
Reference @video1 for camera movement and shot language, [describe new content]
```

### Multi-Modal Combination
```
@image1 as the first frame, reference @video1 for motion, @audio1 for rhythm and mood, [describe full scene]
```

### Video Editing
```
Replace [element A] in @video1 with [element B], [additional constraints]
```

### Video Extension
```
Extend @video1 by [X] seconds, [describe new content]
```

## Settings Consigliati

| Parametro | Valore |
|-----------|--------|
| Duration (test) | 5s |
| Duration (produzione) | 10-30s |
| AR short-form | 9:16 |
| AR horizontal | 16:9 |
| Resolution (speed) | 720p |
| Resolution (quality) | 1080p / 2K |
| Generate Audio | ON (consigliato) |
| Seed | -1 (random) o fisso (riproducibilita) |
| Creativity | Basso = piu vicino al reference |

## Frasi Consistency

```
Keep the same character, same clothing, same hairstyle, no face changes, no flicker, high consistency.
```

```
hands with perfect anatomy, text clear and readable
```

## Fix Comuni

- Evita close-up veloci delle mani
- Usa testo grande e centrato
- Cambia "fast" in "medium speed" per artefatti motion
- Aggiungi video reference per bloccare il movimento
- Genera clip perfette da 5-10s, poi usa video extension

---

---

# FONTE 2: ChatCut.io - Seedance 2 Prompt Guide

## Formula Principale

```
[asset] + [job of asset] + [what happens] + [when it happens] + [camera behavior] + [sound behavior] + [constraints]
```

## Checklist 10 Punti (Fondamentale)

1. **Dai un lavoro a ogni @asset** ("as first-frame reference", "as camera movement reference")
2. **Scrivi su timeline** (0-3s, 3-6s) NON paragrafi narrativi
3. **Distingui "Use As" vs "Reference"** (Use As = fissa il frame, Reference = prende ispirazione)
4. **Specifica se serve un take continuo** ("one continuous take", "no cuts")
5. **Priorita upload:** motion first, subject consistency second, mood third
6. **Verbi fisici** > parole soft ("melt" non "becomes")
7. **Tratta i suoni come cue di movimento**
8. **Definisci composizione PRIMA dell'azione**
9. **Scrivi le transizioni come azioni**, non come tagli
10. **Abbina input mode al bisogno** (semplice: image+text; complesso: multimodal)

## Asset Job Keywords (Copia-Incolla)

```
"as first-frame reference"      = fissa lo shot
"as outfit reference"            = blocca vestiti
"as material reference"          = blocca texture
"as camera movement reference"   = copia camera
"as pacing reference"            = copia ritmo
"as character reference"         = blocca personaggio
"as environment reference"       = blocca ambiente
"as voiceover tone reference"    = tono voce
"as background music reference"  = mood musica
"as beat reference"              = sincro battiti
"as visual content"              = contenuto visivo
```

## Specifiche Tecniche

| Tipo | Limite | Max Size |
|------|--------|----------|
| Immagini | fino a 9 file | < 30MB |
| Video | fino a 3 file | < 50MB (2-15s) |
| Audio | fino a 3 file | < 15MB (fino a 15s) |
| Output | 4-15 secondi | - |
| Upload totali | 12 file | - |
| Formati immagine | jpeg, png, webp, bmp, tiff, gif | - |
| Formati video | mp4, mov | - |
| Formati audio | mp3, wav | - |

## Prompt Esatti (Tutti)

### Multimodal Full - App/Interface Commercial

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

### Product Commercial Template

```
@image1 as product design reference
@video1 as camera movement reference
@audio1 as music mood reference

0-4s: Slow push-in on the product sitting on a reflective black surface. Soft rim light. Premium commercial look.
4-8s: Camera orbits slightly while fine particles drift around the object, synchronized to the beat.
8-12s: Bold centered text appears. Keep the typography crisp, correctly spelled, and free of visual distortion.
```

### Character Consistency (Multi-Angle)

```
@image1 as front-face reference
@image2 as side-profile reference
@image3 as outfit reference

Keep the same facial structure, hairstyle, and clothing details across all shots.
```

### Product Consistency (Multi-Detail)

```
@image1 as overall silhouette reference
@image2 as side profile reference
@image3 as material texture reference
@image4 as zipper and hardware detail reference
```

### Scene Mood Locking

```
@image1 as warm cafe lighting reference
@image2 as wood texture and tabletop reference

Maintain the same amber color temperature throughout the sequence.
```

### Camera Replication con Nuovo Soggetto

```
Reference @video1 for all camera movement.

Generate a tense hallway scene with one character.
At the moment of panic, use a Hitchcock-style zoom effect, then move into a slow orbit shot.
```

### Motion + Scene Swap

```
@image1 as character reference
@image2 as environment reference

Reference @video1 for camera movement and facial performance rhythm.
Generate a dramatic elevator scene with rising tension.
```

### Multiple Video References

```
Reference @video1 for body action.
Reference @video2 for orbiting camera language.

Generate a two-character fight sequence in a warehouse.
```

### Puzzle-Shatter Transition

```
Reference @video1 for the puzzle-shatter transition effect.
Use @image1 as the subject and reveal the product logo after the transition.
```

### Particle Sweep Reveal

```
Reference @video1 for particle texture and movement style.
Golden particles sweep from left to right and reveal the title from @image1 in the center.
```

### Ad Structure Replication

```
Reference @video1 for ad structure and shot rhythm.
Use @image1 and @image2 as product references.
Generate a premium product film with a clean hero shot, fast detail inserts, and a simple logo ending.
```

### Video Extension

```
Extend @video1 by 6 seconds.

0-2s: Camera tilts upward as the neon sign flickers on.
2-4s: Steam rises from the coffee cup. The door opens. Warm street light spills into the room.
4-6s: Title text fades in: Breakfast Served / 7:00-10:00
```

### Voice Tone Reference

```
@audio1 as voiceover tone reference

Narration should sound calm, confident, and premium.
```

### Ambient Sound From Video

```
Reference the ambient sound in @video1.
Use the same rainy city atmosphere with distant traffic and soft footsteps.
```

### BGM Mood

```
@audio1 as background music reference

Use restrained bass, airy synth textures, and a sleek technology-commercial feel.
```

### Dialogue con Direzione Emotiva

```
Dialogue: "I knew you would come back."
Delivery: quiet, intimate, slightly breathless, close-mic tone.
```

### Character Swap Edit

```
Keep the original motion and camera work from @video1.
Change the character's hair to long red hair.
Add the shark from @image1 slowly rising in the background.
```

### Story Rewrite Edit

```
Use @video1 as the scene base.
Keep the original environment and camera rhythm, but completely change the story.
Frame by frame, replace the original suspense with a surreal comedy beat.
```

### Local Motion Edit

```
Keep the restaurant environment and original camera path from @video1.
Add a close-up of the owner handing over a paper bag with the logo from @image1.
```

### Beat-Synced Multi-Image

```
@audio1 as beat reference
@image1, @image2, @image3, and @image4 as visual content

Cut only on strong beats.
Use high-energy transitions.
Every major beat should trigger a scene change, text reveal, or scale shift.
```

## Verbi di Movimento (Usali al Posto di Parole Vaghe)

```
melt, fracture, stretch, implode, snap open, burst, float, flip, sweep, rise, drift, pulse, converge, streak, dissolve
```

## Linguaggio Constraint per Editing

```
"Keep the same [element] across all shots"
"Maintain the same [quality] throughout the sequence"
"All English text must be correctly spelled and visually intact"
"Uninterrupted camera movement"
"One continuous take"
"No cuts"
"Keep the original [element]"
"Change only the [specific element]"
```

## Beat Sync Instructions

```
"Cut only on strong beats"
"Use high-energy transitions"
"Every major beat should trigger a scene change, text reveal, or scale shift"
"synchronized to the beat"
"Glowing title text pulses with the beat"
```

---

---

# FONTE 3: Imagine.art - Seedance 2.0 Prompt Guide (69 Prompt!)

## Formula

```
Subject: [who/what, include age, material, type]
+ Action: [single clear verb, present tense]
+ Camera: [shot size] + [movement] + [angle] + [lens]
+ Style: [one visual anchor] + [lighting] + [color treatment]
```

## Shot Vocabulary

| Shot | Uso |
|------|-----|
| Wide | Stabilisce spazio e contesto. Abbina con slow dolly o locked-off |
| Medium | Include soggetto + contesto |
| Close | Focus su dettaglio ed emozione |
| Pan | Rotazione laterale per rivelare |
| Dolly/Track | Movimento fisico verso/da/lungo il soggetto |
| Handheld | Aggiunge sway e micro-shake |

## CATEGORIA 1: Cinematic Narrative & Drama

### 1. Pizza Shop

```
Single continuous cinematic shot, no music. From outside the glass window, the dim camera slowly pushes inward into a pizza shop. A bearded white male employee is baking pizza. He removes the pizza from the oven with a metal tray, places it into a red takeaway box, closes the lid, and then hands it to a customer with a warm smile. Final shot: over-the-shoulder perspective.
```

### 2. Volleyball Match

```
A women's volleyball match in a spacious indoor gym with an arched wooden ceiling and large windows. The stands are full of cheering spectators, and colorful banners hang on the back wall. The blue and green teams exchange intense rallies while players shout to communicate. The green team fails to save the ball, and an off-screen whistle blows.
```

### 3. Street Dance Battle

```
Generate a 15-second photorealistic street dance battle at night. The urban street has reflective wet pavement, neon lights, and a thin mist. A group of young dancers forms a semicircle. The first 5 seconds focus on one dancer performing challenging solo floor moves.
```

### 4. Cave Exploration POV

```
First-person POV handheld footage with slight natural shake. The only light comes from a headlamp, illuminating damp mossy walls. The camera moves through a narrow tunnel; the hand occasionally enters the frame.
```

### 5. Knight in the Cave

```
A multi-shot sequence of a knight in silver armor. Shot 1: Wide shot as he enters a dark cave with a torch. Shot 2: Close-up of his nervous eyes. Shot 3: He draws his sword, which glows blue. Low-angle tracking shot, 2K resolution.
```

### 6. Steadicam Cafe to Subway

```
Steadicam long take following a man from a warm, yellow-lit cafe into a cool-toned, busy street. He pushes the door open, walks through traffic with cars creating light trails, and finally descends a dim subway staircase.
```

### 7. Hong Kong Retro Film

```
90s Hong Kong art cinema style with retro grain, yellow-green tint, and step-printing effect. A man or woman in a khaki trench coat listens silently at a rain-soaked red phone booth.
```

## CATEGORIA 2: Action, Combat & Chase

### 8. Green-Screen Fight

```
Make the characters from Image 1 and Image 2 fight using the movements from the green-screen reference video. Setting: abandoned parking lot. Add visual effects during combat.
```

### 9. Close-Quarters Combat

```
A short-haired female agent in tactical winter gear engages in close-quarters combat with a mercenary at a snowy military base. The mercenary throws a punch; she dodges swiftly and counters with a powerful elbow strike to his face mask, followed by a heavy knee to the stomach.
```

### 10. Nordic Snow Chase

```
Realistic Nordic snowy night. A man runs fast through deep snow, tracked closely from behind at foot level. A wolf chases him, maintaining a strong sense of speed. The man trips and rolls; the wolf lunges at him.
```

### 11. Cyberpunk Assassin Fight

```
Cyberpunk style, game CGI, dark city corner. A young assassin fights multiple enemies with a lightsaber. The camera rapidly pulls back to show the surrounding foes.
```

### 12. Shibuya Parkour Sprint

```
Single continuous cinematic shot in Shibuya. A schoolgirl sprints at extreme speed, weaving along crosswalks and walls. The camera moves low and close to the ground, following her every leap, roll, and jump.
```

### 13. Neon City Action Chase

```
High-energy cinematic chase at night in a neon-lit city. A lone character sprints through rain-soaked streets while police drones and headlights blur past. Quick cuts show close-ups of eyes, boots splashing puddles, and wide traffic shots.
```

### 14. AAA Game-Style Fight

```
They meet in the dead of night and engage in a fight. The fighting style is incredibly flashy, the atmosphere is tense, and the camera work is cinematic. It's like a promotional trailer for a AAA game, featuring CG and Unreal Engine 5.
```

### 15. Mirror Breakdown Scene

```
The woman in @Image1 walks up to the mirror and looks at her reflection. Her pose should reference @Image2. After a moment of contemplation, she suddenly breaks down and starts screaming.
```

### 16. Battlefield Tactical Action

```
The man from reference image 1 as the protagonist, agile and athletic, running through a battlefield under a hail of bullets while engaging in intense tactical shooting. Visual Style: Cinematic quality with strong Orange and Teal color grading, high contrast, and visible film grain.
```

## CATEGORIA 3: Sports, Racing & Martial Arts

### 17. Pairs Figure Skating

```
A live performance of competitive pairs figure skating. A low-angle camera follows the skaters, showing ice chips and reflections. During the spin section, the male skater miscalculates briefly, and the female skater adjusts to guide him back into rhythm.
```

### 18. Hollywood Racing Scene

```
Hollywood professional racing style at night in the rain. Shot 1 (00-05s): Close-up inside the veteran driver's car as rain lashes the windshield. He stays calm, nods, and mouths 'Let's go.'
```

### 19. Wuxia Duel

```
An Eastern Wuxia-style duel between a grandmaster in white and a grandmaster in black on an ancient stone platform. Shot 1: Both clash at high speed, leaving afterimages as sparks and a ring-shaped shockwave erupt.
```

### 20. Martial Arts Epic Duel

```
A white-clad swordsman faces a straw-cloaked swordsman in a bamboo forest under heavy rain. The camera slowly pans, shifting focus between raindrops and sword hilts, building tension.
```

### 21. Kite Flying Action Long Take

```
A Chinese youth flies a kite through crowded streets, leaps up steps, flips, lands, and dashes toward a high platform for a difficult jump. A drumbeat erupts as he lands. The entire sequence is a single continuous shot with fluid movements.
```

### 22. Horseback Flower Offering

```
A man in orange rides a brown horse toward a large tree blooming with orange flowers. He plucks two flowers, then other riders follow. The camera pushes in and circles as he dismounts swiftly, then approaches a woman in white on a white horse to present the flowers.
```

## CATEGORIA 4: ASMR, Macro & Sensory

### 23. ASMR Skincare Macro

```
Create a vertical ASMR video with no music, focusing on macro details. A light blue skincare gel bottle sits on glass. A pale, elegant hand gently taps the glass, producing crisp fingernail tapping sounds. The hand picks up the bottle and slowly twists the cap, with the rotation sound clearly audible.
```

### 24. Hands ASMR POV

```
A first-person ASMR video featuring hands. Close-up shots show a pair of slender hands gently interacting with different objects in sequence: scratching frosted glass, rubbing plush fabric, tapping an acrylic board, squeezing bubble wrap, and brushing a wooden comb.
```

### 25. Miniature Cooking Sequence

```
A miniature cooking video on a pure black background with dramatic top lighting. Show full-sized hands carefully placing a tiny cutting board and a fingernail-sized knife. Use elegant classical music as background. The hands slice a tiny garlic clove precisely, add a micro drop of olive oil to a mini frying pan over a tea candle, and crack a small quail egg.
```

### 26. Sizzling Wagyu Steak

```
Close-up of a wagyu steak hitting a hot cast-iron skillet. You can see the fat rendering and bubbles of oil. 2K resolution, shallow depth of field. Sound of loud, aggressive sizzling.
```

## CATEGORIA 5: Commercial & Product

### 27. Luxury Perfume Commercial

```
An ultra-luxury perfume commercial with a dreamy electronic soundtrack and steady drum beats. Begin with a macro shot of a transparent rectangular glass bottle surrounded by violently swirling purple liquid. Capture the churning liquid with bubbles and splashes, accompanied by crisp water sounds.
```

### 28. Coke Interaction Story

```
A narrative Coke interaction scene. A figure looks guilty, glancing left and right before peering out of frame. He quickly reaches, grabs the Coke, takes a sip, and shows a satisfied expression.
```

### 29. Sketch to 3D Car Transformation

```
A car sketch on paper. The camera pushes in. The sketch lines rise off the paper, gaining dimensionality and color, transforming into a photorealistic 3D car driving on a road.
```

### 30. Living Room Renovation Time-Lapse

```
Based on the reference image, generate a time-lapse animation showing the living room transforming from an unfinished, raw concrete interior to a fully renovated space. Final shot: all the lights switch on instantly, accompanied by a realistic light-switch sound effect.
```

### 31. Hollywood Sci-Fi Blockbuster

```
Create a 10-second cinematic sequence in a Hollywood sci-fi style with cyberpunk aesthetics, high-contrast neon lighting, and an epic score feel. 00:00-00:04 - Wide Tracking Shot: Show a futuristic Megacity canyon at night, with rain falling. An anti-gravity vehicle weaves rapidly between skyscrapers.
```

## CATEGORIA 6: Lifestyle, Culture & Character

### 32. Girlfriend POV Vlog

```
Create a 15-second vertical (9:16) handheld vlog in natural golden-hour light, with film grain and slight camera shake. Protagonist: A Taiwanese girl with long, slightly curled hair, wearing a soft knit cardigan and clean, sheer makeup. Scene: Taipei Tamsui riverbank at sunset.
```

### 33. 1920s Jazz Club Charleston

```
Create a Charleston dance sequence in a 1920s jazz club style. A female dancer in a gold-fringed dress and a male dancer in a striped suit perform rapid, syncopated steps, aerial tosses, and large arm swings.
```

### 34. 360 Dessert Shop Selfie

```
360-degree panoramic camera selfie. The camera rotates counterclockwise, capturing the dessert shop interior. Then show a woman posing in different scenes, wearing different outfits, and using different props.
```

### 35. Lunar New Year Family Album

```
The Year of the Horse Lunar New Year family video feature quickly scans through a row of individual family photos, like flipping through a photo album. Each photo 'comes to life' the moment the lens passes.
```

## CATEGORIA 7: Creative & Multi-Reference

### 36. Traversing Famous Paintings

```
@Image1 The girl breaks the fourth wall, traversing multiple worlds of famous paintings while retaining realistic textures. The oil painting worlds are presented in a 3D high-saturation animation style. She stands excitedly under the rotating starry sky in @Image2; then she curiously watches the couple embracing in @Image3.
```

### 37. Healing Storyboard Video

```
Refer to the storyboard of @Image1, including its shot composition, framing, camera movement, visuals, and text. The characters are @Image2, the scenes are @Image3, and the props are @Image4. Create a 15-second healing video.
```

## CATEGORIA 8: Comedy & Concept

### 38. Avengers Alternate Scene

```
Avengers Endgame big fight scene, cinematic style. Thanos suddenly freezes the battle and holds up his hands, looking genuinely apologetic. The superheroes pause, looking surprised, and slowly start to nod and walk away, accepting his apology.
```

### 39. Otter Pilot Documentary

```
A nature documentary scene showing an otter piloting a small airplane. The otter wears aviator goggles and a tiny scarf, paws on the controls, looking focused yet playful.
```

### 40. Friends x Game of Thrones

```
The cast of Friends in a Game of Thrones-style sitcom. Chandler as King Joffrey, wearing a crown and royal robes, acting dramatically spoiled and petulant.
```

## CATEGORIA 9: Fantasy & Sci-Fi

### 41. Alien Jungle Exploration

```
A team of explorers moves cautiously through a dense alien jungle, bioluminescent plants glowing softly around them. The camera pans and tilts to reveal enormous alien trees, mist rising from the ground, and strange creatures watching from a distance.
```

### 42. Steampunk Airship Battle

```
A massive steampunk airship engages in battle above a city. Smoke and steam fill the sky, with smaller airships darting around. Explosions throw sparks into the air. Crew members operate mechanical weaponry, levers, and pulleys with precision.
```

### 43. Samurai Duel at Dawn

```
Two samurai face each other at the crest of a misty mountain at dawn. The first light hits their blades as they bow, eyes locked. Each movement is deliberate and slow, the wind rustling through nearby cherry blossoms.
```

### 44. Post-Apocalyptic City Chase

```
A lone survivor sprints through a crumbling cityscape. Debris falls as buildings lean precariously. Neon signs flicker intermittently. The camera follows from behind, then pans to the side as the survivor leaps across broken streets.
```

### 45. Magical Library Discovery

```
A young mage enters a colossal, enchanted library. Endless shelves stretch into the misty heights. Floating candles and glowing books illuminate the space. The camera sweeps upward, revealing a spiraling staircase and floating staircases.
```

### 46. Cyberpunk Rooftop Showdown

```
Two augmented warriors face off on a neon-lit rooftop in a cyberpunk city. Rain pours, reflecting lights off the slick surfaces. The camera rotates around them as they launch attacks, blades, and cybernetic limbs glowing.
```

### 47. Giant Mech vs Dragon

```
A towering mech engages in battle with a massive dragon atop a crumbling city. Flames and smoke billow, debris scatters. The mech fires energy beams, which the dragon dodges with agile flips.
```

## CATEGORIA 10: Quiet Moments & Slice of Life

### 48. Rainy Night Convenience Store

```
Single continuous shot. A young woman in an oversized hoodie pushes open a convenience store door. Rain streaks the glass behind her. Warm fluorescent light floods over her face. She walks slowly down the snack aisle, trailing one finger along the shelves.
```

### 49. Rooftop Sunrise Yoga

```
A woman practices yoga alone on a high rooftop at sunrise. City skyline stretches behind her, golden hour light catching her silhouette. Camera begins on a slow crane shot from below the roofline, rising until the full cityscape is revealed behind her.
```

### 50. Ramen Shop Late Night

```
Single continuous Steadicam shot. A ramen shop at 1am - near empty. One salaryman sits at the counter, hunched over his bowl. Steam rises. The chef moves behind the counter with practiced economy.
```

## CATEGORIA 11: Nature, Landscape & Weather

### 51. Deep Sea Bioluminescence Dive

```
First-person POV dive footage. A scuba diver descends into a pitch-black ocean. The only light is the diver's torch cutting a narrow beam into the dark. At depth, the torch clicks off. Total darkness for two seconds. Then - faint blue pulses.
```

### 52. Time-Lapse City Day to Night

```
Locked-off wide shot from a high vantage point overlooking a dense city. Time-lapse: morning light sweeps across the skyline, shadows rotate, clouds roll through in fast motion.
```

### 53. Storm Chaser POV Dashcam

```
Handheld dashcam-style footage from inside a vehicle driving toward a massive tornado on a flat American plain. The sky is yellow-green. The funnel is fully formed and tracking left to right across the road ahead.
```

### 54. Northern Lights Time-lapse

```
Locked-off wide shot, Iceland or Norway, winter. Foreground: a lone cabin with a single amber window glowing. Background: dark sky over a snow-covered plain. Time-lapse begins. The aurora emerges - first a pale green ribbon.
```

### 55. Mountain Summit Moment

```
Documentary wide shot. A solo hiker crests a mountain ridge at dawn, silhouetted against an enormous orange sky. She stops. The camera is locked-off and distant - she is a small figure against the scale of the landscape.
```

## CATEGORIA 12: Craft, Art & Live Performance

### 56. Elderly Hands Crafting

```
Close-up, intimate documentary-style footage. An elderly craftsman's hands work clay on a potter's wheel. Extreme close-ups alternate: fingers pressing into clay, water spreading across the spinning surface, the form rising and narrowing under steady pressure.
```

### 57. Ballet Rehearsal Behind the Scenes

```
Documentary-style footage inside a ballet rehearsal studio. Mirrors line one wall. A female principal dancer marks through a solo at half speed, then runs it full out. The camera follows with a slow handheld push as she crosses the studio.
```

### 58. Neon Calligraphy Artist

```
Medium shot, dark studio. A calligraphy artist sits at a lit table. She dips a large brush and begins writing a Chinese character on white paper. The camera pushes slowly in. As the brush moves, the ink trails begin to glow - deep red and gold.
```

### 59. Underwater Ballet Sequence

```
A female dancer performs underwater in a large pool. Flowing white fabric moves around her in slow, unpredictable ways. Camera circles at medium distance using a smooth underwater dolly rig.
```

### 60. Sand Animation Performance

```
Overhead locked-off shot, lit table surface. An artist's hands work sand on a backlit glass surface. She sweeps, pinches, and drags the sand in rapid fluid gestures.
```

## CATEGORIA 13: Magic, Wonder & Transformation

### 61. Children's Chalk Drawing Comes to Life

```
A child crouches on a sunlit pavement, drawing with chalk. The camera slowly pushes in on the drawing. The chalk lines shimmer and lift off the ground, animating: the dog wags its tail, birds take flight, the house glows.
```

### 62. Abandoned Theme Park Exploration

```
A solo urban explorer walks through an abandoned theme park at dusk. Camera follows from behind at medium distance - steadicam, slow and steady. Overgrown carousel comes into frame on the left.
```

### 63. Glassmorphic Product Reveal

```
Pure white studio environment. A perfume bottle or tech device sits centered on a frosted glass plinth. Camera begins tight - extreme close-up on the product surface, catching light and refraction. Slow rotation begins.
```

## CATEGORIA 14: Food, Drink & Urban Culture

### 64. Street Food Night Market

```
Handheld camera weaves through a crowded Southeast Asian night market. Golden light from hanging bulbs reflects off wet pavement. Tight tracking shots move between stalls: a wok erupts in a column of flame, skewers char on an open grill.
```

### 65. Whisky Macro Pour

```
Extreme macro commercial shot. A crystal whisky glass sits on a dark, textured surface. A slow pour begins from above: amber liquid streams into the glass, splashing in extreme slow motion.
```

---

## RIEPILOGO TOTALE

| Fonte | Prompt Esatti | Contenuto Chiave |
|-------|--------------|-----------------|
| GLBgpt | 5 prompt + 5 template | Settings, fix comuni, consistency phrases |
| ChatCut | 20+ prompt + formule | Checklist 10 punti, asset keywords, specifiche tecniche, beat sync |
| Imagine.art | 65 prompt in 14 categorie | La collezione piu grande e varia trovata |
| **TOTALE** | **~90 prompt copy-paste** | + template, formule, vocabolario, checklist |
