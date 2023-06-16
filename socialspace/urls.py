# Created by Amit

from django.contrib import admin
from django.urls import path
from socialspace import views

urlpatterns = [
    path("",views.home, name="home"),
    path('testing', views.testing, name='testing')
    
]