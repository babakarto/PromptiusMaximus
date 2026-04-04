# Audio Engineering — Seedance 2.0 Reference

> Seedance 2.0 auto-generates sound effects and background music from text descriptions.
> It supports `@Audio1`, `@Audio2`, `@Audio3` references for uploaded music/voice files.
> Lip-sync works automatically in 8+ languages. Famous character voices are recognized.
> **Rules:** Max 3 audio files, total duration ≤15 seconds. Never write "sound effects" — write SPECIFIC sounds.

---

## The 4-Layer Audio Structure

Every Seedance prompt should address up to four audio layers. Layer 1 (Ambient) is almost always present. Layers 2-4 are added as needed.

```
Layer 1: Ambient Bed        — continuous background tone
Layer 2: Foreground SFX     — specific action-synced sounds (Foley)
Layer 3: Music Cue          — score, song, or @Audio reference
Layer 4: Silence Design     — intentional absence of sound
```

---

### Layer 1: Ambient Bed

The ambient bed is the continuous background sound that establishes location and atmosphere. Always specify it first.

| Scene Type | Ambient Sound Examples |
|---|---|
| City — daytime | distant traffic hum, car horns echoing between buildings, pedestrian chatter |
| City — nighttime | low traffic drone, distant sirens, neon sign buzzing |
| City — rain | rain hitting asphalt, tires splashing through puddles, umbrella fabric rattling |
| Suburban | lawn mower in the distance, birds chirping, dog barking two houses away |
| Rural / countryside | crickets chirping, wind through tall grass, distant cow lowing |
| Forest — day | birdsong canopy, leaves rustling in breeze, twigs snapping underfoot |
| Forest — night | owl hooting, insects droning, branches creaking |
| Beach / ocean | waves crashing on shore, seagulls calling, wet sand squelching |
| River / stream | water babbling over rocks, dragonfly wings buzzing |
| Underwater | deep muffled pressure hum, bubbles rising, whale song in the distance |
| Cave | water dripping on stone, hollow wind echo, bats fluttering |
| Desert | dry wind howling, sand grains skittering across rock, vulture cry |
| Mountain summit | fierce gusting wind, thin air whistling, distant avalanche rumble |
| Interior — living room | clock ticking, refrigerator humming faintly, floorboards settling |
| Interior — kitchen | gas stove hissing, oil sizzling in a pan, knife chopping on wood board |
| Interior — office | keyboard clacking, fluorescent light humming, muffled phone ringing |
| Interior — hospital | heart monitor beeping steadily, rubber-soled shoes on linoleum, intercom paging |
| Interior — bar/pub | glasses clinking, jukebox playing muffled music, pool balls cracking |
| Interior — library | pages turning softly, hushed whispers, pencil scratching on paper |
| Interior — factory | conveyor belt clanking, hydraulic press hissing, metal grinding |
| Interior — elevator | mechanical hum ascending, cable tension creaking, ding at floor arrival |
| Space — exterior | absolute silence punctuated by radio static crackle |
| Space — ship interior | engine core low-frequency thrumming, air recycler whooshing, console beeping |
| Space station | pressurized air hissing through vents, magnetic boot clanks on metal floor |
| War zone | distant artillery thumping, helicopter rotors chopping, rubble settling |
| Carnival / fair | calliope organ playing, crowd laughter, roller coaster rumbling overhead |
| Stadium | crowd roaring, stomping feet reverberating, horn section blaring |
| Train station | PA system announcement echoing, train brakes screeching, suitcase wheels rolling |
| Airport | jet engine whine building, boarding announcement, luggage carousel belt grinding |
| Graveyard | wind moaning through headstones, iron gate creaking, crows cawing |

---

### Layer 2: Foreground SFX (Foley)

Foley sounds are action-specific. They must be timed to visible on-screen events. Write them as precise descriptions, not categories.

