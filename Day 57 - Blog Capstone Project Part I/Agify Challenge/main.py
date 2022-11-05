from flask import Flask, render_template
import requests


# creating flask application
app = Flask(__name__)


def getAge(name):
    """Returns predicted age of provided name from agify API."""

    url = 'https://api.agify.io/'

    parameters = {
        'name': name,
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()['age']


def getGender(name):
    """Returns predicted gender of provided name from agify API."""

    url = 'https://api.genderize.io/'

    parameters = {
        "name": name,
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()['gender']


# defining response for home route!
@app.route('/')
def home():
    return render_template('index.html')


# response for guess router with name parameter
@app.route('/guess/<name>')
def makeGuess(name):
    """Respond back with predicted age and gender of entered name."""
    age = getAge(name)
    gender = getGender(name)

    return render_template("guess.html", name=name.title(), age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)