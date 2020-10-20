from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    if request.method == 'POST':
        user=User()
        form = request.POST
        if form.get('name')!='' and form.get('branch') != 'Choose...' and form.get('email')!='' and form.get('hostel') != 'Choose...' and form.get('password')!='':
            try:
                user = User.objects.get(email=form.get('email'))
                return render(request,'index/index.html',{'error':2})
            except ObjectDoesNotExist:
                user.name= form.get('name')
                user.branch = form.get('branch')
                user.email = form.get('email')
                user.hostel = form.get('hostel')
                user.password = form.get('password')
                user.save()
                return render(request,'authentication/home.html',{'error':0})

        else:
            return render(request,'authentication/home.html',{'error':1})
    else:
        return render(request,'authentication/home.html',{'error':0})     
