from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, ValidationError
import re


class Form(FlaskForm):
    regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    email = EmailField(label="Email",
                       validators=[Email(message="Please Enter a Valid Email Address")])
    password = PasswordField(label="Password")
    submit = SubmitField(label="Submit")

    def validate_password(self, password):
        if re.match(self.regex, self.password.data) is None:
            raise ValidationError(
                "Password must contain an Uppercase Letter, a Lowercase Letter, a Number and a Special Character")

        if self.password.data != "Bikram@2000":
            raise ValidationError("Password Mismatch")

    def validate_email(self, email):
        if self.email.data != "admin@admin.com":
            raise ValidationError("Email Mismatch")


app = Flask(__name__)

app.secret_key = "Bikram"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Form()

    if request.method == "POST":
        if form.validate_on_submit():
            return render_template("success.html")

        return render_template("denied.html", form=form)

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
