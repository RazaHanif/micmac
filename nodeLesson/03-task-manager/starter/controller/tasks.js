const Task = require('../models/Task.js')

const getTasks = async (req, res) => {
    try {
        const allTasks = await Task.find({})
        res.status(200).json({ allTasks })
    } catch (err) {
        return res.status(500).send(err)
    }
}

const createTask = async (req, res) => {
    try {
        const task = await Task.create(req.body).exec()
        res.status(200).json({ task })
    } catch (err) {
        return res.status(500).send(err)
    }
}

// gonna find by some key:value for now, later will set up so its by id
const getTask = async (req, res) => {
    try {
        // find all LIKE x
        const task = await Task.find({ name: `/${req.body.name}/i`}).exec()
        res.status(200).json({ task })
    } catch (err) {
        return res.status(500).send(err)
    }
}

// Used to mark a task complete
const updateTask = async (req, res) => {
    try {
        // Find this task and update
        const task = await Task.findOne({name: req.body.name}).updateOne({completed: true})
        res.status(200).json({ task })
    } catch (err) {
        return res.status(500).send(err)
    }
}

const deleteTask = async (req, res) => {
    try {
        const deletedTask = await Task.deleteOne(req.body)
        res.status(200).json({ deletedTask })
    } catch (err) {
        return res.status(500).send(err)
        
    }
}


module.exports = {
    getTasks,
    createTask,
    getTask,
    updateTask,
    deleteTask
}