from django.shortcuts import redirect
from django.urls import path
from . import views

def redirect_to_spotifywrapped(request):
    return redirect('/wrapped/')

urlpatterns = [
    path("", views.landing, name="landing"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("home/", views.home, name="home"),
    path("delete-account/", views.delete_account, name="delete_account"),
    path("profile/", views.profile, name="profile"),
    path("contact-us/", views.contact_us, name="contact_us"),
]
