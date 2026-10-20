import random
import os
import time
cards = [
    {"Ace of Hearts": 1},
    {"Two of Hearts": 2},
    {"Three of Hearts": 3},
    {"Four of Hearts": 4},
    {"Five of Hearts": 5},
    {"Six of Hearts": 6},
    {"Seven of Hearts": 7},
    {"Eight of Hearts": 8},
    {"Nine of Hearts": 9},
    {"Ten of Hearts": 10},
    {"Jack of Hearts": 11},
    {"Queen of Hearts": 12},
    {"King of Hearts": 13},

    {"Ace of Spades": 1},
    {"Two of Spades": 2},
    {"Three of Spades": 3},
    {"Four of Spades": 4},
    {"Five of Spades": 5},
    {"Six of Spades": 6},
    {"Seven of Spades": 7},
    {"Eight of Spades": 8},
    {"Nine of Spades": 9},
    {"Ten of Spades": 10},
    {"Jack of Spades": 11},
    {"Queen of Spades": 12},
    {"King of Spades": 13},

    {"Ace of Clubs": 1},
    {"Two of Clubs": 2},
    {"Three of Clubs": 3},
    {"Four of Clubs": 4},
    {"Five of Clubs": 5},
    {"Six of Clubs": 6},
    {"Seven of Clubs": 7},
    {"Eight of Clubs": 8},
    {"Nine of Clubs": 9},
    {"Ten of Clubs": 10},
    {"Jack of Clubs": 11},
    {"Queen of Clubs": 12},
    {"King of Clubs": 13},

    {"Ace of Diamonds": 1},
    {"Two of Diamonds": 2},
    {"Three of Diamonds": 3},
    {"Four of Diamonds": 4},
    {"Five of Diamonds": 5},
    {"Six of Diamonds": 6},
    {"Seven of Diamonds": 7},
    {"Eight of Diamonds": 8},
    {"Nine of Diamonds": 9},
    {"Ten of Diamonds": 10},
    {"Jack of Diamonds": 11},
    {"Queen of Diamonds": 12},
    {"King of Diamonds": 13}
]

class player:
    def __init__(self, deckdict):
        self.type = type
        self.deck = deckdict
        self.points = 0

    def flip(self, deck):
        random.shuffle(self.deck)
        top_card = self.deck[0]
        self.deck.remove(self.deck[0])
        return top_card
    
    def win(self, card):
        self.points += 1
        self.deck.append(card)

def war(tickets):
    exit = False
    computer = player(cards.copy())
    person = player(cards.copy())
    while exit == False:
        os.system('clear')
        want = input(f"""You Have {person.points} Points. The Computer Has {computer.points} Points
        Please Press Enter To Commence War, Or Type Exit To Exit. Exiting Would Earn You {person.points // 2} Points: """)
        os.system('clear')
        if want.lower() == "exit":
            print(f"You Have Earned {person.points // 2} Tickets. Thank You For Playing")
            print()
            input("Press Enter To Continue")
            os.system('clear')
            exit = True
            return person.points // 2
        else:
            print("3!")
            time.sleep(0.5)
            print("2!")
            time.sleep(0.5)
            print("1!")
            time.sleep(0.5)
            print("WAR!")
            comp = computer.flip(computer.deck)
            play = person.flip(person.deck)
            print(f"You Flip {list(play)}")
            print(f"Computer Flips {list(comp)}")
            print(comp.values())
            if list(comp.values()) > list(play.values()):
                print("Computer Wins!")
                computer.win(play)
            elif list(play.values()) > list(comp.values()):
                print("You Win!")
                person.win(comp)
            else:
                print("Its A Tie!")
            print()
            input("Press Enter To Continue")
            os.system('clear')
