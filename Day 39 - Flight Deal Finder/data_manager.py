from pprint import pprint
import requests
from dotenv import load_dotenv
import os

# getting envs
load_dotenv()
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

# request headers for sheety api
headers = {
    'Authorization': f'Bearer {SHEETY_AUTH}'
}

SHEET_URL = 'https://api.sheety.co/0ead22775fc71f3ce85bb2cd274ccfee/flightDeals/prices'

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self) -> None:
        pass

    def getSheetData(self):
        """Returns Sheet Data."""
        response = requests.get(url=SHEET_URL, headers=headers)
        response.raise_for_status()
        return response.json()["prices"]

    def updateRowId(self, rowID:str, columnName:str, value:str):
        """Updates Google Sheet column of given row id."""
        data = {
            'price': {
                columnName: value
            }
        }
        rowEndpoint = f'{SHEET_URL}/{rowID}'
        response = requests.put(url=rowEndpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.status_code


