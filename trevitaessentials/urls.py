# Created by Amit
from django.contrib import admin
from django.urls import path
from trevitaessentials import views

urlpatterns = [
    path("",views.home, name="home"),
    path("index",views.index, name="index"),
    path("about",views.about, name="about"),
    path("services",views.services, name="services"),
    path("products",views.products, name="products"),
    path("contact",views.contact, name="contact"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("signout",views.signout, name="signout"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("socialcontacts",views.socialcontacts, name="social_contacts"),
    path("socialcontactdetails/<int:id>",views.socialcontactdetails,name="social_contacts_details"),
    path('testing', views.testing, name='testing')
]
