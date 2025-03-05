import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
# Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

print(dir_path)

letter_path = "./Input/Letters/starting_letter.txt"

names_path = "./Input/Names/invited_names.txt"

output_path = "./Output/ReadyToSend/"

PLACEHOLDER = "[name]"

with open(names_path) as name_fn:
    names = name_fn.readlines()

for name in names: 
    name = name.rstrip()
    with open(letter_path) as letter_fn:
        contents = letter_fn.read()
        contents.replace(PLACEHOLDER, name)
    
    with open(f"{output_path}/{name}.txt", "w") as named_letter:
        named_letter.writelines(contents)