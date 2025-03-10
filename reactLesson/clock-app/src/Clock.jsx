// React desktop clock app 

import React, {useState, useEffect} from "react";

function Clock() {

    const [time, setTime] = useState(new Date().toLocaleTimeString())

    useEffect(() => {
        const timer = setInterval(() => {
            setTime(new Date().toLocaleTimeString())
        }, 1000)

        return () => {
            clearInterval(timer)
        }
    }, [])
    
    return (
        <div className="page">
            <div className="time-container">
                <p className="time">{time}</p>
            </div>
        </div>
    )
}

export default Clock