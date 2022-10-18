# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# calculating bmi


bmi = weight / height**2

bmi = round(bmi, 1)

# applying the logic of bmi

if bmi < 18.5: # less than 18.5 then underwight
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25: # between 18.5 and 25 then normal
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30: # between 25 and 30 then slightly overweiht
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35: # between 30 and 35 then obese
    print(f'Your BMI is {bmi}, you are obese.')
else: # greater than or equal to 35 then clinically obese
    print(f'Your BMI is {bmi}, you are clinically obese.')