| Action Category | Specific Sound Descriptions |
|---|---|
| **Footsteps — hard** | leather boots clicking on marble, high heels clacking on concrete, combat boots thudding on metal grating |
| **Footsteps — soft** | bare feet padding on carpet, sneakers squeaking on gymnasium floor, socks shuffling on hardwood |
| **Footsteps — terrain** | boots crunching through fresh snow, shoes squelching in mud, sandals slapping on wet tile |
| **Impact — punch** | fist connecting with jaw (dull thud with skin slap), knuckles cracking against cheekbone |
| **Impact — kick** | boot slamming into ribs, shin colliding with heavy bag |
| **Impact — blunt** | baseball bat striking watermelon, hammer pounding nail into oak, crowbar clanging against pipe |
| **Impact — body fall** | body crumpling onto gravel, heavy collapse onto wooden floorboards, person slamming into wall |
| **Impact — crash** | car windshield shattering inward, china cabinet toppling and smashing, shopping cart overturning on asphalt |
| **Liquid — pour** | wine glugging from bottle into glass, water cascading into bathtub, hot coffee dripping into ceramic mug |
| **Liquid — splash** | cannonball into swimming pool, puddle stomped by running feet, bucket of water thrown at wall |
| **Liquid — drip** | faucet dripping into stainless sink, blood droplet hitting stone floor, condensation sliding off pipe |
| **Liquid — boil** | pot of water at rolling boil, tea kettle starting to whistle, oil popping and sputtering |
| **Fabric — clothing** | leather jacket zipping up, silk dress rustling with movement, denim jeans scraping against chair |
| **Fabric — tear** | shirt ripping at the seam, velcro strap ripping open, canvas tent tearing in wind |
| **Fabric — impact** | flag snapping in strong wind, wet towel whipping against skin, parachute deploying with whomp |
| **Metal — light** | keys jingling in pocket, coins dropping onto counter, zipper teeth sliding |
| **Metal — medium** | sword unsheathing from scabbard, revolver cylinder spinning and clicking shut, chain links rattling |
| **Metal — heavy** | vault door grinding open, anvil struck by hammer ringing, steel girder crashing onto concrete |
| **Metal — scrape** | knife blade dragging across sharpening steel, car fender scraping guardrail, fork screeching on plate |
| **Wood — light** | pencil snapping in half, matchstick striking and igniting, chopsticks clicking together |
| **Wood — heavy** | axe splitting log with crack, oak door slamming shut, wooden crate splintering on impact |
| **Wood — creak** | old rocking chair rocking on porch, rope bridge planks groaning underfoot, barn door swinging on rusty hinge |
| **Glass — break** | wine glass shattering on tile, window pane cracking from impact, lightbulb popping |
| **Glass — intact** | crystal glass ringing when flicked, jar lid unscrewing with pop, ice cubes clinking in tumbler |
| **Electronic — UI** | phone notification chime, computer startup tone, camera shutter click |
| **Electronic — malfunction** | circuit shorting with electric sizzle, hard drive clicking and dying, static burst from blown speaker |
| **Electronic — power** | power grid surging with deep hum, tesla coil arcing, transformer exploding with bang |
| **Vehicle — engine** | V8 muscle car rumbling at idle, motorcycle revving through gears, electric car whirring silently up to speed |
| **Vehicle — tire** | tires screeching on dry asphalt, gravel spraying from spinning wheels, tire blowout with explosive pop |
| **Vehicle — door** | car door slamming shut, truck tailgate dropping with metallic bang, submarine hatch sealing with pressurized hiss |
| **Weather — wind** | gust rattling window panes, tornado roar building in intensity, gentle breeze through wind chimes |
| **Weather — rain** | single raindrop hitting tin roof, downpour hammering on car hood, thunder cracking overhead |
| **Weather — ice/snow** | icicle snapping off gutter, ice sheet cracking underfoot, hail pelting against glass |
| **Fire** | match head flaring to life, campfire logs crackling and popping, inferno roaring through building |
| **Body — breath** | heavy panting after sprinting, slow controlled exhale through nose, gasp of sudden shock |
| **Body — eating** | apple crunching with first bite, slurping soup from spoon, chewing gum popping |
| **Body — physical** | neck cracking, knuckles popping, stomach growling |
| **Animal — domestic** | cat purring in lap, dog growling low in throat, horse whinnying and stamping hoof |
| **Animal — wild** | wolf howling in the distance, eagle screeching overhead, snake hissing with rattle shaking |
| **Weapon — firearm** | pistol slide racking, suppressed gunshot (muffled thud), shotgun pump-action cycling |
| **Weapon — blade** | knife pulled from wooden block, sword clashing against sword, arrow thudding into target |
| **Weapon — energy (sci-fi)** | laser beam searing through air, plasma rifle charging with rising whine, lightsaber humming and crackling |
| **Door / gate** | heavy church door booming shut, screen door spring stretching and slapping closed, electronic airlock cycling |
| **Paper** | letter envelope tearing open, book pages flipping rapidly, newspaper crumpling into ball |
| **Rope / string** | guitar string snapping, taut rope groaning under strain, whip cracking through air |
| **Explosion** | grenade detonating with sharp concussive blast, distant building demolition rumbling, firework shell bursting overhead |
| **Mechanical** | clock gears engaging, printing press slamming down, elevator cable winding with metallic groan |

