from turtle import Turtle, Screen
import pandas
import time

turtle = Turtle()
screen = Screen()
screen.bgpic("blank_states_img.gif")

turtle.penup()
turtle.hideturtle()

data_file = pandas.read_csv("50_states.csv")
all_states = data_file.state.to_list()

guessed_states = []
score = 0
while not score == 50:
    name = screen.textinput(f"Score: {score}/50", "Enter name of a State: (Enter Quit to Exit)").title()

    if name == "Quit":
        print(f"Your Final Score is {score}")
        time.sleep(1)
        screen.bye()
        break

    elif name in data_file.state.values:
        x_cor = data_file[data_file.state == name].x.item()
        y_cor = data_file[data_file.state == name].y.item()

        turtle.goto(x=x_cor, y=y_cor)
        turtle.write(name, align="center", font=('Arial', 8, 'normal'))
        score += 1
        guessed_states.append(name)

if score == 50:
    print("You Guessed them all Right. Congratulations!")
    time.sleep(1)
    screen.bye()

missing_states = [state for state in all_states if state not in guessed_states]
final_data = {
    "Missed States": missing_states
}

file = pandas.DataFrame(final_data)
file.to_csv("Missing_States.csv")
