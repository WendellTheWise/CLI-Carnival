import random
import os
from Carnival.word_cache import *

def anagram(Tickets):
    os.system('clear')
    answer = list(cache[random.randint(1, len(cache))])
    scramble = answer.copy()
    random.shuffle(scramble)
    answer = ''.join(answer)
    scramble = ''.join(scramble)
    print(f"Your Anagram Is {scramble}")
    guess = input("What Do You Think The Correct Word Is? ").lower()
    if guess == answer:
        print()
        print(f"You Got It Right, You Have Received {len(answer)} Tickets")
        print()
        input("Press Enter To Continue")
        return len(list(answer))
    else:
        print("Sorry, That Is Incorrect")
        print()
        print(f"The Correct Answer Was {answer}"
        )
        print()
        input("Press Enter To Continue")
        return 0