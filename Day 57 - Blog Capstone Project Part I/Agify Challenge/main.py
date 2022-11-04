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
    return f"""<h1>Welcome to Guess Maker!</h1>
    <h2>Enter your name in format /guess/&lt;name&gt to get results</h2>"""


# response for guess router with name parameter
@app.route('/guess/<name>')
def guess(name):
    """Respond back with predicted age and gender of entered name."""
    age = getAge(name)
    gender = getGender(name)

    return render_template("index.html", name=name.title(), age=age, gender=gender)



if __name__ == "__main__":
    app.run(debug=True)