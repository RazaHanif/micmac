from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("following/", views.following, name="following"),
    path("login/", views.login_view, name="login"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    
    # API ROUTES
    path("new/", views.new_post, name="add_post"),
    path("comment/<int:post_id>/", views.comment, name="comment"),
    path("edit/", views.edit_post, name="edit_post"),
    path("posts/", views.all_posts, name="all_posts"),
    path("post/<int:post_id>/", views.this_post, name="this_post"),
    path("user_posts/", views.user_posts, name="user_posts"),
    path("user/<int:user_id>/", views.user, name="user"),
    path("following_posts/", views.following_posts, name="following_posts"),
    path("follow/", views.follow, name="follow"),
    path("unfollow/", views.unfollow, name="unfollow"),
    path("like/", views.like, name="like"),
    path("unlike/", views.unlike, name="unlike"),
    path("comment/", views.unlike, name="unlike"),
]