#A simple fortune telling game, similar to what kids make using paper.
#This took longer than I'd care to admit. I made it too fancy at first.

from turtle import color

import os
clear = lambda: os.system('cls')

color_list = ["red", "green", "blue", "yellow"]
numbers = ["1", "2", "3", "4"]
fortune = {
    "1": "Captain Plort needs $500!",
    "2": "Goodness, you're attractive!",
    "3": "A tasty meal is in your future!",
    "4": "Don't pick your nose!",
    "red": "Brush your teeth! You have Sea-World breath!",
    "green": "Midy stole your fortune ahahahahahahahahahahahaha!",
    "blue": "Sam farted!",
    "yellow": "Gwinna farted!"
}

def fortune_game():
    game_on = True
    keep_guessing = 0
    side = "color"
    while game_on == True and keep_guessing <2:
        if side == "color":
            print(color_list)
            chosen_color = input("Pick a color! ").lower()
            if len(chosen_color) % 2 == 0:
                keep_guessing +=1
            else:
                keep_guessing +=1
                side = "number"
        elif side == "number":
            print(numbers)
            chosen_number = int(input("Pick a number! "))
            if chosen_number % 2 == 0:
                keep_guessing += 1
                side = "number"
            else:
                keep_guessing +=1
                side = "color"
    else:
        if side == "color":
            print(color_list)
            fortune_color = input("Choose a final color! ")
            print(fortune[fortune_color])
            if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
                    fortune_game()
            else:
                    keep_guessing = False
                    clear()
                    print("Thanks for playing! Goodbye!")
        if side == "number":
            print(numbers)
            fortune_number = input("Choose a final number! ")
            print(fortune[fortune_number])
            if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
                    fortune_game()
            else:
                    keep_guessing = False
                    clear()
                    print("Thanks for playing! Goodbye!")

fortune_game()
