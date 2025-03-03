from turtle import Turtle 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

        self.player_one_score = 0
        self.player_two_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.player_one_score}\t\t\t{self.player_two_score}", align="center",font=("Arial", 60, "normal"))


    def update_score(self, player):
        if player == 1:
            self.player_one_score += 1
        else:
            self.player_two_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center",font=("Arial", 24, "normal"))

