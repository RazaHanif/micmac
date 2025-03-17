// File System (FS) Modules 
// Synchronous (Blocking)

const fs = require('fs')
console.log('Start');


const first = fs.readFileSync('./content/first.txt', 'utf-8')
const second = fs.readFileSync('./content/second.txt', 'utf-8')

fs.writeFileSync(
    './content/result-sync.txt', 
    `Here is the result of: ${first}, ${second}`,
    { flag: 'a' } // Append
)
console.log('Done with the task');
console.log('Starting the next task');
