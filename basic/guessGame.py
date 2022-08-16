import random

for i in range(1,10):
    guessNumber=int(input("Enter your guess number 1-10:"))
    randomNumber=random.randint(1,10)
    if guessNumber==randomNumber:
        print("You have Win")

    else:
        print("You Have Lost! Try Again")
        print("Random Number:",randomNumber)