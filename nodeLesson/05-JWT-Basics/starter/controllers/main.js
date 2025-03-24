// This project is not connected to db
// Options for user auth
//  Mongoose Validation, Joi Auth package, custom error handling

const jwt = require('jsonwebtoken')
const CustomAPIError = require('../errors/custom-error')

const login = async (req, res) => {
    const { username, password } = req.body
    if (!username || !password) {
        throw new CustomAPIError('Invalid Login Credentials', 400)
    }

    // Dummy user id to add to jwt
    const id = new Date().getDate()

    const token = jwt.sign(
        { id, username }, 
        process.env.JWT_SECRET,
        { expiresIn: '30d' }
    )

    res.status(200).json({
        msg: 'User Created',
        token: token    
    })
}

const dashboard = async (req, res) => {
    const num = Math.floor(Math.random() * 10000)
    res.status(200).json({ 
        msg: `Hello, Agent 007`, 
        secret: `Your secure passcode is ${num}`
    })
}

module.exports = {
    login, 
    dashboard
}