from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    try:
        if request.method == 'POST':
            u = User()
            u.username = request.POST['username']
            u.email  = request.POST['email']
            u.password = request.POST['pwd']
            u.save()
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
    except Exception as e:
        messages.add_message(request, messages.ERROR, 'A issue occur during registering'+e)
        print(e)
    
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')

def search(request):
    return render(request,'search.html')

def user_logout(request):
    logout(request)
    return redirect('home')
    # render(request,'search.html')