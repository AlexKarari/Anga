from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0670d657e3a550164aee16950a8e1114'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #Requesting the API data and converting the JSON into Python objects
    weather = {

        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather':weather}

    return render(request, 'index.html', context) #Returns the index.html template

