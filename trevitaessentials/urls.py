# Created by Amit
from django.contrib import admin
from django.urls import path
from trevitaessentials import views
from django.conf import settings                        # For Media file upload process
from django.conf.urls.static import static              # For Media file upload process
app_name = "trevitaessentials"


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
    path('uploader_1', views.upload_file_1, name='uploader1'),
    path('uploader_2', views.upload_file_2, name='uploader2'),
    path('uploader_3', views.upload_file_3, name='uploader3'),
    path('uploader_4', views.upload_file_4, name='uploader4'),
    path('uploader_5', views.upload_file_5, name='upload_csv'),
    path('view_5', views.view_file_5, name='view5'),
    path('uploader_6', views.upload_file_6, name='uploader6'),
    path('view_6', views.view_file_6, name='view6'),


    path('testing', views.testing, name='testing')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)