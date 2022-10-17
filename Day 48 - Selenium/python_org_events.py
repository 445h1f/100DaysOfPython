from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# disabling error flags on console
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# setting up chrome drive
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# finding upcoming events in python.org website

# opening python.org website
driver.get('https://www.python.org/')


# getting event details element by using respective info from website
eventNames = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li a')
eventTimes = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li time')
# print(len(eventNames), len(eventTimes))

'''
for event in eventNames:
    print(event.text)

for time in eventTimes:
    print(time.get_attribute('datetime'))
'''
# creating event dictionary to store event info
eventDict = {}

# looping through length of eventNames list to get index
for index in range(len(eventNames)):
    eventName = eventNames[index].text # getting event name
    evenTime = eventTimes[index].get_attribute('datetime')[:10] # getting event time by value of datetime attribue and slicing first 10 index to get date in format YYYY-MM-DD format
    eventDict[index] = {
        'name': eventName,
        'time': evenTime
    }

print(eventDict)

