
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip_perc = int(input("How much tip would you like to leave? 10, 12 or 15? "))
num_people = int(input("How many people are splitting the bill? "))

per_person_price = round((total + (tip_perc / 100 * total)) / num_people, 2)

print(f"Each person should pay: ${per_person_price}")
