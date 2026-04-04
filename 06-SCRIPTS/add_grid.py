from PIL import Image, ImageDraw

# Apri la CHARACTER SHEET
img = Image.open(r"C:\Users\prova\Desktop\PORTFOLIO TOTALE\portfolio-v2\hf_20260330_203211_60845516-53e2-46be-a613-4c0403e44d2c.png")
draw = ImageDraw.Draw(img)

w, h = img.size
color = (255, 255, 255, 220)
line_width = 4

# Griglia 6x6 per coprire bene tutti i pannelli
for i in range(1, 6):
    x = int(w * i / 6)
    draw.line([(x, 0), (x, h)], fill=color, width=line_width)
    y = int(h * i / 6)
    draw.line([(0, y), (w, y)], fill=color, width=line_width)

output_path = r"C:\Users\prova\Desktop\SEEDANCE PROMPT\paolo_charsheet_grid.png"
img.save(output_path)
print(f"Salvato: {output_path}")
print(f"Dimensioni: {w}x{h}")
