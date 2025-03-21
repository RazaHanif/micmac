const express = require('express')
const router = express.Router()

// app.get('/api/v1/tasks')         Get all tasks
// app.post('/api/v1/tasks')        Create new task
// app.get('/api/v1/tasks/:id')     Get this task
// app.patch('/api/v1/tasks/:id')   Update this task
// app.delete('/api/v1/tasks/:id')  Delete this task

const {
    getTasks,
    createTask,
    getTask,
    updateTask,
    deleteTask
} = require('../controller/tasks.js')
 
router.route('/').get(getTasks).post(createTask)
router.route('/:id').get(getTask).patch(updateTask).delete(deleteTask)

module.exports = router