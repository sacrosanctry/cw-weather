from django.shortcuts import render

from django.contrib.auth.models import User #, values_list
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from weather_admin.models import Weather, City, Date
from datetime import datetime
from django.utils.formats import get_format

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

    cities = City.objects.all() # query set
    dates = Date.objects.all()
    all_weather = Weather.objects.all()

    # city_id = City.objects.filter(name='Kyiv').first()
    # temperature = Weather.objects.filter(city_id=city_id) #! Weather.city_id=city_id
    # weather = Weather.objects.filter(id=1) # get a list of objects who have a given id

    # city_name = request.POST.get('city') # gets the first (0) element of list
    # # city_name = request.POST.get('city')
    # # city_name = City.objects.filter(city_name=city_name)
    # print(city_name)

    # date_name = request.POST.getlist('date')[0]

    if request.method == 'POST': # form>select in home.html # POST method is used to transfer data from client to server in HTTP

        alldata = request.POST
        city_name = alldata.get("city", "0") # string item
        date_name = alldata.get("date", "0")
        print(city_name)

        if city_name != '0' and date_name != 'Date': # one of select options (city/date) is not chosen

            dates_list = list(dates) # convert query set to list

            parsed_date = parse_date(date_name)
            query_date = Date.objects.get(date=parsed_date)

            new_dates_list = []
            n = 0
            for i in dates:
                n += 1
                if i == query_date:
                    new_dates_list = Date.objects.all()[n:(n+7)] # dates_list[dates_list.index(i):(dates_list.index(i)+6)]

            place = City.objects.get(name=city_name)
            city_id = place.id
            print(city_id)

            
            # people = People.objects.order_by(name).filter(age__gt=65) # unevaluated
            # people.query.set_limits(start, stop)  # still unevaluated
            # for person in people:  # now its evaluated
            #     person.do_the_thing()


            filtered_allweather = all_weather.order_by('date').filter(city__name=city_name)

            # ids = filtered_allweather.values_list('id', flat=True) # Cannot resolve keyword 'i' into field. Choices are: city, city_id, date, date_id, id, temperature, time, weather
            chosen_date_id = filtered_allweather.get(date=query_date).id #! gets id from the first query set, not from filtered_allweather
            # user = User.objects.get(username='Fokoa')
            # user.id
            # chosen_date_id = 2
            done_weather = filtered_allweather.query.set_limits(low=chosen_date_id-1, high=chosen_date_id+6) #! low=chosen_date_id, high=chosen_date_id+7




            # new_dates_list.filter('query_date')[:7] # error Cannot filter a query once a slice has been taken.

            weather_in_city_list = []
            # for j, k in zip(new_dates_list, range(len(new_dates_list))):
            #     date_name2 = new_dates_list.get("date", "k")
            #     parsed_date2 = parse_date(date_name2)
            #     weather_in_city = Weather.objects.get(date__date=parsed_date2)
            #     weather_in_city_list.append(weather_in_city)
            
            not_chosen_error = False    

        else:
            not_chosen_error = True
            weather_in_city = None
            weather_in_city_list = None
            filtered_allweather = None
            city_id = None
            place = None
            new_dates_list = None   

    else:
        not_chosen_error = False
        weather_in_city = None
        weather_in_city_list = None
        filtered_allweather = None
        city_id = None
        place = None
        new_dates_list = None   


    context = {
        # 'object1': weather_in_city,
        # 'weather_in_city_list': weather_in_city_list,
        'city': city_id,
        'cities': cities,
        'dates': dates,
        'place': place,
        'new_dates_list': new_dates_list,
        'not_chosen_error': not_chosen_error,
        'filtered_allweather': filtered_allweather,
        'done_weather': done_weather
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
