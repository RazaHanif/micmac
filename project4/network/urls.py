
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    # API ROUTES
    path("add/", views.new_post, name="add_post"),
    path("edit/", views.edit_post, name="edit_post"),
    path("posts/", views.all_posts, name="all_posts"),
    path("post/", views.this_post, name="this_post"),
    path("user_posts/", views.user_posts, name="user_posts"),
    path("following_posts", views.following_posts, name="following_posts"),
    path("follow/", views.follow, name="follow"),
    path("unfollow/", views.unfollow, name="unfollow"),
    path("like/", views.like, name="like"),
    path("unlike/", views.unlike, name="unlike"),
    path("comment/", views.unlike, name="unlike"),
]
