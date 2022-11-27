import random
from replit import clear

Cards = {"Jack": 10, "Queen": 10, "King": 10, "Ace": 11, "2": 2,
         "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

DrawedCardsByUser = []
DrawedCardsByComputer = []
MaxValue = 21


def CardDrawForUser():
    '''Draws 2 cards for the user from the deck of cards'''
    Values = list(Cards.values())
    UsersCard1 = random.choice(Values)
    UsersCard2 = random.choice(Values)
    DrawedCardsByUser.append(UsersCard1)
    DrawedCardsByUser.append(UsersCard2)
    return UsersCard1, UsersCard2

def CardDrawForComputer():
    '''Draws 2 cards for the computer from the deck of cards'''
    Values = list(Cards.values())
    ComputersCard1 = random.choice(Values)
    ComputersCard2 = random.choice(Values)
    DrawedCardsByComputer.append(ComputersCard1)
    DrawedCardsByComputer.append(ComputersCard2)
    return ComputersCard1, ComputersCard2

def NewCardForUser():
    '''Draws 1 card for the user from the deck of cards'''
    Values = list(Cards.values())
    UsersCard3 = random.choice(Values)
    DrawedCardsByUser.append(UsersCard3)
    return UsersCard3

def NewCardForComputer():
    '''Draws 1 card for the computer from the deck of cards'''
    Values = list(Cards.values())
    ComputersCard3 = random.choice(Values)
    DrawedCardsByComputer.append(ComputersCard3)
    return ComputersCard3

def Check():
    '''Checks who won'''
    if sum(DrawedCardsByUser) > MaxValue:
        print("You went over. You lose.")
        PlayAgain = input("Do you want to play a game of Blackjack? Type 'y' - yes or 'n' - no: ")
        if PlayAgain == "y":
            ClearEverything()
            Game()
        elif PlayAgain == "n":
            ClearEverything()
            quit()
        else:
            print("Invalid input. Please try again.")
            quit()
    elif sum(DrawedCardsByComputer) > MaxValue:
        print("Computer went over. You won.")
        PlayAgain = input("Do you want to play a game of Blackjack? Type 'y' - yes or 'n' - no: ")
        if PlayAgain == "y":
            ClearEverything()
            Game()
        elif PlayAgain == "n":
            ClearEverything()
            quit()
        else:
            print("Invalid input. Please try again.")
            quit()
    elif sum(DrawedCardsByUser) > sum(DrawedCardsByComputer):
        print("You won.")
        PlayAgain = input("Do you want to play a game of Blackjack? Type 'y' - yes or 'n' - no: ")
        if PlayAgain == "y":
            ClearEverything()
            Game()
        elif PlayAgain == "n":
            ClearEverything()
            quit()
        else:
            print("Invalid input. Please try again.")
            quit()
    elif sum(DrawedCardsByUser) < sum(DrawedCardsByComputer):
        print("You lost")
        PlayAgain = input("Do you want to play a game of Blackjack? Type 'y' - yes or 'n' - no: ")
        if PlayAgain == "y":
            ClearEverything()
            Game()
        elif PlayAgain == "n":
            ClearEverything()
            quit()
        else:
            print("Invalid input. Please try again.")
            quit()
    elif sum(DrawedCardsByUser) == sum(DrawedCardsByComputer):
        print("It's a draw!")
        PlayAgain = input("Do you want to play a game of Blackjack? Type 'y' - yes or 'n' - no: ")
        if PlayAgain == "y":
            ClearEverything()
            Game()
        elif PlayAgain == "n":
            ClearEverything()
            quit()
        else:
            print("Invalid input. Please try again.")
            quit()

def FinalCards():
    '''prints final user and computer cards'''
    print("Your final cards:", DrawedCardsByUser, "final score:", sum(DrawedCardsByUser))
    print()
    print("Computer's final cards:", DrawedCardsByComputer, "final score:", sum(DrawedCardsByComputer))
    print()
    Check()

def ClearEverything():
    '''Clears both terminal and lists'''
    clear()
    DrawedCardsByUser.clear()
    DrawedCardsByComputer.clear()

def Game():
    '''Main function'''
    while True:

        Start = input("Welcome to the Blackjack game. Would you like to play? 'y' - yes 'n' - no: ")
        if Start == "y":
            CardDrawForUser()
            print("Your cards:", DrawedCardsByUser, "current score:", sum(DrawedCardsByUser))
            print()
            CardDrawForComputer()
            print("Computer's 1st card:", DrawedCardsByComputer[0])
            print()

            while sum(DrawedCardsByUser) <= MaxValue or sum(DrawedCardsByComputer) <= MaxValue:
                NewCard = input("Type 'y' to get another card, type 'n' to pass: ")
                if NewCard == "y":
                    NewCardForUser()
                    NewCardForComputer()
                    print("Your cards:", DrawedCardsByUser, "current score:", sum(DrawedCardsByUser))
                    print()
                    print("Computer's 1st card:", DrawedCardsByComputer[0])
                    print()
                    if sum(DrawedCardsByUser) > MaxValue: 
                        FinalCards()
                        Check()
                    elif sum(DrawedCardsByUser) == sum(DrawedCardsByComputer):
                        FinalCards()
                        Check()
                    else:
                        continue
                elif NewCard == "n":
                    FinalCards()
                else:
                    print("Invalid input. Please try again.")
                    continue

        elif Start == "n":
            ClearEverything()
            break
        else:
            print("Invalid input. Please try again.")
            continue

Game()
