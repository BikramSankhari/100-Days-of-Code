from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db.init_app(app)


def search_movie(query: str):
    parameters = {
        "query": query,
        "api_key": "97e63ae2c23095143f6b1fe897d52ca2"

    }
    url = "https://api.themoviedb.org/3/search/movie"
    response = requests.get(url, params=parameters)
    try:
        return response.json()["results"]
    except KeyError:
        print("Invalid API Key")
        return None


class UpdateForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 8.7")
    review = StringField(label="Your Review")
    update = SubmitField(label="Update")


class AddForm(FlaskForm):
    query = StringField(label="Enter The Movie to Search")
    search = SubmitField(label="Search")


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.FLOAT)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


# with app.app_context():
#     db.create_all()

# new_movie = Movies(title="Phone Booth", year=2002,
#                    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
#                                "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's "
#                                "negotiation with the caller leads to a jaw-dropping climax.",
#                    rating=7.3,
#                    ranking=10,
#                    review="My favourite character was the caller.",
#                    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")


# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    results = db.session.scalars(db.select(Movies).order_by(Movies.rating.desc()))
    return render_template("index.html", movies=results)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = UpdateForm()
    if request.method == "POST":
        if form.validate_on_submit():
            movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar_one()
            if form.rating.data != "":
                movie.rating = form.rating.data

            if form.review.data != "":
                movie.review = form.review.data

            db.session.commit()

            return redirect(url_for("home"))

    return render_template("edit.html", form=form, id=id)


@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar_one()
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if request.method == "POST":
        if form.validate_on_submit():
            movies_list = search_movie(form.query.data)
            return render_template("select.html", movies=movies_list)
    return render_template("add.html", form=form)


@app.route("/insert/<int:id>")
def insert(id):
    url = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(url, params={"api_key": "97e63ae2c23095143f6b1fe897d52ca2"})
    response.raise_for_status()
    movie = response.json()
    if movie['release_date'] != "":
        year = int(movie['release_date'].split("-")[0])
    else:
        year = -1
    rank = float("{:.1f}".format(movie["popularity"]))
    if movie["poster_path"] is not None and movie["poster_path"] != "":
        img = f"https://image.tmdb.org/t/p/original{movie['poster_path']}"
    else:
        img = None

    new_movie = Movies(title=movie["original_title"],
                       year=year,
                       description=movie["overview"],
                       rating=None,
                       ranking=rank,
                       review=None,
                       img_url=img)

    with app.app_context():
        db.session.add(new_movie)
        db.session.flush()
        pk = new_movie.id
        db.session.commit()

    return redirect(url_for("update", id=pk))


if __name__ == '__main__':
    app.run(debug=True)
