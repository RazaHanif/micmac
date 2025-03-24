const jwt = require('jsonwebtoken')
const { BadRequestError, UnAuthorizedError } = require('../errors')

const authMiddleware = async (req, res, next) =>  {
    const authHeader = req.headers.authorization

    if ( !authHeader || !authHeader.startsWith('Bearer ') ) {

        throw new BadRequestError (
            'Invalid Credentials'
        )
    }

    const token = authHeader.split(' ')[1]

    try {
        const decoded = jwt.verify(
            token,
            process.env.JWT_SECRET
        )
        const { id, username } = decoded
        req.user = { id, username }
        next()
    } catch (err) {
        throw new UnAuthorizedError (
            'Not authorized to access this route'
        )
    }
}

module.exports = authMiddleware