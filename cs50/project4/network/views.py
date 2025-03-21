import json
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from time import sleep
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Post, Comment



# Constants just to avoid the sonarlint errors
REG = 'network/register.html'
NO_USER_ERROR = 'Users does not exist'
NO_POST_ERROR = 'Posts does not exist'
INPUT_ERROR = 'Method Inputs are Invalid'
ERROR_POST = 'POST request required'
ERROR_PUT = 'PUT request requireds'
ERROR_GET = 'GET request required'

# Min max that can be altered later
POST_MAX = 280
POST_MIN = 4

''' Default paths '''
# Prewritten - Default Route
def index(request):
    # Renders Homepage
    context = {'curr_user_id': request.user.id}
    return render(request, 'network/index.html', context)


# Logs user in - csrf exempt cuz i cant figure it out
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON from React
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken(user)
            return JsonResponse({
                "success": True,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=200)
        else:
            return JsonResponse({
                "success": False,
                "error": "Invalid username or password"
            }, status=401)

    return JsonResponse({"error": "POST request required"}, status=400)


# Prewritten - Logs user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Prewritten - Creates new User
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
    
# Defualt to return a csrf token in http

# Probably delete this
""" def get_csrf_token(request):
    csrf_token = get_token(request)  # Get CSRF token
    response = JsonResponse({'csrfToken': csrf_token})
    response.set_cookie(
        "csrftoken", csrf_token, 
        httponly=False,  # Allow frontend access
        secure=False,    # Set to True if using HTTPS
        samesite="Lax"   # Important for cross-origin requests
    )
    return response """

def following(request):
    # Renders Homepage
    return render(request, 'network/following.html')

def profile(request):
    # Renders Homepage
    return render(request, 'network/profile.html')

''' 
    API ROUTES
    see notes.md for usage 
'''

# will probably need to add in @csrf_exempts here


# Creates new post in db
# POST
@csrf_exempt
@login_required
def new_post(request):
    # Error if request method is not correct
    if request.method != 'POST':
        return JsonResponse({
            'error': ERROR_POST
        }, status=405)
    
    # Gets/Checks data from client
    data = json.loads(request.body)
    if not (post := data.get("post", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    # Server side validation of data
    if len(post) > POST_MAX:
        return JsonResponse({
            'error': 'Post exceeds max length'
        }, status=400)
        
    if len(post) < POST_MIN:
        return JsonResponse({
            'error': 'Tweet does not meet min length'
        }, status=400)
    
    # Should not be an issue but just incase hackermans get in
    try:
        current_user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)

    # Create & Save post
    tweet = Post.objects.create(
        creater=current_user,
        content=post,
        date=datetime.now(),
        edited=False,
    )
    tweet.save()
    
    # fake delay, just wanna see what happens on client side
    sleep(2)
    
    # All good message
    return JsonResponse({
        'message': 'Tweet Created'
    }, status=201)


# Updates contents of a given post in db
# PUT 
@login_required
def edit_post(request):
    # Error if request method is not correct
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
        
    # Get/Check data from client
    data = json.loads(request.body)
    if not (post := data.get("post", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    if not (post_id := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
        
    # Server side validation of data
    if len(post) > POST_MAX:
        return JsonResponse({
            'error': 'Tweet exceeds max length'
        }, status = 400)
        
    if len(post) < POST_MIN:
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
    
    # Update content
    post.content = post
    post.edited = True
    post.save()
    
    # fake delay, just wanna see what happens in js
    sleep(2)
    
    # All good message
    return JsonResponse({
        'message': 'Success'
    }, status=200)
        

# Returns all posts from db in reveres chrono order
# GET
def all_posts(request):
    # Error if request method is not correct
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)
    
    # Gets all posts from db in reverse chrono order
    # If no posts returns error - might get rid of this
    posts = Post.objects.all().order_by('-date') 
    if not posts.exists():
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)
    
    # Convery data from Queryset to a list of dicts
    posts_data = list(posts.values())
       
    # All good response
    return JsonResponse(
        posts_data,
        safe=False,
        status=200
    )


# Returns a given post from the db
# GET
def this_post(request, post_id):
    # Error if request method is not correct
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)
    
    # Server side data validation
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)
        
    post = model_to_dict(post)
    
    # All good response
    return JsonResponse(
        post,
        safe=False,
        status=200
    )


# Returns all posts from a given user
# GET
def user_posts(request):
    # Checks if request method is not correct
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)

    # Get/Check data from client
    data = json.loads(request.body)
    if not (user_id := data.get("user_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)

    # Server side data validation
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)
    
    # Gets all posts from user in reverse chrono order
    # if no posts error -- might delete
    posts = Post.objects.filter(creater=user).order_by('-date')
    if not posts.exists():
       return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)

    # All good response
    return JsonResponse(
        posts.as_dict(),
        safe=False,
        status=200
    )


