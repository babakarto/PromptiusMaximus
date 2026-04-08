# How to work on this project

## IMPORTANT: the user doesn't know how to launch npm/dev
Every time you open a new chat, **YOU (Claude) must start the server**.
Don't ask the user to do it. Do it directly with:

```bash
cd /path/to/remotion-xcite && npm install && npx remotion studio src/index.ts
```

Then open the browser:
```bash
start http://localhost:PORT
```
(the port changes every time, read it from the server output)

## Recommended workflow
1. **Read this guida/ folder** before doing anything
2. **Start the server** for the user (see above)
3. **Make changes** to the .tsx files
4. **Verify** with `npx tsc --noEmit` after each change
5. **Render test frames** to check the visual result:
   ```bash
   npx remotion still src/index.ts XciteShowreel --frame=NUMBER --output=test.png
   ```
6. **Show the result** to the user by reading the rendered PNG

## Useful commands
| Command | What it does |
|---------|-------------|
| `npm install` | Install dependencies |
| `npx remotion studio src/index.ts` | Launch studio (live preview) |
| `npx remotion still src/index.ts XciteShowreel --frame=450 --output=test.png` | Render a single frame |
| `npx remotion render src/index.ts XciteShowreel --output=video.mp4` | Final video MP4 render |
| `npx tsc --noEmit` | Type check without compiling |
| `npx remotion compositions src/index.ts` | List registered compositions |

## Remotion rules (from installed skills)
- **NEVER** use CSS transitions/animations or Tailwind animate-* classes
- **ALWAYS** use `useCurrentFrame()` + `interpolate()`/`spring()` to animate
- **ALWAYS** use `<Img>` from remotion (not HTML `<img>`)
- **ALWAYS** use `staticFile()` for files in public/
- **ALWAYS** `maxWidth: "none"` on Img elements inside containers with overflow:hidden
- **ALWAYS** `premountFor={30}` on Sequences
- Timing in seconds: `Math.round(seconds * fps)` not hardcoded frames
- Spring configs from the skill library: heavy/snappy/bouncy/punch
