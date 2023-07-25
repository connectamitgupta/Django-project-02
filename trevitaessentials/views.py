from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .models import social_contacts
from django.template import loader
from .forms import UploadFileForm
from .forms import DocumentForm
from django.conf import settings
from .models import Upload5
import csv


# Imaginary function to handle an uploaded file.
from .file_handle import handle_uploaded_file

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("signin")
    else:
        return redirect("dashboard")
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the trevita essentials app index function")


def about(request):
    return render(request, "about.html")

    # return HttpResponse("Hello, world. You're at the trevita essentials app for about us")


def contact(request):
    return render(request, "contact.html")

    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")


def signup(request):
    #    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")

    # print(request.method)
    if request.method == "POST":
        # Check whether valid user is trying to login app
        fname1=request.POST.get("firstname")
        lname1=request.POST.get("lastname")
        phone1=request.POST.get("phone")
        user1 = request.POST.get("username")
        pass1 = request.POST.get("password")
        print("Hello world")
        # user = authenticate(request, username=user1, password=pass1)
        if User.objects.filter(username__exact=user1):
            return render(request, "/signup.html")
        
        # if User is not None:
        #     # A backend authentication  the credentials
        #     login(request, User)
        #     # print(user)
        #     return redirect("dashboard")

        else:
            a=User(first_name=fname1,last_name=lname1,username=user1,password=pass1,is_staff=True)
            a.save()
            messages.success(request, "Signup created successfully")
            return render(request, "signin.html")

    return render(request, "signup.html")


def signin(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    print(request.method)
    if request.method == "POST":
        # Check whether valid user is trying to login app
        user1 = request.POST.get("username1")
        pass1 = request.POST.get("password1")
        print("Hello world")
        #  print(request.POST.get('username1'))
        #  print(request.POST.get('password1'))
        user = authenticate(request, username=user1, password=pass1)
        # print(user)
        if user is not None:
            # A backend authentication  the credentials
            login(request, user)
            # print(user)
            return redirect("dashboard")

        else:
            messages.success(request, "Incorrect credentials")
            return render(request, "signin.html")

    return render(request, "signin.html")


def signout(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    logout(request)
    messages.success(request, "You have signed out successfully")

    return redirect("/")


def dashboard(request):
    # return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")
    return render(request, "dashboard.html")


def home(request):
    if request.user.is_anonymous:
        param = {"utype": "guest"}
        return render(request, "home.html", param)
    else:
        param = {"utype": "registered"}
        return render(request, "home.html", param)
    return render(request, "home.html")
    # return HttpResponse("Hello, world. You're at the trevita essentials app index function")


def services(request):
    return render(request, "services.html")


# return HttpResponse("trevita servcies")


def products(request):
    return render(request, "products.html")

def socialcontacts(request):
    contact=social_contacts.objects.all().values
    template=loader.get_template('socialcontacts.html')
    # print(members)
    context = {
    'mymembers': contact,
               }
    return HttpResponse(template.render(context, request))

def socialcontactdetails(request,id):
    contact=social_contacts.objects.get(id=id)
    template=loader.get_template('socialcontacts_details.html')
    context = {
    'mymembers': contact,
               }
    return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('test_template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))


def upload_file_1(request):
    #    return HttpResponse("Hello, world. You're at the trevita essentials app for contact us")

    # print(request.method)
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["file"])
            # form.save()
            a=request.POST.get('firstname')
            b=request.POST.get('lastname')
            c=request.FILES['file'].name
            print(f"a: {a} and b : {b} and c: {c}")

            folder = request.path.replace("/", "_")
            uploaded_filename = request.FILES['file'].name
            
            messages.success(request, "Data received")
            return HttpResponseRedirect("/uploader_1")
        
        # print(UploadedFile.name)
    else:
        form = UploadFileForm()
    return render(request, "uploader_1.html", {"form": form})

def upload_file_2(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploader_2')
    else:
        form = DocumentForm()
    return render(request, 'uploader_2.html', {
        'form': form
    })


def upload_file_3(request):
    if request.method == "POST":
        print("Reuest handling.....")
        p=request.FILES['image']
        from .models import Upload3
        upload=Upload3(pic=p)
        upload.save()
    return render(request, 'uploader_3.html')

# Reference purpose     https://www.youtube.com/watch?v=rNrZStmeD7I


def upload_file_4(request):
    if request.method == "POST":
        print("Reuest handling.....")
        n=request.POST.get("fname")
        p=request.FILES['image']
        from .models import Upload4
        upload=Upload4(name=n, pic=p)
        upload.save()
    return render(request, 'uploader_4.html')


def upload_file_5(request):
    if request.method == "POST":
        print("Reuest handling.....")
        
        # if 'desc' in request.POST:
        #     d = request.POST.get('desc')
        # if 'image' in request.POST:
        #     p = request.FILES.get['image']

        d=request.POST.get("desc")
        p=request.FILES['image']
    # if file is not CSV  
        if not p.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("trevitaessentials:upload_csv"))

    #if file is too large, return
        if p.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (p.size/(1000*1000),))
            return HttpResponseRedirect(reverse("trevitaessentials:upload_csv"))

    # save file upload informtion in db
        from .models import Upload5
        upload=Upload5(description=d, pic=p)
        upload.save()
    # Reading file
        # upload5=Upload5       https://www.youtube.com/watch?v=t3BdM6JlAmY
        obj=Upload6.objects.get(id=rid)
        # contact=social_contacts.objects.all().values
        print(obj.description)
        print(obj.pic.path)
        # import csv

        with open(obj.pic.path) as csv_file:
            print("test")
            if csv_file.closed:
                print ('file is closed')
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            csvdata=[]
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    csvdata=row
                    line_count += 1
        print(f'Processed {line_count} lines.')

     
    return render(request, 'uploader_5.html')

def view_file_5(request):
    from .models import Upload5
    upload5=Upload5.objects.all()
    context = {
    'filesdata': upload5,
               }

    return render(request,"uploader_view5.html",context)



def upload_file_6(request):
    if request.method == "POST":
        print("Reuest handling.....")

        d=request.POST.get("desc")
        p=request.FILES['image']
    # if file is not CSV  
        if not p.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("trevitaessentials:upload_csv"))

    #if file is too large, return
        if p.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (p.size/(1000*1000),))
            return HttpResponseRedirect(reverse("trevitaessentials:upload_csv"))

    # save file upload informtion in db
        from .models import Upload6
        upload=Upload6(description=d, pic=p)
        # upload.save()
        # New way to save record so that we get just saved record id properly
        n = Upload6.objects.create(description=d, pic=p)
        rid=n.pk

    # Reading file
        # upload5=Upload5       https://www.youtube.com/watch?v=t3BdM6JlAmY
        obj=Upload6.objects.get(id=rid)
        # contact=social_contacts.objects.all().values
        print(obj.description)
        print(obj.pic.path)
        # import csv

        context = {}
        reader=csv.DictReader(str(request.FILES['image']))
        for row in reader:
            header = list(row.keys())
            break
        data = {}
        for row in reader:
            for i in header:
                values = []
                values.append(row.get(i))
                if i not in data:
                    data[i] = values
                data[i].extend(values)
        context['header'] = header
        context['data'] = data
        print(reader)
        return render(request, 'uploader_6.html', context)

    

     #https://gurusabarish.medium.com/display-the-uploaded-csv-file-in-django-template-199aa8711695
    return render(request, 'uploader_6.html')


def view_file_6(request):
    from .models import Upload6
    upload6=Upload6.objects.all()
    context = {
    'filesdata': upload6,
               }

    return render(request,"uploader_view6.html",context)