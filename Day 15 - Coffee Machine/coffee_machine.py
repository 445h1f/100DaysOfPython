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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money' : 0
}

coins = {
    'quarter' : 0.25,
    'dime': 0.1,
    'nickel': 0.05,
    'penny' : 0.01
}

def printReport():
    """Prints report of resources left."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}gm')
    print(f'Money: ${resources["money"]}')

def runCoffeeMachine():
    """Runs coffee machine and serves you coffee requirements are met."""
    userInput = input('  What would you like? (espresso/latte/cappuccino): ').lower()
    if userInput == 'off':
        print(f'Coffee Machine turned off.')
        return None
    elif userInput == 'report':
        printReport()
    else:
        if userInput in MENU:
            coffeeRequirements = MENU[userInput]['ingredients']
            for resource in coffeeRequirements:
                if coffeeRequirements[resource] > resources[resource]:
                    print(f'Sorry there is not enough {resource}.')
                    return False
            moneyRequired = MENU[userInput]['cost']
            userMoney = 0
            print(f'Please insert coins.')
            for coin in coins:
                amount = int(input(f'How many {coin}?: '))
                userMoney += amount * coins[coin]
            if moneyRequired > userMoney:
                moneyText = f'Sorry {userInput.title()} requires ${moneyRequired} and you had given ${round(userMoney, 2)}. '
                if userMoney > 0:
                    moneyText += 'Money Refunded.'
                print(moneyText)
                return False
            else:
                resources['money'] += moneyRequired
                for resource in coffeeRequirements:
                    resources[resource] -= coffeeRequirements[resource]
                if userMoney > moneyRequired:
                    extraMoney = round(userMoney - moneyRequired, 2)
                    print(f'Here is ${extraMoney} in change.')
                print(f'Here is your {userInput} ☕️. Enjoy!')
                return True

        else:
            print(f'Invalid Input!')
            return False
machineOn = True

while machineOn:
    run = runCoffeeMachine()
    if run is None:
        machineOn = False