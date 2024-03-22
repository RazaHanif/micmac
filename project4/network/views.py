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

REG = 'network/register.html'
ERROR_USER = 'Users does not exist'
ERROR_POST = 'Posts does not exist'
TWEET_MAX = 280
TWEET_MIN = 4

# Redo this maybe and add a logged in and logged out view 
# redirect to log in screen
def index(request):
    return render(request, 'network/index.html')


# Creates new post in db
# POST
@login_required
def new_post(request, tweet):
    if request.method == 'POST':
        
        if len(tweet) > TWEET_MAX:
            return JsonResponse({
                'error': 'Tweet exceeds max length'
            }, status=400)
            
        if len(tweet) < TWEET_MIN:
            return JsonResponse({
                'error': 'Tweet does not meet min length'
            }, status=400)
            
        # This error should never happen
        # @login_required and getting the user id from request should
        # prevent it but just incase some hacker mans get in
        try:
            current_user = User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            return JsonResponse({
                'error': ERROR_USER
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
    
    # GET
    return JsonResponse({
        'error': 'POST request required'
    }, status=405)


# Updates contents of a given post in db
# PUT 
@login_required
def edit_post(request, post_id, tweet):
    if request.method == 'PUT':
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
                'error': ERROR_USER
            }, status=404)
        
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return JsonResponse({
                'error': ERROR_POST
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
        
    # GET
    return JsonResponse({
        'error': 'POST request required'
    }, status=405)


# Returns all posts from db in reveres chrono order
# GET
def all_posts(request):
    posts = Post.objects.all().order_by('-date') 

    if not posts.exists():
        return JsonResponse({
            'error': ERROR_POST
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
def this_post(post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': ERROR_POST
        }, status=404)
    
    return JsonResponse(
        post.as_dict(),
        safe=False,
        status=200
    )


# Returns all posts from a given user
# GET
def their_posts(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': ERROR_USER
        }, status=404)
    
    posts = Post.objects.filter(creater=user).order_by('-date')
    
    if not posts.exists():
       return JsonResponse({
            'error': ERROR_POST
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
def following_post(request):
    following = User.objects.get(pk=request.user.id).following.all()
    posts = Post.objects.filter(creater__in=following).order_by('-date')
    
    if not posts.exists():
       return JsonResponse({
            'error': ERROR_POST
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
def follow(request, follow_id):
    if request.method == 'PUT':
        return toggle_follow(request, follow_id, False)
    # GET
    return JsonResponse({
        'error': 'PUT request required'
    }, status=405)


# Updates current user unfollows that user
# PUT
@login_required
def unfollow(request, follow_id):
    if request.method == 'PUT':
        return toggle_follow(request, follow_id, True)
    # GET
    return JsonResponse({
        'error': 'PUT request required'
    }, status=405)


# Handles logic to change following status
# Internal
def toggle_follow(request, follow_id, unfollow):
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return JsonResponse({
        'error': ERROR_USER
        }, status=404)
    try:
        user_to_follow = User.objects.get(pk=follow_id)
    except User.DoesNotExist:
        return JsonResponse({
        'error': ERROR_USER
        }, status=404)

    if unfollow:
        user.following.remove(user_to_follow)
    else:
        user.following.add(user_to_follow)
        
    user.save()
    
    return JsonResponse({
        'message': 'Success'
    }, status=200)
        
# Idk if i need this, wasnt in my inital server side docs
# Will complete if needed else will delete
def create_comment(request, comment):
    pass

# Logs user in
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


# Logs user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Creates new User
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, REG, {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, REG, {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, REG)

