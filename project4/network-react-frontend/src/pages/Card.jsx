import React, { useState } from "react";

function Card(props) {
    const imgSrc = "https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f9f1.svg"

    const [user, setUser] = useState(props.user)
    const [content, setContent] = useState(props.content)
    const [date, setDate] = useState(props.date)
    const [edited, setEdited] = useState(props.edited)
    const [id, setId] = useState(props.id)
  
    return(
        <>
            <div className="card">
                <div className="card-user">
                    <div className="card-user-pic">
                        <img src={imgSrc} alt="profile picture"/>
                    </div>
                    <div className="card-user-name">
                        {user}
                    </div>

                </div>
                <div className="card-post">
                    <div className="card-text">
                        <p>Post ID: {id}</p>
                        <p>Date: {date}</p>
                        <p>Edited: {edited ? "Edited" : "Not Edited"}</p>
                        <p>Content: {content}</p>
                    </div>
                </div>
                
            </div>
        </>
    );
}

export default Card

