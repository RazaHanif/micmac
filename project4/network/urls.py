
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    # API ROUTES
    path("add/<str:tweet>", views.new_post, name="add_post"),
    path("edit/<int:post_id>/<str:tweet>", views.edit_post, name="edit_post"),
    path("posts", views.all_posts, name="all_posts"),
    path("post/<int:post_id>", views.this_post, name="this_post"),
    path("posts/<int:user_id>", views.their_posts, name="their_posts"),
    path("posts/following/<int:user_id>", views.following_posts, name="following_posts"),
    path("follow/<int:follow_id>", views.follow, name="follow"),
    path("unfollow/<int:follow_id>", views.unfollow, name="unfollow"),
    path("like/<int:post_id>", views.like, name="like"),
    path("unlike/<int:post_id>", views.unlike, name="unlike"),
    path("comment/<int:post_id>/<str:comment>", views.unlike, name="unlike"),
]
