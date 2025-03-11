 ### TODO Send a motivational quote via email on the current weekday
import datetime as dt
import random
now = dt.datetime.now()
day_of_week = now.weekday()

import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

my_email = os.getenv('EMAIL')
# Go to Gmail->Security->Allow 2-step verification->Search App Passwords->Generate password
password = os.getenv('PASSWORD')


if day_of_week == 0: # for Monday
  with open('quotes.txt', 'r') as file:
    quotes_list = file.readlines()
    today_quote = random.choice(quotes_list)
  with smtplib.SMTP('smtp.gmail.com') as connection:# your host
    connection.starttls() # making connection secure

    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email, 
                        msg=f'Subject:Your Monday Motivation\n\n{today_quote}')


