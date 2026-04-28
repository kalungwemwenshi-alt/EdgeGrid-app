import os
import re

files_to_update = ["about.html", "blog-post-1.html", "blog-post-2.html", "blog.html", "contact.html", "courses.html", "faq.html", "tools.html"]

new_nav_right = """            <div class="nav-right-actions" style="display: flex; align-items: center; gap: 15px;">
                <div class="cta-contact">
                    <a href="tel:+260973493949" class="btn btn-outline"
                        style="display: flex; align-items: center; gap: 8px; padding: 8px 16px;">
                        <i class='bx bxs-phone'></i> <span class="hide-mobile">+260 973 493 949</span>
                    </a>
                </div>
                <a href="VIPmembers.html" class="vip-top-btn" style="display: flex; justify-content: center; align-items: center; width: 40px; height: 40px; background: var(--gold-gradient); color: var(--secondary-color); border-radius: 50%; font-size: 20px; box-shadow: 0 4px 10px rgba(212,175,55,0.4); transition: transform 0.3s ease;">
                    <i class='bx bxs-crown'></i>
                </a>
            </div>"""

for file in files_to_update:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            
        # Regex to replace the <div class="cta-contact"> block in the navbar
        # Since HTML structure is similar across files
        pattern = re.compile(r'<div class="cta-contact">.*?</div>\s*</div>\s*</nav>', re.DOTALL)
        
        if '<div class="nav-right-actions"' not in content:
            replacement = new_nav_right + '\n        </div>\n    </nav>'
            new_content = pattern.sub(replacement, content)
            with open(file, 'w') as f:
                f.write(new_content)

print("Updated Headers.")
