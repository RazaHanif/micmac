const express = require('express')
const router = express.Router()

// Controller
const {
    getAllJobs,
    getThisJob,
    createJob,
    updateJob,
    deleteJob
 } = require('../controllers/jobs')

// Middleware

// Routes
router.route('/').get(getAllJobs).post(createJob)
router.route('/:id').get(getThisJob).patch(updateJob).delete(deleteJob)

module.exports = router