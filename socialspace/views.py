from django.shortcuts import render, HttpResponse, loader
from .models import social_contact

# Create your views here.
def home(request):
  
    template = loader.get_template('main.html')
    return HttpResponse(template.render())    # return HttpResponse("Hello, world. You're at the social app home page")


def testing(request):
    
    return HttpResponse("Hello, world. You're at testing app home page")


def socialcontacts(request):
  contactdata = social_contact.objects.all().values()
  template = loader.get_template('socialcontacts.html')
  context = {
    'Contactdata': contactdata,
  }
  return HttpResponse(template.render(context, request))

def socialcontact_detail(request, slug):
  contactdata = social_contact.objects.get(slug=slug)
  print(contactdata)
  g=contactdata.social_groups.all()             ## for taking many to many relation data
  print(g)
  template = loader.get_template('socialcontact_details.html')
  context = {
        'Contactdata': contactdata,'groupinfo': g
  }
  return HttpResponse(template.render(context, request))