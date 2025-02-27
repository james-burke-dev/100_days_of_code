import random
from turtle import Turtle, Screen

def draw_shape(turtle, sides, colour):
    i = 0
    turtle.pencolor(colour)
    while i < sides:
        turtle.forward(100)
        turtle.right(360/sides)
        i += 1 

t1 = Turtle()
colours = ["light blue", "cyan", "red", "green",
        "yellow", "brown", "pink"]
for i in range(3,10):
    colour = random.choice(colours)
    colours.remove(colour)
    draw_shape(t1, i, colour)

