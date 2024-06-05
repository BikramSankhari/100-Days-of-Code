from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bf9ac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
LAP = 0
after = NONE
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    screen.after_cancel(after)
    canvas.itemconfig(time, text="00:00")
    timer_label.config(text="TIMER")
    cycle_count.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def count_down(minute, second):
    global after
    text = '{:02}'.format(minute) + ":" + '{:02}'.format(second)
    canvas.itemconfig(time, text=text)
    if minute > 0 or second > 0:
        if second == 0:
            minute -= 1
            second = 59
        else:
            second -= 1
        after = screen.after(1000, count_down, minute, second)

    else:
        screen.after(1000, start_timer)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_timer():
    global LAP
    LAP += 1
    print(LAP)

    if LAP % 8 == 0:
        timer_label.config(text="Long Break")
        cycle_count.config(text="")
        count_down(20, 0)

    elif LAP % 2 == 0:
        timer_label.config(text="Short Break")
        count_down(5, 0)

    else:
        timer_label.config(text="Work")
        cycle_count.config(text=cycle_count["text"] + "✔")
        count_down(25, 0)



# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Technique")
screen.config(padx=100, pady=50, bg = YELLOW)

# Timer Label
timer_label = Label(text="TIMER", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Tomato
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="Day_28_Pomodoro_Technique/tomato.png")
canvas.create_image(105, 112, image=image)
time = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="START", command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="RESET", command=reset)
reset_button.grid(row=2, column=2)

# Cycle Count
cycle_count = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
cycle_count.grid(row=3, column=1)



screen.mainloop()