---

### Layer 3: Music Cue

| Music Type | Prompt Syntax |
|---|---|
| No music | *(simply omit any music reference)* |
| Genre — orchestral | `sweeping orchestral score with rising strings and French horn` |
| Genre — electronic | `pulsing synthwave beat with arpeggiated bassline at 120 BPM` |
| Genre — hip-hop | `trap beat with heavy 808 bass and hi-hat rolls` |
| Genre — jazz | `smoky jazz piano trio with brushed drums and walking upright bass` |
| Genre — rock | `distorted electric guitar power chords with driving drum fill` |
| Genre — classical | `solo cello playing a melancholic adagio passage` |
| Genre — ambient | `ethereal pad drones with slow-evolving granular texture` |
| Genre — folk/acoustic | `fingerpicked acoustic guitar with harmonica melody` |
| Genre — Latin | `salsa rhythm with conga, timbale, and brass stabs` |
| Genre — cinematic horror | `dissonant string cluster with low piano note sustaining` |
| Genre — lo-fi | `lo-fi hip-hop beat with vinyl crackle and mellow keys` |
| Mood — triumphant | `triumphant brass fanfare building to cymbal crash crescendo` |
| Mood — melancholic | `slow piano melody in minor key with sparse reverb` |
| Mood — tense | `staccato strings with ticking percussion building in tempo` |
| Mood — playful | `bouncy pizzicato strings with xylophone and light percussion` |
| Mood — romantic | `gentle strings swelling with harp arpeggios and soft flute` |
| Mood — mysterious | `low sustained cello drone with glass harmonica overtones` |
| Mood — epic | `full orchestra fortissimo with choir chanting and taiko drums` |
| @Audio reference | `@Audio1 plays throughout` or `@Audio1 kicks in at the drop moment` |
| @Audio with fade | `@Audio2 fades in gradually` or `@Audio1 fades out as scene ends` |
| Beat-sync | `@Audio1 beat-synced — cut on each downbeat` |

**@Audio reference rules:**
- Use `@Audio1`, `@Audio2`, `@Audio3` (max 3 files)
- Total combined audio duration must be ≤15 seconds
- Reference uploaded files only — do not invent file names
- Can be music tracks, voice recordings, or sound samples

---

### Layer 4: Silence Design

Silence is a sound design choice. Use it intentionally for dramatic weight.

| Technique | When to Use | Prompt Phrasing |
|---|---|---|
| Hard cut to silence | After explosion or loud event | `sudden absolute silence after the blast` |
| Breath beat | Before a reveal or punchline | `a beat of silence, then...` |
| Ringing silence | After gunshot or slap | `ringing tinnitus tone replacing all ambient sound` |
| Muted world | Character dissociation / shock | `all sound drops to muffled underwater murmur` |
| Pre-drop silence | Before bass drop or music hit | `music cuts — one beat of dead silence — then @Audio1 drops` |
| Heartbeat isolation | Fear / intimacy | `all ambient sound fades leaving only a slow heartbeat thudding` |
| Vacuum silence | Space scenes | `no sound — pure vacuum silence with only suit breathing` |

---

## Dialogue Prompt Syntax

