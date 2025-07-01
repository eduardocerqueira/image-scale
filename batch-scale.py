#!/usr/bin/env python3

"""
Batch Image Scaling Script

This script batch scales images for web use. It supports scaling by percentage
or to a maximum width/height while maintaining aspect ratio.

Usage: python batch-scale.py <input_dir> <output_dir> --scale 50
       python batch-scale.py <input_dir> <output_dir> --max-width 1280
       python batch-scale.py <input_dir> <output_dir> --max-height 720
"""

import os
from PIL import Image
import argparse
import logging

def scale_image(input_path, output_path, scale_percentage=None, max_width=None, max_height=None):
    with Image.open(input_path) as img:
        orig_width, orig_height = img.size
        if scale_percentage:
            new_width = int(orig_width * scale_percentage / 100)
            new_height = int(orig_height * scale_percentage / 100)
        elif max_width or max_height:
            # Maintain aspect ratio
            ratio = 1.0
            if max_width and orig_width > max_width:
                ratio = min(ratio, max_width / orig_width)
            if max_height and orig_height > max_height:
                ratio = min(ratio, max_height / orig_height)
            new_width = int(orig_width * ratio)
            new_height = int(orig_height * ratio)
        else:
            raise ValueError("Either scale_percentage or max_width/max_height must be provided.")
        logging.info(f"Processing: {os.path.basename(input_path)} | Original size: {orig_width}x{orig_height} -> New size: {new_width}x{new_height}")
        img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(output_path, optimize=True, quality=85)
        logging.info(f"Saved: {output_path}\n")

def batch_scale_images(input_dir, output_dir, scale_percentage=None, max_width=None, max_height=None):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            scale_image(input_path, output_path, scale_percentage, max_width, max_height)

def main():
    parser = argparse.ArgumentParser(description="Batch scale images for web use.")
    parser.add_argument("input_dir", help="Input folder with images")
    parser.add_argument("output_dir", help="Output folder for scaled images")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scale", type=int, help="Scale percentage (e.g., 50 for 50%)")
    group.add_argument("--max-width", type=int, help="Maximum width in pixels")
    group.add_argument("--max-height", type=int, help="Maximum height in pixels")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(message)s')
    batch_scale_images(
        args.input_dir,
        args.output_dir,
        scale_percentage=args.scale,
        max_width=args.max_width,
        max_height=args.max_height
    )

if __name__ == "__main__":
    main()