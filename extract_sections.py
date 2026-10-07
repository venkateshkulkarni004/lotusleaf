with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract navbar
nav_start = content.find('<nav\n  id="navbar"')
nav_end = content.find('</nav>', nav_start) + len('</nav>')
navbar_html = content[nav_start:nav_end]
print('Navbar extracted:', len(navbar_html), 'chars')

# Extract side menu offcanvas
side_start = content.find('<div\n  class="offcanvas offcanvas-end side-offcanvas')
# Find matching closing </div>
depth = 0
for i in range(side_start, len(content)):
    if content[i:i+5] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            side_end = i + 6
            break
side_menu_html = content[side_start:side_end]
print('Side menu extracted:', len(side_menu_html), 'chars')

# Extract footer
footer_start = content.find('<footer class="bg-emerald grain site-footer')
footer_end = content.find('</footer>', footer_start) + len('</footer>')
footer_html = content[footer_start:footer_end]
print('Footer extracted:', len(footer_html), 'chars')

# Extract menu JS
js_start = content.find('document.addEventListener("DOMContentLoaded"')
js_end = content.find('</script>', js_start) + len('</script>')
menu_js = content[js_start-50:js_end]
print('Menu JS extracted:', len(menu_js), 'chars')

# Save to files for inspection
with open('navbar.html', 'w', encoding='utf-8') as f:
    f.write(navbar_html)
with open('side_menu.html', 'w', encoding='utf-8') as f:
    f.write(side_menu_html)
with open('footer.html', 'w', encoding='utf-8') as f:
    f.write(footer_html)
with open('menu_js.js', 'w', encoding='utf-8') as f:
    f.write(menu_js)

print('Extracted sections saved to files')
