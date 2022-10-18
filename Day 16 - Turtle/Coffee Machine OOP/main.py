from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    flavours = menu.get_items()
    choice = input(f'What flavour would you like to order? {flavours}: ').lower()

    # turns machine off if user choose off
    if choice == 'off':
        is_on = False
    elif choice == 'report': # get report of money and ingredients
        print(coffee_maker.report())
        print(money_machine.report())
    else:
       drink = menu.find_drink(choice) #find flavour if it exists
       if drink:
            # checks if resource is sufficient
            if coffee_maker.is_resource_sufficient(drink):
                cost_of_drink = drink.cost
                print(f'Okay, {choice} cost {money_machine.CURRENCY}{cost_of_drink}!')
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
