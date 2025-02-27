import random
from turtle import Turtle, Screen

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(10)


def rand_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

screen = Screen()
screen.colormode(255)

t1 = Turtle()
t1.speed("fastest")

draw_spirograph(10)


