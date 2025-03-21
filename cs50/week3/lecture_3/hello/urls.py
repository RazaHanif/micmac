from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("name/", views.name, name="name"),
    # placeholder path
    path("<str:name>", views.greet, name="greeting")
]