import os
import random
from pathlib import Path
import time
LEADERBOARD = Path.home() / ".cli_carnival" / "leaderboard.txt"

def retrieve(name):
    with open(LEADERBOARD, "r") as f:
        for first in f:
            if name == first.split()[0]:
                return int(first.split()[3])
                
        else:
            os.system('clear')
            print("Sorry, No Names In The Leaderboard Match The One Provided")
            print()
            input("Press Enter To Continue")