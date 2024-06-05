from turtle import Turtle

SCORE_BOARD_POSITION = (-190, 270)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(SCORE_BOARD_POSITION)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Current Score: {self.score}", align="center", font=('Bahnschrift', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Bahnschrift', 20, 'normal'))
