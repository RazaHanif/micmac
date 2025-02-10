// useEffect() = React Hook that tells React DO X WHEN Y
// Y = Component re-renders OR Component mounts OR state of a value

// useEffect(function, [dependencies])

// useEffect(() => {})              Runs after every re-render
// useEffect(() => {}, [])          Runs only on mount
// useEffect(() => {}, [value])     Runs on mount + when value changes

/* 
Uses

1. Event Listeners
2. DOM manipulation
3. Subscriptions (real-time updates)
4.Fetching Data from an API
5. Clean up when a compenent unmounts
*/


import React, { useState, useEffect } from "react"

function MyEffect() {

    const [count, setCount] = useState(0)
    const [color, setColor] = useState("green")

    // Best practice is to include value to only run code when needed not everytime the comp is rerendered
    useEffect(() => {
        document.title = `Count: ${count} ${color}`
    }, [count, color])
    
    // render only once
    // useEffect(() => {
    //     document.title = `Count: ${count}`
    // }, [])

    function addCount() {
        setCount(prevCount => prevCount + 1)
    }
    
    function minusCount() {
        setCount(prevCount => prevCount - 1)
    }

    function changeColor() {
        setColor(prevColor => prevColor === "green" ? "red" : "green")
    }

    return (<>
        <p style={{color: color}}>Count: { count }</p>
        <button onClick={addCount}>Add</button>
        <button onClick={minusCount}>Minus</button>
        <br/>
        <button onClick={changeColor}>Change Color</button>
        
    </>)
}

export default MyEffect