### Basic Format

```
CHARACTER says: "Dialogue line here."
```

### With Emotion Modifiers

```
CHARACTER says with trembling voice: "I can't believe it's over."
CHARACTER whispers urgently: "Get down — now."
CHARACTER shouts with rage: "You had no right!"
CHARACTER says coldly: "We're done here."
CHARACTER stammers nervously: "I — I didn't mean to —"
CHARACTER says with a warm laugh: "You haven't changed a bit."
```

### Emotion Modifier Reference

| Modifier | Vocal Quality |
|---|---|
| `with trembling voice` | shaky, emotionally fragile |
| `whispering` | quiet, intimate, breathy |
| `whispering urgently` | hushed but intense |
| `shouting` | loud, forceful projection |
| `shouting with rage` | loud, raw, aggressive |
| `screaming in terror` | high-pitched, panicked |
| `says coldly` | flat affect, controlled menace |
| `says sarcastically` | dry, mocking tone |
| `stammers nervously` | broken rhythm, hesitant |
| `murmurs sleepily` | slow, soft, trailing off |
| `says with confidence` | strong, steady, authoritative |
| `says through tears` | wet, breaking voice |
| `growls menacingly` | low, guttural, threatening |
| `says with wonder` | breathy, wide-eyed awe |
| `says with disgust` | clipped, repulsed |
| `pleads desperately` | high, rapid, begging |
| `says deadpan` | zero inflection, dry |
| `says with a warm laugh` | voice breaks into gentle laughter |
| `hisses through clenched teeth` | tight, pressured, seething |
| `bellows` | deep, booming, commanding |

### Multiple Characters

```
ALEX shouts: "Look out!"
MAYA screams in terror: "What is that thing?!"
ALEX says through gritted teeth: "Run. Don't look back."
```

### Famous Character Auto-Voice

Seedance recognizes voices of well-known characters. Write the character name and it auto-matches the vocal timbre.

| Category | Confirmed / Expected Characters |
|---|---|
| Animation | SpongeBob, Shrek, Elsa, Buzz Lightyear, Homer Simpson, Goku |
| Film | Darth Vader, Gandalf, Jack Sparrow, The Joker (Heath Ledger), Forrest Gump |
| Games | Mario, Kratos, Master Chief, GLaDOS |
| Internet/Meme | Morgan Freeman (narrator), David Attenborough (narrator) |

> **Tip:** Write the character name naturally — `Darth Vader says: "I find your lack of faith disturbing."` — and Seedance will apply the recognizable voice timbre.

### Lip-Sync Languages

Automatic lip-sync is supported in: **English, Chinese (Mandarin), Japanese, Korean, Spanish, French, German, Portuguese**, and more. Just write dialogue in the target language — lip-sync adapts automatically.

---

## Audio by Scene Type

| Scene Type | Layer 1: Ambient | Layer 2: Foley | Layer 3: Music | Layer 4: Silence |
|---|---|---|---|---|
| **Action / fight** | rubble settling, crowd panic | fist impacts, body slams, glass breaking, grunts | driving percussion, @Audio for stunt choreography | silence before final blow |
| **Romance** | rain on window, fireplace crackling | wine glass set on table, fabric rustling | slow piano or strings, @Audio for love song | pause before first kiss |
| **Horror** | old house settling, wind moaning | floorboard creak, door handle turning slowly | dissonant drones, staccato stingers | dead silence before jump scare |
| **Comedy** | cafe chatter, park ambience | exaggerated slip sound, cartoon bonk | playful pizzicato, upbeat ukulele | beat of silence before punchline |
| **Commercial / product** | minimal or none | product click, pour, unboxing sounds | upbeat corporate pop, @Audio brand jingle | silence on logo reveal |
| **ASMR** | near-silence, soft room tone | tapping on microphone, whispering, crinkling paper, liquid pouring | none — ASMR relies on Foley purity | long pauses between sounds |
| **Nature documentary** | forest canopy, savanna wind | animal footfalls, wing flaps, water lapping | orchestral wonder theme | silence as predator stalks |
| **Sci-fi** | ship engine hum, console beeping | airlock hiss, hologram flickering, plasma discharge | synth pads, electronic score | vacuum silence in space exterior |
| **Drama / dialogue** | room tone matched to setting | glass set down, chair creak, pen click | understated piano, sparse strings | silence in emotional confrontation |
| **Music video** | none | none (music dominates) | @Audio1 as primary track, beat-synced | break before final chorus |
| **Sports** | stadium crowd roar | ball impact, whistle, shoes on turf | hype electronic track, @Audio for highlight reel | slow-mo silence before goal |
| **Cooking** | kitchen background hum | sizzling, chopping, stirring, pouring | light acoustic guitar | — |
| **War / military** | distant artillery, helicopter rotors | gunfire, shell casings dropping, radio squelch | dark orchestral, snare drum march | silence after explosion (shell shock) |

