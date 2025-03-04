from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def return_to_start(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if (self.distance((0,FINISH_LINE_Y)) < 20):
            return True
        else:
            return False