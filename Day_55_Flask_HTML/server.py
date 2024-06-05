import random

from flask import Flask

app = Flask(__name__)

r = random.randint(0, 10)

color = ["red", "blue", "green", "purple", "orange"]
high_image = [
    "https://media0.giphy.com/media/kGdTMHRwIBhD6VOe6y/200w.webp?cid=ecf05e47x3hivfnrjt0xv36y1tcb7lr0bpre3kohh1z3r6ds&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media2.giphy.com/media/TiuShTf3ehYZi/200w.webp?cid=ecf05e47x3hivfnrjt0xv36y1tcb7lr0bpre3kohh1z3r6ds&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media2.giphy.com/media/KfTsEf7OXeRsIsfPzo/200w.webp?cid=ecf05e47x3hivfnrjt0xv36y1tcb7lr0bpre3kohh1z3r6ds&ep=v1_gifs_search&rid=200w.webp&ct=g"]

low_image = [
    "https://media4.giphy.com/media/WBVzCpHV2e64w/giphy.webp?cid=ecf05e47rx11keu3stlt1j8a33qup11w3k1dcmvar92h8o5n&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media1.giphy.com/media/26n6UOQke3xCpsbWo/200w.webp?cid=ecf05e47ulvcjq8x80q727z7vwujmwis10s0bjxd154ocmt5&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/rGznn87ld7o7S/200.webp?cid=ecf05e47k5m75m7xagsz23rku4tk6cwwej1bv3c6pia5j5m2&ep=v1_gifs_search&rid=200.webp&ct=g"]


@app.route("/")
def home():
    return '<h1>Guess a Number</h1><img src="https://media1.giphy.com/media/xT5LMMneIRG1UJquOI/giphy.gif?cid=ecf05e47ygcdmv28hxwt6s57nwxx1303ixe5wdp5zf7rskjh&ep=v1_gifs_search&rid=giphy.gif&ct=g" />'


@app.route("/<int:num>")
def net(num):
    if num == r:
        return f'<h1 style="color:{random.choice(color)};">You Found Me</h1><img src="https://media2.giphy.com/media/xT3JvPQibFu3C/giphy.webp?cid=ecf05e47umct0ofvp3hqs60wf0rhlzbtpbtg6ppsqo0fxo' \
               f'nt&ep=v1_gifs_search&rid=giphy.webp&ct=g" />'
    elif num > r:
        return f'<h1 style="color:{random.choice(color)};">Too High</h1><img src="{random.choice(high_image)}"' \
               f' width="500" height="500"/>'
    else:
        return f'<h1 style="color:{random.choice(color)};">Too Low</h1><img src="{random.choice(low_image)}"' \
               f' width="500" height="500"/>'


app.run(debug=True)
