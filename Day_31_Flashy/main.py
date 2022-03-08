from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ~~~~ Variables ~~~~
to_learn = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
data = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")

word = {}


# ~~~~ Mechanics ~~~~


def get_word():
    global word, flip_timer
    try:
        window.after_cancel(flip_timer)
        word = random.choice(to_learn)
        canvas.itemconfig(flashcard_background, image=flashcard_front)
        canvas.itemconfig(title_label, text="French", fill="#000000")
        canvas.itemconfig(word_label, text=word["French"], fill="#000000")
        flip_timer = window.after(3000, func=flip_card)
    except IndexError:
        window.after_cancel(flip_timer)
        word = random.choice(data)
        canvas.itemconfig(flashcard_background, image=flashcard_front)
        canvas.itemconfig(title_label, text="French", fill="#000000")
        canvas.itemconfig(word_label, text=word["French"], fill="#000000")
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(flashcard_background, image=flashcard_back)
    canvas.itemconfig(title_label, text="English", fill="#FFFFFF")
    canvas.itemconfig(word_label, text=word["English"], fill="#FFFFFF")


def is_known():
    data.remove(word)
    known_words = pandas.DataFrame(data)
    known_words.to_csv("./data/words_to_learn.csv", index=False)
    get_word()


# ~~~~ UI ~~~~
window = Tk()
window.title("Flashy!")
window.config(width=800, height=500, padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_front = PhotoImage(file="./images/card_front.png")
flashcard_back = PhotoImage(file="./images/card_back.png")
flashcard_background = canvas.create_image(400, 250, image=flashcard_front)
canvas.grid(row=0, column=0, columnspan=2)

# ~~~~ 'Labels' (actually not technically labels but 'canvas.create_text' items) ~~~~
title_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# ~~~~ Buttons ~~~~
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=get_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=is_known)
right_button.grid(row=1, column=1)

# ~~~~ Activate! ~~~~
get_word()

window.mainloop()
