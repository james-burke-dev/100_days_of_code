from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
items = menu.get_items()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

def main():
    control = True
    while control == True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if (choice == 'report'):
            coffee_machine.report()
            money_machine.report()
        elif (choice == 'off'):
            exit()
        else:
            if (choice in menu.get_items()):
                item = menu.find_drink(choice)

                payment = money_machine.make_payment(item.cost)
                if payment == True:
                    coffee_machine.make_coffee(item)
            else:
                print("Invalid Selection. Try again")
                
                
main()