from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.body = []
        self.start_x_coord = 0

        for i in range(4):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(self.start_x_coord, 0)
            self.body.append(t)
            self.start_x_coord -= 20

    def move(self):
        """Move the snake forward """
        for idx in range(len(self.body)-1, 0, -1):
            new_x = self.body[idx-1].xcor()
            new_y = self.body[idx-1].ycor()

            self.body[idx].goto(new_x, new_y)
            self.body[0].forward(20)

    def up(self):
        front = self.body[0]
        if front.heading() != DOWN:
            front.setheading(UP)
 
    def down(self):
        front = self.body[0]
        if front.heading() != UP:
            front.setheading(DOWN)

    def left(self):
        front = self.body[0]
        if front.heading() != RIGHT:
            front.setheading(LEFT)

    def right(self):
        front = self.body[0]
        if front.heading() != LEFT:
            front.setheading(RIGHT)

    def add_piece(self, position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.body.append(t)

    def extend(self):
        self.add_piece(self.body[-1].position())

    def remove(self):
        for piece in self.body:
            piece.goto(1000,1000)



