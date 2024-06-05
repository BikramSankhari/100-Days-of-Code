from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.color('green')
            new_segment.penup()
            new_segment.goto(x, 0)
            x -= 20
            self.segments.append(new_segment)
        self.segments[0].shape('triangle')
        self.head = self.segments[0]

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_upwards(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_downwards(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move(self):
        for segment_index in range((len(self.segments) - 1), 0, -1):
            x = self.segments[segment_index - 1].xcor()
            y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(x, y)
        self.head.forward(20)

    def increase_length(self):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.segments.clear()
        self.create_snake()
