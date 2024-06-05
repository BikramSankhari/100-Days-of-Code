from turtle import Turtle


class Plate:
    def __init__(self, x_cor):
        self.segments = []
        y_cor = -40
        for _ in range(4):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x=x_cor, y=y_cor)
            self.segments.append(new_segment)
            y_cor += 20

    def move_up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(20)

    def move_down(self):
        for segment in self.segments:
            segment.setheading(270)
            segment.forward(40)
