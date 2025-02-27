import turtle as t
import random

# Taken from the output of parse_colours.py
colour_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)]

screen = t.Screen()
screen.setup(width=550, height=600)

turtle = t.Turtle()
t.colormode(255)
turtle.shape("circle")
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.goto(-230, -250)

for _ in range(0, 10):
    for _ in range(0, 10):
        turtle.dot(20, random.choice(colour_list))
        turtle.forward(50)

    turtle.backward(500)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)


turtle.goto(-230, -250)
screen.exitonclick()