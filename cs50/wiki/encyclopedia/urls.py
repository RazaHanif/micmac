from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.entry_new, name="add"),
    path("edit/<str:title>", views.entry_edit, name="edit"),
    path("search", views.search, name="search"),
    path("random", views.entry_random, name="random"),
    path("wiki/<str:title>", views.entry, name="entry"),
]
