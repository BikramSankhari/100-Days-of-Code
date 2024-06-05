from flask import Flask, render_template, request
import requests
import smtplib, ssl

MY_EMAIL = "popww619@gmail.com"
MY_PASSWORD = "vfyuqrhmwxtlsdwb"

app = Flask(__name__)
response = requests.get("https://api.npoint.io/688c13f15eb67026afb9")
all_blogs = response.json()


def send_mail(name, email, mob, msg):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, "bikram1209@gmail.com",
                            msg=f"Subject:New Message\n\nName: {name}\nEmail-ID: {email}\nContact No. - {mob}\nMessage: {msg}")


@app.route("/")
def home():
    return render_template("home.html", blogs=all_blogs)


@app.route("/<int:id>")
def post(id):
    selected_blog = {}
    for blog in all_blogs:
        if blog['id'] == id:
            selected_blog = blog
    return render_template("post.html", blog=selected_blog)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        send_mail(request.form['name'], request.form['email'], request.form['phone'], request.form['msg'])
        return "<h1>Successfully Sent Your Message</h1>"
    return render_template("contact.html")


app.run(debug=True)
