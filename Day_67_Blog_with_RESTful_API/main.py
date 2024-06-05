from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# with app.app_context():
#     db.create_all()

@app.route('/')
def get_all_posts():
    posts = db.session.scalars(db.select(BlogPost))
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.session.scalars(db.select(BlogPost).where(BlogPost.id == index)).first()
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_post(index):
    blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == index)).scalar_one()
    form = CreatePostForm(title=blog.title,
                          subtitle=blog.subtitle,
                          author=blog.author,
                          img_url=blog.img_url,
                          body=blog.body)

    # form = CreatePostForm(obj=blog)

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.author = form.author.data
        blog.img_url = form.img_url.data
        blog.body = form.body.data
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form, index=index)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(title=form.title.data,
                            subtitle=form.subtitle.data,
                            body=form.body.data,
                            author=form.author.data,
                            img_url=form.img_url.data,
                            date=date.today().strftime("%B %d,%Y"))
        with app.app_context():
            db.session.add(new_post)
            db.session.commit()

        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, index=0)


@app.route("/delete/<int:id>")
def delete(id):
    blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == id)).scalar_one()

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(debug=True)
