import time
import random
import os
def guesser(ticket):
    previous = []
    number = random.randint(1, 101)
    correct = False
    os.system('clear')
    while correct != True:

        try:
            guess = int(input("Please Guess A Number: "))
            if number > guess:
                if number - guess >= 25:
                    print("Way Too Low")
                elif number - guess < 25 and number - guess > 5:
                    print("Too Low")
                elif number - guess <= 5:
                    print("Barely Too Low")
            if number < guess:
                if guess - number >= 25:
                    print("Way Too High")
                elif guess - number < 25 and guess - number > 5:
                    print("Too High")
                elif guess - number <= 5:
                    print("Barely Too High")
            if number == guess:
                print("You Got It Correct!")
                correct = True
            previous.append(guess)
            input("Press Enter To Continue")
            os.system('clear')
            print (f"Previous Guesses {previous}")
        except:
            print("Please Enter A Number")
            continue
    if 10 - len(previous) <= 0:
        print("However, You Have Taken Too Many Tries, You Receive 0 Tickets")
        return 0
    else:
        print(f"You Have Earned {10 - len(previous)} Tickets!")
    input()
    os.system('clear')
    return 10 - len(previous)
