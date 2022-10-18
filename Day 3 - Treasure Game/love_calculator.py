# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# combining & making names lower for matching
combinedName = name1.lower() + name2.lower()

# counting total T-R-U-E occurrence in both names
t = combinedName.count('t')
r = combinedName.count('r')
u = combinedName.count('u')
e = combinedName.count('e')
totalTrueCount = t + r + u + e

# counting total L-O-V-E occurrence in both names

lCount = combinedName.count('l')
oCount = combinedName.count('o')
vCount = combinedName.count('v')
eCount = combinedName.count('e')

totalLoveCount = lCount + oCount + vCount + eCount

loveScore = int(f'{totalTrueCount}{totalLoveCount}')

if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f'Your score is {loveScore}.')

