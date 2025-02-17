import React, { useState, useEffect } from "react"
import Card from "./Card"

function MainPage() {
    // Work on making this card talk to api and get info
    // Break down Card into smaller chunks and fill in info with props
    // figrue out how to render multiple Cards within loop

    const [posts, setPosts] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/posts') // For testing changing the path name
        .then ((response) => {
            if (response.status != 200){
                const err = new Error(response.status)
                err.name = 'LoadingAllPostsError'
                throw err
            }

            return response.json()
        })
        .then((data) => {
            setPosts(data)
        })
        .catch((err) => {
            console.error('Error fetching posts:', err)
        })
    }, [])

    useEffect(() => {
        console.log(`in the second useEffect:`)
        console.log(posts)
    }, [posts])

    return(
        <>
            <h1>MainPage</h1>
            <div className="posts">
                {posts.map(post => (
                    <Card 
                        key={post.id}
                        id={post.id}
                        user={post.creater_id}
                        content={post.content}
                        date={post.date}
                        edited={post.edited}
                    />
                ))}

            </div>
        </>
    )
}
export default MainPage