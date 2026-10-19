import random
import os
import time
cards = [
    {"Ace": "Hearts"},
    {"Two": "Hearts"},
    {"Three": "Hearts"},
    {"Four": "Hearts"},
    {"Five": "Hearts"},
    {"Six": "Hearts"},
    {"Seven": "Hearts"},
    {"Eight": "Hearts"},
    {"Nine": "Hearts"},
    {"Ten": "Hearts"},
    {"Jack": "Hearts"},
    {"Queen": "Hearts"},
    {"King": "Hearts"},

    {"Ace": "Diamonds"},
    {"Two": "Diamonds"},
    {"Three": "Diamonds"},
    {"Four": "Diamonds"},
    {"Five": "Diamonds"},
    {"Six": "Diamonds"},
    {"Seven": "Diamonds"},
    {"Eight": "Diamonds"},
    {"Nine": "Diamonds"},
    {"Ten": "Diamonds"},
    {"Jack": "Diamonds"},
    {"Queen": "Diamonds"},
    {"King": "Diamonds"},

    {"Ace": "Clubs"},
    {"Two": "Clubs"},
    {"Three": "Clubs"},
    {"Four": "Clubs"},
    {"Five": "Clubs"},
    {"Six": "Clubs"},
    {"Seven": "Clubs"},
    {"Eight": "Clubs"},
    {"Nine": "Clubs"},
    {"Ten": "Clubs"},
    {"Jack": "Clubs"},
    {"Queen": "Clubs"},
    {"King": "Clubs"},

    {"Ace": "Spades"},
    {"Two": "Spades"},
    {"Three": "Spades"},
    {"Four": "Spades"},
    {"Five": "Spades"},
    {"Six": "Spades"},
    {"Seven": "Spades"},
    {"Eight": "Spades"},
    {"Nine": "Spades"},
    {"Ten": "Spades"},
    {"Jack": "Spades"},
    {"Queen": "Spades"},
    {"King": "Spades"}
]

class player:
    def __init__(self, deckdict):
        self.type = type
        self.deck = deckdict
        self.points = 0

    def flip(deck):
        random.shuffle(self.deck)
        top_card = self.deck[0]
        self.deck.remove(self.deck[0])
        return top_card
    
    def win(card):
        self.points += 1
        self.deck.append(card)

def war(tickets):
    os.system('clear')
    computer = player(cards)
    person = player(cards)
    want = input(f"""You Have {person.points} Points. The Computer Has {computer.points} Points"
    Please Press Enter To Commence War, Or Type Exit To Exit. Exiting Would Earn You {person.points // 2} Points""")
    if want.lower() == "exit":
        print(f"You Have Earned {person.points // 2} Tickets. Thank You For Playing")
        print()
        input("Press Enter To Continue")
        os.system('clear')
        return person.points // 2
    else:
        print("3!")
        time.sleep(1)
        print("2!")
        time.sleep(1)
        print("1!")
        time.sleep(1)
        print("WAR!")
        comp = computer.flip
        play = person.flip
        print(f"You Flip {play}")
        print(f"Computer Flips {play}")
        