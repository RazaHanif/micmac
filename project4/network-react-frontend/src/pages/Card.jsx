import React, { useState, useEffect, useContext } from "react";
import { PostContext } from "./MainPage";
import PropTypes from 'prop-types'

function Card() {
    // Placeholder for user image - i dont have backend func for this
    const imgSrc = "https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f9f1.svg"

    // Context for the post
    const post = useContext(PostContext)

    // deconstruct props and declare inital vars
    const [userState, setUserState] = useState(post.creater_id)
    const [contentState, setContentState] = useState(post.content)
    const [dateState, setDateState] = useState(post.date)
    const [editedState, setEditedState] = useState(post.edited)

    // Checks if post was made today, if made today will change date to 'today'
    useEffect(() => {
        let today = new Date()
        today = today.toISOString().split('T')[0]

        if (dateState == today){
            setDateState("today")
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
            setUserState(data)
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
                    <p className="card-edited-flag">{editedState ? 'edited' : ""}</p>
                    <p>&hearts;</p>
                </div>
            </div>
        </div>
    );
}


export default Card

