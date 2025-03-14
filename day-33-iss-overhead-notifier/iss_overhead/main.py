################
#### Day 33 ####
################
#%% Libraries and static data
import requests
import smtplib
import time
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Load environment variables from .env file
from datetime import datetime
MY_LAT = 50.233608
MY_LNG = 14.411180
#%% first API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code) # 200


# will raise exception if something is wrong e.g. HTTPError: 404 Client Error:
# Not Found for url: http://api.open-notify.org/is-now.json
# response.raise_for_status()

#Response codes
#1xx: hold on, something is happening
#2xx: here you go
#3xx: Permission denied
#4xx: you screwed up - e.g. wrong url
#5xx: I (server) screwed up - server is down
# see statuses here: https://www.webfx.com/web-development/glossary/http-status-codes/


def is_iss_close():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()
  iss_lat = float(data['iss_position']['latitude']) # you get a number
  iss_lng = float(data['iss_position']['longitude']) # you get a number

  if ((MY_LAT-5)<=iss_lat <= (MY_LAT+5)) and ((MY_LNG-5)<=iss_lng <= (MY_LNG+5)):
    return True

def is_dark():
  parameters = {
  'lat':MY_LAT,
  'lng':MY_LNG,
  'formatted':0
} # API parameters should be defined in dict with the same key names as in API documentation
  response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()

  data = response.json()
  sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
  sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
  hour_now = datetime.now().hour
  if (hour_now >= sunset) and (hour_now<=sunrise):
    return True
while True:
  time.sleep(60) # check every 60 seconds
  if is_iss_close() and is_dark():
    my_email = os.getenv('EMAIL')
    # Go to Gmail->Security->Allow 2-step verification->Search App Passwords->Generate password
    password = os.getenv('PASSWORD')
    with smtplib.SMTP('smtp.gmail.com') as connection:# your host
      connection.starttls() # making connection secure

      connection.login(user=my_email,password=password)
      connection.sendmail(from_addr=my_email,
                          to_addrs=my_email, 
                          msg=f'Subject:Look Up for ISS\n\n TheISS is above you!')