import os
import urllib.request
import json
from datetime import datetime

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '38242bd663c6c66cf929f3d00a342b7e'
last_result = None
last_ts = None
is_up = False

def fetch_weather(location=None):
    global is_up, last_result, last_ts
    
    if location is None:
        location = "Melbourne,Victoria,Australia"
    
    if API_KEY is None:
        print("OpenWeatherMap API key not specified")
        return None
    
    url = f"{BASE_URL}?q={location}&units=metric&appid={API_KEY}"
    
    try:
        response = urllib.request.urlopen(url).read()
        src = json.loads(response)
        
        # Simple validation
        if "main" not in src:
            is_up = False
            return None
        
        result = {
            'location': {
                'name': src['name'],
                'country': src['sys']['country'],
                'lat': src['coord']['lat'],
                'lon': src['coord']['lon'],
            },
            'temperature': src['main']['temp'],
            'humidity': src['main']['humidity'],
            'wind': {
                'speed': float(src['wind']['speed']) * 3.6,
                'deg': src['wind']['deg']
            },
            'cloud': src['clouds']['all'],
            'pressure': src['main']['pressure'],
        }
        
        last_result = result
        last_ts = datetime.now()
        is_up = True
        return result
    
    except Exception as e:
        print(f"Error fetching weather: {e}")
        is_up = False
        return None
