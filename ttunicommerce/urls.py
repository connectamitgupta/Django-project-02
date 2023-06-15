from django.contrib import admin
from django.urls import path
from ttunicommerce import views

urlpatterns = [
    path("ttunicommerce/",views.index, name="index")
]
