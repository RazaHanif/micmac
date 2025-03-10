import React, {useState} from 'react'

function MyComp() {
    
    const [name, setName] = useState("Guest")
    const [age, setAge] = useState(0)
    const [isStudent, setIsStudent] = useState(false)

    const updateName = () => {
        setName("Spongebob")
    }

    const updateAge = () => {
        setAge(age+1)
    }

    const toggleStudent = () => {
        setIsStudent(!isStudent)
    }

    return(
        <div>
            <p>Name: {name}</p>
            <button onClick={updateName}>Set Name</button>
            <p>Age: {age}</p>
            <button onClick={updateAge}>Increase Age</button>
            <p>Is Student: {isStudent ? "Yes" : "No"}</p>
            <button onClick={toggleStudent}>{isStudent ? "UnEnroll" : "Enroll"}</button>
        </div>
    )
}

export default MyComp 