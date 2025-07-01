# Batch Image Scaling Script

This project provides a simple Python script to batch scale images for web use. It supports scaling by percentage or to a maximum width or height, while maintaining the aspect ratio. The script uses the Pillow library for image processing.

## Features
- Batch process all PNG, JPG, and JPEG images in a folder
- Scale images by percentage or to a maximum width/height
- Maintains aspect ratio
- Optimizes images for web (quality=85)
- Logs progress and details for each image

## Installation

1. Clone this repository or download the script files.
2. Install the required Python package:

```
pip install -r requirements.txt
```

## Usage

Run the script from the command line:

### Scale by Percentage
```
python batch-scale.py <input_dir> <output_dir> --scale 50
```
This will scale all images in `<input_dir>` to 50% of their original size and save them to `<output_dir>`.

### Scale to Maximum Width
```
python batch-scale.py <input_dir> <output_dir> --max-width 1280
```
This will scale all images so their width does not exceed 1280 pixels, maintaining aspect ratio.

### Scale to Maximum Height
```
python batch-scale.py <input_dir> <output_dir> --max-height 720
```
This will scale all images so their height does not exceed 720 pixels, maintaining aspect ratio.

## Notes
- Only images with `.png`, `.jpg`, or `.jpeg` extensions are processed.
- The output directory will be created if it does not exist.
- The script prints the name, original size, new size, and output path for each processed image. 