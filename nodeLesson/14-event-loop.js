// Node.js Event Loop

/* 
Js is Synchronous - reads all code line by line
    if a part of the code takes extra time,
    everything after will be locked until the first task completes

fetch().then() (and other callback funcs) is an example of Js offloading to the browser

node.js event loop prevents time blocking tasks by registering a callback
*/

/* const { readFile } = require('fs')

console.log('started first task')

readFile('./content/first.txt', 'utf-8', (err, res) => {
    if (err) {
        console.log(err);
        return        
    }
    console.log(res);
    console.log('finished first task');
})

console.log('starting second task') */

/* console.log('first');
setTimeout(() => {
    console.log('second');
}, 0)
console.log('third')
 */


/* setInterval(() => {
   console.log('hello');
    
}, 2000);
console.log('i will run first');
 */

const http = require('http')

const server = http.createServer((req, res) => {
    console.log('request event');
    res.end('Hello')
})

server.listen(1234, () => {
    console.log('Server listening on port : 1234...');
})