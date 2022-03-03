# Day 29. A password manager.
# This took longer than it should have because I was looking at exporting the Entry fields incorrectly.
# Once I figured that out, the rest kinda fell into place.
# The spacing of the GUI is slightly off, but I couldn't figure it out and decided it was GOOD ENOUGH.
# I'm certain that there is a cleaner way to generate a 12-digit password, but I'm happy with what I've come up with.

from tkinter import *
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pw_choices = string.ascii_letters + string.digits + string.punctuation
    pw_choices.split()
    password = random.sample(pw_choices, 12)
    pw = ''.join(password)
    return password_field.insert(index=0, string=pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("./data.txt", mode="a") as file:
        file.write(f"{website_input.get()} | {email_input.get()} | {password_field.get()} \n")
    password_field.delete(0, END)
    website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="./logo.png")
canvas.create_image(75, 100, image=logo)
canvas.grid(column=1, row=0, padx=20, pady=20)


# Labels-------------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, padx=5)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, padx=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, padx=5)


# Fields-------------
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2, sticky=W, padx=5)
website_input.focus()

email_input = Entry(width=39)
email_input.insert(index=0, string="iheartnickelback@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky=W, padx=5)

password_field = Entry(width=19)
password_field.grid(column=1, row=3, sticky=W, padx=5)


# Buttons-------------
generate_password = Button(text="Generate Password", width=14, command=generate_password)
generate_password.grid(column=1, row=3, sticky=E, padx=5)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=W, padx=5)


window.mainloop()
