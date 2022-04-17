from django.shortcuts import render

from weather_admin.models import Weather
from weather_admin.models import City

# Create your views here.

def home_view(request, *args, **kwargs):

    # obj = Weather.objects.get(id=1)
    

    cities = City.objects.all()

    # city_id = City.objects.filter(*args, **kwargs, name='Kyiv').first()
    # temperature = Weather.objects.filter(city_id=city_id) #! Weather.city_id=city_id
    # weather = Weather.objects.filter(id=1) # get a list of objects who have a given id

    if request.method == 'POST':    # form>select in home.html
        city_name = request.POST.getlist('city')[0] # gets the first (0) element of list
        print(city_name)

    
    # if place != None:

        place = City.objects.get(name=city_name)
        city_id = place.id
        print(city_id) 

        weather_in_city = Weather.objects.get(id=city_id)

    else:
        weather_in_city = 0
        city_id = 0
        place = 0


    #place = City.objects.get(name=city_name)

    context = {
        'object': weather_in_city,
        'weather_in_city': weather_in_city,
        'city_id': city_id,
        'place': place,
        'cities': cities,
    }
    return render(request, "home.html", context)
    # "home.html" - template name, {} - context ({} - empty dictionary)


def newadmin_view(request, *args, **kwargs):
    return render(request, "newadmin.html", {})