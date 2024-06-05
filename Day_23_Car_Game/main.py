from turtle import Screen, Turtle
from hero import Hero
from random_cars import RandomCars
import time
from score_board import ScoreBoard

REFRESH_RATE = 0.1


def draw_line():
    while turtle.xcor() <= 300:
        turtle.forward(10)

        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()


# Initialising the Screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

# Drawing Starting and Finishing Lines
turtle = Turtle()
turtle.penup()
turtle.color('white')
turtle.goto(x=-300, y=-260)
draw_line()

turtle.penup()
turtle.goto(x=-300, y=267)
draw_line()

# Initialising Objects
banti = Hero()
objects = RandomCars()
screen.update()
score_board = ScoreBoard()

screen.onkey(fun=banti.move_up, key="Up")
screen.onkey(fun=banti.move_down, key="Down")
screen.onkey(fun=banti.move_left, key="Left")
screen.onkey(fun=banti.move_right, key="Right")

gamis_over = False
while not gamis_over:
    objects.move()

    for car in objects.random_cars:
        if abs(car.xcor() - banti.xcor()) < 40 and abs(car.ycor() - banti.ycor()) < 20:
            score_board.game_over()
            gamis_over = True

    if banti.ycor() > 267:
        score_board.update_score()
        banti.reset_position()
        objects.reset()
        REFRESH_RATE *= 0.7

    time.sleep(REFRESH_RATE)
    screen.update()

screen.exitonclick()
