import React, { useState, useEffect } from "react";

function Card(props) {
    // Placeholder for user image - i dont have backend func for this
    const imgSrc = "https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f9f1.svg"

    // deconstruct props and declare inital vars
    const [user, setUser] = useState(props.user)
    const [content, setContent] = useState(props.content)
    const [date, setDate] = useState(props.date)
    const [edited, setEdited] = useState(props.edited)
    const [id, setId] = useState(props.id)

    // Checks if post was made today, if made today will change date to 'today'
    useEffect(() => {
        let today = new Date()
        today = today.toISOString().split('T')[0]

        if (props.date == today){
            setDate("today")
        }
        else {
            setDate(props.date)
        }
    }, [])

    // Used to get the username for each post
    useEffect(() => {
        const url = 'http://127.0.0.1:8000/user/' + props.user

        fetch(url, {
            method: 'GET',
        })
        .then(response => {
            return response.json()
        })
        .then(data => {
            setUser(data)
        })
        .catch((err) => {
            console.error('Error fetching username:', err)
        })
    }, [])

    
    return(
        <>
            <div className="card">
                <div className="card-user">
                    <div className="card-user-pic">
                        <img src={imgSrc} alt="profile picture"/>
                    </div>
                    <div className="card-user-name">
                        {user.username}
                    </div>

                </div>
                <div className="card-post">
                    <div className="card-text">
                        <p className="card-date">{date}</p>
                        <h6 className="card-content">{content}</h6>
                        <p className="card-edited-flag">{edited ? 'edited' : ""}</p>
                    </div>
                </div>
                
            </div>
        </>
    );
}

export default Card

