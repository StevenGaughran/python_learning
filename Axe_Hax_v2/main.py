from tkinter import *
import random
from axe_quotes import quotes
import axe_data
import axe_brain


# ~~~~ The GUI ~~~~
window = Tk()

window.title("AXE HAX!")
window.config(pady=30, padx=25, background="black")

title_label = Label(text="Axe Hax!", font=("Courier", 30, "bold"), bg="black", fg="red")
title_label.grid(row=0, column=0, columnspan=2)

canvas = Canvas(width=246, height=140, bg="black")
axe_img = PhotoImage(file="./images/axe_portrait.gif")
canvas.create_image(123, 70, image=axe_img)
canvas.grid(row=1, column=0, columnspan=2)

welcome_label = Label(text=random.choice(quotes),
                      font=("Courier", 10, "italic"), bg="black", fg="red", pady=10)
welcome_label.grid(row=2, column=0, columnspan=2)

casual = Label(text="Casual win rate: ",
               font=("Courier", 10, "bold"), bg="black", fg="red", anchor="w")
casual.grid(row=3, column=0)

casual_wr = Label(text=f"{axe_brain.axe_win_rate_casual(axe_data.stats())}%",
                  font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
casual_wr.grid(row=3, column=1)

pro = Label(text="Professional win rate: ",
            font=("Courier", 10, "bold"), bg="black", fg="red", anchor="w")
pro.grid(row=4, column=0)

pro_wr = Label(text=f"{axe_brain.axe_win_rate_pro(axe_data.stats())}%",
               font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
pro_wr.grid(row=4, column=1)

victim = Label(text="Favorite victim: ",
               font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
victim.grid(row=5, column=0)

victim_name = Label(text=f"{axe_brain.axe_victims(axe_data.matchups())}",
                    font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
victim_name.grid(row=5, column=1)

bully = Label(text="Bullied by: ",
              font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
bully.grid(row=6, column=0)

bully_name = Label(text=f"{axe_brain.axe_bully(axe_data.matchups())}",
                   font=("Courier", 10, "bold"), bg="black", fg="red", anchor="e")
bully_name.grid(row=6, column=1)

window.mainloop()
