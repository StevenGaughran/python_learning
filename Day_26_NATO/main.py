# Day 26, using List and Dictionary comprehension.
# The lessons were a breeze until the final exercise, which frankly # left me stumped. I'm not sure why we had to dump
# the DataFrame into a dictionary, but likewise I'm not sure how # to access the data from the DataFrame in any case.
# This whole thing was a nightmare from start to finish, and I am very confused.

# My first method was to break the user input into individual letters using the following comprehension code:
#   example = [letter for letter in input("What is your name?").upper()]
# Which I thought was pretty slick, but I couldn't figure out how to replace the letters from those in the
# Data Frame.

# Oh well. Tomorrow is another lesson, I guess.

import pandas

#TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}

nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_name = input("What is your name?").upper()
output = [nato_dict[letter] for letter in user_name]

print(output)
