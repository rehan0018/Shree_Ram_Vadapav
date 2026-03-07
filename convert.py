import os
from PIL import Image
import glob

image_dir = "images"
png_files = glob.glob(os.path.join(image_dir, "*.png"))

for png_file in png_files:
    webp_file = os.path.splitext(png_file)[0] + ".webp"
    try:
        with Image.open(png_file) as im:
            im.save(webp_file, "webp", quality=80)
        print(f"Converted {png_file} to {webp_file}")
    except Exception as e:
        print(f"Error converting {png_file}: {e}")
