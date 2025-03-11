import pandas as pd 


def get_user_word():
    global nato_alpha_dict

    user_word = input("Please enter your word: ")
    user_word = user_word.lower()

    try: 
        for char in user_word: 
            if char in nato_alpha_dict.keys():
                pass
            else:
                raise KeyError
    except KeyError:
        print("Sorry, only letters of the alphabet please.")
        user_word = get_user_word()

    return user_word

data = pd.read_csv("day_026/project/nato_phonetic_alphabet.csv")

# new_dict = {new_key: new_value for (index, row) in df.iterrows() if test}
nato_alpha_dict = {row.letter.lower(): row.code for (idx, row) in data.iterrows()}

user_word = get_user_word()

# new_list = [new_item for item in list]
response = [nato_alpha_dict[letter] for letter in user_word]

print(response)