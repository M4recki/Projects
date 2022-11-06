import random
from Words import words

HangmanStages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Objects
RandomWord = random.choice(words)
Lives = 7

#Lists
GuessedLetters = []
WrongGuessedLetters = []

#Replacing '_' in the word
Display = []
WordLenght = len(RandomWord)
for Letter in range(WordLenght):
    Display += "_"

print("Welcome to my Hangman game! \n")
while Lives > 0:
    UserGuess = input("Guess a letter: ").lower()

    #Rules
    if len(UserGuess) > 1:
        print("\n\
            You can only enter 1 letter!")
        continue

    elif not UserGuess.isalpha():
        print("\n\
            You can only enter letters!")
        continue

    elif UserGuess in GuessedLetters:
        print("You already guessed this letter!")
        continue

    elif UserGuess in WrongGuessedLetters:
        print("You already guessed this letter!")
        continue
    
    for Position in range(WordLenght):
        Letter = RandomWord[Position]

        #Replacing letters with the sign: "_"
        if Letter == UserGuess:
            Display[Position] = Letter
            GuessedLetters.append(UserGuess)

    #Wrong letter
    if UserGuess not in RandomWord:
        print(f"\n\
            You found wrong letter! \n")
        WrongGuessedLetters.append(UserGuess)
        Lives -= 1
        print(f"Lives remaining: {Lives}")
        print(HangmanStages[Lives])

    print(Display)
    print()

    #Wow
    if Letter in GuessedLetters:
        print("Congratulasions you guessed word!")
        break
#Lost
if Lives == 0:
    print(f"You lost! The word was: {RandomWord}")