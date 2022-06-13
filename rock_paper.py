from random import choice

lit = ["R", "P", "S"]
list2 = ["Rock", "Paper", "Scissors"]
while True:
    while True:
        computer = str(choice(lit))
        player = input("Enter R for Rock, S for Scissors, P for Paper: ")
        if player in lit:
            break
        else:
            print("You entered wrong input!!!\n")
    print("Player({}) : CPU({})" .format(list2[lit.index(player)], list2[lit.index(computer)]))
    if computer != player:
        break
    print("Tie")

if computer == 'R':
    if player == 'P':
        print("Player wins \nComputer loses!!!")
    if player == 'S':
        print("Computer wins \nPlayer loses!!!")
if computer == 'S':
    if player == 'P':
        print("Computer wins \nPlayer loses!!!")
    if player == 'R':
        print("Player wins \nComputer loses!!!")
if computer == 'P':
    if player == 'R':
        print("Computer wins \nPlayer loses!!!")
    if player == 'S':
        print("Player wins \nComputer loses!!!")
