import datetime as dt
import pandas as pd
import random
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

now = dt.datetime.now()
today = (now.month, now.day)

birthdays_df = pd.read_csv('birthdays.csv')

birthdays_dict = {(row.month, row.day):row for (index,row) in birthdays_df.iterrows()}

if today in birthdays_dict:
  number = random.randint(1,3)
  with open(f'./letter-templates/letter_{number}.txt') as file:
    letter = file.read()
    letter = letter.replace('[NAME]', birthdays_dict[today]['name'])


my_email = os.getenv('EMAIL')
# Go to Gmail->Security->Allow 2-step verification->Search App Passwords->Generate password
password = os.getenv('PASSWORD')

with smtplib.SMTP('smtp.gmail.com') as connection:# your host
  connection.starttls() # making connection secure

  connection.login(user=my_email,password=password)
  connection.sendmail(from_addr=my_email,
                      to_addrs=birthdays_dict[today]['email'], 
                      msg=f'Subject:Happy Birthday!\n\n{letter}')