---

## Beat-Sync Technique

Beat-sync ties visual cuts and camera moves to the rhythm of a music track. This requires an `@Audio` reference.

### How to Write Beat-Sync Prompts

```
@Audio1 plays — each visual cut lands precisely on the downbeat.
On beat 1: wide shot of city skyline.
On beat 2: close-up of eyes opening.
On beat 3: tracking shot through crowd.
On beat 4: freeze frame on subject turning.
```

### Beat-Sync Tips

| Tip | Detail |
|---|---|
| Upload a track with a clear beat | Seedance responds best to strong rhythmic patterns (kick drum, snare) |
| Describe cuts per beat | Map each significant visual change to a beat number or musical moment |
| Use musical terms | "on the drop," "during the bridge," "at the crescendo," "on the downbeat" |
| Sync motion to tempo | "walking pace matches the BPM" or "punches land on snare hits" |
| Use silence strategically | "music cuts at 0:08, two beats of silence, then drops back in" |

---

## Sound Modifier Keywords

Add these modifiers to any sound description to shape its quality.

| Modifier | Effect | Example |
|---|---|---|
| `distant` | sounds far away, lower volume, more reverb | `distant thunder rolling` |
| `close-up` | intimate, detailed, present | `close-up sound of pen scratching on paper` |
| `muffled` | blocked by wall or material, reduced high frequencies | `muffled argument through the wall` |
| `echoing` | bouncing off hard surfaces | `footsteps echoing in empty cathedral` |
| `reverberant` | long tail, large space feel | `reverberant gunshot in parking garage` |
| `sharp` | high-frequency emphasis, sudden attack | `sharp crack of a branch snapping` |
| `deep` | low-frequency emphasis, bass-heavy | `deep rumble of approaching earthquake` |
| `resonant` | sustained tone, vibrating | `resonant gong strike decaying slowly` |
| `tinny` | thin, metallic, small speaker quality | `tinny radio playing an old song` |
| `building` | gradually increasing in volume/intensity | `building roar of approaching tornado` |
| `fading` | gradually decreasing | `fading echo of a scream` |
| `staccato` | short, clipped, rhythmic | `staccato burst of machine gun fire` |
| `sustained` | long, continuous, held | `sustained violin note swelling` |
| `wet` | liquid quality, splashy | `wet slap of raw steak on counter` |
| `dry` | no reverb, dead room, close | `dry click of light switch` |
| `harsh` | grating, unpleasant, aggressive | `harsh feedback squeal from microphone` |
| `soft` | gentle, quiet, delicate | `soft rustle of silk sheets` |
| `hollow` | empty resonance, pipe-like | `hollow knock on fiberglass door` |
| `metallic` | ringing, steely quality | `metallic clang of manhole cover dropping` |
| `organic` | natural, non-mechanical | `organic crunch of walking through dry leaves` |
| `distorted` | overdriven, clipping | `distorted bass guitar growling` |
| `filtered` | bandwidth-limited, EQ'd | `filtered voice through walkie-talkie` |
| `underwater` | low-pass, bubbly, murky | `underwater explosion — deep thud with bubble rush` |
| `slowed-down` | time-stretched, lower pitch | `slowed-down heartbeat in slow-motion scene` |
| `rapid-fire` | fast repetition | `rapid-fire typing on mechanical keyboard` |

---

## Common Audio Mistakes

