const http = require('http')

// const server = http.createServer((req, res) => {
//     res.end('Hello, World!')
// })

const server = http.createServer()
server.on('request', (req, res) => {
    res.end('Hello, World!')
    console.log('request');
    
})

server.listen(3000)