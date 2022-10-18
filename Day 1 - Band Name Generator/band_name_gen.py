#1. Create a greeting for your program.
# name variable to store name of user
name = input('What\'s your name?\n')

# greets the user
print(f'Hello {name}! I\'ll generate a band name for you. Let\'s start...')


#2. Ask the user for the city that they grew up in & store in city variable

city = input("What's the name of city you grew up in?\n")

#3. Ask the user for the name of a pet and store in petName variable
petName = input("What's your pet name?\n")

#4. Combine the name of their city and pet and show them their band name.
bandName = f'{city} {petName}'

#5. Make sure the input cursor shows on a new line, see the example at:
print(f'Your band name can be {bandName}!')