| Mistake | Why It Fails | Fix |
|---|---|---|
| Writing "sound effects play" | Too vague — Seedance generates nothing specific | Write exact sounds: `glass shattering on marble floor` |
| Writing "dramatic music" | No genre, no instrumentation, no mood specificity | Write: `tense staccato strings building with timpani crescendo` |
| Forgetting ambient bed | Scene feels sonically empty, unrealistic | Always start with one ambient sentence for the environment |
| Using more than 3 @Audio files | Hard limit — prompt will fail or ignore extras | Consolidate to 3 maximum, total ≤15s |
| Writing silent scenes without intent | Absence of sound reads as a mistake, not a choice | Explicitly write `in complete silence` or add ambient layer |
| Overloading Foley | Too many simultaneous sounds cause muddiness | Limit to 2-3 foreground sounds per moment |
| Generic dialogue with no emotion | Flat, robotic delivery | Always add emotion modifier: `says with barely contained fury` |
| Mismatching audio to visual mood | Happy music on sad scene (unless intentional irony) | Match emotional register or explicitly mark as contrast |
| Writing "background noise" | Undefined — could be anything | Specify: `background hum of air conditioning and muffled office chatter` |
| Describing sounds that aren't visible | Sound of rain when scene is indoors with no windows | Ensure sounds match what the camera can logically "hear" |

---

## Audio Prompt Templates

### Template 1: Action Scene

```
AMBIENT: gravel crunching underfoot, distant police sirens wailing, wind gusting through
broken chain-link fence.

FOLEY: leather boot stomps on concrete — fist slams into jaw with a dull crack — body
crashes through wooden pallets splintering on impact — heavy breathing and grunting.

MUSIC: aggressive industrial percussion with distorted bass pulses building in intensity.

HERO shouts with adrenaline: "Stay down!"
VILLAIN growls through blood: "Not... a chance."
```

### Template 2: Romantic / Emotional Scene

```
AMBIENT: light rain pattering on window glass, fireplace logs crackling softly, clock
ticking on mantel.

FOLEY: wine glass set gently on oak table — fabric of coat sliding off shoulders —
soft footsteps crossing hardwood floor.

MUSIC: @Audio1 — slow acoustic guitar melody fading in.

ELLA says with a trembling voice: "I didn't think you'd come back."
JAMES whispers: "I never left. Not really."

A beat of silence. Only the rain and the fire.
```

### Template 3: Horror / Suspense Scene

```
AMBIENT: old house settling with deep groans, wind moaning through cracked walls,
floorboards creaking on their own.

FOLEY: slow footstep on stairs — wooden step groaning under weight — doorknob
turning with a rusted squeal — long pause — then a sharp BANG of door slamming.

MUSIC: single sustained low cello drone with barely audible dissonant whispers.

Sudden absolute silence.

Then — close-up breathing, fast and panicked.

SARAH whispers urgently: "Don't. Move."
```

### Template 4: Commercial / Product Reveal

```
AMBIENT: none — clean audio space.

FOLEY: crisp unboxing sound — cardboard lid lifting — product clicking into place
with satisfying mechanical snap — fingertip tapping on glass screen with precision.

MUSIC: @Audio1 — upbeat minimal electronic track with clean synth pulse, beat-synced.
Each product angle change lands on the downbeat.

NARRATOR says with confidence: "Designed for the way you move."

Music swells to final chord on logo reveal — then silence.
```

---

## Quick Reference: Audio Layer Checklist

Before finalizing any prompt, verify:

```
[ ] Layer 1 — Ambient bed specified (or explicitly marked as "clean/no ambient")
[ ] Layer 2 — Foley sounds tied to visible on-screen actions
[ ] Layer 3 — Music genre/mood defined OR @Audio referenced OR intentionally omitted
[ ] Layer 4 — Silence used intentionally if scene has dramatic pauses
[ ] Dialogue — Emotion modifiers on every spoken line
[ ] @Audio — Max 3 files, total ≤15 seconds
[ ] Sound modifiers — Distance, texture, and quality descriptors included
[ ] No vague terms — Every sound is specific and visualizable
```
