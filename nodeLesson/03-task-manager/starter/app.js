const express = require('express')
const app = express()
const connectDB = require('./db/connect.js')
require('dotenv').config()


const tasks = require('./routes/tasks.js')

const port = 3000

app.use(express.json())
app.use(express.urlencoded({ extended:false }))

app.use('/api/v1/tasks', tasks)

app.get('/hello', (req, res) => {
    res.status(200).send(`Hello, World!`)
})


const start = async () => {
    try {
        // await connectDB(process.env.MONGO_URI)
        app.listen(port, () => {
            console.log(`Server live on port ${port}...`)
        })
    } catch (err) {
        console.log(err);
        
    }
}

start()
