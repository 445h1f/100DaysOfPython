from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# setting up selenium robo
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

'''
# opening wikipedia main page
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# getting article count
aricleCount = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(aricleCount.text)

# clicking article count hyperlink
aricleCount.click()

# clicking link by passing hyperlink text
contributionsLink = driver.find_element(By.LINK_TEXT, 'Contributions')
contributionsLink.click()

# searching on wikipedia
searchBox = driver.find_element(By.ID, 'searchInput')
searchBox.send_keys('Selenium')
# sending enter key to search
searchBox.send_keys(Keys.ENTER)
'''

# Signup to the lap report challenge
driver.get('https://secure-retreat-92358.herokuapp.com/')

# getting input fields and entering relevant data in them

firstName = driver.find_element(By.NAME, 'fName')
firstName.send_keys('Foo')

lastName = driver.find_element(By.NAME, 'lName')
lastName.send_keys('Bar')

email = driver.find_element(By.NAME, 'email')
email.send_keys('foobar@foo.org')

# submitting form by clicking submit button
submitButton = driver.find_element(By.TAG_NAME, 'button') # submit is the only tag in the html thats why using
submitButton.click()

time.sleep(10) # waiting to see success page
driver.quit()