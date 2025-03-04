import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Traffic!")
screen.tracer(0)

game_is_on = True

player = Player()

cars = CarManager()

scoreboard = Scoreboard()

screen.onkey("Up",player.move_forward)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_finished(): 
        player.return_to_start()
        cars.increase_speed()
        scoreboard.update_level()

screen.exitonclick()