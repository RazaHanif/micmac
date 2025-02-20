import React, { useState, useEffect } from "react";
import PropTypes from 'prop-types'

function Card({ user, content, date, edited, postId}) {
    // Placeholder for user image - i dont have backend func for this
    const imgSrc = "https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f9f1.svg"

    // deconstruct props and declare inital vars
    const [userState, setUserState] = useState(user)
    const [contentState, setContentState] = useState(content)
    const [dateState, setDateState] = useState(date)
    const [editedState, setEditedState] = useState(edited)
    const [postIdState, setPostIdState] = useState(postId)

    // Checks if post was made today, if made today will change date to 'today'
    useEffect(() => {
        let today = new Date()
        today = today.toISOString().split('T')[0]

        if (dateState == today){
            setDate("today")
        }
        else {
            setDate(date)
        }
    }, [])

    // Used to get the username for each post
    useEffect(() => {
        const url = 'http://127.0.0.1:8000/user/' + userState

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
        <div className="card">
            <div className="card-user">
                <div className="card-user-pic">
                    <img src={imgSrc} alt="profile"/>
                </div>
                <div className="card-user-name">
                    {userState.username}
                </div>

            </div>
            <div className="card-post">
                <div className="card-text">
                    <p className="card-date">{dateState}</p>
                    <h6 className="card-content">{contentState}</h6>
                    <p className="card-edited-flag">{editedState ? 'eEditedState' : ""}</p>
     postIdState     PostIdState</div>
            </div>
            
        </div>
    );
}

PropCard.propTypes = {
    name: PropTypes.string,
    date: PropTypes.string,
    id: PropTypes.number,
    user: PropTypes.number,
    edited: PropTypes.bool,
}

PropCard.defaultProps = {
    name: "Guest",
    age: 0,
    isStudent: false,
}

export default Card

