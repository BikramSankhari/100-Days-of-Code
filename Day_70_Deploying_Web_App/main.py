from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.exc import IntegrityError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegistrationForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from typing import List
import ssl, smtplib, os
from dotenv import load_dotenv

load_dotenv(os.path.abspath("/etc/secrets/secret.env"))

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)
Bootstrap(app)
login_manager.init_app(app)

# CONNECT TO DB
sql_string = "postgresql+psycopg2://blog_database_w1oy_user:cpoN8qBNFTvQFEiqOExcsk5d6D6kQx4R@dpg-cibm1faip7vnjjnrojkg-a.singapore-postgres.render.com/blog_database_w1oy"
app.config['SQLALCHEMY_DATABASE_URI'] = sql_string
db = SQLAlchemy(app)


# CONFIGURE TABLES

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey("user_table.id"))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    author: Mapped["User"] = relationship(back_populates="user_blog")
    blog_comment: Mapped[List["Comments"]] = relationship(back_populates="comment_blog")


class User(db.Model, UserMixin):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    user_blog: Mapped[List["BlogPost"]] = relationship(back_populates="author")
    user_comment: Mapped[List["Comments"]] = relationship(back_populates="user")


class Comments(db.Model):
    __tablename__ = "comment_table"
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    user_id = db.Column(db.ForeignKey("user_table.id"))
    blog_id = db.Column(db.ForeignKey("blog_posts.id"))

    user: Mapped["User"] = relationship(back_populates="user_comment")
    comment_blog: Mapped["BlogPost"] = relationship(back_populates="blog_comment")


with app.app_context():
    db.create_all()


def send_mail_to_user(email):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mail:
        mail.login(os.getenv("MY_EMAIL"), os.getenv("MY_PASSWORD"))
        mail.sendmail(os.getenv("MY_EMAIL"), email, msg=f"Subject:THANKS FOR YOUR INTEREST\n\nYour message has been "
                                                        f"received and you will be attended shortly")


def send_mail_to_self(name, email, mob, msg):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mail:
        mail.login(os.getenv("MY_EMAIL"), os.getenv("MY_PASSWORD"))
        mail.sendmail(os.getenv("MY_EMAIL"), os.getenv("MY_EMAIL"),
                      msg=f"Subject:NEW INTEREST\n\nName: {name}\nE-mail: {email}\nMob: {mob}\nMessage = {msg}")


@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).first()
    if user is None:
        return None
    else:
        return user[0]


@login_manager.unauthorized_handler
def unauthorized():
    return "<h1>Please Log In First</h1>"


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost, User.name).join_from(BlogPost, User))
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_active:
        logout_user()

    form = RegistrationForm()
    if form.validate_on_submit():
        user_entered_password = form.password.data
        secured_password = generate_password_hash(user_entered_password, method="pbkdf2:sha256", salt_length=500_000)

        new_user = User(name=form.name.data,
                        email=form.email.data,
                        password=secured_password,
                        )

        with app.app_context():
            db.session.add(new_user)
            try:
                db.session.commit()
            except IntegrityError:
                flash("You have already signed up. Please enter your password to login")
                return redirect(url_for("login"))
            else:
                login_user(new_user)

        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_active:
        return "You are already logged in"
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).first()

        if user is None:
            flash("Please Sign up to continue")
            return redirect(url_for("register"))

        else:
            if check_password_hash(pwhash=user[0].password, password=form.password.data):
                login_user(user[0])
                return redirect(url_for("get_all_posts"))
            else:
                flash("Wrong Password")
                return redirect(url_for("login"))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comments(comment=form.comment.data,
                               user_id=current_user.id,
                               blog_id=post_id)

        with app.app_context():
            db.session.add(new_comment)
            db.session.commit()

        return redirect(url_for("show_post", post_id=post_id))

    post = db.session.execute(
        db.select(BlogPost, User.name).join_from(User, BlogPost).where(BlogPost.id == post_id)).first()

    comments = db.session.execute(
        db.select(Comments.comment, User.name, User.email).join_from(Comments, User).where(Comments.blog_id == post_id))

    return render_template("post.html", post=post, comments=comments, form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        mob = request.form.get("phone")
        msg = request.form.get("msg")

        send_mail_to_user(email)
        send_mail_to_self(name=name, email=email, mob=mob, msg=msg)

        return redirect(url_for("get_all_posts"))
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    if current_user.id != post.author_id:
        return "You are Unauthorised"
    else:
        edit_form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        if edit_form.validate_on_submit():
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data
            post.body = edit_form.body.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))

        return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    if current_user.id != 1:
        return "You are Unauthorised"
    else:
        post_to_delete = BlogPost.query.get(post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
