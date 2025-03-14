from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('VIRTUAL_TWILIO_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('PHONE')


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)