# Returns all posts from users being followed by a given user
# GET
@login_required
def following_posts(request):
    # Error if request method is not correct
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)

    # Get user and posts from db
    # If no posts return error -- might delete
    following = User.objects.get(pk=request.user.id).following.all()
    posts = Post.objects.filter(creater__in=following).order_by('-date')
    if not posts.exists():
       return JsonResponse({
            'error': NO_POST_ERROR
        }, status=404)

    # All good response
    return JsonResponse(
        posts.as_dict(),
        safe=False,
        status=200
    )
    
# Returns User object
# GET
def user(request, user_id):
    # Checks if request method is not correct
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)

    # Server side data validation
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)

    return JsonResponse({
        'username': user.username,
        'email': user.email,
    }, status=200)
    
    
# Returns Comment object
# GET
def comment(request, post_id):
    # Checks if request method is not correct
    if request.method != 'GET':
        return JsonResponse({
            'error': ERROR_GET
        }, status=405)

    # Server side data validation
    try:
        this_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({
            'error': NO_USER_ERROR
        }, status=404)
        
    comments = Comment.objects.filter(post=this_post)
    
    comments = serialize('json', comments)

    return JsonResponse(
        comments,
        safe=False,
        status=200
    )

# Updates current user follows that user
# PUT
@login_required
def follow(request):
    # Error if request method is not correct
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
        
    # Call internal toggle method
    return toggle_follow(request, False)


# Updates current user unfollows that user
# PUT
@login_required
def unfollow(request):
    # Error if request method is not correct
    if request.method == 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)

    # Call internal toggle method
    return toggle_follow(request, True)


# Handles logic to change following status
# Internal
def toggle_follow(request, unfollow):
    
    # Get/Check data from client
    data = json.loads(request.body)
    if not (user_to_follow_id := data.get("follow_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)

    # Server side validation of data
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

    # Update db
    if unfollow:
        user.following.remove(user_to_follow)
    else:
        user.following.add(user_to_follow)
        
    user.save()
    
    # All good response
    return JsonResponse({
        'message': 'Success'
    }, status=200)
    
    
# Updates current user likes this post
# PUT
@login_required
def like(request):
    # Error if request method is not correct
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
    
    # Call internal method
    return toggle_like(request, False)


# Updates current user unlikes this post
# PUT
@login_required
def unlike(request):
    # Error if request method is not correct
    if request.method != 'PUT':
        return JsonResponse({
            'error': ERROR_PUT
        }, status=405)
        
    # Call internal method
    return toggle_like(request, True)


# Handles logic to change like staus
# Internal
def toggle_like(request, unlike):
    # Get/Check data from client
    data = json.loads(request.body)
    if not (post_id := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    # Server side validation of data
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
    
    # Update db
    if unlike:
        post.likes.remove(user)
    else:
        post.likes.add(user)
    
    post.save()
    
    # All good response 
    return JsonResponse({
        'message': 'Success'
    }, status=200)
    

# Allows current user to create a comment on a given post
# POST
def create_comment(request):
    # Error if request method is not correct
    if request.method != "POST":
        return JsonResponse({
            'error': ERROR_POST
        }, status=405)
    
    # Get/Check data from client
    data = json.loads(request.body)
    if not (post_id := data.get("post_id", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    if not (comment := data.get("comment", "")):
        return JsonResponse({
            'error': INPUT_ERROR
        }, status=400)
    
    # Server side validation
    if len(comment) > POST_MAX:
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
    
    # Create new comment in db
    comment = Comment.objects.create(
        comment=comment,
        post=post,
        user=user
    )
    comment.save()
    
    # fake delay, just wanna see what happens in js
    sleep(2)
    
    # All good response
    return JsonResponse({
        'message': 'Comment Created'
    }, status=201)
    
