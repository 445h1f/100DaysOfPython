import random
import turtle as t


tom = t.Turtle()
t.colormode(255)
tom.speed(0)
tom.pensize(15)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    tom.pencolor(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))



screen = t.Screen()
screen.exitonclick()