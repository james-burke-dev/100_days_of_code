from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInteface:

    def __init__(self, quiz_brain:QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("The Quiz App")
        
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.bg_canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.bg_canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.bg_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="day_034/project/images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2,column=1)

        false_image = PhotoImage(file="day_034/project/images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.false_btn.grid(row=2,column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.bg_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")

            q_text = self.quiz.next_question()
            self.bg_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.bg_canvas.itemconfig(self.question_text, text="No more Questions available")
            self.true_btn.config(state="disbaled")
            self.false_btn.config(state="disbaled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.bg_canvas.config(bg="Green")
        else:
            self.bg_canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
            
    
    