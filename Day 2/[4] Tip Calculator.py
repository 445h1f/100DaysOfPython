print('Welcome to Tip Calculator!')

# asking for bill amount, tip percentage and no. of people splitting the bill
billAmount = input('What was the total bill? $')
tipPercentage = input('What percentage of tip you would like to give? 10, 12, or 15? ')
peoplesPaying = input('How many people to split the bill? ')

# calculating total tip amount (multiplying billAmount with percentage of tip)
tipAmount = (int(tipPercentage) / 100) * float(billAmount)

# total bill including tip also
totalBill = float(billAmount) + tipAmount

# splitting the bill by dividing total amount by number of peoples paying and rounding off till 2 decimal places
eachPersonBill = round((totalBill / int(peoplesPaying)), 2)

# result output
print(f'Each person should pay: ${eachPersonBill}')

# waiter thanking for the tip:)
print(f'Waiter: Thank you for your ${tipAmount} tip!')