from turtle import Turtle, Screen

def draw_dahsed_line(turtle):
    turtle.forward(5)
    turtle.penup()
    
    turtle.forward(5)
    turtle.pendown()

t1 = Turtle()

for i in range(0,10):
  draw_dahsed_line(t1)

