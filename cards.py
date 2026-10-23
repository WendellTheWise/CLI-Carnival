import random
cards = [
    ("Ace",  "Hearts"),
    ("Two", "Hearts"),
    ("Three", "Hearts"),
    ("Four", "Hearts"),
    ("Five", "Hearts"),
    ("Six", "Hearts"),
    ("Seven", "Hearts"),
    ("Eight", "Hearts"),
    ("Nine", "Hearts"),
    ("Ten", "Hearts"),
    ("Jack", "Hearts"),
    ("Queen", "Hearts"),
    ("King", "Hearts"),

    ("Ace", "Spades"),
    ("Two", "Spades"),
    ("Three", "Spades"),
    ("Four", "Spades"),
    ("Five", "Spades"),
    ("Six", "Spades"),
    ("Seven", "Spades"),
    ("Eight", "Spades"),
    ("Nine", "Spades"),
    ("Ten", "Spades"),
    ("Jack", "Spades"),
    ("Queen", "Spades"),
    ("King", "Spades"),

    ("Ace", "Clubs"),
    ("Two", "Clubs"),
    ("Three", "Clubs"),
    ("Four", "Clubs"),
    ("Five", "Clubs"),
    ("Six", "Clubs"),
    ("Seven", "Clubs"),
    ("Eight", "Clubs"),
    ("Nine", "Clubs"),
    ("Ten", "Clubs"),
    ("Jack", "Clubs"),
    ("Queen", "Clubs"),
    ("King", "Clubs"),

    ("Ace", "Diamonds"),
    ("Two", "Diamonds"),
    ("Three", "Diamonds"),
    ("Four", "Diamonds"),
    ("Five", "Diamonds"),
    ("Six", "Diamonds"),
    ("Seven", "Diamonds"),
    ("Eight", "Diamonds"),
    ("Nine", "Diamonds"),
    ("Ten", "Diamonds"),
    ("Jack", "Diamonds"),
    ("Queen", "Diamonds"),
    ("King", "Diamonds")
]
ranks = [
    ("Ace",  "Hearts"),
    ("Two", "Hearts"),
    ("Three", "Hearts"),
    ("Four", "Hearts"),
    ("Five", "Hearts"),
    ("Six", "Hearts"),
    ("Seven", "Hearts"),
    ("Eight", "Hearts"),
    ("Nine", "Hearts"),
    ("Ten", "Hearts"),
    ("Jack", "Hearts"),
    ("Queen", "Hearts"),
    ("King", "Hearts"),]

