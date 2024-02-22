document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        const name = document.querySelector('#name');
        document.querySelector('h1').innerHTML = `Hello, ${name}!`;
    };
});


function hello() {
    const header = document.querySelector('h1');
    if (header.innerHTML === 'Hello!') {
        header.innerHTML = 'Goodbye!';
    } else {
        header.innerHTML = 'Hello!';
    }
};