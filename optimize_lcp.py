import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Revert font loading to synchronous to fix text LCP delay
font_async = '''    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap"
        rel="stylesheet" media="print" onload="this.media='all'">
    <noscript>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
    </noscript>'''

font_sync = '''    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">'''

html = html.replace(font_async, font_sync)
html = html.replace('''    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap"
        rel="stylesheet" media="print" onload="this.media='all'">
    <noscript>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
    </noscript>''', font_sync)

# 2. Remove .animate-up and .delay-* from Hero
html = html.replace('<h1 class="animate-up">', '<h1>')
html = html.replace('<p class="animate-up delay-1">', '<p>')
html = html.replace('<div class="hero-btns animate-up delay-2">', '<div class="hero-btns">')

# 3. Add width and height to images to prevent CLS
html = re.sub(r'<img src="images/hero.webp" alt="([^"]+)">', r'<img src="images/hero.webp" alt="\1" width="800" height="600">', html)
html = re.sub(r'<img src="images/logo.webp" alt="([^"]+)"\s+style="([^"]+)">', r'<img src="images/logo.webp" alt="\1" width="96" height="96" style="\2">', html)

# Menu images
html = re.sub(r'<img loading="lazy" src="([^"]+)" alt="([^"]+)">', r'<img loading="lazy" src="\1" alt="\2" width="400" height="300">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
