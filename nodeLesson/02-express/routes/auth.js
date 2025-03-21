const express = require('express')
const router = express.Router()

router.post('/', (req, res) => {
    const { name } = req.body

    if (name) {
        return res.status(200).send(`Hello, ${name}!`)
    }
    return res.status(401).send(`Name Not Found!`)
})

module.exports = router