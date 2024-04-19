// Basic stuff to initialize onload
document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#new-btn').addEventListener('click', openNewPopup);
    // document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  
    // By default, load all posts
    loadAllPosts();
});

how = 'How did you get here?'

// Create new post -- still need to add this in html
function openNewPopup() {
    // Load all info into new post popup
    document.querySelector('#new-user').value = username
    document.querySelector('#new-post').value = ''
    document.querySelector('#new-submit-btn').addEventListener('click', createNewPost)
    document.querySelector('#new-close-btn').addEventListener('click', closeNewPopup)

    // Run animation to display the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'visible'
	})
	fill.style.animationName = 'softOpen'
	fill.style.animationPlayState = 'running'
}

// Close the new post popup
function closeNewPopup() {
	// Reset all the values for next post (redundent but just incase)
    document.querySelector('#new-user').value = ''
    document.querySelector('#new-post').value = ''

    // Remove eventlisteners (redundent but just incase) 
    document.querySelector('#new-submit-btn').removeEventListener('click', createNewPost)
    document.querySelector('#new-close-btn').removeEventListener('click', closeNewPopup)


	// Run animation to close the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'hidden'
	})
	fill.style.animationName = 'softClose'
	fill.style.animationPlayState = 'running'
}

function createNewPost() {
    // Create some second fill layer that has a loading gif
    // Create the post in the db
    fetch('/add', {
        method: 'POST',
        body: JSON.stringify({
            post: document.querySelector('#new-post').value
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
            document.querySelector('#new-error').value = data.error
            document.querySelector('#new-error').style.color = 'red'
            document.querySelector('#new-error').style.opacity = 100
        }
    })
}


/* 
    Populate all posts onto home page
    Use django fixtures to create some fake posts? 
    https://docs.djangoproject.com/en/stable/howto/initial-data/

    Make this a reusable function that can be called from within other routes
    or make it so that you can choose what data is displayed
    instead of creating a different func for each "Page"
*/

// Routes to get posts (all, user, following)
// All use the renderPosts method to display posts on page
// Kinda built in error check that will just console log error (can make this better)

// Will need to add functionality to display which route is selected
function loadAllPosts() {
    fetch('/posts')
    .then(response => response.json())
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.message)
            error.name = "LoadingAllPostsError"
        }
    })
    .then(renderPosts(posts))
    .catch(error => {
        if (error?.name == "LoadingAllPostsError") {
            console.log(error)
        }
    })
}

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
            const error = new Error(response.message)
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

function loadFollowingPosts() {
    fetch('/following_posts')
    .then(response => response.json())
    .then(response => {
        if (response.status != 200){
            const error = new Error(response.message)
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
            const error = new Error(response.message)
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
function renderPosts(posts) {

    // Clear 'main' div 
    const main = document.querySelector('content')
    main.innerHTML = ''

    // Create and add each post to the 'main' div
    posts.forEach(post => {
        const container = document.createElement('div')
        container.className = 'post-container'

        const top = document.createElement('div')
        top.className = 'post-top'

        const postUsername = document.createElement('p')
        postUsername.className = 'username text-info'
        postUsername.innerHTML = post.creator
        
        const postDate = document.createElement('p')
        postDate.className = 'date'
        postDate.innerHTML = post.date

        top.append(postUsername, postDate)
        container.append(top)

        const upper = document.createElement('div')
        upper.className = 'post-upper-middle'

        const content = document.createElement('div')
        content.className = 'post-content'
        content.innerHTML = post.content

        upper.append(content)
        container.append(upper)

        const lower = document.createElement('div')
        lower.className = 'post-lower-middle'

        const editedFlag = document.createElement('p')
        editedFlag.className = 'edited'
        editedFlag.innerHTML = 'Edited'
        if (post.edited) {
            editedFlag.style.opacity = 100
        } else {
            editedFlag.style.opacity = 0
        }

        lower.append(editedFlag)
        container.append(upper)

        const bottom = document.createElement('div')
        bottom.className = 'post-bottom'

        const bottomLeft = document.createElement('div')
        bottomLeft.className = 'bottom-left'

        const likeBtn = document.createElement('div')
        likeBtn.className = 'like-btn'
        likeBtn.addEventListener('click', () => toggleLike(post.id))
        likeBtn.innerHTML = '&lt;3'
        const likeCount = document.createElement('p')
        likeCount.className = 'like-count'
        // Figure this part out, will need to add somthing in the api to calculate the count
        likeCount.innerHTML = '...'

        bottomLeft.append(likeBtn, likeCount)
        bottom.append(bottomLeft)

        const bottomCenter = document.createElement('div')
        bottomCenter.className = 'bottom-center'

        const comments = document.createElement('div')
        comments.className = 'post-comments'
        // Forgot to create an api route for this. Create a way to get all comments for a given post
        comments.innerHTML = 'comments go here.....'

        bottomCenter.append(comments)
        bottom.append(bottomCenter)

        const bottomRight = document.createElement('div')
        bottomRight.className = 'bottom-right'

        const editBtn = document.createElement('div')
        editBtn.className = 'edit-btn text-muted'
        editBtn.innerHTML = 'EditThisShit'
        editBtn.addEventListener('click', () => editPost(post.id))

        bottomRight.append(editBtn)
        bottom.append(bottomRight)

        container.append(bottom)

        main.append(container)
    })
}