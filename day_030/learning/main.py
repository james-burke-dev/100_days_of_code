import pandas as pd 


# Original Solution 
data = pd.read_csv("day_026/project/nato_phonetic_alphabet.csv")
letters = list(data['letter'])
codes = list(data['code'])

# new_dict = {new_key: new_value for item in list if test}
nato_alpha_dict = {letter.lower(): code for letter, code in zip(letters, codes)}


print(nato_alpha_dict)

user_word = input("Please enter your word: ")
user_word = user_word.lower()

# new_list = [new_item for item in list]
response = [nato_alpha_dict[letter] for letter in user_word]

print(response)

# Improved solution with Pandas dict comprehension 

data = pd.read_csv("day_026/project/nato_phonetic_alphabet.csv")

# new_dict = {new_key: new_value for (index, row) in df.iterrows() if test}
nato_alpha_dict = {row.letter.lower(): row.code for (idx, row) in data.iterrows()}

print(nato_alpha_dict)

user_word = input("Please enter your word: ")
user_word = user_word.lower()

# new_list = [new_item for item in list]
response = [nato_alpha_dict[letter] for letter in user_word]

print(response)