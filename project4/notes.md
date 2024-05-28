# Docs:

TODO:
    change all docs to just return full dataset//
    no 10 post per page, will do infinite scroll like in lecture//

    make a bunch of fake posts/users and real superuser
    log in and test

    Create Admin page//

    continue js

    new/edit/comment/like/follow

    compare to mail - check the csrf_exempt & 505 errors//

    instead of error if no posts, return a "no posts aval"

## Server Side: API ROUTES
### POST /new - new_post():
        Used to create a new post by current user
        Requires input of "post" which is the content of a post
        length of post can be 4 - 280 characters
        
        fetch('/add', {
            method: 'POST',
            body: JSON.stringfy({
                post: 'Writing docs sucks!',
            })
        })

        if all good route will respond status 201
        {
            message: "Tweet Created"
        }

        if data is not provided will respond with error status 405
        if data provided is not valid will respond with error status 400
    
### PUT /edit - edit_post():
        Used to update a post with new content and changes edited flag

        fetch('/edit', {
            method: 'PUT',
            body: JSON.stringfy({
                post: 'Editing docs sucks too!',
                post_id: 5,
            })
        })

        if all good will respond with status 200
        {
            message: "Success"
        }

        if data is not provided will respond with error status 405
        if data provided is not valid will respond with error status 400
        if post to edit does not exist, will respond with an error status 403

### GET /posts - getAllPost():
        Used to get all posts in db in reverese chrono order

        fetch('/posts')

        if all good will respond with status 200
        and a dict with all posts

### GET /post - this_post(): 
        Used to get a specific tweet using post_id

        fetch('/post', {
            method: 'GET',
            body: JSON.stringfy({
                post_id: 5,
            })
        })

        if all good will respond with status 200
        and a dict of the post

        if post does not exist will return with error status 404

### GET /user_posts - user_posts():
        Used to get all posts from a given user in reverse chrono order

        fetch('/user_posts', {
            method: 'GET',
            body: JSON.stringfy({
                user_id: 5,
            })
        })

        if all good will respond with status 200
        and a dict of all posts

        if user or posts dont exist will return with error status 404

### GET /following_posts - following_posts():
        Used to get all the posts from users that current user is following in reverse chrono order

        fetch('/follwoing_posts')

        if all good will respond with status 200
        and a dict of all posts

        if user or posts dont exist will return with error status 404

### GET /user - user():
        Used to get all info about a particular user
        used to display username and compare current user to this user

### PUT /follow - follow():
        Creates instance of current user follows this user

        fetch('/follow', {
            method: 'PUT',
            body: JSON.stringfy({
                follow_id: 5,
            })
        })

        if all good will respond with status 200

        if users dont exist will respond with error status 404

### PUT /unfollow - unfollow():
        Creates instance of current user unfollows this user

        fetch('/unfollow', {
            method: 'PUT',
            body: JSON.stringfy({
                follow_id: 5,
            })
        })

        if all good will respond with status 200

        if users dont exist will respond with error status 404

### PUT /like - like():
        Creates instance of current user likes this post

        fetch('/like', {
            method: 'PUT',
            body: JSON.stringfy({
                post_id: 5,
            })
        })

        if all good will respond with status 200

        if post dont exist will respond with error status 404

### PUT /unlike - unlike():
        Creates instance of current user unlikes this post

        fetch('/unlike', {
            method: 'PUT',
            body: JSON.stringfy({
                post_id: 5,
            })
        })

        if all good will respond with status 200

        if post dont exist will respond with error status 404