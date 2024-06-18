/* 
    Populate all posts onto home page
    Use django fixtures to create some fake posts? 
    https://docs.djangoproject.com/en/stable/howto/initial-data/

*/

// Basic stuff to initialize onload
document.addEventListener('DOMContentLoaded', function() {

    // By default, load all posts
    loadAllPosts();

    // Use buttons to toggle between views
    // Prevents error if not logged in
    // Uses js ? chaining 
    document.querySelector('#new-btn')?.addEventListener('click', (e) => {
        e.preventDefault();
        openNewPopup();
    });
    document.querySelector('#home-btn')?.addEventListener('click', (e) => {
        e.preventDefault
        console.log("home-btn")
        loadAllPosts()
    });
    document.querySelector('#profile-btn')?.addEventListener('click', (e) => {
        e.preventDefault
        loadCurrUserProfile(curr_user_id)
    });
    document.querySelector('#following-btn')?.addEventListener('click', (e) => {
        e.preventDefault
        console.log("following-btn")
        loadAllPosts()
    });
});

// New posts 

// Open popup initalized for new post
function openNewPopup() {
    console.log('open')
    
    // Load all info into new post popup
    document.querySelector('#popup-user').innerHTML = username
    document.querySelector('#popup-post').value = ''
    document.querySelector('#popup-error').innerHTML = 'error'
    document.querySelector('#popup-error').style.opacity = 0
    document.querySelector('#popup-submit-btn').addEventListener('click', createNewPost)
    document.querySelector('#popup-close-btn').addEventListener('click', closeNewPopup)

    // Run animation to display the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'visible'
	})
	fill.style.animationName = 'softOpen'
	fill.style.animationPlayState = 'running'
    fill.style.visibility = 'visible'
}

// Close the new post popup
function closeNewPopup() {
	// Reset all the values for next post (redundent but just incase)
    document.querySelector('#popup-user').value = ''
    document.querySelector('#popup-post').value = ''

    // Remove eventlisteners (redundent but just incase) 
    document.querySelector('#popup-submit-btn').removeEventListener('click', createNewPost)
    document.querySelector('#popup-close-btn').removeEventListener('click', closeNewPopup)


	// Run animation to close the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'hidden'
	})
	fill.style.animationName = 'softClose'
	fill.style.animationPlayState = 'running'
}

// Send the post to the db
function createNewPost() {
    // Create some second fill layer that has a loading gif
    // Create the post in the db

    console.log(document.querySelector('#popup-post').value)
    fetch('/new', {
        method: 'POST',
        body: JSON.stringify({
            post: document.querySelector('#popup-post').value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if ("message" in data){
            // Stop loading animation or turn it into a check
            closeNewPopup()
        }
        else {
            // Error handling
            // Stop loading animation or turn into a x
            console.log(data.error)
            document.querySelector('#popup-error').innerHTML = data.error
            document.querySelector('#popup-error').style.color = 'red'
            document.querySelector('#popup-error').style.opacity = 100
        }
    })
}


// Edit posts 

// Open popup initalized for editing this post
function openEditPopup(postId) {
    let currentPost
    let post_id
    
    // Get the info for the post to edit
    fetch('/post', {
        method: 'GET',
        body: JSON.stringify({
            post_id: postId,
        })
    })
    .then(response => response.json())
    // Just incase post doesn't exist
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.error)
            error.name = "LoadingThisPostError"
        }
    })
    .then(data => {
        currentPost = data.content
        post_id = data.id
    })
    .catch(error => {
        if (error?.name == "LoadingThisPostError") {
            console.log(error)
        }
    })

    // Load all info into new post popup
    document.querySelector('#popup-user').value = username
    document.querySelector('#popup-post').value = currentPost
    document.querySelector('#popup-submit-btn').addEventListener('click', () => editThisPost(post_id))
    document.querySelector('#popup-close-btn').addEventListener('click', closeEditPopup)

    // Run animation to display the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'visible'
	})
	fill.style.animationName = 'softOpen'
	fill.style.animationPlayState = 'running'
}

// Close the edit post popup
function closeEditPopup() {
	// Reset all the values for next post (just incase)
    document.querySelector('#popup-user').value = ''
    document.querySelector('#popup-post').value = ''

    // Remove eventlisteners (just incase) 
    document.querySelector('#popup-submit-btn').removeEventListener('click', () => editThisPost(post_id))
    document.querySelector('#popup-close-btn').removeEventListener('click', closeEditPopup)


	// Run animation to close the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'hidden'
	})
	fill.style.animationName = 'softClose'
	fill.style.animationPlayState = 'running'
}

