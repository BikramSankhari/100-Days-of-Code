from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, rating: {self.rating}, author: {self.author}"


# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    all_books = db.session.scalars(db.select(Books))
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Books(title=request.form["title"], rating=request.form["rating"], author=request.form["author"])
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    book = db.session.execute(db.select(Books).where(Books.id == id)).scalar_one()
    if request.method == "POST":
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", book=book)


@app.route("/delete/<int:id>")
def delete(id):
    book = db.session.execute(db.select(Books).where(Books.id == id)).scalar_one()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
