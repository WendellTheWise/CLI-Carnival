import os
import random
import time
cards = [
    ("Ace",  "Hearts"),
    ("Two", "Hearts"),
    ("Three", "Hearts"),
    ("Four", "Hearts"),
    ("Five", "Hearts"),
    ("Six", "Hearts"),
    ("Seven", "Hearts"),
    ("Eight", "Hearts"),
    ("Nine", "Hearts"),
    ("Ten", "Hearts"),
    ("Jack", "Hearts"),
    ("Queen", "Hearts"),
    ("King", "Hearts"),

    ("Ace", "Spades"),
    ("Two", "Spades"),
    ("Three", "Spades"),
    ("Four", "Spades"),
    ("Five", "Spades"),
    ("Six", "Spades"),
    ("Seven", "Spades"),
    ("Eight", "Spades"),
    ("Nine", "Spades"),
    ("Ten", "Spades"),
    ("Jack", "Spades"),
    ("Queen", "Spades"),
    ("King", "Spades"),

    ("Ace", "Clubs"),
    ("Two", "Clubs"),
    ("Three", "Clubs"),
    ("Four", "Clubs"),
    ("Five", "Clubs"),
    ("Six", "Clubs"),
    ("Seven", "Clubs"),
    ("Eight", "Clubs"),
    ("Nine", "Clubs"),
    ("Ten", "Clubs"),
    ("Jack", "Clubs"),
    ("Queen", "Clubs"),
    ("King", "Clubs"),

    ("Ace", "Diamonds"),
    ("Two", "Diamonds"),
    ("Three", "Diamonds"),
    ("Four", "Diamonds"),
    ("Five", "Diamonds"),
    ("Six", "Diamonds"),
    ("Seven", "Diamonds"),
    ("Eight", "Diamonds"),
    ("Nine", "Diamonds"),
    ("Ten", "Diamonds"),
    ("Jack", "Diamonds"),
    ("Queen", "Diamonds"),
    ("King", "Diamonds")
]

def fish(tickets):
    global cards
    playmatches = []
    compmatches = []
    deck = cards[:]
    random.shuffle(deck)
    comp_hand = deck[:7]
    play_hand = deck[7:14]
    deck = deck[14:]
    while len(play_hand) > 0 or len(comp_hand) > 0:
        for card in play_hand:
            for checksum in play_hand:
                if card[0] == checksum[0] and card[1] != checksum[1]:
                    play_hand.remove(card)
                    play_hand.remove(checksum)
                    playmatches.append((card, checksum))
                    break
        for card in comp_hand:
            for checksum in comp_hand:
                if card[0] == checksum[0] and card[1] != checksum[1]:
                    comp_hand.remove(card)
                    comp_hand.remove(checksum)
                    compmatches.append((card, checksum))
        try:
            askfor = int(input(f""" 
            Current Player Matches {len(playmatches)}
            {playmatches}

            Current Computer Matches
            {compmatches}

            Your Hand Is: 
            {list(play_hand)}

            Please Enter A Card Number In Your Hand (1 For The First On The Left, 2 For The Second On The Left, Etc) In Your Hand: """)) - 1
        except:
            os.system('clear')
            print("Please Only Enter Integers")
            input("""
            Press Enter To Continue""")
            os.system('clear')
            continue

        if askfor >= len(list(play_hand)) or askfor < 0:
            os.system('clear')
            print("Please Only Enter Numbers That Coincide With A Card In Your Hand")
            input("""
            Press Enter To Contine""")
            os.system('clear')
            continue
        os.system('clear')
        old_hand = play_hand[:]
        for check in comp_hand:
            if check[0] == play_hand[askfor][0]:
                print("Computer Has It")
                play_hand.append(check)
                print(check)
                comp_hand.remove(check)
                print()
                input("Press Enter To Continue")
        if old_hand == play_hand:
            if len(deck) > 0:
                print("Go Fish")
                play_hand.append(deck[0])
                print(f"You Draw {deck[0]}")
                deck.remove(deck[0])
                print()
                input("Press Enter To Continue")
            else:
                print("The Deck Is Empty, No New Cards May Be Drawn")
        
fish(0)