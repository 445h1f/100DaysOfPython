import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
import time

# loading all needed env variables
load_dotenv()
ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
ACCOUNT_SID = os.getenv('TWILIO_SID')
ACCOUNT_AUTH = os.getenv('TWILIO_AUTH')
SEND_NUMBER = os.getenv('TWILIO_SEND')
RECIEVE_NUMBER = os.getenv('TWILIO_RECIEVE')
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')


# asking user for stock name to get info
STOCK = input('Enter stock name: ').upper()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantageEndpoint = f'https://www.alphavantage.co/query'

def getStockDetails(stock):
    params = {
       'function' : 'SYMBOL_SEARCH',
       'keywords' : stock,
       'apikey' : 'P6I9RFPVBWQY142R'
    }

    response = requests.get(alphavantageEndpoint, params=params)
    if response.status_code == 200:
        jsonData = response.json()
        try:
            return jsonData['bestMatches'][0]
        except:
            return False
    else:
        return False



alphaParameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY
}

alphavantageResponse = requests.get(alphavantageEndpoint, params=alphaParameters)
alphavantageResponse.raise_for_status()
# storing json response
alphavantageJson = alphavantageResponse.json()
# checking if stock name is invalid
if "Error Message" in alphavantageJson:
    print(f'{STOCK} is not a valid stock name!')
else:
    # getting previous two dates close prices from response
    dailyPrices = alphavantageJson['Time Series (Daily)']
    allDates = [key for key in dailyPrices.keys()] # getting all dates in list

    yesterdayPrice = float(dailyPrices[allDates[0]]['4. close']) # index 0 for yesterday
    ereyesterdayPrice = float(dailyPrices[allDates[1]]['4. close']) # index 1 for ereyesterday = yesterday of yesterday

    # calculating percentage. taking abs to absolute value of price change in previous two days
    changePercentage = (abs(yesterdayPrice - ereyesterdayPrice) / yesterdayPrice) * 100
    print(changePercentage)

    # setting up emoji if yesterday price is higher than ereyesterday else down
    if yesterdayPrice > ereyesterdayPrice:
        emoji = '🔺'
    else:
        emoji = '🔻'

    # getting company name from stock name
    companyName = getStockDetails(STOCK).get('2. name')
    # setting company name to stock if company name not found or some error occurred
    if not companyName or companyName is None:
        companyName = STOCK
    print(f'{companyName} ({STOCK}) {emoji}{round(changePercentage)}%')

    # getting news and sending sms when changePercent is greater than or equal to 5
    if changePercentage >= 5:
        newsAPIEndpoint = 'https://newsapi.org/v2/everything'
        ## STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
        newsParams = {
            'q' : companyName,
            'from' : allDates,
            'sortBy' : 'publishedAt',
            'apiKey' : NEWSAPI_KEY
        }

        newsResponse = requests.get(url=newsAPIEndpoint, params=newsParams)
        newsResponse.raise_for_status()
        newsData = newsResponse.json()

        # getting all articles
        articles = newsData['articles']
        latestThreeArticles = [articles[i] for i in range(3)] # first 3 items (news)
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.

        #Optional: Format the SMS message like this:
        """
            TSLA: 🔺2%
            Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
            Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
            or
            "TSLA: 🔻5%
            Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
            Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        """
        # sending sms for first three articles
        twilioClient = Client(ACCOUNT_SID, ACCOUNT_AUTH)
        for index, news in enumerate(latestThreeArticles):
            title = news['title']
            description = news['description']

            messageFormat = f'{STOCK}: {emoji}{round(changePercentage)}%\nHeadline: {title}\nBrief: {description}'
            message = twilioClient.messages.create(
                body=messageFormat,
                from_=SEND_NUMBER,
                to=RECIEVE_NUMBER
            )
            if str(message.status) == 'queued':
                print(f'[{index+1}] Sent SMS!')
            else:
                print(message.status)
            time.sleep(1)