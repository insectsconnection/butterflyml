
from django.contrib import admin
from . import views
from django.urls import path
from django.http import HttpResponse
# from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    # Notice the URL has been named
    path('', views.index, name='index'), 
    path(r'^classify/$', views.classify, name='classify'),
    path(r'^base/$', views.base, name='base'),
    path(r'^data/$', views.data, name='data'),
    path(r'^dashboard/$', views.dashboard, name='dashboard'),
    path(r'^butterfly/$', views.butterfly, name='butterfly'),
    path(r'^covnet/$', views.covnet, name='covnet'),
    path(r'^navbar/$', views.navbar, name='navbar'),
    path(r'^weather/$', views.weather, name='weather'),
    path(r'^main/$', views.main, name='main'),
    path(r'^result/$', views.result, name='result'),
    path(r'^resnet/$', views.restnet, name='restnet'),
    path(r'^objectmeasurement/$', views.objectmeasurement, name='objectmeasurement'),
    path(r'^objectidentifier/$', views.objectidentifier, name='objectidentifier'),
    path(r'^adddevice/$', views.adddevice, name='adddevice'), 
    path(r'^butterfly/$', views.butterfly, name='butterfly'),
    path(r'^camera/$', views.camera, name='camera'),
]

