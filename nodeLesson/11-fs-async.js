// File System (FS) Modules 
// Asynchronous (Non-Blocking)

// Requires callbacks
// can imporve this code with promises & async/await - will learn later

const fs = require('fs')

console.log('Start');

fs.readFile('./content/first.txt', 'utf-8',( err, result ) => {
    if (err) {
        console.log(err)
        return
    }
    const first = result
    fs.readFile('./content/second.txt','utf-8',( err, result ) => {
        if (err) {
            console.log(err)
            return
        }
        const second = result
        fs.writeFile('./content/result-async.txt',`Here is the Async result of: ${first}, ${second}`, ( err, result ) => {
            if (err) {
                console.log(err)
                return
            }
            console.log('Done with this task')
        })
    })
})

console.log('Starting next task');

