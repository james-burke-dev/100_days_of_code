import random

lives = 0
guess = -1

def generate_answer():
    return random.randint(1,100)

def get_difficulty():
    difficulty = input("Select a difficulty, 'easy' or 'hard': ")

    if (difficulty == 'easy'):
        return 10
    elif(difficulty == 'hard'):
        return 5
    else:
        print("Difficulty not set, please try again")
        get_difficulty()

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

answer = generate_answer()

lives = get_difficulty()

while guess != answer and lives > 0:
    guess = int(input("Make a guess: "))

    if guess == answer: 
        print("Correct answer - You Win!")
    elif (guess < answer):
        print("Too low - Guess Again")
        lives -= 1
    elif(guess > answer):
        print("Too high - Guess Again")
        lives -= 1

if lives < 1: 
    print("Out of lives - You Lose")

print(f"The number was {answer}")