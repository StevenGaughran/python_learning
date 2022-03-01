from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=295, height=100)
window.config(padx=20, pady=20)


def convert():
    entry = float(number_box.get())
    number = round(entry*1.6)
    answer_label.config(text=number)


number_box = Entry()
number_box.config(width=5)
number_box.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)


window.mainloop()
