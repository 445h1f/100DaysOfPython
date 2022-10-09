# importing twilio python library
from twilio.rest import Client
import os
from dotenv import load_dotenv
import random


# loading twilio env variables
load_dotenv()
ACCOUNT_SID = os.getenv('TWILIO_SID')
ACCOUNT_AUTH = os.getenv('TWILIO_AUTH')
SEND_NUMBER = os.getenv('TWILIO_SEND')
RECIEVE_NUMBER = os.getenv('TWILIO_RECIEVE')

# creating object of Twilio.rest Client class
twilioClient = Client(ACCOUNT_SID, ACCOUNT_AUTH)

def generateOTP(length:int=6) -> str:
    """Generate OTP of given length."""
    numbers = '0123456789'
    otp = ''.join([random.choice(numbers) for _ in range(length)])
    return otp

# getting otp
otp = generateOTP()

# sending OTP sms from SEND_NUMBER to RECIEVE_NUMBER phone number
message = twilioClient.messages.create(
    body=f'Your verification code is: {otp}',
    from_=SEND_NUMBER,
    to=RECIEVE_NUMBER
)


# printing message send status
# print(message.status)

print(otp)
# asking user to verify otp max chance (3)
chancesLeftText = False
for i in range(3, 0, -1):
    verifyOTP = input(f'Enter OTP to verify {chancesLeftText if chancesLeftText else ""}: ')
    if verifyOTP == otp:
        print('OTP Verified!')
        break
    else:
        chancesLeftText = f'({i-1} chances left)'
else:
    # priniting failed if loop not breaked
    print(f'OTP Verification Failed!')