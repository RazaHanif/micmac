// Express - HTTP

// content-type: text/html or plain
// Express takes care of this tbh

const http = require('http')

const server = http.createServer((req, res) => {
    const url = req.url
    if (url === '/'){
        res.writeHead(200, { 
            'content-type': 'text/html'
        })
        res.write(`<h1>Home Page</h1>`)
        res.end()
    }
    else if (url === '/about') {
        res.writeHead(200, { 
            'content-type': 'text/html'
        })
        res.write(`<h1>About Page</h1>`)
        res.end()
    }
    else if (url === '/contact') {
        res.writeHead(200, { 
            'content-type': 'text/html'
        })
        res.write(`<h1>Contact Page</h1>`)
        res.end()
    }
    else {
        res.writeHead(404, { 
            'content-type': 'text/html'
        })
        res.write(`<h1>404 Page Not Found</h1>`)
        res.end()
    }
        
    
})

server.listen(3000)