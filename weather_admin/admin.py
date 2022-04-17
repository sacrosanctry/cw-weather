from django.contrib import admin

from weather_admin.models import Weather
from weather_admin.models import City

# Register your models here.

class WeatherAdmin(admin.ModelAdmin):
    # fieldsets = [('date',{'fields':['date']}), ('name',{'fields':['city_id']})]

    list_display = ('city_id', 'date', 'time')

admin.site.register(Weather, WeatherAdmin)
admin.site.register(City)