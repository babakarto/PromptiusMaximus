# SEEDANCE 2.0 - GUIDA COMPLETA AI PROMPT PERFETTI

> Raccolta completa di guide, tecniche, template e 100+ prompt pronti all'uso per creare video cinematografici con Seedance 2.0.

---

## INDICE

1. [Cos'e Seedance 2.0](#cose-seedance-20)
2. [Struttura del Prompt Perfetto](#struttura-del-prompt-perfetto)
3. [I 3 Framework Principali](#i-3-framework-principali)
4. [Vocabolario Camera e Shot](#vocabolario-camera-e-shot)
5. [Sistema @Reference Multimodale](#sistema-reference-multimodale)
6. [Template Copia-Incolla per Categoria](#template-copia-incolla-per-categoria)
7. [Negative Prompt e Cosa Evitare](#negative-prompt-e-cosa-evitare)
8. [Tips Avanzati e Troubleshooting](#tips-avanzati-e-troubleshooting)
9. [70+ Prompt Pronti all'Uso per Categoria](#70-prompt-pronti-alluso-per-categoria)
10. [Risorse e Link Utili](#risorse-e-link-utili)

---

# 1. COS'E SEEDANCE 2.0

Seedance 2.0 e il modello AI di generazione video di nuova generazione di ByteDance, rilasciato a febbraio 2026. E il primo modello che supporta l'input simultaneo quad-modale (immagine, video, audio, testo).

### Capacita Chiave

- **Input Multimodale**: Testo + fino a 9 immagini + 3 video + 3 tracce audio di riferimento
- **Controllo da Regista**: Movimenti camera, espressioni facciali, gesti, illuminazione, pacing tramite linguaggio naturale
- **Audio-Video Sync Nativo**: Genera video completi con audio integrato; dialoghi sincronizzati con lip-sync
- **Realismo Fisico Avanzato**: Architettura DiT con mani stabili, movimento naturale dei tessuti, gravita e collisioni accurate
- **Consistenza dei Personaggi**: Volti, abbigliamento, tipo corporeo e stile visivo restano coerenti tra angolazioni e scene
- **Risoluzione**: Fino a 1080p, durata 4-30 secondi
- **Accesso**: Attualmente tramite Jimeng/Dreamina

---

# 2. STRUTTURA DEL PROMPT PERFETTO

## Formula Base

```
SOGGETTO + AZIONE + CAMERA + SCENA + STILE + VINCOLI
```

## Anatomia in 5 Parti (Framework WaveSpeed)

| # | Elemento | Cosa Fa | Esempio |
|---|----------|---------|---------|
| 1 | **Subject** | Chi o cosa appare nella scena | "30s ceramic mug on a workbench, matte white" |
| 2 | **Action** | Cosa fa il soggetto (verbo presente, singolo) | "Steam rises as a hand slides the mug into frame" |
| 3 | **Camera** | Come vediamo la scena (shot + movimento + lente) | "Medium close-up, slow dolly-in, eye level, normal lens" |
| 4 | **Style** | L'aspetto visivo (un riferimento ancora) | "Soft morning window light, subtle film grain, muted palette" |
| 5 | **Constraints** | Cosa tenere fisso, cosa escludere, timing | "No logos, no text overlays, hold on hand steady for 2s" |

### Perche Questo Ordine Funziona

- **Subject prima** ancora il modello a un punto centrale
- **Action** e l'ancora cinetica per il movimento
- **Camera** imposta la logica di inquadratura
- **Style** aggiunge carattere senza interferire con l'azione
- **Constraints** fungono da guardrail

### Regole d'Oro

- **Lunghezza ottimale**: 100-280 parole (troppo corto = risultati vaghi, troppo lungo = diluisce il focus)
- **Un verbo di movimento per shot** — combinare due verbi crea caos
- **Il modello priorizza gli elementi che appaiono per primi** nel prompt
- **Prompt specifici > prompt vaghi**: "The tires smoke as the car drifts 90 degrees" >> "car turns"
- **Framing positivo**: Seedance risponde meglio a istruzioni affermative
  - `Detailed hands`, `Anatomically correct` → anatomia migliore
  - `Physically accurate`, `Natural motion` → movimento migliore
  - `Ultra sharp`, `Masterpiece` → qualita visiva superiore

---

# 3. I 3 FRAMEWORK PRINCIPALI

## Framework 1: Five-Segment Structure (Principianti)

**Logica**: Subject + Scene/Atmosphere + Action/Performance + Camera Movement + Style/Lighting

Ideale per video single-shot con composizioni semplici.

**Esempio - Uomo con Ombrello Rosso:**

> A serious man in a black overcoat, expression firm but tinged with melancholy. He slowly opens a red umbrella as raindrops slide along its edge. He stands on a neon-lit urban street; water splashes around him. The camera performs a slow push from a wide shot to a medium shot. Strong cinematic style, film grain, teal-orange color grading, 4K ultra HD, realistic physical simulation.

---

## Framework 2: CRAFT (Progetti Multi-Asset)

**C**ontext + **R**eference (@assets) + **A**ction + **F**raming/Timing + **T**one/Audio

Ideale quando lavori con piu riferimenti (immagini, video, audio).

**Esempio - Scena Detective Film Noir:**

> Context: 1940s film noir detective office, heavy with smoke. Reference: Character face and wardrobe strictly follow @Image1; movement pacing is based on @Video1. Action: The detective steps out of the shadows, moves to the desk, and picks up a photograph, studying it with a grave expression. Framing: Dutch Angle composition with a tracking camera shot. Tone: Tense and melancholic atmosphere, classic film grain, background music @Audio1.

---

## Framework 3: Timeline Storyboard (Narrativa Multi-Shot)

Dividi il video in segmenti temporali specifici (0-4s, 4-9s...) e descrivi cosa succede in ciascuno.

**Esempio - Duello Samurai Epico:**

> 0-4s: Wide shot. The samurai walks forward from a distance through a bamboo forest; wind ripples his clothing; morning mist fills the scene. Style: @Image1.
> 4-9s: Medium tracking shot. He draws his sword and takes his opening stance; leaves fall around him.
> 9-13s: Close-up. The blade cuts through the air; slow-motion water splashes.
> 13-15s: Whip pan. Sword flashes, Japanese-inspired epic atmosphere.

### Quale Framework Usare?

| Obiettivo | Framework |
|-----------|-----------|
| Narrativa multi-shot | Timeline Storyboard |
| Piu asset di riferimento | CRAFT |
| Singolo shot o principiante | Five-Segment Structure |

---

# 4. VOCABOLARIO CAMERA E SHOT

## Tipi di Shot

| Tipo | Uso | Note |
|------|-----|------|
| **Wide** | Stabilisce spazio e contesto | Abbina con dolly lento o camera fissa; evita pan veloci |
| **Medium** | Soggetto + contesto, dialogo | Handheld = personale; gimbal = professionale |
| **Close-up** | Dettaglio ed emozione | Push-in piccoli funzionano meglio; pan possono risultare fastidiosi |

## Tipi di Movimento

| Movimento | Effetto | Note |
|-----------|---------|------|
| **Pan** | Rotazione laterale per rivelare info | Tieni lento per evitare sbavature |
| **Tilt** | Pan up/down per rivelare verticalmente | Tilt up = grandezza; Tilt down = scoperta |
| **Dolly/Track** | Movimento fisico verso/da/lungo il soggetto | Cinematografico a qualsiasi velocita |
| **Crane** | Movimento verticale | Implica grandiosita |
| **Handheld** | Oscillazione leggera e micro-shake | Perfetto per UGC; rischioso vicino al testo |
| **Gimbal** | Movimento fluido e stabilizzato | Aspetto professionale |
| **Steadicam** | Long take fluido | Ideale per seguire personaggi |

## Shot Speciali

| Shot | Descrizione |
|------|-------------|
| **POV** | Prima persona |
| **360 orbit** | Movimento avvolgente attorno al soggetto |
| **Rack focus** | Cambio di fuoco tra primo piano e sfondo |
| **Whip pan** | Transizione dinamica velocissima |
| **Dutch angle** | Angolazione inclinata per tensione |

## Descrittori Lenti (Evita Millimetri Esatti)

| Tipo | Equivalente |
|------|-------------|
| **Wide** | 24-28mm feel |
| **Normal** | 35-50mm feel |
| **Telephoto** | 85mm+ feel |

## Velocita e Distanza

Usa scalari con distanza approssimativa:
- `slow dolly-in, 1-2 feet`
- `medium pan right`
- `fast whip pan left`

### REGOLA CRITICA
**Un verbo per shot.** Movimenti composti funzionano meglio come beat sequenziali:
> "Start: slow dolly-in. Then: gentle pan right for final 2 seconds"

---

# 5. SISTEMA @REFERENCE MULTIMODALE

## Gerarchia dei Riferimenti

| Tipo | Funzione | Priorita |
|------|----------|----------|
| **@Audio** | Lip-sync e beat matching, timing edit | Ancora ritmica |
| **@Video** | Trasferimento traiettorie di movimento e linguaggio camera | Ancora di movimento |
| **@Image** | Blocco aspetto personaggio (volto, guardaroba, stile) | Ancora visiva |

## Limiti

- Fino a **9 immagini** di riferimento
- Fino a **3 video** di riferimento
- Fino a **3 tracce audio**
- **Totale massimo: 12 asset** in un singolo prompt

## Come Usare i Riferimenti

### Generazione Base
```
@image1 as the first frame, [descrivi soggetto, azione, camera, scena]
```

### Lock Video di Riferimento
```
Reference @video1 for camera movement and shot language, [descrivi nuovo contenuto]
```

### Combinazione Multi-Modale
```
@image1 as the first frame, reference @video1 for motion,
@audio1 for rhythm and mood, [descrivi scena completa]
```

### Imitazione Movimento
```
Imitate the action of @Video1
```
> Il modello prendera il personaggio dalla tua immagine e lo fara muovere come la persona nel video, tracciando fisica e timing perfettamente.

### Editing Video
```
Replace [elemento A] in @video1 with [elemento B], [vincoli aggiuntivi]
```

### Estensione Video
```
Extend @video1 by [X] seconds, [descrivi nuovo contenuto]
```

## Best Practice per i Riferimenti

- **@Image**: Usa ritratti a mezzo busto con composizione semplice per i migliori risultati
- **Consistenza personaggio**: Aggiungi sempre "Maintain facial features and wardrobe fully consistent with @Image1"
- **Rinforzo testuale**: Ribadisci i tratti chiave nel testo anche con immagine di riferimento (es. "short silver hair", "mole under left eye")
- **Ancora visiva**: Usa sempre la stessa reference facciale (@Image1) in tutti i prompt di un progetto

---

# 6. TEMPLATE COPIA-INCOLLA PER CATEGORIA

## Template 1: UGC (Stile Phone-in-Hand)

```
Subject: [persona, fascia eta, ambientazione]

Action: [parla casualmente di X mentre fa Y]

Camera: Medium, handheld phone perspective, slight sway, eye level, normal lens feel

Style: Natural indoor light, ungraded look, light motion blur

Constraints: No captions, no snap zooms, keep hands natural, 8-10s, keep background simple
```

---

## Template 2: Product Ad (Pulito e Stabile)

```
Subject: [nome prodotto/materiale/colore]

Action: [ruota lentamente / scivola nell'inquadratura / movimento hero sottile]

Camera: Close-up to medium close-up, slow dolly-in, locked horizon, normal-to-tele feel

Style: Soft key light + gentle rim, neutral color grade, light film grain

Constraints: No logos/labels, no flares, hold final frame 2s, 6-8s total
```

---

## Template 3: Cinematico (Mood-First)

```
Subject: [personaggio o luogo]

Action: [beat specifico: aspetta, si gira, respira, entra nella luce]

Camera: Wide establishing for 2s then slow push to medium, gimbal-smooth, eye level

Style: [singolo riferimento ancora, es. "overcast natural light, muted blues"]

Constraints: No Dutch angles, no crowd, no neon, maintain overcast look, 10-12s
```

---

## Template 4: Talking Head (Stabile e Leggibile)

```
Subject: [descrizione speaker]

Action: [pronuncia una frase chiara]

Camera: Medium close-up, locked tripod or very subtle dolly-in, eye level

Style: Soft key from 45deg, clean background separation, neutral grade

Constraints: No auto captions, no whip pans, skin tones natural, 12-15s, keep eyeline centered
```

---

## Template 5: Montage (Beat Rapidi Senza Caos)

```
Subject: [tema, es. "morning coffee ritual"]

Action: Beat 1 [wide contesto], Beat 2 [close-up mani], Beat 3 [dettaglio vapore], Beat 4 [sorso]

Camera: Each beat 2s, clear shot size per beat, no compound moves: transitions by cut

Style: Consistent light and palette across beats

Constraints: No text overlays, no speed ramps, keep tempo steady, 8-10s total
```

---

## Template 6: Rotazione Prodotto 360 (E-commerce)

```
Subject: [prodotto] on a pure white infinite studio background

Action: rotating smoothly 360 degrees clockwise. [dettagli specifici del prodotto visibili]

Camera: Fixed macro camera, smooth turntable motion

Style: commercial product photography style, soft high-key lighting, no noise

Constraints: Logo and text remain perfectly consistent. No flicker.
```

---

## Template 7: Music Video Beat Sync (Audio Driven)

```
Subject: [personaggio] dancing in [ambientazione]

Action: Every strong beat triggers a cut or speed-ramped camera move.
[dettagli specifici dell'ambientazione]

Camera: [stile specifico], fast-paced editing, multi-shot continuity

Style: [stile visivo], neon reflections

Constraints: Dance movements and character appearance remain consistent.
Reference: @Audio1 for beat sync + @Video1 for dance reference
```

---

## Template 8: Digital Avatar / Explainer

```
Subject: [descrizione persona/avatar, abbigliamento, eta]

Action: [pausa, respira, inizia a parlare: "FRASE"]. Lip-sync aligns with @Audio1.
[gesti naturali che accompagnano il discorso]

Camera: Frontal medium shot, gentle push-in

Style: [illuminazione], [tono colore], [atmosfera]

Constraints: Consistent eye contact with camera. Expressions follow speech flow
without feeling mechanical or repetitive. 12-15s.
```

---

# 7. NEGATIVE PROMPT E COSA EVITARE

## Checklist Negative Prompt

### Rumore Visivo da Bannare
- No text overlays, watermarks, floating UI, lens flares (a meno che specificato)

### Prevenzione Drift Identita
- No extra characters, crowds, mirrors reflecting others

### Controllo Caos Camera
- No snap zooms, whip pans, Dutch angles, jump cuts (a meno che voluti)

### Prevenzione Artefatti Corporei
- No extra fingers, deformed hands, warped handles, melting edges

### Branding
- No logos, labels, recognizable brands

### Colore/Grading
- No neon lighting, heavy teal/orange, cartoon saturation (a meno che voluti)

### Ambiente
- No rain/fog/smoke (a meno che specificato), confetti, dust particles

### Audio/Testo
- Ban auto captions se aggiungi voiceover in post-produzione

### Nota Strategica
Usa **3-5 negative per prompt**. Troppi ban rendono l'immagine piatta. Se gli artefatti persistono dopo due tentativi, modifica il testo del soggetto o semplifica le note camera piuttosto che aggiungere piu vincoli.

---

# 8. TIPS AVANZATI E TROUBLESHOOTING

## Tips di Scrittura

### Fisicita e Peso
Piuttosto che "car turns", specifica:
> "The tires smoke as the car drifts 90 degrees."

Questo dice all'AI di calcolare attrito e forza, producendo risultati realistici in 2K.

### Audio Nativo
Includi terminologia specifica per il suono: "reverb", "muffled", "high-pitched" per attivare il motore audio nativo.
> "metallic clink of a coin" genera un suono sharp sincronizzato con la vibrazione visiva.

### Illuminazione
Specifica la qualita della luce: "God rays", "Volumetric fog", "Cyberpunk neon" — calcolano il rimbalzo della luce sulle superfici. Indica sempre se la luce e "soft", "harsh" o "flickering".

### Timestamps per il Pacing
Quando la scena ha piu momenti, i timestamp danno molto piu controllo:
> 00:00-00:04 – Wide Tracking Shot: [descrizione]
> 00:04-00:07 – Cockpit / Tight Action Shot: [descrizione]
> 00:07-00:10 – Epic Pull-Back: [descrizione]

## Troubleshooting

### Problema: Break di Consistenza Personaggio
**Soluzione:** Aggiungi vincolo: "Keep the same character, same clothing, same hairstyle, no face changes, no flicker, high consistency."

### Problema: Distorsione Mani e Testo
**Soluzioni:**
- Evita close-up veloci delle mani
- Usa testo piu grande e centrato
- Aggiungi: "hands with perfect anatomy, text clear and readable"

### Problema: Artefatti di Movimento
**Soluzioni:**
- Cambia "fast" in "medium speed"
- Usa video reference per bloccare il movimento

### Problema: Troppa Casualita
**Soluzioni:**
- Carica piu riferimenti
- Abbassa le impostazioni di creativita
- Aggiungi piu vincoli nel prompt

### Problema: Video Lunghi
**Soluzione:** Genera clip perfette da 5-10s, poi usa la funzione di estensione video per continuare.

## Albero Decisionale per Re-Prompting

| Problema | Azione |
|----------|--------|
| Inquadratura sbagliata, azione OK | Re-prompt: sistema prima Camera. Tieni Subject e Action identici |
| Movimento troppo tremolante/veloce | Re-prompt: scambia "handheld" con "gimbal", imposta velocita |
| Drift stile/colore, movimento OK | Re-prompt: sostituisci la riga Style con un'ancora piu forte, rimuovi aggettivi |
| Soggetto che muta (persone/oggetti extra) dopo 2 tentativi | Cambia reference: semplifica Subject con meno descrittori |
| Artefatti ripetuti dopo 3 tentativi | Cambia vincoli o piano shot; considera di allontanarti dal close-up |

**Gestione tempo**: Dai 2 re-prompt rapidi (sotto 5 minuti totali). Se continui a correggere lo stesso errore, cambia la reference o il tipo di shot.

---

# 9. 70+ PROMPT PRONTI ALL'USO PER CATEGORIA

---

## CATEGORIA 1: Cinematico - Narrativa e Dramma

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

## CATEGORIA 2: Azione, Combattimento e Inseguimenti

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

### 16. Mirror Breakdown Scene (con @Reference)
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

## CATEGORIA 3: Sport, Corse e Arti Marziali

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

## CATEGORIA 4: ASMR, Macro e Sensoriale

### 28. ASMR Skincare Macro
> Create a vertical ASMR video with no music, focusing on macro details. A light blue skincare gel bottle sits on glass. A pale, elegant hand gently taps the glass, producing crisp fingernail tapping sounds. The hand picks up the bottle and slowly twists the cap, with the rotation sound clearly audible. A spoon scoops a portion of gel and drops it onto the glass with a soft 'plop,' showing dense gel with tiny air bubbles. Dramatic cool lighting from behind makes the gel glow like a gemstone.

### 29. Hands ASMR POV
> A first-person ASMR video featuring hands. Close-up shots show a pair of slender hands gently interacting with different objects in sequence: scratching frosted glass, rubbing plush fabric, tapping an acrylic board, squeezing bubble wrap, and brushing a wooden comb. The finger movements are slow and gentle, and the trigger sounds are purely natural with no background music.

### 30. Miniature Cooking Sequence
> A miniature cooking video on a pure black background with dramatic top lighting. Show full-sized hands carefully placing a tiny cutting board and a fingernail-sized knife. Use elegant classical music as background. The hands slice a tiny garlic clove precisely, add a micro drop of olive oil to a mini frying pan over a tea candle, and crack a small quail egg into the pan. Use a tiny spatula to nudge the egg, then plate a miniature sunny-side-up egg with a slice of garlic mushroom and a tiny scallion garnish on a coin.

### 31. Sizzling Wagyu Steak
> Close-up of a wagyu steak hitting a hot cast-iron skillet. You can see the fat rendering and bubbles of oil. 2K resolution, shallow depth of field. Sound of loud, aggressive sizzling.

---

## CATEGORIA 5: Commerciale e Prodotto

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

## CATEGORIA 6: Lifestyle, Cultura e Personaggi

### 40. Girlfriend POV Vlog
> Create a 15-second vertical (9:16) handheld vlog in natural golden-hour light, with film grain and slight camera shake. Protagonist: A Taiwanese girl with long, slightly curled hair, wearing a soft knit cardigan. Scene: Taipei Tamsui riverbank at sunset. Shot 1: She walks quickly, looking back pretending to be annoyed. Shot 2: She stops, shows the golden sunset, smiling. Shot 3: She holds ice cream to the camera, licks it, giggles as some lands on her nose.

### 41. 1920s Jazz Club Charleston
> Create a Charleston dance sequence in a 1920s jazz club style. A female dancer in a gold-fringed dress and a male dancer in a striped suit perform rapid, syncopated steps, aerial tosses, and large arm swings. The camera tracks dynamically, with close-ups on feet to show fringe movement and sweat details. Smoky atmosphere and vintage film grain.

### 42. Lunar New Year Family Album
> The Year of the Horse Lunar New Year family video quickly scans through individual family photos, like flipping through an album. Each photo 'comes to life' the moment the lens passes: grandparents, parents, and children perform unique actions with micro-expressions. Different figures are seamlessly connected through rapid panning. Red lanterns and Spring Festival couplets dynamically light up, converging into a lively family portrait.

---

## CATEGORIA 7: Creativo, Multi-Reference e Workflow R2V

### 43. Traversing Famous Paintings
> @Image 1 The girl breaks the fourth wall, traversing multiple worlds of famous paintings while retaining realistic textures. She stands under the rotating starry sky in @Image 2; watches the couple embracing in @Image 3; takes a selfie with the Girl with a Pearl Earring in @Image 4; enters @Image 5 and passes between two samurai; makes faces with @Image 6; the Mona Lisa in @Image 7 pats her head; she exchanges greetings with the woman in @Image 8; paints with Van Gogh in @Image 9; finally turns to the camera and smiles sweetly. High contrast, cinematic quality, smooth transitions.

### 44. Healing Storyboard Video
> Refer to the storyboard of @Image 1, including its shot composition, framing, camera movement, visuals, and text. The characters are @Image 2, the scenes are @Image 3, and the props are @Image 4. Create a 15-second healing video.

---

## CATEGORIA 8: Commedia e Concept

### 45. Avengers Alternate Scene
> Avengers Endgame big fight scene, cinematic style. Thanos suddenly freezes the battle and holds up his hands, looking genuinely apologetic. The superheroes pause, looking surprised, and slowly start to nod and walk away, accepting his apology. Then Spider-Man shouts, 'Oh no, he literally killed a bajillion people!' Everyone immediately turns back and rushes at Thanos, comically tackling and kicking him. Add expressive facial reactions, dynamic poses, and humorous timing.

### 46. Otter Pilot Documentary
> A nature documentary scene showing an otter piloting a small airplane. The otter wears aviator goggles and a tiny scarf, paws on the controls, looking focused yet playful. Camera follows from a dynamic low-angle tracking shot over rivers, forests, and mountains. Style: vibrant, slightly whimsical, photorealistic with cinematic framing.

### 47. Friends x Game of Thrones
> The cast of Friends in a Game of Thrones-style sitcom. Chandler as King Joffrey wearing a crown, acting dramatically spoiled. Joey as the Hand, in medieval attire, looking confused but loyal. Camera alternates between wide shots of the throne room and medium shots of expressions. Style: vibrant, humorous, sitcom-meets-fantasy aesthetic.

---

## CATEGORIA 9: Fantasy e Sci-Fi

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

## CATEGORIA 10: Momenti Quieti e Slice of Life

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

## CATEGORIA 11: Natura, Paesaggi e Meteo

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

## CATEGORIA 12: Artigianato, Arte e Performance dal Vivo

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

## CATEGORIA 13: Magia, Meraviglia e Trasformazione

### 70. Children's Chalk Drawing Comes to Life
> A child crouches on a sunlit pavement, drawing with chalk. Camera slowly pushes in on the drawing. The chalk lines shimmer and lift off the ground, animating: the dog wags its tail, birds take flight, the house glows. The child sits back, delighted. Camera pulls to wide overhead shot showing the chalk world fully surrounding her. Style: warm, soft Miyazaki-inspired palette. Light orchestral music builds.

### 71. Abandoned Theme Park Exploration
> A solo urban explorer walks through an abandoned theme park at dusk. Camera follows from behind at medium distance - steadicam, slow and steady. Overgrown carousel. He stops. Camera circles slowly. A rusted seat sways in the wind. Close-up: peeling paint, a child's handprint fossilized in grime. Wide: full park stretches behind, roller coaster sagging in distance. Low ambient drone. No dialogue.

### 72. Glassmorphic Product Reveal
> Pure white studio. A perfume bottle or tech device sits centered on a frosted glass plinth. Camera begins tight - extreme close-up on product surface. Slow rotation begins. Camera eases back in smooth dolly-out. Light refracts through product, casting shifting color halos. Final shot: product fully revealed, centered, rotating slowly. Camera locks. No music - single low ambient tone. No text, labels, or voiceover.

---

## CATEGORIA 14: Cibo, Bevande e Cultura Urbana

### 73. Street Food Night Market
> Handheld camera weaves through a crowded Southeast Asian night market. Golden light from hanging bulbs reflects off wet pavement. Tight tracking shots between stalls: a wok erupts in flame, skewers char on grill, a vendor's hands fold a banana leaf around sticky rice. Medium shot: young couple shares noodles at a plastic table, steam rising between them. Camera pulls back to wide shot of the whole market. No narration. Only ambient sound.

### 74. Whisky Macro Pour
> Extreme macro commercial shot. A crystal whisky glass on dark textured surface. A slow pour from above: amber liquid streams into the glass, splashing in extreme slow motion. Droplets hang in the air catching backlight. Liquid settles, sloshing against crystal walls, tiny bubbles forming. Camera eases back to reveal full glass and bottle. Warm amber and brown color grade. Deep, low ambient hum. No voiceover.

---

## CATEGORIA 15: Trailer Cinematografici (da SeaArt)

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

## CATEGORIA 16: Danza

### 80. Latin Dance
> A Latin dance couple in a nocturnal tropical setting - she in a red dress, he in black shirt. 0-5s: Close spin at slow tempo; dress flows softly. 5-10s: Rhythm of @Audio1 intensifies - fast spins, leg lift, exchange of glances. 10-13s: Crossed-step sequence at denser beat. 13-15s: Musical pause and final pose in embrace. Camera transitions from circular medium shot to gradual close-up.

### 81. Neon Street Dance
> A street dancer based on @Image1, black hoodie, rainy night street lit by neon. Blurred crowd, wet ground reflecting lights. 0-3s: Subtle warm-up, shoulders following beat. 3-7s: Beat from @Audio1 drops - footwork and jumps. 7-10s: Rhythm intensifies, fast spin and landing. 10-15s: On beat drop, final freeze. Camera: handheld tracking → whip pan on accents → slow push for closing. Color particles burst on beat hits.

### 82. Cyber Electronic Dance
> A dancer floats in cyberspace environment, movements synced to @Audio1 electronic beats. 0-4s: Light floating; body vibrates with low frequencies. 4-8s: Beat starts - segmented popping moves. 8-12s: Acrobatic jump on heavy hit. 12-15s: Suspended in air during beat drop. Quick camera cuts with whip pans on accents. Neon lights pulse with rhythm, particle explosions accompany music.

---

## CATEGORIA 17: Avatar Digitali / Explainer

### 83. Professional Speaker
> A male speaker in his early 30s, navy suit, clean short hairstyle. Frontal medium shot, modern glass-wall office, softly blurred urban skyline. Gentle push-in. He pauses, takes soft breath, begins to speak: "AI is redefining the way we live." Lip-sync aligns with @Audio1. Hands accompany speech with natural gestures; occasional nod or slight smile. Consistent eye contact. Soft cinematic lighting, warm neutral tones.

### 84. Animated Cartoon Girl
> Cartoon-style girl with pink pigtails and large round eyes in rainbow-colored animated room. Medium shot with slight camera sway. She blinks, leans forward, says with enthusiasm: "This little trick is super useful!" Lip-sync with @Audio1. Lively expressions, gestures shifting with vocal rhythm. Warm, bright, saturated lighting.

### 85. On-Camera Host
> Polished host with long straight black hair, red lip makeup, white blouse. Medium-close frontal shot, high-end studio. Three-point lighting. Camera advances slowly. She begins: "This product will transform your daily efficiency." Precise lip-sync with @Audio1. Subtle, refined gestures. Firm eye contact. Premium aesthetic.

### 86. Veteran Historian
> Elderly historian with white hair, round glasses, gray sweater. Medium shot in ancient library, flickering candlelight. Camera slowly moves in. He looks down in reflection, raises eyes: "A thousand years ago, that battle..." Lip-sync with @Audio1. Measured gestures, occasional nod. Wisdom and calm. Warm tones, subtle cinematic grain.

---

## CATEGORIA 18: Featured Prompt dalla Community (GitHub)

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

## CATEGORIA 19: Multi-Shot Storytelling

### 91. Robot Story (4 Scene)
> A lonely robot wakes up in an abandoned factory (Scene 1). It walks outside and sees a sunset wasteland (Scene 2). It discovers a small flower and gently touches it (Scene 3). Finally, it looks up and smiles at the sky (Scene 4). Keep robot appearance consistent. Emotional transition from confusion to warmth. Cinematic camera, warm tones, epic mood, no flicker.

### 92. Anime Girl Healing Entrance
> An 18-year-old Japanese anime girl with short hair, wearing a white dress and straw hat, standing on a forest path in warm summer afternoon sunlight. She slowly turns toward the camera and smiles gently. A light breeze moves her hair and dress. Camera slowly pushes in from medium shot to close-up. Soft natural lighting, film grain, healing and peaceful mood, cinematic quality. Maintain face and clothing consistency, no distortion, high detail.

### 93. Action Fight Scene (Wuxia + Reference)
> A wuxia-style male hero (based on reference video character), wearing black martial outfit, fighting enemies in a rainy bamboo forest at night. Fast sword combos with visible sword light trails and splashing water. Fast follow camera, crane shots, and quick close-ups. Cinematic camera language. Maintain character appearance and clothing consistency. Realistic physics, wet fabric, rain interaction.

---

# 10. RISORSE E LINK UTILI

## Guide Complete Online

| Risorsa | Link |
|---------|------|
| Imagine.art - 70 Prompt | https://www.imagine.art/blogs/seedance-2-0-prompt-guide |
| SeaArt - 20+ Esempi | https://www.seaart.ai/blog/seedance-2-0-prompt |
| GLBGPT - Da Zero a Cinematico | https://www.glbgpt.com/hub/seedance-2-0-prompt-guide/ |
| WeShop - Master Prompt Script | https://www.weshop.ai/blog/seedance-2-0-guide-how-to-master-the-prompt-script/ |
| Freepik - Come Scrivere Prompt | https://www.freepik.com/blog/how-to-write-prompts-for-seedance-2-0/ |
| WaveSpeed - Template Framework | https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/ |
| Vmake - 10 Prompt Multi-Shot | https://vmake.ai/blog/seedance-2-0-prompts |
| Atlabs - Guida 2026 | https://www.atlabs.ai/blog/seedance-2-prompts-guide |
| VideoWeb - Tutorial + Prompt | https://videoweb.ai/blog/detail/Seedance-2-0-Video-Generation-Guide-Tutorial-Prompts-578fb91b8f46/ |

## Repository GitHub

| Repo | Link | Prompt |
|------|------|--------|
| awesome-seedance-2-prompts | https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts | 1078+ prompt |
| awesome-seedance | https://github.com/ZeroLu/awesome-seedance | Raccolta curata |

## Gallery Interattive

| Piattaforma | Link |
|-------------|------|
| YouMind Gallery (video playback) | https://youmind.com/en-US/seedance-2-0-prompts |
| Seedance 2 Prompt Gallery | https://seedance2prompt.org/ |

## Piattaforme di Accesso

- **Jimeng / Dreamina** (piattaforma ufficiale ByteDance): accesso diretto a Seedance 2.0
- **SeaArt AI**: integra modelli video avanzati incluso Kling 3.0 e Wan 2.6

---

# CHEAT SHEET RAPIDO

```
FORMULA PROMPT PERFETTO:
Subject + Action + Camera + Scene + Style + Constraints

LUNGHEZZA: 100-280 parole
UN VERBO PER SHOT
SOGGETTO PRIMA DI TUTTO
POSITIVO > NEGATIVO ("detailed hands" non "no bad hands")
3-5 NEGATIVE MASSIMO
TIMESTAMPS PER MULTI-BEAT

REFERENCE:
@Audio = ritmo e lip-sync
@Video = movimento e camera
@Image = aspetto personaggio
Max: 9 img + 3 video + 3 audio = 12 totali

CAMERA VOCABULARY:
Wide = contesto | Medium = dialogo | Close = emozione
Dolly = cinematografico | Handheld = personale | Gimbal = professionale
Pan lento | Un movimento per shot | Lente: wide/normal/tele
```

---

---

# APPENDICE A: VIDEO TUTORIAL - Character Consistency Secrets (DeepWhite)

> **Video**: [Seedance 2.0 Advanced: Character Consistency Secrets + 3 Ideas & Prompt Templates](https://www.youtube.com/watch?v=I5xk9QiP7QM)
> **Autore**: DeepWhite

## Le 3 Lezioni Chiave

### 1. Le Reference Immagini Sono Fondamentali
- Caricare o meno un'immagine di riferimento ha un **impatto enorme** sul risultato
- Una singola foto frontale viene riconosciuta, ma le caratteristiche facciali non sono sempre mantenute al 100%

### 2. Usa le 4 Viste del Personaggio (Four Views)
- Caricare **4 viste del personaggio su sfondo bianco** (fronte, retro, lato, close-up) fa fare un **salto qualitativo** alla consistenza
- Il personaggio diventa identico all'immagine di riferimento
- Le espressioni dinamiche e gli storyboard risultano perfetti
- Anche 3 viste funzionano, ma 4 sono raccomandate

### 3. Prompt Dettagliati per Controllo Totale
- Il modello e talmente potente che anche keyword semplici producono buoni risultati
- Ma se hai un'idea precisa in mente, i prompt dettagliati permettono di esprimere la tua visione con precisione
- Con prompt dettagliati + four views = il video segue perfettamente la tua idea

## I 3 Metodi di Produzione

Tutti e tre partono dalla base delle **4 viste del personaggio su sfondo bianco**.

### Metodo 1: Singola Immagine (First Frame) + Prompt

1. Pensa alla storia e alla trama
2. Determina lo stile (fotorealistico, anime, cartoon, ecc.)
3. Genera o trova un'immagine che rappresenta la prima inquadratura
4. Scrivi il prompt dettagliato usando un template
5. Carica le 4 viste del personaggio + la first frame
6. **IMPORTANTE**: Dopo il caricamento, verifica che l'ordine delle immagini (@Image1, @Image2...) corrisponda a quello nel prompt

**Quando usarlo**: Buono per la maggior parte delle situazioni

### Metodo 2: Storyboard a 4 Griglie + Prompt

1. Crea uno storyboard con 4 pannelli che mostrano le scene chiave
2. Combina con il template dei prompt
3. Carica le 4 viste + lo storyboard
4. Scrivi una descrizione generale della storia

**Quando usarlo**: Ideale per scene con molti cambi, scene di battaglia, scene intense. Per drammi emotivi o letterari, puo risultare "troppo".

**Durata consigliata**: 10 o 15 secondi (meno non vale la pena con lo storyboard)

### Metodo 3: Approccio Multimodale

1. Parti dalle reference del personaggio (4 viste)
2. Aggiungi opzionalmente: diagramma scena, musica, voce, ecc.
3. Usa il template prompt multimodale
4. La reference del personaggio e obbligatoria; la scena puo essere solo descritta via keyword

**Quando usarlo**: Quando vuoi il massimo controllo su tutti gli aspetti (visivo, audio, movimento)

## Note Importanti da DeepWhite

- **Jimeng/Dreamina e il piu veloce** per la generazione
- Il template dei prompt e basato sul **manuale utente ufficiale di Jimeng 2.0**
- Per generare le 4 viste del personaggio, si puo usare un generatore di immagini AI
- **Attenzione all'ordine delle immagini** caricate: devono corrispondere ai tag @Image1, @Image2, ecc. nel prompt

---

# APPENDICE B: VIDEO TUTORIAL - 10 Viral Prompt Testati (Dom the AI Tutor)

> **Video**: [I Tested 10 BRUTAL Viral Seedance 2.0 Prompts!](https://www.youtube.com/watch?v=KnyrIp9qRuU)
> **Autore**: Dom the AI Tutor | Tech Tutor Zones

## Lezioni dai Test

### Setup Consigliato
- Modello: **Seedance 2.0** (non la versione "fast" — piu qualita)
- Durata: **15 secondi**
- Formato: **16:9**
- Limite prompt: fino a **5.000 caratteri**

### Test 1: Multi-Shot Text-to-Video
- Prompt complesso con transizioni multiple
- Le transizioni tra scene sono estremamente fluide
- Confronto con Veo 3.1: Seedance vince nettamente

### Test 2: Transformer (Bus che si Trasforma)
- Prompt di trasformazione veicolo → robot
- Risultato divertente e convincente

### Test 3: Omni Reference (Immagine + Video)
- Caricata un'immagine di una creatura come reference
- Usato un video come reference per il movimento
- **Prompt semplice**: "Image one doing the same as video one"
- **Risultato**: Consistenza eccellente del personaggio, spada dal video replicata perfettamente
- La consistenza delle caratteristiche facciali e il dettaglio della spada sono "top-notch"

### Test 4: Image-to-Video con Prima Inquadratura
- Usata un'immagine di bassa qualita come first frame
- **Prompt**: "A cinematic and chaotic tracking shot with handheld camera motion and camera shakes"
- Il risultato migliora l'immagine originale e produce un video impressionante

### Test 5: Omni Reference Anime
- Due immagini anime + un video di danza come reference
- **Prompt**: "Create a two model frame video where @Image1 and @Image2 dance and move completely the same as in @Video1"
- I personaggi anime replicano i movimenti del video di riferimento

### Test 6: Realismo + Reference di Movimento
- Stessa tecnica ma con persona realistica
- Aggiunta azione specifica alla fine ("she does a split")
- Il modello esegue sia i movimenti di riferimento che l'azione aggiunta

### Test 7: Emozioni in Multi-Shot (Text-to-Video)
- Test delle espressioni facciali e movimenti di camera
- Le emozioni sono incredibilmente realistiche
- **Mani perfette**: tutti i dettagli delle dita sono corretti
- Il motion e fantastico

### Test 8: Scena di Battaglia Complessa
- Prompt di quasi **3.000 caratteri**
- Specificato "without cuts" → risultato senza tagli, transizione continua della camera
- L'astronave appare in modo cinematografico

### Test 9: Trasformazione Aereo → Transformer
- Atterraggio aereo + trasformazione in transformer
- Risultato "brutale" e convincente

### Test 10: First Frame + Last Frame
- Usati primo e ultimo fotogramma
- La consistenza del personaggio tra i due frame e eccellente

### Bonus: Cat Kung Fu (Viral)
- Prompt text-to-video di gatti che combattono kung fu
- Confronto tra modelli:
  - **Seedance 2.0**: MIGLIORE in assoluto
  - **Kling 3.0**: Buono, ma non al livello di Seedance
  - **Grok**: Meglio di Veo, peggio di Seedance
  - **Sora**: Risultati mediocri, slow motion non richiesto
  - **Veo 3.1**: Il peggiore nel confronto

## Classifica Modelli (dal video)

1. **Seedance 2.0** — Il migliore
2. **Kling 3.0** — Buono
3. **Grok** — Discreto
4. **Sora** — Mediocre
5. **Veo 3.1** — Il peggiore (sorprendentemente)

## Piattaforma Usata
- **LumaFlow AI**: Ha Seedance 2.0 disponibile globalmente + tutti gli altri modelli video/immagine in un unico posto

---

> Documento compilato il 24 Marzo 2026 da 9 fonti web + 2 video YouTube.
> Fonti: Imagine.art, SeaArt, GLBGPT, WeShop, WaveSpeed, Vmake, GitHub/YouMind-OpenLab, Atlabs, VideoWeb, DeepWhite (YouTube), Dom the AI Tutor (YouTube).
