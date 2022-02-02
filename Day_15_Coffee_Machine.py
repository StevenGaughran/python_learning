# Day 15 was making this here Coffee Machine. My program works great, but it's a wordy beast. I'm certain I can
# streamline this monster by calling on the dictionaries more.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def espresso():
    if MENU['espresso']['ingredients']['water'] > RESOURCES['water']:
        print("Sorry, there is not enough water.")
        return
    elif MENU['espresso']['ingredients']['coffee'] > RESOURCES['coffee']:
        print("Sorry, there is not enough coffee.")
        return

    print("An espresso costs $1.50.")
    quarters = float(input("How many quarters are you inserting?"))*.25
    dimes = float(input("How many dimes are you inserting?"))*.1
    nickels = float(input("How many nickels are you inserting?"))*.05
    pennies = float(input("How many pennies are you inserting?"))*.01
    total_payment = round(quarters + dimes + nickels + pennies, 2)
    if total_payment == 1.50:
        print("Thank you! Enjoy your espresso!")
        RESOURCES['water'] -= MENU['espresso']['ingredients']['water']
        RESOURCES['coffee'] -= MENU['espresso']['ingredients']['coffee']
        RESOURCES['money'] += total_payment
        return
    elif total_payment > 1.50:
        RESOURCES['money'] += total_payment
        change = str(round(total_payment - 1.50, 2))
        RESOURCES['money'] -= change
        print(f"Your change is ${change}.")
        print("Thank you! Enjoy your espresso!")
        RESOURCES['water'] -= MENU['espresso']['ingredients']['water']
        RESOURCES['coffee'] -= MENU['espresso']['ingredients']['coffee']
        return
    else:
        print("Insufficient coins. Please order again.")
        return

def latte():
    if MENU['latte']['ingredients']['water'] > RESOURCES['water']:
        print("Sorry, there is not enough water.")
        return
    elif MENU['latte']['ingredients']['coffee'] > RESOURCES['coffee']:
        print("Sorry, there is not enough coffee.")
        return
    elif MENU['latte']['ingredients']['milk'] > RESOURCES['milk']:
        print("Sorry, there is not enough milk.")
        return

    print("A latte costs $2.50.")
    quarters = float(input("How many quarters are you inserting?")) * .25
    dimes = float(input("How many dimes are you inserting?")) * .1
    nickels = float(input("How many nickels are you inserting?")) * .05
    pennies = float(input("How many pennies are you inserting?")) * .01
    total_payment = round(quarters + dimes + nickels + pennies, 2)
    if total_payment == 2.50:
        print("Thank you! Enjoy your latte!")
        RESOURCES['water'] -= MENU['latte']['ingredients']['water']
        RESOURCES['coffee'] -= MENU['latte']['ingredients']['coffee']
        RESOURCES['milk'] -= MENU['latte']['ingredients']['milk']
        RESOURCES['money'] += total_payment
        return
    elif total_payment > 2.50:
        RESOURCES['money'] += total_payment
        change = str(round(total_payment - 1.50, 2))
        RESOURCES['money'] -= change
        print(f"Your change is ${change}.")
        print("Thank you! Enjoy your latte!")
        RESOURCES['water'] -= MENU['latte']['ingredients']['water']
        RESOURCES['coffee'] -= MENU['latte']['ingredients']['coffee']
        RESOURCES['milk'] -= MENU['latte']['ingredients']['milk']
        return
    else:
        print("Insufficient coins. Please order again.")
        return

def cappuccino():
    if MENU['cappuccino']['ingredients']['water'] > RESOURCES['water']:
        print("Sorry, there is not enough water.")
        return
    elif MENU['cappuccino']['ingredients']['coffee'] > RESOURCES['coffee']:
        print("Sorry, there is not enough coffee.")
        return
    elif MENU['cappuccino']['ingredients']['milk'] > RESOURCES['milk']:
        print("Sorry, there is not enough milk.")
        return

    print("A cappuccino costs $3.00.")
    quarters = float(input("How many quarters are you inserting?")) * .25
    dimes = float(input("How many dimes are you inserting?")) * .1
    nickels = float(input("How many nickels are you inserting?")) * .05
    pennies = float(input("How many pennies are you inserting?")) * .01
    total_payment = round(quarters + dimes + nickels + pennies, 2)
    RESOURCES['money'] += total_payment
    if total_payment == 2.50:
        print("Thank you! Enjoy your cappuccino!")
        RESOURCES['water'] -= MENU['cappuccino']['ingredients']['water']
        RESOURCES['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        RESOURCES['milk'] -= MENU['cappuccino']['ingredients']['milk']
        return
    elif total_payment > 2.50:
        RESOURCES['money'] += total_payment
        change = str(round(total_payment - 1.50, 2))
        RESOURCES['money'] -= change
        print(f"Your change is ${change}.")
        print("Thank you! Enjoy your cappuccino!")
        RESOURCES['water'] -= MENU['cappuccino']['ingredients']['water']
        RESOURCES['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        RESOURCES['milk'] -= MENU['cappuccino']['ingredients']['milk']
        return
    else:
        print("Insufficient coins. Please order again.")
        return

def coffee_machine():
    machine_on = True
    while machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
        if user_choice == "report":
            print(f"Water: {RESOURCES.get('water')}mL")
            print(f"Milk: {RESOURCES.get('milk')}mL")
            print(f"Coffee: {RESOURCES.get('coffee')}g")
            print(f"Money: ${RESOURCES.get(round('money', 2))}")
        elif user_choice == "espresso":
            espresso()
        elif user_choice == "latte":
            latte()
        elif user_choice == "cappuccino":
            cappuccino()
        elif user_choice == "off":
            print("The machine is off. Goodbye!")
            machine_on = False

coffee_machine()
