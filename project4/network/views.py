from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User, Post, Likes, Comment, Followers

import datetime

class NewPostForm(forms.Form):
    content=forms.CharField(label="Tweet", widget=forms.Textarea, max_length=280, min_length=4)

# Just to get rid of pylance error
REG = "network/register.html"

'''
Make this server side act more like an api with json responses

    OK:
    emails = emails.order_by("-timestamp").all()
    return JsonResponse([email.serialize() for email in emails], safe=False)
    
    NOT OK:
    return JsonResponse({"error": "Email not found."}, status=404)
    
and then all render everything on client side with js 
'''

def index(request):
    return render(request, "network/index.html")

'''
New Post:
        Open popup (similar to email view)
        empty text area, on submit auto fill id, User, Date, Comment
        refresh on submit
'''

@login_required
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        
        # Serverside check
        if form.is_valid():
            
            current_user = User.objects.get(pk=request.user.id)
            post = Post.objects.create(
                content = form.changed_data['tweet'],
                date = datetime.datetime.now(),
                edited = False,
                user = current_user,
            )
            post.save()
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/add.html", {
                "form": form
            })
            
    return render(request, "network/add.html", {
        "form": NewPostForm()
    })
    
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

# Error handling logic for testing
def error(message, status_code):
    return JsonResponse({
            "error": message
        }, status=status_code)