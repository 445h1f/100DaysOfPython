from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

# Getting links from .env file
load_dotenv()
GoogleFormLink = os.getenv('GOOGLE_FORM_LINK')
ZillowLink = os.getenv('ZILLOW_LINK')

def getPropertyDetails(zillowLink:str) -> list:
    """Returns price, address, and link of property listed on provided zillow link."""

    propertyDetails = []

    # requesting ZillowLink and getting raw html
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    response = requests.get(url=zillowLink, headers=headers)
    response.raise_for_status()
    rawHTML = response.text


    # parsing raw html to beautifulsoup to get started with scraping
    soup = BeautifulSoup(rawHTML, "html.parser")
    # print(soup.prettify())

    # scraping address, prices and links of propertys'

    # prices
    propertyPrices = soup.select(selector="span[data-test='property-card-price']")
    priceList = [i.getText() for i in propertyPrices]
    # print(priceList)

    # address
    propertyAddressess = soup.select(selector='.property-card-data address')
    propertyAddressList = [i.getText() for i in propertyAddressess]
    # print(propertyAddressList)

    # links
    propertyLinks = soup.select(selector='.property-card-link')
    propertyLinksList = [i.get('href') for i in propertyLinks]
    # print(propertyLinksList)

    # adding data in propertyDetails list
    for index, price in enumerate(priceList):
        # double if because price maybe with bed and month both
        if '+' in price:
            price = price.split('+')[0]
        if '/' in price:
            price = price.split('/')[0]

        address = propertyAddressList[index]
        link = propertyLinksList[index]

        data = {
            "price": price,
            "address": address,
            "link": link
        }

        propertyDetails.append(data)

    return propertyDetails #empty list means you need to complete captcha verification

def fillGoogleForm(propertyData:list, googleFormLink:str=GoogleFormLink) -> None:
    """Fills property data in their respective fields in google form."""

    #configuring selenium web driver
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    # looping through data and filling in google form
    for index, data in enumerate(propertyData):
        price = data['price']
        address = data['address']
        link = data['link']

        # opening google form in chrome browser
        driver.get(googleFormLink)

        time.sleep(3) # waiting for website to load

        #getting all inputs
        allInputs = driver.find_elements(By.CSS_SELECTOR, '.whsOnd.zHQkBf')

        # entering address, price and link in their respective input section
        allInputs[0].send_keys(address) # 0 index is input for address
        allInputs[1].send_keys(price) # 1 for price
        allInputs[2].send_keys(link) # 2 for link

        # clicking submit button
        submitButton = driver.find_element(By.CSS_SELECTOR, '.NPEfkd.RveJvd.snByac')
        submitButton.click()

        # calculating % of task completed and printing on console.
        percentComplete = ((index+1)/len(propertyData)) * 100
        print(f'Completed {percentComplete:.2f}%')

        time.sleep(2) # waiting for submit

    # finally closing the browser
    driver.quit()


if __name__ == '__main__':
    # executing the functions
    propertyData = getPropertyDetails(ZillowLink)
    fillGoogleForm(propertyData)