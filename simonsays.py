import random
import os
import time
def simon(Tickets):
    colors = ""
    answer = ""
    while colors == answer:
        os.system('clear')
        num = random.randint(1,4)
        if num == 1:
            color = "blue"
        elif num == 2:
            color = "green"
        elif num == 3:
            color = "red"
        elif num == 4:
            color = "yellow"
        colors += f" {color}"
        print(f"Welcom To Simon, Your Next Color Is {color}")
        print()
        answer = f" {input("Please Input All Previous Colors, Starting With The First: ").lower()}"
        if answer == colors:
            print()
            print("Correct")
            time.sleep(1)
    os.system('clear')
    print("Sorry That Is Incorrect")
    print(f"You Entered{answer}")
    print(f"The Correct Sequence Was{colors}")
    print()
    print(f"You Have Earned {len(colors.split()) - 1} Tickets")
    print()
    input("Press Enter To Continue")
    return len(colors.split()) - 1
