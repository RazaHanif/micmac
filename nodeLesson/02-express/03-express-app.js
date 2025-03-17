// Express 


const express = require('express')
const app = express()
// const path = require('path')

// best to put this in a folder called 'public' but this is just for testing
app.use(express.static('./navbar-app'))

// app.get('/', (req, res) => {
//     res.sendFile(path.resolve(__dirname, './navbar-app/index.html'))

// })

app.all('*', (req, res) => {
    res.status(404).send('Page Not Found')
})



app.listen(3000, () => {
    console.log('Server is live on port : 3000');
    
})