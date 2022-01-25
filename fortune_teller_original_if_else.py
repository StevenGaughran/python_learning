#a fortune teller, much  like the kids create with paper

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

# chosen_color = ""
# chosen_number = ""
# keep_guessing = 0

# def color_side():
#     print(color_list)
#     chosen_color = input("Pick a color: ").lower()
#     if chosen_color != color_list:
#         print("Invalid choice! Please pick one of the listed colors.")
#         color_side()
#     elif len(chosen_color) % 2 == 0:
#         print(chosen_color)
#         color_side()
#     else:
#         number_side()

# def number_side():
#     print(numbers)
#     chosen_number = int(input("Pick a number: "))
#     if chosen_number != numbers:
#         print("Invalid choice! Please pick one of the listed numbers.")
#         numbers()
#     if chosen_number % 2 == 0:
#         number_side()
#     else:
#         color_side()

# def fortune_game():
#     game_on = True
#     keep_guessing = 0
#     while game_on is True and keep_guessing < 3:
#         color_side()
#     else:
#         #This final_choice thing below doesn't work properly. I'll fix it later.
#         final_choice = len(chosen_color) + chosen_number / 4
#         print(fortune[final_choice])
#         if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
#             fortune_game()
#         else:
#             keep_guessing = False
#             clear()
#             print("Thanks for playing! Goodbye!")

# fortune_game()

#a fortune teller, much  like the kids create with paper

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
    keep_guessing = True
    while keep_guessing:
        print(color_list)
        first_color = input("Pick a color! ").lower()
        if len(first_color) % 2 == 0:
            print(color_list)
            second_color = input("Pick another color! ").lower()
            if len(second_color) % 2 == 0:
                print(color_list)
                fortune_color = input("Pick a final color! ").lower()
                print(fortune[fortune_color])
                if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
                    fortune_game()
                else:
                    keep_guessing = False
                    clear()
                    print("Thanks for playing! Goodbye!")
            else:
                print(numbers)
                second_number = input("Pick a number!")
                print(fortune[second_number])
                if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
                    fortune_game()
                else:
                    keep_guessing = False
                    clear()
                    print("Thanks for playing! Goodbye!")
        else:
            print(numbers)
            first_number = int(input("Pick a number! "))
            if first_number % 2 == 0:
                second_number = input("Pick one more number! ")
                print(fortune[second_number])
                if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
                    fortune_game()
                else:
                    keep_guessing = False
                    clear()
                    print("Thanks for playing! Goodbye!")
            else:
                print(color_list)
                fortune_color = input("Pick one more color! ").lower()
                print(fortune[fortune_color])
                if input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
                    fortune_game()
                else:
                    keep_guessing = False
                    clear()
                    print("Thanks for playing! Goodbye!")

fortune_game()