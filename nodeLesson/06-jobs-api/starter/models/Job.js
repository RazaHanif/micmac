const mongoose = require('mongoose')

const JobSchema = new mongoose.Schema({ 
    company: {
        type: String,
        required: [true, 'Please provide company name'],
        maxlength: 50,
    },
    position: {
        type: String,
        required: [true, 'Please provide position'],
        minlength: 5,
        maxlength: 100,
    },
    interview: {
        type: String,
        enum: ['interview', 'declined', 'pending'],
        default: 'pending',
    },
    createdBy: {
        type: mongoose.Types.ObjectId,
        ref: 'User',
        required: [true, 'Please provide user']
    },
}, {timestamps: true})

module.exports = mongoose.model('Job', JobSchema)