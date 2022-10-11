#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
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

    # creating flighData object to get price of flight
    today = dt.datetime.now()
    fromDate = today.strftime(DATE_FORMAT)
    sixMonthsFromToday = today + dt.timedelta(days=30*6) # adding 6 months to current date
    toDate = sixMonthsFromToday.strftime(DATE_FORMAT)
    # getting flight to cityCode from today date to 6 months later.
    priceData = flightSearch.getPrice(toCityCode=iataCode, fromDate=fromDate, toDate=toDate)
    # structuring flight data to class
    if priceData:
        flightData = FlightData(
                price = priceData["price"],
                originCity = priceData["route"][0]["cityFrom"],
                originAirport = priceData["route"][0]["flyFrom"],
                destinationCity = priceData["route"][0]["cityTo"],
                destinationAirport = priceData["route"][0]["flyTo"],
                outDate = priceData["route"][0]["local_departure"].split("T")[0],
                returnDate = priceData["route"][1]["local_departure"].split("T")[0]
            )
        if flightData.price < oldPrice:
            text = f'Low price alert! Only £{flightData.price} to fly from {flightData.originCity}-{flightData.originAirport} to {flightData.destinationCity}{flightData.destinationAirport}, from {flightData.outDate} to {flightData.returnDate}'
            notificationManager = NotificationManager()
            notifySMS = notificationManager.sendSMS(text=text)
            if notifySMS:
                print(f'Sent sms for {city}')
    else:
        print(f'No flight for {city}')

