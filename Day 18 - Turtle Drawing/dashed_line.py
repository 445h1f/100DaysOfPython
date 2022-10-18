from turtle import Turtle, Screen

tom = Turtle()

for i in range(10):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()



screen = Screen()
screen.exitonclick()