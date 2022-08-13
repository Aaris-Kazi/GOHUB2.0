from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import hotel_details

# Create your views here

def index(request):
    return render(request,'index.html')

def register(request):
    try:
        if request.method == 'POST':
            new = User.objects.filter(email=request.POST['email'])  
            if new.count():  
                raise ValidationError("Email Already Existed") 
            u = User()
            u.username = request.POST['username']
            u.email  = request.POST['email']
            u.password = request.POST['pwd']
            u.save()
            u = User.objects.get(username = request.POST['username'])
            u.set_password(request.POST['pwd'])
            u.save()
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
            return redirect('log')
    except Exception as e:
        e = str(e).strip("[")
        e = str(e).strip("]")
        e = str(e).strip("'")
        messages.add_message(request, messages.ERROR, e)
        print(e)
    
    return render(request,'register.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=uname, password=pwd)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
            # HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.add_message(request, messages.ERROR, 'Login invalid please check username or passowrd')
            return render(request,'login.html')
    else:
        messages.add_message(request, messages.ERROR, '')
    return render(request,'login.html')

def search(request):
    if request.method == 'POST':
        if request.POST['location']!= '':
            loc = request.POST['location']
            request.session['location'] = loc
            s_date = request.POST['start_date']
            e_date = request.POST['end_date']
            room = request.POST['rooms']
            request.session['rooms'] = room
            locs = loc.lower()
            h = hotel_details.objects.filter(location = locs)
            print(loc, len(h))
            pg = Paginator(h ,2)
            print(pg.num_pages)
            return render(request,'search.html', {'rooms': h,'location':request.session['location'], 'room':request.session['rooms']})
        else:
            return redirect('home')
    else:
        return render(request,'search.html')
def search2(request):
    if request.method == 'POST':
        loc = request.POST['location']
        room = request.POST['rooms']
        loc = loc.lower()
        h = hotel_details.objects.filter(location = loc)
        print(loc, len(h))
        pg = Paginator(h ,2)
        print(pg.num_pages)
        print(pg.page_range)
        return render(request,'search.html', {'rooms': h})
    else:
        return redirect('home')
    return render(request,'search.html')

def user_logout(request):
    try:
        del request.session['location']
        del request.session['rooms']
    except KeyError:
        pass
    logout(request)
    return redirect('home')
    # render(request,'search.html')