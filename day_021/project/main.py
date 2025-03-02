import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snek = Snake()
food = Food()
screen.listen()

screen.onkey("Up", snek.up)
screen.onkey("Down", snek.down)
screen.onkey("Left", snek.left)
screen.onkey("Right", snek.right)


game_started = True
score = Scoreboard()

while game_started:
    screen.update()
    time.sleep(0.2)
    snek.move()
    
    # Detect food collision 
    if snek.body[0].distance(food) < 15:
        food.generate_location()
        snek.extend()
        score.update_score()
    
    if (snek.body[0].xcor() > 280 or snek.body[0].xcor() < -280) or (snek.body[0].ycor() > 280 or snek.body[0].ycor() < -280):
        game_started = False
        score.game_over()
    
    for piece in snek.body[1:]: 
        if snek.body[0].distance(piece) < 10:
            game_started = False
            score.game_over()

screen.exitonclick()