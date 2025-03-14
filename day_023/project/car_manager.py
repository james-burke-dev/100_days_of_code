import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
        
    def create_car(self):

        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.goto(300 , random.randint(-250, 250))

        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



