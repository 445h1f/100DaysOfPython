from flask import Flask, render_template
from login_form import LoginForm
from dotenv import load_dotenv
import os
from flask_bootstrap import Bootstrap


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
SYSTEM_EMAIL = os.getenv('SYSTEM_EMAIL')
SYSTEM_PASSWORD = os.getenv('SYSTEM_PASSWORD')

app = Flask(__name__)
app.secret_key = SECRET_KEY # setting secret key to flask app
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    """To handle login stuffs."""
    loginForm = LoginForm()
    # validating the form
    if loginForm.validate_on_submit():
        email = loginForm.email.data
        password = loginForm.password.data

        # checking if email password is correct and responding back with respective html
        if email == SYSTEM_EMAIL and password == SYSTEM_PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=loginForm)




if __name__ == '__main__':
    app.run(debug=True)