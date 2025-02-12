art = '''         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|'''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Would you like to head left or right? ")

if direction == "right":
    print("You arrive at a lake")
    choice = input("Would you like to swim or wait? ")

    if(choice == "wait"):
        print("You arrive at a set of three doors.")
        door = input("Which door do you enter, Red, Yellow or Blue? ")

        if(door.lower() == "yellow"):
            print("You win! Here is your treasure")
            print(art)

        elif(door.lower() == "red"):
                print("You fall into a fire.")
                print("Game Over.")
                exit()

        elif(door.lower() == "blue"):
                print("You are eaten by beasts.")
                print("Game Over.")
                exit()

        else:
            print("Game Over.")
            exit()

    else:
        print("You are pulled under the water.")
        print("Game Over.")
        exit()

else: 
    print("You fall in a hole.")
    print("Game Over.")
    exit()

