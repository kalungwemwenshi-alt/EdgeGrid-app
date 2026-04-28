document.addEventListener('DOMContentLoaded', () => {
    // Set current year in footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Theme Toggle Logic
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;
    
    // Check for saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        const icon = themeToggle ? themeToggle.querySelector('i') : null;
        if (icon) {
            icon.className = theme === 'light' ? 'bx bx-moon' : 'bx bx-sun';
        }
    }

    // Inject Wall Street Ticker just after header Navbar
    const tickerData = [
        { symbol: "EUR/USD", price: "1.0854", change: "+0.12%", positive: true },
        { symbol: "GBP/USD", price: "1.2640", change: "-0.05%", positive: false },
        { symbol: "USD/JPY", price: "150.23", change: "+0.34%", positive: true },
        { symbol: "GOLD", price: "$2,034.50", change: "+0.80%", positive: true },
        { symbol: "US30", price: "38,590.20", change: "-0.21%", positive: false },
        { symbol: "BTC/USD", price: "$64,210.00", change: "+2.40%", positive: true }
    ];

    let tickerHTML = `<div class="ticker">`;
    tickerData.forEach(item => {
        const changeClass = item.positive ? "positive" : "negative";
        const icon = item.positive ? "▲" : "▼";
        tickerHTML += `
            <div class="ticker__item">
                <span class="ticker__symbol">${item.symbol}</span>
                <span class="ticker__price">${item.price}</span>
                <span class="ticker__change ${changeClass}">${icon} ${item.change}</span>
            </div>
        `;
    });
    // Duplicate for seamless scroll
    tickerHTML += tickerHTML.replace('<div class="ticker">', '');
    tickerHTML += `</div>`;

    const tickerWrap = document.createElement('div');
    tickerWrap.className = 'ticker-wrap';
    tickerWrap.innerHTML = tickerHTML;

    const navbar = document.querySelector('.navbar');
    if (navbar) {
        navbar.insertAdjacentElement('afterend', tickerWrap);
    }
});
