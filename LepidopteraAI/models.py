
import email
import random
import json
from tkinter import CASCADE
from turtle import ondrag
from datetime import datetime
from django.utils import timezone
from django.forms import DateTimeField
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=10)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Hostplant(models.Model):
    hostplant = (
        (1,'Soursop'), 
        (2,'Aristolochia tagala'), 
        (3,'Pachliopta kotzebuea'),
        )
    make_forage = models.CharField(max_length=20, choices=hostplant,default=random,)

class Lepidoptera(models.Model):
    lepidoptera = (
        (1,'Papilio Lowi'),
        (2,'Papilio Demoleus'),
        (3,'Papilio Palinurus'),
        (4,'Papilio Polytes'),
        (5,'Papilio Rumanzovia'),
    )

    scientific_subspecies_name = models.CharField(
        max_length=30, choices=lepidoptera, default=random,)
    local_name = models.CharField(max_length=30)
    english_name = models.CharField(max_length=30)
    discovered_by = models.CharField(max_length=30)
    family = models. CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateField("Date", auto_now_add=True)
    date_added = models.DateTimeField(
        default=timezone.localtime, blank=True, null=True)
    text = models.TextField()


def __str__(self):
    return self.id + " " + self.scientific_subspecies_name


class EventPhoto(models.Model):
    event_id = models.ForeignKey(Lepidoptera, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='news/')


class temperature(models.Model):
    country_code = models.CharField(max_length=30)
    coordinate = models.CharField(max_length=30)
    temp = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
