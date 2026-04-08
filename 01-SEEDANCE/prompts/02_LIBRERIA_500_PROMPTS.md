# COMPLETE SEEDANCE 2.0 PROMPT LIBRARY

> **Over 500 curated prompts** for video generation with ByteDance's Seedance 2.0.
> Collected from 15+ GitHub repositories and 6+ specialized guides.
> Last updated: March 24, 2026

---

## TABLE OF CONTENTS

1. [PROMPT FRAMEWORK AND STRUCTURE](#1-prompt-framework-and-structure)
2. [CINEMATIC / FILM](#2-cinematic--film)
3. [ANIME / ANIMATION](#3-anime--animation)
4. [COMMERCIAL / ADVERTISING](#4-commercial--advertising)
5. [SOCIAL MEDIA / UGC](#5-social-media--ugc)
6. [NATURE / LANDSCAPE](#6-nature--landscape)
7. [CHARACTER ANIMATION](#7-character-animation)
8. [ABSTRACT / ARTISTIC](#8-abstract--artistic)
9. [PRODUCT SHOWCASE](#9-product-showcase)
10. [ACTION / COMBAT](#10-action--combat)
11. [FANTASY / SCI-FI](#11-fantasy--sci-fi)
12. [FOOD / ASMR / SENSORY](#12-food--asmr--sensory)
13. [MUSIC / DANCE](#13-music--dance)
14. [COMEDY / MEME](#14-comedy--meme)
15. [HORROR / SUSPENSE](#15-horror--suspense)
16. [SPORTS / RACING](#16-sports--racing)
17. [INTIMATE MOMENTS / SLICE OF LIFE](#17-intimate-moments--slice-of-life)
18. [MULTI-SHOT STORYTELLING](#18-multi-shot-storytelling)
19. [AUDIO / LIP-SYNC](#19-audio--lip-sync)
20. [STYLE TRANSFER / VFX](#20-style-transfer--vfx)
21. [APPENDIX: BEST PRACTICES AND TECHNICAL VOCABULARY](#21-appendix-best-practices-and-technical-vocabulary)

---

## 1. PROMPT FRAMEWORK AND STRUCTURE

### 1.1 Universal Formula (5 Segments)

```
Subject + Action + Camera + Style + Constraints
```

**Note:** This structure is the foundation of every effective prompt. The model interprets structured prompts with clear internal logic much better.

### 1.2 Master Template (Copy-Paste)

```
Subject: [a person/object, age or material if relevant]
Action: [specific verb phrase, present tense]
Camera: [shot size] + [movement] + [angle], [focal length]
Style: [one visual anchor: film/process/artist], [lighting], [color treatment]
Constraints: [exclusion list], [frame rate/tempo], [duration or timing], [consistency notes]
```

### 1.3 The 5 Ready-to-Use Templates

**UGC TEMPLATE (Handheld phone effect):**
```
Subject: [person, age range, setting]
Action: [casually talks about X while doing Y]
Camera: Medium, handheld phone perspective, slight sway, eye height, normal lens
Style: Natural indoor light, ungraded look, slight motion blur
Constraints: No captions, no snap zoom, natural hands, 8-10s, simple background
```
> **Why it works:** The handheld sway and absence of color grading communicate authenticity, essential for UGC content.

**PRODUCT AD TEMPLATE (Clean and stable):**
```
Subject: [product name/material/color]
Action: [rotates slowly / slides into frame / subtle hero movement]
Camera: Close-up to medium close-up, slow dolly-in, locked horizon, normal-tele feel
Style: Soft key light + gentle rim, neutral color grade, slight film grain
Constraints: No logos/labels, no flare, hold end frame 2s, 6-8s total
```
> **Why it works:** The slow dolly-in builds desire toward the product; the rim light separates the subject from the background.

**CINEMATIC TEMPLATE (Mood-First):**
```
Subject: [character or location]
Action: [specific beat: waits, turns, breathes, steps into light]
Camera: Wide establishing 2s then slow push to medium, gimbal-smooth, eye height
Style: [single anchor reference, e.g. "natural overcast light, muted blues"]
Constraints: No Dutch angles, no crowds, no neon, maintain overcast look, 10-12s
```
> **Why it works:** A single visual anchor beats six adjectives; the single beat avoids confusing the model.

**TALKING HEAD TEMPLATE (Stable and readable):**
```
Subject: [speaker description]
Action: [delivers a clear phrase]
Camera: Medium close-up, locked tripod or subtle dolly-in, eye height
Style: Soft 45-degree key, clean background separation, neutral grade
Constraints: No auto-captions, no whip pan, natural skin tones, 12-15s, centered eye line
```

**MONTAGE TEMPLATE (Fast beats without chaos):**
```
Subject: [theme, e.g. "morning coffee ritual"]
Action: Beat 1 [wide context], Beat 2 [hand close-up], Beat 3 [steam detail], Beat 4 [sip]
Camera: Each beat 2s, clear shot size per beat, no compound movements - cut transitions
Style: Consistent lighting and palette across beats
Constraints: No text overlay, no speed ramp, constant tempo, 8-10s total
```

### 1.4 Multimodal CRAFT Framework

```
Context + Reference (@assets) + Action + Framing/Timing + Tone/Audio
```

### 1.5 Timeline Structure (for narrative content)

Organize 15-second videos into: setup (0-5s), conflict (5-10s), climax (10-15s).

### 1.6 Quality Suffix (Add to EVERY prompt)

```
4K, Ultra HD, Rich details, Sharp clarity, Cinematic texture, Natural colors,
Soft lighting, No blur, No ghosting, No flickering, Stable picture.
```

### 1.7 Essential Constraint Words

Seedance 2.0 **does not support negative prompts**. Use positive affirmations:
- "Maintain face and clothing consistency, no distortion, high detail."
- "Character face stable without deformation, normal human structure, natural smooth movements."
- "Generate video without subtitles"

---

## 2. CINEMATIC / FILM

### P-001. Pizzeria Cinematic Sequence
```
Single continuous cinematic shot, no music. From outside the glass window, the dim
camera slowly pushes inward into a pizza shop. Inside, a chef stretches dough in the
air, catches it, spreads sauce, and slides it into a wood-fired oven. A customer at the
counter watches, mesmerized. Warm amber lighting from the oven, flour particles
floating in the air.
```
> **Effectiveness:** The continuous uncut shot creates total immersion. The "no music" specification forces the model to generate realistic ambient sounds.

### P-002. Cave Exploration POV
```
First-person POV handheld footage with slight natural shake. The only light comes from
a headlamp cutting through absolute darkness. Dripping water echoes. The beam reveals
ancient crystal formations glowing faintly blue and purple. Hands reach out to touch a
crystal surface. Sound of heavy breathing reverberates.
```
> **Effectiveness:** The first-person POV with natural shake creates cinematic tension. The single light source specification guides the lighting rendering.

### P-003. Knight in the Cave (Multi-Shot)
```
A multi-shot sequence of a knight in silver armor. Shot 1: Wide shot as he enters a
dark cave with a torch. Shot 2: Close-up of his nervous eyes. Shot 3: He draws his
sword, which glows blue, illuminating the entire cavern to reveal a massive sleeping
dragon.
```
> **Effectiveness:** The multi-shot structure with narrative progression (entrance -> tension -> reveal) creates a complete mini-film.

### P-004. Pianist with Butterfly Lighting
```
Cinematic butterfly lighting. Medium shot of a handsome pianist wearing a simple,
elegant black suit, performing passionately at a grand piano in a dimly lit concert hall.
Soft spotlight from above creates butterfly shadow beneath his nose. Fingers move
fluidly across keys. Shallow depth of field isolates him from the blurred audience.
```
> **Effectiveness:** The technical term "butterfly lighting" activates a specific, professional lighting scheme in the model.

### P-005. Steadicam from Cafe to Subway
```
Steadicam long take following a man from a warm, yellow-lit cafe into a cool-toned,
busy street, then descending stairs into a subway station. The color temperature shifts
gradually from warm amber to cold fluorescent blue. Background transitions from quiet
murmur to urban cacophony to echoing tunnel acoustics.
```
> **Effectiveness:** The color temperature transition (warm -> cool) and the ambient sound evolution create a complete sensory journey in a single shot.

### P-006. Retro 90s Hong Kong Film
```
90s Hong Kong art cinema style with retro grain, yellow-green tint, and step-printing
effect. A melancholic young woman in a trench coat stands at a phone booth in the rain.
She lifts the receiver, pauses, then hangs up without dialing. Neon bokeh reflections
on wet pavement. Camera pulls back slowly as she walks away, trailing shadows behind
her in the step-printed frames.
```
> **Effectiveness:** The precise stylistic references (Wong Kar-wai) with specific techniques (step-printing, yellow-green tint) give the model a strong visual anchor.

### P-007. Denis Villeneuve-Style Desert Scene
```
IMAX 70mm film approach. A colossal sandstorm wall approaches a military convoy in a
vast desert. Shot 1: Extreme wide establishing the scale of the storm versus tiny
vehicles. Shot 2: Inside cockpit, pilot screams "GO! GO!" gripping controls in panic.
Shot 3: Convoy attempts emergency U-turn as sand engulfs vehicles. Shot 4: Slow-motion
dune jump with vehicle silhouetted against lightning within the storm, debris suspended
in air.
```
> **Effectiveness:** The "IMAX 70mm" reference sets scale and granularity. The macro-to-micro progression creates epic cinematic tension.

### P-008. Film Noir Woman in Red
```
A woman in a red dress walks confidently down a rainy city street at night, neon
reflections on wet pavement, film noir style, tracking shot. High contrast chiaroscuro
lighting, the red dress is the only saturated color in an otherwise desaturated frame.
Her heels click rhythmically on the wet asphalt.
```
> **Effectiveness:** Chromatic isolation (red on desaturated) is a classic cinematic trick that the model executes well.

### P-009. Traveler at Sunset (Dolly Push-In)
```
A weary traveler in a dusty leather cloak. He slowly removes his wide-brimmed hat and
exhales, looking toward a sunset. Low-angle medium shot, slow dolly-in towards his
face, shallow depth of field. Golden hour backlighting creates a warm halo around his
silhouette. Dust particles dance in the amber light.
```
> **Effectiveness:** The slow dolly-in with low angle conveys respect and grandeur for the character, a classic western technique.

### P-010. Surreal Ronin Scene
```
Complex action sequence with a masked warrior fighting a winged beast on floating
islands during a thunderstorm. Handheld camera chaos captures impossible gravity-defying
leaps between crumbling rock platforms. Lightning illuminates the scene in stroboscopic
flashes. The warrior's tattered cloak trails behind during each impossible jump.
```
> **Effectiveness:** The combination of fantastical elements with chaotic handheld camera creates a contrast that makes the scene visceral and believable.

### P-011. Luxury Car Transforms into Optimus Prime
```
A luxury sports car driving through rainy Tokyo at night suddenly begins transforming
into Optimus Prime. CGI battle scene as the transformed mech fights Godzilla between
skyscrapers. Explosions light up neon-reflected puddles. Energy blasts create shockwaves
that shatter windows. Camera orbits the battle from a news helicopter perspective.
```
> **Effectiveness:** The mix of recognizable brands with a specific setting (nighttime Tokyo) and the "news helicopter" perspective create a sense of realistic event coverage.

### P-012. Live-Action Anime Adaptation: Water vs Thunder Duel
```
Hollywood-style samurai duel with elemental special effects. A water-breathing swordsman
faces a thunder-breathing warrior in a rain-soaked temple courtyard. 15 seconds total.
0-5s: They face each other, rain freezes mid-air between them. 5-10s: Explosive clash,
water serpents meet lightning bolts. 10-15s: Slow-motion aftermath, both kneel, temple
crumbles behind them. Cinematic 2.39:1 aspect ratio.
```
> **Effectiveness:** The precise timeline structure (0-5s, 5-10s, 10-15s) guides the model on what to generate in each segment.

### P-013. Speeder Chase Through the Cliff City
```
Single continuous shot featuring a high-speed chase through monumental cliffside
architecture. A hovering speeder weaves between carved stone buildings and hanging
bridges. Camera mounted on pursuing vehicle, slight vibration from engine. Wind
distortion on audio. Near-misses with market stalls and pedestrians who dive out of
the way.
```
> **Effectiveness:** The "camera mounted on pursuing vehicle" specification creates an immersive perspective with diegetic motivation for the camera movement.

### P-014. John Woo Style - Corridor Bullet Ballet
```
Corridor gunfight in John Woo signature style. Two suited men exchange fire in a narrow
hallway. Rhythm editing with snap-zooms on shell casings ejecting. Slow-motion dove
flies between combatants. Impact beats synchronized to gunfire rhythm. One man slides
on his knees firing both pistols. Spent cartridges ring on marble floor.
```
> **Effectiveness:** The John Woo reference activates a specific recognizable style. The rhythmic details (shell casings, doves) are stylistic trademarks the model knows.

### P-015. Spy Brawl: Suit vs Suit
```
Spy brawl in cramped office space. Two men in tailored suits exchange rapid blows using
office furniture as weapons. Rapid angle switches between over-shoulder and wide shots.
Clean choreography with keyboard used as shield, monitor as projectile. Comedic ending:
both pause, straighten ties simultaneously, resume fighting.
```
> **Effectiveness:** The contrast between elegance (tailored suits) and chaos (fighting with furniture) creates visual interest. The comedic ending adds a memorable narrative beat.

### P-016. Cathedral Under the Black Sea
```
Underwater descent through a flooded megastructure. Camera follows a diver sinking past
massive stone columns covered in bioluminescent coral. A leviathan silhouette passes in
the distant murk. Vertigo-inducing downward camera movement. Shafts of surface light
pierce the depth, creating god rays through particulate water.
```
> **Effectiveness:** The "vertigo-inducing downward" camera movement and the progressive reveal (columns -> coral -> leviathan) build escalating tension.

### P-017. Realistic Cinematic Portrait
```
Dramatic character reveal. A mysterious figure emerges from shadows into golden hour
light, long black coat billowing in wind. Turns with intense piercing eyes toward camera.
Wide shot transitioning to close-up. Cinematic high contrast, film noir aesthetic with
dramatic rim lighting. Shallow depth of field isolates subject from urban background.
```
> **Effectiveness:** The wide-to-close-up transition during a reveal is a fundamental narrative cinema technique.

### P-018. Kitchen Thriller Scene
```
Dark, moody kitchen lit by a single pendant light. Five shots: Shot 1: Over-shoulder of
man staring at phone on table. Shot 2: Woman across table, arms crossed, cold expression.
Shot 3: Close-up man's hand reaching for phone. Shot 4: Woman's hand slams on his.
Shot 5: Profile two-shot, tension palpable, neither speaks. Sound: clock ticking,
refrigerator hum, breathing.
```
> **Effectiveness:** The domestic thriller demonstrates that special effects aren't needed: tension comes from editing and ambient sound.

### P-019. Hollywood Night Race
```
Hollywood professional racing style at night in the rain. Shot 1 (00-05s): Close-up
inside the veteran driver's car, hands grip wheel, eyes narrow with focus, rain
hammering windshield. Shot 2 (05-10s): External tracking shot as the car accelerates
through a sweeping turn, water spray creating a rooster tail of mist. Shot 3 (10-15s):
Drone shot from above showing the car's headlights cutting through rain on an empty
mountain road.
```
> **Effectiveness:** The interior -> exterior -> aerial progression across three shots creates visual escalation typical of racing films.

### P-020. Wong Kar-wai Style Phone Scene
```
Wong Kar-wai rainy phone booth scene. 90s Hong Kong art cinema aesthetic. Rain-covered
phone booth, character in trench coat with melancholic posture. Frame stepping effects
create dreamlike motion. Neon bokeh lighting reflects in every water droplet. Character
exits, trailing shadows multiply due to step-printing effect. Warm yellow-green color
cast throughout.
```
> **Effectiveness:** The specific director reference combined with precise techniques (step-printing, neon bokeh) creates a stylistically coherent result.

---

## 3. ANIME / ANIMATION

### P-021. Healing Anime Girl
```
An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat,
standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the
camera and smiles gently. A light breeze moves her hair and dress. The camera slowly
pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and
peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion,
high detail.
```
> **Effectiveness:** The "healing" prompt is a specific anime genre. The face and clothing consistency specification prevents morphing between frames.

### P-022. Cyberpunk Samurai Duel
```
Cyberpunk samurai with glowing katana faces robotic ninja. Scene 1: Quick zoom on
samurai drawing blade, blue energy crackles along the edge. Scene 2: Wide shot, both
dash towards each other on neon-lit Tokyo street. Scene 3: Extreme close-up of blades
clashing, sparks fly, white flash fills frame. Style: Cyberpunk: Edgerunners anime,
high contrast, fast cuts, motion blur.
```
> **Effectiveness:** The "Cyberpunk: Edgerunners" reference is a powerful stylistic anchor the model recognizes, defining palette and rhythm.

### P-023. Reluctant Hero - Character Narrative
```
A young, timid librarian with messy brown hair and glasses discovers a glowing, ancient
book. Scene 1: nervously pushes glasses up, surrounded by dusty tomes, eyes wide with
fear. Scene 2: book opens, bathing him in golden light, shows determined awe. Scene 3:
stands tall, book held tightly, confident smile as library transforms around him.
Style: Ghibli-inspired, warm lighting, emotional close-ups.
```
> **Effectiveness:** The three-scene emotional arc (fear -> wonder -> determination) creates a complete mini-story in Ghibli style.

### P-024. Emotional Arc - Overcoming Insecurity
```
Shy artist with sketchbook of beautiful hidden drawings. Scene 1: Sits alone in park,
nervously hiding sketchbook, downcast expression. Scene 2: Child peeks over shoulder at
drawing, artist startled, sees child's face light up with wonder. Scene 3: Artist
smiles warmly, confidently displaying art on easel in the park.
Style: Soft pastel anime, gentle sunlight, focus on facial expressions.
```
> **Effectiveness:** The soft pastel palette and focus on facial expressions are stylistic choices that reinforce the emotional theme.

### P-025. Overdramatic Cat - Anime Comedy
```
Fluffy white cat sleeping on laptop keyboard. Scene 1: Owner gently nudges cat, it
opens one eye with deadpan stare. Scene 2: Lifts cat, which goes completely stiff and
board-like in protest, extreme close-up on offended, wide-eyed expression. Scene 3:
Places stiff cat on floor, remains upright before slowly toppling over like a statue.
Style: Slice-of-life anime, clean lines, exaggerated chibi-style reaction faces.
```
> **Effectiveness:** The exaggerated chibi-style expressions are an anime convention the model executes well, creating visual comedy.

### P-026. Anime E-Commerce Streetwear Showcase
```
Cool, confident young woman with silver hair wearing stylish black 'CyberGlow' brand
hoodie with neon-green accents. Scene 1: Sketching graffiti in notebook on nighttime
city rooftop, hoodie's logo subtly visible. Scene 2: Sudden downpour starts; quickly
pulls up hood, water-resistant fabric deflects raindrops, smirks. Scene 3: Stands
looking over neon-lit city, hoodie's glowing accents matching skyline.
Style: Cyberpunk anime, vibrant neon colors, dynamic camera angles, close-up on fabric texture.
```
> **Effectiveness:** Integrating the product into the narrative (rain demonstrates water-resistance) is superior to simple static display.

### P-027. Anime Meme Adaptation - Distracted Boyfriend
```
Anime adaptation of distracted boyfriend meme. Scene 1: Stoic samurai with top-knot and
blue kimono walks beside cheerful shrine maiden in red and white miko outfit. Scene 2:
Powerful female warrior with silver armor and glowing sword walks past; samurai's head
turns, looking impressed and shocked. Scene 3: Close-up on shrine maiden with angry,
betrayed glare. Style: Crisp modern anime, high-contrast, dramatic expressions.
```
> **Effectiveness:** Reinterpreting memes in anime style is a viral format. The dramatic expressions amplify the comedic effect.

### P-028. Anime Educational Productivity Tip
```
Stressed anime office worker with messy black hair overwhelmed by giant, monstrous pile
of paperwork. Scene 1: Close-up on tired face, sighing in despair. Scene 2: Small,
friendly robot flies in, projects simple 2-minute timer, points to one paper. Scene 3:
Worker focuses, finishes one task as timer ends, relieved smile as one paper vanishes.
Text overlay: 'Beat procrastination. Try the 2-Minute Rule.'
Style: Modern anime, clean lines, high-contrast colors, simple animated text graphics.
```
> **Effectiveness:** The educational format in anime style makes informational content visually engaging.

### P-029. Cyberpunk Noir Detective
```
Lone detective in trench coat stands on rain-slicked city street, looking up at
monolithic skyscraper. Scene 1: Close-up on face, illuminated only by flickering
holographic ad. Scene 2: Wide shot of street with flying vehicles and glowing neon
signs reflecting in puddles. Scene 3: Detective pulls up collar, single datastream
visible in cybernetic eye.
Style: Cyberpunk noir, high contrast, saturated neon palette (pinks and teals),
dramatic shadows, cinematic bloom effect, detailed cel-shading.
```
> **Effectiveness:** The combination of classic noir with cyberpunk creates a strong aesthetic. The "datastream in cybernetic eye" detail is a powerful narrative micro-moment.

### P-030. Anime Girl Dance with Motion Capture
```
Anime girl performing an elegant dance sequence on a virtual stage. Motion capture
quality movements with fluid transitions between poses. Cherry blossom petals float
around her. Camera orbits smoothly at medium distance. Soft volumetric lighting creates
atmosphere. Hair and clothing physics respond naturally to each movement.
```
> **Effectiveness:** The "motion capture quality" specification tells the model to aim for a higher level of movement fluidity and realism.

### P-031. Ice-Fire Clash Nezha and Ao Bing
```
Four-act anime battle testing dynamic transitions. Act 1: Stillness to burst
acceleration as two warriors face each other. Act 2: Attribute transition from flame
to ice as attacks collide and transform. Act 3: Fierce physics collision with spiraling
motion and energy vortex. Act 4: Space-folding particle continuity as ice shatters
into flame fragments that reform into new attacks. Vibrant saturated colors, extreme
dynamic camera.
```
> **Effectiveness:** The 4-act structure with attribute transitions (fire -> ice -> fusion) tests the model's advanced capabilities.

### P-032. Anime Otter Mecha Battle
```
An otter enters a large mech suit. Mechanical parts and gears turn with satisfying
clicks. The otter gives a grim thumbs up from the cockpit window. The mech launches
into battle against a colossal marble octopus in a ruined cityscape. Anime mecha style,
dramatic impact frames, speed lines during charges.
```
> **Effectiveness:** The absurd element (otter pilots mecha) combined with the seriousness of the mecha genre creates a visually interesting contrast.

### P-033. Jujutsu Kaisen Style Scene
```
Jujutsu Kaisen-style scene. A dark-haired sorcerer with bandaged arms unleashes a domain
expansion. Blue magical energy erupts from the ground in geometric patterns. Flying
spectral swords materialize and orbit. Dramatic Japanese text overlay appears with
impact. Epic orchestral beats. Camera pulls back to reveal the full scope of the domain
as buildings bend and crack around the energy field.
```
> **Effectiveness:** The specific anime reference (Jujutsu Kaisen) with key franchise elements (domain expansion, spectral swords) creates a recognizable result.

### P-034. Anime Martial Arts Tournament
```
Figure 1 character battling Figure 2 character in the World Martial Arts Tournament.
Wide arena with cheering crowd. Dragon Ball Z style energy auras around both fighters.
Rapid exchange of blows with impact shockwaves. Camera switches between close combat
and crowd reaction shots. Dramatic pause before final attack.
```
> **Effectiveness:** Using image references (@Image1, @Image2) for characters ensures visual consistency during combat.

---

## 4. COMMERCIAL / ADVERTISING

### P-035. Ultra-Luxury Perfume Spot
```
An ultra-luxury perfume commercial with a dreamy electronic soundtrack and steady drum
beats. Opening: Macro shot of perfume bottle, light refracts through crystal-cut glass
creating rainbow prismatic patterns. Middle: A model's hand slowly reaches for the
bottle, fingertips barely touching. Close: Model applies perfume to wrist, closes eyes,
slight smile. Final: Bottle hero shot with soft bokeh background, brand light appears.
```
> **Effectiveness:** The macro -> interaction -> hero shot progression is the classic perfume ad structure the model faithfully reproduces.

### P-036. Narrative Coca-Cola Spot
```
A narrative Coke interaction scene. A painted figure on a wall looks guilty, glancing
left and right. Its hand reaches out of the painting frame, grabs a Coke bottle from a
nearby table. Drinks it quickly, hides it behind the frame. A cowboy figure from another
painting takes the glass. Spotlight hits the Coke bottle for final hero shot on dramatic
black background.
```
> **Effectiveness:** Anthropomorphizing paintings that interact with real products creates a memorable and viral advertising concept.

### P-037. From Sketch to 3D Car
```
A car sketch on paper. The camera pushes in slowly. The sketch lines rise off the paper
and begin assembling in three dimensions. Wire-frame becomes solid surfaces. Color fills
in from front to back. Final: Fully rendered photorealistic car rotates on a showroom
turntable. Camera pulls back to reveal the original sketch beside the final car.
Transformation takes 10 seconds. Clean white studio environment.
```
> **Effectiveness:** The 2D-to-3D transformation is an advertising format that showcases the "creative process" behind the product.

### P-038. Living Room Renovation Time-Lapse
```
Based on the reference image, generate a time-lapse animation showing the living room
transforming from raw concrete and exposed wiring to a fully furnished, warm modern
home. Workers appear and disappear in fast-forward. Paint rolls onto walls, furniture
slides into place. Final reveal: Warm evening lighting turns on, camera slowly pans
across the finished room.
```
> **Effectiveness:** The renovation time-lapse is a popular social media format that the model handles well with image references.

### P-039. Hollywood Sci-Fi Blockbuster
```
Create a 10-second cinematic sequence in a Hollywood sci-fi style with cyberpunk
aesthetics. A flying vehicle chase through a megacity canyon of neon-lit skyscrapers.
Vehicle weaves between holographic advertisements and floating traffic. Camera mounted
on pursuing vehicle with slight vibration. Rain creates streaks on the virtual camera
lens.
```
> **Effectiveness:** Rain on virtual lenses is a subtle detail that adds cinematic realism to the CGI scene.

### P-040. MUJI Promotional Video
```
A MUJI brand promotional video. Minimalist Japanese aesthetic. Slow, contemplative
camera movement through a pristine store. Close-ups of natural materials: wood grain,
cotton fabric texture, ceramic smoothness. No people, no text. Only products breathing
in natural light. Warm wood tones, white spaces, zen-like atmosphere. Each shot holds
for 3 seconds before gentle dissolve transition.
```
> **Effectiveness:** The absence of people and text lets the materials "speak," consistent with the brand's philosophy.

### P-041. Perfume MG Animation
```
Product advertisement combining motion graphics with perfume bottle integration. The
bottle floats and rotates in abstract space as geometric shapes pulse around it. Natural
female voiceover describes the scent. Natural lighting, no texture overlays, brisk
pacing. Gold particles stream from the bottle nozzle forming elegant calligraphic
patterns in the air.
```
> **Effectiveness:** The combination of motion graphics with a physical product creates a modern, sophisticated visual hybrid.

### P-042. Premium Unboxing
```
Show premium product unboxing with close-up shots, animated text highlighting features,
smooth panning to brand logos. Top-down view transitioning to 45-degree angle ending
with close-up on logo. Clean minimalist Apple-style photography with soft studio
lighting. Hands with manicured nails slowly lift lid, tissue paper rustles. Product
gleams under focused spotlight.
```
> **Effectiveness:** The "Apple-like" style is a strong visual anchor that communicates premium quality. The top-down -> 45-degree angle transition is a classic unboxing technique.

### P-043. Lifestyle Product Integration
```
Create lifestyle ad showing people using product in different daily scenarios: morning
coffee ritual with product on kitchen counter, afternoon work session with product on
desk, evening relaxation with product on nightstand. Brand colors and logo subtly visible
in each scene. Handheld documentary style, warm authentic aesthetic, 15 seconds total,
3 distinct scenes of 5 seconds each.
```
> **Effectiveness:** Integration across three daily moments associates the product with the user's routine, a proven advertising technique.

### P-044. Coffee Beverage Spot
```
Steaming cup of premium coffee on rustic wooden table. Cream pours slowly creating
swirling patterns visible from above. Morning light streams through window creating warm
shafts of light with dust particles. Macro close-up, slow motion pour at 120fps feel.
Warm cozy aesthetic. Sound: gentle pouring, ceramic contact, satisfied sigh.
```
> **Effectiveness:** The "120fps feel" in macro on the cream pour is an extremely engaging ASMR-advertising format.

### P-045. Tech Product Demo
```
Sleek smartphone rotates on reflective black surface. Screen lights up showing app
interface with fluid animations. Holographic UI elements appear around the device,
expanding features into floating diagrams. 360-degree orbit around product. Futuristic
premium tech style with dark background and accent lighting. Subtle particle effects
trail the rotation.
```
> **Effectiveness:** Holographic UI elements emerging from the device communicate technological innovation in a visually spectacular way.

### P-046. Fashion Runway
```
Model in long black silk dress walking down a runway. 0-4s: Side-angle tracking shot
capturing the full length of the dress flowing with movement. 4-8s: Gradual orbit
showcasing fabric sheen and texture under runway spotlights. 8-12s: Confident stride
with elegant skirt curve at the turn. 12-15s: Push to frontal close-up showing face
and jewelry details. Fashion show ambient sound with camera shutters.
```
> **Effectiveness:** The timeline structure with progression from dress to face follows the viewer's natural attention at a fashion show.

### P-047. Smartphone Showcase
```
Premium phone with metallic body on gradient background. 0-3s: 360-degree rotation
showing all angles with light reflecting off polished surfaces. 3-7s: Macro shot of
side panel showing button precision and port alignment. 7-10s: Screen illuminates with
fingerprint sensor animation. 10-15s: Camera drifts into the screen where UI elements
breathe and animate organically.
```
> **Effectiveness:** The "into the screen" transition is a WOW effect the model handles well with the right wording.

### P-048. Coffee Machine
```
Coffee machine on wooden table. 0-4s: Powers on with subtle LED glow, steam begins
rising from preheating. 4-8s: Macro of espresso drops creating concentric ripples in
cup. 8-12s: Steam envelops the cup in wisps, camera catches light through vapor.
12-15s: Camera drifts toward the coffee surface reflection where the machine is visible
inverted. Warm domestic lighting, product photography quality.
```
> **Effectiveness:** The machine's reflection on the coffee surface in the final shot is a sophisticated visual detail.

---

## 5. SOCIAL MEDIA / UGC

### P-049. Girlfriend POV Vlog
```
Create a 15-second vertical (9:16) handheld vlog in natural golden-hour light. A
Taiwanese girl at the Tamsui riverbank smiles directly into camera while walking
backward. She says "Come on, the sunset's about to start!" Hair blows in the sea
breeze. She turns and points at the orange sky. Handheld phone perspective with natural
sway. Warm, ungraded look.
```
> **Effectiveness:** The vertical 9:16 format with direct-to-camera address creates the "girlfriend POV" format that goes viral on TikTok/Reels.

### P-050. 360-Degree Selfie in Dessert Shop
```
360-degree panoramic camera selfie. The camera rotates counterclockwise, capturing a
dessert shop interior with pastel walls, display cases of colorful macarons, and hanging
fairy lights. The person changes outfit at each 90-degree rotation: casual -> business
-> evening dress -> sportswear. Same hairstyle and face maintained throughout.
Background customers continue naturally.
```
> **Effectiveness:** The outfit change during the 360 rotation is a viral format that tests the model's ability to maintain face consistency during transformations.

### P-051. Comedic Cat Meme
```
Fast-paced video of cat knocking over objects with exaggerated reactions. Cat sits on
shelf next to vase, looks directly at owner with defiant stare, slowly pushes vase off
edge. Owner gasps. Cat immediately knocks second item. Quick cuts and sudden zoom-ins
on cat's face after each destruction. Meme aesthetic with bold expressions. Fast-paced
comedic timing.
```
> **Effectiveness:** The sudden zooms on cat reactions are the visual language of viral memes that the model replicates well.

### P-052. Morning Routine Montage
```
College student morning routine with upbeat background music. Jump cuts between scenes:
alarm clock slap, stumbling to bathroom, messy toothbrushing, burning toast, grabbing
backpack while hopping into shoe. Text overlays highlighting key moments. Jump cuts
every 2-3 seconds with mixed angles. TikTok/Instagram aesthetic, bright and energetic
style, slightly overexposed like a phone camera.
```
> **Effectiveness:** Jump cuts every 2-3 seconds with the "slightly overexposed like a phone camera" aesthetic perfectly replicate the look of organic UGC content.

### P-053. Before/After Transformation
```
Split-screen fitness journey transformation showing starting point and result with
dramatic reveal at end. Static framing with synchronized movements on both sides: left
side shows struggling workout, right side shows confident version of same exercise.
Light flash transition reveals final comparison. Motivational content, high contrast
inspiring style.
```
> **Effectiveness:** The synchronized split-screen and transformation format are among the most shared on fitness social media.

### P-054. High Society Drama (Real vs Fake Heiress)
```
Luxurious banquet setting. Scene 1: Fake heiress in white gown "accidentally" breaks
antique vase, cries pitifully to gain sympathy from guests. Scene 2: True heiress in
black swan gown produces DNA test document, dramatic slap across fake heiress's face in
slow motion. Scene 3: True heiress sits on ornate throne wearing crown, guests bow.
Dialogue-driven with dramatic slow motion and quick reaction cuts. Golden hour lighting.
```
> **Effectiveness:** The "short drama" format with archetypal roles (real vs fake heiress) is massively viral on Chinese platforms and is exploding globally.

### P-055. CEO Revenge Story
```
Modern luxury office setting. Scene 1: Humble employee receives dismissal letter,
colleagues smirk in background. Scene 2: Six months later title card. Same employee
returns in designer suit, announces purchase of the company. Former boss turns pale.
Scene 3: New CEO sits in power chair, spins dramatically toward camera. Colleagues bow.
Power shots from below, dramatic reveals, reaction close-ups, golden hour lighting.
```
> **Effectiveness:** The "revenge" narrative arc with low-angle power shots is a short drama format that generates millions of views.

### P-056. Giant Orange Cat Meme
```
Mockumentary documentary perspective. A Godzilla-sized orange tabby cat stuck between
city skyscrapers, looking confused. Cat sneezes, blowing away hats and leaves across
city blocks. Cut to: Cat's paw resting on a bridge, blocking all traffic. Police
helicopter circles. Final: Innocent cat expression freeze-frame with documentary-style
caption. Deadpan documentary camera style with shaky zoom-ins.
```
> **Effectiveness:** The "mockumentary" style with documentary camera applied to an absurd subject creates sophisticated, shareable humor.

### P-057. Surreal Mirror Glitch (UGC)
```
Bathroom vlog style. Person brushing teeth normally in front of mirror. They step away
from mirror but reflection continues brushing teeth independently. Person notices,
leans back in - reflection is now ahead in the routine, gargling. Person leaves frame
entirely. Reflection "fast-forwards" through the entire morning routine, then looks
directly at camera and waves before disappearing completely. Handheld phone camera,
bathroom fluorescent lighting.
```
> **Effectiveness:** The "mirror glitch" concept is a light-horror format perfect for social media, playing on the ancestral fear of an autonomous reflection.

### P-058. Hanging Laundry Vlog
```
The girl gracefully hangs the clothes out to dry on a sunny balcony. After finishing
one piece, she takes another from the bucket and shakes it vigorously, creating small
water droplets that catch sunlight like tiny diamonds. Rhythmic, satisfying repetition.
Natural daylight, gentle breeze moves hanging fabrics. Slightly slow motion on water
droplets. Healing, peaceful domestic atmosphere.
```
> **Effectiveness:** Poeticizing an everyday activity with slow-motion on water droplets creates the "healing content" format hugely popular in Asia.

### P-059. Lunar New Year Family Album
```
The Year of the Horse Lunar New Year family video. Camera quickly scans through a row
of individual portrait photos. Each photo comes to life: grandmother waves, father
laughs, child makes peace sign, dog barks. Photos return to still frames. Final wide
shot shows all portraits on a wall with the family sitting beneath them in matching
red outfits. Warm festival lighting, red and gold color palette.
```
> **Effectiveness:** The static-photos-coming-to-life transition is a powerful emotional effect for celebratory family content.

---

## 6. NATURE / LANDSCAPE

### P-060. Bioluminescent Deep Sea Dive
```
First-person POV dive footage. A scuba diver descends into a pitch-black ocean abyss.
At first, nothing but darkness and the sound of breathing through the regulator. Then,
bioluminescent creatures begin appearing: first tiny specks like underwater stars, then
larger jellyfish with pulsing blue light, finally a massive bioluminescent whale passes
below, illuminating an underwater canyon. Pressure sounds intensify with depth.
```
> **Effectiveness:** The progressive reveal from darkness to bioluminescent light creates an arc of growing wonder without the need for narration.

### P-061. Day-to-Night City Time-Lapse
```
Locked-off wide shot from a high vantage point overlooking a dense city skyline.
Accelerated time-lapse: shadows of buildings rotate clockwise as sun crosses the sky.
Golden hour bathes everything in amber. Lights begin switching on building by building.
Full night: the city becomes a grid of light. Stars appear above. Traffic creates light
trails on highways below.
```
> **Effectiveness:** The fixed "locked-off" shot with time-lapse is a format the model handles very well, showing the natural transition of time.

### P-062. Storm Chaser Dashcam POV
```
Handheld dashcam-style footage from inside a vehicle driving toward a massive tornado
on a flat prairie. Yellow-green sky dominates the upper frame. Wind rocks the vehicle.
Debris begins crossing the road. The tornado grows larger in the windshield with each
passing second. Radio crackles with weather alerts. Driver's hands visible gripping
the steering wheel white-knuckled.
```
> **Effectiveness:** The dashcam perspective with the yellow-green sky (a real tornado indicator) creates an immersive and terrifying experience.

### P-063. Aurora Borealis Time-Lapse
```
Locked-off wide shot, Iceland or Norway, winter. Foreground: a lone cabin with a single
amber window glowing warmly. Middle ground: snow-covered landscape perfectly still.
Sky: Aurora borealis begins as a faint green ribbon, then intensifies into curtains of
green, purple, and pink rippling across the entire sky. Stars visible through the
aurora. Absolute silence except for occasional wind.
```
> **Effectiveness:** The contrast between the small warm cabin and the vastness of the aurora creates an emotionally powerful composition.

### P-064. Mountain Summit Moment
```
Documentary wide shot. A solo hiker crests a mountain ridge at dawn. Silhouette against
an orange-pink sky. Clouds fill the valley below like a sea. The hiker pauses, removes
backpack, and stands still absorbing the view. Camera holds the wide shot for 5 seconds
before slow push-in to medium shot. Wind sounds, heavy breathing that gradually calms.
```
> **Effectiveness:** The "camera holds for 5 seconds" is a deliberate directorial choice that lets the moment breathe, creating emotional impact.

### P-065. Alien Jungle
```
A team of explorers moves cautiously through a dense alien jungle. Bioluminescent plants
pulse with rhythmic light like heartbeats. Strange creatures watch from canopy shadows.
One explorer's scanner beeps rapidly. Camera follows the team from behind at ground
level, creating a sense of vulnerability. Fog rolls along the ground. Alien bird calls
echo.
```
> **Effectiveness:** The ground-level camera behind the team creates vulnerability. The specific sound details (scanner, alien calls) add sensory depth.

### P-066. Steampunk Airship Battle
```
A massive steampunk airship engages in battle above a Victorian city. Gears and pulleys
visible on the hull strain under fire. Propellers create vortices in smoke from cannon
fire. A smaller zippy craft weaves between the larger ships. Camera follows the small
craft in a continuous tracking shot. Brass, copper, and leather textures dominate.
Steam vents from hull breaches.
```
> **Effectiveness:** The continuous tracking of the small ship among the larger ones creates dynamism and scale, a classic technique from cinematic aerial battles.

---

## 7. CHARACTER ANIMATION

### P-067. Professional Avatar Speaker
```
Male in navy suit, early 30s, clean-shaven with professional haircut. Modern office
setting with urban skyline through floor-to-ceiling windows. Speaks directly to camera:
"AI is redefining the way we live and work." Lip-sync with @Audio1. Natural hand
gestures accompanying speech rhythm. Maintains eye contact. Cinematic three-point
lighting. Medium close-up, slight dolly-in during key phrase.
```
> **Effectiveness:** The "lip-sync with @Audio1" specification activates Seedance 2.0's native lip-sync for spoken content.

### P-068. Animated Cartoon Girl
```
Animated character with pink pigtails and large expressive eyes in a rainbow-colored
room filled with cute decorations. Says excitedly: "This little trick is super useful!"
Lively but fluid expressions matching vocal rhythm. Head tilts, eyes widen on emphasis
words. Hands gesture enthusiastically. Kawaii anime style with bouncy animation
principles. Bright, saturated colors.
```
> **Effectiveness:** The "expressions matching vocal rhythm" indication guides the model to synchronize facial expressions with speech.

### P-069. On-Camera Female Presenter
```
Female with long black hair, red lipstick, white silk blouse. Professional studio
setting with three-point lighting and clean gradient background. Speaks to camera:
"This product will transform your daily efficiency." Subtle refined gestures. Composed
posture with minimal movement. Warm, trustworthy expression. Medium shot with slight
push-in for emphasis on key message.
```
> **Effectiveness:** The "subtle refined gestures" specification avoids excessive movements that can look unnatural in AI-generated videos.

### P-070. Veteran Historian
```
Elderly man with white hair, wire-rimmed glasses, tweed jacket in a candlelit library
filled with ancient books. Reflects quietly, then speaks slowly: "A thousand years ago,
that battle changed everything..." Measured, deliberate gestures conveying wisdom and
gravitas. Camera slowly pushes in as he speaks. Warm amber candlelight flickers on his
face. Old leather and paper textures visible.
```
> **Effectiveness:** The slow push-in during speech creates growing intimacy, a technique used in documentaries for revelation moments.

### P-071. Multi-Environment Superhero
```
Animate a superhero performing signature move across different city rooftops while
keeping costume, hairstyle, and facial features 100% consistent with @Image1. Dynamic
tracking camera follows the hero. Scene 1: Rooftop at sunset, hero lands from jump.
Scene 2: Same hero on rainy rooftop at night, lightning behind. Scene 3: Snowy rooftop
at dawn, breath visible. Same pose and power-up animation in each scene. Lock costume
colors, facial features, body proportions.
```
> **Effectiveness:** Using @Image1 to lock character appearance across different environments tests and leverages the model's multimodal coherence.

### P-072. Brand Mascot on the Go
```
Show brand mascot character interacting with three different environments without any
changes to its color palette, expression style, or movement characteristics. Scene
transitions: Park (playful wave) -> Office (helpful gesture at desk) -> Home (relaxing
on couch). Maintain exact color palette and proportions. Cheerful, consistent animation
style throughout. 15 seconds total, 5 seconds per scene.
```
> **Effectiveness:** Mascot consistency across different contexts is essential for branding, and Seedance 2.0 handles this challenge well with explicit constraints.

### P-073. Character Dialogue with Multiple References
```
Character face references @Image1, camera movement references @Video1, pacing references
@Audio1. Modern office, professional lighting with window backlight. Character speaks
naturally with realistic lip movements, making eye contact with camera. Medium shot with
push-in during key dialogue moment. Natural skin tones, no flickering, consistent
appearance throughout.
```
> **Effectiveness:** The simultaneous use of three reference types (@Image, @Video, @Audio) demonstrates Seedance 2.0's quad-modal capability.

### P-074. 19th Century London Walking Scene
```
Camera slightly pulls back and follows female lead walking on a 19th-century London
cobblestone street. She wears a long Victorian dress with bustle. A steam engine train
passes on elevated tracks behind her. Sudden wind from the train lifts her skirt
slightly, she gasps and covers it with her hands in shock. Sound effects: footsteps on
cobblestone, distant crowd chatter, steam engine whistle, fabric rustling in wind.
```
> **Effectiveness:** The interaction between character and environment (train wind -> reaction) creates a moment of emergent realism.

---

## 8. ABSTRACT / ARTISTIC

### P-075. Traversing Famous Paintings
```
The girl breaks the fourth wall, traversing multiple worlds of famous paintings. She
steps into Monet's Water Lilies (splashes through pond), emerges into Van Gogh's Starry
Night (wind swirls her hair), walks through Vermeer's room (catches the pearl earring),
slides across Hokusai's Great Wave, dances through Klimt's golden patterns, runs through
Dali's melting landscape, pauses in Munch's Scream backdrop, sits in Hopper's diner,
finally exits through Magritte's door into reality. 15 seconds, rapid transitions.
```
> **Effectiveness:** Traversing 9 iconic artworks in 15 seconds is a visual tour de force that tests the model's rapid style-switching capabilities.

### P-076. Neon Calligraphy
```
Medium shot, dark studio. A calligraphy artist sits at a backlit table with ink and
brush. Each stroke they paint glows with neon light - the wet ink luminescent. As
characters form, the light pulses and ripples. Camera slowly orbits. The completed
character radiates, casting colored shadows on the artist's face. Contrast between
traditional brush technique and futuristic glow effect.
```
> **Effectiveness:** The fusion of traditional technique (brush calligraphy) with futuristic aesthetic (neon) creates a visually mesmerizing contrast.

### P-077. Sand Animation Performance
```
Overhead locked-off shot, illuminated table surface. An artist's hands work sand into
images in continuous transformation without resets. Mountain becomes ocean becomes
city becomes forest becomes face. Each transformation flows organically into the next.
Grains of sand visible in macro detail. Warm dramatic side-lighting creates shadows
in the sand texture. Meditative pace. No cuts.
```
> **Effectiveness:** Continuous transformation without resets is key: each image flows into the next, creating a mesmerizing flow.

### P-078. Chalk Drawing Comes to Life
```
A child crouches on sunlit pavement, drawing with colorful chalk. The camera slowly
pushes in on the drawing: a flower, a butterfly, and a small house. Miyazaki-inspired
animation activates: the chalk butterfly lifts off the pavement and flutters, chalk
flower petals scatter in a drawn breeze, smoke curls from the house chimney. The child
looks up in wonder as their art comes alive. The chalk world expands beyond the
pavement edges.
```
> **Effectiveness:** The "Miyazaki-inspired" reference for chalk animation coming to life establishes a precise tone of childlike wonder.

### P-079. Abandoned Theme Park Exploration
```
A solo urban explorer walks through an abandoned theme park at dusk. Camera follows
from behind in steady tracking. Rusted carousel horses still sway slightly in the wind.
Faded paint peels from attractions. Nature reclaims: vines through roller coaster tracks,
moss on cotton candy booth. The explorer pauses at the carousel, reaches out to touch a
horse. It creaks into slow rotation. Melancholic beauty of decay meets lingering magic.
```
> **Effectiveness:** The oxymoron "melancholic beauty of decay meets lingering magic" guides the model's emotional tone in a poetic yet concrete way.

### P-080. Glassmorphic Product Reveal
```
Pure white studio environment. A perfume bottle or tech device sits centered on a
reflective surface. A frosted glass panel slowly rotates around the product, creating
refraction and distortion effects. Light passing through the glass creates rainbow
caustics on the white surface. The product is revealed in sharp focus as the glass panel
moves past. Minimal, elegant, hyper-clean aesthetic.
```
> **Effectiveness:** The glassmorphic effect (frosted glass with refraction) is a current design trend the model reproduces with premium results.

### P-081. Underwater Ballet
```
A female dancer performs underwater in a large pool lit from below. Flowing white fabric
billows around her in slow, weightless movements. She executes a graceful spin, arms
extended, creating spiraling fabric patterns. Bubbles trail from her movements. She
breaks the surface in the final second, gasping, droplets frozen in mid-air with
backlighting creating a halo effect. Ethereal, dreamlike quality.
```
> **Effectiveness:** The underwater environment eliminates gravity, allowing impossible movements on land that come across as fluid and magical.

### P-082. Fantasy Forest (Style Conversion)
```
Convert a realistic forest scene into a magical fantasy environment. Bioluminescent
plants pulse with inner light. Floating golden particles drift upward like reverse rain.
Mystical fog rolls along the ground at ankle height. Tiny fairy lights weave between
ancient trees. Studio Ghibli meets Avatar aesthetic. Soft volumetric god rays penetrate
the canopy. Color palette shifts to deep teals, warm ambers, and soft violets.
```
> **Effectiveness:** The two combined references (Ghibli + Avatar) create a unique and recognizable hybrid aesthetic.

### P-083. 1960s Vintage Film Look
```
Apply 1960s film aesthetic to modern urban footage. Kodachrome color science with warm
highlights and cool shadows. Film grain visible throughout. Occasional subtle light
leaks at frame edges. Vignette darkening corners. Faded highlights with reduced
saturation. Scratches and dust particles occasionally visible. Frame rate slightly
irregular to simulate hand-cranked projection.
```
> **Effectiveness:** The specific technical references (Kodachrome, vignetting, grain) are anchors the model interprets with high fidelity.

---

## 9. PRODUCT SHOWCASE

### P-084. 360-Degree Mechanical Keyboard Rotation
```
A minimalist black matte mechanical keyboard on a pure white infinite studio background,
rotating smoothly 360 degrees clockwise. RGB lighting gently breathing across the keys
in a rainbow wave pattern. Keycap text sharp and readable at all angles. Fixed macro
camera position, smooth turntable motion. Commercial product photography style with
soft high-key lighting. No noise, no reflections on background. Logo and text remain
perfectly consistent throughout rotation.
```
> **Effectiveness:** The "keycap text sharp and readable" specification forces the model to maintain text legibility, often problematic in AI video.

### P-085. Luxury Watch Macro
```
Close-up macro shot, smooth gimbal orbit, steady motion. A matte black luxury watch on
a velvet stand rotates slowly while soft directional light reflects off the sapphire
crystal glass. The second hand moves with visible precision. Leather strap texture
visible in detail. Camera orbits 180 degrees. Dark background with single rim light
creating dramatic edge definition. Ultra-premium product photography quality.
```
> **Effectiveness:** The gimbal orbit with a single rim light is the classic formula for luxury watch photography.

### P-086. Commercial Showcase with Multiple References
```
Perform commercial-grade camera showcase of @Image1. Side structure references @Image2.
Material detail references @Image3. Camera orbits and pushes in progressively. Premium
texture quality. 4K ultra-high definition. Stable image without distortion. Consistent
lighting from all angles. No background distractions.
```
> **Effectiveness:** Using three reference images for different aspects (shape, structure, material) produces results incredibly faithful to the actual product.

### P-087. 3-Act Product Narrative Arc
```
Three-act product story: Act 1 (Problem, 0-10s): Person struggling with messy cables,
frustrated expression, cluttered desk. Act 2 (Solution, 10-20s): Product introduction
with amazed reaction, hands unboxing the cable organizer, satisfied smile. Act 3
(Result, 20-30s): Clean desk, happy user working efficiently, product visible on desk.
Call-to-action final frame. Same person throughout with consistent wardrobe.
```
> **Effectiveness:** The problem-solution-result structure is the most effective advertising framework, executed here in short-video format.

---

## 10. ACTION / COMBAT

### P-088. Agent Close-Quarters Combat
```
A short-haired female agent in tactical winter gear engages in close-quarters combat
with a mercenary at a snowy military base. She executes a spinning heel kick, connecting
with his chest armor. Impact creates snow burst from his jacket. He staggers back.
She follows with rapid palm strikes. Camera: handheld following the action at shoulder
height, slight shake on impacts. Sound: fabric swish, impact thuds, heavy breathing
in cold air.
```
> **Effectiveness:** The physical impact details (snow burst from jacket, stagger) make the combat tangible and weighty.

### P-089. Nordic Snow Chase
```
Realistic Nordic snowy night. A man runs fast through deep snow, tracked closely from
behind at foot level. Snow explodes from each step. His breath creates thick vapor
clouds. Behind him, wolf eyes glow in the darkness, gaining. He stumbles, recovers.
Ahead, a cabin light appears. He reaches the door, slams it shut. Wolf impacts the
door from outside. Silence. Heavy breathing.
```
> **Effectiveness:** The foot-level camera during the snow run is an immersive angle that amplifies desperation and fatigue.

### P-090. Cyberpunk Assassin
```
Cyberpunk style, game CGI quality. Dark city corner. A young assassin fights multiple
enemies with a lightsaber. She teleports between opponents, leaving afterimage trails.
Each slash creates neon light arcs that linger in the air. Enemies dissolve into digital
particles. Rain falls through holographic advertisements above. Camera: dynamic tracking
with whip-pan transitions between kills.
```
> **Effectiveness:** The "afterimage trails" and digital particles leverage Seedance 2.0's VFX capabilities for effects impossible in the real world.

### P-091. Shibuya Parkour Sprint
```
Single continuous cinematic shot in Shibuya crossing. A schoolgirl sprints at extreme
speed, weaving along crosswalks and walls. She wall-runs past a vending machine, vaults
over a taxi hood, slides under a delivery truck. Camera follows in impossible tracking
shot. 8-bit game sound effects play during acrobatic moves. Shamisen music builds
throughout. Pedestrians freeze in amazement.
```
> **Effectiveness:** The mix of 8-bit sounds with traditional shamisen and the "single continuous shot" format create a unique sensory experience.

### P-092. Neon City Chase
```
High-energy cinematic chase at night in a neon-lit city. A lone character sprints
through rain-soaked streets as police drones and headlights blur past. They vault over
a market stall, slide under a closing security gate, dodge an explosion from a crashed
vehicle. Camera tracks from slightly behind and above. Reflections of neon in every
puddle. Sirens wail in the distance.
```
> **Effectiveness:** The escalating difficulty progression (vault -> slide -> dodge explosion) creates cinematic tension escalation.

### P-093. AAA Game-Style Combat
```
They meet in the dead of night and engage in a fight. The fighting style is incredibly
flashy, the atmosphere is tense and exciting. Unreal Engine 5 visual quality. Cinematic
camera with dramatic slow-motion on key hits. Particle effects on impacts. Volumetric
fog illuminated by moonlight. Character faces remain detailed and consistent. Motion
blur on fast movements, sharp on pauses.
```
> **Effectiveness:** The "Unreal Engine 5" reference is a powerful quality anchor for action scenes with AAA game quality.

### P-094. Mirror Breakdown Scene
```
The woman walks up to a mirror and looks at her reflection. Her expression slowly shifts
from composed to anguished. She screams, slamming both fists against the mirror. Cracks
spider-web across the glass. Her reflection fragments into dozens of pieces, each
showing a different emotion. Camera pushes in aggressively during the scream. Sound
builds from silence to overwhelming.
```
> **Effectiveness:** Mirror fragmentation with different emotions in each fragment is a powerful visual narrative device.

### P-095. Tactical Battlefield Action
```
The man from reference image 1 as the protagonist, agile and athletic, running through
a battlefield. He dodges behind concrete barriers as explosions erupt nearby. Muzzle
flashes strobe from unseen positions. He sprints across open ground, slides into cover.
Debris rains down. Camera: low angle tracking beside him, shaking with each explosion.
Dust and smoke obscure then reveal the action.
```
> **Effectiveness:** Using the reference image for the protagonist ensures recognizability during chaotic scenes with explosions and debris.

### P-096. Wuxia Duel
```
An Eastern Wuxia-style duel between a grandmaster in white and a grandmaster in black
on a mountain peak above the clouds. Energy orbs form around each fighter. They clash
mid-air with martial arts strikes. Each impact creates shockwaves that disperse clouds.
The platform beneath them begins to collapse. Final move: both energy orbs merge and
explode, creating a pillar of light visible from the ground.
```
> **Effectiveness:** Wuxia genre conventions (aerial combat, qi energy, mountains in the clouds) are well understood by the model.

### P-097. Epic Martial Arts Duel
```
A white-clad swordsman faces a straw-cloaked swordsman in a bamboo forest under heavy
rain. They stand motionless for 3 seconds. Lightning flash. They charge simultaneously.
Slow-motion weapon clash creates a shockwave that shatters bamboo stalks in all
directions. Water droplets frozen in air by the force. Camera orbits the impact point
at 180 degrees. Steel ring reverberates.
```
> **Effectiveness:** The moment of stillness before the clash (3 seconds motionless) and the slow-motion impact are the signature of wuxia cinema.

### P-098. Explosive Escape
```
Tactical soldier through burning industrial zone. 0-4s: Cautious advance scanning
threats with weapon raised, red emergency lights flash. 4-8s: Lateral explosion rocks
the frame, soldier ducks instinctively, debris flies past camera. 8-12s: Slow-motion
run through wall of fire, embers trailing from tactical vest. 12-15s: Emerges outside,
collapses to one knee, exhales relief. Sound: ringing ears transitioning to muffled
real-world sounds.
```
> **Effectiveness:** The audio transition "ringing ears to muffled sounds" adds post-explosion realism that few generators handle well.

### P-099. Cyberpunk City Chase
```
Character with minor injuries runs through rainy neon streets. 0-4s: Wide tracking shot,
realistic puddle splashes reflect neon signs with each footstep. 4-9s: Slow-motion leap
over crashed vehicle, mechanical sparks from cybernetic arm activating. 9-13s: Sharp
turn into alley, camera whip-pans to follow. 13-15s: Stops, looks back with heavy
breathing, rain streaming down face. Neon illumination as only light source.
```
> **Effectiveness:** The "realistic puddle splashes reflecting neon" are a detail that enormously elevates the perceived quality of the scene.

### P-100. Forest Swordsmen Duel
```
Two warriors face each other in a forest clearing at dawn. 0-5s: Static medium shot,
tension building, leaves fall slowly between them. 5-10s: Rapid clashing of swords with
realistic sparks and steel sounds, camera follows the action. 10-15s: Camera slowly
circles the victor as the defeated opponent falls. Metal impacts, realistic blood
trajectories, leaf dynamics disturbed by the combat. Morning mist parts around their
movements.
```
> **Effectiveness:** The morning mist parting around movements is a physical detail that adds credibility to the scene.

### P-101. Futuristic Hand-to-Hand Combat
```
Two warriors in a high-tech arena with energy barriers. 0-5s: Standoff, energy charges
visible around their fists and forearms. 5-10s: High-speed exchange of blows with
electric arcs at each contact point. 10-15s: Slow-motion knockout punch, energy
discharge creates expanding sphere of light. Loser crashes through energy barrier.
Blue-purple lighting, sci-fi particle effects trail every movement.
```
> **Effectiveness:** The "electric arcs at each contact point" and the final slow-motion with an energy sphere create a spectacular visual climax.

### P-102. Bollywood-Style Kite Action
```
A Chinese youth flies a kite through crowded market streets. He leaps up stone steps,
flips over a food cart without releasing the string, lands running, dashes between
rickshaws. The kite performs impossible aerial maneuvers synchronized with his ground
parkour. Camera follows in continuous tracking shot. Style transitions mid-sequence from
realistic to slightly anime-influenced during the acrobatic peak. Upbeat traditional
instrument soundtrack.
```
> **Effectiveness:** The kite-acrobat synchronization and mid-sequence style transition test the model's advanced capabilities.

### P-103. Flower Offering on Horseback
```
A man in orange traditional robes rides a brown horse toward a massive tree blooming
with orange flowers. Classical Chinese aesthetic with shadow puppet influence. Color
palette restricted to black, white, and orange. He dismounts, picks a branch of flowers,
offers it upward as petals scatter. Camera follows from a respectful distance, low
angle. Ink wash transitions between shots.
```
> **Effectiveness:** The limited palette (black, white, orange) is a creative constraint that produces visually coherent and stylistically strong results.

### P-104. Boxing Gym Combat Scene
```
Gritty boxing gym, heavy bag era. Two fighters spar in a worn ring with ropes. Handheld
camera circles the ring at eye level. Sweat sprays from impact. Coach shouts instructions
from corner. Close-up on wrapped fists connecting with body. Consistent character
identity maintained through 10-second sequence. Fluorescent overhead lighting with dust
particles. Sound: leather on skin, exhaled grunts, skipping rope in background.
```
> **Effectiveness:** The circular eye-level camera immerses the viewer in the ring, a technique used in classic boxing films.

### P-105. Indian Action Blockbuster
```
Telugu action style with anti-gravity physics. Hero entrance: slow-motion walk through
explosion with debris suspended in air. Crowd combat: hero simultaneously fights 20
opponents using increasingly impossible techniques - a kicked enemy flies backward
through three walls. Vehicle destruction: hero stops a speeding truck with one hand,
it crumples like paper. Exaggerated impact effects with dramatic camera zooms on every
hit. Over-the-top heroic music swells.
```
> **Effectiveness:** Tollywood style with anti-gravity physics is a recognizable genre the model interprets with enthusiasm.

---

## 11. FANTASY / SCI-FI

### P-106. Magical Library
```
A young mage enters a colossal, enchanted library stretching upward into infinity.
Floating books drift between shelves of their own accord. Levitating tomes open,
releasing streams of golden text that swirl in the air. The mage reaches out and a
specific book flies to her hand, opening to reveal a glowing map. Dust motes sparkle
in shafts of light from impossible windows. Camera cranes upward to reveal the
infinite scale.
```
> **Effectiveness:** The upward crane revealing infinite scale is an epic technique for communicating grandeur in fantasy environments.

### P-107. Cyberpunk Rooftop Showdown
```
Two augmented warriors face off on a neon-lit rooftop in a cyberpunk city during heavy
rain. Cybernetic implants glow through their skin. Energy weapons charge with visible
electrical build-up. They clash, energy blades creating lightning arcs against the rain.
The impact shatters rooftop tiles and sends shockwaves rippling through rain puddles.
Camera orbits the fighters during the clash. City hologram advertisements flicker
in the background.
```
> **Effectiveness:** Rain as an element interacting with energy weapons (electrical arcs in the rain) adds an impressive physical layer.

### P-108. Giant Mech vs Dragon
```
A towering mech engages in battle with a massive dragon atop a crumbling city. The
dragon breathes white-hot fire that melts building facades. The mech blocks with an
energy shield, slides back from the force. Counter-attack: mech's chest opens, firing
a concentrated energy beam. Dragon banks left, beam slices through a skyscraper behind
it. Camera: wide shot establishing scale, then close combat cuts. Debris rains
constantly.
```
> **Effectiveness:** The attack-defense-counterattack dynamic with collateral damage (sliced skyscraper) creates readable and epic battle choreography.

### P-109. Post-Apocalyptic City
```
A lone survivor sprints through a crumbling cityscape overgrown with vegetation. Vines
cover rusted vehicles. A pack of mutant creatures emerges from a collapsed subway
entrance. The survivor vaults through a broken window, rolls, keeps running. Falling
debris from a collapsing overpass forces a direction change. Camera: chase perspective
from slightly above and behind. Neon emergency signs flicker on dead buildings.
```
> **Effectiveness:** The post-apocalyptic environment with vegetation reclaiming control creates a fascinating visual contrast between nature and urban ruin.

### P-110. Samurai at Dawn
```
Two samurai face each other at the crest of a misty mountain at dawn. Cherry blossom
petals drift between them. Neither moves for 3 seconds of excruciating tension. A petal
touches the ground. Both draw simultaneously in iaijutsu flash-draw. The camera captures
the crossing of blades in extreme slow motion - every water droplet from the misty air
vibrates from the impact shockwave. One samurai sheathes his sword. The other falls.
```
> **Effectiveness:** The iaijutsu (lightning draw) with a visual trigger (petal touching the ground) is the quintessence of cinematic samurai aesthetics.

### P-111. Lonely Robot - Multi-Shot Storytelling
```
A lonely robot wakes up in an abandoned factory (Scene 1: Rust particles fall as it
powers on, single eye flickers blue). It walks outside and sees a sunset wasteland
(Scene 2: Wide shot, tiny robot silhouette against vast orange sky). It discovers a
small green flower growing through concrete (Scene 3: Macro close-up, robot's metal
finger gently touches a petal). Finally, it looks up at the sky and its eye-light forms
a smile shape (Scene 4: Medium shot, warm tones). Emotional transition from confusion
to warmth. Cinematic camera, no flicker.
```
> **Effectiveness:** The robot's emotional arc (confusion -> discovery -> tenderness) creates empathy with a non-human subject, a supremely powerful narrative technique.

### P-112. Butterfly Fairy Tale
```
A magical artifact: a painted butterfly on an ancient wall begins to twitch. Its wings
peel away from the fresco surface, gaining dimension and color. It flies out of the
painting into a sunlit room, casting a realistic shadow. It circles the room, lands on
a child's outstretched finger. The child laughs. The butterfly senses footsteps
approaching, returns to the wall, and becomes flat paint again. Camera follows the
butterfly throughout in continuous tracking.
```
> **Effectiveness:** The 2D-painting-to-3D-real and back transition is a fascinating effect that leverages Seedance 2.0's capabilities.

---

## 12. FOOD / ASMR / SENSORY

### P-113. ASMR Skincare Macro
```
Create a vertical ASMR video with no music, focusing on macro details. A light blue
skincare gel bottle sits on a frosted glass surface. Hands with manicured nails slowly
twist open the cap. Camera pushes into extreme macro as gel is squeezed onto fingertips.
The gel glistens, catching light in slow motion. Fingers spread the gel, emphasizing
texture and friction sounds. The tactile quality of the product dominates the frame.
No background noise, only product sounds amplified.
```
> **Effectiveness:** The absence of music and the amplification of product sounds (opening, gel, friction) create a pure ASMR experience.

### P-114. POV Hands ASMR
```
A first-person ASMR video featuring hands. Close-up shots show a pair of slender hands
performing a sequence: scratching a textured wooden surface (visible scratch marks form),
rubbing velvet fabric (pile shifts direction), tapping glass with each fingernail in
sequence (visible vibration rings). Each action 3-4 seconds. Camera locked in extreme
close-up. Sound: amplified scratching, soft rubbing, crystalline tapping. No music.
```
> **Effectiveness:** The sequence of different materials (wood -> velvet -> glass) creates sensory variety while maintaining the ASMR format.

### P-115. Miniature Cooking
```
A miniature cooking video on a pure black background with dramatic top lighting. Tiny
real ingredients: crack a quail egg into a miniature pan (visible sizzle), flip with
tiny spatula, garnish with micro-herbs using tweezers. The finished miniature dish is
plated on a coin-sized plate. A full-sized finger enters frame for scale reference.
Camera: overhead macro, slight push-in for plating. Sound: amplified sizzle, scrape,
and sizzle of miniature cooking.
```
> **Effectiveness:** The scale contrast (miniature cooking + finger for reference) creates an extremely popular viral visual effect.

### P-116. Sizzling Wagyu Steak
```
Close-up of a wagyu steak hitting a hot cast-iron skillet. Fat renders instantly,
creating a cascade of sizzling sounds. Maillard reaction visible in real-time as the
surface browns. Butter basted with rosemary sprig - herb sizzles on contact. 2K
resolution, shallow depth of field. Steam and smoke rise. Juices pool and bubble.
Camera: locked macro, slight rack focus from surface detail to overall steak.
Final: meat thermometer inserted, reads 54 degrees C.
```
> **Effectiveness:** The culinary technical terms (Maillard reaction, butter basting) guide the model toward specific and realistic details.

### P-117. Night Market Street Food
```
Handheld camera weaves through a crowded Southeast Asian night market at eye level.
Steam rises from multiple food stalls. Close-up: vendor's hands expertly fold a roti,
oil splatters in a wok, skewers turn on a grill. A couple shares noodles from a single
bowl, laughing. Camera transitions from documentary observation to intimate close-ups
of food textures. Warm tungsten lighting mixes with colored stall lights. Ambient:
sizzling, chatter, distant music, motorcycle passing.
```
> **Effectiveness:** Transitioning from documentary observation to intimate close-ups creates a visual rhythm that replicates the experience of walking through the market.

### P-118. Whisky Macro Pour
```
Extreme macro commercial shot. A crystal whisky glass sits on a dark, textured oak
surface. Amber liquid pours in slow motion, creating thick legs on the glass interior.
A single large ice sphere cracks audibly as the whisky contacts it. Surface tension
creates a perfect meniscus. Light passes through the liquid creating warm caustic
patterns on the dark surface. Camera: locked extreme macro with slight rack focus from
ice to liquid surface. Sound: pour, ice crack, settling liquid.
```
> **Effectiveness:** The detail "ice sphere cracks audibly as whisky contacts it" is a premium ASMR moment that elevates the spot from commercial to sensory.

### P-119. Japanese Sushi
```
Sushi spread on a polished wooden tray with miso soup steaming gently. 0-4s: Overhead
wide shot, a hand adjusts chopsticks with precise etiquette. 4-8s: Chopsticks pick up
a single piece of nigiri, pause mid-air showing rice grain detail. 8-12s: Gentle soy
sauce dip creating expanding ripples in the small dish. 12-15s: Chopsticks exit frame,
steam continues rising from miso soup. Warm natural light, traditional Japanese
restaurant ambiance.
```
> **Effectiveness:** Attention to etiquette (chopstick adjustment) and detail (visible rice grains) communicate culinary respect and premium quality.

---

## 13. MUSIC / DANCE

### P-120. Latin Dance
```
Couple performing Latin dance in tropical night setting. She wears a flowing red dress,
he wears a fitted black shirt. 0-5s: Close embrace, slow spinning together at intimate
tempo. 5-10s: Tempo increases, fast spins with her dress creating circular patterns,
dramatic leg lift and hold. 10-13s: Crossed-step footwork sequence, camera follows
feet. 13-15s: Final pose in close embrace, heavy breathing, slight smiles. Warm string
lights in background, live band barely visible.
```
> **Effectiveness:** The intensity progression (slow -> fast -> finale) with shifting focus (body -> feet -> faces) creates a complete mini-performance.

### P-121. Neon Street Dance
```
Character in black hoodie and sneakers on rainy neon-lit street. 0-3s: Warm-up
shoulder rolls and neck stretches, casual attitude. 3-7s: Explosive footwork and
vertical jumps, puddle splashes with each landing. 7-10s: Fast spin with arms extended,
water droplets creating a spiral pattern. 10-15s: Freeze pose on beat drop, held for
2 seconds, rain continues around motionless body. Camera: handheld tracking to whip
pan to slow push-in for freeze. Bass-heavy electronic music.
```
> **Effectiveness:** The final freeze in the rain with the motionless body while drops continue to fall creates an iconic image.

### P-122. Cyber Electronic Dance
```
Dancer in glowing bodysuit in abstract cyberspace environment. 0-4s: Light floating
movements, body undulates like waves of data. 4-8s: Popping and locking moves, each pop
creates ripple effects in the digital environment. 8-12s: Acrobatic jump with
mid-air split, environment distorts around them. 12-15s: Suspended in mid-air during
beat drop, environment freezes, only light particles continue moving. Neon lights
pulse with music rhythm throughout.
```
> **Effectiveness:** The dancer-environment interaction (each pop creates effects) merges performer and space into an integrated visual experience.

### P-123. 1920s Jazz Club Charleston
```
Create a Charleston dance sequence in a 1920s jazz club style. A female dancer in a
gold-fringed flapper dress, sequined headband, and T-strap heels. She performs rapid
kick-steps, knee-swings, and arm swings on a polished wooden dance floor. Brass band
visible in background. Camera dynamically tracks her movement, low angle captures the
leg work, then rises to capture full body energy. Art deco interior, warm amber
spotlights, cigarette smoke haze.
```
> **Effectiveness:** The costume details (fringed dress, T-strap heels) and specific steps (kick-steps, knee-swings) create historical authenticity.

### P-124. K-Pop Music Video
```
Epic K-pop concert scene. Dramatic stage with programmed LED walls, moving platforms,
and pyrotechnic effects. A group of 4 dancers performs synchronized choreography on
the main stage. Camera: crane shot descending from above, transitions to tracking shot
along the stage edge. Audience ocean of light sticks. Confetti cannons fire on the
chorus. Costumes with holographic fabric catch stage lights. High energy throughout.
```
> **Effectiveness:** The descending crane shot revealing the stage scale is a technique used in real K-pop productions.

### P-125. Girl Dance with Future House
```
Beautiful girl with black wavy hair, pink crop top and yoga pants, dancing to Future
House DJ music with hip movements synchronized to beats. Camera follows music rhythm
with push-pull movements creating a pulsing visual effect. Bedroom setting with soft
colored spotlights. 9:16 aspect ratio. Natural, confident movements. Slight smile.
Hair bounces with each move.
```
> **Effectiveness:** The camera-music synchronization (push-pull on beats) creates a rhythmic visual effect that amplifies the dance energy.

### P-126. Victory Dance with JK Skirt
```
Girl in white crop top and JK plaid skirt dancing to upbeat DJ track. Specific
movements: victory hand signs, playful hair flips, spinning with skirt flair. Bedroom
background with warm soft lighting and fairy lights. 9:16 vertical ratio, 10-second
duration. Cheerful, youthful energy. Clean makeup, natural expression.
```
> **Effectiveness:** The "JK" (Japanese school) style with specific movements (victory signs, hair flips) is a massively viral format on Asian platforms.

### P-127. Behind-the-Scenes Ballet Rehearsal
```
Documentary-style footage inside a ballet rehearsal studio. Natural daylight through
high windows creates long shadows on wooden floor. A principal dancer marks a routine,
then runs it full out. Sweat visible on brow. Feet pound the floor, pointe shoes
scrape. Mirror reflects the movement. Camera: observational, slightly distant, then
push-in during the climax of the routine. Sound: breathing, feet, floor creaks,
distant piano from another studio.
```
> **Effectiveness:** The observational documentary style with real ambient sounds (creaks, distant piano) creates authenticity and intimacy.

---

## 14. COMEDY / MEME

### P-128. Avengers Alternate Scene
```
Avengers Endgame big fight scene, cinematic style. Thanos suddenly freezes the battle
with the Time Stone. All heroes stuck mid-action. Thanos casually walks through the
frozen battlefield, adjusts Captain America's shield angle, moves Thor's hammer slightly
to the left, pats Spider-Man on the head. Resumes time. Everyone confused as their
attacks miss completely. Thanos sits on a rock and watches, amused.
```
> **Effectiveness:** The subversion of expectation (comedic villain instead of threatening) in a well-known epic scene creates humor through tonal contrast.

### P-129. Otter Pilot Documentary
```
A nature documentary scene showing an otter piloting a small propeller airplane. The
otter wears tiny aviator goggles and a leather flight cap. It adjusts miniature
instruments with webbed paws. Camera: cockpit interior shot, then external tracking
as the tiny plane flies over a river. David Attenborough-style narration tone. The
otter does a barrel roll, looks at camera with an expression of pure joy. Documentary
title card appears: "Wings Over Water: An Unexpected Journey."
```
> **Effectiveness:** The "serious documentary on an absurd subject" format is one of the most effective comedic formats achievable with AI.

### P-130. Friends x Game of Thrones
```
The cast of Friends reimagined in a Game of Thrones-style sitcom. Ross as a nervous
Maester, Rachel as a fashionable noble, Joey as a dimwitted knight, Chandler making
sarcastic quips in a castle great hall. Monica obsessively cleaning a medieval kitchen.
Phoebe reading runes. They sit on iron thrones instead of the coffee shop couch.
Laugh track plays after each medieval mishap. Camera: multi-cam sitcom setup.
```
> **Effectiveness:** The mashup of two iconic franchises with precise character mapping (Joey = dimwitted knight) creates comedy for fans of both series.

### P-131. Bollywood Distracted Boyfriend Meme
```
Bollywood-style recreation of the distracted boyfriend meme. The boyfriend character
performs an elaborate dance number with the "other woman" while the girlfriend character
does a dramatic Bollywood gasp with 5 camera angles. Entire street joins the dance.
Rain machine activates. Color powder thrown. Slow-motion slap sequence with 12 reaction
shots. The boyfriend snaps back to reality, girlfriend is staring daggers. Musical
score swells and cuts.
```
> **Effectiveness:** The Bollywood exaggeration of the meme with 12 reaction angles is a parody that amplifies the absurdity of the original format.

### P-132. Narrative Cat Drama
```
Cat drama narrative spanning 15 seconds. Scene 1: White cat sits in rain at window,
sees its partner cat with another cat through the glass. Dramatic zoom on betrayed
expression. Scene 2: Revenge transformation montage - white cat gets a makeover, learns
to play piano, becomes successful. Scene 3: Grand ballroom, white cat in elegant outfit
confronts the cheating cat. Dramatic slap with slow motion paw. White cat exits
victoriously through double doors. Korean drama OST swells.
```
> **Effectiveness:** The K-drama parody with cats as actors is a format that combines the appeal of cats with drama narrative structure, generating maximum shareability.

### P-133. Mona Lisa Steals the Cola
```
The Mona Lisa painting comes to life. She looks left and right nervously, then her
hand reaches out of the painting frame. She grabs a Coca-Cola bottle from a museum
display nearby. Drinks it with exaggerated satisfaction, hides the bottle behind the
frame. A cowboy from a painting next door snatches the bottle. Spotlight hits the Coke
for final hero shot. Museum guard walks past oblivious.
```
> **Effectiveness:** Anthropomorphizing famous paintings that interact with modern products is a viral creative advertising concept.

---

## 15. HORROR / SUSPENSE

### P-134. Reflection Anomaly (15s Horror Template)
```
Bathroom mirror glitch narrative. Person enters bathroom, turns on light. 0-3s: Normal
reflection, brushes hair. 3-7s: Person pauses, reflection continues brushing with 0.5
second latency - movement desynchronized. 7-11s: Person slowly raises right hand.
Reflection raises left hand, then slowly turns its head independently while the real
person remains still. 11-15s: Person bolts, slams door. Final frame: reflection is
still standing there, looking at where the person was, then slowly turns toward the
camera. Black screen.
```
> **Effectiveness:** The progressive reflection desync (delay -> autonomy -> confrontation) builds escalating horror without gore effects.

### P-135. Amusement Park Urban Exploration
```
A solo urban explorer enters an abandoned amusement park at twilight. Security fence
cut. Flashlight beam reveals faded clown faces on the funhouse. A Ferris wheel car
creaks and sways with no wind. Camera: POV handheld, flashlight is the only light
source. Sound: metal groaning, distant calliope music that shouldn't be playing. The
explorer turns a corner, flashlight illuminates fresh footprints in the dust leading
ahead. They weren't there before.
```
> **Effectiveness:** The "fresh footprints in the dust" as the final reveal is a minimal yet terrifying horror detail.

---

## 16. SPORTS / RACING

### P-136. Pairs Figure Skating
```
A live performance of competitive pairs figure skating. A low-angle camera follows the
skaters as they glide across the ice in perfect synchronization. The female skater is
lifted overhead in a one-arm hold, spinning. Ice shavings spray from sharp stops. Camera
adjusts to capture the technical elements: footwork sequences, throw jumps, death
spiral. Crowd gasps and applauds. Arena lighting creates dramatic shadows on the ice.
```
> **Effectiveness:** The figure skating technical terms (death spiral, throw jump) guide the model toward specific, recognizable movements.

### P-137. Le Mans-Style Hollywood Race
```
Structured 15-second racing sequence, Le Mans style. Interior cockpit shots with rain
hammering the windshield. Driver shouts "Let's go!" gripping the wheel. Exterior:
water spray creates rooster tail behind the car. Motion blur on background, car sharp.
Stadium lighting streaks across wet bodywork. Tire smoke mixes with rain mist. Engine
roar builds to redline. Final shot: car crosses finish line under checkered flag,
brake lights glow through spray cloud.
```
> **Effectiveness:** The combination of interior/exterior shots with driver dialogue creates a complete and engaging mini racing film.

### P-138. Realistic Athlete Sprint
```
Athletic sprinter in tracksuit with rapid powerful leg movements and pumping arms,
sprinting down a red track toward camera. Crosses finish line as crowd erupts. Tracking
shot follows runner from side angle, maintaining focus on face showing maximum effort.
24fps cinematic sports documentary style. Shallow depth of field blurs the stadium.
Sweat and breath vapor visible. Sound: feet pounding track, crowd roar building.
```
> **Effectiveness:** The 24fps and sports documentary style with shallow depth of field create the aesthetic of professional sports documentaries.

---

## 17. INTIMATE MOMENTS / SLICE OF LIFE

### P-139. Rainy Night Convenience Store
```
Single continuous shot. A young woman in an oversized hoodie pushes open a convenience
store door, bell jingles. She walks past fluorescent-lit aisles, picks up instant
noodles, pauses. Puts them back. Picks up a fresh bento instead. Pays at the counter,
the clerk nods without speaking. She exits into rain, pauses under the awning to open
the bento, takes one bite. Her expression softens from exhaustion to small comfort.
Camera: follows from behind, then orbits to face her for the final moment.
```
> **Effectiveness:** The instant-noodle-vs-bento choice is a narrative micro-moment that communicates "choosing to take care of yourself."

### P-140. Rooftop Yoga at Dawn
```
A woman practices yoga alone on a high rooftop at sunrise. City skyline silhouette in
background. She flows through sun salutation: mountain pose, forward fold, plank,
upward dog, downward dog. Each pose held for a breath. Camera: wide establishing shot,
then slow arc to capture both her and the rising sun. Golden light gradually warms the
scene. Wind moves her clothes and hair. Sound: distant city awakening, her steady
breathing.
```
> **Effectiveness:** The real sun salutation progression with named poses guides the model through a fluid and anatomically correct sequence.

### P-141. Late Night Ramen Shop
```
Single continuous Steadicam shot. A ramen shop at 1am, near empty. Steam rising from
a single bowl on the counter. A tired salaryman in a wrinkled suit sits down. The cook
silently places the bowl in front of him. He breaks apart chopsticks, pauses. Takes
first sip of broth. Closes eyes. His shoulders drop as tension leaves his body. Camera:
slow approach from door, settles at counter-level beside him. Warm yellow lighting,
wood textures, condensation on windows.
```
> **Effectiveness:** The "shoulders drop as tension leaves" moment is the central emotional beat: a small gesture that tells an entire day's story.

### P-142. Rainy Day at Home
```
20-year-old in oversized knit sweater curled on a couch with a book. 0-5s: Wide shot
of cozy living room, rain streaks on the window behind her, warm lamp light. 5-10s:
Camera pushes to medium shot, she turns a page, lips move slightly as she reads.
10-15s: Close-up of rain on window pane, steam rises from a cocoa mug on the side
table, her hand reaches for it. The sound of rain dominates. No music. Healing
atmosphere.
```
> **Effectiveness:** The absence of music, leaving only the sound of rain, is an aesthetic choice of the "healing" genre that the model faithfully respects.

### P-143. Japanese Healing Aesthetic
```
A young woman stands under a cherry blossom tree in full bloom. Gentle breeze blowing
through her long hair. She slowly looks up at the falling petals, catching one in her
cupped hands. Medium shot slowly pushing in to face close-up. Her eyes reflect the
pink petals. She smiles softly. Soft natural lighting with golden hour warmth. Light
film grain. No music, only wind and distant temple bell.
```
> **Effectiveness:** The "Japanese healing" aesthetic with cherry blossoms, temple bell, and film grain is a specific sub-genre the model handles perfectly.

### P-144. Elderly Craftsman's Hands
```
Close-up, intimate documentary-style footage. An elderly craftsman's hands work clay
on a pottery wheel. Veins and wrinkles visible in detail. His fingers shape the wet
clay with practiced precision. Water drips. The vessel takes form slowly. Camera never
shows his face, only the hands and the emerging creation. Warm natural side-light from
a workshop window. Sound: wet clay spinning, occasional satisfied hum.
```
> **Effectiveness:** The choice to never show the face, only the hands, is a powerful directorial decision that universalizes the subject.

### P-145. Emotional Airport Reunion
```
Airport reunion scene. Shot 1: Child waiting anxiously by arrivals gate, holding a
hand-drawn welcome sign, bouncing on heels. Wide shot of busy terminal. Shot 2:
Parent appears through sliding doors, freeze moment of recognition, both faces light
up. Shot 3: Slow-motion run toward each other, child drops sign. Shot 4: Embrace,
camera circles them, close-up on parent's closed eyes and tears. Swelling emotional
music synchronized with visual beats.
```
> **Effectiveness:** The "freeze moment of recognition" before the slow-motion run is a classic cinematic emotional technique.

---

## 18. MULTI-SHOT STORYTELLING

### P-146. Multi-Camera Chase Sequence
```
Multi-camera chase through busy city streets. Shot 1: Wide establishing shot, target
spotted crossing intersection. Shot 2: Close-up on pursuer's determined face, starts
running. Shot 3: POV shot weaving through pedestrian crowd, people reacting. Shot 4:
Aerial drone view showing the gap closing between pursuer and target. Character
consistency maintained throughout all shots. Spatial continuity preserved. Escalating
tension in each subsequent shot. Urban daytime setting.
```
> **Effectiveness:** The perspective progression (wide -> close -> POV -> aerial) and spatial coherence between shots create a believable cinematic chase.

### P-147. Lord of the Rings Epic
```
Fellowship descending from snow-covered mountain pass, cloaks whipping in blizzard.
Transition to: Moria battle sequence, Gandalf faces goblins with staff glowing white,
creating shockwave that throws back attackers. Climax: Balrog bridge confrontation,
Gandalf slams staff on stone bridge with iconic pose. Freeze frame as bridge cracks.
Camera zooms out to reveal the massive scale of the underground chasm. Epic orchestral
score throughout.
```
> **Effectiveness:** The three-iconic-scene structure with bridge climax and freeze frame creates a recognizable cinematic tribute.

### P-148. Paladin in the Cathedral
```
Character in silver paladin armor fighting 20+ cultists in a gothic cathedral during a
twilight storm. Nine-panel sequence: Panel 1: Crane descends through stained glass
ceiling. Panel 2: Paladin enters through massive doors, lightning behind. Panel 3:
Cultists turn, weapons drawn. Panel 4: First clash, holy light erupts from paladin's
sword. Panel 5: Wide shot of melee. Panel 6: Paladin disarms three opponents
simultaneously. Panel 7: Boss cultist appears. Panel 8: Final duel close-up. Panel 9:
Paladin silhouette in doorway, cathedral burning behind.
```
> **Effectiveness:** The 9-panel grid is a storyboard structure that guides the model through a complex and detailed narrative progression.

### P-149. Two Lovers Confrontation in Red
```
Period drama face-off at cliff edge. Shot 1: Woman in red lifts wine jug, drinks
defiantly. Orbiting camera moves to her back, then focus-shifts to reveal a woman in
black in the distance. Shot 2: Drone aerial wide shot reveals the full cliff landscape
with both figures. Shot 3: Close-up two-shot, intense staring confrontation, wind
moves hair and robes. Classical Chinese aesthetic with muted warm palette.
```
> **Effectiveness:** The perspective change (close-up -> drone -> two-shot) with focus-shift as transition is an elegant directorial technique.

### P-150. Complete Multimodal Video Duel
```
Reference @Video1 for character actions and camera work. Generate @Image1 black-robed
character throwing a flying dagger in a bamboo forest. Starting angle and framing
strictly reference @Video1. After the dagger is thrown, switch to slow-motion tracking
the dagger in focus, with the black-robed character blurred in background. Bamboo
stalks split as dagger passes. Sound: whoosh, bamboo cracking, wind.
```
> **Effectiveness:** The simultaneous use of video and image references with precise focus-shift instructions demonstrates the full multimodal potential.

---

## 19. AUDIO / LIP-SYNC

### P-151. Multilingual Business Dialogue
```
Business meeting with three languages. English speaker presents quarterly results at
head of table. Mandarin-speaking colleague responds with observations. Japanese
participant adds perspective. Phoneme-level lip-sync accuracy for each language. Modern
glass conference room with city view. Professional three-point lighting. Medium shot
with subtle push-in during key statements. Synchronized with @Audio1 timing. Natural
hand gestures appropriate to each cultural context.
```
> **Effectiveness:** The "phoneme-level accuracy" specification for three different languages tests Seedance 2.0's multilingual lip-sync capabilities.

### P-152. Music Video Sync
```
Create video using @Image1 as character reference. Natural head, eye, and subtle ear
movements. Sync facial expressions with playful music rhythm from @Audio1. Subtle body
movements hit the musical beats - head nods on downbeats, shoulders pulse on upbeats.
Match the emotional tone of the music, transitioning from chill to energetic. Dynamic
camera moves synchronized with musical intensity: slow during verse, active during chorus.
```
> **Effectiveness:** The differentiation "head nods on downbeats, shoulders on upbeats" guides sophisticated musical synchronization.

### P-153. Sound Effects Integration
```
A wine glass sits on a marble table edge. 0-3s: Tense silence, glass vibrates slightly
from distant footsteps. 3-6s: Glass slides imperceptibly toward edge. 6-9s: Falls in
extreme slow motion, rotating, catching light. 9-12s: Impact with floor. Dual-branch
audio: Build-up of tense silence, then crisp shatter sound perfectly synced to impact
frame. 12-15s: Tinkling aftermath as shards settle, one piece spins to a stop. High-
speed macro camera with focus pull from glass to impact point to settling shards.
```
> **Effectiveness:** The "dual-branch" audio description with build-up and release perfectly synchronized to visual impact creates sensory cinema.

---

## 20. STYLE TRANSFER / VFX

### P-154. Cyberpunk Transformation
```
Transform daytime city street footage into neon-illuminated cyberpunk environment.
Reference @Video1 for source footage. Day transforms to night, natural light becomes
neon. Rain appears on dry surfaces. Holographic signs replace real signs. Vehicles gain
neon underglow. Puddles appear reflecting the new neon world. High contrast teal and
orange neon color grade. Maintain original camera movement and composition.
```
> **Effectiveness:** The day-to-cyberpunk-night transformation with progressive element addition (rain, holograms, reflections) is a WOW effect.

### P-155. Anime Style Conversion
```
Transform realistic footage into anime style while maintaining original motion and
composition. Reference @Video1 for source, @Image1 for anime style guide. Apply
cel-shading with bold outlines. Stylize expressions. Vibrant anime color palette with
clean gradients. Hair and clothing gain anime physics - slightly exaggerated motion.
Background simplifies to painted anime environments. Maintain character proportions
and movement timing from original footage.
```
> **Effectiveness:** The realism-to-anime conversion while preserving original motion and composition is one of Seedance 2.0's most requested applications.

### P-156. Vintage Film Look
```
Apply 1960s film aesthetic to modern footage. Kodachrome color science: warm highlights,
cool shadows. Visible film grain throughout. Occasional subtle light leaks at frame
edges. Vignette darkens corners. Faded highlights with reduced saturation. Hairline
scratches and dust particles occasionally visible. Frame rate slightly irregular to
simulate hand-cranked projection. Maintain original movement and composition.
```
> **Effectiveness:** The multiple technical references (Kodachrome, vignette, grain, light leaks) work in synergy to create a believable film look.

### P-157. Video Outfit Transformation
```
Girl in cozy house applies paint to her hands. Words appear on screen: "gray," "lake
blue," "silver-blue." She mixes the colors. Quick transition: costume transforms from
casual wear to elegant Hanfu with silver jewelry. She uses a folding fan to reveal her
face. Rembrandt lighting with visible god rays. Color palette shifts from muted to
rich. Maintain face consistency throughout transformation. Cinematic slow motion on
the fan reveal.
```
> **Effectiveness:** The outfit transformation with a "visual trigger" (fan revealing the face) is a viral format on Douyin/TikTok.

### P-158. Ultra-HD Pure Desire Style Transformation
```
Ultra-high definition pure-desire style girl transformation video. Cinematic soft focus
opening. Clean makeup, fair complexion, bedroom setting with warm yellow lighting.
Lazy-casual styling transitioning to refined goddess look. Detailed accessories appear:
earrings, necklace, styled hair. Each transformation beat synced to music. Shallow depth
of field throughout. No blur, no ghosting, no facial distortion. Skin texture
maintained naturally.
```
> **Effectiveness:** The "pure desire" style is a specific Chinese viral aesthetic that the model knows and faithfully interprets.

---

## 21. APPENDIX: BEST PRACTICES AND TECHNICAL VOCABULARY

### A. Camera Movement Vocabulary

| Movement | Keyword | Effect |
|----------|---------|--------|
| Approach | `dolly-in`, `push in` | Builds tension/intimacy |
| Retreat | `dolly-out`, `pull out` | Reveals the environment |
| Tracking | `track left/right` | Horizontal movement alongside subject |
| Pan | `pan left/right` | Horizontal rotation in place |
| Crane | `crane up/down` | Vertical camera movement |
| Orbit | `orbit`, `360 orbit` | Circle around subject |
| Handheld | `handheld` | Documentary/raw feel with micro-shake |
| Gimbal | `gimbal` | Stabilized, fluid movement |
| Dolly Zoom | `dolly zoom` | Hitchcock vertigo effect |
| Whip Pan | `whip pan` | Rapid pan for urgency |
| Aerial | `aerial sweep`, `drone shot` | View from above |

### B. Recommended Shot Sizes

| Shot Size | Ideal for | Recommended Movement |
|-----------|-----------|---------------------|
| Wide | Establishing shot, product panoramics | Slow push-in or static |
| Medium | Dialogue, UGC content | Handheld or Gimbal |
| Close-up | Details, emotion | Micro push-in |
| Extreme close-up | Macro, ASMR, texture | Static or rack focus |

### C. Style Keywords by Genre

| Genre | Recommended Keywords |
|-------|---------------------|
| Daily life/Vlog | Healing fresh, artistic, Japanese fresh, Korean mood |
| Sci-Fi/Blockbuster | Cyberpunk, Dark premium, Retro film, Dreamy soft light |
| Minimalist | Minimalist clean, Premium texture, Realistic photography |
| Cinematic | Cinematic texture, Film grain, Anamorphic lens flare |
| Film Noir | Film noir, Chiaroscuro lighting, High contrast |
| Anime | Anime style, Cel-shading, Studio Ghibli, Cyberpunk: Edgerunners |

### D. Audio Keywords

| Keyword | Effect |
|---------|--------|
| `reverb` | Reverb for large spaces (halls, cathedrals) |
| `muffled` | Muffled sound (enclosed spaces, underwater) |
| `echoing` | Echo effect (large chambers) |
| `metallic clink` | Metallic collision sound |
| `crunchy` | Textured sounds like gravel underfoot |
| `crackling fire` | Crackling fire sound |

### E. The 11 Fundamental Best Practices

1. **One verb per shot** - Multiple movement verbs create confusion
2. **Limit characters to 1-2** - More characters cause identity confusion
3. **Prompt length: 30-200 words** - Too short/long gets ignored
4. **Always include constraint words** for consistency
5. **No negative prompts** - Use only positive affirmations
6. **Add the quality suffix** to every prompt
7. **Start short, then extend** - Generate 5-10 seconds first
8. **Generate multiple variants** - Create 2-4 variants to compare
9. **Check @ tags** - Multi-reference errors are the most common
10. **Keep reference videos short** - Trim to the key segment
11. **Use "lens switch"** for multi-shot transitions in a single generation

### F. Re-Prompting Decision Tree

| Problem | Solution |
|---------|----------|
| Wrong composition, correct action | Modify only the Camera line |
| Movement too blurry/fast | Swap `handheld` with `gimbal`, set explicit speed |
| Style/color drifting | Replace Style with a single stronger anchor |
| Hand/label/flare artifacts | Change constraint words or try a different shot size |
| Chaotic multiple angles | Switch to "single tracking shot" |
| Face morphing | Use 2K+ images with "@Image1 stays identical" |
| Jittery motion | Specify speed ("slow dolly-in") |
| Scene discontinuity | Lock environment to a single reference |

### G. @ Reference System for Assets

| Purpose | Example Syntax |
|---------|---------------|
| Set first frame | `@Image1 as the first frame` |
| Reference camera movements | `Reference the camera movement from @Video1` |
| Assign character roles | `The woman in @Image1 as lead; man in @Image2 as supporting` |
| Reference actions | `Mimic the actions from @Video1` |
| Set background music | `@Audio1 as background music` |
| Extend video | `Extend @Video1 by X seconds` |
| Replace elements | `Replace [element A] in @Video1 with [element B]` |

### H. Seedance 2.0 Technical Specifications

- **Multimodal input:** Up to 12 references (9 images + 3 videos + 3 audio)
- **Native audio-video sync** with lip-sync in 8 languages
- **Automatic storyboarding** from text descriptions
- **2K resolution, 24-60 fps, 15-20 seconds per generation**
- **Usable output rate: 90%+**
- **File limits:** Images <30MB, Video 2-15s <50MB, Audio ≤15s <15MB

---

## SOURCES

This collection was compiled from the following sources:

**GitHub Repositories:**
- [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) - 1099 curated prompts
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - High-fidelity collection
- [gracech0322-cmd/seedance-2-prompt-library](https://github.com/gracech0322-cmd/seedance-2-prompt-library) - 6-dimension framework
- [makesupday/Awesome-Seedance-2.0-Prompt-and-Examples](https://github.com/makesupday/Awesome-Seedance-2.0-Prompt-and-Examples) - Templates and best practices
- [HuyLe82US/awesome-seedance-prompts](https://github.com/HuyLe82US/awesome-seedance-prompts) - Featured prompts
- [weshopai/awesome-Seedance-2.0-prompt](https://github.com/weshopai/awesome-Seedance-2.0-prompt) - Chinese and English prompts
- [seedanceprompts/seedance-prompts](https://github.com/seedanceprompts/seedance-prompts) - Resource aggregator
- [Anil-matcha/Seedance-2.0-API](https://github.com/Anil-matcha/Seedance-2.0-API) - Official Python wrapper
- [ai-seedance/seedance-2.0](https://github.com/ai-seedance/seedance-2.0) - Official Python client

**Guides and Blogs:**
- [imagine.art - 70 Prompt Guide](https://www.imagine.art/blogs/seedance-2-0-prompt-guide)
- [wavespeed.ai - Copy-Paste Framework](https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/)
- [seaart.ai - 20+ Examples](https://www.seaart.ai/blog/seedance-2-0-prompt)
- [redreamality.com - Prompt Engineering Playbook](https://redreamality.com/blog/seedance-2-guide/)
- [atlabs.ai - Prompts Guide](https://www.atlabs.ai/blog/seedance-2-prompts-guide)
- [glbgpt.com - From Zero to Cinematic](https://www.glbgpt.com/hub/seedance-2-0-prompt-guide/)
- [nereo.io - 8 Best Anime Prompts](https://www.nereo.io/blog/seedance-2-0-prompts)

---

> **License:** This collection is compiled for educational purposes. Individual prompts belong to their respective authors and repositories.
> Prompts are maintained in English for maximum compatibility with Seedance 2.0, which interprets English and Chinese prompts best.
> Notes and organizational structure have been translated to English.
