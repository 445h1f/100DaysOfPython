from turtle import Turtle
from random import randint


class Food(Turtle):
    """Making food for snake!"""
    def __init__(self, color):
        super().__init__() # inheriting from turtle class
        self.penup() # stops path drawing of turtle as it moves
        self.shape('circle') # setting turtle shape to cirle (for cookie🍪hahaa)
        self.color(color) # setting food color as per theme
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #changes size of turtle to 10x10
        self.speed(0) # fasted speed
        self.refresh() # calling refresh method to locate the food first time on the screen


    def refresh(self):
        """To place food randomly on screen."""
        random_x, random_y = randint(-270, 270), randint(-270, 270) # getting random x, y co-ordinates
        self.goto(random_x, random_y) # sending turtle/ food to that random coordinate
