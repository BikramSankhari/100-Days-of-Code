from flask import Flask, render_template
import pandas
from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField(label="Cafe Name :", validators=[DataRequired()])
    location = StringField(label="Cafe Location on Google Maps (URL) :", validators=[DataRequired()])
    o_time = StringField(label="Opening Time e.g. 8 AM :", validators=[DataRequired()])
    c_time = StringField(label="Closing Time e.g. 5 PM :", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating :",
                                choices=[(1, "☕︎"), (2, "☕︎☕︎"), (3, "☕︎☕︎☕︎"), (4, "☕︎☕︎☕︎☕︎"), (5, "☕︎☕︎☕︎☕︎☕︎")],
                                validators=[DataRequired()])
    wifi_rating = SelectField(label="Wifi Strength Rating :",
                              choices=[(1, "💪"), (2, "💪💪"), (3, "💪💪💪"), (4, "💪💪💪💪"), (5, "💪💪💪💪💪💪")],
                              validators=[DataRequired()])
    power_rating = SelectField(label="Power Socket Availability :",
                               choices=[(0, "✘"), (1, "🔌"), (2, "🔌🔌"), (3, "🔌🔌🔌"), (4, "🔌🔌🔌🔌"), (5, "🔌🔌🔌🔌🔌")],
                               validators=[DataRequired()])
    submit = SubmitField(label="Add Cafe", validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = "Bikram"

data = pandas.read_csv("./static/data.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cafes")
def cafes():
    global data
    return render_template("cafes.html", table=data)


@app.route("/add", methods=["GET", "POST"])
def add():
    global data
    form = AddForm()
    if form.validate_on_submit():
        data.loc[len(data.index)] = [form.name.data,
                                     form.location.data,
                                     form.o_time.data,
                                     form.c_time.data,
                                     int(form.coffee_rating.data),
                                     int(form.wifi_rating.data),
                                     int(form.power_rating.data)]
        data.to_csv("./static/data.csv")
        return render_template("cafes.html", table=data)
    return render_template("add.html", form=form)


app.run(debug=True)
