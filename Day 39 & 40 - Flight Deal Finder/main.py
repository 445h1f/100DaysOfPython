#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import email
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint # to print output in much readable form
import datetime as dt

# Blueprint of Data Manager class to handle data related stuffs via Sheety API
sheetManager = DataManager()
flightSearch = FlightSearch()

DATE_FORMAT = '%d/%m/%Y'

# getting data of google sheet
sheetData = sheetManager.getSheetData()


# asking if to send on phone or not
sendOnPhone = input('Send Flight Details on Phone? Type (y/n): ').lower()
if sendOnPhone == 'y':
    sendOnPhone = True
else:
    sendOnPhone = False

# asking if to send on email or not
sendOnEmail = input('Send Details on Email? Type (y/n): ').lower()
if sendOnEmail == 'y':
    sendOnEmail = True
else:
    sendOnEmail = False

# checking sheetData if it contains IATACodes
for rowData in sheetData:
    iataCode = rowData['iataCode']
    city = rowData['city']
    rowID = rowData['id']
    oldPrice = rowData['lowestPrice']
    if iataCode == '':
        searchResult = flightSearch.searchCity(city)
        if searchResult:
        # print(f'city: {city}, id: {rowID}, {searchResult}')
        # updating IATACodes of each city in google sheet
            iataCode = searchResult['city']['code']
            sheetManager.updateRowId(rowID=rowID, columnName="iataCode", value=iataCode)

    # formatting date for range of date to search

    # from todays date
    today = dt.datetime.now()
    fromDate = today.strftime(DATE_FORMAT)

    # six month from todays date
    sixMonthsFromToday = today + dt.timedelta(days=30*6) # adding 6 months to current date
    toDate = sixMonthsFromToday.strftime(DATE_FORMAT)
    stopOvers = 0

    # getting flight to cityCode from today date to 6 months later.
    priceData = flightSearch.getPrice(toCityCode=iataCode, fromDate=fromDate, toDate=toDate, stopOvers=stopOvers)

    # searching again with stop over 1 if flight is not found
    if not priceData:
        stopOvers = 1
        priceData = flightSearch.getPrice(toCityCode=iataCode, fromDate=fromDate, toDate=toDate, stopOvers=stopOvers)

    if priceData:
        # structuring flight data to class if data is found
        flightData = FlightData(
                price = priceData["price"],
                originCity = priceData["route"][0]["cityFrom"],
                originAirport = priceData["route"][0]["flyFrom"],
                destinationCity = priceData["route"][0]["cityTo"],
                destinationAirport = priceData["route"][0]["flyTo"],
                outDate = priceData["route"][0]["local_departure"].split("T")[0],
                returnDate = priceData["route"][1]["local_departure"].split("T")[0]
            )

        # adding stop overs and via city in flight data if stopOvers is 1 i.e. True
        if stopOvers: # 1 is True and 0 is false
            flightData.stopOvers = 1
            flightData.viaCity = priceData["route"][0]["cityTo"]

        #sending low price alert if price is less the old price
        if flightData.price < oldPrice:
            text = f'Low price alert! Only £{flightData.price} to fly from {flightData.originCity}-{flightData.originAirport} to {flightData.destinationCity}-{flightData.destinationAirport}, from {flightData.outDate} to {flightData.returnDate}'

            # adding stop over details to email if stop over is greater than 0
            if flightData.stopOvers > 0:
                text += f'\n Flight has {flightData.stopOvers} stop over, via {flightData.viaCity}.'


            if sendOnPhone:
                # sending sms via twilio to phone number
                notificationManager = NotificationManager()
                notifySMS = notificationManager.sendSMS(message=text)
                if notifySMS:
                    print(f'SMS Sent!')

            if sendOnEmail:
                # sending emails to all users
                users = sheetManager.getAllUsersDetails()
                for user in users:
                    firstName = user['firstName']
                    lastName = user['lastName']
                    email = user['email']
                    # email subject
                    subject = f'Subject:Cheap Flight for {city}!\n\n'

                    # adding greetings to user in email
                    greetText = f'Hello, {firstName} {lastName}\n\n'

                    # formatting google flight link (deprecated)
                    # googleFlightLink = f' https://www.google.co.uk/flights?hl=en#flt={flightData.originAirport}.{flightData.destinationAirport}.{today.strftime("%Y-%m-%d")}*{flightData.destinationAirport}.{flightData.originAirport}.{sixMonthsFromToday.strftime("%Y-%m-%d")}'

                    # final email message
                    emailMessage = f'{subject}{greetText}{text}'

                    # sending email
                    notificationManager = NotificationManager()
                    notifyEmail = notificationManager.sendEmail(email=email, message=emailMessage)
                    if notifyEmail:
                        print(f'Email sent to {email}')
    else:
        print(f'No flight for {city} with even 1 stop over!')