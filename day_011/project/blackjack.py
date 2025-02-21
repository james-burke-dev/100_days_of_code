import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def init_game():
    player_cards = get_cards(2)
    player_score = get_score(player_cards)

    comp_cards = get_cards(2)
    comp_score = get_score(comp_cards)

    return player_cards, player_score, comp_cards, comp_score

def get_score(hand):
    score = 0

    for i in range(0,len(hand)):
        score += hand[i]
    
    if score > 21 and 11 in hand:
        score -= 10
        hand.remove(11)
        hand.append(1)
    
    if score < 22 and len(hand) == 5: 
        score = 0

    return score

def display_card_state(player_cards, comp_cards):
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {comp_cards[0]}")

def get_cards(amount):
    holder = []
    for i in range(0,amount):
        holder.append(random.choice(cards))
    return holder

def final_hands(p_cards, c_cards):
    p_score = get_score(p_cards)
    c_score = get_score(c_cards)

    print(f"Your final hand: {p_cards}, final score: {p_score}")
    print(f"Computer's final hand: {c_cards}, final score: {c_score}")

def player_loop(player_hand, player_score, comp_hand):
    player_hand.append(get_cards(1)[0])

    player_score = get_score(player_hand)

    display_card_state(player_hand, comp_hand)

    if player_score > 21: 
        print("You've gone bust - Computer Wins")

        replay = input("Type 'y' to play again: ")

        if replay == 'y':
            main()
        else:
            exit()
    else:
        control = input("Type 'y' to get another card, type 'n' to pass: ")
        return control

def check_winner(player_hand, comp_hand):
    player_score = get_score(player_hand)
    comp_score = get_score(comp_hand)

    final_hands(player_hand, comp_hand)

    if player_score == comp_score:
        return "Draw"
    elif(player_score == 0):
        print("Blackjack - Player Wins")
    elif(comp_score == 0):
        print("Blackjack - Computer Wins")
    elif(player_score > comp_score):
        print("You win!")
    else:
        print("Computer Wins!")

def main():
    player_hand, player_score, comp_hand, comp_score = init_game()

    display_card_state(player_hand, comp_hand)
        
    control = input("Type 'y' to get another card, type 'n' to pass: ")

    while control == 'y':
        control = player_loop(player_hand, player_score, comp_hand)


    while get_score(comp_hand) < 17:
        comp_hand.append(get_cards(1)[0])
        
        comp_score = get_score(comp_hand)

        if (comp_score > 21):
            print("Computer's gone bust! - Player Wins")
            final_hands(player_hand, comp_hand)

            replay = input("Type 'y' to play again: ")

            if replay == 'y':
                main()
            else:
                exit()
    
    check_winner(player_hand, comp_hand)


    replay = input("Type 'y' to play again: ")

    if replay == 'y':
        main()
    else:
        exit()

main()