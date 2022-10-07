from dotenv import load_dotenv
import requests
import os
from datetime import datetime

load_dotenv() # loading all env

# getting environment variables
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# nutrino exercise API endpoint
exerciseEndpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# sheety api endpoint for google sheet of my workout
sheetEndpoint = os.getenv('SHEET_ENDPOINT')

# headers for nutrino api
header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

# asking user to input exercise details in english
query = input('Tell me what exercise you did: ')

# json request body for making post request to nutrino excersie api endpoint
jsonData = {
    "query" : query,
    "gender" : "female",
    "weight_kg" : '51.5',
    "height_cm" : '163.64',
    "age" : '19'
}

# making POST request to Exercise endpoint
neutrinoResponse = requests.post(url=exerciseEndpoint, json=jsonData, headers=header)
neutrinoResponse.raise_for_status() # printing request exception if error occurs
neutrinoData = neutrinoResponse.json() # getting response as json

# formatting todays date in dd/mm/yyyy format
today = datetime.now()
exerciseDate = today.strftime('%d/%m/%Y')
exerciseTime = today.strftime('%H:%M:%S')


sheetyAuthHeader = {
    'Authorization': f'Bearer {BEARER_TOKEN}'
}


# saving each exercise information through POST on google sheet via sheety API
for exerciseData in neutrinoData["exercises"]:
    duration = exerciseData['duration_min']
    calories = exerciseData['nf_calories']
    name = exerciseData['name'].title()
    dateToSave = {
        'workout' : {
            'date': exerciseDate,
            'time': exerciseTime,
            'exercise': name,
            'duration': duration,
            'calories': calories
        }
    }
    sheetResponse = requests.post(url=sheetEndpoint, json=dateToSave,  headers=sheetyAuthHeader)
    sheetResponse.raise_for_status()
    print(sheetResponse.text)






