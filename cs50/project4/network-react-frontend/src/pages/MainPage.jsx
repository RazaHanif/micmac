import React, { useState, useEffect, createContext } from "react"
import Card from "./Card"

export const PostContext = createContext()

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
                <PostContext.Provider value={post} key={post.id}>
                    <Card />
                </PostContext.Provider>
            ))}
        </div>
    )
}
export default MainPage