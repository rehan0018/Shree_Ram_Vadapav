import os
import re
import ssl
import urllib.request

# Disable SSL verification for script environments
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read HTML
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
except Exception as e:
    print(f"Error reading index.html: {e}")
    exit(1)

# FontAwesome URL base
base_url_solid = "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/solid/{}.svg"
base_url_brands = "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/brands/{}.svg"

def get_svg(category, icon_name, custom_style=""):
    url = base_url_solid.format(icon_name) if category == 'solid' else base_url_brands.format(icon_name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            svg_content = response.read().decode('utf-8')
            
            # Format SVG for inline usage
            svg_content = re.sub(r'<!--.*?-->', '', svg_content, flags=re.DOTALL) # remove comments
            svg_content = svg_content.replace('xmlns="http://www.w3.org/2000/svg"', '') # remove duplicate xmlns
            svg_content = re.sub(r'<svg', f'<svg height="1em" width="1em" style="vertical-align: -0.125em; fill: currentColor; {custom_style}"', svg_content)
            
            return svg_content.strip()
    except Exception as e:
        print(f"Failed to fetch {icon_name}: {e}")
        return None

# Find all icons
# Format: <i class="fa-solid fa-star" style="..."></i>
icon_pattern = r'<i\s+class="fa-(solid|brands)\s+fa-([^"\s]+)"(?:\s+style="([^"]+)")?\s*></i>'

def replace_icon(match):
    category = match.group(1)
    icon_name = match.group(2)
    custom_style = match.group(3) or ""
    
    # Handle style attribute correctly
    svg = get_svg(category, icon_name, custom_style)
    if svg:
        return svg
    return match.group(0) # fallback to original

new_html = re.sub(icon_pattern, replace_icon, html)

# Remove the FontAwesome CSS link from <head>
css_link_pattern = r'<!-- Icons -->[\s\S]*?<noscript>[\s\S]*?</noscript>'
new_html = re.sub(css_link_pattern, '', new_html)

# Also remove the basic font-awesome link if it's there
basic_link_pattern = r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome[^>]+>'
new_html = re.sub(basic_link_pattern, '', new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Icons replaced!")
