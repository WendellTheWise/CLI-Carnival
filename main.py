from rock_paper_scissors import *
from Number_Guesser import *
from chance import *
Tickets = 5
game_list = ["rock paper scissors", "number guess", "exit", "1", "2", "3", "chance", "4"]
exit = False
while exit == False: 
    if Tickets <= 0:
        print(Tickets)
        print("Sorry, You Are Too Poor, Why Dont You Come Back When You Are A Little, Hmm, Richer")
        exit = False
        input()
        break
    os.system('clear')
    print("Welcome to Mr Pythons Carnival Of Fun")
    print("")
    print(f"Your Current Ticket Count Is {Tickets}")
    print("")
    print("""The Game Selection And Their Costs Are 
    1: Rock Paper Scissors : 2 Tickets
    2: Number Guess : 5 Tickets
    3: Chance : Wagerable
    4: Exit
    """)
    game = input("What Game Would You Like To Play? ").lower()
    if game not in game_list:
        os.system('clear')
        print("Error: That Game Is Not In The Catalog")
        input("")
        os.system('clear')
    else:
        if game == "rock paper scissors" or game == "1":
            Tickets -= 2
            new_tickets = rock_paper_scissors(Tickets)
            Tickets += new_tickets
            os.system('clear')
        if game == "number guess" or game == 2:
            Tickets -= 5
            new_tickets = guesser(Tickets)
            Tickets += new_tickets
            os.system('clear')
        if game == "chance" or game == "3":
            os.system('clear')
            Tickets += chance(Tickets)
            os.system('clear')
        if game == "exit" or game == "4":
            exit = True
            break