import random
import os
import time

jelly = 0
def p():
    global jelly
    if random.randint(1,3) == 3:
        jelly += 1
        return("0")
    else:
        return(" ")

def jellies(tickets): #26
    global jelly
    jelly = 0
    os.system('clear')
    print(f"""
       _______________________
      |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
     /{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}\\
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
    |{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}{p()}|
     \\-------------------------/                                               """)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Finished")
    time.sleep(1)
    os.system('clear')
    guess = int(input("Roughly How Many Jelly Beans Were In The Jar? "))
    if jelly - guess == 0:
        print(f"You Got It Correct, There Were {jelly} JellyBeans")
        input("""You Earned 12 Tickets
        
        Press Enter To Continue""")
        return 12
    if jelly - guess <= 10:
        print(f"Super Close, The Actual Number Was {jelly}")
        input("""You Have Earned 8 Tickets!!!
        
        Press Enter To Continue""")

        return 8
    if jelly - guess <= 25:
        print(f"Close, The Actual Number Was {jelly}")
        input("""You Have Earned 5 Tickets!

        Press Enter To Continue""")
        return 4
    else:
        print(f"Sorry, Thats Too Far Off, The Actual Number Was {jelly}")
        input("""You Have Earned 0 Tickets
        
        Press Enter To Continue""")
        return 0

