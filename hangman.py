from hangman_word_cache import *
import random
import os
def hangman(tickets):
    wrong = 0
    rand = random.randint(1,501)
    word = list(cache[rand])
    wrong = 0
    win = False
    wronglet = []
    while wrong != 6 and win != True:
        while wrong !=6 and win != True:
            os.system('clear')
            print(art[wrong])
            print(word)
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
                print()
                input("Press Enter To Continue")
                os.system('clear')
                return len(word)
            for let in word:
                if guess == let:
                    print(f"{guess} Is In The Word")
                    for i in range(len(word)):
                        if word[i] == guess:
                            word[i] = guess.upper()
                    if all(letter.isupper() for letter in word):
                        win = True
                        os.system('clear')
                        print(f""" {art[wrong]}
                        The Word Was {word}
                        You Have Received {len(word)}
                        """
                        )
                        input("Press Enter To Continue")
                        os.system('clear')
                        return len(word)
                    print()
                    input("Press Enter To Continue")
                    print()
                    break

            else:
                print("Sorry, That Letter Is Not In The Word")
                wronglet.append(guess)
                wrong += 1
                print()
                input('Press Enter To Continue')
        break
                
    if wrong >= 5:
        print("Better Luck Next Time")
        print()
        input("Press Enter To Continue"
        )
        return 0
    else:
        print(f"You Got The Word Correct, You Have Received {len(word)} Tickets")
        print()
        input("Press Enter To Continue")
        return len(word)
