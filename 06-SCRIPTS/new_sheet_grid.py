from PIL import Image, ImageDraw
import numpy as np

# Nuova sheet realistica multi-angolo
src = r"C:\Users\prova\Desktop\PORTFOLIO TOTALE\portfolio-v2\hf_20260330_214541_2baae010-1657-44e0-b987-ec20359d75b4.png"
out_dir = r"C:\Users\prova\Desktop\SEEDANCE PROMPT"

img = Image.open(src).convert("RGB")
w, h = img.size
print(f"Sheet originale: {w}x{h}")

# =============================================
# 1. GRID PESANTE 8x8 (stesso metodo che ha funzionato)
# =============================================
img1 = img.copy()
draw1 = ImageDraw.Draw(img1)
for i in range(1, 8):
    x = int(w * i / 8)
    draw1.line([(x, 0), (x, h)], fill=(255, 255, 255), width=6)
    y = int(h * i / 8)
    draw1.line([(0, y), (w, y)], fill=(255, 255, 255), width=6)
img1.save(f"{out_dir}\\paolo_newsheet_GRID8x8.png")
print("1: Grid 8x8 pesante - DONE")

# =============================================
# 2. GRID 10x10 + leggero noise (combo che disturba di piu')
# =============================================
img2 = img.copy()
arr2 = np.array(img2)
noise = np.random.randint(-35, 35, arr2.shape, dtype=np.int16)
arr2 = np.clip(arr2.astype(np.int16) + noise, 0, 255).astype(np.uint8)
img2 = Image.fromarray(arr2)
draw2 = ImageDraw.Draw(img2)
for i in range(1, 10):
    x = int(w * i / 10)
    draw2.line([(x, 0), (x, h)], fill=(255, 255, 255), width=5)
    y = int(h * i / 10)
    draw2.line([(0, y), (w, y)], fill=(255, 255, 255), width=5)
img2.save(f"{out_dir}\\paolo_newsheet_GRID10_NOISE.png")
print("2: Grid 10x10 + noise - DONE")

# =============================================
# 3. HEXAGONAL GRID (pattern non-rettangolare)
# =============================================
import math
img3 = img.copy()
draw3 = ImageDraw.Draw(img3)
hex_size = 45
for row in range(0, h // hex_size + 2):
    for col in range(0, w // hex_size + 2):
        cx = col * hex_size * 1.5
        cy = row * hex_size * 1.732
        if col % 2:
            cy += hex_size * 0.866
        points = []
        for i in range(6):
            angle = math.pi / 3 * i + math.pi / 6
            px = cx + hex_size * math.cos(angle)
            py = cy + hex_size * math.sin(angle)
            points.append((px, py))
        points.append(points[0])
        draw3.line(points, fill=(255, 255, 255), width=3)
img3.save(f"{out_dir}\\paolo_newsheet_HEXGRID.png")
print("3: Hexagonal grid - DONE")

# =============================================
# 4. FACE CROP dalla nuova sheet (close-up frontale, riga sotto a sx)
#    Crop della faccia frontale close-up + grid pesante
# =============================================
# La riga sotto ha 3 close-up della faccia: front, 3/4, profile
# Prendo il primo (frontale) che e' in basso a sinistra
face_x1 = 0
face_y1 = int(h * 0.5)  # meta' inferiore
face_x2 = int(w * 0.34)  # primo terzo
face_y2 = h
face_crop = img.crop((face_x1, face_y1, face_x2, face_y2))
face_crop = face_crop.resize((1024, 1024), Image.LANCZOS)
draw4 = ImageDraw.Draw(face_crop)
for i in range(1, 8):
    x = int(1024 * i / 8)
    draw4.line([(x, 0), (x, 1024)], fill=(255, 255, 255), width=5)
    y = int(1024 * i / 8)
    draw4.line([(0, y), (1024, y)], fill=(255, 255, 255), width=5)
face_crop.save(f"{out_dir}\\paolo_newsheet_FACECROP_GRID.png")
print("4: Face crop frontale + grid - DONE")

# =============================================
# 5. FACE CROP + grid + noise (massima protezione)
# =============================================
face_crop2 = img.crop((face_x1, face_y1, face_x2, face_y2))
face_crop2 = face_crop2.resize((1024, 1024), Image.LANCZOS)
arr5 = np.array(face_crop2)
noise5 = np.random.randint(-40, 40, arr5.shape, dtype=np.int16)
arr5 = np.clip(arr5.astype(np.int16) + noise5, 0, 255).astype(np.uint8)
face_crop2 = Image.fromarray(arr5)
draw5 = ImageDraw.Draw(face_crop2)
for i in range(1, 8):
    x = int(1024 * i / 8)
    draw5.line([(x, 0), (x, 1024)], fill=(255, 255, 255), width=5)
    y = int(1024 * i / 8)
    draw5.line([(0, y), (1024, y)], fill=(255, 255, 255), width=5)
face_crop2.save(f"{out_dir}\\paolo_newsheet_FACECROP_GRID_NOISE.png")
print("5: Face crop + grid + noise - DONE")

print(f"\n5 varianti della nuova sheet salvate in {out_dir}")
