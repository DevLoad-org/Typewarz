from os import name
from django.urls import path

from . import views

app_name = "typing_test"
urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="index"),
    path("login", views.login, name = "login"),
    path("register", views.register, name = "register"),
    path("userLogout", views.userLogout, name = "userLogout"),
    path("typing-test", views.test, name="test"),
    path("results", views.result, name="result"),
    path("user", views.user, name = "user"),
    path("how-to-play", views.info, name="how-to")
]