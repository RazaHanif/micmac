import React, { useState } from "react";

function ToDoList() {

    const [tasks, setTasks] = useState(["Eat food", "Take a shower", "Get Coffee", "Go to work"])
    const [newTask, setNewTasks] = useState("")

    function handleAddTask() {
        console.log(`tasks = ${tasks} && newTask = ${newTask}`)
        if (newTask.trim() !== ""){
            setTasks(prevTasks => [...prevTasks, newTask])
            setNewTasks("")
        }       
    }

    function handleSetNewTasks(e) {
        setNewTasks(e.target.value)
    }

    function handleRemoveTask(index) { 
        setTasks(prevTasks => prevTasks.filter((_, i) => i !== index))
    }

    function swapTaskUp(index) {
        const newTaskList = [...tasks]

        if (index > 0){
            const [temp] = newTaskList.splice(index, 1)
            newTaskList.splice(index - 1, 0, temp)
            setTasks(newTaskList)
        }
    }
    
    function swapTaskDown(index) {
        const newTaskList = [...tasks]

        if (index < newTaskList.length){
            const [temp] = newTaskList.splice(index, 1)
            newTaskList.splice(index + 1, 0, temp)
            setTasks(newTaskList)
        }
    }

    return(
        <div className="todo-container">
            <h2>To-Do-List</h2>

            <div className="todo-add-container">
                <input type="text" placeholder="Enter a task..." value={newTask} onChange={(e) => handleSetNewTasks(e)}/>
                <button onClick={() => handleAddTask()}>Add</button>

            </div>

            <div className="task-list">
                {tasks.map((task, index) => 
                    <div className="task-container">
                        <p className="task-name">{task}</p>
                        <button className="task-btn delete" onClick={() => handleRemoveTask(index)}>Delete</button>
                        <button className="task-btn" onClick={() => swapTaskUp(index)}>&uarr;</button>
                        <button className="task-btn" onClick={() => swapTaskDown(index)}>&darr;</button>
                    </div>
                )}
            </div>

        </div>
    )

}

export default ToDoList