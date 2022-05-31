from django.contrib import admin

from weather_admin.models import Mailing, MyUser, Roles, Weather, City, Date

# Register your models here.

class WeatherAdmin(admin.ModelAdmin):
    # fieldsets = [('date',{'fields':['date']}), ('name',{'fields':['city_id']})]
    list_display = ('city', 'date', 'time')

# admin.site.register(Weather, WeatherAdmin)
admin.site.register(Weather, WeatherAdmin)
admin.site.register(City)
admin.site.register(Date)
admin.site.register(Roles)
admin.site.register(MyUser)
admin.site.register(Mailing)