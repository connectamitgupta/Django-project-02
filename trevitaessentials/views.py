from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.user.is_anonumous:
        return redirect('login')
    
    return HttpResponse("Hello, world. You're at the trevita essentials app index function")

def about(request):
    return HttpResponse("Hello, world. You're at the trevita essentials app for about us")

def contact(request):
    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")

def signup(request):
#    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    return render (request,'signup.html')

def signin(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    if request.method=="post":
        # Check whether valid user is trying to login app
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("dashboard.html")
            
        else:
            return render (request,'signin.html')
    
    return render (request,'signin.html')
  
def signout(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    logout(request)
    return redirect ('/signin')
  
def dashboard(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    return render (request,'dashboard.html')