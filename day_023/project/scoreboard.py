from turtle import Turtle 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.level}", align="left",font=("Arial", 60, "normal"))


    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center",font=("Arial", 24, "normal"))

