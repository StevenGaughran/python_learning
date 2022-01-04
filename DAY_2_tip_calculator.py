#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇




#STEVE: So, I figured this exercise out...except for the formatting to round out decimal two spaces. Angela's solution of course worked (see line 19), but it was also a bit of an example of "Draw a circle, now draw an owl." This is the first time the formatting function has been introduced, and saying "Google it" without explaining how or why it works isn't particularly helpful. I'm still not sure why it works?

bill = float(input("What was the total bill? $"))
tip = float(input("What percentage would you like to tip? ")) / 100
people = float(input("How many people to split the bill? "))
total = (bill * tip + bill) / people
final_total = "{:.2f}".format(total)
# final_total = round(total, 2) 
# final_total = "{.2f}".format(final_total)
print(f"Each person pays ${final_total}.")