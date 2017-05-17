from urllib.request import urlopen
import json
import codecs
from sound import *

weather_dict = ['Clear', 'Light Drizzle', 'Heavy Drizzle', 'Light Rain', 'Heavy Rain', 'Light Rain Showers', 'Heavy Rain Showers' ]
word_dict = ['目前天氣晴朗', '目前下毛毛雨', '目前下毛毛雨', '目前下小雨', '目前下傾盆大雨', '目前下傾盆大雨', '目前下傾盆大雨' ]


def tell_temp():
	reader = codecs.getreader("utf-8")

	f = urlopen('http://api.wunderground.com/api/api_key/geolookup/conditions/q/TW/hsin-chu.json')

	json_string = f.read().decode('utf8')

	parsed_json = json.loads(json_string)

	f.close()

def tell_weather():
	reader = codecs.getreader("utf-8")

	f = urlopen('http://api.wunderground.com/api/api_key/geolookup/conditions/q/TW/hsin-chu.json')
	json_string = f.read().decode('utf8')

	parsed_json = json.loads(json_string)

	weather = parsed_json['current_observation']['weather']
	temp_c = parsed_json['current_observation']['temp_c']

	chinese('當前溫度' + str(temp_c) + '度')

	try: 
		chinese(word_dict[weather_dict.index(weather)])
	except: 
		english('The current weather is {}'.format(weather))

	f.close()


def forecast():
	reader = codecs.getreader("utf-8")

	f = urlopen('http://api.wunderground.com/api/api_key/geolookup/forecast/q/TW/hsin-chu.json')
	json_string = f.read().decode('utf8')

	parsed_json = json.loads(json_string)

	for day in parsed_json['forecast']['simpleforecast']['forecastday']:
	    print(day['date']['weekday'] + ":")
	    print("Conditions: ", day['conditions'])
	    print("High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C")

	f.close()
