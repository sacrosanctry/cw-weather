from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from weather_admin.models import Weather, City, Date
from django.http import JsonResponse

# Create your views here.

def home_view(request, *args, **kwargs):

    cities = City.objects.all()
    dates = Date.objects.all()
    all_weather = Weather.objects.all()

    # city_id = City.objects.filter(*args, **kwargs, name='Kyiv').first()
    # temperature = Weather.objects.filter(city_id=city_id) #! Weather.city_id=city_id
    # weather = Weather.objects.filter(id=1) # get a list of objects who have a given id

    
    if request.method == 'GET':    # form>select in home.html # POST method is used to transfer data from client to server in HTTP
        city_name = request.GET.getlist('city')[0] # gets the first (0) element of list
        # city_name = request.POST.get('city')
        # city_name = City.objects.filter(city_name=city_name)
        print(city_name) # print в терминале

    # if place != None: 
        place = City.objects.get(name=city_name)
        city_id = place.id
        print(city_id)

        try: # ! сделать иф для проверки пустого города без погоды
            weather_in_city = Weather.objects.get(city=city_id)
        except Weather.DoesNotExist:
            weather_in_city = None

    
    #place = City.objects.get(name=city_name) #! можно убрать


 
        date_name = request.GET.getlist('date')[0] # gets the first (0) element of list
        print(date_name)

        # date = Date.objects.get(name=date_name)
    
    else:
        weather_in_city = None
        city_id = None
        place = None

    context = {
        'object': weather_in_city,
        'city': city_id,
        'cities': cities,
        'dates': dates,
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
