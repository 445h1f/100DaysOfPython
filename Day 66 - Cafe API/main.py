from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def toDictionary(self):
        """Formats data for json response."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


## HTTP GET - Read Record


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def getRandomCafe():
    cafes = db.session.query(Cafe).all()
    randomCafe = random.choice(cafes)
    return jsonify(cafe = {
        "name": randomCafe.name,
        "map_url": randomCafe.map_url,
        "img_url": randomCafe.img_url,
        "location": randomCafe.location,

        # other properties in sub category
        "amenities" : {
            "seats": randomCafe.seats,
            "has_toilet": randomCafe.has_toilet,
            "has_wifi": randomCafe.has_wifi,
            "has_sockets": randomCafe.has_sockets,
            "can_take_calls": randomCafe.can_take_calls,
            "coffee_price": randomCafe.coffee_price
        }
    })

@app.route('/all')
def getAllCafes():
    allCafes = db.session.query(Cafe).all()
    allCafesList = [cafe.toDictionary() for cafe in allCafes]
    return jsonify(cafes=allCafesList)


@app.route('/search')
def searchCafe():
    queryLocation = request.args.get('loc')
    cafeResults = db.session.query(Cafe).filter_by(location=queryLocation).all()
    if cafeResults:
        return jsonify(cafes=[cafe.toDictionary() for cafe in cafeResults])
    else:
        return jsonify(error={
            "not found": f"Sorry, we don't have a cafe at that location."
        })


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def addNewCafe():
    newCafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(newCafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
# put is replacing the whole data
# patch is updating a fielf in data

@app.route('/update-price/<cafeId>', methods=["PATCH"])
def updateCafePrice(cafeId):
    newPrice = request.args.get('new_price')
    cafe = db.session.query(Cafe).get(cafeId)
    if cafe:
        cafe.coffee_price = newPrice
        db.session.commit()
        # 200 for ok
        return jsonify({"success": "Successfully updated the price."}), 200
    else:
        # 404 for resource not found
        return jsonify(error={
            "not found": "Sorry, a cafe with that id was not found."
        }), 404


## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafeId>', methods=["DELETE"])
def deleteCafe(cafeId):
    apiKey = request.args.get('api_key')

    # checking if api key is valid 🤣🤣🤣
    if apiKey != "ThisIsASecretKeyToDeleteCafe":
        return jsonify(error={
            "unauthorized": "api key passed is invalid."
        }), 403


    cafe = db.session.query(Cafe).get(cafeId)
    if cafe:
        db.session.delete(cafe) # deletes cafe from db
        db.session.commit()
        return jsonify(response={
            "response": "Successfully deleted the cafe."
        })
    else:
        return jsonify(error={
            "not found": "Sorry, a cafe with that id was not found."
        }), 404


if __name__ == '__main__':
    app.run(debug=True)
