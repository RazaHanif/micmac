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
    res.status(200).json({
        success:true,
        data: "this item"
    })
}

const updateTask = (req, res) => {
    res.status(200).json({
        success:true,
        data: "updated item"
    })
}

const deleteTask = (req, res) => {
    res.status(200).json({
        success:true,
        data: "deleted item"
    })
}


module.exports = {
    getTasks,
    createTask,
    getTask,
    updateTask,
    deleteTask
}