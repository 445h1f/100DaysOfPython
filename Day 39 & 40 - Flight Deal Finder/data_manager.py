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

SHEET_URL = 'https://api.sheety.co/0ead22775fc71f3ce85bb2cd274ccfee/flightDeals'

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def getSheetData(self):
        """Returns Sheet Data."""
        response = requests.get(url=f'{SHEET_URL}/prices', headers=headers)
        response.raise_for_status()
        return response.json()["prices"]

    def updateRowId(self, rowID:str, columnName:str, value:str):
        """Updates Google Sheet column of given row id."""
        data = {
            'price': {
                columnName: value
            }
        }
        rowEndpoint = f'{SHEET_URL}/prices/{rowID}'
        response = requests.put(url=rowEndpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.status_code

    def addUserToSheet(self, firstName:str, lastName:str, email:str):
        """Adds user info on google sheet."""
        data = {
            'user': {
                'firstName': firstName,
                'lastName': lastName,
                'email': email
            }
        }

        response = requests.post(url=f'{SHEET_URL}/users', json=data, headers=headers)
        response.raise_for_status()
        return True

    def getAllUsersDetails(self):
        """Returns user name and email from google sheet."""
        response = requests.get(url=f'{SHEET_URL}/users', headers=headers)
        response.raise_for_status()
        return response.json()['users']
