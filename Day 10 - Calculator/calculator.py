logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""


def add(num1, num2):
    """Adds num1 and num2"""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts num2 from num1"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies num1 and num2"""
    return num1 * num2

def divide(num1, num2):
    """Divides num1 by num2"""
    if num2 == 0:
        return 'You can\'t divide by 0.'
    return num1 / num2

def exponent(num1, num2):
    """Returns num1 raise to the power num2"""
    return num1 ** num2

def remainder(num1, num2):
    """Returns remainder of divsion of num1 by num2"""
    if num2 == 0:
        return 'You can\'t divide by 0.'
    return num1 % num2

calculatorOn = True

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
    '**' : exponent,
    '%' : remainder,

}

def calculator():
    print(logo)
    num1 = float(input('What\'s the first number?: '))
    maxWidth = 9 # because remainder has maxWidth (9)
    for symbol in operations:
            print(f'{operations[symbol].__name__.capitalize().ljust(maxWidth)} : {symbol}') # prints func name also

    calculatorOn = True

    while calculatorOn:
        operationSymbol = input('Pick an operation symbol: ')
        if operationSymbol in operations:
            num2 = float(input('What\'s the next number?: '))
            calculation = operations[operationSymbol]
            answer = calculation(num1, num2)
            print(f'{num1} {operationSymbol} {num2} = {answer}')
            askToContinue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
            if askToContinue == 'y':
                num1 = answer
            else:
                calculatorOn = False
                calculator()
        else:
            print(f'Invalid Choice!')

calculator()