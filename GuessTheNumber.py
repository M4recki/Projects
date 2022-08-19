import random
guess=int(input("Guess the number between 0 and 100: "))
print()
rnd_num = random.randint(0,100)
while guess != rnd_num:
    if (guess < rnd_num):
        print("Your number is higher than a mystery number. Try again!")
        print()
        guess=int(input("Guess the number between 0 and 100: "))
        print()
    elif (guess > rnd_num):
        print("Your number is smaller than a mystery number. Try again!")
        print()
        guess=int(input("Guess the number between 0 and 100: "))
        print()
else:
    print()
    print("You guessed the correct number! Congrats!")
    
     