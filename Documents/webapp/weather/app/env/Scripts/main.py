import os
from flask import Flask, request, jsonify
from weather_service import openWeatherMap
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {name}!'

@app.route('/weather')
def getWeather():
    """ Weather web service """
    location = request.args.get("location", None)
    return lookupWeather(location)

def lookupWeather(location):
    ''' Perform the lookup of weather information across our two services '''
    weather = openWeatherMap.fetch_weather(location)
    if not openWeatherMap.is_up:
        weather = openWeatherMap.fetch_weather(location)
        if not openWeatherMap.is_up:
            if openWeatherMap.last_ts is None:
                weather = None
            else:
                if openWeatherMap.last_ts is None:
                    weather = openWeatherMap.last_result
                else:
                    #Get the latest cached
                    if openWeatherMap.last_ts > openWeatherMap.last_ts:
                        weather = openWeatherMap.last_result
                    else:
                        weather = openWeatherMap.last_result  
    if weather is None: 
        weather = {'status':'Offline'}
    return weather

def main():
    hostname = os.getenv('FLASK_HOST', '127.0.0.1')
    print(f"Running on {hostname}")
    app.run(host=hostname)

if __name__ == '__main__':
    main()




# import os
# from flask import Flask, request
# from weather_service.openWeatherMap import fetch_weather

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {name}!'

# @app.route('/weather')
# def getWeather():
#     """ Weather web service """
#     location = request.args.get("location", None)
#     return lookupWeather(location)

# def lookupWeather(location):
#     ''' Perform the lookup of weather information across our two services '''
#     weather = weatherStack.fetch_weather(location)
#     if not weatherStack.is_up:
#         weather = openWeatherMap.fetch_weather(location)
#         if not openWeatherMap.is_up:
#             if weatherStack.last_ts is None:
#                 weather = None
#             else:
#                 if openWeatherMap.last_ts is None:
#                     weather = weatherStack.last_result
#                 else:
#                     #Get the latest cached
#                     if openWeatherMap.last_ts > weatherStack.last_ts:
#                         weather = openWeatherMap.last_result
#                     else:
#                         weather = weatherStack.last_result  
#     if weather is None: 
#         weather = {'status':'Offline'}
#     return weather

# def main():
#     hostname = os.getenv('FLASK_HOST', '127.0.0.1')
#     print(f"Running on {hostname}")
#     app.run(host=hostname)

# if __name__ == '__main__':
#     main()

# from flask import Flask, render_template, request 
  
# import json to load JSON data to a python dictionary 
# import json 
  
# urllib.request to make a request to api 
# import urllib.request 
  
  
# app = Flask(__name__) 
  
# @app.route('/', methods =['POST', 'GET']) 
# def weather(): 
#     if request.method == 'POST': 
#         city = request.form['city'] 
#     else: 
#         for default name mathura 
#         city = 'mathura'
  
#     your API key will come here 
#     api = '38242bd663c6c66cf929f3d00a342b7e' 
  
#     source contain json data from api 
#     source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid =' + api).read() 
  
#     converting JSON data to a dictionary 
#     list_of_data = json.loads(source) 
  
#     data for variable list_of_data 
#     data = { 
#         "country_code": str(list_of_data['sys']['country']), 
#         "coordinate": str(list_of_data['coord']['lon']) + ' ' 
#                     + str(list_of_data['coord']['lat']), 
#         "temp": str(list_of_data['main']['temp']) + 'k', 
#         "pressure": str(list_of_data['main']['pressure']), 
#         "humidity": str(list_of_data['main']['humidity']), 
#     } 
#     print(data) 
#     return render_template('index.html', data = data) 
  
  
  
# if __name__ == '__main__': 
#     app.run(debug = True) 