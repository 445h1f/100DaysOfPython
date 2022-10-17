from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# brewing selenium
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) #disables flags messages in console
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# finding cookie (which ruined life of someone as per post on reddit)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# finding evil cookie
cookie = driver.find_element(By.ID, 'cookie')


# killing cookie
startTime = time.time()
timeout = startTime + 5

while True:
    cookie.click() # clicking cookie
    currentTime = time.time() # getting current time

    # buying options if current time difference with timeout time is greater than 5
    if currentTime > timeout:
        # getting money
        money = driver.find_element(By.ID, 'money')
        money = money.text.strip()

        # replacing ',' in money if in money str
        if ',' in money:
            money = money.replace(',', '')

        money = int(money)

        canBuy = {}

        # getting all buyable items
        items = driver.find_elements(By.CSS_SELECTOR, '#store b')
        for item in items:
            if item.text == '':
                continue

            # splitting item text to get name and price
            itemTextSplitted = item.text.split('-')

            itemName = itemTextSplitted[0].strip()
            itemPrice = itemTextSplitted[1].strip()

            # replacing ',' in price if in price str
            if ',' in itemPrice:
                itemPrice = itemPrice.replace(',', '')
            itemPrice = int(itemPrice) # converting to int for comparison

            # checking if item can be bought (money greater than its price)
            if money > itemPrice:
                # adding in canBuy dict
                canBuy[itemPrice] = itemName


        # getting maximum of canBuy keys to buy max power
        maxBuyPrice = max(canBuy)
        maxBuyItem = canBuy[maxBuyPrice]

        # buying maxBuyItem
        buyItemID = f'buy{maxBuyItem}'
        buyItem = driver.find_element(By.ID, buyItemID)
        buyItem.click()
        print(f'Bought {maxBuyItem} for {maxBuyPrice}!')

        # increasing timeout to 5 seconds from current time
        timeout = currentTime + 5

    if currentTime - startTime > 300: #exiting loop if 5 minutes is elapsed
        # getting cookie per second
        cps = driver.find_element(By.ID, 'cps').text.split(':')[-1].strip()
        print(f'Killed {cps} cookie per second!')
        break

input('Enter any key to exit...')

driver.quit()