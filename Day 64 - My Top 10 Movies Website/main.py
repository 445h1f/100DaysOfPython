from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_V3_KEY')
print(TMDB_API_KEY)
TMDB_MOVIE_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
TMDB_MOVIE_DETAILS_URL = 'https://api.themoviedb.org/3/movie/'
TMDB_MOVIE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(250), unique=True, nullable=True)


with app.app_context():
    db.create_all() # creates sql database with movie table

class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = StringField("Your Review", validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired(), Length(min=1, max=250)])
    submit = SubmitField("Add Movie")



def searchMovie(query):
    """Search movie query on TMBD and returns results!"""
    params = {
        "api_key" : TMDB_API_KEY,
        "language": "en-US",
        "query": query,
    }

    response = requests.get(TMDB_MOVIE_SEARCH_URL, params=params)
    response.raise_for_status()
    results = response.json()["results"]
    return results


def getMovieDetails(movieId):
    """Returns movie details from TMBD API"""
    url = f'{TMDB_MOVIE_DETAILS_URL}/{movieId}'
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }

    response = requests.get(url, params)
    response.raise_for_status()
    return response.json()


@app.route("/")
def home():
    movies = db.session.query(Movie).all()

    # updating movie rankings by sorting ratings from high to low
    ratings = [movie.rating for movie in movies]
    ratings.sort(reverse=True)
    for movie in movies:
        rating = movie.rating
        index = ratings.index(rating)
        movie.ranking = index + 1

    return render_template("index.html", movies=movies[::-1]) # [::-1] for top rank to low


# route to add movies
@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        query = form.title.data
        results = searchMovie(query)

        return render_template('select.html', results=results)


    return render_template("add.html", form=form)


# route to find movie by id
@app.route('/find')
def find():
    movieId = request.args.get('id')
    # checking if movie is already in database
    movie = Movie.query.get(movieId)
    print(movie, type(movie), "==========")
    if movie is not None:
        # if yes redrecting to edit review page
        print("Movie is already in db!")
        return redirect(url_for("edit", id=movie.id))

    movieDetails = getMovieDetails(movieId)

    try:
        releaseDate = int(movieDetails["release_date"][:4])
    except:
        releaseDate = None

    newMovie = Movie(
        id = movieDetails["id"],
        title = movieDetails["original_title"],
        year = releaseDate,
        description = movieDetails["overview"],
        rating = movieDetails["vote_average"],
        img_url = f'{TMDB_MOVIE_IMAGE_URL}{movieDetails["poster_path"]}'
    )

    db.session.add(newMovie)
    db.session.commit()

    return redirect(url_for("edit", id=movieDetails["id"]))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movieId = request.args.get("id")
    movie = Movie.query.get(movieId)

    if form.validate_on_submit():
        newRating = float(form.rating.data)
        newReview = form.review.data
        movie.rating = newRating
        movie.review = newReview
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)

# route to delete movie
@app.route('/delete')
def delete():
    movieId = request.args.get("id")
    movieToDelete = Movie.query.get(movieId)
    db.session.delete(movieToDelete) # deleting movie from sql database
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
