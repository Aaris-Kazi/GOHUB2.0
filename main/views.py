from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def search(request):
    return render(request,'search.html')

def logout(request):
    pass
    # render(request,'search.html')