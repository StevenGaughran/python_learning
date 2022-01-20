from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
name = input("What is your name?: ")
bid = int(input("What is your bid?: "))

auction = {
    "Name": "",
    "Bid": 0,
}

def add_bid(auctioner_name, final_bid):
    finished = False
    new_bidder = ""
    while finished == False:
        if final_bid >= auction["Bid"]:
            auction.update({"Name": auctioner_name, "Bid": final_bid})
        new_bidder = input("Is there another bidder? Please type 'yes' or 'no': ").lower()
        if new_bidder == "no":
            finished = True
            clear()
        else:
            clear()
            
    print(auction["Name"] +" won the bid with $" +str(auction["Bid"]))

add_bid(auctioner_name=name, final_bid=bid)