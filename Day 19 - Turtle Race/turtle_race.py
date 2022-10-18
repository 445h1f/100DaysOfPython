from turtle import Turtle, Screen
import random
import time

is_race_on = False

screen = Screen()

# setting screen size
width=500
height=400
screen.setup(width=width, height=height)


# color list of turtles
colors = ['red', 'green', 'yellow', 'orange', 'blue', 'purple', 'black']

# shuffling colors
random.shuffle(colors)

# generating input string
prompt_string = 'Which color turtle will win?\n\n'
for index, value in enumerate(colors):
    prompt_string += f'{index+1}: {value.capitalize()}\n'
prompt_string += '\nEnter Number:'

# asking user to input turtle number
user_input = int(screen.numinput(title='Input', prompt=prompt_string, default=random.randint(1, 8), minval=1, maxval=7))
print(f'You\'d chosen {colors[user_input-1]} turtle.')
# inital y coordinates of turtle
home_y_coordinates = [150, 100, 50, 0, -50, -100, -150]


# list to store all instances of turtle
all_turtles = []

for i in colors:
    t = Turtle(shape='turtle')
    t.penup()
    t.color(i)
    all_turtles.append(t)

for index, value in enumerate(home_y_coordinates):
    all_turtles[index].goto(x=-((width/2)-20), y=value)

if user_input:
    is_race_on = True

while is_race_on:
    for index, value in enumerate(all_turtles):
        random_distance = random.randint(0, 10)
        value.forward(random_distance)
        if value.xcor() >= (width/2) - (40/2): #turtle size is 40 x 40
            is_race_on = False
            winner_turtle = colors[index]
            if user_input == index+1:
                print('You won!', end=' ')
            else:
                print('You lost!', end=' ')
            print(f'{winner_turtle.capitalize()} Turtle is the winner!')
            break
    
screen.exitonclick()