
from tkinter import *
import time
import math 

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
TOMATO_PATH = "day_028/project/tomato.png"
CHECK_MARK = "✓"

reps = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    bg_canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: 
        print(f"Long: {reps % 8}")
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0: 
        print(f"Short: {reps % 2}")
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        print(f"Work: {reps}")
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count_time):
    global reps
    count_mins = math.floor(count_time / 60)
    count_seconds = count_time % 60

    if count_seconds in range(0,10):
        count_seconds = "0" + str(count_seconds)

    bg_canvas.itemconfig(timer_text, text=f"{count_mins}:{count_seconds}")
    if count_time > 0: 
        global timer
        timer = window.after(1000, countdown, count_time - 1 )
    else:
        start_timer()

        if reps % 2 == 0: 
            check_mark_label.config(text=f"{CHECK_MARK * round(reps/2)}")
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
#window.minsize()
window.config(padx=50, pady=50, bg=YELLOW)

bg_img = PhotoImage( file = TOMATO_PATH)

bg_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_canvas.create_image(100, 112, image=bg_img)
timer_text = bg_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
bg_canvas.grid(column=1,row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1,row=0)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=3,row=2)

check_mark_label = Label(text=f"{CHECK_MARK * 0}", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check_mark_label.grid(column=1,row=3)

window.mainloop()
