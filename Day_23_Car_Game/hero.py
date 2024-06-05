from turtle import Turtle
STARTING_POSITION = (0, -280)


class Hero (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_left(self):
        self.goto(x=(self.xcor() - 20), y = self.ycor())

    def move_right(self):
        self.goto(x=(self.xcor() + 20), y = self.ycor())

    def move_up(self):
        self.goto(x=self.xcor(), y =(self.ycor() + 20))

    def move_down(self):
        self.goto(x=self.xcor(), y = (self.ycor() - 20))

    def reset_position(self):
        self.goto(STARTING_POSITION)
