"""ML_Butterfly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#from xml.etree.ElementInclude import include
from django.contrib import admin
# from django.conf.urls import url   # Add include to the imports here
from django.urls import path,include
from django.urls import re_path as url 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # tell django to read urls.py in example app
    url(r'^', include('LepidopteraAI.urls')),
    # url(r'^', include('classification.urls')),
    # url(r'^', include('segmentation.urls')),
    # url(r'^', include('object_detection.urls')),
   
]


