from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def rand():
    result = db.session.scalars(db.select(Cafe).order_by(db.func.random())).first()

    response = {
        "cafe": {
            "can_take_calls": result.can_take_calls,
            "coffee_price": result.coffee_price,
            "has_sockets": result.has_sockets,
            "has_wifi": result.has_wifi,
            "id": result.id,
            "img_url": result.img_url,
            "location": result.location,
            "map_url": result.map_url,
            "name": result.name,
            "seats": result.seats
        }
    }

    return jsonify(response)


@app.route("/all")
def all():
    results = db.session.scalars(db.select(Cafe))
    out = []
    for result in results:
        out.append(result.to_dict())

    return jsonify(out)


@app.route("/search")
def search():
    location = request.args.get("loc")
    results = db.session.execute(db.select(Cafe).where(Cafe.location == location)).all()

    if results:
        dick = []
        for result in results:
            dick.append(result[0].to_dict())
        return jsonify(dick)
    return jsonify({"error": "No Cafe Found at this Location"})


# HTTP POST - Create Record
@app.route("/post", methods=["POST"])
def post():
    data = request.get_json()

    name = data["name"]
    map_url = data["map_url"]
    img_url = data["img_url"]
    location = data["location"]

    try:
        seats = int(data["seats"])
    except ValueError:
        return jsonify({"error": "seats parameter should be an integer"})

    try:
        has_toilet = bool(data["has_toilet"])
    except ValueError:
        return jsonify({"error": "has_toilet parameter should be a Boolean"})

    try:
        has_wifi = bool(data["has_wifi"])
    except ValueError:
        return jsonify({"error": "has_wifi parameter should be a Boolean"})

    try:
        has_sockets = bool(data["has_sockets"])
    except ValueError:
        return jsonify({"error": "has_sockets parameter should be a Boolean"})

    try:
        can_take_calls = bool(data["can_take_calls"])
    except ValueError:
        return jsonify({"error": "can_take_calls parameter should be a Boolean"})

    try:
        coffee_price = float(data["coffee_price"])
    except ValueError:
        return jsonify({"error": "coffee_price parameter should be a Float"})

    new_entry = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, seats=seats, has_toilet=has_toilet,
                     has_wifi=has_wifi, has_sockets=has_sockets, can_take_calls=can_take_calls,
                     coffee_price=coffee_price)

    with app.app_context():
        db.session.add(new_entry)
        db.session.commit()

    return jsonify({"Success": "Record entered Successfully"})


# HTTP PUT/PATCH - Update Record
@app.route("/patch", methods=["PATCH"])
def patch():
    header = request.headers
    data = request.get_json()

    try:
        result = db.session.scalars(db.select(Cafe).where(Cafe.id == header["id"])).first()

    except KeyError:
        return jsonify({"Error": "ID is required"})

    else:
        if result:
            try:
                result.name = data["name"]
            except KeyError:
                pass
            try:
                result.map_url = data["map_url"]
            except KeyError:
                pass
            try:
                result.img_url = data["img_url"]
            except KeyError:
                pass
            try:
                result.location = data["location"]
            except KeyError:
                pass
            try:
                result.seats = data["seats"]
            except KeyError:
                pass
            try:
                result.has_toilet = data["has_toilet"]
            except KeyError:
                pass
            try:
                result.has_wifi = data["has_wifi"]
            except KeyError:
                pass
            try:
                result.has_sockets = data["has_sockets"]
            except KeyError:
                pass
            try:
                result.can_take_calls = data["can_take_calls"]
            except KeyError:
                pass
            try:
                result.coffee_price = data["coffee_price"]
            except KeyError:
                pass
            db.session.commit()
            return jsonify({"Success": "Record updated Successfully"})

        return jsonify({"Error": "The ID doesn't exists"})


# HTTP DELETE - Delete Record
@app.route("/delete", methods=["DELETE"])
def delete():
    header = request.headers
    id = request.args.get("id")
    print(header)
    try:
        ak = header["api-key"]
    except KeyError:
        return jsonify({"Error": "An API KEY is required"})

    else:
        if ak == "Topa":
            if id:
                result = db.session.scalars(db.select(Cafe).where(Cafe.id == id)).first()

                if result:
                    db.session.delete(result)
                    db.session.commit()
                    return jsonify({"Success": "Record Deleted Successfully"})

                return jsonify({"Error": "No Cafe with this ID found"})

            return jsonify({"Error": "ID Parameter is required"})
        else:
            return jsonify({"Error": "Wrong API KEY"})


if __name__ == '__main__':
    app.run(debug=True)
