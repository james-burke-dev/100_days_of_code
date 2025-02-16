import requests
import random
intro_art = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/               
'''
def get_game_word():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = str(random.choice(WORDS))
    
    # Cleanup word
    word = word[1:len(word)]
    word = word.replace("'","")

    return word

def main():
    '''Main execution for the game'''

    print(intro_art)

    lives = 5
    answer = get_game_word()
    guess_string = ["_" for letter in answer]

    while lives > 0:

        # Check if the current string of guesses is equal to the answer & exit if the player wins 
        if("".join(guess_string) == answer):

            print(f"\nCongrats, you win! \nThe word was {answer}")
            exit()

        print(f"\nWord to guess: {"".join(guess_string)}")
        guess = str(input("Guess a letter: "))

        # Check an individual letter guessed is in the answer 
        if guess in answer:
            indices = [i for i, val in enumerate(answer) if val == guess]
            
            for index in indices:
                guess_string[index] = guess

        else:
            lives -= 1
            print("Letter not found in word")
            print(f"Lives left: {lives}")
    print("\nOut of lives, you lose!")
    print(f"The word was {answer}")
    exit()


main()