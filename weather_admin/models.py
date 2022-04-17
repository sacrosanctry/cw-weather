from django.db import models

# Create your models here.

class City(models.Model):
    id   = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30) # max_length = required


class Weather(models.Model):
    class Time(models.IntegerChoices):
        DAY = 1
        NIGHT = 2
    id          = models.AutoField(primary_key=True, unique=True)
    city_id     = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True)
    date        = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    time        = models.IntegerField(choices=Time.choices)
    temperature = models.IntegerField(blank=True, null=True)
    weather     = models.TextField(blank=True, null=True)
    
