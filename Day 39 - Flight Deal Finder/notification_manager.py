from dotenv import load_dotenv
import os
from twilio.rest import Client

# setting up twilio client
load_dotenv()
ACCOUNT_SID = os.getenv('TWILIO_SID')
ACCOUNT_AUTH = os.getenv('TWILIO_AUTH')
SEND_NUMBER = os.getenv('TWILIO_SEND')
RECIEVE_NUMBER  = os.getenv('TWILIO_RECIEVE')

twilioClient = Client(ACCOUNT_SID, ACCOUNT_AUTH)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def sendSMS(self, text:str):
        send =  twilioClient.messages.create(
            body=text,
            to=RECIEVE_NUMBER,
            from_=SEND_NUMBER
        )

        if send.status == "queued":
            return True
        else:
            return False
