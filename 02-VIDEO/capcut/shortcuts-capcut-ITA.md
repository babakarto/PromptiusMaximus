# Scorciatoie da Tastiera CapCut — Riferimento Completo

> Estratte da tutti e 5 i tutorial di Patrik Key. Il tuo cheat sheet per editare veloce.

---

## Editing Base

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **S** | Taglia tutti i layer alla posizione del playhead | Usa costantemente — funziona su TUTTI i layer insieme |
| **Q** | Elimina tutto a SINISTRA del playhead | Il modo piu veloce per trimmare. Sostituisce B > X > A (3 click → 1) |
| **W** | Elimina tutto a DESTRA del playhead | Come Q ma nella direzione opposta |
| **X** | Elimina la clip selezionata | Rimappato da Backspace — tieni la mano sinistra sulla tastiera |
| **A** | Deseleziona la modalita taglio | Dopo aver tagliato, torna alla modalita selezione |
| **B** | Attiva lo strumento taglio/lama | Strumento di taglio default (ma Q/W sono piu veloci nella maggior parte dei casi) |

---

## Layer e Visibilita

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **V** | Nascondi/Mostra layer | Organizzare caption, nascondere text layer di riferimento, toggle visibilita |
| **Command + Click** (Mac) / **Alt + Click** (Win) | Deseleziona un singolo layer da una multi-selezione | Tieni premuto mentre clicchi per escludere un layer dal gruppo |

---

## Marker e Organizzazione

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **M** | Aggiungi marker alla posizione del playhead | Segna la fine di ogni reel nel batch editing, etichetta le sezioni |

---

## Export e Punti I/O

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **I** | Imposta il punto di INIZIO (In point) | Posiziona il playhead all'inizio del reel → premi I |
| **O** | Imposta il punto di FINE (Out point) | Posiziona il playhead alla fine del reel → premi O, poi Esporta |

---

## Navigazione nella Timeline

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **Freccia Destra** | Avanza di 1 frame | Navigazione precisa frame per frame (es. 5 frame per counter effect) |
| **Freccia Sinistra** | Torna indietro di 1 frame | Navigazione precisa frame per frame |
| **Shift + Freccia Destra** | Avanza di 10 frame | Salto veloce per impostare keyframe di animazione |
| **Shift + Freccia Sinistra** | Torna indietro di 10 frame | Salto veloce indietro |

---

## Animazione e Keyframe

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **Shift + W** | Smootha automaticamente i keyframe selezionati | Seleziona prima i keyframe, poi Shift+W — sostituisce l'editing manuale del grafico |

---

## Compound Clip

| Tasto | Azione | Contesto |
|-------|--------|----------|
| **Option + G** (Mac) | Crea Compound Clip | Essenziale per sbloccare: mask, glow, freeze, effetti avanzati |
| **Tasto destro > Create Compound** | Come sopra (tutte le piattaforme) | Usa quando la scorciatoia non e disponibile |

---

## Controllo Velocita

| Azione | Come | Contesto |
|--------|------|----------|
| Velocita clip a 2x | Seleziona clip > Speed > imposta 2 | Sprinta attraverso il footage nel batch editing |
| Resetta velocita a 1x | Seleziona clip > Speed > imposta 1 | Resetta dopo il raw cut di ogni reel |

---

## Combo Pro per il Workflow

### Raw Cut Veloce (Batch Editing)
```
Q → Q → Q → (sposta playhead) → Q → ...
```
Sprinta attraverso il footage eliminando tutto a sinistra. Molto piu veloce di B > X > A.

### Trim Completo di un Reel + Etichetta
```
S (taglia) → Q o W (elimina) → ... ripeti ...
→ M (marker alla fine)
→ trascina text layer → scrivi etichetta → V (nascondi etichetta)
```

### Esportare un Singolo Reel dalla Timeline Batch
```
(playhead all'inizio) → I (punto di inizio)
(playhead alla fine/marker) → O (punto di fine)
→ Export → incolla il nome → fatto
```

### Setup Animazione Caption
```
V (nascondi layer) → posiziona il layer
→ keyframe su Transform + Blend
→ Shift + Freccia Destra x10 (10 frame avanti)
→ keyframe di nuovo
→ torna al primo keyframe → imposta i valori
→ seleziona entrambi i keyframe → Shift + W (smootha)
```

### Editing Solo con la Mano Sinistra (senza lasciare il mouse)
```
A (deseleziona) → S (taglia) → Q (elimina sx) → X (elimina) → W (elimina dx)
Tutti i tasti sono sul lato sinistro della tastiera.
```

---

## Variable Speed Animation — Non e una Shortcut, Ma e Essenziale

Tasto destro su qualsiasi clip > **Show Variable Speed Animation** per accedere a:

| Opzione | Effetto |
|---------|---------|
| **Auto Curve** | Ease in/out automatico (seleziona UN keyframe alla volta) |
| **Quad Out** | Inizio veloce → fine lenta (seleziona piu keyframe) |
| **Rebound Out** | Effetto rimbalzo/overshoot (ottimo per animazioni shine) |
| **Trascinamento linea blu** | Controllo manuale: trascina verso l'inizio = partenza veloce, fine lenta |

> **Regola:** Per Auto Curve, seleziona sempre UN SOLO keyframe. Se ne selezioni due, il pulsante non funziona.

---

## Versione Stampa Rapida

```
S     = Taglia tutto
Q     = Elimina a sinistra
W     = Elimina a destra
X     = Elimina clip
A     = Deseleziona modalita taglio
V     = Nascondi/mostra layer
M     = Marker
I     = Punto inizio
O     = Punto fine
⇧+→   = Salta 10 frame
⇧+W   = Smootha keyframe
⌥+G   = Compound clip (Mac)
```
