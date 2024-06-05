from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from datetime import timedelta

login_manager = LoginManager()
app = Flask(__name__)

login_manager.init_app(app)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).first()
    if user is None:
        return None
    else:
        return user[0]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_provided_password = request.form["password"]
        secured_password = generate_password_hash(user_provided_password, method='pbkdf2', salt_length=500_000)
        new_user = User(email=request.form["email"],
                        password=secured_password,
                        name=request.form["name"],
                        )

        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, duration=timedelta(seconds=1))

        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form['email'])).first()

        if user is None:
            return render_template("login.html", user_found=False, from_post=True, password_mismatch=False)

        else:
            if check_password_hash(pwhash=user[0].password, password=request.form['password']):
                login_user(user[0], duration=timedelta(seconds=1))
                flash("Success")
                return redirect(url_for("secrets"))
            else:
                return render_template("login", user_found=True, from_post=True, password_mismatch=True)

    return render_template("login.html", from_post=False, user_found=False, password_mismatch=False)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@login_manager.unauthorized_handler
def unauthorized():
    return "<h1>Please Log In First</h1>"


@app.route('/download')
@login_required
def download():
    folder = os.path.join(app.root_path, "static/files")
    return send_from_directory(directory=folder, path="cheat_sheet.pdf", as_attachment=True,
                               download_name="Changed_name.pdf")


if __name__ == "__main__":
    app.run(debug=True)
