from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()

# height and width of screen
HEIGHT = 600
WIDTH = 800
screen.setup(width=WIDTH, height=HEIGHT)

# black background
screen.bgcolor('black')
screen.tracer(0)

# paddles
r_paddle = Paddle((350, 50))
l_paddle = Paddle((-350, 50))


# ball
ball = Ball()

#scoreboard
scoreboard = Scoreboard()


# event listener
screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')
# screen.()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        print('yes')
        ball.bounce_y()

    # detecting collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detecting collision with right and left wall
    if ball.xcor() > 380: #right
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380: #left
        scoreboard.r_point()
        ball.reset_position()
        

    
    

    
    

# exit on click
screen.exitonclick()