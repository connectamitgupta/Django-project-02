# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.template import loader



# Create your views here.


def index(request):
   return render(request, "start.html")
    # return HttpResponse("Hello, world. You're at the trevita essentials app index function")


def products(request):
   return render(request, "products.html")
    # return HttpResponse("Hello, world. You're at the trevita essentials app index function")

def smanalytics(request):
   return render(request, "smanalytics.html")
    # return HttpResponse("Hello, world. You're at the trevita essentials app index function")



# def about(request):
#     return render(request, "about.html")

#     # return HttpResponse("Hello, world. You're at the trevita essentials app for about us")


# def contact(request):
#     return render(request, "contact.html")

#     # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")


# def signup(request):
#     #    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")

#     # print(request.method)
#     if request.method == "POST":
#         # Check whether valid user is trying to login app
#         fname1=request.POST.get("firstname")
#         lname1=request.POST.get("lastname")
#         phone1=request.POST.get("phone")
#         user1 = request.POST.get("username")
#         pass1 = request.POST.get("password")
#         print("Hello world")
#         # user = authenticate(request, username=user1, password=pass1)
#         if User.objects.filter(username__exact=user1):
#             return render(request, "/signup.html")
        
#         # if User is not None:
#         #     # A backend authentication  the credentials
#         #     login(request, User)
#         #     # print(user)
#         #     return redirect("dashboard")

#         else:
#             a=User(first_name=fname1,last_name=lname1,username=user1,password=pass1,is_staff=True)
#             a.save()
#             messages.success(request, "Signup created successfully")
#             return render(request, "signin.html")

#     return render(request, "signup.html")


# def signin(request):
#     # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
#     print(request.method)
#     if request.method == "POST":
#         # Check whether valid user is trying to login app
#         user1 = request.POST.get("username1")
#         pass1 = request.POST.get("password1")
#         print("Hello world")
#         #  print(request.POST.get('username1'))
#         #  print(request.POST.get('password1'))
#         user = authenticate(request, username=user1, password=pass1)
#         # print(user)
#         if user is not None:
#             # A backend authentication  the credentials
#             login(request, user)
#             # print(user)
#             return redirect("dashboard")

#         else:
#             messages.success(request, "Incorrect credentials")
#             return render(request, "signin.html")

#     return render(request, "signin.html")


# def signout(request):
#     # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
#     logout(request)
#     messages.success(request, "You have signed out successfully")

#     return redirect("/")


# def dashboard(request):
#     # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
#     return render(request, "dashboard.html")


# def home(request):
#     if request.user.is_anonymous:
#         param = {"utype": "guest"}
#         return render(request, "home.html", param)
#     else:
#         param = {"utype": "registered"}
#         return render(request, "home.html", param)
#     return render(request, "home.html")
#     # return HttpResponse("Hello, world. You're at the trevita essentials app index function")


# def services(request):
#     return render(request, "services.html")


# # return HttpResponse("trevita servcies")


# def products(request):
#     return render(request, "products.html")

# def socialcontacts(request):
#     contact=social_contacts.objects.all().values
#     template=loader.get_template('socialcontacts.html')
#     # print(members)
#     context = {
#     'mymembers': contact,
#                }
#     return HttpResponse(template.render(context, request))

# def socialcontactdetails(request,id):
#     contact=social_contacts.objects.get(id=id)
#     template=loader.get_template('socialcontacts_details.html')
#     context = {
#     'mymembers': contact,
#                }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#   template = loader.get_template('test_template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))