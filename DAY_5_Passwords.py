#Password Generator Project

#Hola. Steve here.

#So, Day 5 was a lot better than Day 4. I was able to make my way through the exercises without too much hassle.

#The real difficulty here was (a) having to muddle about with Lists, considering the sub-standard lesson plan of the previous day, and (b) having to Google the necessary Random commands. 

#Struggled with the 'random() method does not accept any arguments' error for a lil' bit, and the good people of the internet were not helpeful. 'It says exactly what the problem is!' they chuckled, as if that was in any way helpful. Anyone can recite a line in a foreign langugae without understanding a goddamn thing. But I figured it out in the end.

#As per usual, there is almost certainly a more elegant solution to this problem, but this works in a pinch.


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for letter in letters:
  rndm_ltr = random.sample(letters, nr_letters)

for number in numbers:
  rndm_nmbr = random.sample(numbers, nr_numbers)

for symbol in symbols:
  rndm_symbl = random.sample(symbols, nr_symbols)

password = rndm_ltr + rndm_nmbr + rndm_symbl
random.shuffle(password)
print(password)