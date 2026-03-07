import os
from PIL import Image
import glob

image_dir = "images"
webp_files = glob.glob(os.path.join(image_dir, "*.webp"))

for webp_file in webp_files:
    try:
        with Image.open(webp_file) as im:
            if "logo" in webp_file:
                im = im.resize((96, 96), Image.Resampling.LANCZOS)
            im.save(webp_file, "webp", quality=40)
        print(f"Compressed {webp_file}")
    except Exception as e:
        print(f"Error compressing {webp_file}: {e}")
