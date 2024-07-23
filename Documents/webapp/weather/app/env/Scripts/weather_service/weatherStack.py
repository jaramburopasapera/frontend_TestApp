'''' Functions to interact with the OpenWeatherMap service to get the weather'''
import os
import urllib.request
import json
from datetime import datetime
BASE_URL = 'http://api.weatherstack.com/current?access_key='
last_result = None
last_ts = None
is_up = False
def fetch_weather(location=None):
    """Perform the retrieval of the weather - default location is Melbourne, AUS"""
    global is_up, last_result, last_ts
    if location is None: 
        location = "Melbourne,Victoria,Australia"
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if api_key is None:
        print("OpenWeatherMap API key not specified")
        return None
url = BASE_URL + location + '&units=metric&appid=' + api_key
    response = urllib.request.urlopen(url).read() 
    src = json.loads(response) 
    #Some simple validation
    if not "main" in src:
        is_up = False
        return None
    result = {
        'location': {
            'name': src['name'],
            'country' : src['sys']['country'],
            'lat': src['coord']['lat'],
            'lon': src['coord']['lon'],
            },
        'temperature' : src['main']['temp'],
        'humidity': src['main']['humidity'],
        'wind' : {
            'speed' : float(src['wind']['speed']) * 3.6,
            'deg' : src['wind']['deg'] 
        },
        'cloud' : src['clouds']['all'],
        'pressure' : src['main']['pressure'],
    }
    last_result = result
    last_ts = datetime.now()
    return result