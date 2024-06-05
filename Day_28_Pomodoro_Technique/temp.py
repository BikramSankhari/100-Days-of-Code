from tkinter import *

REP = 0
counter = NONE


def reset():
    screen.after_cancel(counter)
    canvas.itemconfig(time, text="00:00")
    heading.config(text="TIMER", font=("Times New Roman", 45, 'bold'), fg = "#B2A4FF")


def count_down(minute, second):
    text = '{:02}'.format(minute) + ":" + '{:02}'.format(second)
    canvas.itemconfig(time, text=text)
    if minute > 0 or second > 0:
        if second == 0:
            minute -= 1
            second = 59
        else:
            second -= 1

        global counter
        counter = screen.after(1000, count_down, minute, second)

    else:
        screen.after(1000, start_timer)


def start():
    global REP
    REP = 0
    start_timer()


def start_timer():
    global REP
    REP += 1
    screen.after_cancel(counter)

    if REP % 8 == 0:
        heading.config(text="BREAK", fg = "#9A208C")
        count_down(0, 4)

    elif REP % 2 == 0:
        heading.config(text="BREAK", fg="#9A208C")
        count_down(0, 2)

    else:
        heading.config(text="WORK", fg="#0B2447")
        count_down(0, 5)


screen = Tk()
screen.minsize(height=500, width=500)
screen.config(padx=100, pady=100, bg="#F9E2AF")
screen.title("Pomodoro")

heading = Label(text="TIMER", font=("Times New Roman", 45, 'bold'), fg = "#B2A4FF", bg="#F9E2AF", highlightthickness=0)
heading.grid(row=0, column=1)

canvas = Canvas(height=230, width=220, bg="#F9E2AF", highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(110, 116, image=tomato)
time = canvas.create_text(110, 130, text="00:00", font=("Arial", 30, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text="START",pady=5, padx=20, bg="#27E1C1", highlightthickness=0, fg='black', font=("Arial", 10), command=start)
start.grid(row=2, column=0)

reset = Button(text="RESET",pady=5, padx=20, bg="#27E1C1", highlightthickness=0, fg='black', font=("Arial", 10), command=reset)
reset.grid(row=2, column=2)







screen.mainloop()