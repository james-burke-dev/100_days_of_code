control = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(mode, message, shift):
    message = list(message)
    if mode == 'encode':
        for letter in message:
            message[message.index(letter)] = alphabet[alphabet.index(letter) + shift]
        print(f"Here is the encoded result:  {"".join(message)}")

    elif mode == 'decode':
        for letter in message:
            message[message.index(letter)] = alphabet[alphabet.index(letter) - shift]
        print(f"Here is the decoded result:  {"".join(message)}")
    else:
        print("Incorrect mode detected. Wiping all data. Terminating... ")


def main():
    print("Welcome to the Caeser Cipher!")

    while control == True:

        mode = str(input("Type 'encode' to encrypt, type 'decode' to decrypt\n"))

        message = str(input("What is the message?\n"))

        shift = int(input("How many letters would you like to shift?\n"))

        cipher(mode, message, shift)

        again = str(input("Type 'yes' if you want to go again \n"))

        if again != 'yes':
            control == False

main()
