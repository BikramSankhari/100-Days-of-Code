from turtle import Turtle


class Line:
    def __init__(self):
        self.line = Turtle()
        self.line.color('white')
        self.line.penup()
        self.line.pensize(5)
        self.line.goto(x=0, y=-300)
        self.line.setheading(90)

        while self.line.ycor() < 300:
            self.line.forward(15)

            if self.line.pen()["pendown"]:
                self.line.penup()
            else:
                self.line.pendown()

        self.line.hideturtle()
