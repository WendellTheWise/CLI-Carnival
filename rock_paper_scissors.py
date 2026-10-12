import random
import os
points = 0
cpoints = 0
def rock_paper_scissors(ticket):
    os.system('cls' if os.name == 'nt' else 'clear')
    global points
    global cpoints
    while points < 3 or cpoints < 3:
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
            if pguess != "Rock" and pguess != "Scissors" and pguess != "Paper":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Throw, Try Again")
                proper = False
            os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You Guessed: {pguess}")
        print(f"Computer Guessed: {guess}")
        if guess == "Rock":
            if pguess == "Paper":
                    print("You Lose")
                    cpoints += 1
            if pguess == "Scissors":
                    print("You Win")
                    points += 1
            else:
                    print("Its A Tie")
        if guess == "Paper":
                if pguess == "Scissors":
                    print("You Lose")
                    cpoints += 1
                if pguess == "Rock":
                    print("You Win")
                    points += 1
                else:
                    print("Its A Tie")
        if guess == "Scissors":
                if pguess == "Rock":
                    print("You Lose")
                    cpoints += 1
                if pguess == "Paper":
                    print("You Win")
                    points += 1
                else:
                    print("Its A Tie")
    os.system('cls' if os.name == 'nt' else 'clear')
    if cpoints > points:
        print ("You Have Lost")
    else:
        print ("You Win")
    os.system('cls' if os.name == 'nt' else 'clear')
rock_paper_scissors(0)