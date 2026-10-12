import random
import os
points = 0
cpoints = 0
def rock_paper_scissors(ticket):
    os.system('cls' if os.name == 'nt' else 'clear')
    global points
    global cpoints
    while points < 3 and cpoints < 3:
        print(f"Your Points: {points}")
        print(f"Computer Points: {cpoints}")
        computer = random.randint(1, 4)
        if computer == 1:
            guess = "Rock"
        elif computer == 2:
            guess = "Paper"
        elif computer == 3:
            guess = "Scissors"
        proper = False
        while proper == False:
            proper = True
            pguess = input("Your Guess: ")
            if pguess != "Rock" and pguess != "Scissors" and pguess != "Paper" and pguess != "Exit":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Throw, Try Again")
                proper = False
                input()
            os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You Guessed: {pguess}")
        print(f"Computer Guessed: {guess}")
        if pguess == "Rock":
            if guess == "Paper":
                print("You Lose")
                cpoints += 1
            if guess == "Scissors":
                print("You Win")
                points += 1
            if guess == "Rock":
                print("Its A Tie")
        if pguess == "Paper":
            if guess == "Scissors":
                print("You Lose")
                cpoints += 1
            if guess == "Rock":
                print("You Win")
                points += 1
            if guess == "Paper":
                print("Its A Tie")
        if pguess == "Scissors":
            if guess == "Rock":
               print("You Lose")
               cpoints += 1
            if guess == "Paper":
                print("You Win")
                points += 1
            if guess == "Scissors":
                print("Its A Tie")
        if pguess == "Exit":
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    if cpoints > points:
        print ("You Have Lost")
    else:
        print ("You Win")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')

    
rock_paper_scissors(0)