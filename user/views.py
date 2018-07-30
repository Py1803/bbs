from django.shortcuts import render
from user.models import User
# Create your views here.
def register(request):
    return render(request,'register.html',{})

def login(request):
    return render(request,'login.html',{})

def logout(request):
    return render(request,'logout.html',{})

def user_info(request):
    return render(request,'user_info.html',{})


