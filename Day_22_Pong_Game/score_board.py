from turtle import Turtle


class ScoreBoard:
    def __init__(self, position):
        self.point = -1
        self.score = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.score.color('white')
        self.score.goto(position)
        self.score.pendown()
        self.update()

    def update(self):
        self.point += 1;
        self.score.clear()
        self.score.write(self.point, align="center", font=('Bahnschrift', 70, 'normal'))
