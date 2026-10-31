#!/usr/bin/env python3
"""
Prepare backpacking photos for the al-folio gallery page.

  pip install pillow pyyaml
  python3 prep_gallery.py path/to/originals

Run from the root of your al-folio repo. For every image in the folder it:
  * fixes rotation from camera EXIF data (common with older cameras)
  * strips metadata, including GPS locations
  * writes a full-size web copy  -> assets/img/gallery/<name>.jpg
  * writes a small grid thumbnail -> assets/img/gallery/thumbs/<name>.jpg
  * records width/height in _data/gallery.yml so the page can lay photos out
    by their real aspect ratio (panoramas included)

Re-running is safe: captions and the order you set in _data/gallery.yml are
kept, new photos are added at the end, and deleted photos are removed.
"""
import pathlib
import sys

import yaml
from PIL import Image, ImageOps

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "originals")
OUT = pathlib.Path("assets/img/gallery")
THUMBS = OUT / "thumbs"
DATA = pathlib.Path("_data/gallery.yml")

FULL_MAX_EDGE = 2400     # long edge for normal photos in the lightbox
PANO_MAX_HEIGHT = 1600   # panoramas are capped by height instead...
PANO_MAX_WIDTH = 7000    # ...and by a sane max width
PANO_RATIO = 2.2         # width/height above this counts as a panorama
THUMB_HEIGHT = 600       # grid rows are ~240px tall; 600 stays sharp on retina
QUALITY = 82
EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}


def scaled(img, max_w, max_h):
    w, h = img.size
    s = min(1.0, max_w / w, max_h / h)
    if s < 1.0:
        img = img.resize((round(w * s), round(h * s)), Image.LANCZOS)
    return img


def save(img, path):
    img.save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True)


def main():
    if not SRC.is_dir():
        sys.exit(f"Folder not found: {SRC}")
    THUMBS.mkdir(parents=True, exist_ok=True)
    DATA.parent.mkdir(parents=True, exist_ok=True)

    old = []
    if DATA.exists():
        old = yaml.safe_load(DATA.read_text()) or []
    old_by_name = {e["name"]: e for e in old if "name" in e}

    built = {}
    for src in sorted(SRC.iterdir()):
        if src.suffix.lower() not in EXTS:
            continue
        name = src.stem.lower().replace(" ", "-") + ".jpg"
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            w, h = im.size
            if w / h >= PANO_RATIO:
                full = scaled(im, PANO_MAX_WIDTH, PANO_MAX_HEIGHT)
            else:
                full = scaled(im, FULL_MAX_EDGE, FULL_MAX_EDGE)
            thumb = scaled(im, 10_000, THUMB_HEIGHT)
            save(full, OUT / name)
            save(thumb, THUMBS / name)
        prev = old_by_name.get(name, {})
        built[name] = {
            "name": name,
            "full": f"/assets/img/gallery/{name}",
            "thumb": f"/assets/img/gallery/thumbs/{name}",
            "width": full.width,
            "height": full.height,
            "caption": prev.get("caption", ""),
        }
        kind = "pano" if w / h >= PANO_RATIO else "photo"
        print(f"{kind:5}  {src.name} -> {name} ({full.width}x{full.height})")

    # keep the existing order, then append new photos
    order = [e["name"] for e in old if e.get("name") in built]
    order += [n for n in built if n not in order]
    entries = [built[n] for n in order]

    DATA.write_text(yaml.safe_dump(entries, sort_keys=False, allow_unicode=True))
    print(f"\n{len(entries)} photos written to {DATA}")


if __name__ == "__main__":
    main()
