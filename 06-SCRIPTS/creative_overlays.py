from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import numpy as np
import math

src = r"C:\Users\prova\Desktop\PORTFOLIO TOTALE\portfolio-v2\hf_20260330_203211_60845516-53e2-46be-a613-4c0403e44d2c.png"
out_dir = r"C:\Users\prova\Desktop\SEEDANCE PROMPT"

img = Image.open(src).convert("RGB")
w, h = img.size

# =============================================
# 1. TRIANGULAR MESH (wireframe 3D style)
# =============================================
img1 = img.copy()
draw1 = ImageDraw.Draw(img1)
spacing = 80
for y in range(0, h + spacing, spacing):
    for x in range(0, w + spacing, spacing):
        offset = spacing // 2 if (y // spacing) % 2 else 0
        x1 = x + offset
        # Triangle connections
        draw1.line([(x1, y), (x1 + spacing, y)], fill=(200, 220, 255), width=2)
        draw1.line([(x1, y), (x1 + spacing//2, y + spacing)], fill=(200, 220, 255), width=2)
        draw1.line([(x1 + spacing, y), (x1 + spacing//2, y + spacing)], fill=(200, 220, 255), width=2)
img1.save(f"{out_dir}\\paolo_sheet_TRIANGLEMESH.png")
print("1: Triangle mesh wireframe - DONE")

# =============================================
# 2. DIAGONAL CROSSHATCH (like pencil sketch overlay)
# =============================================
img2 = img.copy()
draw2 = ImageDraw.Draw(img2)
spacing2 = 40
# Diagonal lines going right
for i in range(-h, w + h, spacing2):
    draw2.line([(i, 0), (i + h, h)], fill=(255, 255, 255, 180), width=2)
# Diagonal lines going left
for i in range(-h, w + h, spacing2):
    draw2.line([(i + h, 0), (i, h)], fill=(255, 255, 255, 180), width=2)
img2.save(f"{out_dir}\\paolo_sheet_CROSSHATCH.png")
print("2: Diagonal crosshatch - DONE")

# =============================================
# 3. RGB CHANNEL SHIFT (glitch art style)
# =============================================
arr3 = np.array(img)
result = np.zeros_like(arr3)
shift = 25  # pixel shift
# Red channel shifted left
result[:, :w-shift, 0] = arr3[:, shift:, 0]
# Green channel stays
result[:, :, 1] = arr3[:, :, 1]
# Blue channel shifted right
result[:, shift:, 2] = arr3[:, :w-shift, 2]
Image.fromarray(result).save(f"{out_dir}\\paolo_sheet_RGBSHIFT.png")
print("3: RGB channel shift glitch - DONE")

# =============================================
# 4. BLUEPRINT TECHNICAL (blue tint + white measurement lines)
# =============================================
img4 = img.copy()
# Blue tint
arr4 = np.array(img4).astype(np.float32)
arr4[:,:,0] = arr4[:,:,0] * 0.3  # reduce red
arr4[:,:,1] = arr4[:,:,1] * 0.4  # reduce green
arr4[:,:,2] = np.clip(arr4[:,:,2] * 1.3 + 40, 0, 255)  # boost blue
img4 = Image.fromarray(arr4.astype(np.uint8))
draw4 = ImageDraw.Draw(img4)
# Technical grid lines
for i in range(1, 12):
    x = int(w * i / 12)
    draw4.line([(x, 0), (x, h)], fill=(255, 255, 255), width=1)
    # Add tick marks
    for ty in range(0, h, 100):
        draw4.line([(x-8, ty), (x+8, ty)], fill=(255, 255, 255), width=1)
    y = int(h * i / 12)
    draw4.line([(0, y), (w, y)], fill=(255, 255, 255), width=1)
    for tx in range(0, w, 100):
        draw4.line([(tx, y-8), (tx, y+8)], fill=(255, 255, 255), width=1)
# Measurement arrows and circles on key points
for cx, cy, r in [(w//6, h//6, 120), (w//4, h//4, 80), (w*3//4, h//4, 150)]:
    draw4.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(255, 255, 255), width=2)
    draw4.line([(cx-r-30, cy), (cx-r, cy)], fill=(255, 255, 255), width=2)
    draw4.line([(cx+r, cy), (cx+r+30, cy)], fill=(255, 255, 255), width=2)
img4.save(f"{out_dir}\\paolo_sheet_BLUEPRINT.png")
print("4: Blueprint technical - DONE")

# =============================================
# 5. HEXAGONAL GRID
# =============================================
img5 = img.copy()
draw5 = ImageDraw.Draw(img5)
hex_size = 50
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
        draw5.line(points, fill=(255, 255, 255), width=2)
img5.save(f"{out_dir}\\paolo_sheet_HEXGRID.png")
print("5: Hexagonal grid - DONE")

# =============================================
# 6. OIL PAINT EFFECT (median filter + slight posterize)
# =============================================
img6 = img.copy()
# Heavy median filter for oil paint look
img6 = img6.filter(ImageFilter.MedianFilter(size=7))
# Slight edge enhancement
img6 = img6.filter(ImageFilter.EDGE_ENHANCE)
# Posterize slightly
arr6 = np.array(img6)
levels = 24
arr6 = (arr6 // (256 // levels)) * (256 // levels)
img6 = Image.fromarray(arr6)
# Add subtle grid
draw6 = ImageDraw.Draw(img6)
for i in range(1, 8):
    x = int(w * i / 8)
    draw6.line([(x, 0), (x, h)], fill=(255, 255, 255), width=3)
    y = int(h * i / 8)
    draw6.line([(0, y), (w, y)], fill=(255, 255, 255), width=3)
img6.save(f"{out_dir}\\paolo_sheet_OILPAINT.png")
print("6: Oil paint + grid - DONE")

print(f"\n6 varianti creative salvate in {out_dir}")
