def add(num1, num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def main():
    control = 'y'
    answer = 0

    first_num = float(input("What's the first number?: "))

    while control == 'y': 
        operator = input("Pick an operation (+, -, *, /): ")

        second_num = float(input("What's the next number?: "))

        if (operator == '+'):
            answer = add(first_num, second_num)
            print(f"{first_num} + {second_num} = {answer}")
            first_num = answer

        elif (operator == '-'):
            answer = subtract(first_num, second_num)
            print(f"{first_num} - {second_num} = {answer}")
            first_num = answer

        elif (operator == '*'):
            answer = multiply(first_num, second_num)
            print(f"{first_num} * {second_num} = {answer}")
            first_num = answer

        elif (operator == '/'):
            answer = divide(first_num, second_num)
            print(f"{first_num} / {second_num} = {answer}")
            first_num = answer
        else: 
            print("Invalid operation - Exiting")
            exit()

        control = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calulation: ")

        if (control == 'n'):
            main()

main()
