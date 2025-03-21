const Task = require('../models/Task.js')

const getTasks = (req, res) => {
    res.status(200).json({
        success:true,
        data: "all items"
    })
}

const createTask = async (req, res) => {
    try {
        const task = await Task.create(req.body)
        res.status(200).json({ task })
    } catch (err) {
        return res.status(400).send(err)
    }
    
}

const getTask = (req, res) => {
    const { id } = req.params 
    res.status(200).json({
        success:true,
        data: `this item : ${id}`
    })
}

const updateTask = (req, res) => {
    const { id } = req.params 
    res.status(200).json({
        success:true,
        data: `updated item : ${id}`
    })
}

const deleteTask = (req, res) => {
    const { id } = req.params 
    res.status(200).json({
        success:true,
        data: `deleted item : ${id}`
    })
}


module.exports = {
    getTasks,
    createTask,
    getTask,
    updateTask,
    deleteTask
}