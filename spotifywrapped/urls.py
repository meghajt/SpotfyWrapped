from django.shortcuts import redirect
from django.urls import path
from . import views

def redirect_to_spotifywrapped(request):
    return redirect('/spotifywrapped/')

urlpatterns = [
    path("", views.landing, name="landing"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home, name="home"),
]
