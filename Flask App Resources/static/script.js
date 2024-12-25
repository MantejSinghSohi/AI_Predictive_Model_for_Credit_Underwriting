document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('result').innerHTML = 
                `<div class="${data.prediction === 'approved' ? 'success' : 'error'}">
                    The loan is likely to be ${data.prediction}!
                </div>`;
        } else {
            document.getElementById('result').innerHTML = 
                `<div class="error">Error: ${data.error}</div>`;
        }
    } catch (error) {
        document.getElementById('result').innerHTML = 
            `<div class="error">Error: ${error.message}</div>`;
    }
}); 