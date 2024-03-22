
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    # API ROUTES
    path("add/<str:tweet>", views.new_tweet, name="add"),
    path("edit/<int:post_id>/<str:tweet>", views.edit_tweet, name="edit"),
    path("posts", views.all_posts, name="all"),
    path("posts/<int:user_id>", views.their_posts, name="their"),
    path("posts/following/<int:user_id>", views.following_post, name="following"),
    path("post/<int:post_id>", views.this_post, name="this"),
    path("follow/<int:follow_id>", views.follow, name="follow"),
    path("unfollow/<int:follow_id>", views.unfollow, name="unfollow"),
]
