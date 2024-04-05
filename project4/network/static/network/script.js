// do all the basic on load stuff up here first

// Create new post -- still need to add this in html
function open_new_popup() {
    /* 
        New email popup should have
            P - User name
            Form Text Input - Post
            Btn - Create New Post
    */

    // Load all info into new post popup
    document.querySelector('#new-user').value = username
    document.querySelector('#new-post').value = ''
    document.querySelector('#new-submit-btn').addEventListener('click', create_new_post)
    document.querySelector('#new-close-btn').addEventListener('click', close_new_popup)


    // Run animation to display the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'visible'
	})
	fill.style.animationName = 'softOpen'
	fill.style.animationPlayState = 'running'
}

// Close the new post popup
function close_new_popup() {
	// Reset all the values for next email
    document.querySelector('#new-user').value = ''
    document.querySelector('#new-post').value = ''

    // Remove eventlisteners
    document.querySelector('#new-submit-btn').removeEventListener('click', create_new_post)
    document.querySelector('#new-close-btn').removeEventListener('click', close_new_popup)


	// Run animation to close the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'hidden'
	})
	fill.style.animationName = 'softClose'
	fill.style.animationPlayState = 'running'
}

function create_new_post() {

    // Create some second fill layer that has a loading gif
    // Until the route returns something
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
            close_new_popup()
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

/* 
    For the posts use the hierarchy layed out in the index.html
    create dynamically obvs

    idk maybe avoid react for this project and update it with that later??
*/