from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

# getting environment variables
load_dotenv()
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
PROMISED_DOWNLOAD_SPEED = float(os.getenv('PROMISED_DOWNLOAD'))
PROMISED_UPLOAD_SPEED = float(os.getenv('PROMISED_UPLOAD'))

class InternetSpeedTwitterBot:

    def __init__(self):
        # setting up selenium driver for chrome browser
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

        # attributes to save speed results
        self.ooklaSpeedtestURL = 'https://www.speedtest.net'
        self.uploadSpeed = None
        self.downloadSpeed = None
        self.resultID = None

        # running speed test and tweet methods
        self.getInternetSpeed()
        self.tweetAtProvider()

    def getInternetSpeed(self):
        """Gets internet speed from Ookla Speed test website."""

        self.driver.get(self.ooklaSpeedtestURL) #opening speedtest website

        # starting internet speed test by pressing go button
        goButton = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        goButton.click() # clicking go button

        time.sleep(40) # waiting 40 seconds to finialize the result


        # scraping results
        self.downloadSpeed = float(self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text) # gets download speed

        self.uploadSpeed = float(self.driver.find_element(By.CSS_SELECTOR, '.upload-speed').text) # gets upload speed

        self.resultID = self.driver.find_element(By.CSS_SELECTOR, '.result-data > a').text # gets result id

        # print(self.uploadSpeed, self.downloadSpeed, self.resultID)



    def tweetAtProvider(self):
        """Tweets at internet provider if speed is less than promised speed."""
        if self.downloadSpeed < PROMISED_DOWNLOAD_SPEED or self.uploadSpeed < PROMISED_UPLOAD_SPEED:

            tweetText = f'Hey Internet Provider, why is my internet speed {self.downloadSpeed}down/{self.uploadSpeed}up when I pay for {PROMISED_DOWNLOAD_SPEED}down/{PROMISED_UPLOAD_SPEED}up?\n{self.ooklaSpeedtestURL}/result/{self.resultID}'
            # print(tweetText)

            # opening twitter.com
            self.driver.get('https://twitter.com/')

            # clicking sign in button
            self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()

            time.sleep(3)

            # entering username
            usernameInput = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            usernameInput.send_keys(TWITTER_USERNAME)
            usernameInput.send_keys(Keys.ENTER) # sending enter key

            time.sleep(3)

            # entering password
            passwordInput = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            passwordInput.send_keys(TWITTER_PASSWORD)
            passwordInput.send_keys(Keys.ENTER) # sending enter key to log in

            time.sleep(5) # waiting 5 seconds to laod home page

            # entering tweetText in tweet input field
            tweetInput = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweetInput.send_keys(tweetText)

            # pressing tweet button
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

            input('Enter any key to close....')


if __name__ == "__main__":
    InternetSpeedTwitterBot()