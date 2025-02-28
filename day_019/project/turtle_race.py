import random
from turtle import Turtle, Screen

race_started = False

screen = Screen()
screen.setup(width=500, height=400)

player_bet = screen.textinput(title="Place your bet", prompt="What turtle will win the race? Enter a colour: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
start_coord = [230, -100]
turtles = []

for colour in colours:
    t1 = Turtle(shape="turtle", color=colour)
    t1.penup()
    t1.goto(start_coord[0], start_coord[1])
    start_coord[1] += 25
    turtles.append(t1)

if player_bet:
    race_started = True
    
    while race_started:

        for t in turtles:
            if(t.xcor > 230):
                winner = t.pencolor()

                if winner == player_bet:
                    print(f"You've won! The {winner} turtle won")

                else:
                    print(f"You've lost! The {winner} turtle won")

                race_started = False
                break
            t.forward(random.randint(0,10))
            

screen.exitonclick()