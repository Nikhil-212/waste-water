document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('waterForm');
    
    if (form) {
        // Set default date and time
        const now = new Date();
        document.getElementById('date').valueAsDate = now;
        document.getElementById('time').value = now.toTimeString().slice(0, 5);
        
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = {
                date: document.getElementById('date').value,
                time: document.getElementById('time').value,
                tankCapacity: document.getElementById('tankCapacity').value,
                prevLevel: document.getElementById('prevLevel').value,
                currLevel: document.getElementById('currLevel').value,
                students: document.getElementById('students').value,
                area: document.getElementById('area').value,
                block: document.getElementById('block').value
            };
            
            // Validation
            if (parseFloat(formData.currLevel) > parseFloat(formData.prevLevel)) {
                showMessage('Current water level cannot be greater than previous level!', 'error');
                return;
            }
            
            if (parseFloat(formData.prevLevel) > parseFloat(formData.tankCapacity)) {
                showMessage('Previous water level cannot exceed tank capacity!', 'error');
                return;
            }
            
            try {
                const response = await fetch('/api/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    showMessage(`Data submitted successfully! Water used: ${result.waterUsed.toFixed(2)} liters`, 'success');
                    form.reset();
                    document.getElementById('date').valueAsDate = new Date();
                    document.getElementById('time').value = new Date().toTimeString().slice(0, 5);
                } else {
                    showMessage('Error submitting data. Please try again.', 'error');
                }
            } catch (error) {
                showMessage('Error connecting to server. Please try again.', 'error');
                console.error('Error:', error);
            }
        });
    }
});

function showMessage(text, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
    messageDiv.style.display = 'block';
    
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 5000);
}
