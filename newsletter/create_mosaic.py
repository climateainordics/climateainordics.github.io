#!/usr/bin/env python3
"""
Create a seamless image mosaic from URLs, cropping each image to fill its tile.

Usage (with the provided newsletter images):
    python mosaic.py --out mosaic.jpg --size 1800x1800

You can also pass your own URLs:
    python mosaic.py --out mosaic.jpg --size 2000x1200 \
        https://example.com/a.jpg https://example.com/b.jpg ...
"""

import argparse
import io
import math
import sys
from typing import List, Tuple
import requests
from PIL import Image

# ---- Your newsletter images (default) ----
DEFAULT_URLS = [
    "https://climateainordics.com/images/posts/2025-08-25-bayesian-optimization-against-climate-change-1.png",
    "https://climateainordics.com/images/posts/2025-08-12-ai-environment-summit.jpg",
    "https://climateainordics.com/images/people/miki-verma.jpg",
    "https://climateainordics.com/images/posts/2025-08-18-2025-09-11-generative-domain-adaptation-and-foundation-models.jpg",
    "https://climateainordics.com/images/posts/2025-08-21-2025-10-23-self-supervised-pre-training-for-glacier-calving-front.jpg",
    "https://climateainordics.com/images/posts/sweo2025logo.png",
    "https://climateainordics.com/images/posts/2025-08-26-2025-09-17-short-course.png",
    "https://climateainordics.com/images/posts/2025-08-18-2025-08-26-esa-phi-lab-sweden-opening.png",
    "https://climateainordics.com/images/posts/2025-08-26-norway-ai-centers.webp",
]

# ---- Helpers ----
def parse_size(s: str) -> Tuple[int, int]:
    try:
        w, h = s.lower().split("x")
        return int(w), int(h)
    except Exception:
        raise argparse.ArgumentTypeError("Size must be like 1800x1200")

def cover_resize_crop(im: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """
    Resize using 'cover' behavior and center-crop to exactly (target_w, target_h).
    """
    src_w, src_h = im.size
    scale = max(target_w / src_w, target_h / src_h)
    new_w, new_h = int(math.ceil(src_w * scale)), int(math.ceil(src_h * scale))
    im_resized = im.resize((new_w, new_h), Image.LANCZOS)

    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    right = left + target_w
    bottom = top + target_h
    return im_resized.crop((left, top, right, bottom))

def best_grid(n: int) -> Tuple[int, int]:
    """
    Choose rows, cols for a near-square grid for n images.
    """
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n / cols)
    return rows, cols

def fetch_image(url: str) -> Image.Image:
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    im = Image.open(io.BytesIO(r.content)).convert("RGB")
    return im

def build_mosaic(urls: List[str], out_size: Tuple[int, int], gutter: int = 0) -> Image.Image:
    n = len(urls)
    if n == 0:
        raise ValueError("No image URLs provided")

    rows, cols = best_grid(n)
    out_w, out_h = out_size

    # Compute tile size accounting for gutters (default 0 for seamless mosaic)
    total_gutter_x = (cols - 1) * gutter
    total_gutter_y = (rows - 1) * gutter
    tile_w = (out_w - total_gutter_x) // cols
    tile_h = (out_h - total_gutter_y) // rows

    canvas = Image.new("RGB", (out_w, out_h), (0, 0, 0))

    for idx, url in enumerate(urls):
        r = idx // cols
        c = idx % cols
        x = c * (tile_w + gutter)
        y = r * (tile_h + gutter)

        try:
            im = fetch_image(url)
        except Exception as e:
            print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)
            # Use a blank tile if fetch fails
            tile = Image.new("RGB", (tile_w, tile_h), (30, 30, 30))
        else:
            tile = cover_resize_crop(im, tile_w, tile_h)

        canvas.paste(tile, (x, y))

    return canvas

# ---- CLI ----
def main():
    parser = argparse.ArgumentParser(description="Create a seamless, cropped image mosaic.")
    parser.add_argument("--out", default="mosaic.jpg", help="Output file path (jpg/png/webp).")
    parser.add_argument("--size", type=parse_size, default=(1800, 1800),
                        help="Final mosaic size, e.g., 1800x1800.")
    parser.add_argument("--gutter", type=int, default=0,
                        help="Pixels between tiles (default 0 for seamless).")
    parser.add_argument("urls", nargs="*", help="Image URLs. If empty, uses the newsletter defaults.")
    args = parser.parse_args()

    urls = args.urls if args.urls else DEFAULT_URLS
    mosaic = build_mosaic(urls, args.size, gutter=args.gutter)
    # Choose format from extension
    ext = args.out.split(".")[-1].lower()
    if ext in ("jpg", "jpeg"):
        mosaic.save(args.out, quality=92, subsampling=1, optimize=True)
    else:
        mosaic.save(args.out)
    print(f"Saved mosaic to {args.out}")

if __name__ == "__main__":
    main()

