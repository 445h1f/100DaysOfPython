import requests
import time
from datetime import datetime
import smtplib

# Email setup
MYEMAIL = input('Enter your Hotmail Email: ')
PASSWORD = input('Enter password: ')
print(f'Wait few seconds while we configure settings.')
# connecting to hotmail smtp server
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
# enabling tls security
connection.starttls()
# logging in to email
connection.login(user=MYEMAIL, password=PASSWORD)


# specifying my latitude and longitude
MYLAT = 51.507351
MYLONG = -0.127758

sunAPI = 'https://api.sunrise-sunset.org/json'
issAPI = 'http://api.open-notify.org/iss-now.json'

def isISSOverhead():
    # making request to iss api
    issRequest = requests.get(url=issAPI)
    issRequest.raise_for_status()

    # getting current latitude and longitude of ISS
    issLocation = issRequest.json()['iss_position']
    issLatitude = float(issLocation['latitude'])
    issLongitude = float(issLocation['longitude'])

    # checking if iss lat and long is +-5 of my lat and long
    if MYLAT-5 <= issLatitude <= MYLAT+5 and MYLONG-5 <= issLatitude <= MYLONG+5:
        return True # returning true
    else:
        return False

def isNight():
    # parameters to be passed while requesting sunrise-sunset api
    parameters = {
        'lat': MYLAT,
        'lng': MYLONG,
        'formatted': 0
    }

    # requesting sunrise api
    sunResponse = requests.get(url=sunAPI, params=parameters)
    # throwing exception if status code in 200 (Success)
    sunResponse.raise_for_status()
    # json data from sunAPI
    sunData = sunResponse.json()
    # splitting sunData to get sunrise and sunset hours
    sunrise = int(sunData['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(sunData['results']['sunset'].split('T')[1].split(':')[0])
    # getting current hour
    today = datetime.now()
    hour = today.hour

    # returning True if it is night i.e. current hour is greater than sunset time and less than sunrise time
    if sunset < hour < sunrise:
        return True
    else:
        return False

print(f'Process started!')

while True:
    # checking if its night and iss is overhead
    if isNight():
        # checking if iss is overhead
        if isISSOverhead():
            # sending email notification to look up iss in the night sky
            message = f'Subject:Look Up🌃\n\nThe International Space Station is up above you in the sky!'
            connection.sendmail(
                from_addr=MYEMAIL,
                to_addrs=MYEMAIL,
                msg=message.encode('utf-8')
            )
            print(f'Notification sent!')
        else:
            print(f'ISS not overhead!')
    else:
        print(f'Not night!')

    # waiting for 60 seconds before going to next iteration
    time.sleep(60)