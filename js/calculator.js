document.addEventListener('DOMContentLoaded', () => {
    const calcBtn = document.getElementById('calculateBtn');
    if (!calcBtn) return;

    calcBtn.addEventListener('click', () => {
        const pairPipValue = parseFloat(document.getElementById('currencyPair').value);
        const accountBalance = parseFloat(document.getElementById('accountBalance').value);
        const riskPercentage = parseFloat(document.getElementById('riskPercentage').value);
        const stopLoss = parseFloat(document.getElementById('stopLoss').value);
        const errorMsg = document.getElementById('errorMsg');

        // Validation
        if (isNaN(accountBalance) || isNaN(riskPercentage) || isNaN(stopLoss) || accountBalance <= 0 || riskPercentage <= 0 || stopLoss <= 0) {
            errorMsg.style.display = 'block';
            resetResults();
            return;
        }

        errorMsg.style.display = 'none';

        // Calculation
        const riskAmount = accountBalance * (riskPercentage / 100);
        
        // Position size in standard lots
        // Risk Amount = (Pip Value * Lots) * StopLoss
        // Lots = Risk Amount / (Pip Value * StopLoss)
        const standardLots = riskAmount / (pairPipValue * stopLoss);
        const miniLots = standardLots * 10;
        const microLots = standardLots * 100;

        // Display results
        document.getElementById('moneyRisk').textContent = `$${riskAmount.toFixed(2)}`;
        document.getElementById('standardLots').textContent = standardLots.toFixed(2);
        document.getElementById('miniLots').textContent = miniLots.toFixed(2);
        document.getElementById('microLots').textContent = microLots.toFixed(2);
    });

    function resetResults() {
        document.getElementById('moneyRisk').textContent = '$0.00';
        document.getElementById('standardLots').textContent = '0.00';
        document.getElementById('miniLots').textContent = '0.00';
        document.getElementById('microLots').textContent = '0.00';
    }
});
