from django.contrib import admin

from weather_admin.models import Weather
from weather_admin.models import City

# Register your models here.

admin.site.register(Weather)
admin.site.register(City)