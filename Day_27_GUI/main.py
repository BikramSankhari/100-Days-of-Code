from tkinter import *
label_pad = 20

screen = Tk()
screen.title("Miles to KiloMeter Converter")
screen.config(padx=50, pady=50)


def focus_in(event):
    input.config(highlightcolor="SkyBlue", highlightthickness=2)


def focus_out(event):
    input.config(highlightthickness=0)


def calculate():
    m = int(input.get())
    answer.config(text=str(round(m * 1.6)))

input = Entry(width=10, font=("Arial", 20))
input.grid(row=0, column=1)
input.bind("<FocusIn>", focus_in)
input.bind("<FocusOut>", focus_out)

miles = Label(text="Miles",font=("Arial", 20), padx= label_pad)
miles.grid(row=0, column=2)

equal = Label(text="is equal to",font=("Arial", 20), padx= label_pad)
equal.grid(row=1, column=0)

answer = Label(text="0",font=("Arial", 20), padx= label_pad)
answer.grid(row=1,column=1)

km = Label(text="Km", font=("Arial", 20), padx= label_pad)
km.grid(row=1, column=2)

button = Button(text = "Calculate", font=("Arial", 20), command=calculate)
button.grid(row=2, column=1)



screen.mainloop()