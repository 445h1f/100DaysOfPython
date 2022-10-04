from turtle import Turtle, Screen
import random

screen = Screen()

tom = Turtle()


colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

def draw_shape(num_sides):    
    angle = 360 / num_sides
    tom.pencolor(random.choice(colors))
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)


for i in range(3, 15):
    draw_shape(i)


screen.exitonclick()

