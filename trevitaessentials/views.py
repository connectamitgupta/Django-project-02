from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('signin')
    else:
        return redirect('dashboard')
    return render(request,"index.html") 
    #return HttpResponse("Hello, world. You're at the trevita essentials app index function")

def about(request):
    return HttpResponse("Hello, world. You're at the trevita essentials app for about us")

def contact(request):
    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")

def signup(request):
#    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    
    
    return render (request,'signup.html')

def signin(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    print(request.method)
    if request.method=="POST":
        # Check whether valid user is trying to login app
        user1=request.POST.get('username1')
        pass1=request.POST.get('password1')
        print("Hello world")
      #  print(request.POST.get('username1'))
      #  print(request.POST.get('password1'))
        user = authenticate(request,username=user1, password=pass1)
        # print(user)
        if user is not None:
            # A backend authentication  the credentials
            login(request,user)
            # print(user)
            return redirect("/")
            
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