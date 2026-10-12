from rock_paper_scissors import *
Tickets = 0
game_list = ["rock paper scissors", "number guesser"]
exit = False
while exit = False: 
    print("Welcome to Mr Pythons Carnival Of Fun")
    print("""The Game Selection is 
    Rock Paper Scissors
    Number Guesser
    """)
    game = input("What Game Would You Like To Play")
    if game.lower not in game_list:
        print("Error: That Game Is Not In The Catalog")
    else:
        if game.lower == "rock paper scissors"
            rock_paper_scissors(Tickets)