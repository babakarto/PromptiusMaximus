# 2D Character Rig & Body Part Separation Tools — Research Report

**Date:** 2026-03-17
**Source:** Web research (X API non disponibile — token 401)
**Focus:** Tool AI per separazione automatica body parts, asset puppet pre-riggati, template per animazione 2D

---

## 1. AI TOOLS — Auto-Separazione Body Parts

### KomikoAI — AI Layer Splitter ⭐ TOP PICK
- **Cosa fa:** Carica un'illustrazione e l'AI separa automaticamente in layer: personaggi, background, occhi, capelli, arti, props
- **Come funziona:** Deep learning su milioni di immagini, riconosce bordi, colori, contesto
- **Input:** JPG, PNG
- **Output:** Layer separati alla risoluzione originale
- **Compatibilità:** Live2D, Spine, After Effects (generico "animation-ready")
- **Pricing:** Free credits (500 "Zaps") per nuovi utenti, poi piani a pagamento
- **Limitazioni:** Scene complesse possono raggruppare elementi; dettagli fini (capelli, pelliccia) sono problematici; oggetti molto sovrapposti difficili da separare
- **Target:** VTuber artists, Live2D riggers, indie animators
- **Link:** [komiko.app/layer_splitter](https://komiko.app/layer_splitter)
- **Blog:** [How to Instantly Split Anime Art into Layers](https://komiko.app/blog/how-to-instantly-split-anime-art-into-layers-for-animation-and-rigging)

### GodMode AI — Spine Animation Generator ⭐ TOP PICK
- **Cosa fa:** Genera automaticamente file Spine con body parts separati da un'immagine 2D
- **Come funziona:** 1) Genera modello 3D con idle animation per capire la struttura scheletrica → 2) Converte in formato Spine 2D con layering corretto
- **Input:** JPG, PNG, WebP (fino a 10MB)
- **Output:** Spine JSON + PNG atlas — compatibile Unity, Unreal, Godot
- **Auto-rigging:** Sì, crea strutture scheletriche professionali ottimizzate per Spine
- **Animazioni:** 2000+ animazioni professionali con one-click retargeting
- **Limitazione:** Solo personaggi umani/umanoidi
- **Pricing:**
  - Free: 3 crediti alla registrazione
  - Starter: $12 per 20 crediti
  - Popular: $32 per 60 crediti
  - Ultimate: $100 per 250 crediti
  - Subscription: $19/mese (fino a 200 generazioni)
