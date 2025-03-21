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
        const newTask = await Task.create(req.body)
        res.status(200).json({ newTask })
    } catch (err) {
        return res.status(500).send(err)
    }
}

// Forgot that all these routes below use :id

const getTask = async (req, res) => {
    try {
        const { id: taskID } = req.params
        const task = await Task.findOne({ _id: taskID })
        if (!task) {
            return res.status(404).json({ msg: `No task found with id : ${taskID}` })
        }
        res.status(200).json({ task })
    } catch (err) {
        return res.status(500).send(err)
    }
}

const updateTask = async (req, res) => {
    try {
        const { id: taskID } = req.params
        const task = await Task.findOneAndUpdate({ _id: taskID }, req.body, {
            new: true,
            runValidators: true
        })
        if (!task) {
            return res.status(404).json({ msg: `No task found with id : ${taskID}` })
        }       
        res.status(200).json({ task })
    } catch (err) {
        return res.status(500).send(err)
    }
}

const deleteTask = async (req, res) => {
    try {
        const { id: taskID } = req.params
        const task = await Task.findOneAndDelete({ _id: taskID })
        if (!task) {
            return res.status(404).json({ msg: `No task found with id : ${taskID}` })
        }       
        res.status(200).json({ task })
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