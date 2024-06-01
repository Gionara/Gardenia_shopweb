#from django.conf.urls impor url

from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
]