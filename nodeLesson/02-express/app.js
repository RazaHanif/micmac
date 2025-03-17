// Application Program Interface vs Server Side Rendering
// API vs SSR

// API - Json      |   SSR - Template
// Send Data       |   Send Template
// res.json()      |   res.render()


const express = require('express')
const app = express()

const { products } = require('./data.js')

app.get('/', (req, res) => {
    res.status(200).send(`<h1>Home Page</h1><a href='/api/products'>products</a>`)
})

app.get('/api/products', (req, res) => {
    const newProducts = products.map((product) => {
        const {id, name, image} = product
        return {id, name, image}
    })
    res.status(200).json(newProducts)
})

// Dynamic Route w/ req.params
app.get('/api/products/:prodId', (req, res) => {
    const { prodId } = req.params
    
    const singleProduct = products.find((product) => product.id === Number(prodId))

    if (!singleProduct) {
        res.status(404).send('Product Not Found')
    }

    res.status(200).json(singleProduct)
})


app.listen(3000, () => {
    console.log('Server is live on port : 3000');
})