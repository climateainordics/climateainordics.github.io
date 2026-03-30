#!/usr/bin/env python3
"""
Create a seamless image mosaic from all <img> elements on a given web page.

Usage:
    python mosaic.py --out mosaic.jpg --size 1800x1800 https://example.com/page.html

Notes:
- Collects images from <img src>, lazy-loading attributes (data-src, data-original),
  and srcset/data-srcset (chooses the largest candidate).
- Relative URLs are resolved against the page URL.
- Images that fail to download are skipped (a blank tile is shown instead).
"""

import argparse
import io
import math
import sys
from typing import List, Tuple, Set
import requests
from PIL import Image
from urllib.parse import urljoin
from bs4 import BeautifulSoup

FORBIDDEN_WORDS = ['logo', 'partners']

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
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Python/requests (mosaic-image-fetcher)"
    }
    r = requests.get(url, timeout=20, headers=headers)
    r.raise_for_status()
    im = Image.open(io.BytesIO(r.content)).convert("RGB")
    return im

def parse_srcset(srcset: str) -> List[str]:
    """
    Parse a srcset string into a list of URLs, ordered by descriptor (largest first).
    Example: "a.jpg 320w, b.jpg 640w, c.jpg 1024w" -> ['c.jpg','b.jpg','a.jpg']
    If descriptors missing, keep original order.
    """
    candidates = []
    for part in srcset.split(","):
        item = part.strip()
        if not item:
            continue
        tokens = item.split()
        url = tokens[0]
        desc = tokens[1] if len(tokens) > 1 else ""
        # Extract numeric width/scale if present (e.g., 1024w or 2x)
        score = 0
        if desc.endswith("w"):
            try:
                score = int(desc[:-1])
            except ValueError:
                score = 0
        elif desc.endswith("x"):
            try:
                # Prefer higher DPR first; multiply by 1000 to outrank widths if mixed
                score = int(float(desc[:-1]) * 1000)
            except ValueError:
                score = 0
        candidates.append((score, url))
    # Sort by score desc, then by original order if equal
    candidates.sort(key=lambda t: t[0], reverse=True)
    return [u for _, u in candidates] if candidates else []

