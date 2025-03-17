// Middleware
// request => middleware => response

const express = require('express')
const app = express()
const logger = require('./logger.js')
const authorize = require('./auth.js')

// applies the middleware to all routes
// needs to be at the very top of the routes
app.use(logger, authorize)

app.get('/', (req, res) => {
    console.log(req);
    
    res.send("Home")
})

app.get('/about', (req, res) => {
    res.send("About")
})

app.listen(3000, () => {
    console.log('Server is live on port : 3000');
})