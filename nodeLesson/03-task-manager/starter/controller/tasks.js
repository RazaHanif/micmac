const getTasks = (req, res) => {
    res.status(200).json({
        success:true,
        data: "all items"
    })
}

const createTask = (req, res) => {
    res.status(200).json({
        success:true,
        data: "new item"
    })
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