import pyowm
import commands
import datetime
import time 


def espeak(string):
    output = 'espeak "%s"' % string
    a = commands.getoutput(output)




owm = pyowm.OWM('44e0336fae5b9287ac46faf9721fd336')  # You MUST provide a valid API key

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
#forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)

timetemp=time.gmtime()
espeak("the time is")
espeak(timetemp.tm_hour)
espeak(timetemp.tm_min)
espeak("hours") 

observation = owm.weather_at_place('Pune,in')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20, 
                              # status=Clouds>

# Weather details

a=w.get_humidity()              # 87
b=w.get_temperature('fahrenheit')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print a 
print b

espeak("wheather update for today is max temperature")
espeak(b['temp_max'])
espeak("degree farhenite and minimum temperature")
espeak(b['temp_min'])


