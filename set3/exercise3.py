"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between _ and 20 ?")
    while True:
      try:
        lowerBound = int(input("Enter a lower bound: "))
      except ValueError as e:
        print("Hey mate, a pure digital number is better for me to understand ")
        continue
      if lowerBound > 20:
        print("Hey mate, {} is bigger than 20".format(lowerBound))
      else:
        print("OK then, a number between {low} and 20 ?".format(low=lowerBound))
        break

    lowerBound = int(lowerBound)
    actural_number = random.randint(lowerBound, 20)

    while True:
      try:
        guess = int(input("Let's try it: "))
      except ValueError as e:
        print("Hey mate, please give me a pure digital number:")
        continue
      if guess < int(lowerBound):
        print("Hey mate, TOO SMALl ")
      if guess > 20:
        print("Hey mate, you go too wild!:")
      if guess > actural_number:
        print("Too big, try again: ")
      elif guess < actural_number:
        print("Too small, try again: ")
      else:
       break
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
