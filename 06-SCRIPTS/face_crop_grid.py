from PIL import Image, ImageDraw
import numpy as np

# Apri la foto originale di Paolo
img = Image.open(r"C:\Users\prova\Desktop\PORTFOLIO TOTALE\portfolio-v2\673a0bbf69782.r_d.1971-1343-2050.png")
w, h = img.size

# Crop generoso della faccia e spalle (zona superiore dell'immagine)
# La foto mostra Paolo dal busto in su, braccia incrociate
# Croppiamo la zona testa/faccia con un po' di margine
face_crop = img.crop((w*0.2, 0, w*0.75, h*0.65))

# Ridimensiona a buona risoluzione
face_crop = face_crop.resize((1024, 1024), Image.LANCZOS)

# Aggiungi grid pesante 8x8
draw = ImageDraw.Draw(face_crop)
for i in range(1, 8):
    x = int(1024 * i / 8)
    draw.line([(x, 0), (x, 1024)], fill=(255, 255, 255), width=5)
    y = int(1024 * i / 8)
    draw.line([(0, y), (1024, y)], fill=(255, 255, 255), width=5)

face_crop.save(r"C:\Users\prova\Desktop\SEEDANCE PROMPT\paolo_FACE_GRID.png")
print("Face crop con grid - DONE (1024x1024)")

# Versione con grid + noise
arr = np.array(face_crop)
noise = np.random.randint(-40, 40, arr.shape, dtype=np.int16)
noisy = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
img_noisy = Image.fromarray(noisy)
draw2 = ImageDraw.Draw(img_noisy)
for i in range(1, 8):
    x = int(1024 * i / 8)
    draw2.line([(x, 0), (x, 1024)], fill=(255, 255, 255), width=5)
    y = int(1024 * i / 8)
    draw2.line([(0, y), (1024, y)], fill=(255, 255, 255), width=5)
img_noisy.save(r"C:\Users\prova\Desktop\SEEDANCE PROMPT\paolo_FACE_GRID_NOISE.png")
print("Face crop con grid+noise - DONE (1024x1024)")
