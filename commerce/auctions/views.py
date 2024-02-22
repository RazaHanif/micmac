from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Bid, Comment, Category, Listing, Wishlist


HOME = "auctions/index.html"
REGISTER = "auctions/register.html"


class NewListingForm(forms.Form):
    options=Category.objects.order_by("name")
    title=forms.CharField(label="Title", max_length=80)
    desc=forms.CharField(label="Description", widget=forms.Textarea)
    bid=forms.FloatField(label="Starting Bid")
    img_link=forms.URLField(label="Image Link", required=False)
    category=forms.ModelMultipleChoiceField(label="Category", queryset=options)

# Kinda useless might not keep for final version 
class NewCommentForm(forms.Form):
    comment=forms.CharField(label="Comments", widget=forms.Textarea)

# Home page 
# Shows all active listings with current prices
def index(request):
    item_with_prices = zip(Listing.objects.all(), highest_bidder_list(Listing.objects.all()))
    return render(request, HOME, {
        "items": item_with_prices,
        "listings": Listing.objects.all(),
    })

# Item Page
# Displays info about items, variable if user is logged in
def item(request, listing_id):
    item = Listing.objects.get(pk=listing_id)
    
    if request.user.is_authenticated:
    
        try:
            wishlist = Wishlist.objects.get(
                wish_listing = Listing.objects.get(id=listing_id),
                wish_user = request.user,
                )
        except Wishlist.DoesNotExist:
            wishlist = None
    else:
        wishlist = None
    
    
    return render(request, "auctions/item.html", {
        "comments": Comment.objects.filter(comment_listing=item),
        "comment_input": NewCommentForm(),
        "listing": item,
        "price": highest_bidder(item),
        "wishlist": wishlist
    })
    
# Item - Add Page 
# Displays form, Creates new item on Submit 
@login_required
def add(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        
        # Serverside check
        if form.is_valid():
            
            current_user = User.objects.get(pk=request.user.id)
            item = Listing.objects.create(
                desc = form.cleaned_data["desc"], 
                image_link = form.cleaned_data["img_link"],
                seller = current_user,
                starting_bid = form.cleaned_data["bid"], 
                title = form.cleaned_data["title"], 
                )
            item.category.set(form.cleaned_data["category"])
            item.save()
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/add.html", {
                "form": form
            })
    return render(request, "auctions/add.html", {
        "form": NewListingForm()
    })

# Item - Wishlist
# Displays all items in user wishlist, or links to homepage
@login_required
def watchlist(request):
    wishlist = Wishlist.objects.filter(wish_user=request.user)
    wishlist_id = wishlist.values_list("wish_listing", flat=True)
    item_with_prices = zip(wishlist, highest_bidder_list(wishlist_id))
    return render(request, "auctions/wishlist.html", {
        "items": item_with_prices,
        "listings": wishlist,
    })
    
# Categories Page 
# Show a list of catigories links - similar to wiki index page
def categories(request):
    # clicking a category displays all ACTIVE listings in there
    return render(request, "auctions/category.html", {
        "categories": Category.objects.order_by("name")
    })

# Shows all active listings in a given category
def categories_list(request, category_id):
    return render(request, "auctions/category_list.html", {
        "listings": Listing.objects.filter(category=category_id),
        "category": Category.objects.get(pk=category_id)
    })

# Function to add a bid to a given listing
def bid(request): 
    if request.method == "POST":
        bid = Bid.objects.create(
            bid = request.POST["bid"], 
            bid_listing = Listing.objects.get(pk=request.POST["listing_id"]), 
            bid_user = User.objects.get(pk=request.user.id)
            )
        bid.save()
    return HttpResponseRedirect(reverse("item", args=[request.POST["listing_id"]]))

# Show all listings for a given user
def user(request, user_id):
    seller = User.objects.get(pk=user_id)
    items = Listing.objects.filter(seller=seller)
    listings = zip(items, highest_bidder_list(items))
    
    return render(request, "auctions/user.html", {
        "listings": listings,
        "seller":seller,
    })

