const logger = (req, res, next) => {
    const m = req.method
    const u = req.url
    const y = new Date().getFullYear()
    console.log(m, u, y)
    next()
}

module.exports = logger