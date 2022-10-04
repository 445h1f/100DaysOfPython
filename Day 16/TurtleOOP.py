from turtle import Turtle, Screen
import time
import random

def randomColor():
    hexList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color = '#'
    for i in range(6):
        color += random.choice(hexList)
    return color


tim = Turtle()
tim.shape('turtle')
tim.color('red')

myScreen = Screen()

# while True:
#     command = input('What you want to do with turtle: ')
#     exec(f'tim.{command}')

for i in range(4):
    times = 0
    for i in range(10):
        tim.forward(20)
        time.sleep(0.3)
        if i == 9:
            tim.right(90)
        tim.color(randomColor())
myScreen.exitonclick()
