// Express - Router
const express = require('express')
const app = express()

const people = require('./routes/people.js')
const auth = require('./routes/auth.js')

// Static assets
app.use(express.static('./methods-public'))
// Parse form data
app.use(express.urlencoded({extended:false}))
// Parse json
app.use(express.json())

app.use('/api/people', people)

app.use('/login', auth)

app.listen(3000, () => {
    console.log('Server live on port: 3000');
})
