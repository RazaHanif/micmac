
function Click(props) {

    const handleClick = () => console.log("Click!")
    
    const handleClick2 = (name) => console.log(`${name} stop clicking me!`)
   
    let count = 0
    
    const handleClick3 = () => {
        if (count < 3){
            count++
            console.log(`you clicked me ${count} time/s`)
        }
        else {
            console.log(`stop clicking me!`)
        }
    }

    const eventClick = (e) => e.target.textContent = "Ouch!"

    return(
        <button onClick={() => handleClick()} onDoubleClick={(e) => eventClick(e)}>Click Here!</button>
    )

}

export default Click