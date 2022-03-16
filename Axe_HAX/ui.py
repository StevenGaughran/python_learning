from tkinter import *
import random
import axe_data
from axe_quotes import quotes
import axe_brain


class UI:
    def __init__(self):
        self.window = Tk()

        self.window.title("AXE HAX!")
        self.window.config(pady=30, padx=25, background="black")

        self.title_label = Label(text="Axe Hax!", font=("Courier", 30, "bold"), bg="black", fg="red")
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=246, height=140, bg="black")
        self.axe_img = PhotoImage(file="./images/axe_portrait.gif")
        self.canvas.create_image(123, 70, image=self.axe_img)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.welcome_label = Label(text=random.choice(quotes),
                                   font=("Courier", 10, "italic"), bg="black", fg="red", pady=10)
        self.welcome_label.grid(row=2, column=0, columnspan=2)

        self.casual = Label(text="Casual win rate: ",
                            font=("Courier", 10, "bold"), bg="black", fg="red", anchor="w")
        self.casual.grid(row=3, column=0)

        self.casual_wr = Label(text=f"{axe_brain.axe_win_rate_casual(axe_data.stats)}%",
                               font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
        self.casual_wr.grid(row=3, column=1)

        self.pro = Label(text="Professional win rate: ",
                         font=("Courier", 10, "bold"), bg="black", fg="red", anchor="w")
        self.pro.grid(row=4, column=0)

        self.pro_wr = Label(text=f"{axe_brain.axe_win_rate_pro(axe_data.stats)}%",
                            font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
        self.pro_wr.grid(row=4, column=1)

        self.window.mainloop()
