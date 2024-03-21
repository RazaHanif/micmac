# TODO:

## Models:
### Posts:
        Id
        User
        Content
        Date
        Edited
        Likes
        Comment

### Users:
        Id
        Name
        Followers
        Following
        Posts
    
### Comments:
        Id
        Posts
        Content
    
### Likes:
        Id
        Post

## Server Side: API ROUTES
### newPost(current_user_id, content): POST
        required input from client, current user id & content

        json {
            user: current user
            content: the content
        }

        check if current user exists
        check if content is within max_length constraint
        if either fail output
            return json response {
                message: specific error
            } code: 400

        create a new post{
            content : content
            date: new datetime.now()
            edited: False
            user : user
        }

        if all good output
        return json response {
            message: success
        } code: 200

### editPost(post_id): PUT
        Used to update the tweet with updated content
        required input from client is user, content & post id

        get post with id

        if content exceeds max_length output error
        if post doesnt exist output error
        if current user != post user output error

        update entry in db {
            content: new content
            edited: True
        }

        if all good output
            return json response {
                message: all good
            }code: 200

**ALL GET POST ROUTES** 
    implement django paginator
    run numOfLikes function and add it for each post
        all posts are a list of dicts, for each dict check numOfLikes and add that category before returning

        do it while you pull the data into the dict to start with so you dont have to traverse the list again

### getAllPost(): GET
        Used to get all posts

        no required input from client

        get all posts from db
        include numOfLikes

        if no posts
            reutn json response{
                posts: None
            } code: 404

        if all good return list of posts
            return json response{
                posts: posts
            } code: 200

### getThisPost(post_id): GET    
        Used to get the specific tweet

        required input from client is post id

        get post from db
        include numOfLikes

        if post doesnt exist output
            return json response {
                message: not found
            } code: 404

        if all good output
        return json response {
            tweet: all tweet info
        } code: 200

### getUsersPosts(user_id): GET
        Used to get all posts from current_user

        input required from client, current user id

        get all posts from db, where poster is current user
        include numOfLikes

        if no posts
            reutn json response{
                posts: None
            } code: 404

        if all good return list of posts
            return json response{
                followers: numOfFollowers
                following: numOfFollowing
                posts: posts
            } code: 200


<!-- Idk this seems redundent -->
### getFollowingPosts(current_user_id): GET
        Used to get all posts from users that current user is following

        input required from client, current user id

        get all user ids current user follows

        get all posts from db, posted by those users

        if no posts
            reutn json response{
                posts: None
            } code: 404

        if all good return list of posts
            return json response{
                posts: posts
            } code: 200

<!-- Could combine this with unfollow with a flag -->
<!-- follow(current_user_id, follow_user_id, unfollow=False) -->
### follow(current_user_id, follow_user_id): PUT
        input required from client, current user id, following user id

        if current user == follwojng user 
            error

        check if current user & new user exist else error
            return json error{
                message: {x} user id does not exists
            } code 404

        try to get this from following table
            follwer - current user
            following - new user
        if you get it
            return json error {
                message: {current user} already follwoing {new user}
            } code: 400
        
        else
            create that entry in db 
            do a fake 1 second delay sleep(1second)
            return json resonse {
                message: all good
            } code 200

### unfollow(current_user_id, follow_user_id): PUT
    same as follow but in delete the entry if it exists

<!-- Could combine with unlike same as follow -->
<!-- like(user_id, post_id, unlike=False) -->
### like(user_id, post_id):
        same as follows but with likes
        user cannot like own post

### unlike(user_id, post_id):
        same as likes but delete the entry if it exists

## Server Side: Internal

### userLike(user_id, post_id):
    Checks if user likes this post
        return true/false

### numOfLikes(post_id):
    Checks how many likes a post has
    count how many times the post is in the likes table
        return count

### numOfFollow(user_id):
    Used to get the number of accounts the current user follows

    iterate through following table
        followerCount++ when follower == user_id
        followingCount++ when following == user_id

        return counts


## Client Side:

### Post Layout:
        Layout to follow anywhere posts are displayed
        
        +-------------------------------------------------+
        |                      USER                       |
        |                      date                       |
        |                                                 |
        |                                                 |
        |                     CONTENT                     |
        |                                                 |
        |                     (edited)                    |
        |----------+----------------------------+---------|
        | Likes    |                            |         |
        | LikeBtn  |    comments|scrollable     | EditBtn |
        +-------------------------------------------------+

        Django Paginator
        Posts should load 10 at a time,
            with a nextBtn to load next 10
            and prevBtn to load previous 10
            buttons should be greyed out with not usable


### Home Page:
        Show all posts from all users newest - oldest
        10 at a time following above guideline


### Profile Page:
        Users profile page should follow same guidelines as homepage

        Display numFollowers & numFollowing
        <!-- Maybe this can be clickable and show a list of all the names of users in that category? -->

#### OtherSignedIn:
        Users should be able to follow or unfollow a user from thier profile page
        
        button should be colored and say "Follow" if not followed
        and be greyed (pressed in) and say "Following" if following

### Following Page: SIGNED IN
        Same as Home page but show only posts from users that current user follows


### New Post: SIGNED IN
        Open popup (similar to email view)
        Empty Text Area with button on bottom right
            submit user & content
                body: JSON.stringify({
                    user: current_user
                    content: content
                })
        on submit close popup and refresh content on page


### Edit Post: SIGNED IN
        edit button only availbe to the user who posted the tweet, else hidden
            content of post becomes a prefilled text area with save btn on bottom right
            use getThisPost(post_id) to prefill text area
        
        check if content iswithin maxlength if not dont submit, just show error

        submit to editPost(post_id) if all good use js to toggle back to content hide textarea and btn, do not refresh page


### Like / Unlike: SIGNED IN
        Users should be able to like/unlike posts made by others
        Like btn should not be displayed for posts made by current user

        Like btn should be a heart or thumbs up that fills in when when the liked status is true    


# Random Notes:
    Create - Post/Put
    Read - Get
    Update - Put/Post/Patch
    Delete - Delete

```py
    urlpatterns = [
        path("", views.index, name="index"),
        path("login", views.login_view, name="login"),
        path("logout", views.logout_view, name="logout"),
        path("register", views.register, name="register"),

        # API Routes
        path("emails", views.compose, name="compose"),
        path("emails/<int:email_id>", views.email, name="email"),
        path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
    ]
```

    