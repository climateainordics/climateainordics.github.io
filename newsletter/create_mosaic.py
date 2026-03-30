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
import numpy as np
EASYOCR_AVAILABLE = True

try:
    import easyocr
    # Initialize Reader; this may also fail if model weights can't be downloaded
    READER = easyocr.Reader(['en'])
except Exception as e:
    print(f"Notice: EasyOCR not initialized ({e}). Falling back to standard cropping.", file=sys.stderr)
    EASYOCR_AVAILABLE = False


FORBIDDEN_WORDS = ['logo', 'partners', 'posts/newsletter', 'nordic-workshop-2026']

# ---- Helpers ----
def parse_size(s: str) -> Tuple[int, int]:
    try:
        w, h = s.lower().split("x")
        return int(w), int(h)
    except Exception:
        raise argparse.ArgumentTypeError("Size must be like 1800x1200")

def get_safe_crop(im: Image.Image) -> Image.Image:
    """
    Returns a version of the image cropped to the boundary of all
    detected text (plus a margin). If no text, returns original.
    """
    if not EASYOCR_AVAILABLE:
        return im

    try:
        img_np = np.array(im)
        # We need the bounding boxes (detail=1)
        results = READER.readtext(img_np, detail=1)

        if not results:
            return im

        # Extract all corner points from all text blocks
        all_points = []
        for (bbox, text, prob) in results:
            all_points.extend(bbox)

        # Find the min/max bounds
        t_left = min(p[0] for p in all_points)
        t_top = min(p[1] for p in all_points)
        t_right = max(p[0] for p in all_points)
        t_bottom = max(p[1] for p in all_points)

        # Add a 10% padding so text isn't flush against the tile edge
        w, h = im.size
        pad_w = int(w * 0.1)
        pad_h = int(h * 0.1)

        crop_box = (
            max(0, t_left - pad_w),
            max(0, t_top - pad_h),
            min(w, t_right + pad_w),
            min(h, t_bottom + pad_h)
        )

        return im.crop(crop_box)
    except Exception:
        return im

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
    target_w, _ = out_size
    processed_images = []

    print(f"Processing {len(urls)} images...")
    for url in urls:
        try:
            im = fetch_image(url)
            im = get_safe_crop(im)
            processed_images.append(im)
        except Exception as e:
            print(f"Skipping {url}: {e}")

    if not processed_images:
        raise ValueError("No images to process.")

    # 1. Distribute images into rows
    # Target a row height that keeps the mosaic roughly square
    avg_row_height = out_size[1] / math.sqrt(len(processed_images))
    rows = []
    current_row = []
    current_row_width = 0

    for im in processed_images:
        aspect = im.width / im.height
        norm_w = avg_row_height * aspect
        current_row.append(im)
        current_row_width += norm_w + gutter
        if current_row_width >= target_w:
            rows.append(current_row)
            current_row = []
            current_row_width = 0

    if current_row:
        rows.append(current_row)

    # 2. Calculate row heights and total canvas height
    row_data = []
    total_h = 0
    for i, row in enumerate(rows):
        row_aspect_sum = sum(im.width / im.height for im in row)
        usable_w = target_w - (gutter * (len(row) - 1))
        row_h = int(usable_w / row_aspect_sum)

        # Cap last row height to avoid "Giant Image" syndrome
        is_last = (i == len(rows) - 1)
        if is_last and len(rows) > 1:
            avg_h = sum(d['h'] for d in row_data) / len(row_data)
            if row_h > avg_h * 1.5:
                row_h = int(avg_h)

        row_data.append({'images': row, 'h': row_h, 'is_last': is_last})
        total_h += row_h + (gutter if not is_last else 0)

    # 3. Render with pixel-gap correction
    canvas = Image.new("RGB", (target_w, total_h), (255, 255, 255))
    curr_y = 0

    for data in row_data:
        row_h = data['h']
        curr_x = 0

        for j, im in enumerate(data['images']):
            # Calculate width based on the row height
            img_w = int(row_h * (im.width / im.height))

            # --- PIXEL-PERFECT CORRECTION ---
            # If this is the last image in a FULL row,
            # make it fill exactly to the target_w edge.
            is_last_in_row = (j == len(data['images']) - 1)
            if is_last_in_row and not (data['is_last'] and curr_x + img_w < target_w * 0.8):
                img_w = target_w - curr_x
            # --------------------------------

            tile = im.resize((img_w, row_h), Image.LANCZOS)
            canvas.paste(tile, (curr_x, curr_y))
            curr_x += img_w + gutter

        curr_y += row_h + gutter

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


