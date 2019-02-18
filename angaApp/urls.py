from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.index, name='landingpage'), #Path to the index view
]
