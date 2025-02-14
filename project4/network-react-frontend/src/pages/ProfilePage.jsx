import React, {useState} from "react";

function ProfilePage() {

    
    const one = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel enim vel libero tincidunt tincidunt a sit amet odio. Nulla at nisl ut."
    const two = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel enim vel libero tincidunt tincidunt a sit amet odio. Nulla at nisl ut libero pretium pharetra. Aliquam erat volutpat. Fusce convallis, sapien nec feugiat lacinia, eros eros auctor mi, id sollicitudin eros risus vel odio."
    
    const [text, setText] = useState(one)
    
    function change(){
        setText(text === one ? two : one)
    }

    return(
        <>
            <h1>Profile</h1>
            <button onClick={() => change()}>Change</button>
            <p>{ text }</p>
        </>
    )
}

export default ProfilePage