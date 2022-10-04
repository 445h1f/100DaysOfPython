from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def turn_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def turn_right():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def pen_up():
    tom.penup()


def pen_down():
    tom.pendown()


# clears the drawing on screen
def clear_screen():
    tom.clear()
    pen_up()
    tom.home()
    pen_down()


screen.onkey(move_forward, 'f')
screen.onkey(move_backward, 'b')
screen.onkey(turn_left, 'l')
screen.onkey(turn_right, 'r')
screen.onkey(pen_up, 'u')
screen.onkey(pen_down, 'd')
screen.onkey(clear_screen, 'c')


screen.exitonclick()
