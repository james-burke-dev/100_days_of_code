import time
from turtle import Screen
from ball import Ball
from racket import Racket
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

game_started = True

player_one = Racket((350, 0))
player_two = Racket((-350, 0))

ball = Ball((0,0))

scoreboard = Scoreboard()

screen.onkey("w", player_one.up)
screen.onkey("s", player_one.down)
screen.onkey("Up", player_two.up)
screen.onkey("Down", player_two.down)

while game_started:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor < -280:
        ball.bounce_y()

    if (ball.distance(player_one) < 50 and ball.xcor() > 320) or (ball.distance(player_two) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.update_score(1)

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_score(2)


