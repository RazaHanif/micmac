const authorize = (req, res, next) => {
    const { user } = req.query
    if (user === 'raza') {
        req.user = { name: 'raza', id: 1}
        next()
    } else {
        res.status(401).send('Unauthorized')
    }
}

module.exports = authorize