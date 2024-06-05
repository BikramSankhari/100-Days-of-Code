from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.title("BABURAM SAPURE")
screen.listen()
screen.tracer(0)
screen.setup(width=600, height=600)

sapu = Snake()
food = Food()
score_board = ScoreBoard()
screen.update()

screen.onkey(key="Right", fun=sapu.turn_right)
screen.onkey(key="Left", fun=sapu.turn_left)
screen.onkey(key="Up", fun=sapu.turn_upwards)
screen.onkey(key="Down", fun=sapu.turn_downwards)

gamis_on = True
while gamis_on:
    sapu.move()
    screen.update()
    time.sleep(0.1)

    if sapu.head.distance(food) < 15:
        food.refresh()
        sapu.increase_length()
        score_board.increase_score()

    if sapu.head.xcor() > 270 or sapu.head.xcor() < -270 or sapu.head.ycor() > 270 or sapu.head.ycor() < -270:
        gamis_on = False
        score_board.goto(0, 0)
        sapu.head.color('red')
        score_board.write("Game Over", align='center', font=('Arial', 30, 'normal'))

    for segment in sapu.segments[1:]:
        if sapu.head.distance(segment) < 10:
            gamis_on = False
            sapu.head.color('red')
            score_board.goto(0, 0)
            score_board.write("Game Over", align='center', font=('Arial', 30, 'normal'))


screen.exitonclick()
