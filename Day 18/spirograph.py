import random
import turtle as t


tom = t.Turtle()
t.colormode(255)
tom.speed(6)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# num_circle = 50
# angle = 360/num_circle

# for _ in range(num_circle):
#     tom.pencolor(random_color())
#     tom.circle(100)
#     tom.right(angle)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tom.pencolor(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(50)

screen = t.Screen()
screen.exitonclick()