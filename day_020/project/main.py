import random
import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snek = Snake()

screen.listen()

screen.onkey("Up", snek.up)
screen.onkey("Down", snek.down)
screen.onkey("Left", snek.left)
screen.onkey("Right", snek.right)


game_started = True
score = 0 

while game_started:
    screen.update()
    time.sleep(0.2)
    snek.move()
    


    

screen.exitonclick()