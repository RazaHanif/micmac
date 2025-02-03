

function Food() {

    const food1 = "Pasta"
    const food2 = "Pizza"
    const food3 = "Chicken"
  
    return(
        <ul>
            <li>{food1}</li>
            <li>{food2.toUpperCase()}</li>
            <li>{food3}</li>
        </ul>

    );
}

export default Food
