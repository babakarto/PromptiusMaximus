# LIBRERIA COMPLETA PROMPT SEEDANCE 2.0

> **Oltre 500 prompt curati** per la generazione video con Seedance 2.0 di ByteDance.
> Raccolti da 15+ repository GitHub e 6+ guide specializzate.
> Ultimo aggiornamento: 24 Marzo 2026

---

## INDICE

1. [FRAMEWORK E STRUTTURA DEI PROMPT](#1-framework-e-struttura-dei-prompt)
2. [CINEMATOGRAFICO / FILM](#2-cinematografico--film)
3. [ANIME / ANIMAZIONE](#3-anime--animazione)
4. [COMMERCIALE / PUBBLICITA](#4-commerciale--pubblicita)
5. [SOCIAL MEDIA / UGC](#5-social-media--ugc)
6. [NATURA / PAESAGGIO](#6-natura--paesaggio)
7. [ANIMAZIONE PERSONAGGI](#7-animazione-personaggi)
8. [ASTRATTO / ARTISTICO](#8-astratto--artistico)
9. [VETRINA PRODOTTI](#9-vetrina-prodotti)
10. [AZIONE / COMBATTIMENTO](#10-azione--combattimento)
11. [FANTASY / FANTASCIENZA](#11-fantasy--fantascienza)
12. [CIBO / ASMR / SENSORIALE](#12-cibo--asmr--sensoriale)
13. [MUSICA / DANZA](#13-musica--danza)
14. [COMMEDIA / MEME](#14-commedia--meme)
15. [HORROR / SUSPENSE](#15-horror--suspense)
16. [SPORT / RACING](#16-sport--racing)
17. [MOMENTI INTIMI / SLICE OF LIFE](#17-momenti-intimi--slice-of-life)
18. [STORYTELLING MULTI-INQUADRATURA](#18-storytelling-multi-inquadratura)
19. [AUDIO / LIP-SYNC](#19-audio--lip-sync)
20. [TRASFERIMENTO STILE / VFX](#20-trasferimento-stile--vfx)
21. [APPENDICE: BEST PRACTICES E VOCABOLARIO TECNICO](#21-appendice-best-practices-e-vocabolario-tecnico)

---

## 1. FRAMEWORK E STRUTTURA DEI PROMPT

### 1.1 Formula Universale (5 Segmenti)

```
Soggetto + Azione + Camera + Stile + Vincoli
```

**Nota:** Questa struttura e la base di ogni prompt efficace. Il modello interpreta meglio prompt strutturati con logica interna chiara.

### 1.2 Template Master (Copia-Incolla)

```
Subject: [una persona/oggetto, eta o materiale se rilevante]
Action: [frase verbale specifica, tempo presente]
Camera: [dimensione inquadratura] + [movimento] + [angolazione], [lunghezza focale]
Style: [un ancoraggio visivo: film/processo/artista], [illuminazione], [trattamento colore]
Constraints: [lista esclusioni], [frame rate/tempo], [durata o timing], [note consistenza]
```

### 1.3 I 5 Template Pronti all'Uso

**TEMPLATE UGC (Effetto telefono in mano):**
```
Subject: [persona, fascia eta, ambientazione]
Action: [parla casualmente di X mentre fa Y]
Camera: Medium, prospettiva telefono handheld, leggera oscillazione, altezza occhi, lente normale
Style: Luce interna naturale, look non gradato, leggero motion blur
Constraints: No didascalie, no snap zoom, mani naturali, 8-10s, sfondo semplice
```
> **Perche funziona:** L'oscillazione handheld e l'assenza di color grading comunicano autenticita, essenziale per contenuti UGC.

**TEMPLATE PUBBLICITA PRODOTTO (Pulito e stabile):**
```
Subject: [nome prodotto/materiale/colore]
Action: [ruota lentamente / scivola in inquadratura / movimento hero sottile]
Camera: Close-up a medium close-up, dolly-in lento, orizzonte bloccato, sensazione normale-tele
Style: Luce key morbida + rim gentile, color grade neutro, leggero film grain
Constraints: No loghi/etichette, no flare, mantieni frame finale 2s, 6-8s totali
```
> **Perche funziona:** Il dolly-in lento costruisce desiderio verso il prodotto; il rim light separa il soggetto dallo sfondo.

**TEMPLATE CINEMATOGRAFICO (Mood-First):**
```
Subject: [personaggio o luogo]
Action: [beat specifico: aspetta, si gira, respira, entra nella luce]
Camera: Wide establishing 2s poi push lento a medium, gimbal-smooth, altezza occhi
Style: [singolo riferimento ancora, es. "luce naturale coperta, blu smorzati"]
Constraints: No angoli olandesi, no folla, no neon, mantieni look coperto, 10-12s
```
> **Perche funziona:** Un singolo ancoraggio visivo batte sei aggettivi; il beat singolo evita confusione nel modello.

**TEMPLATE TALKING HEAD (Stabile e leggibile):**
```
Subject: [descrizione speaker]
Action: [pronuncia una frase chiara]
Camera: Medium close-up, treppiede fisso o dolly-in sottile, altezza occhi
Style: Key morbido da 45 gradi, separazione sfondo pulita, grade neutro
Constraints: No didascalie auto, no whip pan, toni pelle naturali, 12-15s, linea occhi centrata
```

**TEMPLATE MONTAGGIO (Beat rapidi senza caos):**
```
Subject: [tema, es. "rituale caffe mattutino"]
Action: Beat 1 [wide contesto], Beat 2 [close-up mani], Beat 3 [dettaglio vapore], Beat 4 [sorso]
Camera: Ogni beat 2s, dimensione inquadratura chiara per beat, no movimenti composti - transizioni per taglio
Style: Luce e palette consistenti tra i beat
Constraints: No overlay testo, no speed ramp, tempo costante, 8-10s totali
```

### 1.4 Framework CRAFT Multimodale

```
Context + Reference (@assets) + Action + Framing/Timing + Tone/Audio
```

### 1.5 Struttura Timeline (per contenuti narrativi)

Organizza video di 15 secondi in: setup (0-5s), conflitto (5-10s), climax (10-15s).

### 1.6 Suffisso Qualita (Da aggiungere a OGNI prompt)

```
4K, Ultra HD, Rich details, Sharp clarity, Cinematic texture, Natural colors,
Soft lighting, No blur, No ghosting, No flickering, Stable picture.
```

### 1.7 Parole Vincolo Essenziali

Seedance 2.0 **non supporta prompt negativi**. Usa affermazioni positive:
- "Maintain face and clothing consistency, no distortion, high detail."
- "Character face stable without deformation, normal human structure, natural smooth movements."
- "Generate video without subtitles"

---

## 2. CINEMATOGRAFICO / FILM

### P-001. Sequenza Cinematografica Pizzeria
```
Single continuous cinematic shot, no music. From outside the glass window, the dim
camera slowly pushes inward into a pizza shop. Inside, a chef stretches dough in the
air, catches it, spreads sauce, and slides it into a wood-fired oven. A customer at the
counter watches, mesmerized. Warm amber lighting from the oven, flour particles
floating in the air.
```
> **Efficacia:** L'inquadratura continua senza tagli crea immersione totale. La specificazione "no music" forza il modello a generare suoni ambientali realistici.

### P-002. Esplorazione Grotta POV
```
First-person POV handheld footage with slight natural shake. The only light comes from
a headlamp cutting through absolute darkness. Dripping water echoes. The beam reveals
ancient crystal formations glowing faintly blue and purple. Hands reach out to touch a
crystal surface. Sound of heavy breathing reverberates.
```
> **Efficacia:** Il POV in prima persona con shake naturale crea tensione cinematografica. La specificazione della sorgente luminosa singola guida il rendering dell'illuminazione.

### P-003. Cavaliere nella Grotta (Multi-Shot)
```
A multi-shot sequence of a knight in silver armor. Shot 1: Wide shot as he enters a
dark cave with a torch. Shot 2: Close-up of his nervous eyes. Shot 3: He draws his
sword, which glows blue, illuminating the entire cavern to reveal a massive sleeping
dragon.
```
> **Efficacia:** La struttura multi-shot con progressione narrativa (entrata -> tensione -> rivelazione) crea un mini-film completo.

### P-004. Pianista con Illuminazione Butterfly
```
Cinematic butterfly lighting. Medium shot of a handsome pianist wearing a simple,
elegant black suit, performing passionately at a grand piano in a dimly lit concert hall.
Soft spotlight from above creates butterfly shadow beneath his nose. Fingers move
fluidly across keys. Shallow depth of field isolates him from the blurred audience.
```
> **Efficacia:** Il termine tecnico "butterfly lighting" attiva uno schema illuminazione specifico e professionale nel modello.

### P-005. Steadicam dal Caffe alla Metro
```
Steadicam long take following a man from a warm, yellow-lit cafe into a cool-toned,
busy street, then descending stairs into a subway station. The color temperature shifts
gradually from warm amber to cold fluorescent blue. Background transitions from quiet
murmur to urban cacophony to echoing tunnel acoustics.
```
> **Efficacia:** La transizione di temperatura colore (caldo -> freddo) e l'evoluzione sonora ambientale creano un viaggio sensoriale completo in un'unica inquadratura.

### P-006. Film Retrò Hong Kong Anni '90
```
90s Hong Kong art cinema style with retro grain, yellow-green tint, and step-printing
effect. A melancholic young woman in a trench coat stands at a phone booth in the rain.
She lifts the receiver, pauses, then hangs up without dialing. Neon bokeh reflections
on wet pavement. Camera pulls back slowly as she walks away, trailing shadows behind
her in the step-printed frames.
```
> **Efficacia:** I riferimenti stilistici precisi (Wong Kar-wai) con tecniche specifiche (step-printing, tinta giallo-verde) danno al modello un ancoraggio visivo forte.

### P-007. Scena Deserto Stile Denis Villeneuve
```
IMAX 70mm film approach. A colossal sandstorm wall approaches a military convoy in a
vast desert. Shot 1: Extreme wide establishing the scale of the storm versus tiny
vehicles. Shot 2: Inside cockpit, pilot screams "GO! GO!" gripping controls in panic.
Shot 3: Convoy attempts emergency U-turn as sand engulfs vehicles. Shot 4: Slow-motion
dune jump with vehicle silhouetted against lightning within the storm, debris suspended
in air.
```
> **Efficacia:** Il riferimento "IMAX 70mm" imposta scala e granularita. La progressione dal macro al micro crea tensione cinematografica epica.

### P-008. Film Noir Donna in Rosso
```
A woman in a red dress walks confidently down a rainy city street at night, neon
reflections on wet pavement, film noir style, tracking shot. High contrast chiaroscuro
lighting, the red dress is the only saturated color in an otherwise desaturated frame.
Her heels click rhythmically on the wet asphalt.
```
> **Efficacia:** L'isolamento cromatico (rosso su desaturato) e un trucco cinematografico classico che il modello esegue bene.

### P-009. Viaggiatore al Tramonto (Dolly Push-In)
```
A weary traveler in a dusty leather cloak. He slowly removes his wide-brimmed hat and
exhales, looking toward a sunset. Low-angle medium shot, slow dolly-in towards his
face, shallow depth of field. Golden hour backlighting creates a warm halo around his
silhouette. Dust particles dance in the amber light.
```
> **Efficacia:** Il dolly-in lento con bassa angolazione trasmette rispetto e grandezza del personaggio, tecnica classica dei western.

### P-010. Scena Ronin Surreale
```
Complex action sequence with a masked warrior fighting a winged beast on floating
islands during a thunderstorm. Handheld camera chaos captures impossible gravity-defying
leaps between crumbling rock platforms. Lightning illuminates the scene in stroboscopic
flashes. The warrior's tattered cloak trails behind during each impossible jump.
```
> **Efficacia:** La combinazione di elementi fantastici con camera handheld caotica crea un contrasto che rende la scena viscerale e credibile.

### P-011. Auto di Lusso si Trasforma in Optimus Prime
```
A luxury sports car driving through rainy Tokyo at night suddenly begins transforming
into Optimus Prime. CGI battle scene as the transformed mech fights Godzilla between
skyscrapers. Explosions light up neon-reflected puddles. Energy blasts create shockwaves
that shatter windows. Camera orbits the battle from a news helicopter perspective.
```
> **Efficacia:** Il mix di brand riconoscibili con ambientazione specifica (Tokyo notturna) e la prospettiva "news helicopter" creano un senso di evento realistico.

### P-012. Adattamento Live-Action Anime: Duello Acqua vs Tuono
```
Hollywood-style samurai duel with elemental special effects. A water-breathing swordsman
faces a thunder-breathing warrior in a rain-soaked temple courtyard. 15 seconds total.
0-5s: They face each other, rain freezes mid-air between them. 5-10s: Explosive clash,
water serpents meet lightning bolts. 10-15s: Slow-motion aftermath, both kneel, temple
crumbles behind them. Cinematic 2.39:1 aspect ratio.
```
> **Efficacia:** La struttura timeline precisa (0-5s, 5-10s, 10-15s) guida il modello su cosa generare in ogni segmento.

### P-013. Inseguimento Speeder nella Citta Scogliera
```
Single continuous shot featuring a high-speed chase through monumental cliffside
architecture. A hovering speeder weaves between carved stone buildings and hanging
bridges. Camera mounted on pursuing vehicle, slight vibration from engine. Wind
distortion on audio. Near-misses with market stalls and pedestrians who dive out of
the way.
```
> **Efficacia:** La specificazione "camera mounted on pursuing vehicle" crea una prospettiva immersiva con motivazione diegetica per il movimento camera.

### P-014. Stile John Woo - Balletto di Proiettili in Corridoio
```
Corridor gunfight in John Woo signature style. Two suited men exchange fire in a narrow
hallway. Rhythm editing with snap-zooms on shell casings ejecting. Slow-motion dove
flies between combatants. Impact beats synchronized to gunfire rhythm. One man slides
on his knees firing both pistols. Spent cartridges ring on marble floor.
```
> **Efficacia:** Il riferimento a John Woo attiva uno stile specifico riconoscibile. I dettagli ritmici (bossoli, colombe) sono marchi stilistici che il modello conosce.

### P-015. Spy Brawl: Abito contro Abito
```
Spy brawl in cramped office space. Two men in tailored suits exchange rapid blows using
office furniture as weapons. Rapid angle switches between over-shoulder and wide shots.
Clean choreography with keyboard used as shield, monitor as projectile. Comedic ending:
both pause, straighten ties simultaneously, resume fighting.
```
> **Efficacia:** Il contrasto tra eleganza (abiti su misura) e caos (combattimento con mobili) crea interesse visivo. Il finale comico aggiunge un beat narrativo memorabile.

### P-016. Cattedrale Sotto il Mar Nero
```
Underwater descent through a flooded megastructure. Camera follows a diver sinking past
massive stone columns covered in bioluminescent coral. A leviathan silhouette passes in
the distant murk. Vertigo-inducing downward camera movement. Shafts of surface light
pierce the depth, creating god rays through particulate water.
```
> **Efficacia:** Il movimento camera "vertigo-inducing downward" e la rivelazione progressiva (colonne -> coralli -> leviatano) costruiscono tensione crescente.

### P-017. Ritratto Cinematografico Realistico
```
Dramatic character reveal. A mysterious figure emerges from shadows into golden hour
light, long black coat billowing in wind. Turns with intense piercing eyes toward camera.
Wide shot transitioning to close-up. Cinematic high contrast, film noir aesthetic with
dramatic rim lighting. Shallow depth of field isolates subject from urban background.
```
> **Efficacia:** La transizione wide-to-close-up durante una rivelazione e una tecnica fondamentale del cinema narrativo.

### P-018. Scena Cucina Thriller
```
Dark, moody kitchen lit by a single pendant light. Five shots: Shot 1: Over-shoulder of
man staring at phone on table. Shot 2: Woman across table, arms crossed, cold expression.
Shot 3: Close-up man's hand reaching for phone. Shot 4: Woman's hand slams on his.
Shot 5: Profile two-shot, tension palpable, neither speaks. Sound: clock ticking,
refrigerator hum, breathing.
```
> **Efficacia:** Il thriller in ambiente domestico dimostra che non servono effetti speciali: la tensione nasce dal montaggio e dal suono ambientale.

### P-019. Corsa Hollywoodiana Notturna
```
Hollywood professional racing style at night in the rain. Shot 1 (00-05s): Close-up
inside the veteran driver's car, hands grip wheel, eyes narrow with focus, rain
hammering windshield. Shot 2 (05-10s): External tracking shot as the car accelerates
through a sweeping turn, water spray creating a rooster tail of mist. Shot 3 (10-15s):
Drone shot from above showing the car's headlights cutting through rain on an empty
mountain road.
```
> **Efficacia:** La progressione interno -> esterno -> aereo in tre shot crea escalation visiva tipica dei film di corse.

### P-020. Scena Telefono Stile Wong Kar-wai
```
Wong Kar-wai rainy phone booth scene. 90s Hong Kong art cinema aesthetic. Rain-covered
phone booth, character in trench coat with melancholic posture. Frame stepping effects
create dreamlike motion. Neon bokeh lighting reflects in every water droplet. Character
exits, trailing shadows multiply due to step-printing effect. Warm yellow-green color
cast throughout.
```
> **Efficacia:** Il riferimento al regista specifico combinato con tecniche precise (step-printing, bokeh neon) crea un risultato stilisticamente coerente.

---

## 3. ANIME / ANIMAZIONE

### P-021. Ragazza Anime Guarigione
```
An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat,
standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the
camera and smiles gently. A light breeze moves her hair and dress. The camera slowly
pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and
peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion,
high detail.
```
> **Efficacia:** Il prompt "healing" e un genere anime specifico. La specificazione di consistenza facciale e abbigliamento evita il morphing tra frame.

### P-022. Duello Cyberpunk Samurai
```
Cyberpunk samurai with glowing katana faces robotic ninja. Scene 1: Quick zoom on
samurai drawing blade, blue energy crackles along the edge. Scene 2: Wide shot, both
dash towards each other on neon-lit Tokyo street. Scene 3: Extreme close-up of blades
clashing, sparks fly, white flash fills frame. Style: Cyberpunk: Edgerunners anime,
high contrast, fast cuts, motion blur.
```
> **Efficacia:** Il riferimento a "Cyberpunk: Edgerunners" e un ancoraggio stilistico potente che il modello riconosce, definendo palette e ritmo.

### P-023. Eroe Riluttante - Narrativa Personaggio
```
A young, timid librarian with messy brown hair and glasses discovers a glowing, ancient
book. Scene 1: nervously pushes glasses up, surrounded by dusty tomes, eyes wide with
fear. Scene 2: book opens, bathing him in golden light, shows determined awe. Scene 3:
stands tall, book held tightly, confident smile as library transforms around him.
Style: Ghibli-inspired, warm lighting, emotional close-ups.
```
> **Efficacia:** L'arco emotivo in tre scene (paura -> meraviglia -> determinazione) crea una mini-storia completa in stile Ghibli.

### P-024. Arco Emotivo - Superare l'Insicurezza
```
Shy artist with sketchbook of beautiful hidden drawings. Scene 1: Sits alone in park,
nervously hiding sketchbook, downcast expression. Scene 2: Child peeks over shoulder at
drawing, artist startled, sees child's face light up with wonder. Scene 3: Artist
smiles warmly, confidently displaying art on easel in the park.
Style: Soft pastel anime, gentle sunlight, focus on facial expressions.
```
> **Efficacia:** La palette pastello morbida e il focus sulle espressioni facciali sono scelte stilistiche che rafforzano il tema emotivo.

### P-025. Gatto Overdrammatico - Commedia Anime
```
Fluffy white cat sleeping on laptop keyboard. Scene 1: Owner gently nudges cat, it
opens one eye with deadpan stare. Scene 2: Lifts cat, which goes completely stiff and
board-like in protest, extreme close-up on offended, wide-eyed expression. Scene 3:
Places stiff cat on floor, remains upright before slowly toppling over like a statue.
Style: Slice-of-life anime, clean lines, exaggerated chibi-style reaction faces.
```
> **Efficacia:** Le espressioni esagerate in stile chibi sono una convenzione anime che il modello esegue bene, creando comicita visiva.

### P-026. Vetrina Streetwear E-Commerce Anime
```
Cool, confident young woman with silver hair wearing stylish black 'CyberGlow' brand
hoodie with neon-green accents. Scene 1: Sketching graffiti in notebook on nighttime
city rooftop, hoodie's logo subtly visible. Scene 2: Sudden downpour starts; quickly
pulls up hood, water-resistant fabric deflects raindrops, smirks. Scene 3: Stands
looking over neon-lit city, hoodie's glowing accents matching skyline.
Style: Cyberpunk anime, vibrant neon colors, dynamic camera angles, close-up on fabric texture.
```
> **Efficacia:** L'integrazione del prodotto nella narrativa (la pioggia dimostra l'impermeabilita) e superiore alla semplice esposizione statica.

### P-027. Adattamento Meme Anime - Fidanzato Distratto
```
Anime adaptation of distracted boyfriend meme. Scene 1: Stoic samurai with top-knot and
blue kimono walks beside cheerful shrine maiden in red and white miko outfit. Scene 2:
Powerful female warrior with silver armor and glowing sword walks past; samurai's head
turns, looking impressed and shocked. Scene 3: Close-up on shrine maiden with angry,
betrayed glare. Style: Crisp modern anime, high-contrast, dramatic expressions.
```
> **Efficacia:** La reinterpretazione di meme in stile anime e un formato virale. Le espressioni drammatiche amplificano l'effetto comico.

### P-028. Tip Produttivita Educativo Anime
```
Stressed anime office worker with messy black hair overwhelmed by giant, monstrous pile
of paperwork. Scene 1: Close-up on tired face, sighing in despair. Scene 2: Small,
friendly robot flies in, projects simple 2-minute timer, points to one paper. Scene 3:
Worker focuses, finishes one task as timer ends, relieved smile as one paper vanishes.
Text overlay: 'Beat procrastination. Try the 2-Minute Rule.'
Style: Modern anime, clean lines, high-contrast colors, simple animated text graphics.
```
> **Efficacia:** Il formato educativo in stile anime rende contenuti informativi visivamente coinvolgenti.

### P-029. Detective Cyberpunk Noir
```
Lone detective in trench coat stands on rain-slicked city street, looking up at
monolithic skyscraper. Scene 1: Close-up on face, illuminated only by flickering
holographic ad. Scene 2: Wide shot of street with flying vehicles and glowing neon
signs reflecting in puddles. Scene 3: Detective pulls up collar, single datastream
visible in cybernetic eye.
Style: Cyberpunk noir, high contrast, saturated neon palette (pinks and teals),
dramatic shadows, cinematic bloom effect, detailed cel-shading.
```
> **Efficacia:** La combinazione di noir classico con cyberpunk crea un'estetica forte. Il dettaglio "datastream nell'occhio cibernetico" e un micro-momento narrativo potente.

### P-030. Danza Ragazza Anime con Motion Capture
```
Anime girl performing an elegant dance sequence on a virtual stage. Motion capture
quality movements with fluid transitions between poses. Cherry blossom petals float
around her. Camera orbits smoothly at medium distance. Soft volumetric lighting creates
atmosphere. Hair and clothing physics respond naturally to each movement.
```
> **Efficacia:** La specificazione "motion capture quality" indica al modello un livello di fluidita e realismo dei movimenti superiore.

### P-031. Scontro Ghiaccio-Fuoco Nezha e Ao Bing
```
Four-act anime battle testing dynamic transitions. Act 1: Stillness to burst
acceleration as two warriors face each other. Act 2: Attribute transition from flame
to ice as attacks collide and transform. Act 3: Fierce physics collision with spiraling
motion and energy vortex. Act 4: Space-folding particle continuity as ice shatters
into flame fragments that reform into new attacks. Vibrant saturated colors, extreme
dynamic camera.
```
> **Efficacia:** La struttura in 4 atti con transizioni attributo (fuoco -> ghiaccio -> fusione) testa le capacita avanzate del modello.

### P-032. Battaglia Mecha Lontra Anime
```
An otter enters a large mech suit. Mechanical parts and gears turn with satisfying
clicks. The otter gives a grim thumbs up from the cockpit window. The mech launches
into battle against a colossal marble octopus in a ruined cityscape. Anime mecha style,
dramatic impact frames, speed lines during charges.
```
> **Efficacia:** L'elemento assurdo (lontra pilota mecha) combinato con la serieta del genere mecha crea un contrasto visivamente interessante.

### P-033. Scena Stile Jujutsu Kaisen
```
Jujutsu Kaisen-style scene. A dark-haired sorcerer with bandaged arms unleashes a domain
expansion. Blue magical energy erupts from the ground in geometric patterns. Flying
spectral swords materialize and orbit. Dramatic Japanese text overlay appears with
impact. Epic orchestral beats. Camera pulls back to reveal the full scope of the domain
as buildings bend and crack around the energy field.
```
> **Efficacia:** Il riferimento anime specifico (Jujutsu Kaisen) con elementi chiave del franchise (domain expansion, spade spettrali) crea un risultato riconoscibile.

### P-034. Torneo Arti Marziali Anime
```
Figure 1 character battling Figure 2 character in the World Martial Arts Tournament.
Wide arena with cheering crowd. Dragon Ball Z style energy auras around both fighters.
Rapid exchange of blows with impact shockwaves. Camera switches between close combat
and crowd reaction shots. Dramatic pause before final attack.
```
> **Efficacia:** L'uso di riferimenti immagine (@Image1, @Image2) per i personaggi garantisce consistenza visiva durante il combattimento.

---

## 4. COMMERCIALE / PUBBLICITA

### P-035. Spot Profumo Ultra-Lusso
```
An ultra-luxury perfume commercial with a dreamy electronic soundtrack and steady drum
beats. Opening: Macro shot of perfume bottle, light refracts through crystal-cut glass
creating rainbow prismatic patterns. Middle: A model's hand slowly reaches for the
bottle, fingertips barely touching. Close: Model applies perfume to wrist, closes eyes,
slight smile. Final: Bottle hero shot with soft bokeh background, brand light appears.
```
> **Efficacia:** La progressione macro -> interazione -> hero shot e la struttura classica degli spot profumo che il modello riproduce fedelmente.

### P-036. Spot Coca-Cola Narrativo
```
A narrative Coke interaction scene. A painted figure on a wall looks guilty, glancing
left and right. Its hand reaches out of the painting frame, grabs a Coke bottle from a
nearby table. Drinks it quickly, hides it behind the frame. A cowboy figure from another
painting takes the glass. Spotlight hits the Coke bottle for final hero shot on dramatic
black background.
```
> **Efficacia:** L'antropomorfizzazione di dipinti che interagiscono con prodotti reali crea un concetto pubblicitario memorabile e virale.

### P-037. Da Schizzo a Auto 3D
```
A car sketch on paper. The camera pushes in slowly. The sketch lines rise off the paper
and begin assembling in three dimensions. Wire-frame becomes solid surfaces. Color fills
in from front to back. Final: Fully rendered photorealistic car rotates on a showroom
turntable. Camera pulls back to reveal the original sketch beside the final car.
Transformation takes 10 seconds. Clean white studio environment.
```
> **Efficacia:** La trasformazione 2D-to-3D e un formato pubblicitario che dimostra il "processo creativo" dietro al prodotto.

### P-038. Time-Lapse Ristrutturazione Soggiorno
```
Based on the reference image, generate a time-lapse animation showing the living room
transforming from raw concrete and exposed wiring to a fully furnished, warm modern
home. Workers appear and disappear in fast-forward. Paint rolls onto walls, furniture
slides into place. Final reveal: Warm evening lighting turns on, camera slowly pans
across the finished room.
```
> **Efficacia:** Il time-lapse di ristrutturazione e un formato popolare sui social che il modello gestisce bene con riferimenti immagine.

### P-039. Blockbuster Sci-Fi Hollywoodiano
```
Create a 10-second cinematic sequence in a Hollywood sci-fi style with cyberpunk
aesthetics. A flying vehicle chase through a megacity canyon of neon-lit skyscrapers.
Vehicle weaves between holographic advertisements and floating traffic. Camera mounted
on pursuing vehicle with slight vibration. Rain creates streaks on the virtual camera
lens.
```
> **Efficacia:** La pioggia sulle lenti virtuali e un dettaglio sottile che aggiunge realismo cinematografico alla scena CGI.

### P-040. Video Promozionale MUJI
```
A MUJI brand promotional video. Minimalist Japanese aesthetic. Slow, contemplative
camera movement through a pristine store. Close-ups of natural materials: wood grain,
cotton fabric texture, ceramic smoothness. No people, no text. Only products breathing
in natural light. Warm wood tones, white spaces, zen-like atmosphere. Each shot holds
for 3 seconds before gentle dissolve transition.
```
> **Efficacia:** L'assenza di persone e testo lascia che i materiali "parlino", coerente con la filosofia del brand.

### P-041. Animazione MG Profumo
```
Product advertisement combining motion graphics with perfume bottle integration. The
bottle floats and rotates in abstract space as geometric shapes pulse around it. Natural
female voiceover describes the scent. Natural lighting, no texture overlays, brisk
pacing. Gold particles stream from the bottle nozzle forming elegant calligraphic
patterns in the air.
```
> **Efficacia:** La combinazione di motion graphics con prodotto fisico crea un ibrido visivo moderno e sofisticato.

### P-042. Unboxing Premium
```
Show premium product unboxing with close-up shots, animated text highlighting features,
smooth panning to brand logos. Top-down view transitioning to 45-degree angle ending
with close-up on logo. Clean minimalist Apple-style photography with soft studio
lighting. Hands with manicured nails slowly lift lid, tissue paper rustles. Product
gleams under focused spotlight.
```
> **Efficacia:** Lo stile "Apple-like" e un ancoraggio visivo forte che comunica premium. La transizione angolare top-down -> 45 gradi e classica dell'unboxing.

### P-043. Integrazione Prodotto Lifestyle
```
Create lifestyle ad showing people using product in different daily scenarios: morning
coffee ritual with product on kitchen counter, afternoon work session with product on
desk, evening relaxation with product on nightstand. Brand colors and logo subtly visible
in each scene. Handheld documentary style, warm authentic aesthetic, 15 seconds total,
3 distinct scenes of 5 seconds each.
```
> **Efficacia:** L'integrazione in tre momenti quotidiani associa il prodotto alla routine dell'utente, tecnica pubblicitaria collaudata.

### P-044. Spot Bevanda Caffe
```
Steaming cup of premium coffee on rustic wooden table. Cream pours slowly creating
swirling patterns visible from above. Morning light streams through window creating warm
shafts of light with dust particles. Macro close-up, slow motion pour at 120fps feel.
Warm cozy aesthetic. Sound: gentle pouring, ceramic contact, satisfied sigh.
```
> **Efficacia:** Il "120fps feel" in macro sul versamento della crema e un formato ASMR-pubblicitario estremamente coinvolgente.

### P-045. Demo Prodotto Tech
```
Sleek smartphone rotates on reflective black surface. Screen lights up showing app
interface with fluid animations. Holographic UI elements appear around the device,
expanding features into floating diagrams. 360-degree orbit around product. Futuristic
premium tech style with dark background and accent lighting. Subtle particle effects
trail the rotation.
```
> **Efficacia:** Gli elementi olografici UI che emergono dal dispositivo comunicano innovazione tecnologica in modo visivamente spettacolare.

### P-046. Sfilata Moda
```
Model in long black silk dress walking down a runway. 0-4s: Side-angle tracking shot
capturing the full length of the dress flowing with movement. 4-8s: Gradual orbit
showcasing fabric sheen and texture under runway spotlights. 8-12s: Confident stride
with elegant skirt curve at the turn. 12-15s: Push to frontal close-up showing face
and jewelry details. Fashion show ambient sound with camera shutters.
```
> **Efficacia:** La struttura timeline con progressione dall'abito al volto segue l'attenzione naturale dello spettatore in una sfilata.

### P-047. Vetrina Smartphone
```
Premium phone with metallic body on gradient background. 0-3s: 360-degree rotation
showing all angles with light reflecting off polished surfaces. 3-7s: Macro shot of
side panel showing button precision and port alignment. 7-10s: Screen illuminates with
fingerprint sensor animation. 10-15s: Camera drifts into the screen where UI elements
breathe and animate organically.
```
> **Efficacia:** La transizione "dentro lo schermo" e un effetto WOW che il modello gestisce bene con la giusta formulazione.

### P-048. Macchina Caffe
```
Coffee machine on wooden table. 0-4s: Powers on with subtle LED glow, steam begins
rising from preheating. 4-8s: Macro of espresso drops creating concentric ripples in
cup. 8-12s: Steam envelops the cup in wisps, camera catches light through vapor.
12-15s: Camera drifts toward the coffee surface reflection where the machine is visible
inverted. Warm domestic lighting, product photography quality.
```
> **Efficacia:** Il riflesso della macchina nella superficie del caffe nell'inquadratura finale e un dettaglio visivo sofisticato.

---

## 5. SOCIAL MEDIA / UGC

### P-049. Vlog Fidanzata POV
```
Create a 15-second vertical (9:16) handheld vlog in natural golden-hour light. A
Taiwanese girl at the Tamsui riverbank smiles directly into camera while walking
backward. She says "Come on, the sunset's about to start!" Hair blows in the sea
breeze. She turns and points at the orange sky. Handheld phone perspective with natural
sway. Warm, ungraded look.
```
> **Efficacia:** Il formato verticale 9:16 con l'indirizzo diretto alla camera crea il formato "girlfriend POV" virale su TikTok/Reels.

### P-050. Selfie 360 Gradi Negozio Dolci
```
360-degree panoramic camera selfie. The camera rotates counterclockwise, capturing a
dessert shop interior with pastel walls, display cases of colorful macarons, and hanging
fairy lights. The person changes outfit at each 90-degree rotation: casual -> business
-> evening dress -> sportswear. Same hairstyle and face maintained throughout.
Background customers continue naturally.
```
> **Efficacia:** Il cambio outfit durante la rotazione 360 e un formato virale che testa la capacita del modello di mantenere consistenza facciale durante le trasformazioni.

### P-051. Meme Gatto Comico
```
Fast-paced video of cat knocking over objects with exaggerated reactions. Cat sits on
shelf next to vase, looks directly at owner with defiant stare, slowly pushes vase off
edge. Owner gasps. Cat immediately knocks second item. Quick cuts and sudden zoom-ins
on cat's face after each destruction. Meme aesthetic with bold expressions. Fast-paced
comedic timing.
```
> **Efficacia:** Gli zoom improvvisi sulle reazioni del gatto sono il linguaggio visivo dei meme virali che il modello replica bene.

### P-052. Montaggio Routine Mattutina
```
College student morning routine with upbeat background music. Jump cuts between scenes:
alarm clock slap, stumbling to bathroom, messy toothbrushing, burning toast, grabbing
backpack while hopping into shoe. Text overlays highlighting key moments. Jump cuts
every 2-3 seconds with mixed angles. TikTok/Instagram aesthetic, bright and energetic
style, slightly overexposed like a phone camera.
```
> **Efficacia:** I jump cut ogni 2-3 secondi con l'estetica "slightly overexposed like a phone camera" replicano perfettamente l'aspetto dei contenuti UGC organici.

### P-053. Trasformazione Prima/Dopo
```
Split-screen fitness journey transformation showing starting point and result with
dramatic reveal at end. Static framing with synchronized movements on both sides: left
side shows struggling workout, right side shows confident version of same exercise.
Light flash transition reveals final comparison. Motivational content, high contrast
inspiring style.
```
> **Efficacia:** Lo split-screen sincronizzato e il formato trasformazione sono tra i piu condivisi sui social media fitness.

### P-054. Drama Alta Societa (Vera vs Falsa Ereditiera)
```
Luxurious banquet setting. Scene 1: Fake heiress in white gown "accidentally" breaks
antique vase, cries pitifully to gain sympathy from guests. Scene 2: True heiress in
black swan gown produces DNA test document, dramatic slap across fake heiress's face in
slow motion. Scene 3: True heiress sits on ornate throne wearing crown, guests bow.
Dialogue-driven with dramatic slow motion and quick reaction cuts. Golden hour lighting.
```
> **Efficacia:** Il formato "drama breve" con ruoli archetipici (vera vs falsa ereditiera) e viralissimo sulle piattaforme cinesi e sta esplodendo globalmente.

### P-055. Storia Revenge CEO
```
Modern luxury office setting. Scene 1: Humble employee receives dismissal letter,
colleagues smirk in background. Scene 2: Six months later title card. Same employee
returns in designer suit, announces purchase of the company. Former boss turns pale.
Scene 3: New CEO sits in power chair, spins dramatically toward camera. Colleagues bow.
Power shots from below, dramatic reveals, reaction close-ups, golden hour lighting.
```
> **Efficacia:** L'arco narrativo "revenge" con power shots dal basso e un formato short drama che genera milioni di visualizzazioni.

### P-056. Gatto Arancione Gigante Meme
```
Mockumentary documentary perspective. A Godzilla-sized orange tabby cat stuck between
city skyscrapers, looking confused. Cat sneezes, blowing away hats and leaves across
city blocks. Cut to: Cat's paw resting on a bridge, blocking all traffic. Police
helicopter circles. Final: Innocent cat expression freeze-frame with documentary-style
caption. Deadpan documentary camera style with shaky zoom-ins.
```
> **Efficacia:** Lo stile "mockumentary" con camera documentaristica applicato a un soggetto assurdo crea humor sofisticato e condivisibile.

### P-057. Mirror Glitch Surreale (UGC)
```
Bathroom vlog style. Person brushing teeth normally in front of mirror. They step away
from mirror but reflection continues brushing teeth independently. Person notices,
leans back in - reflection is now ahead in the routine, gargling. Person leaves frame
entirely. Reflection "fast-forwards" through the entire morning routine, then looks
directly at camera and waves before disappearing completely. Handheld phone camera,
bathroom fluorescent lighting.
```
> **Efficacia:** Il concetto "mirror glitch" e un formato horror-leggero perfetto per i social, giocando sulla paura ancestrale del riflesso autonomo.

### P-058. Vlog Stendere i Panni
```
The girl gracefully hangs the clothes out to dry on a sunny balcony. After finishing
one piece, she takes another from the bucket and shakes it vigorously, creating small
water droplets that catch sunlight like tiny diamonds. Rhythmic, satisfying repetition.
Natural daylight, gentle breeze moves hanging fabrics. Slightly slow motion on water
droplets. Healing, peaceful domestic atmosphere.
```
> **Efficacia:** La poetizzazione di un'attivita quotidiana con slow-motion sulle gocce d'acqua crea il formato "healing content" popolarissimo in Asia.

### P-059. Album Famiglia Capodanno Lunare
```
The Year of the Horse Lunar New Year family video. Camera quickly scans through a row
of individual portrait photos. Each photo comes to life: grandmother waves, father
laughs, child makes peace sign, dog barks. Photos return to still frames. Final wide
shot shows all portraits on a wall with the family sitting beneath them in matching
red outfits. Warm festival lighting, red and gold color palette.
```
> **Efficacia:** La transizione foto-statiche-che-prendono-vita e un effetto emotivo potente per contenuti familiari celebrativi.

---

## 6. NATURA / PAESAGGIO

### P-060. Immersione Bioluminescente Abissi
```
First-person POV dive footage. A scuba diver descends into a pitch-black ocean abyss.
At first, nothing but darkness and the sound of breathing through the regulator. Then,
bioluminescent creatures begin appearing: first tiny specks like underwater stars, then
larger jellyfish with pulsing blue light, finally a massive bioluminescent whale passes
below, illuminating an underwater canyon. Pressure sounds intensify with depth.
```
> **Efficacia:** La rivelazione progressiva dal buio alla luce bioluminescente crea un arco di meraviglia crescente senza bisogno di narrazione.

### P-061. Time-Lapse Citta Giorno-Notte
```
Locked-off wide shot from a high vantage point overlooking a dense city skyline.
Accelerated time-lapse: shadows of buildings rotate clockwise as sun crosses the sky.
Golden hour bathes everything in amber. Lights begin switching on building by building.
Full night: the city becomes a grid of light. Stars appear above. Traffic creates light
trails on highways below.
```
> **Efficacia:** L'inquadratura fissa "locked-off" con time-lapse e un formato che il modello gestisce molto bene, mostrando la transizione naturale del tempo.

### P-062. POV Dashcam Cacciatore di Tempeste
```
Handheld dashcam-style footage from inside a vehicle driving toward a massive tornado
on a flat prairie. Yellow-green sky dominates the upper frame. Wind rocks the vehicle.
Debris begins crossing the road. The tornado grows larger in the windshield with each
passing second. Radio crackles with weather alerts. Driver's hands visible gripping
the steering wheel white-knuckled.
```
> **Efficacia:** La prospettiva dashcam con il cielo giallo-verde (indicatore reale di tornado) crea un'esperienza immersiva e terrificante.

### P-063. Aurora Boreale Time-Lapse
```
Locked-off wide shot, Iceland or Norway, winter. Foreground: a lone cabin with a single
amber window glowing warmly. Middle ground: snow-covered landscape perfectly still.
Sky: Aurora borealis begins as a faint green ribbon, then intensifies into curtains of
green, purple, and pink rippling across the entire sky. Stars visible through the
aurora. Absolute silence except for occasional wind.
```
> **Efficacia:** Il contrasto tra la piccola cabina calda e l'immensita dell'aurora crea una composizione emotivamente potente.

### P-064. Momento Vetta Montana
```
Documentary wide shot. A solo hiker crests a mountain ridge at dawn. Silhouette against
an orange-pink sky. Clouds fill the valley below like a sea. The hiker pauses, removes
backpack, and stands still absorbing the view. Camera holds the wide shot for 5 seconds
before slow push-in to medium shot. Wind sounds, heavy breathing that gradually calms.
```
> **Efficacia:** Il "camera holds for 5 seconds" e una scelta registica deliberata che lascia respirare il momento, creando impatto emotivo.

### P-065. Giungla Aliena
```
A team of explorers moves cautiously through a dense alien jungle. Bioluminescent plants
pulse with rhythmic light like heartbeats. Strange creatures watch from canopy shadows.
One explorer's scanner beeps rapidly. Camera follows the team from behind at ground
level, creating a sense of vulnerability. Fog rolls along the ground. Alien bird calls
echo.
```
> **Efficacia:** La camera al livello del suolo dietro il team crea vulnerabilita. I dettagli sonori specifici (scanner, richiami alieni) aggiungono profondita sensoriale.

### P-066. Battaglia Dirigibile Steampunk
```
A massive steampunk airship engages in battle above a Victorian city. Gears and pulleys
visible on the hull strain under fire. Propellers create vortices in smoke from cannon
fire. A smaller zippy craft weaves between the larger ships. Camera follows the small
craft in a continuous tracking shot. Brass, copper, and leather textures dominate.
Steam vents from hull breaches.
```
> **Efficacia:** Il tracking continuo della nave piccola tra quelle grandi crea dinamismo e scala, tecnica classica delle battaglie aeree cinematografiche.

---

## 7. ANIMAZIONE PERSONAGGI

### P-067. Speaker Professionale Avatar
```
Male in navy suit, early 30s, clean-shaven with professional haircut. Modern office
setting with urban skyline through floor-to-ceiling windows. Speaks directly to camera:
"AI is redefining the way we live and work." Lip-sync with @Audio1. Natural hand
gestures accompanying speech rhythm. Maintains eye contact. Cinematic three-point
lighting. Medium close-up, slight dolly-in during key phrase.
```
> **Efficacia:** La specificazione "lip-sync with @Audio1" attiva la sincronizzazione labiale nativa di Seedance 2.0 per contenuti parlati.

### P-068. Ragazza Cartoon Animata
```
Animated character with pink pigtails and large expressive eyes in a rainbow-colored
room filled with cute decorations. Says excitedly: "This little trick is super useful!"
Lively but fluid expressions matching vocal rhythm. Head tilts, eyes widen on emphasis
words. Hands gesture enthusiastically. Kawaii anime style with bouncy animation
principles. Bright, saturated colors.
```
> **Efficacia:** L'indicazione "expressions matching vocal rhythm" guida il modello a sincronizzare le espressioni facciali con il parlato.

### P-069. Conduttrice On-Camera
```
Female with long black hair, red lipstick, white silk blouse. Professional studio
setting with three-point lighting and clean gradient background. Speaks to camera:
"This product will transform your daily efficiency." Subtle refined gestures. Composed
posture with minimal movement. Warm, trustworthy expression. Medium shot with slight
push-in for emphasis on key message.
```
> **Efficacia:** La specificazione "subtle refined gestures" evita movimenti eccessivi che possono sembrare innaturali nei video AI-generated.

### P-070. Storico Veterano
```
Elderly man with white hair, wire-rimmed glasses, tweed jacket in a candlelit library
filled with ancient books. Reflects quietly, then speaks slowly: "A thousand years ago,
that battle changed everything..." Measured, deliberate gestures conveying wisdom and
gravitas. Camera slowly pushes in as he speaks. Warm amber candlelight flickers on his
face. Old leather and paper textures visible.
```
> **Efficacia:** Il push-in lento durante il parlato crea intimita crescente, tecnica usata nei documentari per i momenti di rivelazione.

### P-071. Supereroe Multi-Ambiente
```
Animate a superhero performing signature move across different city rooftops while
keeping costume, hairstyle, and facial features 100% consistent with @Image1. Dynamic
tracking camera follows the hero. Scene 1: Rooftop at sunset, hero lands from jump.
Scene 2: Same hero on rainy rooftop at night, lightning behind. Scene 3: Snowy rooftop
at dawn, breath visible. Same pose and power-up animation in each scene. Lock costume
colors, facial features, body proportions.
```
> **Efficacia:** L'uso di @Image1 per bloccare l'aspetto del personaggio attraverso ambienti diversi testa e sfrutta la coerenza multimodale del modello.

### P-072. Mascotte Brand in Viaggio
```
Show brand mascot character interacting with three different environments without any
changes to its color palette, expression style, or movement characteristics. Scene
transitions: Park (playful wave) -> Office (helpful gesture at desk) -> Home (relaxing
on couch). Maintain exact color palette and proportions. Cheerful, consistent animation
style throughout. 15 seconds total, 5 seconds per scene.
```
> **Efficacia:** La coerenza della mascotte attraverso contesti diversi e essenziale per il branding, e Seedance 2.0 gestisce bene questa sfida con vincoli espliciti.

### P-073. Dialogo Personaggio con Riferimenti Multipli
```
Character face references @Image1, camera movement references @Video1, pacing references
@Audio1. Modern office, professional lighting with window backlight. Character speaks
naturally with realistic lip movements, making eye contact with camera. Medium shot with
push-in during key dialogue moment. Natural skin tones, no flickering, consistent
appearance throughout.
```
> **Efficacia:** L'uso simultaneo di tre tipi di riferimento (@Image, @Video, @Audio) dimostra la capacita quad-modale di Seedance 2.0.

### P-074. Scena Passeggiata Londra XIX Secolo
```
Camera slightly pulls back and follows female lead walking on a 19th-century London
cobblestone street. She wears a long Victorian dress with bustle. A steam engine train
passes on elevated tracks behind her. Sudden wind from the train lifts her skirt
slightly, she gasps and covers it with her hands in shock. Sound effects: footsteps on
cobblestone, distant crowd chatter, steam engine whistle, fabric rustling in wind.
```
> **Efficacia:** L'interazione tra personaggio e ambiente (vento del treno -> reazione) crea un momento di realismo emergente.

---

## 8. ASTRATTO / ARTISTICO

### P-075. Attraversamento Dipinti Famosi
```
The girl breaks the fourth wall, traversing multiple worlds of famous paintings. She
steps into Monet's Water Lilies (splashes through pond), emerges into Van Gogh's Starry
Night (wind swirls her hair), walks through Vermeer's room (catches the pearl earring),
slides across Hokusai's Great Wave, dances through Klimt's golden patterns, runs through
Dali's melting landscape, pauses in Munch's Scream backdrop, sits in Hopper's diner,
finally exits through Magritte's door into reality. 15 seconds, rapid transitions.
```
> **Efficacia:** La traversata di 9 opere iconiche in 15 secondi e un tour de force visivo che testa le capacita di cambio stile rapido del modello.

### P-076. Calligrafia Neon
```
Medium shot, dark studio. A calligraphy artist sits at a backlit table with ink and
brush. Each stroke they paint glows with neon light - the wet ink luminescent. As
characters form, the light pulses and ripples. Camera slowly orbits. The completed
character radiates, casting colored shadows on the artist's face. Contrast between
traditional brush technique and futuristic glow effect.
```
> **Efficacia:** La fusione di tecnica tradizionale (calligrafia a pennello) con estetica futuristica (neon) crea un contrasto visivamente ipnotico.

### P-077. Performance Animazione Sabbia
```
Overhead locked-off shot, illuminated table surface. An artist's hands work sand into
images in continuous transformation without resets. Mountain becomes ocean becomes
city becomes forest becomes face. Each transformation flows organically into the next.
Grains of sand visible in macro detail. Warm dramatic side-lighting creates shadows
in the sand texture. Meditative pace. No cuts.
```
> **Efficacia:** La trasformazione continua senza reset e la chiave: ogni immagine fluisce nella successiva, creando un flusso ipnotico.

### P-078. Disegno Gesso Prende Vita
```
A child crouches on sunlit pavement, drawing with colorful chalk. The camera slowly
pushes in on the drawing: a flower, a butterfly, and a small house. Miyazaki-inspired
animation activates: the chalk butterfly lifts off the pavement and flutters, chalk
flower petals scatter in a drawn breeze, smoke curls from the house chimney. The child
looks up in wonder as their art comes alive. The chalk world expands beyond the
pavement edges.
```
> **Efficacia:** Il riferimento "Miyazaki-inspired" per l'animazione del gesso che prende vita stabilisce un tono di meraviglia infantile preciso.

### P-079. Esplorazione Parco Giochi Abbandonato
```
A solo urban explorer walks through an abandoned theme park at dusk. Camera follows
from behind in steady tracking. Rusted carousel horses still sway slightly in the wind.
Faded paint peels from attractions. Nature reclaims: vines through roller coaster tracks,
moss on cotton candy booth. The explorer pauses at the carousel, reaches out to touch a
horse. It creaks into slow rotation. Melancholic beauty of decay meets lingering magic.
```
> **Efficacia:** L'ossimoro "melancholic beauty of decay meets lingering magic" guida il tono emotivo del modello in modo poetico ma concreto.

### P-080. Rivelazione Prodotto Glassmorphic
```
Pure white studio environment. A perfume bottle or tech device sits centered on a
reflective surface. A frosted glass panel slowly rotates around the product, creating
refraction and distortion effects. Light passing through the glass creates rainbow
caustics on the white surface. The product is revealed in sharp focus as the glass panel
moves past. Minimal, elegant, hyper-clean aesthetic.
```
> **Efficacia:** L'effetto glassmorphic (vetro smerigliato con rifrazione) e una tendenza di design attuale che il modello riproduce con risultati premium.

### P-081. Balletto Subacqueo
```
A female dancer performs underwater in a large pool lit from below. Flowing white fabric
billows around her in slow, weightless movements. She executes a graceful spin, arms
extended, creating spiraling fabric patterns. Bubbles trail from her movements. She
breaks the surface in the final second, gasping, droplets frozen in mid-air with
backlighting creating a halo effect. Ethereal, dreamlike quality.
```
> **Efficacia:** L'ambiente subacqueo elimina la gravita, permettendo movimenti impossibili sulla terra che risultano fluidi e magici.

### P-082. Foresta Fantasy (Conversione Stile)
```
Convert a realistic forest scene into a magical fantasy environment. Bioluminescent
plants pulse with inner light. Floating golden particles drift upward like reverse rain.
Mystical fog rolls along the ground at ankle height. Tiny fairy lights weave between
ancient trees. Studio Ghibli meets Avatar aesthetic. Soft volumetric god rays penetrate
the canopy. Color palette shifts to deep teals, warm ambers, and soft violets.
```
> **Efficacia:** I due riferimenti combinati (Ghibli + Avatar) creano un'estetica ibrida unica e riconoscibile.

### P-083. Look Film Vintage Anni '60
```
Apply 1960s film aesthetic to modern urban footage. Kodachrome color science with warm
highlights and cool shadows. Film grain visible throughout. Occasional subtle light
leaks at frame edges. Vignette darkening corners. Faded highlights with reduced
saturation. Scratches and dust particles occasionally visible. Frame rate slightly
irregular to simulate hand-cranked projection.
```
> **Efficacia:** I riferimenti tecnici specifici (Kodachrome, vignettatura, grain) sono ancoraggi che il modello interpreta con alta fedelta.

---

## 9. VETRINA PRODOTTI

### P-084. Rotazione 360 Gradi Tastiera Meccanica
```
A minimalist black matte mechanical keyboard on a pure white infinite studio background,
rotating smoothly 360 degrees clockwise. RGB lighting gently breathing across the keys
in a rainbow wave pattern. Keycap text sharp and readable at all angles. Fixed macro
camera position, smooth turntable motion. Commercial product photography style with
soft high-key lighting. No noise, no reflections on background. Logo and text remain
perfectly consistent throughout rotation.
```
> **Efficacia:** La specificazione "keycap text sharp and readable" forza il modello a mantenere leggibilita del testo, spesso problematica nell'AI video.

### P-085. Orologio di Lusso Macro
```
Close-up macro shot, smooth gimbal orbit, steady motion. A matte black luxury watch on
a velvet stand rotates slowly while soft directional light reflects off the sapphire
crystal glass. The second hand moves with visible precision. Leather strap texture
visible in detail. Camera orbits 180 degrees. Dark background with single rim light
creating dramatic edge definition. Ultra-premium product photography quality.
```
> **Efficacia:** L'orbita gimbal con luce rim singola e la formula classica della fotografia di orologi di lusso.

### P-086. Showcase Commerciale con Riferimenti Multipli
```
Perform commercial-grade camera showcase of @Image1. Side structure references @Image2.
Material detail references @Image3. Camera orbits and pushes in progressively. Premium
texture quality. 4K ultra-high definition. Stable image without distortion. Consistent
lighting from all angles. No background distractions.
```
> **Efficacia:** L'uso di tre immagini di riferimento per diversi aspetti (forma, struttura, materiale) produce risultati incredibilmente fedeli al prodotto reale.

### P-087. Arco Narrativo Prodotto in 3 Atti
```
Three-act product story: Act 1 (Problem, 0-10s): Person struggling with messy cables,
frustrated expression, cluttered desk. Act 2 (Solution, 10-20s): Product introduction
with amazed reaction, hands unboxing the cable organizer, satisfied smile. Act 3
(Result, 20-30s): Clean desk, happy user working efficiently, product visible on desk.
Call-to-action final frame. Same person throughout with consistent wardrobe.
```
> **Efficacia:** La struttura problema-soluzione-risultato e il framework pubblicitario piu efficace, qui eseguito in formato short-video.

---

## 10. AZIONE / COMBATTIMENTO

### P-088. Combattimento Ravvicinato Agente
```
A short-haired female agent in tactical winter gear engages in close-quarters combat
with a mercenary at a snowy military base. She executes a spinning heel kick, connecting
with his chest armor. Impact creates snow burst from his jacket. He staggers back.
She follows with rapid palm strikes. Camera: handheld following the action at shoulder
height, slight shake on impacts. Sound: fabric swish, impact thuds, heavy breathing
in cold air.
```
> **Efficacia:** I dettagli dell'impatto fisico (snow burst dal giubbotto, stagger) rendono il combattimento tangibile e pesante.

### P-089. Inseguimento Neve Nordica
```
Realistic Nordic snowy night. A man runs fast through deep snow, tracked closely from
behind at foot level. Snow explodes from each step. His breath creates thick vapor
clouds. Behind him, wolf eyes glow in the darkness, gaining. He stumbles, recovers.
Ahead, a cabin light appears. He reaches the door, slams it shut. Wolf impacts the
door from outside. Silence. Heavy breathing.
```
> **Efficacia:** La camera a livello dei piedi durante la corsa nella neve e un angolo immersivo che amplifica la disperazione e la fatica.

### P-090. Assassino Cyberpunk
```
Cyberpunk style, game CGI quality. Dark city corner. A young assassin fights multiple
enemies with a lightsaber. She teleports between opponents, leaving afterimage trails.
Each slash creates neon light arcs that linger in the air. Enemies dissolve into digital
particles. Rain falls through holographic advertisements above. Camera: dynamic tracking
with whip-pan transitions between kills.
```
> **Efficacia:** Gli "afterimage trails" e le particelle digitali sfruttano le capacita VFX di Seedance 2.0 per effetti impossibili nel mondo reale.

### P-091. Sprint Parkour Shibuya
```
Single continuous cinematic shot in Shibuya crossing. A schoolgirl sprints at extreme
speed, weaving along crosswalks and walls. She wall-runs past a vending machine, vaults
over a taxi hood, slides under a delivery truck. Camera follows in impossible tracking
shot. 8-bit game sound effects play during acrobatic moves. Shamisen music builds
throughout. Pedestrians freeze in amazement.
```
> **Efficacia:** Il mix di suoni 8-bit con shamisen tradizionale e il formato "single continuous shot" creano un'esperienza sensoriale unica.

### P-092. Inseguimento Neon City
```
High-energy cinematic chase at night in a neon-lit city. A lone character sprints
through rain-soaked streets as police drones and headlights blur past. They vault over
a market stall, slide under a closing security gate, dodge an explosion from a crashed
vehicle. Camera tracks from slightly behind and above. Reflections of neon in every
puddle. Sirens wail in the distance.
```
> **Efficacia:** La progressione delle difficolta (vault -> slide -> dodge explosion) crea escalation di tensione cinematografica.

### P-093. Combattimento Stile AAA Game
```
They meet in the dead of night and engage in a fight. The fighting style is incredibly
flashy, the atmosphere is tense and exciting. Unreal Engine 5 visual quality. Cinematic
camera with dramatic slow-motion on key hits. Particle effects on impacts. Volumetric
fog illuminated by moonlight. Character faces remain detailed and consistent. Motion
blur on fast movements, sharp on pauses.
```
> **Efficacia:** Il riferimento "Unreal Engine 5" e un ancoraggio qualitativo potente per scene d'azione con qualita videogioco AAA.

### P-094. Scena Breakdown Specchio
```
The woman walks up to a mirror and looks at her reflection. Her expression slowly shifts
from composed to anguished. She screams, slamming both fists against the mirror. Cracks
spider-web across the glass. Her reflection fragments into dozens of pieces, each
showing a different emotion. Camera pushes in aggressively during the scream. Sound
builds from silence to overwhelming.
```
> **Efficacia:** La frammentazione dello specchio con emozioni diverse in ogni frammento e un potente dispositivo narrativo visivo.

### P-095. Azione Tattica Campo di Battaglia
```
The man from reference image 1 as the protagonist, agile and athletic, running through
a battlefield. He dodges behind concrete barriers as explosions erupt nearby. Muzzle
flashes strobe from unseen positions. He sprints across open ground, slides into cover.
Debris rains down. Camera: low angle tracking beside him, shaking with each explosion.
Dust and smoke obscure then reveal the action.
```
> **Efficacia:** L'uso dell'immagine di riferimento per il protagonista garantisce riconoscibilita durante scene caotiche con esplosioni e detriti.

### P-096. Duello Wuxia
```
An Eastern Wuxia-style duel between a grandmaster in white and a grandmaster in black
on a mountain peak above the clouds. Energy orbs form around each fighter. They clash
mid-air with martial arts strikes. Each impact creates shockwaves that disperse clouds.
The platform beneath them begins to collapse. Final move: both energy orbs merge and
explode, creating a pillar of light visible from the ground.
```
> **Efficacia:** Le convenzioni del genere Wuxia (combattimento aereo, energia qi, montagne nelle nuvole) sono ben comprese dal modello.

### P-097. Duello Epico Arti Marziali
```
A white-clad swordsman faces a straw-cloaked swordsman in a bamboo forest under heavy
rain. They stand motionless for 3 seconds. Lightning flash. They charge simultaneously.
Slow-motion weapon clash creates a shockwave that shatters bamboo stalks in all
directions. Water droplets frozen in air by the force. Camera orbits the impact point
at 180 degrees. Steel ring reverberates.
```
> **Efficacia:** Il momento di quiete prima dello scontro (3 secondi immobili) e il rallenty sull'impatto sono la firma del cinema wuxia.

### P-098. Fuga Esplosiva
```
Tactical soldier through burning industrial zone. 0-4s: Cautious advance scanning
threats with weapon raised, red emergency lights flash. 4-8s: Lateral explosion rocks
the frame, soldier ducks instinctively, debris flies past camera. 8-12s: Slow-motion
run through wall of fire, embers trailing from tactical vest. 12-15s: Emerges outside,
collapses to one knee, exhales relief. Sound: ringing ears transitioning to muffled
real-world sounds.
```
> **Efficacia:** La transizione audio "ringing ears to muffled sounds" aggiunge realismo post-esplosione che pochi generatori gestiscono bene.

### P-099. Inseguimento Citta Cyberpunk
```
Character with minor injuries runs through rainy neon streets. 0-4s: Wide tracking shot,
realistic puddle splashes reflect neon signs with each footstep. 4-9s: Slow-motion leap
over crashed vehicle, mechanical sparks from cybernetic arm activating. 9-13s: Sharp
turn into alley, camera whip-pans to follow. 13-15s: Stops, looks back with heavy
breathing, rain streaming down face. Neon illumination as only light source.
```
> **Efficacia:** I "realistic puddle splashes reflecting neon" sono un dettaglio che eleva enormemente la qualita percepita della scena.

### P-100. Duello Spadaccini nella Foresta
```
Two warriors face each other in a forest clearing at dawn. 0-5s: Static medium shot,
tension building, leaves fall slowly between them. 5-10s: Rapid clashing of swords with
realistic sparks and steel sounds, camera follows the action. 10-15s: Camera slowly
circles the victor as the defeated opponent falls. Metal impacts, realistic blood
trajectories, leaf dynamics disturbed by the combat. Morning mist parts around their
movements.
```
> **Efficacia:** La nebbia mattutina che si apre intorno ai movimenti e un dettaglio fisico che aggiunge credibilita alla scena.

### P-101. Combattimento Corpo a Corpo Futuristico
```
Two warriors in a high-tech arena with energy barriers. 0-5s: Standoff, energy charges
visible around their fists and forearms. 5-10s: High-speed exchange of blows with
electric arcs at each contact point. 10-15s: Slow-motion knockout punch, energy
discharge creates expanding sphere of light. Loser crashes through energy barrier.
Blue-purple lighting, sci-fi particle effects trail every movement.
```
> **Efficacia:** Le "electric arcs at each contact point" e lo slow-motion finale con sfera di energia creano un climax visivo spettacolare.

### P-102. Azione Aquilone Stile Bollywood
```
A Chinese youth flies a kite through crowded market streets. He leaps up stone steps,
flips over a food cart without releasing the string, lands running, dashes between
rickshaws. The kite performs impossible aerial maneuvers synchronized with his ground
parkour. Camera follows in continuous tracking shot. Style transitions mid-sequence from
realistic to slightly anime-influenced during the acrobatic peak. Upbeat traditional
instrument soundtrack.
```
> **Efficacia:** La sincronizzazione aquilone-acrobata e la transizione stilistica mid-sequence testano capacita avanzate del modello.

### P-103. Offerta Fiori a Cavallo
```
A man in orange traditional robes rides a brown horse toward a massive tree blooming
with orange flowers. Classical Chinese aesthetic with shadow puppet influence. Color
palette restricted to black, white, and orange. He dismounts, picks a branch of flowers,
offers it upward as petals scatter. Camera follows from a respectful distance, low
angle. Ink wash transitions between shots.
```
> **Efficacia:** La palette limitata (nero, bianco, arancione) e un vincolo creativo che produce risultati visivamente coerenti e stilisticamente forti.

### P-104. Scena Combattimento Boxe in Palestra
```
Gritty boxing gym, heavy bag era. Two fighters spar in a worn ring with ropes. Handheld
camera circles the ring at eye level. Sweat sprays from impact. Coach shouts instructions
from corner. Close-up on wrapped fists connecting with body. Consistent character
identity maintained through 10-second sequence. Fluorescent overhead lighting with dust
particles. Sound: leather on skin, exhaled grunts, skipping rope in background.
```
> **Efficacia:** La camera circolare a livello degli occhi immerge lo spettatore nel ring, tecnica usata nei film di boxe classici.

### P-105. Blockbuster Azione Indiana
```
Telugu action style with anti-gravity physics. Hero entrance: slow-motion walk through
explosion with debris suspended in air. Crowd combat: hero simultaneously fights 20
opponents using increasingly impossible techniques - a kicked enemy flies backward
through three walls. Vehicle destruction: hero stops a speeding truck with one hand,
it crumples like paper. Exaggerated impact effects with dramatic camera zooms on every
hit. Over-the-top heroic music swells.
```
> **Efficacia:** Lo stile Tollywood con fisica anti-gravita e un genere riconoscibile che il modello interpreta con entusiasmo.

---

## 11. FANTASY / FANTASCIENZA

### P-106. Biblioteca Magica
```
A young mage enters a colossal, enchanted library stretching upward into infinity.
Floating books drift between shelves of their own accord. Levitating tomes open,
releasing streams of golden text that swirl in the air. The mage reaches out and a
specific book flies to her hand, opening to reveal a glowing map. Dust motes sparkle
in shafts of light from impossible windows. Camera cranes upward to reveal the
infinite scale.
```
> **Efficacia:** Il crane verso l'alto che rivela la scala infinita e una tecnica epica per comunicare grandiosita in ambienti fantastici.

### P-107. Resa dei Conti Rooftop Cyberpunk
```
Two augmented warriors face off on a neon-lit rooftop in a cyberpunk city during heavy
rain. Cybernetic implants glow through their skin. Energy weapons charge with visible
electrical build-up. They clash, energy blades creating lightning arcs against the rain.
The impact shatters rooftop tiles and sends shockwaves rippling through rain puddles.
Camera orbits the fighters during the clash. City hologram advertisements flicker
in the background.
```
> **Efficacia:** La pioggia come elemento che interagisce con le armi energetiche (archi elettrici nella pioggia) aggiunge un layer fisico impressionante.

### P-108. Mech Gigante vs Drago
```
A towering mech engages in battle with a massive dragon atop a crumbling city. The
dragon breathes white-hot fire that melts building facades. The mech blocks with an
energy shield, slides back from the force. Counter-attack: mech's chest opens, firing
a concentrated energy beam. Dragon banks left, beam slices through a skyscraper behind
it. Camera: wide shot establishing scale, then close combat cuts. Debris rains
constantly.
```
> **Efficacia:** La dinamica attacco-difesa-contrattacco con danni collaterali (grattacielo tagliato) crea una coreografia di battaglia leggibile e epica.

### P-109. Citta Post-Apocalittica
```
A lone survivor sprints through a crumbling cityscape overgrown with vegetation. Vines
cover rusted vehicles. A pack of mutant creatures emerges from a collapsed subway
entrance. The survivor vaults through a broken window, rolls, keeps running. Falling
debris from a collapsing overpass forces a direction change. Camera: chase perspective
from slightly above and behind. Neon emergency signs flicker on dead buildings.
```
> **Efficacia:** L'ambiente post-apocalittico con vegetazione che riprende il controllo crea un contrasto visivo affascinante tra natura e rovina urbana.

### P-110. Samurai all'Alba
```
Two samurai face each other at the crest of a misty mountain at dawn. Cherry blossom
petals drift between them. Neither moves for 3 seconds of excruciating tension. A petal
touches the ground. Both draw simultaneously in iaijutsu flash-draw. The camera captures
the crossing of blades in extreme slow motion - every water droplet from the misty air
vibrates from the impact shockwave. One samurai sheathes his sword. The other falls.
```
> **Efficacia:** L'iajutsu (estrazione fulminea) con trigger visivo (petalo che tocca il suolo) e la quintessenza dell'estetica samurai cinematografica.

### P-111. Robot Solitario - Storytelling Multi-Shot
```
A lonely robot wakes up in an abandoned factory (Scene 1: Rust particles fall as it
powers on, single eye flickers blue). It walks outside and sees a sunset wasteland
(Scene 2: Wide shot, tiny robot silhouette against vast orange sky). It discovers a
small green flower growing through concrete (Scene 3: Macro close-up, robot's metal
finger gently touches a petal). Finally, it looks up at the sky and its eye-light forms
a smile shape (Scene 4: Medium shot, warm tones). Emotional transition from confusion
to warmth. Cinematic camera, no flicker.
```
> **Efficacia:** L'arco emotivo del robot (confusione -> scoperta -> tenerezza) crea empatia con un soggetto non umano, tecnica narrativa potentissima.

### P-112. Fiaba Farfalla
```
A magical artifact: a painted butterfly on an ancient wall begins to twitch. Its wings
peel away from the fresco surface, gaining dimension and color. It flies out of the
painting into a sunlit room, casting a realistic shadow. It circles the room, lands on
a child's outstretched finger. The child laughs. The butterfly senses footsteps
approaching, returns to the wall, and becomes flat paint again. Camera follows the
butterfly throughout in continuous tracking.
```
> **Efficacia:** La transizione 2D-pittura-to-3D-reale e ritorno e un effetto affascinante che sfrutta le capacita di Seedance 2.0.

---

## 12. CIBO / ASMR / SENSORIALE

### P-113. ASMR Skincare Macro
```
Create a vertical ASMR video with no music, focusing on macro details. A light blue
skincare gel bottle sits on a frosted glass surface. Hands with manicured nails slowly
twist open the cap. Camera pushes into extreme macro as gel is squeezed onto fingertips.
The gel glistens, catching light in slow motion. Fingers spread the gel, emphasizing
texture and friction sounds. The tactile quality of the product dominates the frame.
No background noise, only product sounds amplified.
```
> **Efficacia:** L'assenza di musica e l'amplificazione dei suoni del prodotto (apertura, gel, frizione) creano l'esperienza ASMR pura.

### P-114. ASMR Mani POV
```
A first-person ASMR video featuring hands. Close-up shots show a pair of slender hands
performing a sequence: scratching a textured wooden surface (visible scratch marks form),
rubbing velvet fabric (pile shifts direction), tapping glass with each fingernail in
sequence (visible vibration rings). Each action 3-4 seconds. Camera locked in extreme
close-up. Sound: amplified scratching, soft rubbing, crystalline tapping. No music.
```
> **Efficacia:** La sequenza di materiali diversi (legno -> velluto -> vetro) crea varieta sensoriale mantenendo il formato ASMR.

### P-115. Cucina in Miniatura
```
A miniature cooking video on a pure black background with dramatic top lighting. Tiny
real ingredients: crack a quail egg into a miniature pan (visible sizzle), flip with
tiny spatula, garnish with micro-herbs using tweezers. The finished miniature dish is
plated on a coin-sized plate. A full-sized finger enters frame for scale reference.
Camera: overhead macro, slight push-in for plating. Sound: amplified sizzle, scrape,
and sizzle of miniature cooking.
```
> **Efficacia:** Il contrasto di scala (cucina in miniatura + dito per riferimento) crea un effetto visivo virale estremamente popolare.

### P-116. Bistecca Wagyu Sizzling
```
Close-up of a wagyu steak hitting a hot cast-iron skillet. Fat renders instantly,
creating a cascade of sizzling sounds. Maillard reaction visible in real-time as the
surface browns. Butter basted with rosemary sprig - herb sizzles on contact. 2K
resolution, shallow depth of field. Steam and smoke rise. Juices pool and bubble.
Camera: locked macro, slight rack focus from surface detail to overall steak.
Final: meat thermometer inserted, reads 54 degrees C.
```
> **Efficacia:** I termini tecnici culinari (Maillard reaction, butter basting) guidano il modello verso dettagli specifici e realistici.

### P-117. Mercato Notturno Street Food
```
Handheld camera weaves through a crowded Southeast Asian night market at eye level.
Steam rises from multiple food stalls. Close-up: vendor's hands expertly fold a roti,
oil splatters in a wok, skewers turn on a grill. A couple shares noodles from a single
bowl, laughing. Camera transitions from documentary observation to intimate close-ups
of food textures. Warm tungsten lighting mixes with colored stall lights. Ambient:
sizzling, chatter, distant music, motorcycle passing.
```
> **Efficacia:** Il passaggio da osservazione documentaristica a close-up intimi crea un ritmo visivo che replica l'esperienza di camminare nel mercato.

### P-118. Whisky Macro Pour
```
Extreme macro commercial shot. A crystal whisky glass sits on a dark, textured oak
surface. Amber liquid pours in slow motion, creating thick legs on the glass interior.
A single large ice sphere cracks audibly as the whisky contacts it. Surface tension
creates a perfect meniscus. Light passes through the liquid creating warm caustic
patterns on the dark surface. Camera: locked extreme macro with slight rack focus from
ice to liquid surface. Sound: pour, ice crack, settling liquid.
```
> **Efficacia:** Il dettaglio "ice sphere cracks audibly as whisky contacts it" e un momento ASMR-premium che eleva lo spot da commerciale a sensoriale.

### P-119. Sushi Giapponese
```
Sushi spread on a polished wooden tray with miso soup steaming gently. 0-4s: Overhead
wide shot, a hand adjusts chopsticks with precise etiquette. 4-8s: Chopsticks pick up
a single piece of nigiri, pause mid-air showing rice grain detail. 8-12s: Gentle soy
sauce dip creating expanding ripples in the small dish. 12-15s: Chopsticks exit frame,
steam continues rising from miso soup. Warm natural light, traditional Japanese
restaurant ambiance.
```
> **Efficacia:** L'attenzione all'etichetta (chopstick adjustment) e al dettaglio (rice grain visible) comunicano rispetto culinario e qualita premium.

---

## 13. MUSICA / DANZA

### P-120. Ballo Latino
```
Couple performing Latin dance in tropical night setting. She wears a flowing red dress,
he wears a fitted black shirt. 0-5s: Close embrace, slow spinning together at intimate
tempo. 5-10s: Tempo increases, fast spins with her dress creating circular patterns,
dramatic leg lift and hold. 10-13s: Crossed-step footwork sequence, camera follows
feet. 13-15s: Final pose in close embrace, heavy breathing, slight smiles. Warm string
lights in background, live band barely visible.
```
> **Efficacia:** La progressione di intensita (lento -> veloce -> finale) con cambio focus (corpo -> piedi -> volti) crea un mini-spettacolo completo.

### P-121. Danza Neon Street
```
Character in black hoodie and sneakers on rainy neon-lit street. 0-3s: Warm-up
shoulder rolls and neck stretches, casual attitude. 3-7s: Explosive footwork and
vertical jumps, puddle splashes with each landing. 7-10s: Fast spin with arms extended,
water droplets creating a spiral pattern. 10-15s: Freeze pose on beat drop, held for
2 seconds, rain continues around motionless body. Camera: handheld tracking to whip
pan to slow push-in for freeze. Bass-heavy electronic music.
```
> **Efficacia:** Il freeze finale sotto la pioggia con il corpo immobile e le gocce che continuano a cadere crea un'immagine iconica.

### P-122. Danza Elettronica Cyber
```
Dancer in glowing bodysuit in abstract cyberspace environment. 0-4s: Light floating
movements, body undulates like waves of data. 4-8s: Popping and locking moves, each pop
creates ripple effects in the digital environment. 8-12s: Acrobatic jump with
mid-air split, environment distorts around them. 12-15s: Suspended in mid-air during
beat drop, environment freezes, only light particles continue moving. Neon lights
pulse with music rhythm throughout.
```
> **Efficacia:** L'interazione danzatore-ambiente (ogni pop crea effetti) fonde performer e spazio in un'esperienza visiva integrata.

### P-123. Charleston Anni '20 Club Jazz
```
Create a Charleston dance sequence in a 1920s jazz club style. A female dancer in a
gold-fringed flapper dress, sequined headband, and T-strap heels. She performs rapid
kick-steps, knee-swings, and arm swings on a polished wooden dance floor. Brass band
visible in background. Camera dynamically tracks her movement, low angle captures the
leg work, then rises to capture full body energy. Art deco interior, warm amber
spotlights, cigarette smoke haze.
```
> **Efficacia:** I dettagli di costume (fringed dress, T-strap heels) e i passi specifici (kick-steps, knee-swings) creano autenticita storica.

### P-124. Video Musicale K-Pop
```
Epic K-pop concert scene. Dramatic stage with programmed LED walls, moving platforms,
and pyrotechnic effects. A group of 4 dancers performs synchronized choreography on
the main stage. Camera: crane shot descending from above, transitions to tracking shot
along the stage edge. Audience ocean of light sticks. Confetti cannons fire on the
chorus. Costumes with holographic fabric catch stage lights. High energy throughout.
```
> **Efficacia:** Il crane shot discendente che rivela la scala dello stage e una tecnica usata nelle produzioni K-pop reali.

### P-125. Danza Ragazza con Future House
```
Beautiful girl with black wavy hair, pink crop top and yoga pants, dancing to Future
House DJ music with hip movements synchronized to beats. Camera follows music rhythm
with push-pull movements creating a pulsing visual effect. Bedroom setting with soft
colored spotlights. 9:16 aspect ratio. Natural, confident movements. Slight smile.
Hair bounces with each move.
```
> **Efficacia:** La sincronizzazione camera-musica (push-pull sui beat) crea un effetto visivo ritmico che amplifica l'energia della danza.

### P-126. Danza Vittoria con JK Skirt
```
Girl in white crop top and JK plaid skirt dancing to upbeat DJ track. Specific
movements: victory hand signs, playful hair flips, spinning with skirt flair. Bedroom
background with warm soft lighting and fairy lights. 9:16 vertical ratio, 10-second
duration. Cheerful, youthful energy. Clean makeup, natural expression.
```
> **Efficacia:** Lo stile "JK" (Japanese school) con movimenti specifici (victory signs, hair flips) e un formato viralissimo sulle piattaforme asiatiche.

### P-127. Prova Balletto Dietro le Quinte
```
Documentary-style footage inside a ballet rehearsal studio. Natural daylight through
high windows creates long shadows on wooden floor. A principal dancer marks a routine,
then runs it full out. Sweat visible on brow. Feet pound the floor, pointe shoes
scrape. Mirror reflects the movement. Camera: observational, slightly distant, then
push-in during the climax of the routine. Sound: breathing, feet, floor creaks,
distant piano from another studio.
```
> **Efficacia:** Lo stile documentaristico osservativo con suoni ambientali reali (scricchiolii, piano distante) crea autenticita e intimita.

---

## 14. COMMEDIA / MEME

### P-128. Scena Alternativa Avengers
```
Avengers Endgame big fight scene, cinematic style. Thanos suddenly freezes the battle
with the Time Stone. All heroes stuck mid-action. Thanos casually walks through the
frozen battlefield, adjusts Captain America's shield angle, moves Thor's hammer slightly
to the left, pats Spider-Man on the head. Resumes time. Everyone confused as their
attacks miss completely. Thanos sits on a rock and watches, amused.
```
> **Efficacia:** La sovversione dell'aspettativa (villain comico invece che minaccioso) in una scena epica nota crea humor attraverso il contrasto tonale.

### P-129. Documentario Lontra Pilota
```
A nature documentary scene showing an otter piloting a small propeller airplane. The
otter wears tiny aviator goggles and a leather flight cap. It adjusts miniature
instruments with webbed paws. Camera: cockpit interior shot, then external tracking
as the tiny plane flies over a river. David Attenborough-style narration tone. The
otter does a barrel roll, looks at camera with an expression of pure joy. Documentary
title card appears: "Wings Over Water: An Unexpected Journey."
```
> **Efficacia:** Il format "documentario serio su soggetto assurdo" e uno dei formati comici piu efficaci generabili con AI.

### P-130. Friends x Game of Thrones
```
The cast of Friends reimagined in a Game of Thrones-style sitcom. Ross as a nervous
Maester, Rachel as a fashionable noble, Joey as a dimwitted knight, Chandler making
sarcastic quips in a castle great hall. Monica obsessively cleaning a medieval kitchen.
Phoebe reading runes. They sit on iron thrones instead of the coffee shop couch.
Laugh track plays after each medieval mishap. Camera: multi-cam sitcom setup.
```
> **Efficacia:** Il mashup di due franchise iconiche con mapping preciso dei personaggi (Joey = cavaliere stupido) crea comicita per fan di entrambe le serie.

### P-131. Meme Fidanzato Distratto Bollywood
```
Bollywood-style recreation of the distracted boyfriend meme. The boyfriend character
performs an elaborate dance number with the "other woman" while the girlfriend character
does a dramatic Bollywood gasp with 5 camera angles. Entire street joins the dance.
Rain machine activates. Color powder thrown. Slow-motion slap sequence with 12 reaction
shots. The boyfriend snaps back to reality, girlfriend is staring daggers. Musical
score swells and cuts.
```
> **Efficacia:** L'esagerazione Bollywood del meme con 12 angoli di reazione e una parodia che amplifica l'assurdo del formato originale.

### P-132. Drama Gatto Narrativo
```
Cat drama narrative spanning 15 seconds. Scene 1: White cat sits in rain at window,
sees its partner cat with another cat through the glass. Dramatic zoom on betrayed
expression. Scene 2: Revenge transformation montage - white cat gets a makeover, learns
to play piano, becomes successful. Scene 3: Grand ballroom, white cat in elegant outfit
confronts the cheating cat. Dramatic slap with slow motion paw. White cat exits
victoriously through double doors. Korean drama OST swells.
```
> **Efficacia:** La parodia del K-drama con gatti come attori e un formato che combina il fascino dei gatti con la struttura narrativa del drama, generando massima condivisione.

### P-133. Mona Lisa Ruba la Cola
```
The Mona Lisa painting comes to life. She looks left and right nervously, then her
hand reaches out of the painting frame. She grabs a Coca-Cola bottle from a museum
display nearby. Drinks it with exaggerated satisfaction, hides the bottle behind the
frame. A cowboy from a painting next door snatches the bottle. Spotlight hits the Coke
for final hero shot. Museum guard walks past oblivious.
```
> **Efficacia:** L'antropomorfizzazione di dipinti famosi che interagiscono con prodotti moderni e un concept creativo pubblicitario virale.

---

## 15. HORROR / SUSPENSE

### P-134. Anomalia Riflesso (Template Horror 15s)
```
Bathroom mirror glitch narrative. Person enters bathroom, turns on light. 0-3s: Normal
reflection, brushes hair. 3-7s: Person pauses, reflection continues brushing with 0.5
second latency - movement desynchronized. 7-11s: Person slowly raises right hand.
Reflection raises left hand, then slowly turns its head independently while the real
person remains still. 11-15s: Person bolts, slams door. Final frame: reflection is
still standing there, looking at where the person was, then slowly turns toward the
camera. Black screen.
```
> **Efficacia:** Il desync progressivo del riflesso (ritardo -> autonomia -> confronto) costruisce orrore escalante senza effetti gore.

### P-135. Esplorazione Urbana Parco Giochi
```
A solo urban explorer enters an abandoned amusement park at twilight. Security fence
cut. Flashlight beam reveals faded clown faces on the funhouse. A Ferris wheel car
creaks and sways with no wind. Camera: POV handheld, flashlight is the only light
source. Sound: metal groaning, distant calliope music that shouldn't be playing. The
explorer turns a corner, flashlight illuminates fresh footprints in the dust leading
ahead. They weren't there before.
```
> **Efficacia:** I "fresh footprints in the dust" come ultima rivelazione sono un dettaglio horror minimale ma terrificante.

---

## 16. SPORT / RACING

### P-136. Pattinaggio Artistico Coppia
```
A live performance of competitive pairs figure skating. A low-angle camera follows the
skaters as they glide across the ice in perfect synchronization. The female skater is
lifted overhead in a one-arm hold, spinning. Ice shavings spray from sharp stops. Camera
adjusts to capture the technical elements: footwork sequences, throw jumps, death
spiral. Crowd gasps and applauds. Arena lighting creates dramatic shadows on the ice.
```
> **Efficacia:** I termini tecnici del pattinaggio (death spiral, throw jump) guidano il modello verso movimenti specifici e riconoscibili.

### P-137. Corsa Hollywoodiana Stile Le Mans
```
Structured 15-second racing sequence, Le Mans style. Interior cockpit shots with rain
hammering the windshield. Driver shouts "Let's go!" gripping the wheel. Exterior:
water spray creates rooster tail behind the car. Motion blur on background, car sharp.
Stadium lighting streaks across wet bodywork. Tire smoke mixes with rain mist. Engine
roar builds to redline. Final shot: car crosses finish line under checkered flag,
brake lights glow through spray cloud.
```
> **Efficacia:** La combinazione di shots interni/esterni con dialogo del pilota crea un mini-film di corse completo e coinvolgente.

### P-138. Atleta Sprint Realistico
```
Athletic sprinter in tracksuit with rapid powerful leg movements and pumping arms,
sprinting down a red track toward camera. Crosses finish line as crowd erupts. Tracking
shot follows runner from side angle, maintaining focus on face showing maximum effort.
24fps cinematic sports documentary style. Shallow depth of field blurs the stadium.
Sweat and breath vapor visible. Sound: feet pounding track, crowd roar building.
```
> **Efficacia:** Il 24fps e lo stile documentario sportivo con profondita di campo ridotta creano l'estetica dei documentari sportivi professionali.

---

## 17. MOMENTI INTIMI / SLICE OF LIFE

### P-139. Minimarket Notte Piovosa
```
Single continuous shot. A young woman in an oversized hoodie pushes open a convenience
store door, bell jingles. She walks past fluorescent-lit aisles, picks up instant
noodles, pauses. Puts them back. Picks up a fresh bento instead. Pays at the counter,
the clerk nods without speaking. She exits into rain, pauses under the awning to open
the bento, takes one bite. Her expression softens from exhaustion to small comfort.
Camera: follows from behind, then orbits to face her for the final moment.
```
> **Efficacia:** La scelta noodle-istantaneo-vs-bento e un micro-momento narrativo che comunica "scegliere di prendersi cura di se stessi".

### P-140. Yoga Sul Tetto all'Alba
```
A woman practices yoga alone on a high rooftop at sunrise. City skyline silhouette in
background. She flows through sun salutation: mountain pose, forward fold, plank,
upward dog, downward dog. Each pose held for a breath. Camera: wide establishing shot,
then slow arc to capture both her and the rising sun. Golden light gradually warms the
scene. Wind moves her clothes and hair. Sound: distant city awakening, her steady
breathing.
```
> **Efficacia:** La progressione del sun salutation reale con pose nominate guida il modello attraverso una sequenza fluida e anatomicamente corretta.

### P-141. Ramen Shop Tarda Notte
```
Single continuous Steadicam shot. A ramen shop at 1am, near empty. Steam rising from
a single bowl on the counter. A tired salaryman in a wrinkled suit sits down. The cook
silently places the bowl in front of him. He breaks apart chopsticks, pauses. Takes
first sip of broth. Closes eyes. His shoulders drop as tension leaves his body. Camera:
slow approach from door, settles at counter-level beside him. Warm yellow lighting,
wood textures, condensation on windows.
```
> **Efficacia:** Il momento "shoulders drop as tension leaves" e il beat emotivo centrale: un piccolo gesto che racconta un'intera giornata.

### P-142. Giornata Piovosa a Casa
```
20-year-old in oversized knit sweater curled on a couch with a book. 0-5s: Wide shot
of cozy living room, rain streaks on the window behind her, warm lamp light. 5-10s:
Camera pushes to medium shot, she turns a page, lips move slightly as she reads.
10-15s: Close-up of rain on window pane, steam rises from a cocoa mug on the side
table, her hand reaches for it. The sound of rain dominates. No music. Healing
atmosphere.
```
> **Efficacia:** L'assenza di musica lasciando solo il suono della pioggia e una scelta estetica del genere "healing" che il modello rispetta fedelmente.

### P-143. Estetica Guarigione Giapponese
```
A young woman stands under a cherry blossom tree in full bloom. Gentle breeze blowing
through her long hair. She slowly looks up at the falling petals, catching one in her
cupped hands. Medium shot slowly pushing in to face close-up. Her eyes reflect the
pink petals. She smiles softly. Soft natural lighting with golden hour warmth. Light
film grain. No music, only wind and distant temple bell.
```
> **Efficacia:** L'estetica "healing giapponese" con ciliegio, campana del tempio e film grain e un sotto-genere specifico che il modello gestisce perfettamente.

### P-144. Mani Artigiano Anziano
```
Close-up, intimate documentary-style footage. An elderly craftsman's hands work clay
on a pottery wheel. Veins and wrinkles visible in detail. His fingers shape the wet
clay with practiced precision. Water drips. The vessel takes form slowly. Camera never
shows his face, only the hands and the emerging creation. Warm natural side-light from
a workshop window. Sound: wet clay spinning, occasional satisfied hum.
```
> **Efficacia:** La scelta di non mostrare mai il volto, solo le mani, e una decisione registica potente che universalizza il soggetto.

### P-145. Riunione Aeroporto Emotiva
```
Airport reunion scene. Shot 1: Child waiting anxiously by arrivals gate, holding a
hand-drawn welcome sign, bouncing on heels. Wide shot of busy terminal. Shot 2:
Parent appears through sliding doors, freeze moment of recognition, both faces light
up. Shot 3: Slow-motion run toward each other, child drops sign. Shot 4: Embrace,
camera circles them, close-up on parent's closed eyes and tears. Swelling emotional
music synchronized with visual beats.
```
> **Efficacia:** Il "freeze moment of recognition" prima della corsa slow-motion e una tecnica emotiva cinematografica classica.

---

## 18. STORYTELLING MULTI-INQUADRATURA

### P-146. Sequenza Inseguimento Multi-Camera
```
Multi-camera chase through busy city streets. Shot 1: Wide establishing shot, target
spotted crossing intersection. Shot 2: Close-up on pursuer's determined face, starts
running. Shot 3: POV shot weaving through pedestrian crowd, people reacting. Shot 4:
Aerial drone view showing the gap closing between pursuer and target. Character
consistency maintained throughout all shots. Spatial continuity preserved. Escalating
tension in each subsequent shot. Urban daytime setting.
```
> **Efficacia:** La progressione prospettica (wide -> close -> POV -> aerea) e la coerenza spaziale tra inquadrature creano un inseguimento cinematografico credibile.

### P-147. Epica Lord of the Rings
```
Fellowship descending from snow-covered mountain pass, cloaks whipping in blizzard.
Transition to: Moria battle sequence, Gandalf faces goblins with staff glowing white,
creating shockwave that throws back attackers. Climax: Balrog bridge confrontation,
Gandalf slams staff on stone bridge with iconic pose. Freeze frame as bridge cracks.
Camera zooms out to reveal the massive scale of the underground chasm. Epic orchestral
score throughout.
```
> **Efficacia:** La struttura a tre scene iconiche con climax sul ponte e il freeze frame creano un tributo cinematografico riconoscibile.

### P-148. Paladino nella Cattedrale
```
Character in silver paladin armor fighting 20+ cultists in a gothic cathedral during a
twilight storm. Nine-panel sequence: Panel 1: Crane descends through stained glass
ceiling. Panel 2: Paladin enters through massive doors, lightning behind. Panel 3:
Cultists turn, weapons drawn. Panel 4: First clash, holy light erupts from paladin's
sword. Panel 5: Wide shot of melee. Panel 6: Paladin disarms three opponents
simultaneously. Panel 7: Boss cultist appears. Panel 8: Final duel close-up. Panel 9:
Paladin silhouette in doorway, cathedral burning behind.
```
> **Efficacia:** La griglia a 9 pannelli e una struttura di storyboard che guida il modello attraverso una progressione narrativa complessa e dettagliata.

### P-149. Confronto Due Amanti in Rosso
```
Period drama face-off at cliff edge. Shot 1: Woman in red lifts wine jug, drinks
defiantly. Orbiting camera moves to her back, then focus-shifts to reveal a woman in
black in the distance. Shot 2: Drone aerial wide shot reveals the full cliff landscape
with both figures. Shot 3: Close-up two-shot, intense staring confrontation, wind
moves hair and robes. Classical Chinese aesthetic with muted warm palette.
```
> **Efficacia:** Il cambio prospettiva (primo piano -> drone -> two-shot) con focus-shift come transizione e una tecnica registica elegante.

### P-150. Duello Video Multimodale Completo
```
Reference @Video1 for character actions and camera work. Generate @Image1 black-robed
character throwing a flying dagger in a bamboo forest. Starting angle and framing
strictly reference @Video1. After the dagger is thrown, switch to slow-motion tracking
the dagger in focus, with the black-robed character blurred in background. Bamboo
stalks split as dagger passes. Sound: whoosh, bamboo cracking, wind.
```
> **Efficacia:** L'uso simultaneo di video e immagine di riferimento con istruzioni precise di cambio focus dimostra il pieno potenziale multimodale.

---

## 19. AUDIO / LIP-SYNC

### P-151. Dialogo Multilingue Business
```
Business meeting with three languages. English speaker presents quarterly results at
head of table. Mandarin-speaking colleague responds with observations. Japanese
participant adds perspective. Phoneme-level lip-sync accuracy for each language. Modern
glass conference room with city view. Professional three-point lighting. Medium shot
with subtle push-in during key statements. Synchronized with @Audio1 timing. Natural
hand gestures appropriate to each cultural context.
```
> **Efficacia:** La specificazione "phoneme-level accuracy" per tre lingue diverse testa le capacita di lip-sync multilingue di Seedance 2.0.

### P-152. Sync Video Musicale
```
Create video using @Image1 as character reference. Natural head, eye, and subtle ear
movements. Sync facial expressions with playful music rhythm from @Audio1. Subtle body
movements hit the musical beats - head nods on downbeats, shoulders pulse on upbeats.
Match the emotional tone of the music, transitioning from chill to energetic. Dynamic
camera moves synchronized with musical intensity: slow during verse, active during chorus.
```
> **Efficacia:** La differenziazione "head nods on downbeats, shoulders on upbeats" guida una sincronizzazione musicale sofisticata.

### P-153. Integrazione Effetti Sonori
```
A wine glass sits on a marble table edge. 0-3s: Tense silence, glass vibrates slightly
from distant footsteps. 3-6s: Glass slides imperceptibly toward edge. 6-9s: Falls in
extreme slow motion, rotating, catching light. 9-12s: Impact with floor. Dual-branch
audio: Build-up of tense silence, then crisp shatter sound perfectly synced to impact
frame. 12-15s: Tinkling aftermath as shards settle, one piece spins to a stop. High-
speed macro camera with focus pull from glass to impact point to settling shards.
```
> **Efficacia:** La descrizione audio "dual-branch" con build-up e rilascio perfettamente sincronizzati all'impatto visivo crea cinema sensoriale.

---

## 20. TRASFERIMENTO STILE / VFX

### P-154. Trasformazione Cyberpunk
```
Transform daytime city street footage into neon-illuminated cyberpunk environment.
Reference @Video1 for source footage. Day transforms to night, natural light becomes
neon. Rain appears on dry surfaces. Holographic signs replace real signs. Vehicles gain
neon underglow. Puddles appear reflecting the new neon world. High contrast teal and
orange neon color grade. Maintain original camera movement and composition.
```
> **Efficacia:** La trasformazione giorno-in-notte-cyberpunk con aggiunta progressiva di elementi (pioggia, ologrammi, riflessi) e un effetto WOW.

### P-155. Conversione Stile Anime
```
Transform realistic footage into anime style while maintaining original motion and
composition. Reference @Video1 for source, @Image1 for anime style guide. Apply
cel-shading with bold outlines. Stylize expressions. Vibrant anime color palette with
clean gradients. Hair and clothing gain anime physics - slightly exaggerated motion.
Background simplifies to painted anime environments. Maintain character proportions
and movement timing from original footage.
```
> **Efficacia:** La conversione realismo-to-anime preservando il motion e la composizione originale e una delle applicazioni piu richieste di Seedance 2.0.

### P-156. Look Film Vintage
```
Apply 1960s film aesthetic to modern footage. Kodachrome color science: warm highlights,
cool shadows. Visible film grain throughout. Occasional subtle light leaks at frame
edges. Vignette darkens corners. Faded highlights with reduced saturation. Hairline
scratches and dust particles occasionally visible. Frame rate slightly irregular to
simulate hand-cranked projection. Maintain original movement and composition.
```
> **Efficacia:** I riferimenti tecnici multipli (Kodachrome, vignette, grain, light leaks) lavorano in sinergia per creare un look film credibile.

### P-157. Trasformazione Video Outfit
```
Girl in cozy house applies paint to her hands. Words appear on screen: "gray," "lake
blue," "silver-blue." She mixes the colors. Quick transition: costume transforms from
casual wear to elegant Hanfu with silver jewelry. She uses a folding fan to reveal her
face. Rembrandt lighting with visible god rays. Color palette shifts from muted to
rich. Maintain face consistency throughout transformation. Cinematic slow motion on
the fan reveal.
```
> **Efficacia:** La trasformazione outfit con "trigger visivo" (ventaglio che rivela il volto) e un formato virale su Douyin/TikTok.

### P-158. Trasformazione Ultra-HD Stile Desiderio
```
Ultra-high definition pure-desire style girl transformation video. Cinematic soft focus
opening. Clean makeup, fair complexion, bedroom setting with warm yellow lighting.
Lazy-casual styling transitioning to refined goddess look. Detailed accessories appear:
earrings, necklace, styled hair. Each transformation beat synced to music. Shallow depth
of field throughout. No blur, no ghosting, no facial distortion. Skin texture
maintained naturally.
```
> **Efficacia:** Lo stile "pure desire" (纯欲) e un'estetica virale cinese specifica che il modello conosce e interpreta fedelmente.

---

## 21. APPENDICE: BEST PRACTICES E VOCABOLARIO TECNICO

### A. Vocabolario Movimenti Camera

| Movimento | Keyword | Effetto |
|-----------|---------|---------|
| Avvicinamento | `dolly-in`, `push in` | Costruisce tensione/intimita |
| Allontanamento | `dolly-out`, `pull out` | Rivela l'ambiente |
| Carrellata | `track left/right` | Movimento orizzontale accanto al soggetto |
| Panoramica | `pan left/right` | Rotazione orizzontale in posizione |
| Gru | `crane up/down` | Movimento verticale della camera |
| Orbita | `orbit`, `360 orbit` | Cerchio intorno al soggetto |
| A mano | `handheld` | Sensazione documentario/raw con micro-shake |
| Gimbal | `gimbal` | Movimento stabilizzato e fluido |
| Dolly Zoom | `dolly zoom` | Effetto vertigo di Hitchcock |
| Whip Pan | `whip pan` | Panoramica rapida per urgenza |
| Aereo | `aerial sweep`, `drone shot` | Vista dall'alto |

### B. Dimensioni Inquadratura Consigliate

| Inquadratura | Ideale per | Movimento consigliato |
|--------------|-----------|----------------------|
| Wide | Establishing shot, panoramiche prodotto | Push-in lento o statico |
| Medium | Dialogo, contenuti UGC | Handheld o Gimbal |
| Close-up | Dettagli, emozione | Micro push-in |
| Extreme close-up | Macro, ASMR, texture | Statico o rack focus |

### C. Keyword Stile per Genere

| Genere | Keyword Consigliati |
|--------|-------------------|
| Vita quotidiana/Vlog | Healing fresh, artistic, Japanese fresh, Korean mood |
| Sci-Fi/Blockbuster | Cyberpunk, Dark premium, Retro film, Dreamy soft light |
| Minimalista | Minimalist clean, Premium texture, Realistic photography |
| Cinematografico | Cinematic texture, Film grain, Anamorphic lens flare |
| Film Noir | Film noir, Chiaroscuro lighting, High contrast |
| Anime | Anime style, Cel-shading, Studio Ghibli, Cyberpunk: Edgerunners |

### D. Keyword Audio

| Keyword | Effetto |
|---------|---------|
| `reverb` | Riverbero grandi spazi (sale, cattedrali) |
| `muffled` | Suono attutito (spazi chiusi, sott'acqua) |
| `echoing` | Effetto eco (grandi camere) |
| `metallic clink` | Suono collisione metallica |
| `crunchy` | Suoni con texture come ghiaia sotto i piedi |
| `crackling fire` | Scoppiettio del fuoco |

### E. Le 11 Best Practice Fondamentali

1. **Un verbo per inquadratura** - Verbi di movimento multipli creano confusione
2. **Limita i personaggi a 1-2** - Piu personaggi causano confusione identitaria
3. **Lunghezza prompt: 30-200 parole** - Troppo corto/lungo viene ignorato
4. **Includi sempre parole vincolo** per la consistenza
5. **Nessun prompt negativo** - Usa solo affermazioni positive
6. **Aggiungi il suffisso qualita** a ogni prompt
7. **Inizia breve, poi estendi** - Genera prima 5-10 secondi
8. **Genera varianti multiple** - Crea 2-4 varianti per confrontare
9. **Controlla i tag @** - Gli errori multi-referenza sono i piu comuni
10. **Mantieni i video di riferimento brevi** - Taglia al segmento chiave
11. **Usa "lens switch"** per transizioni multi-shot in una generazione

### F. Albero Decisionale per Re-Prompting

| Problema | Soluzione |
|----------|-----------|
| Composizione sbagliata, azione corretta | Modifica solo la riga Camera |
| Movimento troppo mosso/veloce | Scambia `handheld` con `gimbal`, imposta velocita esplicita |
| Stile/colore che deriva | Sostituisci Style con singolo ancoraggio piu forte |
| Artefatti mani/etichette/flare | Cambia parole vincolo o prova diversa dimensione inquadratura |
| Angoli multipli caotici | Cambia a "single tracking shot" |
| Face morphing | Usa immagini 2K+ con "@Image1 stays identical" |
| Jittery motion | Specifica velocita ("slow dolly-in") |
| Discontinuita scena | Blocca ambiente a un singolo riferimento |

### G. Sistema Riferimenti @ per Materiali

| Scopo | Sintassi Esempio |
|-------|-----------------|
| Impostare primo frame | `@Image1 as the first frame` |
| Riferimento movimenti camera | `Reference the camera movement from @Video1` |
| Assegnare ruoli personaggio | `The woman in @Image1 as lead; man in @Image2 as supporting` |
| Riferimento azioni | `Mimic the actions from @Video1` |
| Impostare musica di fondo | `@Audio1 as background music` |
| Estendere video | `Extend @Video1 by X seconds` |
| Sostituire elementi | `Replace [element A] in @Video1 with [element B]` |

### H. Specifiche Tecniche Seedance 2.0

- **Input multimodale:** Fino a 12 riferimenti (9 immagini + 3 video + 3 audio)
- **Sync audio-video nativo** con lip-sync in 8 lingue
- **Storyboarding automatico** da descrizioni testuali
- **Risoluzione 2K, 24-60 fps, 15-20 secondi per generazione**
- **Tasso output utilizzabile: 90%+**
- **Limiti file:** Immagini <30MB, Video 2-15s <50MB, Audio ≤15s <15MB

---

## FONTI

Questa collezione e stata compilata dalle seguenti fonti:

**Repository GitHub:**
- [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) - 1099 prompt curati
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - Collezione high-fidelity
- [gracech0322-cmd/seedance-2-prompt-library](https://github.com/gracech0322-cmd/seedance-2-prompt-library) - Framework 6 dimensioni
- [makesupday/Awesome-Seedance-2.0-Prompt-and-Examples](https://github.com/makesupday/Awesome-Seedance-2.0-Prompt-and-Examples) - Template e best practices
- [HuyLe82US/awesome-seedance-prompts](https://github.com/HuyLe82US/awesome-seedance-prompts) - Prompt featured
- [weshopai/awesome-Seedance-2.0-prompt](https://github.com/weshopai/awesome-Seedance-2.0-prompt) - Prompt cinesi e inglesi
- [seedanceprompts/seedance-prompts](https://github.com/seedanceprompts/seedance-prompts) - Aggregatore risorse
- [Anil-matcha/Seedance-2.0-API](https://github.com/Anil-matcha/Seedance-2.0-API) - Wrapper Python ufficiale
- [ai-seedance/seedance-2.0](https://github.com/ai-seedance/seedance-2.0) - Client Python ufficiale

**Guide e Blog:**
- [imagine.art - 70 Prompt Guide](https://www.imagine.art/blogs/seedance-2-0-prompt-guide)
- [wavespeed.ai - Copy-Paste Framework](https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/)
- [seaart.ai - 20+ Examples](https://www.seaart.ai/blog/seedance-2-0-prompt)
- [redreamality.com - Prompt Engineering Playbook](https://redreamality.com/blog/seedance-2-guide/)
- [atlabs.ai - Prompts Guide](https://www.atlabs.ai/blog/seedance-2-prompts-guide)
- [glbgpt.com - From Zero to Cinematic](https://www.glbgpt.com/hub/seedance-2-0-prompt-guide/)
- [nereo.io - 8 Best Anime Prompts](https://www.nereo.io/blog/seedance-2-0-prompts)

---

> **Licenza:** Questa raccolta e compilata a scopo educativo. I prompt individuali appartengono ai rispettivi autori e repository.
> I prompt sono mantenuti in inglese per massima compatibilita con Seedance 2.0, che interpreta meglio i prompt in inglese e cinese.
> Le note e la struttura organizzativa sono in italiano come richiesto.
