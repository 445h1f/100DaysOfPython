from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Respond the request with index.html file in templates folder."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)