import React, {useState, createContext} from "react";
import CompA from "./CompA";


// useContext() = React hook that lets you pass values within nested components without using props

/* 
Provider Comp

1. import {createContext}
2. export const Var = createContext()
3.  <Var.Provider value={value}>
     <Child />
    </Var.Provider>
*/

/* 
Consumer Comp
1.  import {useContext}
    import { Var } from ./ProviderComp
2. const value = useContext(Var)
*/

export const UserContext = createContext()

function MyContext() {

    const [user, setUser] = useState("Raza")

    return(
        <div className="box">
            <h1>Context</h1>
            <h2>{`Hello ${user}`}</h2>
            <UserContext.Provider value={user}>
                <CompA></CompA>
            </UserContext.Provider>
        </div>
    )

}

export default MyContext