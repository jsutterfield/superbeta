import requests

API_KEY = "5b3a5aef22952102"

def get_forecast(lat=None, lon=None, city=None, state=None, zipcode=None):
    query = None
    if lat and lon: 
        query = "{0},{1}".format(lat, lon) 
    elif city and state:
        query = "{0}/{1}".format(state, "_".join(city.split()))
    elif zipcode: 
        query = zipcode

    if not query: 
        return

    fp = requests.get("http://api.wunderground.com/api/{0}/conditions/forecast/q/{1}.json".format(API_KEY, query))

    # Check if this request goes through before converiting it to json
    # Also set a timeout

    json = fp.json()
    weather = {'today': {'temp': None, 'icon': None, 'day': None},
               'tomorrow': {'temp': None, 'icon': None, 'day': None},
               'twodays': {'temp': None, 'icon': None, 'day': None}}
    try: 
        weather['today']['temp'] = json["current_observation"]["temp_f"]
    except KeyError:
        return None
    weather['today']['icon'] = json["current_observation"]["icon"]
    weather['today']['day'] = json['forecast']['simpleforecast']['forecastday'][0]['date']['weekday_short']
    weather['tomorrow']['temp'] = json['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit']
    weather['tomorrow']['icon'] = json['forecast']['simpleforecast']['forecastday'][1]['icon']
    weather['tomorrow']['day'] = json['forecast']['simpleforecast']['forecastday'][1]['date']['weekday_short']
    weather['twodays']['temp'] = json['forecast']['simpleforecast']['forecastday'][2]['high']['fahrenheit']
    weather['twodays']['icon'] = json['forecast']['simpleforecast']['forecastday'][2]['icon']
    weather['twodays']['day'] = json['forecast']['simpleforecast']['forecastday'][2]['date']['weekday_short']
 
    return weather
