from django.contrib import admin
from django.urls import path, include
from trevitaessentials import views

urlpatterns = [
    path("",views.index, name="index"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("signout",views.signout, name="signout"),
    path("dashboard",views.dashboard, name="dashboard"),
    
    
    
    
]
