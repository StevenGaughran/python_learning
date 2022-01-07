#Let me be on record as saying that Day 4 of this course was absolute bullshit. So 'owly' as to be offputting. I learned more from the comments section than the actual lecture, which was not sufficient for the needs of the exercises. 

#Ultimately I think I was supposed to use lists to do this, but I haven't fully figured everything out yet because I found the lesson frustrating. I'll have to return to it in a day or so and give it another once-over once I'm less frustrated.

# Anyway, here's 'Wonderwall'

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." ))

computer_choice = random.randint(0,2)

#0 is rock
#1 is paper
#2 is scissors

#printouts of the player's action
if player_choice >=3 or player_choice < 0:
  print("Pick a real number, cheater.")
elif player_choice == 0:
  print(rock)
  print("You chose rock.")
elif player_choice == 1:
  print(paper)
  print("You chose paper.")
else:
  print(scissors)
  print("You chose scissors.")

#printouts of the computer's action
if computer_choice == 0:
  print(rock)
  print("The computer chose rock.")
elif computer_choice == 1:
    print(paper)
    print("The computer chose paper.")
else:
  print(scissors)
  print("The computer chose scissors.")

#The actual RPS part. Tried using a list like the lessons "taught" us, but I had a real bitch of a time with it. I had created the "grid," but couldn't figure out how to call on it properly. Thankfully, a fellow named "Howard" in the comments had the same idea, and his insight helped me substantially. Howard, wherever you are: you're a gem.
row_r = ["It's a draw!", "You lose!", "You win!"]
row_p = ["You win!", "It's a draw!", "You lose!"]
row_s = ["You lose!", "You win!", "It's a draw!"]
map = [row_r, row_p, row_s]
result = map[player_choice][computer_choice]
print(result)

#Okay, so this works now, but it took longer than I would care to admit. I am going to go drink some wine now.