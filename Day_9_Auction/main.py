from replit import clear
#HINT: You can call clear() to clear the output in the console.
#ALSO HINT: Apparently the clear() command is only for replit, so I'm not sure how worthwhile it is to get used to it.

#This was the easiest part, right here.
from art import logo
print(logo)

#I originally had empty variables for 'name' and 'bid' here, but then realized I didn't need 'em.
auction = {}

#My original code for this part was a hot mess. Thanks to 'aetimmes' for helping me with the 'while' loops and dicitonary updating. I almost understand it now! I wound up deleting and redoing the ENTIRE THING. It was worth it.

#I had a lot of trouble with closing out the 'while' loops, but then the instructor went about it in the solution video in a way that made sense, and which should have been communicated earlier.

finished = False

while finished == False:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    auction[name] = bid
    another_bidder = input("Would anyone else like to bid? Please type 'yes' or 'no': ").lower()
    if another_bidder == "no":
        finished = True
        clear()
    elif another_bidder == "yes":
        clear()

#The code below was shamelessly stolen from Travis on the udemy course questions. The instructor's way of getting this done was weird as Hell, involving a complex and confusing 'for/in' loop.
winner = max(auction, key = auction.get)

print(f"The winner is {winner} with a bid of ${auction[winner]}.")
