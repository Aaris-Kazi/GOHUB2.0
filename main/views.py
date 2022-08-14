from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import hotel_details

# Create your views here

def index(request):
    try:
        loc = request.COOKIES['location_hotel']
        room = request.COOKIES['room_hotel']
    except Exception as e:
        loc = ''
        room = ''
    return render(request,'index.html', {'session_location':loc,'rooms':room})

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
            room = request.POST['rooms']
            request.session['location'] = loc
            request.session['rooms'] = room
            
            loc1 = request.session['location']
            room1 = request.session['rooms']
            s_date = request.POST['start_date']
            e_date = request.POST['end_date']
            locs = loc.lower()
            h = hotel_details.objects.filter(location = locs)
            # print(loc, len(h))
            pg = Paginator(h ,10)
            
            print(pg.num_pages)
            print(pg.count)
            print(pg.page_range)
            p1 =pg.page(1)
            print(p1)
            # print(p1.object_list)

            response = render(request,'search.html', {'rooms': h,'location':request.session['location'], 'room':request.session['rooms'], 'page': pg})
            response.set_cookie('location_hotel', loc1)
            response.set_cookie('room_hotel', room1)
            return response
        else:
            return redirect('home')
    else:
        return render(request,'search.html')

def search2(request):
    if request.method == 'POST':
        loc = request.POST['location']
        room = request.POST['rooms']
        request.session['location'] = loc
        request.session['rooms'] = room
        loc = loc.lower()
        h = hotel_details.objects.filter(location = loc)
        print(loc, len(h))
        pg = Paginator(h ,10)
        print(pg.num_pages)
        print(pg.page_range)
        response = render(request,'search.html', {'rooms': h,'location':request.session['location'], 'room':request.session['rooms'], 'page': pg})
        response.set_cookie('location_hotel', loc)
        response.set_cookie('room_hotel', room)
        return response
    else:
        return redirect('home')

def user_logout(request):
    try:
        del request.session['location']
        del request.session['rooms']
    except KeyError as e:
        pass
    logout(request)
    return redirect('home')
    # render(request,'search.html')