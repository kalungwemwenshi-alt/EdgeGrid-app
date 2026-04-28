import os

footer_html = """
    <!-- Mobile Bottom Navigation -->
    <div class="mobile-bottom-nav">
        <a href="index.html" class="active">
            <i class='bx bxs-home'></i>
            Home
        </a>
        <a href="courses.html">
            <i class='bx bx-book-open'></i>
            Courses
        </a>
        <a href="tools.html">
            <i class='bx bx-calculator'></i>
            Tools
        </a>
        <a href="about.html">
            <i class='bx bx-user'></i>
            Profile
        </a>
    </div>

    <!-- WhatsApp Floating Button & Popup -->
    <div class="whatsapp-container">
        <div id="waPopup" class="wa-popup">
            <div class="wa-header">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <i class='bx bxl-whatsapp' style="font-size: 24px;"></i>
                    <h4 style="margin: 0; font-size: 15px;">EdgeGrid Support</h4>
                </div>
                <i class='bx bx-x' style="font-size: 20px; cursor: pointer;" onclick="toggleWAPopup()"></i>
            </div>
            <div class="wa-body">
                <div class="wa-message-received">
                    Welcome to EdgeGrid Team Support, how may we help you today?
                </div>
            </div>
            <div class="wa-footer">
                <input type="text" id="waMessageInput" placeholder="Type a message..." onkeypress="if(event.key === 'Enter') sendWAMessage()">
                <button onclick="sendWAMessage()"><i class='bx bxs-send'></i></button>
            </div>
        </div>
        <div class="whatsapp-float" onclick="toggleWAPopup()">
            <div class="wa-waves"></div>
            <i class='bx bxl-whatsapp'></i>
        </div>
    </div>

    <script src="js/main.js"></script>
    <script>
        function toggleWAPopup() {
            const popup = document.getElementById('waPopup');
            popup.classList.toggle('active');
            if (popup.classList.contains('active')) {
                document.getElementById('waMessageInput').focus();
            }
        }
        function sendWAMessage() {
            const input = document.getElementById('waMessageInput');
            const message = input.value.trim();
            if (message) {
                navigator.clipboard.writeText(message).catch(err => console.log('Clipboard err:', err)).finally(() => {
                    const encodedMsg = encodeURIComponent(message);
                    window.open(`https://wa.me/260973493949?text=${encodedMsg}`, '_blank');
                    input.value = '';
                    toggleWAPopup();
                });
            }
        }
    </script>
</body>
"""

files_to_update = ["about.html", "blog-post-1.html", "blog-post-2.html", "blog.html", "contact.html", "courses.html", "faq.html", "tools.html"]

for file in files_to_update:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            
        # Very basic check: replace `</body>` with the new footer + `</body>`
        if 'class="mobile-bottom-nav"' not in content:
            # We also remove old whatsapp float if present
            # For simplicity, we just replace </body>
            new_content = content.replace("</body>", footer_html)
            with open(file, 'w') as f:
                f.write(new_content)
                
print("Updated HTML files.")
