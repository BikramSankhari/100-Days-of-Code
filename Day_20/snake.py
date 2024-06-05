from turtle import Turtle, Screen
import time

class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen = Screen()
        self.screen.setup(height=600, width=600)
        self.screen.bgcolor("black")
        self.screen.title("Baburam Sapure")
        self.screen.tracer(0)
        self.screen.listen()

        self.turtles = []
        x_pos = 0
        for _ in range(3):
            self.turtles.append(Turtle(shape='square'))
            self.turtles[_].penup()
            self.turtles[_].color('white')
            self.turtles[_].goto(x=x_pos, y=0)
            x_pos -= 20

        self.screen.update()
        time.sleep(0.1)


    def move_forward(self):
        for turtl in self.turtles:
            turtl.forward(20)
        self.screen.update()
        time.sleep(0.1)


    def turn_right(self):
        self.turtles[0].right(90)
        self.turtles[0].forward(2 * 20)

        self.turtles[1].forward(20)
        self.turtles[1].right(90)
        self.turtles[1].forward(20)

        self.turtles[2].forward(2 * 20)
        self.turtles[2].right(90)

        self.screen.update()
        time.sleep(0.1)


    def turn_left(self):
        self.turtles[0].left(90)
        self.turtles[0].forward(2 * 20)

        self.turtles[1].forward(20)
        self.turtles[1].left(90)
        self.turtles[1].forward(20)

        self.turtles[2].forward(2 * 20)
        self.turtles[2].left(90)

        self.screen.update()
        time.sleep(0.1)


    def move_backward(self):
        for turtl in self.turtles:
            turtl.backward(20)
        self.screen.update()
        time.sleep(0.1)

    def right_key(self):
        while True:
            if self.turtles[0].heading() == 0:  # Heading Right
                self.move_forward()

            elif self.turtles[0].heading() == 90:  # Heading Upward
                self.turn_right()

            elif self.turtles[0].heading() == 180:  # Heading Left
                self.move_backward()

            else:  # Heading Downwards
                self.turn_left()

    def up_key(self):
        while True:
            if self.turtles[0].heading() == 0:  # Heading Right
                self.turn_left()

            elif self.turtles[0].heading() == 90:  # Heading Upwardself.
                self.move_forward()

            elif self.turtles[0].heading() == 180:  # Heading Left
                self.turn_right()

            else:  # Heading Downwards
                self.move_backward()

    def down_key(self):
        while True:
            if self.turtles[0].heading() == 0:  # Heading Right
                self.turn_right()

            elif self.turtles[0].heading() == 90:  # Heading Upward
                self.move_backward()

            elif self.turtles[0].heading() == 180:  # Heading Left
                self.turn_left()

            else:  # Heading Downwards
                self.move_forward()

    def left_key(self):
        while True:
            if self.turtles[0].heading() == 0:  # Heading Right
                self.move_backward()

            elif self.turtles[0].heading() == 90:  # Heading Upward
                self.turn_left()

            elif self.turtles[0].heading() == 180:  # Heading Left
                self.move_forward()

            else:  # Heading Downwards
                self.turn_right()

    def move(self):
        self.screen.onkey(key='Right', fun=self.right_key)
        self.screen.onkey(key='Left', fun=self.left_key)
        self.screen.onkey(key='Up', fun=self.up_key)
        self.screen.onkey(key='Down', fun=self.down_key)