# Combines Start/End listing status functions
# Mainly for testing, will be locked to just end in production 
def change(request):
    if request.method == "POST":
        # Flips current status of listing
        item = Listing.objects.get(id=request.POST["listing_id"])
        item.active = not item.active
        item.save()
        
        # Based on status updates buyer/seller transaction#
        try:
            User.objects.get(pk=request.POST["buyer"])
        except:
            # Checks for MultiValueDictKeyError 
            # but idk how to add that in rn so just as a temp it skips
            pass
        else:
            if item.active:
                User.objects.get(pk=request.user.id).remove_transactions()
                User.objects.get(pk=request.POST["buyer"]).remove_transactions()
            else:
                User.objects.get(pk=request.user.id).add_transactions()
                User.objects.get(pk=request.POST["buyer"]).add_transactions()   
            
    return HttpResponseRedirect(reverse("item", args=[request.POST["listing_id"]])) 

# Functions to toggle active status of listing
""" Updated to change() """
def active(request):
    if request.method == "POST":
        # Update buyer/seller transaction numbers
        User.objects.get(pk=request.user.id).add_transactions()
        User.objects.get(pk=request.POST["buyer"]).add_transactions()
        
        item = Listing.objects.get(id=request.POST["listing_id"])
        # item.active = not item.active
        item.active=False
        item.save()
            
    return HttpResponseRedirect(reverse("item", args=[request.POST["listing_id"]])) 
def reactive(request):
    if request.method == "POST":
        # Update buyer/seller transaction numbers
        User.objects.get(pk=request.user.id).remove_transactions()
        User.objects.get(pk=request.POST["buyer"]).remove_transactions()
        
        item = Listing.objects.get(id=request.POST["listing_id"])
        # item.active = not item.active
        item.active=True
        item.save()
    return HttpResponseRedirect(reverse("item", args=[request.POST["listing_id"]])) 

# Add/Delete item from Wishlist
# Checks if obj exists to prevent multiple objs for same user and listing
def wish(request):
    if request.method == "POST":
        try:
            wishlist = Wishlist.objects.get(
                wish_listing = Listing.objects.get(id=request.POST["listing_id"]),
                wish_user = request.user
                )
            wishlist.delete()
            return HttpResponseRedirect(reverse("watchlist"))
        
        except Wishlist.DoesNotExist:
            wishlist = Wishlist.objects.create(
                wish_listing = Listing.objects.get(id=request.POST["listing_id"]),
                wish_user = request.user
            )
            wishlist.save()
            return HttpResponseRedirect(reverse("watchlist"))

    return HttpResponseRedirect(reverse("index"))
    
# Add a comment obj using NewCommentForm
# Dont think this needs to use NewCommentForm for one input?
def comment(request):
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        # redundent serverside validation
        if form.is_valid():
            current_user = User.objects.get(pk=request.user.id)
            comment = Comment.objects.create(
                comment=form.cleaned_data["comment"], 
                comment_listing=Listing.objects.get(id=request.POST["listing_id"]), 
                comment_user=current_user
                )
            comment.save()
        return HttpResponseRedirect(reverse("item", args=[request.POST["listing_id"]]))


# Reusable func to get highest bid obj for a given item
""" Maybe run this as default whenever some interaction happens with bidding """
def highest_bid(item):
    bids = Bid.objects.filter(bid_listing=item)
    
    if not bids:
        return item.starting_bid
    highest_bid = bids.aggregate(Max('bid'))
    
    return max(highest_bid["bid__max"], item.starting_bid)

# Quick reusable function 
# Gets the Bid Instance of the highest_bidder on a given item
def highest_bidder(item):
    return Bid.objects.filter(bid_listing=item).order_by("-bid").first()

def highest_bidder_list(list):
    listings = []
    for item in list:
        listings.append(highest_bidder(item))
        
    return listings


# Prewritten User Functions 
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

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
            return render(request, REGISTER, {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, REGISTER, {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, REGISTER)
