# Split string method
namesString = input("Give me everybody's names, separated by a comma: ")
names = namesString.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# gets the length of string
length = len(names)

# getting random index for list 
randomIndex = random.randint(0, length-1) # because of 0 indexing

# getting random person by index
randomPerson = names[randomIndex]

# using choice function
# randomPerson = random.choice(names)

# output
print(f'{randomPerson} is going to buy the meal today!')