# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Small Pizza: $15
if size == 'S':
    bill = 15
# Medium Pizza: $20
elif size == 'M':
    bill = 20
# Large Pizza: $25
else:
    bill = 25


if add_pepperoni == 'Y':
    if size == 'S':
        # Pepperoni for Small Pizza: add $2 to bill
        bill += 2
    else:
        # Pepperoni for Medium or Large Pizza: add $3 to bill
        bill += 3

# IF Extra cheese for any size pizza: plus $1 to bill
if extra_cheese == 'Y':
    bill += 1

# final bill
print(f'Your final bill is: ${bill}')