// HTTP - Routes 
// Use Postman to quickly test API endpoints

const express = require('express')
const app = express()

let { people } = require('./data.js')

// Static assets
app.use(express.static('./methods-public'))

// Parse form data
app.use(express.urlencoded({extended:false}))

// Parse json
app.use(express.json())

app.get('/api/people', (req, res) => {
    res.status(200).json({
        success:true,
        data:people
    })
})

app.post('/api/people', (req, res) => {
    const { name } = req.body

    if (!name) {
        return res.status(400).json({
            success:false,
            msg:'Name Not Found!'
        })
    }

    res.status(201).send({
        success: true,
        person: name
    })
})

app.put('/api/people/:id', (req, res) => {
    const { id } = req.params
    const { name } = req.body

    const person = people.find((person) => person.id === Number(id))
    
    if (!person) {
        return res.status(404).json({
            success: false,
            msg: `No person with id ${id}`
        })
    }
    
    // Temp logic cuz no db
    if (!name) {
        return res.status(200).json(person)
    }
    person.name = name
    res.status(200).json(person)
})

app.delete('/api/people/:id', (req, res) => {
    const { id } = req.params

    const person = people.find((person) => person.id === Number(id))

    if (!person) {
        return res.status(404).json({
            success: false,
            msg: `No person with id ${id}`
        })
    }
    
    const newPeople = people.filter((person) => person.id !== Number(id))

    res.status(200).json({
        success: true,
        data: newPeople
    })
})

app.post('/login', (req, res) => {
    const { name } = req.body

    if (name) {
        return res.status(200).send(`Hello, ${name}!`)
    }
    return res.status(401).send(`Name Not Found!`)
})

app.listen(3000, () => {
    console.log('Server live on port: 3000');
})
