from django.contrib import admin

# Register your models here.
from .models import Comment, Post, User


# Create a superuser -- python3 manage.py createsuperuser
""" Admin interface:
        Add, Delete, Edit, View any Post, User or Comment
"""

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(User)
