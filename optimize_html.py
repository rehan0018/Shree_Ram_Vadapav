import re
import os

html_path = 'c:/Users/Rehan Shaikh/Downloads/web dev/project/project_by_antigravity/shree_ram_vadapav/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace PNG with WebP
content = content.replace('.png"', '.webp"')

# 2. Add loading="lazy" to all menu images (except hero and logo which are handled differently)
# Looking at the HTML, menu images are inside <div class="card-img"> \n <img src="...">
# and franchise section might have no images. 
# We can just replace '<img src="images/' with '<img src="images/' and then lazy load carefully later, OR just:
# replace '<img src="images/' with '<img loading="lazy" src="images/'
content = content.replace('<img src="images/', '<img loading="lazy" src="images/')
# Revert for hero and logo (above the fold)
content = content.replace('<img loading="lazy" src="images/hero.webp"', '<img src="images/hero.webp"')
content = content.replace('<img loading="lazy" src="images/logo.webp"', '<img src="images/logo.webp"')

# 3. Add defer to script
content = content.replace('<script src="script.js"></script>', '<script src="script.js" defer></script>')

# 4. Add preconnect to cloudflare
if '<link rel="preconnect" href="https://cdnjs.cloudflare.com">' not in content:
    content = content.replace('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/', 
                              '<link rel="preconnect" href="https://cdnjs.cloudflare.com">\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html optimized successfully.")
