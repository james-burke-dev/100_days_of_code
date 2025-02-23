import os
from game_data import data 
import random

def get_player_choice(A, B):
    print(f"Compare A: {A['name']}, {A['description']} from {A['country']}")

    print("VS")

    print(f"Against B: {B['name']}, {B['description']} from {B['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if (choice == "A"):
        return A
    elif (choice == "B"):
        return B
    else:
        print("Invalid selection try again!")
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_elem(): 
    elem = random.choice(data)
    return elem

def main():
    lives = 1 
    score = 0
    A = get_elem()
    B = get_elem()

    while lives > 0: 
        choice = get_player_choice(A, B)

        if A['follower_count'] > B['follower_count']: 
            if choice['follower_count'] < A['follower_count']:
                clear()
                print("Incorrect Guess - You Lose!")
                print(f"Your score was: {score}")
                lives -= 1
            else:
                clear()
                score += 1
                print(f"Correct Guess! Current score: {score}")
                A = B 
                B = get_elem()


        elif A['follower_count'] < B['follower_count']:
            if choice['follower_count'] < B['follower_count']:
                clear()
                print("Incorrect Guess - You Lose!")
                print(f"Your score was: {score}")
                lives -= 1
            else:
                clear()
                score += 1
                print(f"Correct Guess! Current score: {score}")
                A = B 
                B = get_elem()
        else:
            print("Follower count equal")

    play_again = input("Would you like to play again? Type 'y' or 'n': ")

    if play_again == 'y':
        main()

main()