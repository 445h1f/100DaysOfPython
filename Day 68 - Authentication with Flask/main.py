from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

loginManager = LoginManager()
loginManager.init_app(app)


@loginManager.user_loader
def loadUser(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))
    name = db.Column(db.String(1000))


#Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email').lower()
        # checking email if its already signed up
        checkEmail = User.query.filter_by(email=email).first()
        if checkEmail:
            #email already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        password = request.form.get('password')
        hashedPassword = generate_password_hash(password=password, salt_length=32)
        newUser = User(
            name = request.form.get('name'),
            email = email,
            password = hashedPassword
        )
        db.session.add(newUser)
        db.session.commit()

        #Log in and authenticate user after adding details to database.
        login_user(newUser)


        return redirect(url_for('secrets'))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # checking password

        # getting user
        user = User.query.filter_by(email=email).first()
        if user:
            hashedPassword = user.password
            if check_password_hash(hashedPassword, password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                # password is not same as in database
                flash('You\'d entered incorrect password. Please try again.')
                return redirect(url_for('login'))
        else:
            # email not in database means user not signed up
            flash("That email does not exist, please register it.")
            return redirect(url_for('login'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
def logout():
    # check whether user is logged in
    if current_user.is_authenticated:
        # yes then log out
        logout_user()
        flash('Successfully logged out.')
    else:
        # display not logged in as user is not logged in
        flash('User not logged in.')

    return redirect(url_for('login'))

@app.route('/download')
def download():
    # allowing file access only if user is logged in else displaying user not logged in.
    if current_user.is_authenticated:
        return send_from_directory(directory='static', path='files/cheat_sheet.pdf')
    else:
        # display not logged in as user is not logged in
        flash('Log in first to get access to the secret file.')
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
