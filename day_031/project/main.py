import pandas as pd
from tkinter import *
from tkinter import messagebox
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK = "day_031/project/images/card_back.png"
CARD_FRONT = "day_031/project/images/card_front.png"
RIGHT = "day_031/project/images/right.png"
WRONG = "day_031/project/images/wrong.png"

current_card = {}

def load_data():
    try: 
        data = pd.read_csv("day_031/project/data/words_to_learn.csv")
        data = data.to_dict(orient="records")
    except FileNotFoundError:
        data = pd.read_csv("day_031/project/data/french_words.csv")
        data = data.to_dict(orient="records")
        return data
    else:
        return data

def generate_word_group(): 

    pair = random.choice(data)
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)
    current_card = pair
    french_word, eng_word = pair["French"], pair["English"]

    bg_canvas.itemconfig(bg_card, image=card_front_img)
    bg_canvas.itemconfig(heading, text="French", fill="black")
    bg_canvas.itemconfig(word_label, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    print(current_card)
    bg_canvas.itemconfig(heading, text="English", fill="white")
    bg_canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    bg_canvas.itemconfig(bg_card, image=card_back_img)


def known_word():
    global current_card
    known_words.append(current_card)

    # remove current_card 
    data.remove(current_card)
    output = pd.DataFrame(data)

    output.to_csv("day_031/project/data/words_to_learn.csv", index=False)

    generate_word_group()

data = load_data()
known_words = []
############## UI ###############

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file = CARD_BACK)
card_front_img =  PhotoImage(file = CARD_FRONT)

bg_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_card = bg_canvas.create_image((400, 263), image=card_front_img)
heading = bg_canvas.create_text((400, 150), font=("Ariel", 40, "italic"))
word_label = bg_canvas.create_text((400, 263), font=("Ariel", 60, "bold"))
bg_canvas.grid(column=0,row=0, columnspan=2)

wrong_btn_img = PhotoImage(file = WRONG)
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=generate_word_group)
wrong_btn.grid(column=0, row=1)

right_btn_img =  PhotoImage(file = RIGHT)
right_btn = Button(image=right_btn_img, highlightthickness=0, command=known_word)
right_btn.grid(column=1, row=1)

flip_timer = window.after(3000, flip_card)

generate_word_group()

window.mainloop()
