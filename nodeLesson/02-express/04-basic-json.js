// Application Program Interface vs Server Side Rendering
// API vs SSR

// API - Json      |   SSR - Template
// Send Data       |   Send Template
// res.json()      |   res.render()


const express = require('express')
const app = express()

const { products } = require('./data.js')

app.get('/', (req, res) => {
    res.status(200).json(products)
})


app.listen(3000, () => {
    console.log('Server is live on port : 3000');
})