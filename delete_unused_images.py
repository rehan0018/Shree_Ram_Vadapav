import os
import re
import glob

# Read HTML and CSS files with utf-8 encoding
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
except Exception as e:
    html = ""
    print(f"Error reading index.html: {e}")

try:
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()
except Exception as e:
    css = ""
    print(f"Error reading style.css: {e}")

# Find all image usages
used_html = re.findall(r'images/([^"\'\s]+)', html)
used_css = re.findall(r'images/([^"\'\s\)]+)', css)

used_files = set(used_html + used_css)

# List all files in images/
image_dir = 'images'
all_files = os.listdir(image_dir)

# Delete unused files
unused_files = [f for f in all_files if f not in used_files]
deleted_count = 0

for f in unused_files:
    file_path = os.path.join(image_dir, f)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted unused image: {f}")
        deleted_count += 1

print(f"Total deleted: {deleted_count}")
