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
ranks = [
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
    ("King", "Hearts"),]

suits = [
    "Diamonds",
    "Clubs",
    "Spades",
    "Hearts"
]

def fish(tickets):
    global cards
    playmatches = []
    compmatches = []
    counter = 0
    adder = []
    deck = cards[:]
    random.shuffle(deck)
    comp_hand = deck[:7]
    play_hand = deck[7:14]
    deck = deck[14:]
    while len(playmatches) + len(compmatches) < 13:
        for typing in ranks:
            counter = 0
            for card in play_hand:
                if card[0] == typing[0]:
                    counter  += 1
            for card in play_hand[:]:
                if counter == 4 and card[0] == typing[0]:
                    play_hand.remove(card)
                    adder.append(card)
        if adder:
            playmatches.append(adder)
        adder = []

        for typing in ranks:
            counter = 0
            for card in comp_hand:
                if card[0] == typing[0]:
                    counter  += 1
            for card in comp_hand[:]:
                if counter == 4 and card[0] == typing[0]:
                    comp_hand.remove(card)
                    adder.append(card)
        if adder:
            compmatches.append(adder)
        adder = []

        try:
            askfor = int(input(f""" 
            Current Player Matches {len(playmatches)}
            {playmatches}

            Current Computer Matches {len(compmatches)}
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
        os.system('clear')
        print("Its The Computers Turn")
        random.shuffle(comp_hand)
        if len(comp_hand) > 0:
            take = comp_hand[0]
            print(f"The Computer Asks For {take}")
            old_comp = comp_hand[:]
            for cm in play_hand[:]:
                if take[0] == cm[0]:
                    print(f"The Computer Has Taken Your {cm}")
                    play_hand.remove(cm)
                    comp_hand.append(cm)
                    input("""
                    Press Enter To Continue""")
            if old_comp == comp_hand:
                if len(deck) > 0:
                    print("Go Fish")
                    comp_hand.append(deck[0])
                    deck.remove(deck[0])
                else:
                    print("The Deck Is Empty, No New Cards May Be Drawn")
                print()
                input("Press Enter To Continue")
        if len(comp_hand) <= 0:
            print("The Computers Hand Is Empty, Automatic Go Fish")
            comp_hand.append(deck[0])
            deck.remove(deck[0])
            print()
            input("Press Enter To Continue")
fish(0)