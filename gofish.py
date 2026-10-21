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
    for card in play_hand:
        for checksum in play_hand:
            if card[0] == checksum[0] and card[1] != checksum[1]:
                play_hand.remove(card)
                play_hand.remove(checksum)
                playmatches.append((card, checksum))
    for card in comp_hand:
        for checksum in comp_hand:
            if card[0] == checksum[0] and card[1] != checksum[1]:
                comp_hand.remove(card)
                comp_hand.remove(checksum)
                compmatches.append((card, checksum))
    
    askfor = input(f""" 
    Current Player Matches 
    {playmatches}

    Current Computer Matches
    {compmatches}

    Your Hand Is: 
    {list(play_hand)}

    Please Enter A Card Number In Your Hand (1 For The First On The Left, 2 For The Second On The Left, Etc) In Your Hand: """)
fish(0)