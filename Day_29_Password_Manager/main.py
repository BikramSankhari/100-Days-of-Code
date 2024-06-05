from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

LOWER_CASE_LETTERS = list(string.ascii_lowercase)
UPPER_CASE_LETTERS = list(string.ascii_uppercase)
SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', "*"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def generate():
    password_entry.delete(0, END)
    passkey = []

    for _ in range(random.randint(6,7)):
        passkey.append(random.choice(LOWER_CASE_LETTERS))

    for _ in range(random.randint(6,7)):
        passkey.append(random.choice(UPPER_CASE_LETTERS))

    for _ in range(random.randint(3,4)):
        passkey.append(random.choice(SPECIAL_CHARACTERS))

    for _ in range(random.randint(1,2)):
        passkey.append(str(random.choice(NUMBERS)))

    random.shuffle(passkey)

    pass_word = "".join(passkey)
    pyperclip.copy(pass_word)
    password_entry.insert(0, pass_word)


def add():
    if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title="Oops", message="Please fill all the Entries")

    else:
        save = messagebox.askokcancel(title="Confirmation!", message="Do You Want to Save the Details?")

        if save:
            with open("Day_29_Password_Manager/data.txt", "a") as file:
                text = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
                file.write(text)
            messagebox.showinfo(title="Done!", message="Records Saved Successfully!")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


screen = Tk()
screen.title("Password Manager")
screen.config(pady=20, padx=20)

canvas = Canvas(height=200, width=150)
image = PhotoImage(file="Day_29_Password_Manager/logo.png")
canvas.create_image(70, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "popww619@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')

password = Label(text="Password", pady=2)
password.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

generate_password = Button(text="Generate Password", command=generate)
generate_password.grid(row=3, column=2, sticky='w')

add = Button(text="Add", width=36, command=add)
add.grid(row=4, column=1, columnspan=2, sticky='w')

screen.mainloop()
