import random

choices = ["Rock", "Paper", "Scissors"]

player_choice = int(input("Enter your choice (0 for Rock, 1 for Paper or 2 for Scissors): "))

if player_choice < 0 or player_choice > 2:
    print("Invalid selection. You Lose!")
else:
    print(f"You chose: {choices[player_choice]}")

    computer_choice = random.randint(0,2)
    print(f"Computer chose: {choices[computer_choice]}")

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif player_choice < computer_choice: 
        print("You Lose!")
    elif player_choice > computer_choice:
        print("You win!")
    else:
        print("It's a Tie!")
