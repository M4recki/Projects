from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

city = "Hackney"

# Cafe TABLE Configuration


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

    def to_dict(self):
        # Method 1.
        # dictionary = {}
        # Loop through each column in the data record

        # for column in self.__table__.columns:
        # Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.

        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def cafe():
    cafes = Cafe.query.all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    loc = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=loc).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["GET", "POST"])
def add():
    new_cafe = Cafe(name=request.form.get("name"),
    map_url = request.form.get("map_url"),
    img_url = request.form.get("img_url"),
    location = request.form.get("location"),
    seats = request.form.get("seats"),
    has_sockets=bool(request.form.get("sockets")),
    has_toilet=bool(request.form.get("toilet")),
    has_wifi=bool(request.form.get("wifi")),
    can_take_calls = bool(request.form.get("calls")),
    coffee_price=request.form.get("coffee_price")
    )
    
    db.session.add(new_cafe)
    db.session.commit()
    
    return jsonify(response={"Success": "Successfully added the new cafe."})

@app.route("/update/<id>", methods=["PATCH"])
def update(id):
    cafe = Cafe.query.get(id)
    
    if not cafe:
        return jsonify(error={"Not Found": "That cafe hasn't been found in database."})
    new_price = request.form.get("coffee_price")
    if new_price:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the price of coffee"})
    else:
        return jsonify({"Bad Request": "Please provide a new coffee price."})

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    cafe = Cafe.query.get(id)
    
    if not cafe:
        return jsonify(error={"Not Found": "That cafe hasn't been found in database."})
    secret_key = request.args.get("secret_key")
    if secret_key == "123":
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"Success": "Successfully deleted the requested cafe"})
    else:
        return jsonify(error={"Bad Request": "Please provide a valid key for deleting."})
        


if __name__ == '__main__':
    app.run(debug=True)
