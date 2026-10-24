from pathlib import Path

LEADERBOARD = Path.home() / ".cli_carnival" / "leaderboard.txt"
LEADERBOARD.parent.mkdir(parents=True, exist_ok=True)
LEADERBOARD.touch(exist_ok=True)
from rock_paper_scissors import *
from Number_Guesser import *
from chance import *
from gofish import *
from typer import *
from hangman import *
from mastermind import *
from anagram import *
from cardwar import *
from simonsays import *
from wallet import *
from moreorless import *
import os
Tickets = 5
game_list = ["rock paper scissors", "number guess", "exit", "1", "2", "3", "chance", "4", "hangman", "5", "mastermind", "6", "anagrams", "7", "war", "8", "reset", "simon", "9", "go fish", "10", "typing test", "11", "higher or lower", "12", "retrieve"]
exit = False
while exit == False: 
    os.system('clear')
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
    print(f"Your Current Tickets Count Is {Tickets}")
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
    8: Simon : 10
    9: Go Fish : 4
    10: Typing Test : 5
    11: Higher or Lower : 2
    12: Exit
    Enter "Retrieve" To Set Tickets To A Previously Logged Amount
    Or Enter "Reset" To Reset The Leaderboard
    """)
    game = input("What Game Would You Like To Play? ").lower()
    if game not in game_list:
        os.system('clear')
        print("Error: That Game Is Not In The Catalog")
        input("")
        os.system('clear')
    else:
        if game == "rock paper scissors" or game == "1":
            os.system('clear')
            if Tickets < 2:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 2
                new_Tickets = rock_paper_scissors(Tickets)
                Tickets += new_Tickets
                os.system('clear')
        if game == "number guess" or game == "2":
            os.system('clear')
            if Tickets < 5:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 5
                new_Tickets = guesser(Tickets)
                Tickets += new_Tickets
                os.system('clear')
        
        if game == "chance" or game == "3":
            try:
                os.system('clear')
                Tickets += chance(Tickets)
                os.system('clear')

            except:
                os.system('clear')
                print("Please Enter A Valid, Non-Negative Integer")
                print()
                input("Press Enter To Continue")
                
        if game == "hangman" or game == "4":
            os.system('clear')
            if Tickets < 3:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                os.system('clear')
                Tickets -= 3
                new_Tickets = hangman(Tickets)
                Tickets += new_Tickets
                os.system('clear')
            os.system('clear')

        if game == "mastermind" or game == "5":
            os.system('clear')
            if Tickets < 4:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 4
                new_Tickets = mastermind(Tickets)
                Tickets += new_Tickets
                os.system('clear')

        if game == "anagrams" or game == "6":
            os.system('clear')
            if Tickets < 2:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 2
                new_Tickets = anagram(Tickets)
                Tickets += new_Tickets
                os.system('clear')

        if game == "war" or game == "7":
            os.system('clear')
            if Tickets < 8:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 8
                new_Tickets = war(Tickets)
                Tickets += new_Tickets
                os.system('clear')

        if game == "simon" or game == "8":
            os.system('clear')
            if Tickets < 10:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor to Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 10
                new_Tickets = simon(Tickets)
                Tickets += new_Tickets
                os.system('clear')
                
        if game == "go fish" or game == "9":
            os.system('clear')
            if Tickets <  4:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor To Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 4
                new_Tickets = fish(Tickets)
                Tickets += new_Tickets
                os.system('clear')

        if game == "typing test" or game == "10":
            os.system('clear')
            if Tickets < 5:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor To Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Press Enter To Continue")
            else:
                Tickets -= 5
                new_Tickets = typing(Tickets)
                Tickets += new_Tickets
                os.system('clear')
        
        if game == "higher or lower" or game == "11":
            os.system('clear')
            if Tickets < 2:
                print("Oh Hoh Hoh, My Good Man, You Are Much Too Poor To Play This Game. Go Get Yourself Some More Tickets")
                print()
                input("Pres Enter To Contine")
            else:
                Tickets -= 2
                new_Tickets = moreorless(Tickets)
                Tickets += new_Tickets
                os.system('clear')

        if game == "retrieve":
            os.system('clear')
            Tickets = retrieve(input("Please Enter The Name Of A Player On The Leaderboard: "))
            os.system('clear')

        if game == "reset":
            os.system('clear')
            with open(LEADERBOARD, "w") as f:
                f.write("")

        if game == "exit" or game == "12":
            exit = True
            os.system('clear')
            correct = True
            while correct == True:
                correct = False
                question = input("Would You Like To Save Your Tickets On The Leaderboard. Y/N: ").lower()
                if question.lower() != "y" and question.lower() != "n" and question.lower() != "yes" and question.lower() != "no":
                    os.system('clear')
                    input(""" Please Make Sure Your Answer Is Either Yes, No, Y, or N. 
                
                    Press Enter To Continue""")
                    correct = True

            if question == "y" or question == "yes":
                os.system('clear')
                name = input("Please Enter A Name For You: ")
                with open(LEADERBOARD, "a") as f:
                    f.write(f"{name} Has Earned {Tickets} Tickets\n")
            break
