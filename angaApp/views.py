from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    cities = City.objects.all() #returns all cities in the database
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0670d657e3a550164aee16950a8e1114'
    
    if request.method == 'POST':  # only true if form is submitted
        # add actual request data to form for processing
        form = CityForm(request.POST)
        form.save()  # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:
        # Requesting the API data and converting the JSON into Python objects
        city_weather = requests.get(url.format(city)).json()
        weather = {

        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'index.html', context) #Returns the index.html template

