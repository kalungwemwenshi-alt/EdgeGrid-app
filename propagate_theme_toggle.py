import os
import re

files_to_update = ["about.html", "blog-post-1.html", "blog-post-2.html", "blog.html", "contact.html", "courses.html", "faq.html", "tools.html"]

theme_toggle_html = """                <div id="themeToggle" class="theme-toggle">
                    <i class='bx bx-moon'></i>
                </div>"""

for file in files_to_update:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            
        # Target the nav-right-actions container
        if 'id="themeToggle"' not in content:
            if '<div class="nav-right-actions"' in content:
                content = content.replace('<div class="nav-right-actions" style="display: flex; align-items: center; gap: 15px;">', 
                                          '<div class="nav-right-actions" style="display: flex; align-items: center; gap: 15px;">\n' + theme_toggle_html)
                with open(file, 'w') as f:
                    f.write(content)

print("Propagated theme toggle to public pages.")
