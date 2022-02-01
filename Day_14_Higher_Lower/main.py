import random
from game_data import data
from art import logo
from art import vs

def high_low_game(contestants):
    print(logo)
    playing = True
    score = 0
    while playing == True:
        choice_A = random.choice(contestants)
        choice_B = random.choice(contestants)

        print(f"Compare {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}.")

        print(vs)

        print(f"Against {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}.")

        if input("Who has more followers? Type 'A' or 'B': ").upper() == "A":
            player_guess = choice_A
        else:
            player_guess = choice_B
        
        if player_guess == choice_A:
            if player_guess['follower_count'] > choice_B['follower_count']:
                print("Correct! Next round:")
                print("-------------------")
                score += 1
            else:
                playing = False
        elif player_guess == choice_B:
            if player_guess['follower_count'] > choice_A['follower_count']:
                print("Correct! Next round:")
                print("-------------------")
                score += 1
            else:
                playing = False
    else:
        print("-------------------")
        print("Whoops! Wrong choice!")
        print(f"The game is over! Your final score is {score}!")
        print("Thank you for playing!")
        

high_low_game(data)