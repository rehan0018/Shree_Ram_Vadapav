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
            # Re-saving with even lower quality and smaller size if it's very large
            if im.width > 800:
                new_width = 800
                new_height = int((new_width / im.width) * im.height)
                im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
            im.save(webp_file, "webp", quality=35, optimize=True)
        print(f"Aggressively Compressed {webp_file}")
    except Exception as e:
        print(f"Error compressing {webp_file}: {e}")
