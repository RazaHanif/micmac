from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from time import sleep

from .models import User, Post, Likes, Comment, Followers


# See todo.md for server side docs
# consistent style, snake_case & 'single quotes' & space = around

REG = 'network/register.html'
TWEET_MAX = 280
TWEET_MIN = 4


def index(request):
    return render(request, 'network/index.html')


@login_required
def new_post(request, tweet):
    if request.method == 'POST':
        
        if len(tweet) > TWEET_MAX:
            return JsonResponse({
                'error': 'Tweet exceeds max length'
            }, status = 400)
        
        # This error should never happen
        # @login_required and getting the user id from request should
        # prevent it but just incase some hackermans get in
        try:
            current_user = User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            return JsonResponse({
                'error': 'user does not exist'
            }, status = 404)

        post = Post.objects.create(
            content = tweet,
            date = datetime.now(),
            edited = False,
            user = current_user,
        )
        post.save()
        
        # fake delay, just wanna see what happens in js
        sleep(3)
        
        return JsonResponse({
            'message': 'Tweet Created'
        }, status = 201)
    
    return JsonResponse({"error": "GET Method not Allowed"}, status=405)
    
@login_required
def edit_post(request, post_id):
    current_user = User.objects.get(pk=request.user.id)
    post = Post.objects.get(pk=post_id)
    
    # Serverside check if user is same as poster
    if post.user != current_user:
        return error('edit_post: Post User != Current User', 500)
    
    if request.method == 'PUT':
        form = NewPostForm(request.PUT)        
        
        # Serverside check, update and su
        if form.is_valid():            
            post.content = form.cleaned_data['tweet']
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            error('edit_post: Form is not Valid', 400)
            
    # GET
    return render(request, 'network/edit.html', {
        'form': NewPostForm(),
        'post': post,
    })
    






# Default Functions for login/logout/register
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


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

# This is not needed, do error handling in each function
def error(message, status_code):
    return JsonResponse({
            "error": message
        }, status=status_code)