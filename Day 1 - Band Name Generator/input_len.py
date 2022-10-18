# this piece of code will ask you for your name and will return number of characters (length) of your name

#asking user for name
name = input("What's your name? ")

# getting length of name using len() function
length = len(name)

# printing length
print(f'Okay {name}! Your name is {length} character long.')