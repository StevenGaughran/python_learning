# Day 17.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order_menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()

is_running = True

while is_running:
    order = (input(f"What would you like? " + "(" + order_menu.get_items() + "): ").lower())
    if order == "report":
        coffeemaker.report(), money.report()
    elif order == "off":
        print("The machine is turning off. Goodbye!")
        is_running = False
    else:
        drink = order_menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
