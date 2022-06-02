from django.shortcuts import render

from django.contrib.auth.models import User #, values_list
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from weather_admin.models import Weather, City, Date
from django.http import JsonResponse
from datetime import datetime
from django.utils.formats import get_format

# from django.import log

# Create your views here.



def parse_date(date_str):
    """Parse date from string by DATE_INPUT_FORMATS of current language"""
    for item in get_format('DATE_INPUT_FORMATS'):
        try:
            return datetime.strptime(date_str, item).date()
        except (ValueError, TypeError):
            continue

    return None



def home_view(request, *args, **kwargs):

    class ListAsQuerySet(list):

        def init(self, *args, model, **kwargs):
            self.model = model
            super().init(*args, **kwargs)

        def filter(self, *args, **kwargs):
            return self  # filter ignoring, but you can impl custom filter

        def order_by(self, *args, **kwargs):
            return self


    cities = City.objects.all() # query set
    dates = Date.objects.all()
    all_weather = Weather.objects.all()

    # city_id = City.objects.filter(name='Kyiv').first()
    # temperature = Weather.objects.filter(city_id=city_id) #! Weather.city_id=city_id
    # weather = Weather.objects.filter(id=1) # get a list of objects who have a given id

    # city_name = request.POST.get('city') # gets the first (0) element of list
    # # city_name = request.POST.get('city')
    # # city_name = City.objects.filter(city_name=city_name)
    # print(city_name) # print в терминале



    if request.method == 'POST': # form>select in home.html # POST method is used to transfer data from client to server in HTTP

        alldata = request.POST
        city_name = alldata.get("city", "0") # string item
        date_name = alldata.get("date", "0")
        print(city_name)


        new_dates_list = []

        dates_list = list(dates) # convert query set to list

        parsed_date = parse_date(date_name)
        query_date = Date.objects.get(date=parsed_date)

        n = 0
        for i in dates:
            n += 1
            if i == query_date:
                new_dates_list = Date.objects.all()[n:(n+7)] # dates_list[dates_list.index(i):(dates_list.index(i)+6)]


        # dates_queryset7 = ListAsQuerySet(new_dates_list, model=Date)


        if city_name != '0' and date_name != 'Date': # one of select options (city/date) is not chosen

            place = City.objects.get(name=city_name)
            city_id = place.id
            print(city_id)

            try: 
                weather_in_city = Weather.objects.get(id=2) #!!!!!!!WRONG ID!=2 problems with date (foreiggn field does not have date field)
            except Weather.DoesNotExist:
                weather_in_city = None

        else:
            weather_in_city = None
            city_id = None
            place = None   

    else:
        weather_in_city = None
        city_id = None
        place = None   



        # date_name = request.POST.getlist('date')[0] # gets the first (0) element of list
        # print(date_name)

        # date = Date.objects.get(date=date_name)

    
              

    context = {
        'object': weather_in_city,
        'city': city_id,
        'cities': cities,
        'dates': dates,
        'new_dates_list': new_dates_list,
        'place': place,
    }
    return render(request, "home.html", context)
    # "home.html" - template name, {} - context ({} - empty dictionary)


def newadmin_view(request, *args, **kwargs):
    return render(request, "newadmin.html", {})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2:
            
            User.objects.create_user(username, email, password)
            messages.success(request, 'Account created successfully')
            return redirect(reverse('home'))
            
    return render(request, 'register.html', {})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')    

    return render(request, 'login.html', {})
