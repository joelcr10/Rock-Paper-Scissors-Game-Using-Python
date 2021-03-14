#!/usr/bin/env python 3
import random
from playsound import playsound

def checking(user, comp):
    if user=="Rock":
        if comp=="Rock":
            Result="draw"
        elif comp=="Paper":
            Result="lose"
        elif comp=="Scissors":
            Result="win"
    elif user=="Paper":
        if comp=="Rock":
            Result="win"
        elif comp=="Paper":
            Result="draw"
        elif comp=="Scissors":
            Result="lose"
    elif user=="Scissors":
        if comp=="Rock":
            Result="lose"
        elif comp=="Paper":
            Result="win"
        elif comp=="Scissors":
            Result="draw"
        
    
    if Result=="win":
        return 1
    elif Result=="lose":
        return 0
    else:
        return -1



rounds = int(input("Enter the Number of rounds:"))
user_points=0
user_points=int(user_points)
comp_points=0
comp_points=int(comp_points)

victory_sound=""

while(rounds):
    RPS = ["Rock","Paper","Scissors"]

    comp = random.choice(RPS)


    print("\n1. Rock \n2. Paper \n3. Scissors")
    option = int(input("choose:"))

    if option==1:
        user = "Rock"
    elif option==2:
        user = "Paper"
    elif option==3:
        user = "Scissors"
    else:
        print("Invalid")

    print("\nUser: "+user+"  Computer: "+comp)
    points=checking(user,comp)
    points=int(points)

    if points==1:
        user_points=user_points+1
        print("WON")
    elif points==0:
        comp_points=comp_points+1
        print('LOST')
    else:
        print("DRAW")

    rounds=rounds-1

print('\nFinal points:')
print("User= ",user_points,"  Computer= ",comp_points)
if user_points>comp_points:
    print(" -------------")
    print('|YOU HAVE WON|')
    print(' -------------')
elif user_points<comp_points:
    print(' --------')
    print("|YOU LOST|")
    print('----------')
else:
    print("it's a draw")
