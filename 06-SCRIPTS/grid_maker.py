#!/usr/bin/env python3
"""
SeedForge / FaceForge Grid Maker — Applies grid overlays and texture effects
to bypass Seedance 2.0 face detection.

PRIMARY METHOD (proven in production):
  8x8 white grid overlay with thick lines drawn ON TOP of the image.
  This breaks facial feature patterns enough to drop detection confidence
  below the blocking threshold, while Seedance still reads the character.

FALLBACK METHODS (if 8x8 grid is blocked):
  --style grid10_noise    10x10 grid + noise
  --style hexgrid         Hexagonal grid pattern
  --style crosshatch      Diagonal crosshatch lines
  --style noise           Heavy noise only (no grid)
  --style facecrop        Crop face region + 8x8 grid
  --style oilpaint        Oil paint effect + grid
  --style blueprint       Blue tint + technical grid

Usage:
    python grid_maker.py input.png output.png                      (default: 8x8 grid)
    python grid_maker.py input.png output.png --style grid10_noise (fallback)
    python grid_maker.py input.png output.png --style all          (generate ALL variants)
    python grid_maker.py input.png --face-crop output.png          (crop face + grid)
"""

import sys
import os
import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
    import numpy as np
except ImportError:
    print("ERROR: Pillow and numpy required. Install with: pip install Pillow numpy")
    sys.exit(1)


# =============================================================================
# PRIMARY METHOD — 8x8 Grid Overlay (PROVEN WINNER)
# =============================================================================

def grid_8x8(img: Image.Image, line_width: int = 6) -> Image.Image:
    """
    Draw an 8x8 white grid overlay on the image.
    This is the method that passed face detection in real production tests.
    Grid density 8x8 + line width 6px breaks facial patterns reliably.
    6x6 was tested and FAILED — not dense enough.
    """
    out = img.copy()
    draw = ImageDraw.Draw(out)
    w, h = out.size
    for i in range(1, 8):
        x = int(w * i / 8)
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255), width=line_width)
        y = int(h * i / 8)
        draw.line([(0, y), (w, y)], fill=(255, 255, 255), width=line_width)
    return out


# =============================================================================
# FALLBACK METHODS — Try these if 8x8 grid gets blocked
# =============================================================================

def grid_10x10_noise(img: Image.Image) -> Image.Image:
    """10x10 denser grid + noise (+-35). More disruption than 8x8."""
    arr = np.array(img)
    noise = np.random.randint(-35, 35, arr.shape, dtype=np.int16)
    arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    out = Image.fromarray(arr)
    draw = ImageDraw.Draw(out)
    w, h = out.size
    for i in range(1, 10):
        x = int(w * i / 10)
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255), width=5)
        y = int(h * i / 10)
        draw.line([(0, y), (w, y)], fill=(255, 255, 255), width=5)
    return out


def hexgrid(img: Image.Image, hex_size: int = 45) -> Image.Image:
    """Hexagonal grid — non-rectangular pattern, harder for detectors."""
    out = img.copy()
    draw = ImageDraw.Draw(out)
    w, h = out.size
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
            draw.line(points, fill=(255, 255, 255), width=3)
    return out


def crosshatch(img: Image.Image, spacing: int = 40) -> Image.Image:
    """Diagonal crosshatch lines — pencil sketch effect."""
    out = img.copy()
    draw = ImageDraw.Draw(out)
    w, h = out.size
    for i in range(-h, w + h, spacing):
        draw.line([(i, 0), (i + h, h)], fill=(255, 255, 255), width=2)
    for i in range(-h, w + h, spacing):
        draw.line([(i + h, 0), (i, h)], fill=(255, 255, 255), width=2)
    return out


def heavy_noise(img: Image.Image, strength: int = 60) -> Image.Image:
    """Heavy noise only (+-60). Passes but lower quality output."""
    arr = np.array(img)
    noise = np.random.randint(-strength, strength, arr.shape, dtype=np.int16)
    arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


def oilpaint_grid(img: Image.Image) -> Image.Image:
    """Oil paint effect (median filter + posterize) + 8x8 grid."""
    out = img.copy()
    out = out.filter(ImageFilter.MedianFilter(size=7))
    out = out.filter(ImageFilter.EDGE_ENHANCE)
    arr = np.array(out)
    levels = 24
    arr = (arr // (256 // levels)) * (256 // levels)
    out = Image.fromarray(arr)
    draw = ImageDraw.Draw(out)
    w, h = out.size
    for i in range(1, 8):
        x = int(w * i / 8)
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255), width=3)
        y = int(h * i / 8)
        draw.line([(0, y), (w, y)], fill=(255, 255, 255), width=3)
    return out


def blueprint(img: Image.Image) -> Image.Image:
    """Blue tint + technical measurement grid with tick marks."""
    arr = np.array(img).astype(np.float32)
    arr[:, :, 0] = arr[:, :, 0] * 0.3   # reduce red
    arr[:, :, 1] = arr[:, :, 1] * 0.4   # reduce green
    arr[:, :, 2] = np.clip(arr[:, :, 2] * 1.3 + 40, 0, 255)  # boost blue
    out = Image.fromarray(arr.astype(np.uint8))
    draw = ImageDraw.Draw(out)
    w, h = out.size
    for i in range(1, 12):
        x = int(w * i / 12)
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255), width=1)
        for ty in range(0, h, 100):
            draw.line([(x - 8, ty), (x + 8, ty)], fill=(255, 255, 255), width=1)
        y = int(h * i / 12)
        draw.line([(0, y), (w, y)], fill=(255, 255, 255), width=1)
        for tx in range(0, w, 100):
            draw.line([(tx, y - 8), (tx, y + 8)], fill=(255, 255, 255), width=1)
    return out


