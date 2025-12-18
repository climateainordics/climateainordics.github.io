#!/usr/bin/env python3
"""
Create a seamless image mosaic from URLs, cropping each image to fill its tile.
1. Scrapes HTML pages for images if one URL is provided.
2. Filters out URLs containing 'logo' or 'partner'.
3. Expands the last row to fill the width if it's incomplete.
"""

import argparse
import io
import math
import sys
from typing import List, Tuple
from urllib.parse import urljoin

import requests
from PIL import Image
from bs4 import BeautifulSoup

# ---- Your newsletter images (default) ----
DEFAULT_URLS = [
    "https://climateainordics.com/images/posts/2025-08-25-bayesian-optimization-against-climate-change-1.png",
    "https://climateainordics.com/images/posts/2025-08-12-ai-environment-summit.jpg",
    "https://climateainordics.com/images/people/miki-verma.jpg",
    "https://climateainordics.com/images/posts/2025-08-18-2025-09-11-generative-domain-adaptation-and-foundation-models.jpg",
    "https://climateainordics.com/images/posts/2025-08-21-2025-10-23-self-supervised-pre-training-for-glacier-calving-front.jpg",
    "https://climateainordics.com/images/posts/sweo2025logo.png", # This will now be filtered out
    "https://climateainordics.com/images/posts/2025-08-26-2025-09-17-short-course.png",
    "https://climateainordics.com/images/posts/2025-08-18-2025-08-26-esa-phi-lab-sweden-opening.png",
    "https://climateainordics.com/images/posts/2025-08-26-norway-ai-centers.webp",
]

# Keywords to exclude from the mosaic
EXCLUDE_KEYWORDS = ["logo", "partner"]

# ---- Helpers ----
def parse_size(s: str) -> Tuple[int, int]:
    try:
        w, h = s.lower().split("x")
        return int(w), int(h)
    except Exception:
        raise argparse.ArgumentTypeError("Size must be like 1800x1200")

def filter_urls(urls: List[str]) -> List[str]:
    """Filters out URLs containing excluded keywords."""
    filtered = []
    for url in urls:
        if any(kw in url.lower() for kw in EXCLUDE_KEYWORDS):
            continue
        filtered.append(url)
    return filtered

def scrape_images_from_url(page_url: str) -> List[str]:
    """Fetches HTML from a URL and extracts all image source URLs."""
    print(f"Fetching page: {page_url}...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        response = requests.get(page_url, headers=headers, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching page: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')
    found_urls = []

    # Common image extensions to filter
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            full_url = urljoin(page_url, src)
            # Filter for extensions
            if any(full_url.lower().endswith(ext) for ext in valid_exts):
                if full_url not in found_urls:
                    found_urls.append(full_url)

    return found_urls

def cover_resize_crop(im: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """Resize using 'cover' behavior and center-crop to exactly (target_w, target_h)."""
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
    """Choose rows, cols for a near-square grid for n images."""
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

    total_gutter_y = (rows - 1) * gutter
    tile_h = (out_h - total_gutter_y) // rows

    canvas = Image.new("RGB", (out_w, out_h), (0, 0, 0))

    remainder = n % cols

    for idx, url in enumerate(urls):
        r = idx // cols
        c = idx % cols

        # Determine how many items are in this specific row
        is_last_row = (r == rows - 1)
        items_in_this_row = remainder if (is_last_row and remainder > 0) else cols

        # Recalculate width for this specific row (Justified layout)
        total_gutter_x = (items_in_this_row - 1) * gutter
        tile_w = (out_w - total_gutter_x) // items_in_this_row

        x = c * (tile_w + gutter)
        y = r * (tile_h + gutter)

        print(f"[{idx+1}/{n}] Processing: {url.split('/')[-1]}")
        try:
            im = fetch_image(url)
            tile = cover_resize_crop(im, tile_w, tile_h)
        except Exception as e:
            print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)
            tile = Image.new("RGB", (tile_w, tile_h), (30, 30, 30))

        canvas.paste(tile, (x, y))

    return canvas

# ---- CLI ----
def main():
    parser = argparse.ArgumentParser(description="Create a seamless, cropped image mosaic.")
    parser.add_argument("--out", default="mosaic.jpg", help="Output file path.")
    parser.add_argument("--size", type=parse_size, default=(1800, 1800), help="Mosaic size (WxH).")
    parser.add_argument("--gutter", type=int, default=0, help="Pixels between tiles.")
    parser.add_argument("urls", nargs="*", help="Image URLs or a single HTML URL.")
    args = parser.parse_args()

    # Determine initial list
    if len(args.urls) == 1:
        single_url = args.urls[0]
        # Scrape if it's not a direct image link
        if not any(single_url.lower().endswith(ext) for ext in ('.jpg', '.jpeg', '.png', '.webp')):
            raw_urls = scrape_images_from_url(single_url)
        else:
            raw_urls = [single_url]
    elif len(args.urls) > 1:
        raw_urls = args.urls
    else:
        raw_urls = DEFAULT_URLS

    # APPLY FILTER (Logo/Partner)
    urls = filter_urls(raw_urls)

    if not urls:
        print("Error: No valid images found (they may have been filtered out).")
        sys.exit(1)

    print(f"\nUsing {len(urls)} images:")
    for u in urls:
        print(f"  - {u}")
    print("-" * 30)

    # Build and Save
    mosaic = build_mosaic(urls, args.size, gutter=args.gutter)

    ext = args.out.split(".")[-1].lower()
    if ext in ("jpg", "jpeg"):
        mosaic.save(args.out, quality=92, subsampling=1, optimize=True)
    else:
        mosaic.save(args.out)
    print(f"\nSaved mosaic to {args.out}")

if __name__ == "__main__":
    main()

