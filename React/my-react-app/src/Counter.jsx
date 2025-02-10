import React, {useState} from 'react'

function Counter() {
    const [count, setCount] = useState(0)

    const countUp = () => {
        setCount(prevCount => prevCount + 1)
    }
    const countDown = () => {
        if (count > 0) {
            setCount(c => c - 1)
        }
    }
    const countReset = () => {
        setCount(0)
    }

    return(
        <div className='counter-container'>
            <p className='counter-display'>{count}</p>
            <button className='counter-button' onClick={countDown}>-</button>
            <button className='counter-button' onClick={countReset}>Reset</button>
            <button className='counter-button' onClick={countUp}>+</button>
        </div>
    )

}

export default Counter