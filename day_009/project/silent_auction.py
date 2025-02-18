import os

bids = {}

def find_highest_bidder():
    return max(bids, key=bids.get), max(bids.values())

def main():
    more_bids = True
    print("Welcome to the silent auction! ")

    while more_bids == True:
        name = input("What is your name?: ")
        bid =  int(input("What is your bid?: "))

        bids[name] = bid

        control = str(input("Are there any other bidders? Type 'yes' or 'no': "))

        if control == 'no':
            more_bids = False
            name, bid = find_highest_bidder()
            print(f"The winner is {name} with a bid of ${bid}")
        else:
            os.system('clear')

main()