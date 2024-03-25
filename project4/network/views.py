import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from time import sleep

from .models import User, Post, Comment

# See todo.md for server side docs

# Constants just to avoid the sonarlint errors
REG = 'network/register.html'
NO_USER_ERROR = 'Users does not exist'
NO_POST_ERROR = 'Posts does not exist'
INPUT_ERROR = 'Method Inputs are Invalid'
ERROR_POST = 'POST request required'
ERROR_PUT = 'PUT request requireds'
ERROR_GET = 'GET request required'

TWEET_MAX = 280
TWEET_MIN = 4

''' Default paths '''
# Home page
def index(request):
    return render(request, 'network/index.html')


# Logs user in
def login_view(request):
    if request.method == 'POST':

        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'network/login.html', {
                'message': 'Invalid username and/or password.'
            })
    else:
        return render(request, 'network/login.html')


# Logs user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Creates new User
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, REG, {
                'message': 'Passwords must match.'
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, REG, {
                'message': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, REG)


''' API ROUTES -- see todo.md '''

# Creates new post in db
# POST
@login_required
def new_post(request):
    if request.method != 'POST':
        return JsonResponse({
            'error': ERROR_POST
        }, status=405)
    
    data = json.loads(request.body)
    if not (tweet := data.get("post", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    
    if len(tweet) > TWEET_MAX:
        return JsonResponse({
            'error': 'Post exceeds max length'
        }, status=400)
        
    if len(tweet) < TWEET_MIN:
        return JsonResponse({
            'error': 'Tweet does not meet min length'
        }, status=400)
        
    # Not required but just incase
    try:
        current_user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)

    post = Post.objects.create(
        content=tweet,
        date=datetime.now(),
        edited=False,
        user=current_user,
    )
    post.save()
    
    # fake delay, just wanna see what happens in js
    sleep(3)
    
    return JsonResponse({
        'message': 'Tweet Created'
    }, status=201)



# Updates contents of a given post in db
# PUT 
@login_required
def edit_post(request):
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
        
    # Get data from POST request
    data = json.loads(request.body)
    if not (tweet := data.get("post", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    if not (post := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
        
    if len(tweet) > TWEET_MAX:
        return JsonResponse({
            'error': 'Tweet exceeds max length'
        }, status = 400)
        
    if len(tweet) < TWEET_MIN:
        return JsonResponse({
            'error': 'Tweet does not meet min length'
        }, status=400)

    # Again should never run into this but just incase
    try:
        current_user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)
    
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)

    if post.user != current_user:
        return JsonResponse({
            'error': 'Current User is not Post Creator'
        }, status=403)
    
    post.content = tweet
    post.edited = True
    post.save()
    
    # fake delay, just wanna see what happens in js
    sleep(3)
    
    return JsonResponse({
        'message': 'Success'
    }, status=200)
        


# Returns all posts from db in reveres chrono order
# GET
def all_posts(request):
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)
    
    posts = Post.objects.all().order_by('-date') 

    if not posts.exists():
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)
    
    page_num = request.GET.get('page')
    p = Paginator(posts, 10)
    page_obj = p.get_page(page_num)
    
    data = {
        'objects': serialize('json', list(page_obj.object_list)),
        'prev': page_obj.has_previous,
        'next': page_obj.has_next
    } 

    return JsonResponse(data, safe=False, status=200)


# Returns a given post from the db
# GET
def this_post(request):
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)
        
    data = json.loads(request.body)
    if not (post_id := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)
    
    return JsonResponse(
        post.as_dict(),
        safe=False,
        status=200
    )


# Returns all posts from a given user
# GET
def their_posts(request):
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)

    data = json.loads(request.body)
    if not (user_id := data.get("user_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)
    
    posts = Post.objects.filter(creater=user).order_by('-date')
    
    if not posts.exists():
       return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)

    page_num = request.GET.get('page')
    p = Paginator(posts, 10)
    page_obj = p.get_page(page_num)
    
    data = {
        'objects': serialize('json', list(page_obj.object_list)),
        'prev': page_obj.has_previous,
        'next': page_obj.has_next
    } 

    return JsonResponse(data, safe=False, status=200)


# Returns all posts from users being followed by a given user
# GET
@login_required
def following_posts(request):
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)

    following = User.objects.get(pk=request.user.id).following.all()
    posts = Post.objects.filter(creater__in=following).order_by('-date')
    
    if not posts.exists():
       return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)

    page_num = request.GET.get('page')
    p = Paginator(posts, 10)
    page_obj = p.get_page(page_num)
    
    data = {
        'objects': serialize('json', list(page_obj.object_list)),
        'prev': page_obj.has_previous,
        'next': page_obj.has_next
    } 

    return JsonResponse(data, safe=False, status=200)


# Updates current user follows that user
# PUT
@login_required
def follow(request):
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
        
    return toggle_follow(request, False)


# Updates current user unfollows that user
# PUT
@login_required
def unfollow(request):
    if request.method == 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)

    return toggle_follow(request, True)


# Handles logic to change following status
# Internal
def toggle_follow(request, unfollow):
    data = json.loads(request.body)
    
    if not (user_to_follow_id := data.get("follow_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
        
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return JsonResponse({
        'error': NO_USER_ERROR
        }, status=404)
    try:
        user_to_follow = User.objects.get(pk=user_to_follow_id)
    except User.DoesNotExist:
        return JsonResponse({
        'error': NO_USER_ERROR
        }, status=404)

    if unfollow:
        user.following.remove(user_to_follow)
    else:
        user.following.add(user_to_follow)
        
    user.save()
    
    return JsonResponse({
        'message': 'Success'
    }, status=200)
    
    
# Updates current user likes this post
# PUT
@login_required
def like(request):
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
    
    return toggle_like(request, False)


# Updates current user unlikes this post
# PUT
@login_required
def unlike(request):
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
        
    return toggle_like(request, True)


# Handles logic to change like staus
# Internal
def toggle_like(request, unlike):
    data = json.loads(request.body)
    
    if not (post_id := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)
    
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)
    
    if unlike:
        post.likes.remove(user)
    else:
        post.likes.add(user)
        
    return JsonResponse({
        'message': 'Success'
    }, status=200)
    

# Allows current user to create a comment on a given post
# POST
def create_comment(request):
    if request.method != "POST":
        return JsonResponse({
            'error': ERROR_POST
        }, status=405)
    
    data = json.loads(request.body)
    if not (post_id := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    if not (comment := data.get("comment", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    
    if len(comment) > TWEET_MAX:
        return JsonResponse({
            'error': 'Tweet exceeds max length'
        }, status=400)
        
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)
    
    try:
        user = User.objects.get(pk=request.user.id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)
    
    comment = Comment.objects.create(
        comment=comment,
        post=post,
        user=user
    )
    comment.save()
    
    # fake delay, just wanna see what happens in js
    sleep(3)
    
    return JsonResponse({
        'message': 'Comment Created'
    }, status=201)
            

