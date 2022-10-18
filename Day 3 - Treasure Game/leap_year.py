# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# applying logic to check year is leap or not
if year % 4 == 0: # first if divisible by 4
    if year % 100 == 0: # if divisible by 4 then check for century by dividing with 100
        if year % 400 == 0: # year is a century. leap year only if divisible by 400
            print('Leap year')
        else:
            print('Not leap year')
    else: # not century. is leap year
        print('Leap year')
else: # not leap year because not divisble by 4
    print('Not leap year')
