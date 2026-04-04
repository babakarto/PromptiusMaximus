from PIL import Image, ImageDraw, ImageEnhance
import random
import numpy as np

src = r"C:\Users\prova\Desktop\PORTFOLIO TOTALE\portfolio-v2\hf_20260330_203211_60845516-53e2-46be-a613-4c0403e44d2c.png"
out_dir = r"C:\Users\prova\Desktop\SEEDANCE PROMPT"

img = Image.open(src).convert("RGB")
w, h = img.size
arr = np.array(img)

# --- VERSIONE B: Noise PESANTE visibile ---
noise = np.random.randint(-60, 60, arr.shape, dtype=np.int16)
img_noise = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
Image.fromarray(img_noise).save(f"{out_dir}\\paolo_sheet_NOISE.png")
print("B: Noise PESANTE - DONE")

# --- VERSIONE D: Grid densa + Noise PESANTE ---
noise2 = np.random.randint(-50, 50, arr.shape, dtype=np.int16)
img_combo_arr = np.clip(arr.astype(np.int16) + noise2, 0, 255).astype(np.uint8)
img_combo = Image.fromarray(img_combo_arr)
draw = ImageDraw.Draw(img_combo)
# Grid 10x10 molto fitta
for i in range(1, 10):
    x = int(w * i / 10)
    draw.line([(x, 0), (x, h)], fill=(255, 255, 255), width=6)
    y = int(h * i / 10)
    draw.line([(0, y), (w, y)], fill=(255, 255, 255), width=6)
img_combo.save(f"{out_dir}\\paolo_sheet_GRID_NOISE.png")
print("D: Grid 10x10 + Noise PESANTE - DONE")

# --- VERSIONE F: Scanlines orizzontali (TV effect) ---
img_scan = arr.copy()
for y in range(0, h, 4):  # ogni 4 pixel una scanline
    img_scan[y:y+2, :] = np.clip(img_scan[y:y+2, :].astype(np.int16) - 80, 0, 255).astype(np.uint8)
Image.fromarray(img_scan).save(f"{out_dir}\\paolo_sheet_SCANLINES.png")
print("F: Scanlines TV - DONE")

# --- VERSIONE G: Halftone dots pattern ---
img_half = img.copy()
draw_h = ImageDraw.Draw(img_half)
dot_spacing = 12
for y in range(0, h, dot_spacing):
    for x in range(0, w, dot_spacing):
        draw_h.ellipse([x, y, x+5, y+5], fill=(255, 255, 255, 180))
img_half.save(f"{out_dir}\\paolo_sheet_HALFTONE.png")
print("G: Halftone dots - DONE")

print(f"\nTutto salvato in {out_dir}")
