from dotenv import load_dotenv
import os
import smtplib
from twilio.rest import Client



# setting up twilio client
load_dotenv()
ACCOUNT_SID = os.getenv('TWILIO_SID')
ACCOUNT_AUTH = os.getenv('TWILIO_AUTH')
SEND_NUMBER = os.getenv('TWILIO_SEND')
RECIEVE_NUMBER  = os.getenv('TWILIO_RECIEVE')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')

# twilio client for sending details on phone number
twilioClient = Client(ACCOUNT_SID, ACCOUNT_AUTH)

# email client for sending details on email
emailClient = smtplib.SMTP(host='smtp.office365.com', port=587)
emailClient.starttls()
emailClient.login(user=EMAIL, password=PASSWORD)



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def sendSMS(self, message:str, phoneNumber:str=RECIEVE_NUMBER):
        """Sends text message on phone number"""
        send =  twilioClient.messages.create(
            body=message,
            to=phoneNumber,
            from_=SEND_NUMBER
        )

        if send.status == "queued":
            return True
        else:
            return False

    def sendEmail(self, email:str, message:str):
        """Sends E-Mail to email address with message (included subject)."""
        emailClient.sendmail(
            from_addr=EMAIL,
            to_addrs=email,
            msg=message.encode('utf-8')
        )
        return True