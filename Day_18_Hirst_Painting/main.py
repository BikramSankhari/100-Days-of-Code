import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

maya = Turtle()
maya.speed(0)
position = -200

for _ in range(10):
    maya.penup()
    print(position)
    maya.goto(-300, position)
    maya.pendown()
    for _ in range(10):
        maya.dot(20, random.choice(colors))
        maya.penup()
        maya.forward(50)
        maya.pendown()
    position += 50








sc = Screen()
sc.screensize(800, 800)
sc.exitonclick()