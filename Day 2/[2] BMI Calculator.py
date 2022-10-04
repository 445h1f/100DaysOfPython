# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# applying bmi formula
bmi = float(weight) / float(height)**2

# converting bmi to int type to get whole number
bmi = int(bmi)

print(f'Your BMI is {bmi}')