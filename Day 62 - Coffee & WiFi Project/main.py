from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name: ', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL): ', validators=[DataRequired(), URL()])
    openingTime = StringField('Opening Time e.g. 8AM: ', validators=[DataRequired()])
    closingTime = StringField('Closing Time e.g. 9PM: ', validators=[DataRequired()])
    coffeeRating = SelectField('Coffee Rating: ', choices=['☕'*i for i in range(1, 6)],validators=[DataRequired()])
    wifiRating = SelectField('WiFi Rating: ', choices=['💪'*i if i > 0 else '✘' for i in range(6)], validators=[DataRequired()]) # adding all 5 choices with list comprehension with x as first choice
    powerRating = SelectField('Power Outlet Rating: ', choices=['🔌'*i if i > 0 else '✘' for i in range(6)], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # adding submitted data to csv file
        with open('cafe-data.csv', 'a', encoding='utf-8') as csvFile:

            submittedData = [form.cafe.data, form.location.data, form.openingTime.data, form.closingTime.data, form.coffeeRating.data, form.wifiRating.data, form.powerRating.data]

            csvFile.write(f'\n{(",").join(submittedData)}')

        return redirect(url_for('cafes')) # redirects to route for cafes func

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csvFile:
        # reading data from csv file and storing each row data in list as nested list of listOfRows
        csvData = csv.reader(csvFile, delimiter=',')
        listOfRows = []
        for row in csvData:
            listOfRows.append(row)
    return render_template('cafes.html', cafes=listOfRows)


if __name__ == '__main__':
    app.run(debug=True)
