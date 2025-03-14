################
#### Day 35 ####
################
import requests
import json
from twilio.rest import Client
import os
from dotenv import load_dotenv

# to create env variables in terminal, use export <variable_name>=...
# Load environment variables from .env file
load_dotenv()
MY_LAT = 50.233608
MY_LNG = 14.411180
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
my_phone_number = os.getenv('PHONE')
api_key = 'fbbcd4c15c24e2d256f9508f36ac1d25'
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast?'
parameters = {'lat':MY_LAT, 
              'lon':MY_LNG, 
              'appid':api_key,
              'exclude':'current,minutely,daily',
              'cnt': 4} # next 4 forecasts (each for 3 hour intervals)
'https://api.openweathermap.org/data/2.5/forecast?lat=50.233608&lon=14.411180&appid=fbbcd4c15c24e2d256f9508f36ac1d25'

response = requests.get(url=OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()

def take_umbrella(weather_data:json)->bool:
  is_rain = False
  for forecast in weather_data['list']:
    condition_code = int(forecast['weather'][0]['id'])
    if condition_code< 700:
      is_rain = True
      break
  return is_rain

if take_umbrella(weather_data):

  client = Client(account_sid, auth_token)
  message = client.messages.create(from_='+12694445788',
                                  body="It's going to rain today! Remember to bring an ☂️",
                                  to=my_phone_number)
  print(message.status)