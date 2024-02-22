from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:category_id>", views.categories_list, name="item_categories"),
    path("item/active", views.active, name="active"),
    path("item/add", views.add, name="add"),
    path("item/bid", views.bid, name="bid"),
    path("item/change", views.change, name="change"),
    path("item/comment", views.comment, name="comment"),
    path("item/<int:listing_id>", views.item, name="item"),
    path("item/reactive", views.reactive, name="reactive"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("user/<int:user_id>", views.user, name="user"),
    path("wish", views.wish, name="wish")
]
