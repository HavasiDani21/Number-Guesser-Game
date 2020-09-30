#  This is a number guesser app
import random

print("NUMBER GUESSER")

number = random.randrange(1000)
guess = int(input("Guess a number: "))

while guess != number:
    print("Guess again")
    hint = input("do you need hint? y/n\n")

    if hint == "y":
        hint_type = int(input("What type of hint do you want?\n"
                              " 1: Larger or Smaller  \n 2: Odd or even \n 3: Divisibility\n"))
        if hint_type == 1:
            if number > guess:
                print("The thought number is larger than your guess.")
            if number < guess:
                print("The thought number is smaller than your guess.")
        elif hint_type == 2:
            if number % 2 == 0:
                print("The thought number is even.")
            else:
                print("The thought number is odd.")
        elif hint_type == 3:
            if number % 2 == 0:
                print("The thought number is multiple of 2.")
            if number % 3 == 0:
                print("The thought number is multiple of 3.")
            if number % 5 == 0:
                print("The thought number is multiple of 5.")
            if number % 10 == 0:
                print("The thought number is multiple of 10.")
            else:
                print("The thought number is prime.")
    guess = int(input("Guess a number: "))

if guess == number:
    print("You got it!")
