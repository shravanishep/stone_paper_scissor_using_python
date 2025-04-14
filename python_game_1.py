"""
 input from user
 computer choice computer will choose ramdomly not conditionally
 and at last result will display on screen
 rock-rock=tie
 rock-paper=paper win
 rock scissor =rock win

 paper-paper=tie
 paper-rock=paper win
 paper-scissor=scissor win

 scissor-scissor=tie
 scissor-rock=rock win
 scissor-paper=scissor win
 """

import random
list=["rock","paper","scissor"]

choose=input("select any one from rock,paper,scissor= ")
computer=random.choice(list)
print("user choice=",choose)
print("computer choice",computer)

if choose==computer:
    print("match tie")

elif choose=="rock"and computer=="paper":
    print("computer win the match")

elif choose=="rock"and computer=="scissor":
    print("you win the match")

elif choose=="paper"and computer=="scissor":
    print("computer win the match")

elif choose=="paper"and computer=="rock":
    print("computer win the match")

elif choose=="scissor"and computer=="paper":
    print("you win the match")

elif choose=="scissor"and computer=="rock":
    print("computer win the match")