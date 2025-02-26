class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")

        self.check_answer(current_question.answer, guess)
        print("\n")
        print("\n")


    def still_has_questions(self):
        if(self.question_number < len(self.question_list)):
            return True
        else:
            return False

    def check_answer(self, answer ,guess):
        if( guess == answer): 
            print("Correct Answer!")
            self.score += 1
        else:
            print("Incorrect Answer :( ")
        print(f"The correct answer was {answer}")
        print(f"Current score {self.score}/{self.question_number}")
    
