# new_list = [new_item for item in list]

numbers = [1,2,3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

name = "James"
letters_list = [letter for letter in name]
print(letters_list)

doubled = [num * 2 for num in range(1,5)]
print(doubled)

# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

# new_dict = {key: value for (key, value) in dict.items()}