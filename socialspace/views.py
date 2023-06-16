from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  
    return HttpResponse("Hello, world. You're at the social app home page")


def testing(request):
    
    return HttpResponse("Hello, world. You're at testing app home page")
