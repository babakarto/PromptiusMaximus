# Come lavorare su questo progetto

## IMPORTANTE: l'utente non sa lanciare npm/dev
Ogni volta che apri una nuova chat, **TU (Claude) devi avviare il server**.
Non chiedere all'utente di farlo. Fallo direttamente tu con:

```bash
cd "/c/Users/prova/Desktop/REMOTION XCITE" && npm install && npx remotion studio src/index.ts
```

Poi apri il browser:
```bash
start http://localhost:PORT
```
(la porta cambia ogni volta, leggila dall'output del server)

## Workflow consigliato
1. **Leggi questa cartella guida/** prima di fare qualsiasi cosa
2. **Avvia il server** per l'utente (vedi sopra)
3. **Fai le modifiche** ai file .tsx
4. **Verifica** con `npx tsc --noEmit` dopo ogni cambio
5. **Renderizza frame di test** per controllare il risultato visivo:
   ```bash
   npx remotion still src/index.ts XciteShowreel --frame=NUMERO --output=test.png
   ```
6. **Mostra il risultato** all'utente leggendo il PNG renderizzato

## Comandi utili
| Comando | Cosa fa |
|---------|---------|
| `npm install` | Installa dipendenze |
| `npx remotion studio src/index.ts` | Avvia studio (preview live) |
| `npx remotion still src/index.ts XciteShowreel --frame=450 --output=test.png` | Renderizza un singolo frame |
| `npx remotion render src/index.ts XciteShowreel --output=video.mp4` | Render video finale MP4 |
| `npx tsc --noEmit` | Type check senza compilare |
| `npx remotion compositions src/index.ts` | Lista composizioni registrate |

## Regole Remotion (dalle skills installate)
- **MAI** usare CSS transitions/animations o classi Tailwind animate-*
- **SEMPRE** usare `useCurrentFrame()` + `interpolate()`/`spring()` per animare
- **SEMPRE** usare `<Img>` da remotion (non `<img>` HTML)
- **SEMPRE** usare `staticFile()` per file in public/
- **SEMPRE** `maxWidth: "none"` sulle Img dentro container con overflow:hidden
- **SEMPRE** `premountFor={30}` sulle Sequence
- Timing in secondi: `Math.round(seconds * fps)` non frame hardcodati
- Spring configs dalla skill library: heavy/snappy/bouncy/punch