# =============================================================================
# FACE CROP — Extract face region + apply grid
# =============================================================================

def face_crop_grid(
    img: Image.Image,
    crop_box: tuple = None,
    size: int = 1024,
) -> Image.Image:
    """
    Crop the face region from a character sheet, resize to 1024x1024,
    then apply 8x8 grid. Use as @Image2 for close-up face reference.

    crop_box: (left_pct, top_pct, right_pct, bottom_pct) as fractions 0-1.
              Default: lower-left third (where face close-ups usually are in sheets).
    """
    w, h = img.size
    if crop_box is None:
        # Default: lower-left region (common position for face close-up in sheets)
        crop_box = (0.0, 0.5, 0.34, 1.0)

    left = int(w * crop_box[0])
    top = int(h * crop_box[1])
    right = int(w * crop_box[2])
    bottom = int(h * crop_box[3])

    face = img.crop((left, top, right, bottom))
    face = face.resize((size, size), Image.LANCZOS)
    return grid_8x8(face, line_width=5)


# =============================================================================
# STYLE REGISTRY
# =============================================================================

STYLES = {
    "grid8x8":       ("Grid 8x8 (DEFAULT — proven winner)", grid_8x8),
    "grid10_noise":  ("Grid 10x10 + noise", grid_10x10_noise),
    "hexgrid":       ("Hexagonal grid", hexgrid),
    "crosshatch":    ("Diagonal crosshatch", crosshatch),
    "noise":         ("Heavy noise only", heavy_noise),
    "oilpaint":      ("Oil paint + grid", oilpaint_grid),
    "blueprint":     ("Blueprint technical", blueprint),
}


def save_image(img: Image.Image, path: str):
    """Save with appropriate format and quality."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() in (".jpg", ".jpeg"):
        img.save(str(path), "JPEG", quality=95)
    else:
        img.save(str(path), "PNG")
    size_mb = path.stat().st_size / (1024 * 1024)
    print(f"  Saved: {path} ({img.size[0]}x{img.size[1]}, {size_mb:.1f} MB)")
    if size_mb > 30:
        print(f"  WARNING: Exceeds Seedance 30MB limit! Save as JPEG or reduce size.")


def main():
    if len(sys.argv) < 3:
        print("FaceForge Grid Maker")
        print("=" * 50)
        print()
        print("Usage:")
        print("  python grid_maker.py <input> <output>                    Default: 8x8 grid overlay")
        print("  python grid_maker.py <input> <output> --style hexgrid    Use specific style")
        print("  python grid_maker.py <input> <output> --style all        Generate ALL variants")
        print("  python grid_maker.py <input> <output> --face-crop        Crop face + grid (for @Image2)")
        print()
        print("Available styles:")
        for key, (desc, _) in STYLES.items():
            marker = " <-- TRY THIS FIRST" if key == "grid8x8" else ""
            print(f"  {key:16s}  {desc}{marker}")
        print()
        print("Escalation order (if blocked, try next):")
        print("  1. grid8x8        (default, proven in production)")
        print("  2. grid10_noise   (denser grid + noise)")
        print("  3. hexgrid        (non-rectangular pattern)")
        print("  4. crosshatch     (diagonal lines)")
        print("  5. oilpaint       (style filter + grid)")
        print("  6. blueprint      (blue tint + tech grid)")
        print("  7. noise          (last resort, lower quality)")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(input_path):
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)

    # Parse options
    style = "grid8x8"
    do_face_crop = False
    crop_box = None

    i = 3
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--style" and i + 1 < len(sys.argv):
            style = sys.argv[i + 1]
            i += 2
        elif arg == "--face-crop":
            do_face_crop = True
            i += 1
        elif arg == "--crop-box" and i + 1 < len(sys.argv):
            # Format: "left,top,right,bottom" as percentages 0-1
            parts = sys.argv[i + 1].split(",")
            crop_box = tuple(float(p) for p in parts)
            i += 2
        else:
            print(f"Unknown argument: {arg}")
            sys.exit(1)

    img = Image.open(input_path).convert("RGB")
    w, h = img.size
    print(f"Input: {input_path} ({w}x{h})")

    if do_face_crop:
        print(f"\nFace crop + 8x8 grid (for @Image2)...")
        result = face_crop_grid(img, crop_box=crop_box)
        save_image(result, output_path)
        return

    if style == "all":
        # Generate ALL variants
        base = Path(output_path)
        stem = base.stem
        suffix = base.suffix or ".png"
        parent = base.parent

        print(f"\nGenerating ALL {len(STYLES)} variants...")
        for key, (desc, func) in STYLES.items():
            print(f"\n  [{key}] {desc}")
            result = func(img)
            out_path = parent / f"{stem}_{key}{suffix}"
            save_image(result, str(out_path))

        # Also generate face crop version
        print(f"\n  [facecrop] Face crop + grid")
        result = face_crop_grid(img, crop_box=crop_box)
        out_path = parent / f"{stem}_facecrop{suffix}"
        save_image(result, str(out_path))

        print(f"\nAll {len(STYLES) + 1} variants saved to {parent}")
        print(f"\nRecommended order to try:")
        print(f"  1. {stem}_grid8x8{suffix}      <-- START HERE")
        print(f"  2. {stem}_grid10_noise{suffix}")
        print(f"  3. {stem}_hexgrid{suffix}")
        print(f"  4. {stem}_crosshatch{suffix}")
        return

    if style not in STYLES:
        print(f"ERROR: Unknown style '{style}'. Available: {', '.join(STYLES.keys())}, all")
        sys.exit(1)

    desc, func = STYLES[style]
    print(f"\nApplying: {desc}...")
    result = func(img)
    save_image(result, output_path)


if __name__ == "__main__":
    main()
