// useState() = Re renders comp when state changes

// useRef() = Does not re render when value changes
//            Use when you want a component to 'remember' a value but not trigger a re render
//            1. Accessing/Interacting with DOM elements
//            2. Handling Focus, Animations & Transitions
//            3. Managing Timers & Intervels

import React, {useState, useEffect, useRef} from "react";

function MyRef() {
    // let [num, setNum] = useState(0)
    const inputRef1 = useRef(null)
    const inputRef2 = useRef(null)
    const inputRef3 = useRef(null)

    useEffect(() => {
        console.log("Click")
    })


    function handleClick1(){
        inputRef1.current.focus()
        inputRef1.current.style.backgroundColor = "red"
        inputRef2.current.style.backgroundColor = ""
        inputRef3.current.style.backgroundColor = ""
    }
    
    function handleClick2(){
        inputRef2.current.focus()
        inputRef1.current.style.backgroundColor = ""
        inputRef2.current.style.backgroundColor = "red"
        inputRef3.current.style.backgroundColor = ""
    }
    
    function handleClick3(){
        inputRef3.current.focus()
        inputRef1.current.style.backgroundColor = ""
        inputRef2.current.style.backgroundColor = ""
        inputRef3.current.style.backgroundColor = "red"
    }


    return(
        <div>
            <button onClick={handleClick1}>
                Click Here 1!
            </button>
            <input ref={inputRef1}/>
            <br/>
            <button onClick={handleClick2}>
                Click Here 2!
            </button>
            <input ref={inputRef2}/>
            <br/>
            <button onClick={handleClick3}>
                Click Here 3!
            </button>
            <input ref={inputRef3}/>

        </div>
    )
}

export default MyRef