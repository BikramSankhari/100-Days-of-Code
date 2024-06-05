from turtle import Turtle, Screen
import random

colors = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
screen = Screen()
screen.screensize(canvwidth= 600, canvheight= 500)
screen.title("Welcome to the Turtle Race")
turtle = []
y_pos = -100

user_choice = screen.textinput(title="Make Your Bet", prompt="Which turtle will win")
winner = 0
for _ in range(6):
    turtle.append(Turtle(shape='turtle'))
    turtle[_].color(colors[_])
    turtle[_].penup()
    turtle[_].speed(3)
    turtle[_].goto(-250, y_pos)
    y_pos += 50


match_finished = False
while not match_finished:
    for _ in range(6):
        turtle[_].speed(random.randint(0, 8))
        turtle[_].forward(random.randint(0, 10))
        if turtle[_].position()[0] > 230:
            winner = _
            match_finished = True
            break

screen.exitonclick()
if colors[winner] == user_choice:
    print("Your Turtle won")

else:
    print(f"You lose. The {colors[winner]} turtle is the winner")

