// Hyper Text Transfer Protocol (HTTP) Module
// Brief intro, will go in depth later

const http = require('http')

// Standard to call methods req & res for http request & response
const server = http.createServer((req, res) => {
    if (req.url === '/'){
        res.end('Welcome to our Home Page')
    }
    else if (req.url === '/about'){
        res.end('This is our history')
    }
    else {
        res.end(`
            <h1>OOPS!</h1>
            <p>Page Not Found</p>
            <a href='/'>Home</a>
            `)
    }
})

server.listen(3000)