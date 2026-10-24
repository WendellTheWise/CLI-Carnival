import random
import os
from cards import *
from gofish import cards

def moreorless(tickets):
    os.system('clear')
    pull = pullcard()
    good = False
    while good == False:
        print(pull[0])
        print(pull[1])
        good = True
        response = input("Do You Think That The Next Card Will Be Higher, Or Lower Than This Card? ").lower()
        if response != "lower" and response != "higher":
            os.system('clear')
            print("Please Make Sure Your Answer Is Either Higher, or Lower")
            print()
            input("Press Enter To Continue")
            os.system('clear')
            good = False
        secondpull = pullcard()
        print(
        secondpull[0],
        secondpull[1])
        if response == "higher":
            if pull[3] < secondpull[3]:
                print("You Win 4 Tickets")
                print()
                input("Press Enter To Continue")
                return 4
            else:
                print("You Lose")
                print()
                input("Press Enter To Continue")
                return 0

        if response == "lower":
            if pull[3] > secondpull[3]:
                print("You Win 4 Tickets")
                print()
                input("Press Enter To Continue")
                return 4
            else:
                print("You Lose")
                print()
                input("Press Enter To Continue")
                return 0
    os.system('clear')









    
