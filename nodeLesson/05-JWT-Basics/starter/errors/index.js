// Naming this index.html means you can do require('./foldername) 
// And still have access to everything being exported from this file

const CustomAPIError = require('./custom-error')
const BadRequestError = require('./bad-request')
const UnAuthorizedError = require('./unauth')

module.exports = {
    CustomAPIError,
    BadRequestError,
    UnAuthorizedError
}