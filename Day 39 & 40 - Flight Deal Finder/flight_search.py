import requests
from dotenv import load_dotenv
import os

load_dotenv()
KIWI_APIKEY = os.getenv('KIWI_APIKEY')

headers = {
    'apikey': KIWI_APIKEY
}

SEARCH_ENDPOINT = 'https://api.tequila.kiwi.com/locations/query'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def searchCity(self, city:str):
        """Returns Airport Details of searched City."""
        parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
        }
        response = requests.get(url=SEARCH_ENDPOINT, params=parameters, headers=headers)
        response.raise_for_status()
        try:
            return response.json()["locations"][0] # returning first result in location key
        except:
            return False

    def getPrice(self, toCityCode:str, fromDate:str, toDate:str, departureAirportCode:str="LON", stopOvers:int=0):
        """Getting flight price to City from date range."""
        headers['Content-Type'] = 'application/json'
        priceEndpoint = 'https://api.tequila.kiwi.com/v2/search'
        # fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
        parameters = {
            "fly_from": departureAirportCode,
            "fly_to": toCityCode,
            "dateFrom": fromDate,
            "dateTo": toDate,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": stopOvers,
            "curr": "GBP"
        }
        response = requests.get(url=priceEndpoint, headers=headers, params=parameters)
        response.raise_for_status()
        try:
            return response.json()['data'][0]
        except:
            return False