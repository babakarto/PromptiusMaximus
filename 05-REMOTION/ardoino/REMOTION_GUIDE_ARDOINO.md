# REMOTION GUIDE — Progetto Paolo Ardoino News Video

> Progetto Remotion per overlay di testo animato sul video mockumentary di Paolo Ardoino.
> Creato: 31 Marzo 2026
> Video sorgente: `popo.mp4` (1280x720, 29.97fps, ~2 minuti, H.264 + AAC)

---

## STRUTTURA PROGETTO

```
remotion-news/
  src/
    index.ts          ← Entry point, registra RemotionRoot
    Root.tsx           ← Composizione "NewsVideo" (1280x720, 29.97fps, 3622 frame)
    NewsVideo.tsx      ← Layer principale: Video + Captions + Locations
    Captions.tsx       ← Overlay caption con typewriter (bottom-left)
    Locations.tsx      ← Overlay location title con orologio live (top-left/right)
  public/
    popo.mp4           ← Video sorgente (copiato da news/)
  package.json
  tsconfig.json
```

---

## COMANDI

```bash
# Avviare lo studio (preview nel browser)
cd remotion-news
npx remotion studio

# Lo studio si apre su http://localhost:3000
# Hot reload automatico — ogni modifica ai file si aggiorna in tempo reale
```

---

## COMPONENTE 1: CAPTIONS (`Captions.tsx`)

### Cosa fa
Testi animati con effetto typewriter che appaiono in basso a sinistra sul video.
Servono come contrappunto visivo all'audio delle news — prima i numeri delle accuse, poi le prove che hanno vinto.

### Stile
- **Font:** `dec_terminal_modern` (installato sul sistema), monospace
- **Posizione:** bottom-left, padding 60px dal basso, 40px da sinistra
- **Colore:** bianco con text-shadow scuro (`0 0 10px rgba(0,0,0,0.8), 0 0 20px rgba(0,0,0,0.5)`)
- **Dimensione:** 24px durante il typing, si rimpicciolisce a 15px quando la riga successiva inizia

### Animazione typewriter
- Ogni riga si scrive lettera per lettera alla velocita' definita nel campo `speed` (chars per frame)
- Cursore `▌` lampeggiante ogni 15 frame, visibile solo durante la fase di typing
- Il cursore sparisce quando tutte le righe sono scritte

### Animazione shrink (rimpicciolimento)
- Quando la riga successiva inizia a scriversi, la riga precedente si rimpicciolisce fluidamente:
  - Font: 24px → 15px
  - Opacity: 1 → 0.7
  - Durata: 15 frame con `Easing.out(cubic)`
- L'ultima riga di ogni caption resta grande (nessuna riga dopo di lei)

### Fade out
- Negli ultimi 10 frame di ogni caption, l'intero blocco sfuma a opacity 0
- Easing: `Easing.out(cubic)`

### Parametri per riga
Ogni riga ha 3 parametri configurabili:
- `text` — il testo da mostrare
- `speed` — caratteri per frame (1 = lento/leggibile, 2 = veloce)
- `pauseAfter` — frame di pausa dopo che la riga finisce di scriversi (prima che parta la successiva)

Il `pauseAfter` controlla quanto tempo ogni riga resta "in grande" prima di rimpicciolirsi.
Righe piu' lunghe/importanti → pauseAfter piu' alto. Righe corte → pauseAfter basso.

### Le 4 caption attuali

**Caption 1 — Le accuse (frame 325-625, 300 frame)**
```
Riga 1: "6 lawsuits filed. 19 federal investigations opened."
        speed: 1, pauseAfter: 20
Riga 2: "$61 million in fines paid. $1.4 trillion in damages claimed against Tether."
        speed: 1, pauseAfter: 20
Riga 3: "Every single case was dismissed or settled. Zero findings of fraud."
        speed: 1, pauseAfter: 0
```

