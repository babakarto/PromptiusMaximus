"""Generate SeedForge logo — centered stacked layout: icon above, text below."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 600
SCALE = 4
hw, hh = W * SCALE, H * SCALE
img = Image.new("RGBA", (hw, hh), (13, 13, 18, 255))


def rounded_triangle_points(cx, cy, size, rotation_deg, corner_radius_pct=0.42):
    points = []
    corner_angles = [math.radians(rotation_deg + i * 120) for i in range(3)]
    corners = [(cx + size * math.cos(a), cy + size * math.sin(a)) for a in corner_angles]
    cr = size * corner_radius_pct

    for i in range(3):
        p_prev = corners[(i - 1) % 3]
        p_curr = corners[i]
        p_next = corners[(i + 1) % 3]

        dx1 = p_prev[0] - p_curr[0]
        dy1 = p_prev[1] - p_curr[1]
        len1 = math.sqrt(dx1**2 + dy1**2)
        dx1 /= len1; dy1 /= len1

        dx2 = p_next[0] - p_curr[0]
        dy2 = p_next[1] - p_curr[1]
        len2 = math.sqrt(dx2**2 + dy2**2)
        dx2 /= len2; dy2 /= len2

        arc_start = (p_curr[0] + dx1 * cr, p_curr[1] + dy1 * cr)
        arc_end = (p_curr[0] + dx2 * cr, p_curr[1] + dy2 * cr)

        bisect_x = dx1 + dx2
        bisect_y = dy1 + dy2
        bl = math.sqrt(bisect_x**2 + bisect_y**2)
        if bl > 0.001: bisect_x /= bl; bisect_y /= bl

        dot = dx1 * dx2 + dy1 * dy2
        half_angle = math.acos(max(-1, min(1, dot))) / 2
        center_dist = cr / math.sin(half_angle) if half_angle > 0.001 else cr

        arc_cx = p_curr[0] + bisect_x * center_dist
        arc_cy = p_curr[1] + bisect_y * center_dist

        start_a = math.atan2(arc_start[1] - arc_cy, arc_start[0] - arc_cx)
        end_a = math.atan2(arc_end[1] - arc_cy, arc_end[0] - arc_cx)
        diff = end_a - start_a
        while diff > math.pi: diff -= 2 * math.pi
        while diff < -math.pi: diff += 2 * math.pi

        arc_r = math.sqrt((arc_start[0] - arc_cx)**2 + (arc_start[1] - arc_cy)**2)
        for j in range(25):
            t = j / 24
            a = start_a + diff * t
            points.append((arc_cx + arc_r * math.cos(a), arc_cy + arc_r * math.sin(a)))

    return points


def draw_shape(img, cx, cy, size, rotation, color, alpha=240):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    pts = rounded_triangle_points(cx, cy, size, rotation)
    if not pts: return

    min_y = min(p[1] for p in pts)
    max_y = max(p[1] for p in pts)
    ry = max(1, max_y - min_y)
    light = tuple(min(255, int(c * 1.12)) for c in color)
    dark = tuple(max(0, int(c * 0.88)) for c in color)

    for y in range(int(min_y), int(max_y) + 1):
        t = (y - min_y) / ry
        r = int(light[0] + (dark[0] - light[0]) * t)
        g = int(light[1] + (dark[1] - light[1]) * t)
        b = int(light[2] + (dark[2] - light[2]) * t)
        ixs = []
        for k in range(len(pts)):
            p1 = pts[k]; p2 = pts[(k+1) % len(pts)]
            if (p1[1] <= y < p2[1]) or (p2[1] <= y < p1[1]):
                if abs(p2[1] - p1[1]) > 0.01:
                    x = p1[0] + (y - p1[1]) / (p2[1] - p1[1]) * (p2[0] - p1[0])
                    ixs.append(x)
        ixs.sort()
        for k in range(0, len(ixs) - 1, 2):
            od.line([(int(ixs[k]), y), (int(ixs[k+1]), y)], fill=(r, g, b, alpha))

    img.alpha_composite(overlay)


# ======== ICON — centered at top ========
icx = (W // 2) * SCALE
icy = 175 * SCALE
sz = 120 * SCALE

# Purple (behind)
draw_shape(img, icx + 38*SCALE, icy + 26*SCALE, sz, rotation=-30,
           color=(115, 95, 235), alpha=215)

# Teal (front)
draw_shape(img, icx, icy, sz, rotation=-30,
           color=(85, 232, 212), alpha=245)

# ======== GRID on teal ========
grid = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
sp = 18 * SCALE
lw = max(1, int(SCALE * 0.7))
gc = (255, 255, 255, 30)
for x in range(icx - sz - 10*SCALE, icx + sz + 10*SCALE, sp):
    gd.line([(x, icy - sz - 10*SCALE), (x, icy + sz + 10*SCALE)], fill=gc, width=lw)
for y in range(icy - sz - 10*SCALE, icy + sz + 10*SCALE, sp):
    gd.line([(icx - sz - 10*SCALE, y), (icx + sz + 10*SCALE, y)], fill=gc, width=lw)

mask = Image.new("L", (hw, hh), 0)
pts_m = rounded_triangle_points(icx, icy, int(sz * 0.92), -30)
ImageDraw.Draw(mask).polygon(pts_m, fill=200)
grid.putalpha(Image.composite(grid.getchannel("A"), Image.new("L", (hw, hh), 0), mask))
img.alpha_composite(grid)

# ======== SPARK ========
spark = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
sd = ImageDraw.Draw(spark)
sr = 5 * SCALE
sd.ellipse([icx-sr, icy-sr, icx+sr, icy+sr], fill=(255, 255, 255, 55))
sr2 = 2 * SCALE
sd.ellipse([icx-sr2, icy-sr2, icx+sr2, icy+sr2], fill=(255, 255, 255, 120))
img.alpha_composite(spark)

# ======== DOWNSCALE ========
img = img.resize((W, H), Image.LANCZOS)
draw = ImageDraw.Draw(img)

# ======== TEXT — centered below icon ========
font_large = None
font_tag = None
for fp in ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"]:
    try: font_large = ImageFont.truetype(fp, 100); break
    except: continue
for fp in ["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"]:
    try: font_tag = ImageFont.truetype(fp, 20); break
    except: continue

# Measure "SEEDFORGE" total width
seed_w = draw.textlength("SEED", font=font_large)
forge_w = draw.textlength("FORGE", font=font_large)
total_w = seed_w + forge_w + 5
text_x = (W - total_w) / 2
text_y = 370

draw.text((text_x, text_y), "SEED", fill=(235, 235, 240), font=font_large)
draw.text((text_x + seed_w + 5, text_y), "FORGE", fill=(80, 232, 212), font=font_large)

# Tagline centered
tag = "SEEDANCE 2.0 PROMPT ENGINE  +  FACEFORGE"
tag_w = draw.textlength(tag, font=font_tag)
draw.text(((W - tag_w) / 2, text_y + 115), tag, fill=(120, 120, 132), font=font_tag)

# ======== SAVE ========
final = Image.new("RGB", (W, H), (13, 13, 18))
final.paste(img, mask=img.getchannel("A"))
final.save("assets/seedforge-logo.png", "PNG", optimize=True)
print(f"Logo saved: assets/seedforge-logo.png ({W}x{H})")
