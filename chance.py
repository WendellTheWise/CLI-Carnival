import time
import os
import random
def chance(tickets):
    os.system('clear')
    timer = 0
    timeing = 0.001
    good = False
    while good == False:
        good = True
        wager = int(input("How Many Tickets Are You Wagering? "))
        if wager > tickets:
            print(" You Cannot Wager More Tickets Than You Have")
            good = False
            print()
            input("Press Enter To Continue")
            os.system('clear')
    rand = random.randint((-wager),(2 * wager))
    problem = random.randint(0,2)
    while timer < 75:
        print(f"""
            ---
        /{rand +1 }\\
        |{rand}|   
        \{rand - 1}/
            ---""")
        print(timeing)
        print(timer)
        rand += 1
        time.sleep(0.00 + timeing)
        os.system('clear')
        timeing *= 1.1
        timer += 1
        if rand > (2 * wager):
            rand = (-wager)
    if rand <= 0:
        print(f"******:( {rand} ):******")
        print("Better Luck Next Time")
        print()
        input("Press Enter To Continue")
    else:
        print(f"!!!!!!!!!!{rand}!!!!!!!!!")
        print("WINNER WINNER WINNER")
        print()
        input("Press Enter To Continue")
    return rand