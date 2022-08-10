from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    u = User()
    u.username
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')

def search(request):
    return render(request,'search.html')

def user_logout(request):
    logout(request)
    return redirect('home')
    # render(request,'search.html')