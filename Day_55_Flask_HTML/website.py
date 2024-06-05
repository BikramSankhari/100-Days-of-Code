from flask import Flask

app = Flask(__name__)


def make_bold(fx):
    def inner():
        return f"<h1> {fx()} </h1>"

    return inner


@app.route("/")
@make_bold
def home():
    return "Hello World!"


app.run(debug=True)

def decorator(fx):
    def wrapper(**kwargs):
        if kwargs["name"] == "Banti":
            fx(name=kwargs["name"])
    return wrapper


@decorator
def show(name):
    print(name)


show(name="Bant")
