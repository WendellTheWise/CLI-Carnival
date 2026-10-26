import os
import time
import random

dice = [""" 
  ┌───────┐
  │       │
  │   ●   │
  │       │
  └───────┘""",
"""
  ┌───────┐
  │ ●     │
  │       │
  │     ● │
  └───────┘""",
  """  
  ┌───────┐
  │ ●     │
  │   ●   │
  │     ● │
  └───────┘""",
  """
  ┌───────┐
  │ ●   ● │
  │       │
  │ ●   ● │
  └───────┘""",
  """  
  ┌───────┐
  │ ●   ● │
  │   ●   │
  │ ●   ● │
  └───────┘""",
  """  
  ┌───────┐
  │ ●   ● │
  │ ●   ● │
  │ ●   ● │
  └───────┘"""
]

def roll(tickets):
    os.system('clear')
    wager = False
    while wager == False:
        wager = True
        try:
            wagered = int(input("Please Enter A Wager: "))
            if wagered > tickets:
                os.system('clear')
                print("Wager Is Too High, Please Try Again")
                print()
                input("Press Enter To Continue")
                os.system('clear')
                wager = False
            if wagered <= 0:
                os.system('clear')
                print("Wager Cannot Be A Negative Number Or 0")
                print()
                input("Press Enter To Continue")
                os.system('clear')
                wager = False
        except ValueError:
            os.system('clear')
            print("Please Enter A Valid Number")
            print()
            input("Press Enter To Continue")
            os.system('clear')
            wager = False
    os.system('clear')
    print(f"Your Wager Was {wagered}")
    wager = False
    while wager == False:
        wager = True
        print()
        try:
            number = int(input("Please Pick A Number: "))
            if (number) > 6:
                raise ValueError
        except ValueError:
            ("Please Enter A Valid Number Between 1 And 6")
            wager = False
            os.system('clear')
            print(f"Your Wager Was {wagered}")
    os.system('clear')
    print(f"""Your Wager Was {wagered}
    Your Selected Number Was {number}""")
    print()
    input("Please Press Enter To Roll The Dice")
    count = 0
    times = 0
    rolled = []
    while times < 4:
        while count <= 0.1:
            rand = random.randint(0, 5)
            die = dice[rand]
            print(f"{die}")
            time.sleep(0 + count)
            count += 0.005
            if count < 0.1:
                os.system('clear')
        rolled.append(rand + 1)
        times += 1
        time.sleep(1)
        count = 0
    print(f"You Rolled {rolled}")
    print(f"You Guessed {number}")
    check = 0
    ticket_count = 0
    for num in rolled:
        if num == number:
            ticket_count += 1
    print(f"You Got {ticket_count} Correct")
    print(f"You Have Received {ticket_count * 5} Tickets")
    return (tickets - wagered) + (ticket_count * 5)