// Should send the edited post to the db
function editThisPost(postId) {
    console.log(`Edit ${postId}`)
    // Create some second fill layer that has a loading gif
    // Edit the post in the db
    fetch('/add', {
        method: 'PUT',
        body: JSON.stringify({
            post: document.querySelector('#popup-post').value,
            post_id: postId,
        })
    })
    .then(response => response.json())
    .then(data => {
        if ("message" in data){
            // Stop loading animation or turn it into a check
            closeNewPopup()
        }
        else {
            // Error handling
            // Stop loading animation or turn into a x
            document.querySelector('#popup-error').value = data.error
            document.querySelector('#popup-error').style.color = 'red'
            document.querySelector('#popup-error').style.opacity = 100
        }
    })
}




// Routes to get posts (All, User, Following)
// All use the renderPosts method to display posts on page
// Kinda built in error check that will just console log error (can make this better)
// Will need to add functionality to display which route is selected

// Loads all posts

/* Tryna figure out why all posts arent loading error 500 */
function loadAllPosts() {
    fetch('/posts', {
        method: 'GET'
    })
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.status)
            error.name = 'LoadingAllPostsError'
            throw error
        }

        return response.json()
    })
    .then(posts => {
        // posts is a string by default? Parse it to make it work
        posts = JSON.parse(posts)
        // Map over the posts and return only the 'fields' property
        const fields = posts.map(post => ({...post.fields, id: post.pk}))
        return fields;
    })
    .then(fields => renderPosts(fields, "all"))
    .catch(error => {
        if (error?.name == "LoadingAllPostsError") {
            console.log(error)
        }
    })
}

// Loads only this users posts
function loadUserPosts(userId) {
    fetch('/user_posts', {
        method: 'GET',
        body: JSON.stringify({
            user_id: userId,
        })
    })
    .then(response => response.json())
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.error)
            error.name = "LoadingUserPostsError"
        }
    })
    .then(renderPosts(posts))
    .catch(error => {
        if (error?.name == "LoadingUserPostsError") {
            console.log(error)
        }
    })
}

// Loads all posts from users that current user follows
function loadFollowingPosts() {
    fetch('/following_posts')
    .then(response => response.json())
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.error)
            error.name = "LoadingFollowingPostsError"
        }
    })
    .then(renderPosts(posts))
    .catch(error => {
        if (error?.name == "LoadingFollowingPostsError") {
            console.log(error)
        }
    })
}

// IDK if this is needed
// this post is really only to get post info to edit it
function loadThisPost(postId) {
    fetch('/post', {
        method: 'GET',
        body: JSON.stringify({
            post_id: postId,
        })
    })
    .then(response => response.json())
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.error)
            error.name = "LoadingThisPostError"
        }
    })
    .then(renderPosts(posts))
    .catch(error => {
        if (error?.name == "LoadingThisPostError") {
            console.log(error)
        }
    })
}


