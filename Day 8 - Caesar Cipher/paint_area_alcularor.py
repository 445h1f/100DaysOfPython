#Write your code below this line 👇
import math

def paint_calc(height, width, coverage):
    num_cans = (height * width) / coverage
    print(f'You\'ll need {math.ceil(num_cans)} cans of paint')


#Write your code above this line 👆

# 🚨 don't change the code below
test_h = int(input('Height of the wall: '))
test_w = int(input('Width of the wall: '))
coverage = 5

paint_calc(height=test_h, width=test_w, coverage=coverage)
