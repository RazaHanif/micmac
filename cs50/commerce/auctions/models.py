from django.contrib.auth.models import AbstractUser
from django.db import models

# Any time changes are made here
# python3 manage.py makemigrations
# python3 manage.py migrate


# Bids linked to User and Listing
class Bid(models.Model):
    bid = models.FloatField()
    bid_listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="bidding_listing")
    bid_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="bidding_user")
    
    def __str__(self):
        return f"{self.bid_user}: ${self.bid}"

# Category List
class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    
    def __str__(self):
        return self.name

# Comments, linked to User and Listing
class Comment(models.Model):
    comment = models.TextField()
    comment_listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="commenting_listing")
    comment_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="commenting_user")
    
    def __str__(self):
        return f"{self.comment_user}: {self.comment}"

# Lisitngs with all needed feilds, links to Bids and Categories 
""" Change to asking price & current price """
class Listing(models.Model):
    active = models.BooleanField(default=True)
    category = models.ManyToManyField("Category", blank=False, related_name="catigories")
    desc = models.TextField()
    image_link = models.URLField()
    seller = models.ForeignKey("User", on_delete=models.CASCADE, related_name="seller")
    starting_bid = models.FloatField()
    title = models.CharField(max_length=80)
    # Need to do this so I can save who made the bid and what the highest bid is
    # current_bid = models.ForeignKey("Bid", on_delete=models.CASCADE, default=0, related_name="current_bid")
    
    def __str__(self):
        return f"{self.id}: {self.title}"
    
# AbstractUser: default username, pass, email etc
class User(AbstractUser):
    transactions = models.PositiveIntegerField(default=0)
    
    def add_transactions(self):
        self.transactions += 1
        self.save()
        
    def remove_transactions(self):
        self.transactions -= 1
        self.save()
    
    def __str__(self):
        return f"{self.username}: {self.transactions}".capitalize()

# Wishlist items linked to User and Listing
class Wishlist(models.Model):
    wish_listing = models.ForeignKey("Listing", on_delete=models.CASCADE, blank=True, related_name="wishlist_listing")
    wish_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="wishlisht_user")
    
    def __str__(self):
        return f"{self.wish_user} Wants {self.wish_listing}"
        