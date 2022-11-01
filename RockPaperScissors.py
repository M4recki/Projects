from enum import IntEnum
from random import randint

Possibillities1 = IntEnum("Rock Paper Scissors", ("Rock", "Paper", "Scissors"))
Possibillities2 = IntEnum("Play again ", ("Yes", "No"))

def Score():
    global UserScore
    global ComputerScore
    if result == "win":
        UserScore += 1
    elif result == "lost":
        ComputerScore += 1
    else:
        ComputerScore += 1
        UserScore += 1

Computer = randint(1, 3)
game = 1
UserScore = 0
ComputerScore = 0


while True:
    print("--------------------------------------------------------------------")
    print("Game: ", game, )
    print("--------------------------------------------------------------------")
    print("User score: ", UserScore, "Computer score: ", ComputerScore)
    print("--------------------------------------------------------------------")
    UserChoice = int(input("What do you choose?: Rock - 1 Paper - 2 Scissors - 3 \n"))
    print("--------------------------------------------------------------------")

    if UserChoice == Possibillities1.Rock:

        if Computer == 1:
            print("You chose the Rock, but Computer also chose the Rock. It's a tie!")
            result = "tie"

        elif Computer == 2:
            print("You chose the Rock, but Computer  chose the Paper. You lost.")
            result = "lost"

        elif Computer == 3:
            print("You chose the Rock, but Computer chose Scissors. You won!")
            result = "win"

    elif UserChoice == Possibillities1.Paper:

        if Computer == 1:
            print("You chose the Paper, but Computer chose the Rock. You won!")
            result = "win"

        elif Computer == 2:
            print("You chose the Paper, but Computer also chose the Paper. It's a tie!")
            result = "tie"

        elif Computer == 3:
            print("You chose the Paper, but Computer chose Scissors. You lost.")
            result = "lost"

    elif UserChoice == Possibillities1.Scissors:

        if Computer == 1:
            print("You chose Scissors, but Computer chose the Rock. You lost.")
            result = "lost"

        elif Computer == 2:
            print("You chose Scissors, but Computer chose the Paper. You won!")
            result = "win"

        elif Computer == 3:
            print("You chose Scissors, but Computer also chose Scissors. It's a tie!")
            result = "tie"

    else:
        print("Invalid input. Please try again.")
        continue

    print("--------------------------------------------------------------------")
    PlayAgain = int(input("Would you like to play again?: 1 - yes 2 - no \n"))

    if PlayAgain == Possibillities2.Yes:
        game += 1
        Score()
        continue

    elif PlayAgain == Possibillities2.No:
        break

    else:
        print("Invalid input. Please try again.")
        continue
