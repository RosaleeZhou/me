# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import random

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    print("It's a guess game!")
    print("Ok I'll find the number between {low} and {high} for you".format(low=low,high=high))


    low = 0
    high = high - 1
    guess = random.randict(low,high)

    while guess != actual_number:
        mid = (low + high) // 2
       
        if guess < mid:
            low = mid + 1
            print("Guessed {}, not the one".format(guess))
            tries = tries + 1
        elif guess > mid:
            high = mid - 1
            print("Guessed {}, not the one".format(guess))
            tries = tries + 1
    else:
        print("Got it, it was {}. ".format(actual_number))
        tries = str(tries)

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
