from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed(0)
        self.x_move = 10 # x axis moving pixels
        self.y_move = 10 # y axis moving pixels
        self.move_speed = 0.1 # moving speed (factor)

    def move(self):
        f"""Moves the ball (x, y) positions ({self.x_move}, {self.y_move}) pixels."""
        new_x = self.xcor() + self.x_move # adding x move pixels to previous x cordinate
        new_y = self.ycor() + self.y_move # same as above but for y axis
        self.goto(new_x, new_y) # sending ball to new moved coordinates

    def bounce_x(self):
        """Reversing the ball x coordinate to bounce back"""
        self.x_move *= -1
        self.move_speed *= 0.9 # multiplying the speed of ball on every x bounce by 0.9

    def bounce_y(self):
        """Reversing the ball y coordinate to bounce back"""
        self.y_move *= -1

    def reset_position(self):
        """Resetting the ball position and move speed."""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1