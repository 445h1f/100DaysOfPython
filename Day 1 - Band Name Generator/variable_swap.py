# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# storing value of a in c
c = a

# assigning value of a to b
a = b

# now, assigning value of c ( value of a) to b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


## swapping variable without introducing third variable
a, b = b, a # value of b will be assigned to a and vice-versa

print(f'a: {a} & b: {b}')