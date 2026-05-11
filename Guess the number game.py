
# NUMBER GUESSING GAME

import random
number = random.randint(1,100)
user_input = 0

while user_input != number:
    user_input = int(input("Enter your Guess: "))

    if user_input < number:
        print("too low, guess a higher number")
    elif user_input > number:
        print ("too high, guess a lower number")
    else:
        print("Congratulations you've guessed the number")
