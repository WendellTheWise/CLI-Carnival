from hangman_word_cache import *
import random
import os
def hangman(tickets):
    wrong = 0
    rand = random.randint(1,501)
    word = list(cache[rand])
    wrong = 0
    win = False
    print(word)
    wronglet = []
    while wrong != 5 and win != True:
        while wrong !=5 and win != True:
            print(art[wrong])
            print(f"Guessed Letters {wronglet}")
            for letter in word:
                if letter.isupper():
                    print(f" {letter} ", end="")
                else:
                    print("---  ", end="")
            guess = input("Please Guess A Letter Or A Word: ").lower()
            if guess == cache[rand]:
                win = True
                print(f"You Got It Correct! You Have Earned {len(word)} Tickets")
                os.system('clear')
                return len(word)
            for let in word:
                if guess == let:
                    print(f"{guess} Is In The Word")
                    print()
                    input("Press Enter To Continue")
                    let.replace(let, let.capitalize())
                    print(word)
                    break
                else:
                    print("Sorry, That Letter Is Not In The Word")
                    wronglet.append(guess)
                    wrong += 1
hangman(0)