from flask import Flask, render_template, request


app = Flask(__name__)



# response for home route
@app.route('/')
def home():
    return render_template('index.html')


# recieving login form data
@app.route('/login', methods=['POST'])
def recieveData():
    username = request.form['username']
    password = request.form['password']

    return f'<h1>Hello <b>{username}</b>, your password is <i>{password}</i>'

if __name__ == "__main__":
    app.run(debug=True) # starts flask server with automatic relaod when code changes