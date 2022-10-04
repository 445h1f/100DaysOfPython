from calendar import week
import smtplib
from datetime import date, datetime
import random

# email address from which you want to send email
myEmail = input('Enter your hotmail email: ')

# opening quote.txt and storing all quotes in a list
with open('quotes.txt') as r:
    quotes = r.readlines()

# getting current datetime object
today = datetime.now()

# checking if day is saturday from weekday method (0-Monday,....,5-Saturday,6-Sunday)
weekDay = today.weekday()
if weekDay == 5: #i.e. Saturday:

    # picking random qoute from quotes list using choice method
    quote = random.choice(quotes)
    print(f'Starting process...')
    # making connection to smtp server of hotmail
    with smtplib.SMTP('smtp.office365.com', port=587) as connection:

        # enabling tls security
        connection.starttls()

        # asking user to input password (don't want to save passowrd on code)
        password = input(f'Enter password for {myEmail}: ')

        # logging in with credentials
        connection.login(user=myEmail, password=password)

        # asking user where for receiving email address
        recieverEmail = input(f'Enter Email for Saturday Motivation: ')

        emailContent = f'Subject:Your Saturday Motivation\n\n{quote}'

        # sending email
        connection.sendmail(
            from_addr=myEmail,
            to_addrs=recieverEmail,
            msg=emailContent
        )
        print(f'Email Sent!\nGo and check what you got.')







