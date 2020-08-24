import random

i=1
T=1
a=0
b=0

while i<4:

    # player
    print()
    print("TURN ",T)
    print("*** Player Turn ***")
    print("** r for ROCK ** p for PAPER ** s for SCISSOR **")
    print()
    player_option=input("enter an option: ")
    if player_option== 'r':
        p = ("ROCK")
        print(p)
    elif player_option== 'p':
        p = ("PAPER")
        print(p)
    else:
        p = ("SCISSOR")
        print(p)

    # computer
    print()
    print("*** Computer Turn ***")
    options = ["ROCK", "PAPER", "SCISSOR"]
    c = random.choice(options)
    print(c)
    print()
    T=T+1

    #Who Wins

    if ((p=="ROCK" and c=="PAPER") or (p=="PAPER" and c== "ROCK")):
        win = "PAPER"
    elif ((p=="ROCK" and c=="SCISSOR") or (p=="SCISSOR" and c== "ROCK")):
        win = "ROCK"
    elif ((p=="PAPER" and c=="SCISSOR") or (p=="SCISSOR" and c== "PAPER")):
        win = "SCISSOR"
    else:
        win = "Tie"

    if win == p:
        a=a+1
    elif win == c:
        b=b+1
    else:
        pass
    i=i+1


if a>b:
    print("*** PLAYER WINS ***")
elif b>a:
    print("*** COMPUTER WINS ***")
elif a==b:
    print("*** MATCH IS TIE ***")
