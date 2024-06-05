from turtle import  Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.setheading(180)
        self.shapesize(stretch_len=3)