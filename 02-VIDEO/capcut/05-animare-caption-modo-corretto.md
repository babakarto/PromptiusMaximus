# Stai Animando le Caption nel Modo Sbagliato - Il Sistema Corretto

> **Autore:** Patrik Key
> **Video:** https://www.youtube.com/watch?v=hjNH5JUVgEw
> **Concetto chiave:** Il sistema esatto per creare caption animate stile pro con 3 movimenti master riutilizzabili

---

## I 3 Step Fondamentali

Se non padroneggi questi 3 step, non otterrai gli stessi risultati.

---

## Step 1: La Base - I Due Font

Devi scegliere **2 font** e decidere i loro ruoli:

| Tipo | Ruolo | Uso |
|------|-------|-----|
| **Font Primario** | Contesto | Parole di contenuto principale |
| **Font Secondario** | Emozione | Highlight di keyword e parole emotive |

> **Trucco:** Se tratti ogni parola allo stesso modo, nulla risalta. Il font primario gestisce il contesto, il secondario gestisce le emozioni e gli highlight.

---

## Step 2: Stilizzare il Testo PRIMA di Generare le Caption

### Impostazioni del Font Primario (Helvetica):
1. Font: **Helvetica**
2. Attiva **Bold**
3. Attiva **Uppercase**
4. **Character Level** (spaziatura caratteri): **-2**
5. **Stroke** (contorno): circa **4**
6. **Shadow**: opacity circa **70**

### Animazione:
1. Vai su **Animation**
2. Imposta **Blur** sia su **In** che su **Out**
3. Durata: **0.6 secondi**

> Queste impostazioni creano un look professionale e cinematico.

---

## Step 3: Creare i 3 Movimenti Master

Questi 3 movimenti si riusano per tutto il video. Creali una volta, replicali all'infinito.

### Setup Iniziale:
1. Clicca **Generate Captions**
2. Prendi il layer e portalo sopra
3. Nascondi il layer con **V**
4. Posiziona il layer poco sotto il mento

---

### Movimento 1: Slide Left (Da Sinistra al Centro)

1. Vai all'**inizio** del layer
2. Attiva **keyframe su Transform**
3. Attiva **keyframe su Blend** (opacity)
4. Tieni **Shift** + premi **freccia destra 10 volte** (= 10 frame avanti)
5. Attiva un altro keyframe su Transform e Blend
6. Torna al **primo keyframe**:
   - **Opacity** = 0 (crea fade in)
   - **Position X** = **-600** (parte da sinistra)
7. **Smoothing:** Apri Variable Speed Animation > seleziona entrambi i keyframe > **Shift + W** (shortcut per smoothare)
8. Fai lo stesso per l'opacity

> **Shortcut Shift + W** = smooth automatico dei keyframe selezionati

---

### Movimento 2: Slide Right (Da Destra al Centro)

1. **Duplica** il layer Slide Left
2. Vai al primo keyframe
3. Cambia **Position X** da -600 a **+600**

> Tutto il resto rimane identico.

---

### Movimento 3: Slide Up (Dal Basso verso l'Alto)

1. **Duplica** il layer
2. Nascondi con **V**
3. Vai al primo keyframe
4. **Position X** = **0** (non si muove orizzontalmente)
5. **Position Y** = **-1200** (parte dal basso)
6. Apri il **Graph Editor** e smooth tutti i keyframe

> Direzione diversa = devi ri-smoothare nel graph editor.

---

### Organizzazione dei Movimenti:

1. Rinomina i 3 layer:
   - `Slide Left`
   - `Slide Right`
   - `Slide Up`
2. **Copia tutti e 3** e incollali alla **fine della clip** (backup per non perderli)

---

## Creare le Caption con i Movimenti

### Procedura:
1. Crea un **Compound Clip** per ognuno dei 3 layer (separatamente)
2. Scrivi la prima parola nel layer appropriato
3. Posiziona visivamente sotto la caption precedente

### Esempio Pratico ("If you buy make smooth captions in CapCut"):

| Parola | Movimento | Note |
|--------|-----------|------|
| "if" | Slide Up | Font primario |
| "you" | Slide Left | Font primario |
| "buy" | Slide Left | Font primario, layer 3 |
| "make" | Slide Left | Compound, font size ~18 |
| "smooth" | Slide Up | Font size ~20 |
| "captions" | Slide Right | **Font secondario** (Shell), title case, no bold, character level 0 |

### Per Ogni Parola:
1. Duplica il movimento che vuoi usare
2. Posiziona sulla timeline
3. Cambia il testo
4. Regola dimensione font se necessario
5. Crea **Compound Clip**
6. Posiziona visivamente nel frame

### Timing:
- Seleziona tutti i layer
- **Offsetta** ogni layer per allinearsi con il parlato
- Ogni parola appare quando viene detta

---

## Highlight delle Parole Chiave

1. Apri il compound della parola da evidenziare
2. Seleziona il **text layer** interno
3. **Cambia il colore** della parola

> Questo fa risaltare le keyword importanti rispetto al resto delle caption.

---

## Font Secondario - Impostazioni

Quando usi il font secondario (es. per "captions"):

| Impostazione | Valore |
|--------------|--------|
| Font | Shell (o altro secondario) |
| Bold | **Disattivato** |
| Character Level | **0** (reset) |
| Title Case | **Attivato** |
| Font Size | Piu grande del primario |

---

## Workflow Completo Riassunto

```
1. STILIZZA il testo (Helvetica, bold, uppercase, -2 char, stroke 4, shadow 70)
2. ANIMA con Blur in/out a 0.6s
3. CREA i 3 movimenti master (Left, Right, Up)
4. RINOMINA e SALVA i movimenti come backup
5. Per ogni parola:
   a. Duplica il movimento giusto
   b. Cambia il testo
   c. Crea compound
   d. Posiziona nel frame
   e. Offsetta per il timing
6. HIGHLIGHT le keyword con il font secondario + colore diverso
7. RIPETI per tutto il video
```

---

## Shortcuts Importanti

| Shortcut | Azione |
|----------|--------|
| **V** | Nascondi/Mostra layer |
| **Shift + freccia** | Avanza di 10 frame |
| **Shift + W** | Smooth keyframe selezionati |
| **Option + G** (Mac) | Crea Compound Clip |
| **S** | Split All |

---

## Note Finali

- All'inizio ci vuole tempo, ma diventa **memoria muscolare**
- I 3 movimenti master sono la chiave: creali una volta, usali per sempre
- Mescola i movimenti per varieta visiva
- Il font secondario crea **gerarchia visiva** nelle caption
- Versione CapCut consigliata: **6.40+**