// Create and display posts on page
// Needs some work -- some routes/calcs missing
function renderPosts(posts, name) {

    // Clear 'main' div 
    const main = document.querySelector('#content')
    main.innerHTML = ''

    // Create and add each post to the 'main' div

    if (posts) {

        posts.forEach(post => {

            // Create container for post
            const container = document.createElement('div')
            container.className = 'post-container'

            // MicroContainers
            const top = document.createElement('div')
            top.className = 'post-top'

            // Query server for info on user
            const postUsername = document.createElement('p')
            postUsername.className = 'username text-info'
            let url = '/user/' + post.creater
            fetch(url, {
                method: 'GET',
            })
            .then(response => {
                return response.json()
            })
            .then(user => {
                postUsername.innerHTML = user.username
            })
            
            // Date from post
            const postDate = document.createElement('p')
            postDate.className = 'date'
            postDate.innerHTML = post.date

            // Add to container
            top.append(postUsername, postDate)
            container.append(top)

            // MicroContainers - might combine with lower
            const upper = document.createElement('div')
            upper.className = 'post-upper-middle'

            // Content from post
            const content = document.createElement('div')
            content.className = 'post-content'
            content.innerHTML = post.content

            // Add to container - might combine upper with lower
            upper.append(content)
            container.append(upper)

            // MicroContainers - might combine with upper
            const lower = document.createElement('div')
            lower.className = 'post-lower-middle'

            // Edited flag updated from post
            const editedFlag = document.createElement('div')
            editedFlag.className = 'edited'
            editedFlag.innerHTML = 'Edited'
            editedFlag.style.color = 'grey'
            if (post.edited) {
                editedFlag.style.opacity = '50%'
            } else {
                editedFlag.style.opacity = '0%'
            }

            lower.append(editedFlag)
            container.append(lower)

            // MicroContainer
            const bottom = document.createElement('div')
            bottom.className = 'post-bottom'

            // MicroMicroContainer
            const bottomLeft = document.createElement('div')
            bottomLeft.className = 'bottom-left'

            // Still need to create implementation for btn
            const likeBtn = document.createElement('div')
            likeBtn.className = 'like-btn'
            likeBtn.addEventListener('click', () => toggleLike(post.id))
            likeBtn.innerHTML = '&lt;3'
            const likeCount = document.createElement('p')
            likeCount.className = 'like-count'

            // Figure this part out
            // Will need to get like count - like is array in post
            if (post.likes.length > 0) {
                likeCount.innerHTML = post.likes.length
            } else {
                likeCount.innerHTML = 'Zero'
            }

            bottomLeft.append(likeBtn, likeCount)
            bottom.append(bottomLeft)

            const bottomCenter = document.createElement('div')
            bottomCenter.className = 'bottom-center'

            // Create new api route to get all comments for x post
            const comments = document.createElement('div')
            comments.className = 'post-comments'
            comments.innerHTML = 'Comments'

            // idk if i need this
            let commentList = []

            url = '/comment/' + post.id
            fetch(url, {
                method: 'GET',
            })
            .then(response => {
                return response.json()
            })
            .then(obj => {
                obj = JSON.parse(obj)
                
                if (obj.length > 0){
                    const fields = obj.map(post => post.fields)
                    return fields
                }

            })
            .then(fields => {
                if (fields) {
                    if (fields.length > 0) {
                        comments.innerHTML = null
                        fields.forEach(comment => {
                            const commentContainer = document.createElement('p')
                            commentContainer.className =  'post-comment-container'
                            
                            // Get the commenters name
                            let url = '/user/' + comment.user
                            fetch(url, {
                                method: 'GET',
                            })
                            .then(response => {
                                return response.json()
                            })
                            .then(user => {
                                let username = user.username
                                commentContainer.innerHTML = `${comment.comment}  - ${username}`
                                comments.append(commentContainer)
                            })
                        })
                    }
                }
            })

            bottomCenter.append(comments)
            bottom.append(bottomCenter)

            const bottomRight = document.createElement('div')
            bottomRight.className = 'bottom-right'

            // Create functionality for edit btn only if post user id == current user id
            const editBtn = document.createElement('div')
            editBtn.className = 'edit-btn text-muted'
            editBtn.innerHTML = 'EditThisShit'
            
            editBtn.addEventListener('click', () => editThisPost(post.id))

            bottomRight.append(editBtn)
            bottom.append(bottomRight)

            container.append(bottom)

            main.append(container)
        })
    }
    else {
        main.innerHTML = name
    }
}

// Idk if im gonna keep this
// Rn just grabs current user name and prints to screen
// Wanna keep curr user profile and regular profile page sepeareate
function loadCurrUserProfile(user_id) {

    let url = '/user/' + user_id
    fetch(url, {
        method: 'GET',
    })
    .then(response => {
        return response.json()
    })
    .then(user => {
        let username = user.username
        renderPosts(null, username)
    })
}

// This is redundent with loadUserPosts will rename/combine later
function loadUserProfile(user_id) {

    let url = '/user/' + user_id
    fetch(url, {
        method: 'GET',
    })
    .then(response => {
        return response.json()
    })
    .then(user => {
        let username = user.username
        renderPosts(null, username)
    })
}



// Create funcs for Home, User, Following, Profile btns/pages
// Home page should be same signed in or not
// User page should have 'Follow' or 'Following' Btn - if user signed in else blank
// Folloing page should only be for signed in users, should be able to go to User page by poster name

// Create func to like/unlike posts

// Create func to follow/unfollow users