def extract_image_urls(page_url: str) -> List[str]:
    """
    Fetch the HTML at page_url and return a list of absolute image URLs found in <img> tags.
    Handles src, data-src, data-original, srcset, data-srcset. Deduplicates while preserving order.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Python/requests (mosaic-page-scraper)"
    }
    resp = requests.get(page_url, timeout=20, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    seen: Set[str] = set()
    ordered_urls: List[str] = []

    def add(url_rel: str):
        if not url_rel:
            return
        abs_url = urljoin(page_url, url_rel)
        # Basic guard against data: URIs or non-http(s)
        if not abs_url.lower().startswith(("http://", "https://")):
            return
        if abs_url not in seen:
            seen.add(abs_url)
            ordered_urls.append(abs_url)

    for img in soup.find_all("img"):
        # Prefer the largest candidate from srcset/data-srcset if available
        srcset = img.get("srcset") or img.get("data-srcset")
        if srcset:
            for candidate in parse_srcset(srcset):
                add(candidate)
            # If we had srcset, we already added candidates from largest to smaller;
            # still consider 'src' as a fallback at the end.
        # Lazy-load & common attributes
        for key in ("src", "data-src", "data-original", "data-lazy-src"):
            add(img.get(key))

    print('before filtering:',ordered_urls)
    ordered_urls = [u for u in ordered_urls if not any([(w in u) for w in FORBIDDEN_WORDS])]
    print('after filtering:',ordered_urls)
    return ordered_urls

def build_mosaic(urls: List[str], out_size: Tuple[int, int], gutter: int = 0) -> Image.Image:
    n = len(urls)
    if n == 0:
        raise ValueError("No image URLs found on the page")

    rows, cols = best_grid(n)
    out_w, out_h = out_size

    # Compute standard tile size
    total_gutter_x = (cols - 1) * gutter
    total_gutter_y = (rows - 1) * gutter
    
    # Standard dimensions for full rows
    std_tile_w = (out_w - total_gutter_x) // cols
    tile_h = (out_h - total_gutter_y) // rows

    canvas = Image.new("RGB", (out_w, out_h), (0, 0, 0))

    # Calculate the index of the last row
    max_r = (n - 1) // cols

    for idx, url in enumerate(urls):
        r = idx // cols
        c = idx % cols
        
        # Default vertical position
        y = r * (tile_h + gutter)

        # Logic to handle the last row specifically
        if r == max_r:
            # Calculate how many items are actually in this last row
            # If n % cols is 0, the row is full (count = cols). 
            # Otherwise, it's the remainder.
            remainder = n % cols
            items_in_last_row = remainder if remainder > 0 else cols

            # Recalculate width for this row to fill the canvas
            last_row_gutter_total = (items_in_last_row - 1) * gutter
            current_tile_w = (out_w - last_row_gutter_total) // items_in_last_row
            
            # Recalculate X position based on the new width
            x = c * (current_tile_w + gutter)
        else:
            # Standard grid logic for non-last rows
            current_tile_w = std_tile_w
            x = c * (std_tile_w + gutter)

        try:
            im = fetch_image(url)
            # Use the calculated current_tile_w
            tile = cover_resize_crop(im, current_tile_w, tile_h)
        except Exception as e:
            print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)
            tile = Image.new("RGB", (current_tile_w, tile_h), (30, 30, 30))
    
        canvas.paste(tile, (x, y))

    return canvas

def build_mosaic_old(urls: List[str], out_size: Tuple[int, int], gutter: int = 0) -> Image.Image:
    n = len(urls)
    if n == 0:
        raise ValueError("No image URLs found on the page")

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
            tile = cover_resize_crop(im, tile_w, tile_h)
        except Exception as e:
            print(f"Warning: failed to fetch {url}: {e}", file=sys.stderr)
            # Use a blank tile if fetch fails
            tile = Image.new("RGB", (tile_w, tile_h), (30, 30, 30))

        canvas.paste(tile, (x, y))

    return canvas

# ---- CLI ----
def main():
    parser = argparse.ArgumentParser(
        description="Create a seamless, cropped image mosaic from all images on a web page."
    )
    parser.add_argument("--out", default="mosaic.jpg", help="Output file path (jpg/png/webp).")
    parser.add_argument("--size", type=parse_size, default=(1800, 1800),
                        help="Final mosaic size, e.g., 1800x1800.")
    parser.add_argument("--gutter", type=int, default=0,
                        help="Pixels between tiles (default 0 for seamless).")
    parser.add_argument("page_url", help="A single web page URL to scrape for images.")
    args = parser.parse_args()

    # Enforce exactly one URL (argparse ensures presence; we ensure it's not empty string)
    page_url = args.page_url.strip()
    if not page_url:
        parser.error("You must provide exactly one non-empty web page URL.")

    try:
        urls = extract_image_urls(page_url)
    except Exception as e:
        print(f"Error fetching/parsing page: {e}", file=sys.stderr)
        sys.exit(1)

    if not urls:
        print("No images found on the page.", file=sys.stderr)
        sys.exit(2)

    mosaic = build_mosaic(urls, args.size, gutter=args.gutter)
    # Choose format from extension
    ext = args.out.split(".")[-1].lower()
    try:
        if ext in ("jpg", "jpeg"):
            mosaic.save(args.out, quality=92, subsampling=1, optimize=True)
        else:
            mosaic.save(args.out)
    except Exception as e:
        print(f"Failed to save output image: {e}", file=sys.stderr)
        sys.exit(3)

    print(f"Found {len(urls)} images.")
    print(f"Saved mosaic to {args.out}")

if __name__ == "__main__":
    main()


