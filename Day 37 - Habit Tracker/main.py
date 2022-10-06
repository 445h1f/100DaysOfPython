from urllib import response
import requests
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv() #imports all env var from .env file

# getting env from .env
token = os.getenv('PIXELA_TOKEN')
username = os.getenv('PIXELA_USERNAME')

pixelaEndpoint = 'https://pixe.la/v1/users'

# new account creation data to be send in post request
userParams = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# creating new account by making post req.
# response = requests.post(url=pixelaEndpoint, json=userParams)

# print(response.text)


graphEndpoint = f'{pixelaEndpoint}/{username}/graphs'

# post data for creating new graph
postData = {
    'id': 'codingstreak',
    'name': 'Coding Tracker',
    'unit': 'minutes',
    'type': 'float',
    'color': 'shibafu' # green for japanese
}

# including token in header of request
header = {
    'X-USER-TOKEN': token
}
# creating graph by making post request
# response = requests.post(url=graphEndpoint, json=postData, headers=header)
# print(response.text) #{"message":"Success.","isSuccess":true}


# adding pixel (data) to graph
myGraphEndpoint = f'{graphEndpoint}/{postData["id"]}'

# formatting datetime object
today = datetime.now()
date = today.strftime('%Y%m%d') #return in YYYYMMDD format
# shortcut
# date = f'{date:%Y%m%d}'

# data to be added in my graph
graphData = {
    'date': date, #yyyyMMdd format
    'quantity': '180' #60 minutes
}




# making post request to add data to graph id
# response = requests.post(url=myGraphEndpoint, json=graphData, headers=header)
# print(response.text) #{"message":"Success.","isSuccess":true}


# updating the existing pixel data
updateEndpoint = f'{myGraphEndpoint}/{date}'


# data for updating
updateData = {
    'quantity': '180' # update today's date pixel to 60 min
}

# making PUT request to update {today} data
# response = requests.put(url=updateEndpoint, json=updateData, headers=header)
# print(response.text)

# deleting pixel using DELETE request

# response = requests.delete(url=updateEndpoint, headers=header)
# print(response.text) #{"message":"Success.","isSuccess":true}