**Caption 2 — Gli short seller (frame 970-1170, 200 frame)**
```
Riga 1: '"Fir Tree" bet billions on Tether's collapse. Shut down 2025.'
        speed: 1, pauseAfter: 35
Riga 2: "Hindenburg offered $1M bounty for proof of fraud."
        speed: 1.5, pauseAfter: 25
Riga 3: "No report. They shut down too."
        speed: 2, pauseAfter: 0
```
Nota: riga 1 la piu' lenta (piu' lunga), riga 3 la piu' veloce (piu' corta).
pauseAfter decrescente: 35 → 25 → 0 (riga 1 sta in grande piu' di tutte).

**Caption 3 — I numeri (frame 1444-1628, 184 frame)**
```
Riga 1: "$10B redeemed in two weeks during the 2022 crash. Every dollar honored."
        speed: 1.5, pauseAfter: 45
Riga 2: "$13 billion profit in 2024. Fewer than 200 employees."
        speed: 1.5, pauseAfter: 0
```

**Caption 4 — Le origini (frame 2504-2683, 179 frame)**
```
Riga 1: "A family of farmers from a village of 1,900 people."
        speed: 1, pauseAfter: 30
Riga 2: "Two Italians from small towns built the largest stablecoin on Earth."
        speed: 1, pauseAfter: 0
```

### Come aggiungere una nuova caption
Aggiungi un oggetto all'array `CAPTIONS` in `Captions.tsx`:
```tsx
{
  start: FRAME_INIZIO,
  end: FRAME_FINE,
  lines: [
    { text: "Testo riga 1", speed: 1, pauseAfter: 20 },
    { text: "Testo riga 2", speed: 1.5, pauseAfter: 0 },
  ],
},
```

### Come modificare velocita' e timing
- `speed: 1` = 1 carattere per frame (lento, ~30 chars/sec)
- `speed: 1.5` = 1.5 chars/frame (medio)
- `speed: 2` = 2 chars/frame (veloce)
- `pauseAfter: 20` = 20 frame (~0.67 sec) di pausa prima della riga successiva
- Piu' alto il `pauseAfter`, piu' a lungo la riga resta grande e visibile

---

## COMPONENTE 2: LOCATIONS (`Locations.tsx`)

### Cosa fa
Titoli di luogo stile documentario che appaiono in alto. Effetto typewriter in entrata,
hold con orologio che ticchetta in tempo reale, reverse typewriter (backspace) in uscita.

### Stile
- **Font:** `Inter` / `Helvetica Neue`, weight 300 (thin), sans-serif
- **Dimensione:** 16px, tutto UPPERCASE, letter-spacing 3px
- **Colore:** bianco, opacity 0.85
- **Text-shadow:** `0 0 8px rgba(0,0,0,0.6)`
- **Posizione:** top-left di default (40px top, 40px left), configurabile top-right per singola location

### Animazione
1. **Type in** — lettere appaiono una per una, 2 chars/frame, cursore `▌` lampeggiante
2. **Hold** — 90 frame (~3 sec), testo completo visibile, orologio che ticchetta
3. **Type out (reverse)** — lettere spariscono dalla fine, come un backspace, 2 chars/frame

### Orologio live
- I secondi avanzano in tempo reale (1 incremento ogni 30 frame)
- I due punti `:` lampeggiano ogni mezzo secondo (15 frame visibili, 15 frame spazio vuoto)
- Ogni location ha un orario di partenza diverso con secondi diversi
- L'orologio ticchetta sia durante l'hold che durante il typing (se i caratteri dell'ora sono gia' visibili)

### Le 6 location attuali

| Frame | Location | Orario | Posizione |
|-------|----------|--------|-----------|
| 0 | El Salvador, Central America | 4:48:03 AM | top-left |
| 214 | El Salvador, Central America | 5:30:14 AM | top-left |
| 1154 | Undisclosed Dojo | 6:00:37 PM | **top-right** |
| 2170 | Private Residence | 11:47:52 PM | top-left |
| 2501 | Cisano sul Neva, North Italy — Population: 1,900 | (nessuno) | top-left |
| 3176 | Washington D.C., United States | (nessuno) | top-left |

### Come aggiungere una nuova location
```tsx
// Con orologio:
{ startFrame: 500, location: "Nome Luogo", time: { hour: 3, minute: 15, startSecond: 42, ampm: "PM" } },

// Senza orologio:
{ startFrame: 500, location: "Nome Luogo" },

// Posizione top-right:
{ startFrame: 500, location: "Nome Luogo", position: "top-right" },
```

### Come cambiare il timing
- `HOLD_FRAMES = 90` — quanto tempo il testo resta visibile (in frame)
- `CHARS_PER_FRAME = 2` — velocita' del typewriter in/out
- La durata totale e' calcolata automaticamente: type_in + hold + type_out

---

## COMPOSIZIONE (`NewsVideo.tsx`)

```tsx
<AbsoluteFill style={{ backgroundColor: "black" }}>
  <Video src={staticFile("popo.mp4")} />   ← Video sotto
  <Captions />                              ← Testi bottom-left
  <Locations />                             ← Location top-left/right
</AbsoluteFill>
```

I layer sono sovrapposti: video in fondo, caption sopra, location in cima.
Non si sovrappongono visivamente perche' le caption sono in basso e le location in alto.

---

## ESPORTAZIONE PER PREMIERE PRO

Per esportare SOLO i testi (senza video) con sfondo trasparente:

1. Creare una composizione alternativa senza il `<Video>`, solo `<Captions />` e `<Locations />`
   con `backgroundColor: "transparent"`
2. Renderizzare come WebM con trasparenza:
   ```bash
   npx remotion render src/index.ts OverlayOnly out/overlay.webm --codec=vp8
   ```
3. Oppure come sequenza PNG trasparente:
   ```bash
   npx remotion render src/index.ts OverlayOnly out/frames --image-format=png
   ```
4. Importare in Premiere come layer sopra il video originale

---

## COSTANTI GLOBALI DA RICORDARE

| Costante | Captions | Locations |
|----------|----------|-----------|
| Font | dec_terminal_modern | Inter / Helvetica Neue |
| Dimensione | 24px (big) / 15px (small) | 16px |
| Posizione | bottom 60px, left 40px | top 40px, left/right 40px |
| Cursore | `▌` blink ogni 15 frame | `▌` blink ogni 15 frame |
| FPS video | 29.97 | 30 (approssimato per orologio) |
| Fade out | 10 frame, easeOut cubic | nessuno (reverse typewriter) |
| Shrink | 15 frame, 24→15px, 1→0.7 opacity | nessuno |
