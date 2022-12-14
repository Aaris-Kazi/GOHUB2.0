from datetime import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from django.http import QueryDict

from .models import hotel_details, resultsnotfound, hotel_booking

from .forms import NewUserForm

# Create your views here

def removeAddtional(text):
    text = str(text).strip(']')
    text = text.strip('[')
    text = text.strip("'")
    return text

def index(request):
    try:
        loc = request.COOKIES['location_hotel']
        room = request.COOKIES['room_hotel']
    except Exception as e:
        loc = ''
        room = ''
    pgname = request.session['pagename'] =request.build_absolute_uri()
    
    if str(request.user) != 'AnonymousUser':
        HB = hotel_booking.objects.all()
        date = datetime.today()
        date = date.strftime("%Y-%m-%d")
        try:
            print(request.session['userid'])
            queryset = hotel_booking.objects.filter(userid = request.session['userid'], startday__gte = date)
            return render(request,'index.html', {'session_location':loc,'rooms':room, "results": queryset})
        except Exception:
            pass
        
    return render(request,'index.html', {'session_location':loc,'rooms':room})

def register(request):
    try:
        if request.method == 'POST':
            new = User.objects.filter(email=request.POST['email'])  
            if new.first() is not None: 
                raise ValidationError("Email Already Existed") 
            else:
                query_dict = QueryDict("", mutable=True)
                data = request.POST.copy()
                pwd1 = data.pop('password')
                pwd1 = removeAddtional(pwd1)
                query_dict.update(data)
                query_dict.update({'password': pwd1,'password1': pwd1, 'password2': pwd1})
                form = NewUserForm(query_dict)
                error = str(form).split('<ul class="errorlist"><li>')
                error = str(error[1]).split('</li>')
                if form.is_valid():
                    print("Registeration successful")
                    messages.add_message(request, messages.SUCCESS, 'Registeration successful')
                    form.save()
                else:
                    raise ValidationError(error[0])
                return redirect('log')
    except Exception as e:
        e = removeAddtional(e)
        messages.add_message(request, messages.ERROR, e)
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
    loc = loc.lower()
    room = request.session['rooms']
    request.session['sdate']
    request.session['edate']
    h = hotel_details.objects.filter(location = loc)
    # print(h)
    # print(len(h))
    # print(loc)
    # print(type(loc))
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