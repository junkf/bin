#!/usr/bin/python2

import urllib2
import json
import datetime

f = urllib2.urlopen('http://api.wunderground.com/api/cc8d4e50c10110fe/geolookup/forecast/q/DC/Washington.json')
json_string = f.read()
parsed_json = json.loads(json_string)
city = parsed_json['location']['city']
state = parsed_json['location']['state']
forecast_today = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
forecast_tomorrow = parsed_json['forecast']['txt_forecast']['forecastday'][1]['fcttext']
high_today = parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
low_today = parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
high_tomorrow = parsed_json['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit']
low_tomorrow = parsed_json['forecast']['simpleforecast']['forecastday'][1]['low']['fahrenheit']
f.close()
g = urllib2.urlopen('http://api.wunderground.com/api/cc8d4e50c10110fe/geolookup/conditions/q/DC/Washington.json')
json_string = g.read()
parsed_json = json.loads(json_string)
current_today = parsed_json['current_observation']['temp_f']
g.close()


print "\n\nWeather in %s, %s. \n\nCurrently:\n\n%s degrees; high of %s and low of %s today. \n\nToday's forecast:\n\n%s \n\nTomorrow:\n\n%s / %s. %s. \n\n" % (city, state, current_today, high_today, low_today, forecast_today, high_tomorrow, low_tomorrow, forecast_tomorrow)


