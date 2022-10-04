from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


# event listener
screen.listen()

def move_forward():
    tom.forward(20)

# moving turtle forward when space button is pressed
screen.onkey(fun=move_forward, key='space')

screen.exitonclick()