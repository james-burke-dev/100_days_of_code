from turtle import Turtle, Screen


t1 = Turtle()
screen = Screen()

def turn_left():
    t1.left(10)

def turn_right():
    t1.right(10)

def move_forward():
    t1.forward(10)

def move_backwards():
    t1.backward(10)

def clear():
    t1.clear()
    t1.penup()
    t1.home()
    t1.pendown()

screen.listen()
screen.onkey("a", turn_left)
screen.onkey("d", turn_right)
screen.onkey("w", move_forward)
screen.onkey("s", move_backwards)
screen.onkey("c", clear)

screen.exitonclick()