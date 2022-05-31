from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    id   = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30) # max_length = required

    def __str__(self):
        return self.name


class Weather(models.Model):
    class Time(models.IntegerChoices):
        DAY = 1
        NIGHT = 2
    id          = models.AutoField(primary_key=True, unique=True)
    city        = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True)
    date        = models.ForeignKey('Date', on_delete=models.CASCADE, blank=True, null=True)
    time        = models.IntegerField(choices=Time.choices)
    temperature = models.IntegerField(blank=True, null=True)
    weather     = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.city} {self.date}"


class Date(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return f"{self.date}"


class Roles(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)

class MyUser(User):
    name = models.CharField(max_length=40)
    roles = models.ManyToManyField('Roles', blank=True, null=True)

class Mailing(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.OneToOneField('MyUser', on_delete=models.CASCADE, blank=True, null=True)

# понять как привязать сити и тайм к зарег юзеру

# class RoleUser(models.Model):
#     user_id = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     role_id = models.ForeignKey('Roles', on_delete=models.CASCADE, blank=True, null=True)
