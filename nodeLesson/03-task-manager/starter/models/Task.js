const mongoose = require('mongoose')

const TaskSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'Must Provide Name'],
        trim: true,
        maxlength: [20, 'Name cannot exceed 20 characters'],
        minlength: [3, 'Name must exceed 3 characters']
    },
    completed: {
        type: Boolean,
        default: false
    }
})

module.exports = mongoose.model('Task', TaskSchema)