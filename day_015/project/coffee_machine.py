MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


def turn_off():
    print("Goodbye")
    exit()

def display_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")

def check_resources(coffee):
    if (resources['water'] > MENU[coffee]['ingredients']['water']):
        if (resources['coffee'] > MENU[coffee]['ingredients']['coffee']):
            if(coffee == 'espresso'):
                return True
            else:
                if (resources['milk'] > MENU[coffee]['ingredients']['milk']):
                    return True
                else:
                    print("Sorry there is not enough coffee")
                    return False
        else:
            print("Sorry there is not enough coffee")
            return False
    else:
        print("Sorry there is not enough water")
        return False

def process_coins():
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickles = int(input("Enter number of nickles: "))
    pennies = int(input("Enter number of pennies: "))

    value = round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01),2)

    return value

def check_transaction(coins, coffee):
    if (coins < MENU[coffee]['cost']):
        print("Sorry that's not enough money. Money refunded.")
        main()
    elif (coins > MENU[coffee]['cost']):
        money['value'] += MENU[coffee]['cost']
        print(f"Here is ${coins - MENU[coffee]['cost']} dollars in change")
    else:
        money["value"] += MENU[coffee]['cost']

def make_coffee(coffee):
    if (coffee == 'espresso'):
        resources["water"] -= MENU[coffee]['ingredients']['water']
        resources["coffee"] -= MENU[coffee]['ingredients']['coffee']
    else:
        resources["water"] -= MENU[coffee]['ingredients']['water']
        resources["coffee"] -= MENU[coffee]['ingredients']['coffee']
        resources["milk"] -= MENU[coffee]['ingredients']['milk']
        
def main():
    control = True
    while control == True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if (choice == 'report'):
            display_report()
        elif (choice == 'off'):
            turn_off()
        else:
            if (choice == 'espresso') or (choice == 'latte') or (choice == 'cappuccino'):
                check_resources(choice)

                coins = process_coins()

                check_transaction(coins, choice)

                make_coffee(choice)

                print(f"Here is your {choice}. Enjoy!")

            else:
                print("Invalid Selection. Try again")
                main()




main()