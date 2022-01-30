#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def easy_game():
    easy_number = random.randint(1, 100)
    guesses_remaining = 10
    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
        easy_player_guess = int(input("Make a guess: "))
        if easy_player_guess > easy_number:
            guesses_remaining -= 1
            print("Too high.")
            if guesses_remaining > 0:
                print("Guess again!")
        elif easy_player_guess < easy_number:
            guesses_remaining -= 1
            print("Too low.")
            if guesses_remaining > 0:
                print("Guess again!")
        else:
            print(f"You got it! The secret number was {easy_number}!")
            return
    else:
        print("You are out of guesses. You lose!")
        return

def hard_game():
    hard_number = random.randint(1, 100)
    guesses_remaining = 5
    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
        hard_player_guess = int(input("Make a guess: "))
        if hard_player_guess > hard_number:
            guesses_remaining -= 1
            print("Too high.")
            if guesses_remaining > 0:
                print("Guess again!")
        elif hard_player_guess < hard_number:
            guesses_remaining -= 1
            print("Too low.")
            if guesses_remaining > 0:
                print("Guess again!")
        else:
            print(f"You got it! The secret number was {hard_number}!")
            return
    else:
        print("You are out of guesses. You lose!")
        return

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    easy_game()
elif difficulty == "hard":
    hard_game()



