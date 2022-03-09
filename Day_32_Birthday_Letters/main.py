# Day 32.
# The hardest part of this lesson was, once again, dictionaries and DataFrames. My problem was reading the "hint" the
# instructor gave for how to import and organize the CSV file, which was unnecessarily convoluted. Once I ignored that
# and figured out how to organize the dictionary properly, everything fell into place.
#
# ALL of the code below is my own and it works great, which feels nice after yesterday's catastrophe.
# I'm pretty sure I could organize the Letters better, but eh.

import smtplib
import random
import pandas
import datetime as dt

my_email = "EyeHeartNickelback@gmail.com"
password = "12345"
name = ""
now = dt.datetime.now()


# ~~~~ Setting up the letters ~~~~
letters = []
with open("./letter_templates/letter_1.txt", "r") as l1:
    letter_1 = l1.read()
    letters.append(letter_1)

with open("./letter_templates/letter_2.txt", "r") as l2:
    letter_2 = l2.read()
    letters.append(letter_2)

with open("./letter_templates/letter_3.txt", "r") as l3:
    letter_3 = str(l3.read())
    letters.append(letter_3)

selected_letter = random.choice(letters)


# ~~~~ Getting the Birthdays ~~~~
birthdays_dict = pandas.read_csv("./birthdays.csv").to_dict(orient="records")


# ~~~~ The Mechanics ~~~~
for f in birthdays_dict:
    if f["month"] == now.month and f["day"] == now.day:
        name = f["name"]
        send_email = f["email"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=send_email,
                msg="Subject:Happy Birthday!\n\n" + selected_letter.replace("[NAME]", name)
            )
