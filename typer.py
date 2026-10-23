from datetime import datetime
import os
import time
import random

phrases = [
    "hello world",
    "a bright sunny day",
    "the early bird catches the worm",
    "practice makes perfect",
    "a stitch in time saves nine",
    "the cat sat on the windowsill",
    "actions speak louder than words",
    "better late than never",
    "a walk in the park",
    "the grass is always greener on the other side",
    "break the ice",
    "a piece of cake",
    "once in a blue moon",
    "the quick brown fox jumps over the lazy dog",
    "every cloud has a silver lining",
    "the calm before the storm",
    "birds of a feather flock together",
    "when it rains it pours",
    "a blessing in disguise",
    "the best of both worlds",
    "burning the midnight oil",
    "the ball is in your court",
    "a penny for your thoughts",
    "curiosity killed the cat",
    "the apple does not fall far from the tree",
    "don't count your chickens before they hatch",
    "two heads are better than one",
    "where there's a will there's a way",
    "the elephant in the room",
    "a watched pot never boils",
    "easy come easy go",
    "fortune favors the bold",
    "out of sight out of mind",
    "let sleeping dogs lie",
    "the last straw",
    "a storm in a teacup",
    "bite off more than you can chew",
    "burning bridges",
    "hit the nail on the head",
    "spill the beans",
    "the writing is on the wall",
    "a wild goose chase",
    "through thick and thin",
    "every dog has its day",
    "the whole nine yards",
    "a wolf in sheep's clothing",
    "cutting corners leads to trouble",
    "the road less traveled",
    "time flies when you're having fun",
    "silence speaks volumes",
    "the world is your oyster",
    "a leopard cannot change its spots",
    "don't put all your eggs in one basket",
    "the squeaky wheel gets the grease",
    "still waters run deep",
    "you reap what you sow",
    "a rolling stone gathers no moss",
    "the proof is in the pudding",
    "look before you leap",
    "all that glitters is not gold",
    "the devil is in the details",
    "keep your friends close and your enemies closer",
    "the darkest hour is just before dawn",
    "there is no smoke without fire",
    "a journey of a thousand miles begins with a single step",
    "the pen is mightier than the sword",
    "don't judge a book by its cover",
    "every rose has its thorn",
    "necessity is the mother of invention",
    "you cannot make an omelet without breaking eggs",
    "the bigger they are the harder they fall",
    "a chain is only as strong as its weakest link",
    "all roads lead to Rome",
    "don't bite the hand that feeds you",
    "a bird in the hand is worth two in the bush",
    "the exception proves the rule",
    "hope for the best and prepare for the worst",
    "make hay while the sun shines",
    "you can't have your cake and eat it too",
    "one man's trash is another man's treasure",
    "the road to hell is paved with good intentions",
    "good things come to those who wait",
    "two wrongs don't make a right",
    "the grass grows greener where you water it",
    "fortune favors those who dare",
    "a little knowledge is a dangerous thing",
    "the customer is always right",
    "discretion is the better part of valor",
    "blood is thicker than water",
    "the calm sea never made a skilled sailor",
    "a fool and his money are soon parted",
    "every beginning has an end",
    "the truth will always find its way to the surface",
    "the stars shine brightest in the darkest skies",
    "even the smallest candle can light a dark room",
    "the strongest trees grow in the harshest winds",
    "patience is bitter but its fruit is sweet",
    "the world belongs to those who dare to dream",
    "great oaks from little acorns grow",
    "even a broken clock is right twice a day",
    "the longest journey begins beneath your feet"
]

def typing(Tickets):
    picked = phrases[random.randint(1,100)]
    old = time.perf_counter()
    correct = False
    os.system('clear')
    while correct == False:
        correct = True
        print(picked)
        entry = input("""Please Type The Presented Phrase
        
        """)
        if entry.lower() != picked:
            os.system('clear')
            print("Please Try Again. 1 Second Penaly")
            time.sleep(1)
            correct = False
            os.system('clear')
        new = time.perf_counter()
    print(f"It Took You {(new - old) // 1} Seconds")
    print()
    input(f"""You Have Earned {(12 - (new - old)) // 1} Tickets""")
    return (12 - (new - old)) // 1
