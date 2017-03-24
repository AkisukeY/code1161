# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""
from __future__ import division
from __future__ import print_function
# import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
      """

    count = 0
    cases = 0
    scenario = 10
    lower = low
    higher = high
    while scenario >= 2:
        scenario = (higher - lower)/2
        higher = scenario
        cases += 1

    guessed = False
    lower = low
    higher = high
    while guessed is False:
        count += 1
        guess = int((lower + higher)/2)
        print("guess: {}".format(guess))
        if guess == actual_number:
            guessed = True
        elif guess > actual_number:
            if count == cases:
                guess -= 1
                guessed = True
            higher = guess
        elif guess < actual_number:
            if count == cases:
                guess += 1
                guessed = True
            lower = guess
    # if count > cases:
    #    count = cases
    return {'guess': guess, 'tries': count}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
