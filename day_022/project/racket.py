from turtle import Turtle

class Racket(Turtle):
    def __init__(self, start_coords):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.heading(90)
        self.goto(start_coords)
        

    def up(self):
        self.goto(self.ycor() + 20)

    def down(self):
        self.goto(self.ycor() - 20)
    