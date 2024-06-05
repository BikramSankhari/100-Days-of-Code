import random
from flask import Flask

app = Flask(__name__)

a = 5


@app.route('/')
def hello_world():
    global a
    return f"Hello, World! {a}"


@app.route("/<int:num>")
def myFun(num):
    return f"Number {num + 1}"


@app.route("/bye")
def bye():
    return "Bye"


app.run(debug=True)
