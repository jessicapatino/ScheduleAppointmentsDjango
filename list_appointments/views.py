from django.http import request
from django.shortcuts import redirect, render
from list_appointments.models import RolesUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm


# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html',{})

def login_view(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        user= authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error': 'username or password incorrect'})
    return render(request,'login.html', {})

@login_required
def list_patients(request):
    users =User.objects.all()
    roles_users = RolesUser.objects.all()
    for rol_user in roles_users:
        return render(request, 'list_appointments/list.html',{'roles_users': roles_users})

@login_required
def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message ="Image uploaded succesfully!"

        else:
            form = UploadImageForm()

        return render('index.html', locals(), context_instance=RequestContext(request))


def home_view(request):
    return render('base.html')