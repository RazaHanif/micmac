import React, { useState, useEffect } from "react"
import Card from "./Card"

function MainPage() {

    const [posts, setPosts] = useState([])

    // Used to get all posts from api 
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

    return(
        <div className="posts">
            {/* Map func on posts to create multiple <Card/> comps */}
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
    )
}
export default MainPage