suits = [
    "Diamonds",
    "Clubs",
    "Spades",
    "Hearts"
]
cardart = [
    # Spades
    " +---------+\n |A        |\n |         |\n |    S    |\n |         |\n |        A|\n +---------+",
    " +---------+\n |2        |\n |         |\n |    S    |\n |         |\n |        2|\n +---------+",
    " +---------+\n |3        |\n |         |\n |    S    |\n |         |\n |        3|\n +---------+",
    " +---------+\n |4        |\n |         |\n |    S    |\n |         |\n |        4|\n +---------+",
    " +---------+\n |5        |\n |         |\n |    S    |\n |         |\n |        5|\n +---------+",
    " +---------+\n |6        |\n |         |\n |    S    |\n |         |\n |        6|\n +---------+",
    " +---------+\n |7        |\n |         |\n |    S    |\n |         |\n |        7|\n +---------+",
    " +---------+\n |8        |\n |         |\n |    S    |\n |         |\n |        8|\n +---------+",
    " +---------+\n |9        |\n |         |\n |    S    |\n |         |\n |        9|\n +---------+",
    " +---------+\n |10       |\n |         |\n |    S    |\n |         |\n |       10|\n +---------+",
    " +---------+\n |J        |\n |         |\n |    S    |\n |         |\n |        J|\n +---------+",
    " +---------+\n |Q        |\n |         |\n |    S    |\n |         |\n |        Q|\n +---------+",
    " +---------+\n |K        |\n |         |\n |    S    |\n |         |\n |        K|\n +---------+",

    # Hearts
    " +---------+\n |A        |\n |         |\n |    H    |\n |         |\n |        A|\n +---------+",
    " +---------+\n |2        |\n |         |\n |    H    |\n |         |\n |        2|\n +---------+",
    " +---------+\n |3        |\n |         |\n |    H    |\n |         |\n |        3|\n +---------+",
    " +---------+\n |4        |\n |         |\n |    H    |\n |         |\n |        4|\n +---------+",
    " +---------+\n |5        |\n |         |\n |    H    |\n |         |\n |        5|\n +---------+",
    " +---------+\n |6        |\n |         |\n |    H    |\n |         |\n |        6|\n +---------+",
    " +---------+\n |7        |\n |         |\n |    H    |\n |         |\n |        7|\n +---------+",
    " +---------+\n |8        |\n |         |\n |    H    |\n |         |\n |        8|\n +---------+",
    " +---------+\n |9        |\n |         |\n |    H    |\n |         |\n |        9|\n +---------+",
    " +---------+\n |10       |\n |         |\n |    H    |\n |         |\n |       10|\n +---------+",
    " +---------+\n |J        |\n |         |\n |    H    |\n |         |\n |        J|\n +---------+",
    " +---------+\n |Q        |\n |         |\n |    H    |\n |         |\n |        Q|\n +---------+",
    " +---------+\n |K        |\n |         |\n |    H    |\n |         |\n |        K|\n +---------+",

    # Diamonds
    " +---------+\n |A        |\n |         |\n |    D    |\n |         |\n |        A|\n +---------+",
    " +---------+\n |2        |\n |         |\n |    D    |\n |         |\n |        2|\n +---------+",
    " +---------+\n |3        |\n |         |\n |    D    |\n |         |\n |        3|\n +---------+",
    " +---------+\n |4        |\n |         |\n |    D    |\n |         |\n |        4|\n +---------+",
    " +---------+\n |5        |\n |         |\n |    D    |\n |         |\n |        5|\n +---------+",
    " +---------+\n |6        |\n |         |\n |    D    |\n |         |\n |        6|\n +---------+",
    " +---------+\n |7        |\n |         |\n |    D    |\n |         |\n |        7|\n +---------+",
    " +---------+\n |8        |\n |         |\n |    D    |\n |         |\n |        8|\n +---------+",
    " +---------+\n |9        |\n |         |\n |    D    |\n |         |\n |        9|\n +---------+",
    " +---------+\n |10       |\n |         |\n |    D    |\n |         |\n |       10|\n +---------+",
    " +---------+\n |J        |\n |         |\n |    D    |\n |         |\n |        J|\n +---------+",
    " +---------+\n |Q        |\n |         |\n |    D    |\n |         |\n |        Q|\n +---------+",
    " +---------+\n |K        |\n |         |\n |    D    |\n |         |\n |        K|\n +---------+",

    # Clubs
    " +---------+\n |A        |\n |         |\n |    C    |\n |         |\n |        A|\n +---------+",
    " +---------+\n |2        |\n |         |\n |    C    |\n |         |\n |        2|\n +---------+",
    " +---------+\n |3        |\n |         |\n |    C    |\n |         |\n |        3|\n +---------+",
    " +---------+\n |4        |\n |         |\n |    C    |\n |         |\n |        4|\n +---------+",
    " +---------+\n |5        |\n |         |\n |    C    |\n |         |\n |        5|\n +---------+",
    " +---------+\n |6        |\n |         |\n |    C    |\n |         |\n |        6|\n +---------+",
    " +---------+\n |7        |\n |         |\n |    C    |\n |         |\n |        7|\n +---------+",
    " +---------+\n |8        |\n |         |\n |    C    |\n |         |\n |        8|\n +---------+",
    " +---------+\n |9        |\n |         |\n |    C    |\n |         |\n |        9|\n +---------+",
    " +---------+\n |10       |\n |         |\n |    C    |\n |         |\n |       10|\n +---------+",
    " +---------+\n |J        |\n |         |\n |    C    |\n |         |\n |        J|\n +---------+",
    " +---------+\n |Q        |\n |         |\n |    C    |\n |         |\n |        Q|\n +---------+",
    " +---------+\n |K        |\n |         |\n |    C    |\n |         |\n |        K|\n +---------+",
]
def pullcard():
    cardlist = cards.copy()
    random.shuffle(cardlist)
    art = 0
    if cardlist[0][1] == "Spades":
        art += 0
    elif cardlist[0][1] == "Hearts":
        art += 13
    elif cardlist[0][1] == "Diamonds":
        art += 26
    elif cardlist[0][1] == "Clubs":
        art += 39
    if cardlist[0][0] == "Ace":
        art += 0
    if cardlist[0][0] == "Two":
        art += 1
    if cardlist[0][0] == "Three":
        art += 2
    if cardlist[0][0] == "Four":
        art += 3
    if cardlist[0][0] == "Five":
        art += 4
    if cardlist[0][0] == "Six":
        art += 5
    if cardlist[0][0] == "Seven":
        art += 6
    if cardlist[0][0] == "Eight":
        art += 7
    if cardlist[0][0] == "Nine":
        art += 8
    if cardlist[0][0] == "Ten":
        art += 9
    if cardlist[0][0] == "Jack":
        art += 10
    if cardlist[0][0] == "Queen":
        art += 11
    if cardlist[0][0] == "King":
        art += 12
    return[cardart[art], cardlist[0]]