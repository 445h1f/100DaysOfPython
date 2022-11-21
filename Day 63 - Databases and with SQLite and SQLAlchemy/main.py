from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired



# flask app configs
app = Flask(__name__)
app.config["SECRET_KEY"] = 'a6f77c5e1c9273f9942cf2eea22dbe6e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app) # sqlalchemy instance for handling sql database stuffs
Bootstrap(app)



# add book form
class AddBookForm(FlaskForm):
    bookTitle = StringField('Book Title: ', validators=[DataRequired()])
    bookAuthor = StringField('Book Author: ', validators=[DataRequired()])
    bookRating = StringField('Rating: ', validators=[DataRequired()])
    submit = SubmitField('Add Book')



# creating sql database model
class Books(db.Model): # creates books table
    id = db.Column(db.Integer, primary_key=True) # id column with int type
    title = db.Column(db.String(250), unique=True, nullable=False)  # title of book as unique string
    author = db.Column(db.String(250), nullable=False) # author of book as string
    rating = db.Column(db.Float, nullable=False) # rating of book as float greater than 0

with app.app_context():
    db.create_all()


# homepage
@app.route('/')
def home():
    allBooks = db.session.query(Books).all()
    return render_template('index.html', books=allBooks)


# route for adding books
@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        ## adding book on form submit
        bookTitle = form.bookTitle.data
        bookAuthor = form.bookAuthor.data
        bookRating = form.bookRating.data

        book = Books(
            title=bookTitle,
            author=bookAuthor,
            rating=bookRating
        )
        db.session.add(book) # adding book to sql session
        db.session.commit() # saving book to sql db

        return redirect(url_for('home'))

    return render_template('add.html', form=form)


# route for editing book rating
@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # updating rating of book id from form data
        bookID = request.form["id"]
        newRating = request.form["rating"]
        bookToUpdate = Books.query.get(bookID)
        bookToUpdate.rating = newRating
        db.session.commit() # saving changes
        redirect(url_for('home'))

    bookID = request.args.get('id')
    book = Books.query.get(bookID)
    return render_template("edit_rating.html", book=book)


@app.route("/delete")
def delete():
    # getting book id from request args
    bookID = request.args.get('id')

    # deleting book by book id
    bookToDelete = Books.query.get(bookID)
    db.session.delete(bookToDelete)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

