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
    deck = cards[:]
    random.shuffle(deck)
    comp_hand = deck[:7]
    play_hand = deck[7:14]
    deck = deck[14:]

    askfor = input(f""" Current Matches {matches}
    Your Hand Is
    {list(play_hand)}
    Please Enter A Card In Your Hand""")
fish(0)