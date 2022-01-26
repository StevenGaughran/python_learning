# The Day 11 "capstone" project: a functional game of Blackjack.
#I'm very pleased that I got about 95% of the way there by myself on this one.
#Thanks to aetimmes for helping me with functions as well as list modifications.

import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)

def player_deal():
    player_hand = []
    player_hand = random.sample(cards, 2)
    if sum(player_hand) == 21:
        print("Blackjack! You win!")
        another_game()
    while sum(player_hand) <= 21:
        print(player_hand)
        print(f"Your total is {sum(player_hand)}.")
        if input("Would you like another card? Press 'y' for yes, or 'n' for no. ") == "y":
            player_hand += random.sample(cards, 1)
            if sum(player_hand) > 21 and 11 in player_hand:
                for card in player_hand:
                    if card==11:
                        card=1
        else:
            return sum(player_hand)
    else:
        print(player_hand)
        print(f"Your total is {sum(player_hand)}")
        print("Bust! You lose! Game over!")
        another_game()

def dealer_deal():
    dealer_continue = True
    dealer_hand = []
    dealer_hand = random.sample(cards, 2)
    while dealer_continue == True:
        print(dealer_hand)
        print(f"The dealer has {sum(dealer_hand)}.")
        if sum(dealer_hand) <= 16:
            dealer_hand += random.sample(cards, 1)
        elif sum(dealer_hand) in range(17,22):
            return sum(dealer_hand)
        elif sum(dealer_hand) > 21 and 11 in dealer_hand:
                for card in dealer_hand:
                    if card==11:
                        card=1
                dealer_hand += random.sample(cards, 1)
        elif sum(dealer_hand) > 21:
                dealer_continue == False
                print("The dealer busts! You win!")
                another_game()

def victor(player, dealer):
    print(f"Your total is {player}.")
    print(f"The dealer's total is {dealer}.")
    if player > dealer:
        print("Congratulations! You win!")
    if player == dealer:
        print("It's a draw!")
    else:
        print("The dealer wins!")

def another_game():
    if input("Do you want to play again? Type 'y' for yes, or 'n' for no.") == 'y':
            blackjack()
    else:
        print("Thanks for playing! Goodbye!")
        return

def blackjack():
    victor(player_deal(), dealer_deal())
    if input("Do you want to play again? Type 'y' for yes, or 'n' for no.") == 'y':
            blackjack()
    else:
        print("Thanks for playing! Goodbye!")
        return

blackjack()
