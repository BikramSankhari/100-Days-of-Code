from turtle import Turtle
import random


class Ball:
    def __init__(self):
        self.ball = Turtle(shape='turtle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.speed(7)
        self.ball.setheading(random.randint(-30, 30))

    def move(self):
        self.ball.forward(20)

    def bounce_sideways(self):
        self.ball.setheading(180 - self.ball.heading())

    def bounce_updown(self):
        self.ball.setheading(0 - self.ball.heading())

    def refresh(self):
        self.ball.goto(0, 0)
        self.ball.setheading(random.randint(-30, 30))

