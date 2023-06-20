# Created by Amit

from django.contrib import admin
from django.urls import path
from socialspace import views

urlpatterns = [
    path("",views.home, name="home"),
    path('testing', views.testing, name='testing'),
    path('socialcontacts/', views.socialcontacts, name='socialcontact'),
    path('socialcontact/<slug:slug>', views.socialcontact_detail, name='socialcontact_details'),
    
]