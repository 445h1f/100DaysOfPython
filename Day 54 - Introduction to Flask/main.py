from flask import Flask

# minimal flask app

app = Flask(__name__)

# path of server
@app.route('/') # # for 127.0.0.1:5000/
@app.route('/home') # for 127.0.0.1:5000/home
def home():
    return "Welcome, This server is served by Flask!"


@app.route('/hello') # for 127.0.0.1:5000/hello
def hello():
    return "Hello, There!👋"


if __name__ == "__main__":
    app.run()