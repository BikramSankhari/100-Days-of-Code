import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

def change_pen_status():
    global timmy
    if timmy.isdown():
        timmy.penup()
    else:
        timmy.pendown()


timmy = Turtle()
timmy.shape("turtle")

def set_random_color():
    global timmy
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)

timmy.speed(0)
timmy.pen(resizemode="noresize", pensize=1)
for _ in range(int(360/5)):
    set_random_color()
    timmy.circle(100)
    timmy.left(5)

screen = Screen()
screen.screensize(400, 400)
screen.exitonclick()
