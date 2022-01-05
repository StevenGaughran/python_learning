print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#STEVE NOTES: This was a pretty simple exercise in if/else logic. I feel like there is likely a more elegant way to do this sort of linear story thing; embedding everying inside a nesting doll of if/else statements seems unwise. But it works! So there!

#Write your code below this line 👇
print("You're at a crossroads.")
xroad = input("Where do you want to go? Type 'left' or 'right'. ").lower()
if xroad == "left":
  print("You continue down the road.")

  print("You've come to a lake. There is an island in the middle of the lake.")
  lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
  if lake == "wait":
    print("The boat takes you across the water.")

    print("You arrive at the island unharmed. There is a house with 3 doors, behind one of which sits the treasure you seek. One red, one yellow and one blue.")
    door = input("Which colour do you choose?").lower()
    if door == "red":
      print("You are engulfed by fire and die a terrible, horrible death. That's rough, buddy. Game over.")
    elif door == "blue":
      print("A rabid squirrel leaps from behind the door and eats you alive. Them's the breaks. Game over.")
    elif door == "yellow":
      print("Congratulations! You find the treasure and book a flight to Vegas. The End.")
    else:
      print("That isn't a valid option, and the gods of Python punish you for your hubris. A large foot comes crashing down from the sky and squishes you flat. You are dead. Game over.")
  else:
    print("You are devoured by man-eating trout. Tough break. Game over.")

else:
  print("You fall into a hole and die. Game over.")

