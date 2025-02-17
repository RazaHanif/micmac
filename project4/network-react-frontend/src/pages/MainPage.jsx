import React, { useState } from "react"
import Card from "./Card"

function MainPage() {
    // Work on making this card talk to api and get info
    // Break down Card into smaller chunks and fill in info with props
    // figrue out how to render multiple Cards within loop

    

    return(
        <>
            <div className="posts">
                <Card></Card>
                <Card></Card>
                <Card></Card>
                <Card></Card>
                <Card></Card>
            </div>
        </>
    )
}

export default MainPage