# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# getting years left to live if you're about to live 90 years
# subtracting the current age from 90 to get years left
yearsLeft = 90 - int(age)

# calculating days, weeks, months left to live

# 1 day = 365 days (365.25 to be exact 😂)

daysLeft = yearsLeft * 365

# 1 year = 52 weeks
weeksLeft = yearsLeft * 52

# 1 year = 12 months
monthsLeft = yearsLeft * 12

# printing out result
print(f'You have {daysLeft} days OR {weeksLeft} weeks OR {monthsLeft} months left in your life.')
