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
USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')
TARGET_USERNAME = os.getenv('TARGET_ACCOUNT')



class InstaFollower:

    def __init__(self):

        # setting up selenium driver for chrome browser
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get('https://www.instagram.com') # opening instagram.com

        self.login()


    def login(self):
        """Logins to Instagram."""

        # entering username and password
        usernameInput = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        usernameInput.send_keys(USERNAME)

        passwordInput = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        passwordInput.send_keys(PASSWORD)

        # sending enter key to log in
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(10) # waiting for login credentials to be verified

        # dismissing save login info popup
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()

        time.sleep(3) # waiting for home page to load

        # dismissing turn on notification popup
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()

        # input('enter any key to proceed...')


    def findFollowers(self, username:str=TARGET_USERNAME):
        """Search instagram user and return their follower counts."""

        # clicking search button
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div').click()

        time.sleep(3)

        # entering username in search field
        searchInput = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/input')
        searchInput.send_keys(TARGET_USERNAME)

        time.sleep(3)

        # clicking on first search result
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div').click()

        time.sleep(5)

        # getting follower
        self.followerElement = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span')
        print(self.followerElement.text)


    def follow(self):
        """Follow followers of target account."""

        # opening followers popup
        self.followerElement.click()

        time.sleep(5) # waiting for popup to load
        # getting all user elements for usernames
        userElements = self.driver.find_elements(By.CSS_SELECTOR, '._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm')

        # getting all follow button texts and button elements

        followButtonTexts = self.driver.find_elements(By.CSS_SELECTOR, '._aacl._aaco._aacw._aad6._aade')

        # print(followButtonsTexts)

        # getting all follow buttons
        followButtons = self.driver.find_elements(By.CSS_SELECTOR, '._acan._acap._acas')

        # looping through all follow button and following user if not followed already
        for index, button in enumerate(followButtons):

            username = userElements[index].text # getting username of user
            buttonText = followButtonTexts[index].text.lower() # getting button text to check if already followed
            # print(username, buttonText)

            if buttonText == 'follow': # user is not already followed so following user
                # try:
                button.click()
                # except Exception as e:
                    # print(str(e))
                print(f'Followed {username}!')
                time.sleep(1) # sleeping 1 seconds between every follow to avoid bot detection
            else:
                print(f'{username} is already followed!')

        while True:
            command = input('Enter command to execute: ')
            exec(command)

if __name__ == "__main__":
    instaBot = InstaFollower()
    instaBot.findFollowers()
    instaBot.follow()