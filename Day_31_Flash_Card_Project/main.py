from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

BACK = PhotoImage(file="Day_31_Flash_Card_Project/images/card_front.png")
FRONT = PhotoImage(file="Day_31_Flash_Card_Project/images/card_back.png")
AFTER = NONE
CANVAS = Canvas(bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)
image = CANVAS.create_image(400, 263, image=FRONT)
text = CANVAS.create_text(400, 263, text="word", font=("Verdana" ,50), fill='black')
text1 = CANVAS.create_text(400, 180, text='Title', font=("Arial", 30, 'italic'), fill='black')
CANVAS.grid(row=0, column=0, columnspan=2)
CARD = NONE
data = pandas.read_csv("Day_31_Flash_Card_Project/data/french_words.csv")
all_cards = [[data.French, data.English] for (index , data) in data.iterrows()]
known_cards = []


def right_click():
    global CARD, AFTER

    screen.after_cancel(AFTER)
    known_cards.append(CARD)
    new_card()


def new_card():
    global CANVAS, text, image,CARD, all_cards, known_cards, text1, AFTER
    try:
        CARD = random.choice([item for item in all_cards if item not in known_cards])
    except IndexError:
        messagebox.showinfo(message="You are an Expert", title="You Won!")
    else:
        image = CANVAS.create_image(400, 263, image=FRONT)
        text1 = CANVAS.create_text(400, 180, text='SPANISH', font=("Arial", 30, 'italic'), fill='white')
        text = CANVAS.create_text(400, 263, text=CARD[0], font=("Verdana", 50), fill='white')
        CANVAS.grid(row=0, column=0, columnspan=2)
        AFTER = screen.after(3000, change)


def change():
    global CANVAS, text, image
    CANVAS.itemconfig(text1, text="ENGLISH", fill='black')
    CANVAS.itemconfig(text, text=CARD[1], fill='black')
    CANVAS.itemconfig(image, image=BACK)


right_image = PhotoImage(file="Day_31_Flash_Card_Project/images/right.png")
wrong_image = PhotoImage(file="Day_31_Flash_Card_Project/images/wrong.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=right_click)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command= new_card)
wrong_button.grid(row=1, column=0)

screen.after(2000, new_card)

screen.mainloop()
