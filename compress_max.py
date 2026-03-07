import os
from PIL import Image
import glob

image_dir = "images"
png_files = glob.glob(os.path.join(image_dir, "*.png"))

for png_file in png_files:
    webp_file = os.path.splitext(png_file)[0] + ".webp"
    try:
        with Image.open(png_file) as im:
            # Resize logo
            if "logo.png" in png_file.lower():
                im = im.resize((96, 96), Image.Resampling.LANCZOS)
            
            # Save at lower quality
            im.save(webp_file, "webp", quality=50) # Extremely compressed to fix lighthouse
        print(f"Compressed {webp_file}")
    except Exception as e:
        print(f"Error converting {png_file}: {e}")
