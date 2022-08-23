
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import hotel_details, resultsnotfound, hotel_booking

# Create your views here

def index(request):
    try:
        loc = request.COOKIES['location_hotel']
        room = request.COOKIES['room_hotel']
    except Exception as e:
        loc = ''
        room = ''
    pgname = request.session['pagename'] =request.build_absolute_uri()
    print(pgname)
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
        pgname = request.session['pagename']
        # request.session['userid'] = user.id
        print(pgname)
        uname = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=uname, password=pwd)
        # print(user)
        if user is not None:
            login(request, user)
            user = User.objects.filter(username=user)
            for i in user:
                request.session['userid'] = i.id
            
            if 'search' in pgname:
                print('True')
                
                return redirect(search3, '1')
            # if 'next' in request.POST:
            #     next = request.POST['next']
            #     print(next)
            #     return redirect(next)
            return redirect(pgname)
        else:
            messages.add_message(request, messages.ERROR, 'Login invalid please check username or passowrd')
            return render(request,'login.html')
    else:
        messages.add_message(request, messages.ERROR, '')
        pgname = request.session['pagename']
        print(pgname)
    return render(request,'login.html')

def search(request):
    if request.method == 'POST':
        request.session['pagename'] =request.build_absolute_uri()
        if request.POST['location']!= '':
            loc = request.POST['location']
            room = request.POST['rooms']
            request.session['location'] = loc
            request.session['rooms'] = room
            
            loc1 = request.session['location']
            room1 = request.session['rooms']
            s_date = request.POST['start_date']
            request.session['sdate'] = request.POST['start_date']
            e_date = request.POST['end_date']
            request.session['edate'] = request.POST['end_date']
            locs = loc.lower()
            h = hotel_details.objects.filter(location = locs)
            # print(loc, len(h))
            if len(h) == 0:
                res = resultsnotfound.objects.filter(location = loc)
                if len(res) == 0:
                    res = resultsnotfound()
                    res.location = loc
                    res.save()
            pg = Paginator(h ,10)
            
            # print(pg.num_pages)
            # print(pg.count)
            # print(pg.page_range)
            p1 =pg.page(1)
            # print(p1)
            # print(p1.object_list)

            response = render(request,'search.html', {'rooms': p1.object_list,'location':request.session['location'], 'room':request.session['rooms'], 'pages': pg})
            response.set_cookie('location_hotel', loc1)
            response.set_cookie('room_hotel', room1)
            return response
        else:
            return redirect('home')
    else:
        return render(request,'search.html')

def search2(request):
    if request.method == 'POST':
        request.session['pagename'] =request.build_absolute_uri()
        loc = request.POST['location']
        room = request.POST['rooms']
        request.session['location'] = loc
        request.session['rooms'] = room
        request.session['sdate']
        request.session['edate']
        loc = loc.lower()
        h = hotel_details.objects.filter(location = loc)
        if len(h) == 0:
            print('result not found')
            res = resultsnotfound.objects.filter(location = loc)
            if len(res) == 0:
                res = resultsnotfound()
                res.location = loc
                res.save()
        print(loc, len(h))
        pg = Paginator(h ,10)
        p1 = pg.page(1)
        response = render(request,'search.html', {'rooms': p1.object_list,'location':request.session['location'], 'room':request.session['rooms'], 'pages': pg})
        response.set_cookie('location_hotel', loc)
        response.set_cookie('room_hotel', room)
        return response
    else:
        return redirect('home')

def search3(request, pagenumber):
    request.session['pagename'] =request.build_absolute_uri()
    print(pagenumber)
    loc = request.session['location']
    room = request.session['rooms']
    request.session['sdate']
    request.session['edate']
    print(loc)
    h = hotel_details.objects.filter(location = loc)
    pg = Paginator(h ,10)
    p1 =pg.page(pagenumber)
    # print(p1.object_list)
    response = render(request,'search.html', {'rooms': p1.object_list,'location':request.session['location'], 'room':request.session['rooms'], 'pages': pg})
    response.set_cookie('location_hotel', loc)
    response.set_cookie('room_hotel', room)
    return response

def user_logout(request):
    try:
        del request.session['location']
        del request.session['rooms']
    except KeyError as e:
        pass
    logout(request)
    return redirect('home')


@login_required(login_url='/login')
def booking(request, userid, hotelid, location):
    pgname = request.session['pagename']
    try:
        hb = hotel_booking()
        hd = hotel_details.objects.get(pk = hotelid)
        if userid == None:
            userid = request.session['userid']
        sday = request.session['sdate']
        eday = request.session['edate']
        
        hb.userid = request.user
        hb.hotelid = hd
        hb.location = location
        hb.startday = sday
        hb.endday = eday
        sday, eday = datetime.strptime(sday,"%Y-%m-%d"), datetime.strptime(eday,"%Y-%m-%d")
        delta = eday-sday
        delta = delta.days
        price = delta * hd.price
        hb.price = price
        hb.save()
        return redirect('home')
    except Exception as e:
        print(e)
        return redirect(pgname)
    print(userid, hotelid, location, sday, eday)