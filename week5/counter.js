if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0)
}

let counter = localStorage.getItem('counter')

function count(){
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter)
}

function reset(){
    counter = 0;
    alert(`RESET: Count is now ${counter}`);
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('h1').innerHTML = counter
    document.querySelector('#count').onclick = count 
    document.querySelector('#reset').onclick = reset
    
    setInterval(count, 1000)
})
