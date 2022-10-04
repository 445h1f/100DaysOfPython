##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from math import remainder
import smtplib
from datetime import datetime
import pandas
from random import randint


systemEmail = input('Enter your Hotmail E-mail: ')
systemName = 'Python Birthday Wisher!'

def getSuffix(year:int):
    """To get suffix for number like 1[st] for 1, 2[nd] for 2, etc."""
    remainder = year % 10
    if remainder == 1:
        suffix = 'st'
    elif remainder == 2:
        suffix = 'nd'
    elif remainder == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    return suffix


def randomTemplate(name, yearsOld):
    # generating random number from 1-3 inclusive for random template file
    randomTemplateNumber = randint(1, 3)
    templateFilename = f'.\letter_templates\letter_{randomTemplateNumber}.txt'
    with open(templateFilename) as r:
        content = r.read() # reading template
        # renaming particular string to format template for person
        content = content.replace('[NAME]', name.capitalize())
        content = content.replace('[YEAR]', f'{yearsOld}{getSuffix(yearsOld)}')
        content = content.replace('[SYSTEM_NAME]', systemName)
        return content

print(f'Starting Birthday Wisher...')

# reading birthday.csv using pandas
data = pandas.read_csv('birthdays.csv')

# email part -- logging in
with smtplib.SMTP('smtp.office365.com', port=587) as connection:
    connection.starttls()
    password = input('Enter system Email Password: ')
    connection.login(user=systemEmail, password=password)
    print(f'Started!\n')
    # running the wisher always
    # while True:
    today = datetime.now()
    month = today.month
    day = today.day
    currentYear = today.year
    # iterating over rows of pandas data object
    for index, value in data.iterrows():

        # checking if today is user birthday
        if value['month'] == month and value['day'] == day:
            # storing basic details
            name = value['name']
            email = value['email']
            year = value['year']

            # calculating nth birthday
            yearsOld = currentYear - year
            # getting random template
            template = randomTemplate(name, yearsOld)
            birthdayMessage = f'Subject:Happy Birthday!🎉🎊🎉\n\n{template}'
            print(f'Sending birthday wish to {name} [{email}]')
            # sending birthday email
            connection.sendmail(
                from_addr=systemEmail,
                to_addrs=email,
                msg=birthdayMessage.encode('utf-8')
            ) # utf-8 encoding message to avoid encoding error
            print(f'Sent!')

