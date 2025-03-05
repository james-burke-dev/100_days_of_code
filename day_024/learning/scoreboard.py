from turtle import Turtle 
file_name = "high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

        self.score = 0
        self.high_score = 0

        with open(file_name) as fn:
            self.high_score = int(fn.read())
        

        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align="center",font=("Arial", 24, "normal"))


    def update_score(self):
        self.score() += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file_name, "w") as fn:
                fn.write(f"{self.high_score}")
        self.score = 0
        
