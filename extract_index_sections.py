import os

SITE_ROOT = r"D:\soical media\ssm\saveweb2zip-com-pdf-site-builder-33-preview-emergentagent-com\leafcollection"

# Load index.html and extract header/footer/JS/CSS sections
with open(os.path.join(SITE_ROOT, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract navbar
nav_start = index_content.find('<nav\n  id="navbar"')
nav_end = index_content.find('</nav>', nav_start) + len('</nav>')
navbar_html = index_content[nav_start:nav_end]

# Extract side menu offcanvas
side_start = index_content.find('<div\n  class="offcanvas offcanvas-end side-offcanvas')
depth = 0
for i in range(side_start, len(index_content)):
    if index_content[i:i+5] == '<div':
        depth += 1
    elif index_content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            side_end = i + 6
            break
side_menu_html = index_content[side_start:side_end]

# Extract footer
footer_start = index_content.find('<footer class="bg-emerald grain site-footer')
footer_end = index_content.find('</footer>', footer_start) + len('</footer>')
footer_html = index_content[footer_start:footer_end]

# Extract menu JS
js_start = index_content.find('document.addEventListener("DOMContentLoaded"')
js_end = index_content.find('</script>', js_start) + len('</script>')
menu_js = index_content[js_start-50:js_end]

# Extract CSS blocks for header/footer
lines = index_content.splitlines(keepends=True)
css1 = "".join(lines[762:1341])
css2 = "".join(lines[4706:4729])
header_footer_css = css1 + "\n" + css2

# Save extracted sections to files for verification
with open(os.path.join(SITE_ROOT, "extracted_navbar.html"), "w", encoding="utf-8") as f:
    f.write(navbar_html)
with open(os.path.join(SITE_ROOT, "extracted_side_menu.html"), "w", encoding="utf-8") as f:
    f.write(side_menu_html)
with open(os.path.join(SITE_ROOT, "extracted_footer.html"), "w", encoding="utf-8") as f:
    f.write(footer_html)
with open(os.path.join(SITE_ROOT, "extracted_menu_js.js"), "w", encoding="utf-8") as f:
    f.write(menu_js)
with open(os.path.join(SITE_ROOT, "extracted_header_footer.css"), "w", encoding="utf-8") as f:
    f.write(header_footer_css)

print("Extracted sections saved to files")
print(f"Navbar: {len(navbar_html)} chars")
print(f"Side menu: {len(side_menu_html)} chars")
print(f"Footer: {len(footer_html)} chars")
print(f"Menu JS: {len(menu_js)} chars")
print(f"Header/Footer CSS: {len(header_footer_css)} chars")
