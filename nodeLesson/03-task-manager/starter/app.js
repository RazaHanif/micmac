const express = require('express')
const app = express()

const tasks = require('./routes/tasks.js')

const port = 3000

app.use(express.json())
app.use(express.urlencoded({ extended:false }))

app.use('/api/v1/tasks', tasks)

app.get('/hello', (req, res) => {
    res.status(200).send(`Hello, World!`)
})

app.listen(port, () => {
    console.log(`Server live on port ${port}...`)
})