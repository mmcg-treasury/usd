javascript
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    const email = this.elements[0].value;
    const amount = this.elements[1].value;
    const platform = this.elements[2].value;
    
    // Send deposit with API call
    sendDeposit(email, amount, platform);
});

function sendDeposit(email, amount, platform) {
    const endpoint = `https://api.example.com/send_deposit`;
    const data = {
        email: email,
        amount: amount,
        platform: platform
    };

    fetch(endpoint, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        console.log('Deposit sent');
    })
    .catch(error => {
        console.error('There was a problem sending your deposit:', error);
    });
}
