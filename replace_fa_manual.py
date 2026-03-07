import re

# Read HTML
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
except Exception as e:
    print(f"Error reading index.html: {e}")
    exit(1)

svg_map = {
    'xmark': '<svg height="1em" width="1em" viewBox="0 0 384 512" style="vertical-align: -0.125em; fill: currentColor;"><path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/></svg>',
    'mug-hot': '<svg height="1em" width="1em" viewBox="0 0 512 512" style="vertical-align: -0.125em; fill: currentColor;"><path d="M400 192V368c0 53-43 96-96 96H160c-53 0-96-43-96-96V192c0-35.3 28.7-64 64-64H336c35.3 0 64 28.7 64 64zM400 224h48c35.3 0 64 28.7 64 64s-28.7 64-64 64H400v-128zM144 48H128c-17.7 0-32 14.3-32 32s14.3 32 32 32h16c17.7 0 32-14.3 32-32s-14.3-32-32-32zm80 0H208c-17.7 0-32 14.3-32 32s14.3 32 32 32h16c17.7 0 32-14.3 32-32s-14.3-32-32-32zm80 0H288c-17.7 0-32 14.3-32 32s14.3 32 32 32h16c17.7 0 32-14.3 32-32s-14.3-32-32-32zm80 0H368c-17.7 0-32 14.3-32 32s14.3 32 32 32h16c17.7 0 32-14.3 32-32s-14.3-32-32-32z"/></svg>',
    'star-half-stroke': '<svg height="1em" width="1em" viewBox="0 0 576 512" style="vertical-align: -0.125em; fill: currentColor;"><path d="M288 389.5L144.9 464c-12 6.3-26.6 2-32.5-10.4s-3.7-27.1 8.2-35.5L257.4 316.3 128.7 202.9c-10.4-9.2-12-24.6-3.8-35.7s24-14.6 38.3-10l169.3 54 58.7-183c5.3-16.4 21.6-26.8 38.8-23.7s29.7 18.2 31.8 35.6l23.5 194.5L528 261c14.2-4.5 30.1 .9 38.3 12s6.6 26.5-3.8 35.7L433.9 418.1l23.7 190.5c2.1 17.5-8.4 34-25.2 39.5s-34.9-.7-42.6-15.5L288 389.5zM280 23.9l0 380 91.5 59.5L341 332.6l10-84.3L427.6 219.7l-104.9-33.4-14.4-4.6L280 23.9z"/></svg>',
    'location-dot': '<svg height="1em" width="1em" viewBox="0 0 384 512" style="vertical-align: -0.125em; fill: currentColor;"><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>'
}

icon_pattern = r'<i\s+class="fa-(solid|brands)\s+fa-([^"\s]+)"(?:\s+style="([^"]*)")?\s*></i>'

def replace_icon(match):
    category = match.group(1)
    icon_name = match.group(2)
    style = match.group(3) or ""
    
    if icon_name in svg_map:
        svg = svg_map[icon_name]
        # Inject style into the SVG if there is one
        if style:
            svg = svg.replace('style="', f'style="{style} ')
        return svg
    return match.group(0)

new_html = re.sub(icon_pattern, replace_icon, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Manual SVGs replaced!")
