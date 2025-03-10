import React, { useState } from "react";

function Car(){

    const [car, setCar] = useState({year: 2019, 
                                    make: "Honda", 
                                    model: "CR-V"
    })

    function handleYearChange(e){
        setCar(prevCar => ({
            ...prevCar,
            year: e.target.value,
        }))
        
    }
    function handleMakeChange(e){
        setCar(prevCar => ({
            ...prevCar,
            make: e.target.value,
        }))
    }
    function handleModelChange(e){
        setCar(prevCar => ({
            ...prevCar,
            model: e.target.value,
        }))
    }

    return(
        <div>
        <p>Your car is: {car.year} {car.make} {car.model}</p><br/>

        <input type='number' value={car.year} onChange={handleYearChange}/><br/>
        <input type='text' value={car.make} onChange={handleMakeChange}/><br/>
        <input type='text' value={car.model} onChange={handleModelChange}/><br/>
        </div>
    )

}

export default Car