import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
import time

print(f'Welcome to Amazon Price Tracker.')
print(f'We send E-Mail to notify you if price of product goes down to your set target price.\n')

# getting email and password from environment variables
load_dotenv()
EMAIL = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('EMAIL_PASSWORD')


headers = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def getProductDetails(productLink:str):
    """Get name, price of Product on Amazon with Product Link."""
    response = requests.get(url=productLink, headers=headers)
    response.raise_for_status()
    html = response.text

    # scraping the response html
    soup = BeautifulSoup(html, "html.parser")

    # getting product name
    productName = soup.find(name='span', id="productTitle").getText().strip()
    productPrice = soup.find(name='span', class_='a-offscreen').getText().strip().replace('$', '').replace(',', '')

    return productName, float(productPrice)

# asking user to enter product link
productLink = input('Enter Amazon Product link to track: ')

# fetching prodcut details
print(f'Hang on, Getting info from Amazon...')

name, price = getProductDetails(productLink)
print(f'\n\nProduct Name: {name}\n\nCurrent Price: ${price}\n\n')

# asking user for their target price
targetPrice = float(input('Enter target price below which we\'ll notfiy you: '))

# checking if target price is equal to or greater than current price
if targetPrice >= price:
    # ending tracking target price is greater or equal to current price as not one wants to buy something at high price unless s/he likes wasting money.
    print(f'Current price of product is already {"equal to" if targetPrice == price else "less than"} your target price.')
else:
    # asking user for email address to send email when price is equal to or below target price
    userEmail = input('Enter your E-Mail address where we can notify: ').lower()

    # asking user whether to notify only once or always when price is below
    oneTimeNotification = input('Do you want us to notify only once? Type (y/n): ').lower()
    if oneTimeNotification == 'y':
        oneTimeNotification = True
    else:
        oneTimeNotification = False

    # asking user to enter minutes
    minutes = int(input('Enter time gap between two successive tracks (in minutes): '))

    print(f'Starting price tracking...')

    # connecting to hotmail smtp server
    emailClient = smtplib.SMTP('smtp.office365.com', port=587)
    emailClient.starttls()
    emailClient.login(user=EMAIL, password=PASSWORD)

    print(f'Started Tracking for every {minutes} minutes.')

    # checking price every provided minutes
    while True:
        name, price = getProductDetails(productLink)

        #checking if price is less than or equal to target price
        if price <= targetPrice:
            print(f'\nAlert!!! Price is now ${price}.\nSending E-Mail...')
            # sending email to user.
            emailSubject = f'Subject:Amazon Price Alert!'
            emailBody = f'Beep Boop!\nPrice of {name} is now ${price}!\nHurry up and grab it now before it goes up again!\n\n{productLink}'
            emailClient.sendmail(
                from_addr=EMAIL,
                to_addrs=userEmail,
                msg=f'{emailSubject}\n\n{emailBody}'.encode('utf-8')
            )
            print(f'E-Mail Sent!\n')

            # if one time notification exiting the loop
            if oneTimeNotification:
                print(f'Tracking Finished!')
                break
        # sleeping for given minutes
        time.sleep(minutes*60) # 1 minute = 60 seconds
        print(f'Sleeping for {minutes} min.')

