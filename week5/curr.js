/* 
API_KEY = "8c320f362211eeec45a71caaa5b08d42"
info = requests.get(
    "http://api.exchangeratesapi.io/v1/latest",
    params={"access_key": API_KEY, "symbols": "CAD,EUR,GBP,JPY,USD"},
)
response = info.json()
*/

document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('form').onsubmit = function() {
        fetch('https://open.er-api.com/v6/latest/USD')
        .then(response => response.json())

        .then(data => {

            const currency = document.querySelector('#currency').value.toUpperCase()
            const rate = data.rates[currency]
            if (rate !== undefined) {
                document.querySelector('#results').innerHTML = `$1 USD is ${rate.toFixed(2)} ${currency}`
            } else {
                document.querySelector('#results').innerHTML = 'Invalid Currency'
            }
        })
        .catch(error => {
            console.log('Error: ', error)
        })
        
        return false
    }
})