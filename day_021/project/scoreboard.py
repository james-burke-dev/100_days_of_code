from turtle import Turtle 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center",font=("Arial", 24, "normal"))


    def update_score(self):
        self.score() += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center",font=("Arial", 24, "normal"))

