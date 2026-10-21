import os
import time
import random 

def mastermind(Tickets):
    code1 = random.randint(1, 9)
    code2 = random.randint(1, 9)
    code3 = random.randint(1, 9)
    code4 = random.randint(1, 9)
    code5 = random.randint(1, 9)
    code = str(code1) + str(code2) + str(code3) + str(code4) + str(code5)
    win = False
    attempt = 0
    while win != True and attempt < 10:
        while win != True and attempt < 10:
            guess = list(input("Please Guess A 5 Digit Combo: "))
            if len(guess) != 5:
                os.system('clear')
                print("This Game Requires Exactly 5 Digits")
                print()
                input("Press Enter To Continue")
                os.system('clear')
                break
            if all(s.isdigit() for s in guess) == False:
                os.system('clear')
                print("Please Only Enter Numbers")
                print()
                input("Press Enter To Continue")
                os.system('clear')
                break
            print(f"Attempt {attempt}/10")
            print(guess)
            check = -1
            for num in guess:
                check += 1
                if num in code:
                    if num == code[check]:
                        print("🟢", end="")
                    else:
                        print("🟡", end="")
                else:
                    print("🔴", end="")
            attempt += 1
            if "".join(guess) == code:
                win = True
    if attempt >= 10 and win != True:
        os.system('clear')
        print("Too Many Attempts, You Have Failed")
        print(f"The Correct Combination Was {code}")
        print()
        input("Press Enter To Continue")
        return 0

    if win == True:
        os.system('clear')
        print("You Gessed The Code, Congratulations, You Have Earned 8 Tickets")
        print()
        input("Press Enter To Continue")
        return (10 - attempt)



        