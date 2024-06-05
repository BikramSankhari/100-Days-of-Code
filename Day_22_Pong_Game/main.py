from turtle import Screen
from ball import Ball
from line import Line
from left_player import LeftPlayer
from right_player import RightPlayer
import time

WINNING_SCORE = 10

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

p1 = LeftPlayer()
p2 = RightPlayer()
ball = Ball()
line = Line()

while True:
    screen.onkey(key="w", fun=p1.plate.move_up)
    screen.onkey(key="s", fun=p1.plate.move_down)
    screen.onkey(key="Up", fun=p2.plate.move_up)
    screen.onkey(key="Down", fun=p2.plate.move_down)
    ball.move()

    if ball.ball.ycor() > 270 or ball.ball.ycor() < -270:
        ball.bounce_updown()

    if ball.ball.xcor() > 380:
        ball.refresh()
        p1.score_board.update()

    if ball.ball.xcor() < -380:
        ball.refresh()
        p2.score_board.update()

    if p1.score_board.point == WINNING_SCORE:
        print("P1 Won!")
        break

    if p2.score_board.point == WINNING_SCORE:
        print("P2 Won!")
        break

    for segment in p1.plate.segments:
        if segment.distance(ball.ball) < 40 and p1.plate.segments[0].ycor() - 10 <= ball.ball.ycor() <= \
                p1.plate.segments[
                    2].ycor() + 20:
            ball.bounce_sideways()
            break

    for segment in p2.plate.segments:
        if segment.distance(ball.ball) < 30 and p2.plate.segments[0].ycor() - 10 <= ball.ball.ycor() <= \
                p2.plate.segments[
                    2].ycor() + 20:
            ball.bounce_sideways()
            break

    screen.update()
    time.sleep(0.07)

screen.exitonclick()
