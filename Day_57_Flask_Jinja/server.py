from flask import Flask, render_template
import requests

app = Flask(__name__)

all_blogs = []


@app.route("/")
def home():
    global all_blogs
    response = requests.get("https://api.npoint.io/688c13f15eb67026afb9")
    all_blogs = response.json()
    return render_template("blog.html", blogs=all_blogs, len=len(all_blogs))


@app.route("/<int:id>")
def detail(id):
    selected_post = {}
    for blog in all_blogs:
        if blog["id"] == id:
            selected_post = blog
    return render_template("detailed_blog.html", post=selected_post)


app.run(debug=True)
