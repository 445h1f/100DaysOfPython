from flask import Flask
from random import randint

# creating flask app
app = Flask(__name__)

gifs = {
    "guess": "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif",
    "high" : "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",
    "low" : "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif",
    "correct" : "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
}

randomNumber = randint(0, 9)

@app.route('/')
def home():
    """Sending respone when user visits home route."""
    return f"""<h1>Guess a number between 0 and 9</h1>
    <img src='{gifs['guess']}' alt='guess-number-img'>"""

@app.route('/<int:number>')
def checkNumber(number):
    """Checks answer from Url and response back as per condition."""

    # checking if number is <,> or == to randomNumber and setting text, gif accordingly
    if number < randomNumber:
        text = 'Too low, try again!'
        color = 'red'
        gifKey = 'low'
    elif number > randomNumber:
        text = 'Too high, try again!'
        color = 'purple'
        gifKey = 'high'
    else:
        text = 'You find me!'
        gifKey = 'correct'
        color = 'green'

    html = f"""<h1 style='color:{color}'>{text}</h1>
            <img src='{gifs[gifKey]}' alt='{gifKey}-img'>"""

    # sending response
    return html


if __name__ == "__main__":
    app.run(debug=True) # running flask app if run as a script with automatic reload on code change