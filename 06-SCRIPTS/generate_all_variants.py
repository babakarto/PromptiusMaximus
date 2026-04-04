from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random

src = r"C:\Users\prova\Desktop\PORTFOLIO TOTALE\portfolio-v2\hf_20260330_203211_60845516-53e2-46be-a613-4c0403e44d2c.png"
out_dir = r"C:\Users\prova\Desktop\SEEDANCE PROMPT"

img = Image.open(src)
w, h = img.size

# --- VERSIONE B: Noise pesante ---
img_noise = img.copy()
pixels = img_noise.load()
for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y][:3]
        noise = random.randint(-25, 25)
        pixels[x, y] = (
            max(0, min(255, r + noise)),
            max(0, min(255, g + noise)),
            max(0, min(255, b + noise))
        )
img_noise.save(f"{out_dir}\\paolo_sheet_NOISE.png")
print("B: Noise - DONE")

# --- VERSIONE C: Desaturazione ---
img_desat = img.copy()
enhancer = ImageEnhance.Color(img_desat)
img_desat = enhancer.enhance(0.3)  # 30% saturazione
img_desat.save(f"{out_dir}\\paolo_sheet_DESAT.png")
print("C: Desaturazione - DONE")

# --- VERSIONE D: Grid + Noise combo ---
img_combo = img.copy()
# Noise
pixels_c = img_combo.load()
for y in range(h):
    for x in range(w):
        r, g, b = pixels_c[x, y][:3]
        noise = random.randint(-20, 20)
        pixels_c[x, y] = (
            max(0, min(255, r + noise)),
            max(0, min(255, g + noise)),
            max(0, min(255, b + noise))
        )
# Grid
draw = ImageDraw.Draw(img_combo)
for i in range(1, 8):
    x = int(w * i / 8)
    draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 200), width=3)
    y = int(h * i / 8)
    draw.line([(0, y), (w, y)], fill=(255, 255, 255, 200), width=3)
img_combo.save(f"{out_dir}\\paolo_sheet_GRID_NOISE.png")
print("D: Grid+Noise combo - DONE")

# --- VERSIONE E: Leggero blur sui volti + grid ---
img_blur_grid = img.copy()
img_blur_grid = img_blur_grid.filter(ImageFilter.GaussianBlur(radius=1.5))
draw2 = ImageDraw.Draw(img_blur_grid)
for i in range(1, 6):
    x = int(w * i / 6)
    draw2.line([(x, 0), (x, h)], fill=(255, 255, 255, 220), width=4)
    y = int(h * i / 6)
    draw2.line([(0, y), (w, y)], fill=(255, 255, 255, 220), width=4)
img_blur_grid.save(f"{out_dir}\\paolo_sheet_BLUR_GRID.png")
print("E: Blur+Grid - DONE")

print(f"\nTutte le varianti salvate in {out_dir}")
