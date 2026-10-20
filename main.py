from pathlib import Path

LEADERBOARD = Path.home() / ".cli_carnival" / "leaderboard.txt"
LEADERBOARD.parent.mkdir(parents=True, exist_ok=True)
LEADERBOARD.touch(exist_ok=True)
from Carnival.rock_paper_scissors import *
from Carnival.Number_Guesser import *
from Carnival.chance import *
from Carnival.hangman import *
from Carnival.mastermind import *
from Carnival.anagram import *
from Carnival.cardwar import *
Tickets = 5
game_list = ["rock paper scissors", "number guess", "exit", "1", "2", "3", "chance", "4", "hangman", "5", "mastermind", "6", "anagram", "7", "War", "8"]
exit = False
while exit == False: 
    if Tickets <= 0:
        print(Tickets)
        print("Sorry, You Are Too Poor, Why Dont You Come Back When You Are A Little, Hmm, Richer")
        print(""
        )
        exit = False
        input()
        break
    os.system('clear')
    print("Welcome to Mr Pythons Carnival Of Fun")
    print("")
    print(f"Your Current Ticket Count Is {Tickets}")
    print("")
    with open(LEADERBOARD) as f:
        leader = [line.strip() for line in f if line.strip()]
    leader.sort(key=lambda line: int(line.split()[-2]), reverse=True)
    print("The Current Leaderboard:\n")
    for line in leader:
        print(line)
    print()
    print("""The Game Selection And Their Costs Are 
    1: Rock Paper Scissors : 2 Tickets
    2: Number Guess : 5 Tickets
    3: Chance : Wagerable
    4: Hangman : 3
    5: Mastermind : 4
    6: Anagrams : 2
    7: War : 8
    8: Exit
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
        if game == "hangman" or game == "4":
            os.system('clear')
            Tickets -= 3
            Tickets += hangman(Tickets)
            os.system('clear')
        if game == "mastermind" or game == "5":
            os.system('clear')
            Tickets -= 4
            Tickets += mastermind(Tickets)
            os.system('clear')
        if game == "anagrams" or game == "6":
            os.system('clear')
            Tickets -= 2
            Tickets += anagram(Tickets)
            os.system('clear')
        if game == "war" or game == "7":
            os.system('clear')
            Tickets -= 7
            Tickets += war(Tickets)
            os.system('clear')
        if game == "exit" or game == "8":
            exit = True
            os.system('clear')
            correct = True
            while correct == True:
                correct = False
                question = input("Would You Like To Save Your Tickets On The Leaderboard. Y/N: ").lower()
                if question.lower() != "y" and question.lower() != "n" and question.lower() != "yes" and question.lower() != "n":
                    os.system('clear')
                    input(""" Please Make Sure Your Answer Is Either Yes, No, Y, or N. 
                
                    Press Enter To Continue""")
                    correct = True
            if question == "y" or "yes":
                os.system('clear')
                name = input("Please Enter A Name For You: ")
                with open(LEADERBOARD, "a") as f:
                    f.write(f"{name} Has Earned {Tickets} Tickets\n")
            break
