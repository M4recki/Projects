Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Numbers2 = ['1', '2']


def CaesarCipher(PlainText, Choice, ShiftAmount):
    CipherText = ""
    if Direction == "2":
        Alphabet.reverse()
    for Letter in PlainText:
        if Letter in Alphabet:
            Position = Alphabet.index(Letter)
            ChangedPosition = Position + ShiftAmount
            ChangedLetter = Alphabet[ChangedPosition]
            CipherText += ChangedLetter
        else:
            CipherText += Letter
    print(f"Encrypted text is: {CipherText}")


End = False
while not End:
    Direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
    if Direction not in Numbers2:
        print("Invalid input. Please try again.")
        continue
    Text = input("Type your message:\n").lower()
    Shift = int(input("Type the shift number:\n"))
    if Shift not in Numbers:
        print("Invalid input. Please try again.")
        continue
    Shift = Shift % 26

    CaesarCipher(PlainText=Text, Choice=Direction, ShiftAmount=Shift)

    Restart = input("Type 'y' if you want to go again. Otherwise type 'n'.\n")
    if Restart == "n":
        End = True
    elif Restart != "y" or Restart != 'n':
        print("Invalid input. Please try again.")
        continue
