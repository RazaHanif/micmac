from django.contrib import admin

# Register your models here.
from .models import Bid, Category, Comment, Listing, User, Wishlist


# Create a superuser -- python3 manage.py createsuperuser
""" Admin interface:
        Add, Delete, Edit, View any lisiting, comments or bids
"""
class BidAdmin(admin.ModelAdmin):
        list_display = ("bid", "bid_user", "bid_listing")

class CommentAdmin(admin.ModelAdmin):
        list_display = ("comment", "comment_user", "comment_listing")

class ListingAdmin(admin.ModelAdmin):
        list_display = ("active", "title", "desc", "starting_bid", "image_link", "seller")
        

 

admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(User)
admin.site.register(Wishlist)