from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

# getting linked user name and password from os environment
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# setting up chrome browser with selenium
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) #disables flags messages in console
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# opening linkedin website
driver.get('https://www.linkedin.com')


# getting job button element and clicking it
navButtons = driver.find_elements(By.CLASS_NAME, 'top-nav-link')
jobButton = navButtons[3]
jobButton.click()
time.sleep(5) # waiting 5 seconds so that the job page is loaded


# getting search box
jobSearchInput = driver.find_element(By.NAME, "keywords")
jobQuery = 'Python Developer'
jobSearchInput.send_keys(jobQuery) #entering job query in search box
jobSearchInput.send_keys(Keys.ENTER) # sending enter button to search
time.sleep(5) # waiting for 5 seconds so that the job can be loaded


# clicking first job search result
jobResults = driver.find_element(By.CSS_SELECTOR, '.jobs-search__results-list a')
jobResults.click()
time.sleep(5) # waiting for 5 seconds to load signup page


# clicking apply button
applyNowButton = driver.find_element(By.CSS_SELECTOR, '.top-card-layout__cta-container .apply-button')
applyNowButton.click()
time.sleep(5) # waiting for sign up page to load


# clinking log in button on signup page
logIn = driver.find_element(By.CLASS_NAME, 'main__sign-in-link')
logIn.click()
time.sleep(5) # waiting 5 seconds for login page to load


#entering login info and logging in to linkedin
emailInput = driver.find_element(By.ID, 'username')
emailInput.send_keys(EMAIL) # entering email
passwordInput = driver.find_element(By.ID, 'password')
passwordInput.send_keys(PASSWORD) # entering password

# clicking sign button
signIn = driver.find_element(By.CSS_SELECTOR, '.login__form_action_container  button')
signIn.click()
time.sleep(5) # sleeping 5 seconds to login

# saving job
saveButton = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
saveButton.click()
input('Enter any key to close...')

driver.quit()