import pandas as pd 
import turtle

image = "blank_states_img.gif"
data = pd.read_csv("50_states.csv")

print(data.head)

screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

guessed_states = []
states_list = data.state.to_list()


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Name a State").title()

    if answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        
    if answer in states_list:
        if answer not in guessed_states:
            guessed_states.append(answer)
            check_answer = data[data.state == answer]
            x_axis, y_axis = int(check_answer.x.item()), int(check_answer.y.item())
            t.goto(x_axis, y_axis)
            t.write(f"{answer}")
