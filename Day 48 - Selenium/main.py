from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# load_dotenv()
# CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
# print(CHROME_DRIVER_PATH)

# setting up chrome driver with selenium
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# opening amazon.com with selenium chrome driver
driver.get('https://www.amazon.com/dp/B09MGGD6XH?ref_=cm_sw_r_cp_ud_dp_KK61M6JV4MX4MR6RNCZV')

# finding price of product using find_element by class name
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.text)

# finding search box in amazon.com
searchBox = driver.find_element(by=By.ID, value='twotabsearchtextbox')
print(searchBox.get_attribute('placeholder')) # getting placeholder of search bar input element

# closing chrome driver browser
# driver.close() # closes the active tab
# driver.quit() # closes the whole chrome browser