import turtle as t
import random

tom = t.Turtle()
t.colormode(255)
tom.penup()
tom.hideturtle()
tom.speed(0)
tom.setheading(255)
tom.forward(300)
tom.setheading(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

dots = 100

for dot_count in range(1, dots+1):
    tom.dot(20, random_color())
    tom.forward(50)
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)



screen = t.Screen()
screen.exitonclick()