- **Link:** [godmodeai.co/ai-spine-animation](https://www.godmodeai.co/ai-spine-animation)

### Pixa — AI 2D Character Rigging
- **Cosa fa:** Upload di un character design → AI rileva punti di articolazione (gomiti, ginocchia, spalle) → costruisce scheletro digitale
- **Input:** PNG, PSD
- **Best practice:** Immagine in T-pose con arti separati dal corpo, sfondo trasparente
- **Output:** Personaggio riggato + animazione da text prompt
- **Pricing:** Free to try
- **Link:** [pixa.com/create/2d-character-rigging](https://www.pixa.com/create/2d-character-rigging)

### Live2D Cubism — Material Separation Plugin
- **Cosa fa:** Plugin Photoshop ufficiale per separare materiali/layer per Live2D
- **Auto-mesh:** Generazione automatica mesh basata su densità di punti specificata
- **Versione:** R1 beta2 (giugno 2025)
- **Link:** [docs.live2d.com - Material Separation Plugin](https://docs.live2d.com/en/cubism-editor-manual/material-separation-ps-plugin-download/)

### Cascadeur
- **Cosa fa:** Software standalone per animazione keyframe 3D con AI-assist
- **Focus:** Più 3D che 2D, ma utile per reference di movimenti
- **Link:** [cascadeur.com](https://cascadeur.com)

---

## 2. ASSET PUPPET PRE-RIGGATI

### Rive — Community Templates (FREE)
File della community con bones e constraints:
- [Character rigging and animation](https://rive.app/community/files/13636-25823-character-rigging-and-animation/) — bones + constraints
- [Marty animation](https://rive.app/community/files/52-69-marty-animation/) — binding method, bones collegati a parti diverse del personaggio
- [Character animation](https://rive.app/community/files/10837-20734-character-animation/) — animazione base con bones
- [Joints and bones rig](https://rive.app/community/files/6082-11833-joints-and-bones-rig/) — test di rig per bending joints
- [Mouth Rig Demo](https://rive.app/community/files/3216-6766-mouth-rig-demo/) — rig bocca con 3 controlli

### Spine 2D — Asset Packs (PAID)
- **Hitman - Platformer** ($10) — Scheletro riggato, animazioni platformer (walk, run, jump, wall slide, punch), progetto Unity 5
- **Gunman - Jetpack Platformer** ($10) — Scheletro IK-rigged, jetpack, 4 armi, progetto Unity 5
- **Sconto:** 50% su tutti i pack dopo il primo
- **Link:** [esotericsoftware.com/spine-asset-packs](https://esotericsoftware.com/spine-asset-packs)

### Spine 2D — Marketplace di terze parti
- **itch.io** — [Tag: 2D + Spine](https://itch.io/game-assets/newest/tag-2d/tag-spine) — asset indie
- **GraphicRiver** — [124+ Spine 2D game assets](https://graphicriver.net/spine-and-2d-graphics-in-game-assets) — inclusi flat art characters
- **GameDev Market** — [Character Spine animation](https://www.gamedevmarket.net/asset/2d-character-spine-animation-and-item-7166)

### DragonBones — Asset gratuiti
- [Free 2D Character + DragonBones setup](https://forum.starling-framework.org/d/20516-free-2d-character-dragonbones-set-up-and-animations-art-assets) — personaggio con animazioni e setup

### Adobe Character Animator — Puppet Templates (FREE)
- **Okay Samurai** — [okaysamurai.com/puppets](https://okaysamurai.com/puppets/) — libreria di puppet gratuiti, inclusi pack con Limb IK (4 puppet + project file)
- **ElectroPuppet** — [85+ Free Puppets per il 2026](https://electropuppet.com/free-adobe-puppet-templates/) — catalogo aggiornato feb 2026
- **Adobe ufficiale** — [Pro mode example puppets](https://pages.adobe.com/character/en/puppets)
- **GraphicMama** — [63 Free Character Animator Puppets](https://graphicmama.com/blog/free-character-animator-puppets-2021/)
- **ReallyGoodDesigns** — [600+ Fully Rigged Puppets](https://reallygooddesigns.com/adobe-character-animator-puppets-download/)

### SVG Puppet Resources (FREE)
- **FreeSVG** — [Vector Puppet Male](https://freesvg.org/1539432292) — puppet multi-parte posabile
- **FreeSVG** — [Toy Clown Puppet Animation](https://freesvg.org/clown-jointtest-v4) — puppet animato con SMIL
- **Vecteezy** — [Puppet Vectors](https://www.vecteezy.com/free-vector/puppet) — vettori gratuiti
- **Vexels** — [Puppet vectors](https://www.vexels.com/free-vectors/puppet/) — AI, SVG, JPG, PNG con licenza commerciale

---

## 3. SOFTWARE PER RIGGING (Non-AI, Manuale)

| Software | Tipo | Costo | Note |
|----------|------|-------|------|
| **Rive** | Web-based, bones & constraints | Free tier + paid | Ideale per web/app, export leggero |
| **Spine 2D** | Desktop, skeletal animation | $69 Essential / $299 Pro | Standard per gamedev |
| **DragonBones** | Desktop, open source | FREE | Alternativa gratuita a Spine |
| **Adobe Character Animator** | Desktop, motion capture | Creative Cloud sub | Auto-tag layers da PSD/AI |
| **Cartoon Animator 5** | Desktop, puppet animation | ~$99-$199 | Bone-rigging, Smart IK |
| **Duik (After Effects)** | Plugin AE, rigging | FREE (open source) | Standard per motion design |
| **Adobe Animate** | Desktop, vector animation | Creative Cloud sub | Rigging nativo dal 2024 |
| **Live2D Cubism** | Desktop, mesh deformation | Free tier + Pro | Ideale per VTuber/anime style |
| **Blender (Grease Pencil)** | Desktop, 2D in 3D | FREE | Potente ma curva di apprendimento ripida |

---

## 4. WORKFLOW CONSIGLIATO — Dal Character al Puppet Animato

### Opzione A: Full AI (veloce, meno controllo)
1. **Disegna/genera** il character in stile flat vector/vinyl toy
2. **GodMode AI** → carica immagine → ricevi Spine JSON con body parts separati + rig automatico
3. Importa in **Unity/Godot** e applica animazioni dal catalogo di 2000+

### Opzione B: AI + Manuale (bilanciato)
1. **Disegna** il character come illustrazione completa
2. **KomikoAI Layer Splitter** → separa in layer (testa, corpo, braccia, gambe)
3. Importa layer separati in **Spine 2D** o **Rive**
4. Rigga manualmente con bones
5. Anima

### Opzione C: Manuale + Template (massimo controllo)
1. **Disegna** ogni body part separatamente in Illustrator/Figma
2. Esporta come SVG/PNG con layer nominati
3. Importa in **Rive** (usando template community come base) o **After Effects + Duik**
4. Rigga e anima con pieno controllo

---

## 5. RICERCHE EFFETTUATE

- Queries web: 9
- Pagine analizzate in dettaglio: 4
- Fonte: Google Web Search (X API non disponibile)
- Stima costo: $0 (web search gratuita)
- Data: 2026-03-17
