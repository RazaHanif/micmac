// Basic stuff to initialize onload
document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#new-btn').addEventListener('click', open_new_popup);
    // document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  
    // By default, load all posts
    load_posts('all');
});

how = 'How did you get here?'

// Create new post -- still need to add this in html
function open_new_popup() {
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
	// Reset all the values for next post (redundent but just incase)
    document.querySelector('#new-user').value = ''
    document.querySelector('#new-post').value = ''

    // Remove eventlisteners (redundent but just incase) 
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

// type = all | user | following
function load_posts(type) {
    let url;
    switch(type) {
        case "all":
            url = '/posts'
            break;
        case "user":
            url = '/user_posts'
            break;
        case "following":
            url = '/following_posts'
            break
        default:
            console.log(how)
            return how
    }

    fetch(url)
    .then(response => response.json())
    /* 
        Finish the implementation of how posts with the right info
    */
    .then(posts => {
      posts.forEach(post => {
            const post_username = document.createElement('p')
            post_username.className = 'username text-info'
            post_username.innerHTML = post.user



            const top = document.createElement('div')    
        
        
        
        
        
        const container = document.createElement('div')
            container.className = 'post-container'






              const element = document.createElement('div')
              element.innerHTML = output
              element.className = 'email_div'
              if (email.read && mailbox === 'inbox') {
                  element.className += ' read'
              }
              element.addEventListener('click', () => {
                  open_popup(email.id)
              })
  
              document.querySelector('#content').append(element)
      });
    })
}

/* 
    For the posts use the hierarchy layed out in the index.html
    create dynamically obvs

    idk maybe avoid react for this project and update it with that later??
*/