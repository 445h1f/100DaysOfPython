from urllib import response
import requests

# open trivia api endpoint
openTriviaUrl = 'https://opentdb.com/api.php'

# params for requesting 50 questions from openTriviaAPI of True/False type
parameters = {
    "amount": 50,
    "type" : "boolean"
}

response = requests.get(url=openTriviaUrl, params=parameters)
response.raise_for_status()

question_data = response.json()['results']



