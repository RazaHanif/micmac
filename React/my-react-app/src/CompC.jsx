import React, {useContext} from "react"
import { UserContext } from "./MyContext"

function CompC() {

    const user = useContext(UserContext)

    return(
        <div className="box">
            <h1>CompC</h1>
            <p>{`Bye ${user}`}</p>
        </div>
    )
}

export default CompC