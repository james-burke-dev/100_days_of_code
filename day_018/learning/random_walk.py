import random
from turtle import Turtle, Screen

def draw_walk(turtle, direction, colour):

    turtle.pencolor(colour)
    turtle.left(direction)
    turtle.forward(25)


t1 = Turtle()
t1.pensize(15)
t1.speed("fastest")

directions = [90, 180, 270, 360]
colours = ["light blue", "cyan", "red", "green",
        "yellow", "brown", "pink"]

for i in range(100):
    direction = random.choice(directions)
    colour = random.choice(colours)

    draw_walk(t1, direction, colour)

