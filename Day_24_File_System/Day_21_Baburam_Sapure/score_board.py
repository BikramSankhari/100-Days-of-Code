from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.score = -1
        with open("High Score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 30, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High Score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.increase_score()
